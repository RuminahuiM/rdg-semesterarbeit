"""Print a page of the built MkDocs site to PDF with headless Chromium.

Used by the pages workflow after `mkdocs build`:

    python scripts/build_pdf.py site gesamtdokument/ \
        site/downloads/rdg-semesterarbeit-gesamtdokument.pdf

The site is served locally so relative links, CSS and scripts work. Mermaid
diagrams are rendered in the browser before printing, collapsible blocks are
opened, and the light colour scheme is forced.
"""

from __future__ import annotations

import functools
import http.server
import sys
import threading

from playwright.sync_api import sync_playwright

FOOTER = (
    '<div style="width:100%;font-size:8px;color:#666;padding:0 15mm;'
    'display:flex;justify-content:space-between;font-family:sans-serif">'
    '<span class="title"></span>'
    '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
)

# Full page width; every top-level chapter (h1 after the title) starts on a new page;
# table rows, admonitions, code blocks and diagrams are not split.
PRINT_CSS = """
.md-grid { max-width: none; }
.md-main__inner, .md-content__inner { margin: 0; padding: 0; }
.md-typeset h1 ~ h1 { break-before: page; }
.md-typeset tr, .md-typeset .admonition, .md-typeset pre,
.md-typeset .mermaid { break-inside: avoid; }
.md-typeset h1, .md-typeset h2, .md-typeset h3 { break-after: avoid; }
"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main(site_dir: str, page: str, out: str) -> None:
    handler = functools.partial(QuietHandler, directory=site_dir)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{httpd.server_address[1]}/{page}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        tab = browser.new_page(color_scheme="light")
        tab.goto(url, wait_until="networkidle", timeout=120_000)
        # Mermaid renders asynchronously; give it time after the network is idle
        tab.wait_for_timeout(3000)
        tab.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
        tab.emulate_media(media="print", color_scheme="light")
        tab.add_style_tag(content=PRINT_CSS)
        tab.pdf(
            path=out,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=FOOTER,
            margin={"top": "15mm", "bottom": "18mm", "left": "15mm", "right": "15mm"},
        )
        browser.close()
    httpd.shutdown()
    print(f"PDF written: {out}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: build_pdf.py <site_dir> <page_path> <out.pdf>")
    main(*sys.argv[1:])
