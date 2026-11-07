# Projekt-Steckbrief

Zentrale Stammdaten der Semesterarbeit.

## Stammdaten

| Feld | Wert |
| --- | --- |
| Titel | RDG als DevOps-Projekt mit KI-Wartung: Eine Pipeline, die GitHub-Issues selbst löst |
| Produkt-Repository | [RuminahuiM/rdg](https://github.com/RuminahuiM/rdg) (öffentlich, Open Source) |
| Doku-Repository | [RuminahuiM/rdg-semesterarbeit](https://github.com/RuminahuiM/rdg-semesterarbeit) (öffentlich, GitHub Pages) |
| Studierender | Dodoe Rumiñahui Mannale |
| Studiengang / Klasse | Dipl. Informatiker/in HF, ITCNE25, TBZ |
| Semester | 4 |
| Form | Solo |
| Themenfelder | Projektmanagement (Pflicht), DevOps |
| Experten | Projektmanagement: Corrado Parisi. Fachlich (DevOps): wird ergänzt |
| Zeitbudget | ca. 50 Stunden (Vorgabe TBZ), max. 12 Wochen |

## Termine

| Termin | Datum | Notiz |
| --- | --- | --- |
| Einreichung Formular | 21.10.2026 | Version 2 nach Feedback am 07.11.2026 |
| Besprechung 1 | 16.11.2026 | Ende Sprint 1 |
| Besprechung 2 | 14.12.2026 | Ende Sprint 2 |
| Besprechung 3 | 22.01.2027 | Ende Sprint 3 |
| Feature-Freeze | 09.01.2027 | Danach nur noch Tests, Fehlerbehebung, Auswertung und Doku |
| Abgabe mit Schlusspräsentation | 27.01.2027 | Termine laut Ablaufplan der TBZ sind fix |

## Arbeitsrhythmus

| Wann | Kapazität |
| --- | --- |
| Wochenende (Samstag und/oder Sonntag) | je ca. 4 bis 6 h |
| Ein Abend unter der Woche | ca. 2 bis 3 h |
| Übrige Tage | keine Projektarbeit |

## Sprints

| Sprint | Zeitraum | Ziel | Status |
| --- | --- | --- | --- |
| 1 | 26.10. bis 16.11.2026 | Sauberes DevOps-Projekt: Repos, Board, Branch-Schutz, CI-Pipeline repariert und getestet (Z1) | aktiv |
| 2 | 17.11. bis 14.12.2026 | Automatisches Deployment in die Testumgebung und Release mit Freigabe (Z2), erste KI-Pipeline mit Sicherheitsregeln (Z4) | geplant |
| 3 | 15.12.2026 bis 22.01.2027 | KI-Pipeline fertig, 8 Test-Issues und Prompt-Injection-Test durchspielen und auswerten (Z3, Z4) | geplant |
| Abschluss | 23.01. bis 27.01.2027 | Reflexion, Schlusspräsentation, Abgabe | geplant |

**Aktueller Sprint:** 1

## Tracking

| Feld | Wert |
| --- | --- |
| Tool | GitHub Projects (Kanban-Board), Issues im RDG-Repository |
| Status-Workflow | To Do, In Progress, In Review, Done |
| Priorisierung | MoSCoW (Must, Should, Could, Won't) |
| Schätzung | Story Points (Fibonacci) |

## Ziele

1. **Z1 Sauberes DevOps-Projekt:** Branch-Schutz auf `main`, Merge nur per Pull Request mit grüner CI. Nachweis: Ein absichtlich fehlerhafter Pull Request wird blockiert.
2. **Z2 Automatisches Deployment und Freigabe:** Jeder Merge auf `main` deployt automatisch in die Testumgebung (mit Smoke-Test), ein Release gibt es nur nach Freigabe von Hand. Nachweis: mindestens 5 automatische Deployments und ein freigegebenes Release.
3. **Z3 KI-Wartung als Versuch:** 8 Test-Issues aus vier Issue-Arten, pro Issue Ergebnis, eigener Aufwand, Dauer und Kosten. Nachweis: Auswertung mit Erfolgen und Grenzen.
4. **Z4 Die KI bleibt eingeschränkt:** kein Push auf `main`, kein Zugriff auf Azure und die Umgebungen, reagiert nur auf meine Issues. Nachweis: Prompt-Injection-Test ohne unerlaubte Aktion.

## Projektspezifische Regeln

- **Kubernetes:** Für diese Arbeit ausnahmsweise nicht nötig (abgesprochen mit Thanam Pangri und Marcel Bernet am 21.10.2026). Kubernetes kommt in die 5. Semesterarbeit.
- **Keine echten Firmendaten:** Keine Passwörter, Secrets oder echten Tenant-Daten in den Repositories. Beispiele verwenden `contoso`.
- **Getestet wird im eigenen Test-Tenant:** Die produktive Installation beim ersten Anwender wird in dieser Arbeit nicht verändert.
- **Die KI arbeitet nur über Pull Requests:** Jeder Pull Request wird vor dem Merge von mir geprüft.
