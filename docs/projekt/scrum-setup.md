# Scrum-Setup

Wie ich Scrum in dieser Solo-Arbeit anwende. Grundlage ist der Scrum Guide 2020 und der Unterricht Projektmanagement an der TBZ.

## Rollen

In einer Solo-Arbeit habe ich alle drei Verantwortlichkeiten selbst.

| Verantwortlichkeit | Wer | Wie gelebt |
| --- | --- | --- |
| Product Owner | ich | Backlog pflegen und priorisieren (MoSCoW), Abnahme im Review |
| Scrum Master | ich | Events einhalten, Retrospektive, Hindernisse aus dem Weg räumen |
| Developer | ich, mit Unterstützung durch einen KI-Assistenten (Claude) | Umsetzung, Tests, Code-Review |
| Stakeholder | die beiden Experten, HEKS als erster Anwender von RDG | Feedback in den Besprechungen und über den Teams-Kanal |

### Grenzen der Solo-Anwendung

| Grenze | Was ich dagegen mache |
| --- | --- |
| Keine Rollentrennung, Gefahr von "ScrumBut" | Feste Events mit Vorlagen, Prozess ist ein eigener Punkt in jeder Retro |
| Kein Team-Daily | Daily Journal pro Arbeitstag |
| Niemand, der den Code reviewt | Jeder Pull Request wird vor dem Merge geprüft, die CI-Pipeline ist Pflicht |

## Events

Die Sprint-Längen richten sich nach den fixen Besprechungsterminen der TBZ, darum sind die Sprints unterschiedlich lang.

| Event | Timebox | Ablage |
| --- | --- | --- |
| Sprint | 3 bis 5 Wochen (siehe [Steckbrief](steckbrief.md)) | |
| Sprint Planning | 2 h | `sprints/sprint-<n>/planning.md` |
| Daily | 5 min | `sprints/sprint-<n>/daily.md` |
| Sprint Review | 1 h | `sprints/sprint-<n>/review.md`, danach Post im Teams-Kanal |
| Retrospektive | 45 min | `sprints/sprint-<n>/retro.md` |

## Artefakte

- **Product Backlog** mit Product Goal: GitHub Projects, Issues im RDG-Repository
- **Sprint Backlog** mit Sprint Goal: Sprint-Ansicht im Board und `planning.md`
- **Increment** mit Definition of Done: Release am Ende jedes Sprints (MVP, MLP, MMP, siehe [Roadmap](roadmap.md))

### Product Goal

RDG ist ein sauber aufgesetztes Open-Source-Projekt mit CI/CD, automatischem Testdeployment und Release-Freigabe von Hand, und es ist ausgewertet, wie weit ein KI-Agent bei der Wartung helfen kann.

### Definition of Ready

Eine Story kommt erst in einen Sprint, wenn:

- sie als User Story oder als klare technische Aufgabe beschrieben ist
- sie mindestens zwei Akzeptanzkriterien hat (als Checkliste im Issue)
- Abhängigkeiten geklärt sind
- sie geschätzt ist (Story Points)
- sie einem Ziel (Z1 bis Z4) zugeordnet ist
- sie klein genug für einen Sprint ist

### Definition of Done

Eine Story ist fertig, wenn:

- alle Akzeptanzkriterien erfüllt und abgehakt sind
- die CI-Pipeline grün ist (Tests, Linting, Sicherheits-Scan)
- es für Änderungen am Verhalten einen automatischen Test gibt oder einen dokumentierten manuellen Test mit Screenshot
- der Pull Request geprüft und gemergt ist
- die Doku nachgeführt ist (README, Guides, Design, wo betroffen)
- Architekturentscheide als ADR im RDG-Repository festgehalten sind
- übernommene Texte und Code-Teile mit Quelle angegeben sind
- der Nachweis im Sprint Journal steht und die Zeit erfasst ist

## Schätzung

Story Points nach Fibonacci. Die Stunden sind ein Richtwert ohne KI-Unterstützung. Die tatsächliche Zeit erfasse ich pro Story, so sieht man am Schluss, wie viel die KI-Unterstützung ausgemacht hat.

| Story Points | Richtwert |
| --- | --- |
| 1 | bis 1 h |
| 2 | ca. 2 h |
| 3 | ca. 3 h |
| 5 | ca. 7 h |
| 8 | ca. 15 h |
| 13 | zu gross, aufteilen |

## Kapazität

Kapazität laut Arbeitsrhythmus im [Steckbrief](steckbrief.md). Pro Sprint plane ich ca. 20 Prozent Reserve ein.

## Kommunikation mit den Experten

- Nach jedem Sprint Planning und Sprint Review ein Post im Teams-Kanal mit Link auf die passende Seite dieser Doku.
- Die Besprechungen werden vorbereitet und protokolliert, Action Items kommen ins Backlog (siehe [Besprechungen](../besprechungen/index.md)).
