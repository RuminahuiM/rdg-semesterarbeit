# Sprint 1: Daily Journal

**Sprint-Zeitraum:** 26.10.2026 bis 16.11.2026  
**Release:** MVP  
**Board:** [Milestone Sprint 1](https://github.com/RuminahuiM/rdg-semesterarbeit/milestone/1)

Ein Eintrag pro Arbeitstag, höchstens drei Sätze.

## Einträge

### Sa 07.11.2026 (ca. 5 h)

Start der Umsetzung: Projekt übernommen, Einreichungsformular nach dem Feedback von Corrado Parisi zu Version 2 überarbeitet und mit einer Antwort an ihn gesendet. RDG-Repository bereinigt auf GitHub gepusht (CI-Job `infra` rot, Findings F-001 bis F-003), Doku-Repository mit MkDocs und GitHub Pages aufgesetzt, Board mit 6 Epics und 41 Stories angelegt, Doku-Gerüst nach den TBZ-Vorgaben gebaut und Sprint 1 geplant. Ausserdem Theorie, Anforderungen, Compliance und Teststrategie im Bericht ergänzt und ADR 0001 (Deployment mit GitHub Actions) als Pull Request im RDG-Repository erstellt.

!!! note "Zusatz ausserhalb der Semesterarbeit"
    Am gleichen Tag habe ich zusätzlich mein Portfolio unter [ruminahuim.github.io](https://ruminahuim.github.io/) aufgebaut: Hauptseite mit allen Semesterarbeiten, Doku der früheren Semesterarbeiten im gleichen Format, Bereinigung der öffentlichen Repositories. Diese Seite hier ist dort als Projektseite verlinkt und hat seither dasselbe Farbschema und Logo. Das war eigene Arbeit neben der Semesterarbeit und ist in der Zeiterfassung unten nicht enthalten.

### So 08.11.2026 (ca. 6 h)

Projektdokumentation gegengelesen und das Feedback eingearbeitet (Begründung für Scrum, Kapazität mit Mittwoch, Funktionen von RDG, Ablauf vom Issue zum Release, Label `auto-maintain`), dabei geprüft, ob der KI-Agent über das Claude-Abo statt über die API laufen kann, und daraus die Stories AI-9, CI-6, AI-10 und SEC-5 abgeleitet. Story Points ins Board eingetragen, Sprint 1 auf ToDo gesetzt, Zwischenstand mit allen Links an die Experten gepostet, PM-1 bis PM-4 gegen ihre Akzeptanzkriterien abgenommen, ADR 0001 gemergt, Finding F-004 erfasst und die ganze Doku zusätzlich als PDF und Markdown zum Download bereitgestellt. CI-1 umgesetzt: MIT-Lizenz mit ADR 0002 als [Pull Request #3](https://github.com/RuminahuiM/rdg/pull/3), wartet auf Review.

!!! note "Zusatz ausserhalb der Semesterarbeit"
    Für das Portfolio habe ich Farbschema und Logo überarbeitet. Diese Doku lädt beides zentral von der Portfolio-Hauptseite, und das Logo im Kopf führt jetzt dorthin zurück. Die Zeit dafür ist in der Zeiterfassung unten nicht enthalten.

## Zeiterfassung pro Story

| Story | Story Points | Schätzung (h) | Sa 07.11. (h) | So 08.11. (h) | Total (h) | Stand |
| --- | --- | --- | --- | --- | --- | --- |
| [PM-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/7) | 3 | 3 | 4.0 | | 4.0 | Done |
| [PM-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/8) | 2 | 2 | 0.3 | | 0.3 | Done |
| [PM-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/9) | 3 | 3 | 0.3 | 0.5 | 0.8 | Done |
| [PM-4](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/10) | 1 | 1 | 0.3 | 0.5 | 0.8 | Done |
| [PM-5](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/11) | 1 | 1 | 0.1 | | 0.1 | wartet auf Freigabe |
| [CI-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/12) | 1 | 1 | | 1.5 | 1.5 | In Review |
| Ohne Story: Feedback in der Projektdokumentation, Recherche Abo, neue Stories | | | | 2.5 | 2.5 | |
| Ohne Story: Gesamtdokument als PDF und Markdown | | | | 0.75 | 0.75 | |
| Ohne Story: ADR 0001 freigegeben (gehört zu Z2) | | | | 0.25 | 0.25 | |
| **Total** | **11** | **11** | **5.0** | **6.0** | **11.0** | |

Die Schätzung in Stunden ist der Richtwert ohne KI aus dem [Scrum-Setup](../../projekt/scrum-setup.md#schatzung). Bei PM-2 bis PM-5 war ich mit KI-Unterstützung deutlich schneller als geschätzt. Länger als geschätzt brauchten das Projekt-Setup (PM-1), in dem auch Theorie, Anforderungen und ADR 0001 mitliefen, und die Lizenz (CI-1), weil der Lizenzvergleich mit ADR mehr Aufwand war als nur die Datei. Am Sonntag ging fast die Hälfte der Zeit in Arbeit ohne eigene Story, vor allem in die Doku. Das nehme ich in die Retrospektive mit.
