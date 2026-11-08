"""MkDocs hook: combine all pages of the navigation into one document.

Why: one of the experts wants the whole thesis documentation as a single
file (Markdown or PDF). This hook builds that file from the same sources as
the website, so it never drifts from the online version.

What it produces on every build:
    gesamtdokument.md (virtual page)   rendered at /gesamtdokument/, hidden
                                       from nav and search; the CI workflow
                                       prints it to PDF (scripts/build_pdf.py)
    downloads/<NAME>.md                the combined Markdown for download

How the pages are merged:
    - Order and grouping follow `nav` in mkdocs.yml. Nav sections become
      headings, page headings are shifted below them.
    - Links between pages become jump links inside the document. A link to a
      heading keeps its anchor when that heading is unique in the document,
      otherwise it points to the start of the target page.
    - Links to files that are not pages become absolute URLs (site_url).
    - Footnote labels get a per-page prefix so they cannot collide.
    - Content between <!-- export:skip --> and <!-- /export:skip --> is left
      out (e.g. the download buttons themselves).
"""

from __future__ import annotations

import datetime as dt
import os
import posixpath
import re

from markdown.extensions.toc import slugify
from mkdocs.structure.files import File

NAME = "rdg-semesterarbeit-gesamtdokument"
PAGE_URI = "gesamtdokument.md"
DOWNLOAD_URI = f"downloads/{NAME}.md"
TITLE = "Gesamtdokument"

FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})(\s+.*)$")
LINK = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
FOOTNOTE = re.compile(r"\[\^([^\]\s]+)\]")
SKIP = re.compile(r"<!--\s*export:skip\s*-->.*?<!--\s*/export:skip\s*-->\n?", re.S)
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)

_combined = ""


# --- helpers -----------------------------------------------------------------

def _walk(nav, depth=1):
    """Yield ("section", title, level) and ("page", path, level) in nav order.
    A section whose first entry is an untitled page (section index) uses that
    page as its heading instead of an extra section heading."""
    for item in nav:
        if isinstance(item, str):
            yield ("page", item, depth)
            continue
        if not isinstance(item, dict):
            continue
        for title, value in item.items():
            if isinstance(value, str):
                if not EXTERNAL.match(value):
                    yield ("page", value, depth)
            elif isinstance(value, list):
                children = list(value)
                if children and isinstance(children[0], str):
                    yield ("page", children.pop(0), depth)
                else:
                    yield ("section", title, depth)
                yield from _walk(children, depth + 1)


def _anchor(path: str) -> str:
    stem = path[:-3] if path.endswith(".md") else path
    if stem == "index":
        return "doc-start"
    if stem.endswith("/index"):
        stem = stem[: -len("/index")]
    return "doc-" + re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def _outside_code(line: str, fn) -> str:
    """Apply fn only to the parts of a line that are not inline code."""
    parts = re.split(r"(`+[^`]*`+)", line)
    return "".join(p if i % 2 else fn(p) for i, p in enumerate(parts))


def _split_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def _shift_and_collect(text: str, shift: int, headings: list) -> str:
    out, fence = [], None
    for line in text.split("\n"):
        m = FENCE.match(line)
        if m:
            mark = m.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            out.append(line)
            continue
        h = HEADING.match(line) if fence is None else None
        if h:
            level = min(6, len(h.group(1)) + shift)
            line = "#" * level + h.group(2)
            text_only = re.sub(r"\s*\{[^}]*\}\s*$", "", h.group(2)).strip()
            headings.append(slugify(text_only, "-"))
        out.append(line)
    return "\n".join(out)


def _map_lines(text: str, fn) -> str:
    out, fence = [], None
    for line in text.split("\n"):
        m = FENCE.match(line)
        if m:
            mark = m.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            out.append(line)
            continue
        out.append(line if fence else _outside_code(line, fn))
    return "\n".join(out)


# --- build -------------------------------------------------------------------

