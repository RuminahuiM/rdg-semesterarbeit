# Sprint 1: Planning

**Datum:** 08.11.2026  
**Sprint-Zeitraum:** 26.10.2026 bis 16.11.2026  
**Release:** MVP  
**Board:** [Milestone Sprint 1](https://github.com/RuminahuiM/rdg-semesterarbeit/milestone/1)

!!! note "Später Start"
    Sprint 1 begann laut Ablaufplan am 26.10.2026. Die Umsetzung startete erst am 07.11.2026, weil das Einreichungsformular nach dem Feedback des PM-Experten überarbeitet werden musste und ein anderes Projekt dazwischenkam. Für Sprint 1 bleiben darum nur vier Arbeitstage. Das wird in der Retrospektive ausgewertet.

## 1. Sprint-Ziel

RDG liegt als sauberes DevOps-Projekt auf GitHub: Projekt-Setup und Board stehen, die Arbeitsregeln sind festgelegt, die CI-Pipeline ist grün und `main` ist geschützt (Z1, Release MVP).

## 2. Ausgewählte Stories

| Story | Titel | Ziel | Story Points | Priorität | Stand 08.11. |
| --- | --- | --- | --- | --- | --- |
| [PM-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/7) | Projekt-Setup mit Doku-Repo und GitHub Pages | PM | 3 | must | umgesetzt, wartet auf Abnahme |
| [PM-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/8) | Kanban-Board einrichten | PM | 2 | must | fast fertig |
| [PM-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/9) | Product Backlog erstellen und Sprint 1 ausdefinieren | PM | 3 | must | fast fertig |
| [PM-4](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/10) | Sprint 1 Planning dokumentieren | PM | 1 | must | in Arbeit |
| [PM-5](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/11) | Formular Version 2 einreichen und Freigabe einholen | PM | 1 | must | offen |
| [CI-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/12) | Lizenz festlegen und ergänzen | Z1 | 1 | must | offen |
| [CI-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/13) | Tote Links in der RDG-Doku entfernen | Z1 | 1 | should | offen (Stretch) |
| [CI-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/14) | Arbeitsregeln festlegen (Branching, Commits, Versionen) | Z1 | 2 | must | offen |
| [CI-4](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/15) | CI-Pipeline reparieren | Z1 | 5 | must | offen |
| [CI-5](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/16) | Branch-Schutz auf main und Nachweis | Z1 | 3 | must | offen |
| [PM-6](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/17) | Besprechung 1 vorbereiten und protokollieren | PM | 1 | must | offen |
| [PM-7](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/18) | Sprint 1 Review und Retrospektive | PM | 2 | must | offen |

**Summe Story Points:** 25 (davon 8 SP am 07.11. weitgehend erledigt)  
**Verfügbare Kapazität ab 08.11.:** ca. 17.5 h, davon ca. 14 h planbar (20 Prozent Reserve)

## 3. Umsetzungsplan

| Tag | Stories |
| --- | --- |
| Sa 07.11. (erledigt) | PM-1 Projekt-Setup, PM-2 Board, PM-3 Backlog, Formular Version 2 |
| So 08.11. | PM-3 und PM-4 abschliessen, PM-5 Update an die Experten, CI-1 Lizenz |
| Mi 11.11. | CI-3 Arbeitsregeln mit ADR, CI-2 falls Zeit bleibt |
| Sa 14.11. | CI-4 CI-Pipeline reparieren |
| So 15.11. | CI-5 Branch-Schutz und Nachweis, PM-6 Vorbereitung Besprechung 1, Entwurf PM-7 |
| Mo 16.11. | Besprechung 1, PM-7 Review und Retro abschliessen, Teams-Post |

## 4. Risiken und Abhängigkeiten

| Risiko / Abhängigkeit | Wahrscheinlichkeit | Auswirkung | Massnahme |
| --- | --- | --- | --- |
| CI-4 braucht mehr Zeit als geschätzt, weil die Ursachen der roten Jobs noch unbekannt sind (R-T03, F-001) | Mittel | Hoch | Früh starten, nicht nötige Prüfungen notfalls als nicht blockierend markieren und als Finding nachziehen |
| CI-5 hängt von CI-4 ab: Pflicht-Checks ergeben erst Sinn, wenn die CI grün ist | Hoch | Mittel | CI-5 erst nach CI-4, Nachweis notfalls mit den Jobs, die schon grün sind |
| Nur vier Arbeitstage wegen des späten Starts | Hoch | Mittel | CI-2 als Stretch, Reserve nutzen |

## 5. Bewusst nicht im Sprint

Alles zum Deployment (DEP), zum Sicherheitsrahmen (SEC) und zur KI-Pipeline (AI). Das kommt ab Sprint 2.

## 6. Reserve und Stretch

- **Stretch:** CI-2 (should). Falls die Zeit nicht reicht, geht CI-2 in Sprint 2.
- **Reserve:** ca. 3.5 h für unerwartete Probleme, vor allem in CI-4.

## 7. Definition-of-Ready-Check

- [x] Alle ausgewählten Stories haben mindestens zwei Akzeptanzkriterien
- [x] Alle ausgewählten Stories sind geschätzt (Story Points im Issue)
- [ ] Story Points im Board eingetragen, Stories auf ToDo
- [x] Abhängigkeiten geklärt (CI-5 nach CI-4)
- [x] Offene Findings (F-001 bis F-003) und aktive Risiken geprüft
