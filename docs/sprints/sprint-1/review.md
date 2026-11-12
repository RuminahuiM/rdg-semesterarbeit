# Sprint 1: Review

**Datum:** 12.11.2026  
**Sprint-Zeitraum:** 26.10.2026 bis 12.11.2026 (geplant bis 16.11.2026, vorzeitig abgeschlossen)  
**Release:** MVP  
**Board:** [Milestone Sprint 1](https://github.com/RuminahuiM/rdg-semesterarbeit/milestone/1)

!!! note "Vorzeitiger Abschluss"
    Am 12.11. waren alle Stories von Sprint 1 erledigt. Ich habe den Sprint darum vier Tage früher abgeschlossen und Sprint 2 am gleichen Tag gestartet. Die geplanten Arbeitstage 14. und 15.11. gehören damit zu Sprint 2. Besprechung 1 bleibt am 16.11.2026.

## 1. Erreichung des Sprint-Ziels

**Sprint-Ziel:** Sauberes DevOps-Projekt: RDG liegt sauber auf GitHub, Board steht, Branch-Schutz aktiv, CI-Pipeline grün (Z1)

- [x] Vollständig erreicht
- [ ] Teilweise erreicht
- [ ] Nicht erreicht

Der Nachweis für Z1 ist erbracht: Ein absichtlich fehlerhafter Pull Request wird vom Ruleset auf `main` blockiert (T-01 im [Testprotokoll](../../nachweise/testprotokoll.md)).

## 2. Stories und Akzeptanzkriterien

| Story | Ergebnis | Nachweis |
| --- | --- | --- |
| [PM-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/7) Projekt-Setup | Doku-Repository mit MkDocs, Veröffentlichung über GitHub Pages | [Doku-Seite](https://ruminahuim.github.io/rdg-semesterarbeit/) |
| [PM-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/8) Kanban-Board | Board mit Status Backlog bis Done, Story Points, Labels, Milestones, Automatik | [Board](https://github.com/users/RuminahuiM/projects/1) |
| [PM-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/9) Product Backlog | 6 Epics mit Stories als Unter-Issues, MoSCoW, Sprint 1 nach DoR | [Board](https://github.com/users/RuminahuiM/projects/1) |
| [PM-4](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/10) Sprint 1 Planning | Planning dokumentiert, Zwischenstand am 08.11. im Teams-Kanal | [Planning](planning.md) |
| [PM-5](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/11) Formular Version 2 | Am 09.11. ohne Auflagen freigegeben, Thanam Pangri betreut fachlich | [Einreichungsformular](../../projekt/einreichungsformular.md) |
| [CI-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/12) Lizenz | MIT-Lizenz mit ADR 0002 | RDG-PR [#3](https://github.com/RuminahuiM/rdg/pull/3) |
| [CI-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/13) Tote Links | Links auf Dateien im Repository, Bezüge zum ersten Anwender entfernt | RDG-PRs [#6](https://github.com/RuminahuiM/rdg/pull/6), [#7](https://github.com/RuminahuiM/rdg/pull/7) |
| [CI-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/14) Arbeitsregeln | GitHub Flow, Conventional Commits, SemVer in `CONTRIBUTING.md`, ADR 0003 | RDG-PR [#5](https://github.com/RuminahuiM/rdg/pull/5) |
| [CI-4](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/15) CI-Pipeline | Alle 6 Jobs auf `main` grün, Ursachen in [Kapitel 10.2](../../projektdokumentation.md#102-ci-pipeline-z1) | RDG-PRs [#8](https://github.com/RuminahuiM/rdg/pull/8) bis [#11](https://github.com/RuminahuiM/rdg/pull/11), [#15](https://github.com/RuminahuiM/rdg/pull/15) |
| [CI-5](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/16) Branch-Schutz | Ruleset auf `main` als Code, fehlerhafter PR blockiert | RDG-PRs [#13](https://github.com/RuminahuiM/rdg/pull/13), [#16](https://github.com/RuminahuiM/rdg/pull/16), [#17](https://github.com/RuminahuiM/rdg/pull/17) |
| [PM-6](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/17) Besprechung 1 | Vorbereitung mit Stand, Fragen und Demo-Plan, im Teams-Kanal geteilt | [Besprechung 1](../../besprechungen/besprechung-1.md) |
| [PM-7](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/18) Review und Retro | Diese Seite und die [Retrospektive](retro.md), Teams-Post | diese Seite |

## 3. Nicht abgeschlossene Stories

| Story | Anteil fertig | Was passiert damit |
| --- | --- | --- |
| keine | | Das Protokoll von Besprechung 1 kann erst nach dem Termin am 16.11. entstehen. Es ist darum aus PM-6 herausgelöst und als [PM-14](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/52) in Sprint 2 geplant |

## 4. Demo

Das Increment (MVP) ist der Stand von `main` im RDG-Repository vom 11.11.2026. Gezeigt wird es in der Besprechung am 16.11. live, hier als Rundgang mit Links:

1. **Doku:** Die [Startseite](https://ruminahuim.github.io/rdg-semesterarbeit/) führt zu Bericht, Planung, Sprints und Nachweisen. Die ganze Doku gibt es auch als ein Dokument (PDF und Markdown).
2. **Board:** Im [Board](https://github.com/users/RuminahuiM/projects/1) stehen alle Stories von Sprint 1 auf Done, Sprint 2 und 3 auf Backlog.
3. **CI:** Auf `main` laufen alle 6 Jobs grün ([GitHub Actions](https://github.com/RuminahuiM/rdg/actions)).
4. **Branch-Schutz:** Der absichtlich fehlerhafte [Pull Request #17](https://github.com/RuminahuiM/rdg/pull/17) wurde blockiert und ohne Merge geschlossen.
5. **Arbeitsregeln:** `CONTRIBUTING.md`, PR-Vorlage und ADR 0001 bis 0003 liegen im RDG-Repository.

## 5. Risk Review

| Risiko | Was ist passiert / neue Bewertung | Reaktion |
| --- | --- | --- |
| R-T03 Pipelines brauchen mehr Arbeit | Eingetreten: 4 von 6 CI-Jobs waren rot, mit mehreren Ursachen | Pro Ursache ein Pull Request, nach Review nachgebessert, gelöst |
| R-S01 Zu wenig Zeit | Sprint 1 trotz spätem Start früher fertig. Sprint 2 bekommt durch den frühen Start zwei Arbeitstage mehr. Score von 9 auf 6 gesenkt | Weiter beobachten, die Ferien bleiben in Sprint 2 |
| R-P01 Belastung | Nicht eingetreten | Keine |

## 6. Velocity und Zeit

| Geplante SP | Erledigte SP | Geschätzte Stunden | Tatsächliche Stunden |
| --- | --- | --- | --- |
| 25 | 25 | 27 | 16 (davon 3.5 ohne Story) |

Die Schätzung in Stunden ist der Richtwert ohne KI aus dem [Scrum-Setup](../../projekt/scrum-setup.md#schatzung). Mit KI-Unterstützung lag die tatsächliche Zeit deutlich darunter, vor allem bei der CI-Reparatur (CI-4: geschätzt 7 h, gebraucht ca. 2 h). Details pro Story im [Daily Journal](daily.md).

## 7. Erkenntnisse für den Backlog

- **PM-14:** Protokoll von Besprechung 1 mit Action Items (Sprint 2).
- **Belege:** Für die Nachweise fehlen noch Screenshots (CI grün, blockierter Pull Request, Board). Sie kommen beim nächsten Nachweis direkt mit ins Testprotokoll.
- **Release-Tag:** Für das MVP gibt es noch kein Release mit Versionsnummer. Das erste Release entsteht mit dem Release-Workflow (DEP-5).
- **F-006:** Die Laufzeit von PowerShell 7.4 ist seit dem 10.11.2026 ohne Support. Kandidat für ein Test-Issue des KI-Agenten.

## 8. Kommunikation

Post im Teams-Kanal am: 12.11.2026, mit Link auf dieses Review und auf die Vorbereitung von Besprechung 1
