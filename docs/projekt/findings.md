# Findings

Probleme und Verbesserungen, die beim Arbeiten auffallen, aber nicht sofort gelöst werden. Jedes Finding kommt hierhin, damit nichts verloren geht. Grössere Findings bekommen zusätzlich ein Issue im RDG-Repository.

- **ID:** `F-NNN`, fortlaufend
- **Schweregrad:** Must, Should, May, Info
- **Auslöser:** wann das Finding angegangen wird (z.B. "Sprint 2", "vor dem Release")
- **Status:** offen, in Arbeit, als Issue erfasst, gelöst (Datum), wird nicht gemacht (Begründung)

## Offene Findings

| ID | Titel | Schweregrad | Auslöser | Status |
| --- | --- | --- | --- | --- |
| F-001 | CI auf GitHub rot: 4 von 6 Jobs schlagen fehl (`infra`, `powershell lint`, `engine` mit 8 fehlschlagenden Sync-Tests, `web` mit 1 fehlschlagendem E2E-Test); `contracts` und `security` sind grün | Must | Sprint 1 (CI-4) | offen |
| F-002 | `docs/README.md` im RDG-Repository verlinkt auf alte, nicht öffentliche Design-Dokumente | Should | Sprint 1 | in Arbeit (CI-2, RDG-PR #6) |
| F-003 | RDG-Repository hat noch keine Lizenz-Datei | Must | Sprint 1 | gelöst (11.11.2026, MIT-Lizenz mit ADR 0002, RDG-PR #3) |
| F-004 | Veröffentlichte RDG-Texte enthalten noch Bezüge zum ersten Anwender (Name, Grösse, Testreihenfolge); laut Implementation Plan vor der Veröffentlichung umformulieren | Should | Sprint 1 oder 2, zusammen mit CI-2 | in Arbeit (RDG-PR #7) |

## Historie

| Datum | Änderung |
| --- | --- |
| 07.11.2026 | F-001 bis F-003 beim Aufsetzen des Repositories erfasst |
| 08.11.2026 | F-004 bei der Prüfung der öffentlichen Repositories erfasst |
| 11.11.2026 | F-001 präzisiert: nicht nur `infra`, sondern 4 von 6 Jobs rot (Läufe der PRs #2 und #3) |
| 11.11.2026 | F-003 gelöst: MIT-Lizenz im RDG-Repository (PR #3) |
| 11.11.2026 | F-002 und F-004 in Arbeit: RDG-PRs #6 (Links) und #7 (neutrale Formulierungen) |
