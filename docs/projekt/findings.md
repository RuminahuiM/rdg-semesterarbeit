# Findings

Probleme und Verbesserungen, die beim Arbeiten auffallen, aber nicht sofort gelöst werden. Jedes Finding kommt hierhin, damit nichts verloren geht. Grössere Findings bekommen zusätzlich ein Issue im RDG-Repository.

- **ID:** `F-NNN`, fortlaufend
- **Schweregrad:** Must, Should, May, Info
- **Auslöser:** wann das Finding angegangen wird (z.B. "Sprint 2", "vor dem Release")
- **Status:** offen, in Arbeit, als Issue erfasst, gelöst (Datum), wird nicht gemacht (Begründung)

## Offene Findings

| ID | Titel | Schweregrad | Auslöser | Status |
| --- | --- | --- | --- | --- |
| F-001 | CI auf GitHub rot: 4 von 6 Jobs schlagen fehl (`infra`, `powershell lint`, `engine` mit 8 fehlschlagenden Sync-Tests, `web` mit 1 fehlschlagendem E2E-Test); `contracts` und `security` sind grün | Must | Sprint 1 (CI-4) | gelöst (11.11.2026, CI-4: RDG-PRs #8 bis #11 und #15) |
| F-002 | `docs/README.md` im RDG-Repository verlinkt auf alte, nicht öffentliche Design-Dokumente | Should | Sprint 1 | gelöst (11.11.2026, CI-2, RDG-PR #6) |
| F-003 | RDG-Repository hat noch keine Lizenz-Datei | Must | Sprint 1 | gelöst (11.11.2026, MIT-Lizenz mit ADR 0002, RDG-PR #3) |
| F-004 | Veröffentlichte RDG-Texte enthalten noch Bezüge zum ersten Anwender (Name, Grösse, Testreihenfolge); laut Implementation Plan vor der Veröffentlichung umformulieren | Should | Sprint 1 oder 2, zusammen mit CI-2 | gelöst (11.11.2026, RDG-PR #7) |
| F-005 | Die Git-Historie des öffentlichen RDG-Repositorys (erster Import) enthält die alten Bezüge zum ersten Anwender weiterhin; F-004 bereinigt nur den aktuellen Stand | Info | Entscheid durch Maintainer | wird nicht gemacht (11.11.2026: akzeptiert, die Historie bleibt unverändert; ein Umschreiben würde Commit-Links ungültig machen) |
| F-006 | RDG läuft auf PowerShell 7.4, dessen Support am 10.11.2026 endete; die CI läuft bereits auf 7.6. Laufzeit in Azure Functions und Automation auf 7.6 umstellen | Should | Sprint 2 (Kandidat für ein Test-Issue des KI-Agenten) | als Issue erfasst ([RDG #14](https://github.com/RuminahuiM/rdg/issues/14)) |
| F-007 | Die API nennt bei Fehlern in verschachtelten Objekten (z.B. `target.mode`) kein Feld, sondern `(body)`: `Test-Json` in PowerShell 7.6 liefert dafür keine Meldung. Felder auf oberster Ebene werden seit RDG-PR #9 wieder genannt | May | zusammen mit F-006 | als Issue erfasst ([RDG #14](https://github.com/RuminahuiM/rdg/issues/14)) |

## Historie

| Datum | Änderung |
| --- | --- |
| 07.11.2026 | F-001 bis F-003 beim Aufsetzen des Repositories erfasst |
| 08.11.2026 | F-004 bei der Prüfung der öffentlichen Repositories erfasst |
| 11.11.2026 | F-001 präzisiert: nicht nur `infra`, sondern 4 von 6 Jobs rot (Läufe der PRs #2 und #3) |
| 11.11.2026 | F-003 gelöst: MIT-Lizenz im RDG-Repository (PR #3) |
| 11.11.2026 | F-002 und F-004 in Arbeit: RDG-PRs #6 (Links) und #7 (neutrale Formulierungen) |
| 11.11.2026 | F-005 bei der Umsetzung von F-004 erfasst |
| 11.11.2026 | F-002 und F-004 gelöst (RDG-PRs #6 und #7), F-005 akzeptiert |
| 11.11.2026 | F-001: Ursachen gefunden und behoben (siehe Projektdokumentation 10.2); F-006 bei der CI-Reparatur erfasst |
| 11.11.2026 | Review der CI-Reparatur: Web-Test mit fester Uhrzeit (RDG-PR #15), Schema-Auflösung abgesichert; F-007 erfasst |
| 11.11.2026 | F-001 gelöst: alle CI-Jobs auf `main` grün |