def _combine(config, files) -> str:
    entries = list(_walk(config.nav or []))
    pages = [e[1] for e in entries if e[0] == "page"]
    site_url = (config.site_url or "").rstrip("/") + "/"

    # pass 1: read, strip, shift headings, collect slugs
    bodies = {}
    all_slugs = [slugify(f"{config.site_name}: {TITLE}", "-"), "inhalt"]
    for kind, value, level in entries:
        if kind != "page":
            all_slugs.append(slugify(value, "-"))
            continue
        f = files.get_file_from_path(value)
        if f is None:
            continue
        text = SKIP.sub("", _split_frontmatter(f.content_string))
        bodies[value] = _shift_and_collect(text.strip("\n"), level - 1, all_slugs)
    unique = {s for s in all_slugs if all_slugs.count(s) == 1}

    # pass 2: rewrite links and footnotes per page
    def rewrite(page_path, index):
        base = posixpath.dirname(page_path)

        def link(m):
            target = m.group(2)
            if EXTERNAL.match(target):
                return m.group(0)
            path, _, frag = target.partition("#")
            if not path:  # same page anchor
                new = f"#{frag}" if frag in unique else f"#{_anchor(page_path)}"
                return m.group(1) + new + m.group(3)
            resolved = posixpath.normpath(posixpath.join(base, path))
            if resolved.endswith("/") or not posixpath.splitext(resolved)[1]:
                resolved = posixpath.join(resolved, "index.md")
            if resolved in bodies:
                new = f"#{frag}" if frag and frag in unique else f"#{_anchor(resolved)}"
            else:
                new = site_url + resolved + (f"#{frag}" if frag else "")
            return m.group(1) + new + m.group(3)

        def line_fn(s):
            s = LINK.sub(link, s)
            return FOOTNOTE.sub(lambda m: f"[^p{index}-{m.group(1)}]", s)

        return line_fn

    toc, parts = [], []
    for kind, value, level in entries:
        indent = "    " * (level - 1)
        if kind == "section":
            parts.append("#" * min(6, level) + f" {value}")
            toc.append(f"{indent}- {value}")
            continue
        if value not in bodies:
            continue
        idx = pages.index(value) + 1
        body = _map_lines(bodies[value], rewrite(value, idx))
        first = HEADING.search(body.split("\n", 1)[0]) if body else None
        title = re.sub(r"\s*\{[^}]*\}\s*$", "", first.group(2)).strip() if first else value
        toc.append(f"{indent}- [{title}](#{_anchor(value)})")
        parts.append(f'<a id="{_anchor(value)}"></a>\n\n{body}')

    now = dt.datetime.now(dt.timezone.utc).astimezone()
    sha = os.environ.get("GITHUB_SHA", "")[:7]
    stand = now.strftime("%d.%m.%Y") + (f", Commit {sha}" if sha else "")
    header = (
        f"# {config.site_name}: {TITLE}\n\n"
        f"Dieses Dokument fasst alle Seiten der Online-Dokumentation <{site_url}> "
        f"zu einer Datei zusammen. Es wird bei jeder Änderung automatisch neu erzeugt.\n\n"
        f"| | |\n| :--- | :--- |\n| Stand | {stand} |\n| Online-Version | <{site_url}> |\n\n"
        "## Inhalt\n\n" + "\n".join(toc) + "\n"
    )
    return header + "\n\n" + "\n\n".join(parts) + "\n"


# --- MkDocs events -----------------------------------------------------------

def on_files(files, config, **kwargs):
    global _combined
    _combined = _combine(config, files)
    page = (
        "---\n"
        f"title: {TITLE}\n"
        "search:\n  exclude: true\n"
        "hide:\n  - navigation\n"
        "---\n\n" + _combined
    )
    files.append(File.generated(config, PAGE_URI, content=page))
    return files


def on_post_build(config, **kwargs):
    out = os.path.join(config.site_dir, DOWNLOAD_URI)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(_combined)
