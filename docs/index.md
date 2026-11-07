# RDG als DevOps-Projekt mit KI-Wartung

| | |
| :--- | :--- |
| Titel der Semesterarbeit | RDG als DevOps-Projekt mit KI-Wartung: Eine Pipeline, die GitHub-Issues selbst löst |
| Name | Dodoe Rumiñahui Mannale |
| Studiengang | Dipl. Informatiker/in HF, ITCNE25, TBZ |
| Semester / Abgabe | Semester 4 / 27.01.2027 |
| Themenfelder | Projektmanagement, DevOps |

Diese Seite ist die Dokumentation meiner 4. Semesterarbeit. Sie wird laufend nachgeführt und zeigt jederzeit den aktuellen Stand.

## Worum geht es?

RDG (Real Dynamic Groups) ist ein Tool, das ich bei meiner Arbeit gebaut habe. Es pflegt Gruppen in Microsoft 365 nach Regeln und schreibt das Resultat als normale Mitgliederliste in die Gruppe. So funktionieren die Gruppen auch dort, wo Microsoft dynamische Gruppen ablehnt.

In dieser Arbeit mache ich aus RDG ein sauberes DevOps-Projekt: mit Tests, automatischem Deployment in eine Testumgebung und einer Release-Freigabe von Hand. Danach probiere ich aus, wie gut ein KI-Agent bei der Wartung helfen kann, und werte das aus.

## Ziele

| Ziel | Kurz | Umfang |
| --- | --- | --- |
| Z1 | Sauberes DevOps-Projekt: Repo, Branch-Schutz, CI-Pipeline, Kanban-Board | Must |
| Z2 | Automatisches Deployment in die Testumgebung und Release-Freigabe von Hand | Must |
| Z3 | KI-Wartung als Versuch mit 8 Test-Issues und Auswertung | Must (Durchführung und Auswertung) |
| Z4 | Die KI bleibt eingeschränkt (nur Pull Requests, keine Rechte auf Umgebungen) | Must |

Details im [Einreichungsformular](projekt/einreichungsformular.md).

## Aktueller Stand

| | |
| :--- | :--- |
| Aktueller Sprint | Sprint 1 (26.10. bis 16.11.2026) |
| Nächste Besprechung | 16.11.2026 |
| Feature-Freeze | 09.01.2027 |

## Links

| Was | Wo |
| --- | --- |
| Produkt-Repository (RDG, Open Source) | [github.com/RuminahuiM/rdg](https://github.com/RuminahuiM/rdg) |
| Repository dieser Dokumentation | [github.com/RuminahuiM/rdg-semesterarbeit](https://github.com/RuminahuiM/rdg-semesterarbeit) |
| Kanban-Board (GitHub Projects) | wird in Sprint 1 verlinkt |

## Aufbau dieser Dokumentation

| Bereich | Inhalt |
| --- | --- |
| [Projektdokumentation](projektdokumentation.md) | Der Schlussbericht mit Teil A Projektmanagement und Teil B fachliche Umsetzung. Wird laufend ergänzt |
| [Projekt](projekt/steckbrief.md) | Steckbrief, Einreichungsformular, Roadmap, Scrum-Setup, Risk Register, Findings, Traceability |
| [Sprints](sprints/index.md) | Planning, Daily Journal, Review und Retrospektive pro Sprint |
| [Besprechungen](besprechungen/index.md) | Vorbereitung und Protokolle der Einzelbesprechungen mit den Experten |

Die Doku des Produkts selbst (Requirements, Design, Architekturentscheide, Guides) liegt im RDG-Repository, weil sie zum Tool gehört und dort weiterlebt.
