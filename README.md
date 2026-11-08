# RDG als DevOps-Projekt mit KI-Wartung

| | |
| :--- | :--- |
| Titel der Semesterarbeit | RDG als DevOps-Projekt mit KI-Wartung: Eine Pipeline, die GitHub-Issues selbst löst |
| Name | Dodoe Rumiñahui Mannale |
| Studiengang | Dipl. Informatiker/in HF, ITCNE25, TBZ |
| Semester / Abgabe | Semester 4 / 27.01.2027 |

Dieses Repository enthält die Dokumentation meiner 4. Semesterarbeit: Projektmanagement, Sprint Journal, Besprechungen und die Projektdokumentation. Der Code des Produkts liegt im Repository [RuminahuiM/rdg](https://github.com/RuminahuiM/rdg).

**Lesen:** <https://ruminahuim.github.io/rdg-semesterarbeit/>

## Aufbau

| Pfad | Inhalt |
| --- | --- |
| `docs/index.md` | Startseite mit Zielen, Stand und Links |
| `docs/projektdokumentation.md` | Projektdokumentation (Schlussbericht), wird laufend ergänzt |
| `docs/projekt/` | Steckbrief, Einreichungsformular, Roadmap, Scrum-Setup, Risk Register, Findings, Traceability |
| `docs/sprints/` | Planning, Daily Journal, Review und Retrospektive pro Sprint |
| `docs/besprechungen/` | Vorbereitung und Protokolle der Besprechungen mit den Experten |
| `docs/nachweise/` | Testprotokoll und Auswertung der KI-Wartung |
| `docs/abschluss/` | Schlusspräsentation |
| `docs/anhang/` | Quellen und Glossar |

## Gesamtdokument (Markdown und PDF)

Für die Abgabe gibt es die ganze Dokumentation auch als eine Datei. Die Startseite hat dafür zwei Buttons.

| Datei | Erzeugt durch |
| --- | --- |
| `downloads/rdg-semesterarbeit-gesamtdokument.md` | `hooks/gesamtdokument.py` bei jedem `mkdocs build` |
| `downloads/rdg-semesterarbeit-gesamtdokument.pdf` | `scripts/build_pdf.py` im Workflow (Chromium druckt die Seite `/gesamtdokument/`) |

Der Hook nimmt alle Seiten in der Reihenfolge von `nav` in `mkdocs.yml`. Eine neue Seite kommt also automatisch ins Gesamtdokument, sobald sie in der Navigation steht. Links zwischen den Seiten werden zu Sprungmarken im Dokument, externe Links bleiben als URL. Text zwischen `<!-- export:skip -->` und `<!-- /export:skip -->` wird nicht übernommen.

PDF lokal erzeugen (optional):

```bash
pip install playwright && python -m playwright install chromium
mkdocs build
python scripts/build_pdf.py site gesamtdokument/ gesamtdokument.pdf
```

## Lokal ansehen

```bash
pip install -r requirements.txt
mkdocs serve
```

Die Seite wird bei jedem Push auf `main` automatisch mit GitHub Actions gebaut und auf GitHub Pages veröffentlicht.
