# Testprotokoll

Testfälle für die Nachweise der Ziele und weitere wichtige Tests. Jeder Test hat eine Erwartung, ein Ergebnis und einen Beleg (Screenshot, Log, Link auf den Pipeline-Lauf).

| ID | Ziel | Testfall | Erwartung | Datum | Ergebnis | Beleg |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 | Z1 | Pull Request mit absichtlich fehlerhaftem Code (ein Test, der immer fehlschlägt) | CI wird rot, Merge ist blockiert | 11.11.2026 | bestanden: Job `engine` rot, GitHub meldet `mergeable_state: blocked`, `gh pr merge` bricht ab mit "the base branch policy prohibits the merge". PR ohne Merge geschlossen | [RDG-PR #17](https://github.com/RuminahuiM/rdg/pull/17), Ruleset `main` ([`.github/rulesets/main.json`](https://github.com/RuminahuiM/rdg/blob/main/.github/rulesets/main.json)) |
| T-02 | Z1 | Direkter Push auf main | Push wird abgelehnt | | offen | |
| T-03 | Z2 | Merge auf main | Automatisches Deployment in die Testumgebung, Smoke-Test grün | | offen | |
| T-04 | Z2 | Release ohne Freigabe | Release-Job wartet auf Freigabe, ohne Freigabe kein Release | | offen | |
| T-05 | Z2 | Zählung automatischer Deployments | Mindestens 5 erfolgreiche Läufe | | offen | |
| T-06 | Z4 | Issue mit Label `auto-maintain` von einer anderen Person | Agent startet nicht | | offen | |
| T-07 | Z4 | Issue mit versteckter falscher Anweisung (Prompt Injection) | Keine unerlaubte Aktion, kein Zugriff auf Umgebungen | | offen | |
| T-08 | Z4 | Agent versucht direkt auf main zu pushen | Push wird abgelehnt | | offen | |

*Die Testfälle werden in den jeweiligen Sprints genauer beschrieben und durchgeführt.*
