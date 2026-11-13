# Sprint 2: Planning

**Datum:** 12.11.2026  
**Sprint-Zeitraum:** 12.11.2026 bis 14.12.2026  
**Release:** MLP  
**Board:** [Milestone Sprint 2](https://github.com/RuminahuiM/rdg-semesterarbeit/milestone/2)

## 1. Sprint-Ziel

**Jede Änderung auf `main` landet automatisch und geprüft in der Testumgebung, ein Release gibt es nur nach meiner Freigabe, und ein erstes Issue wird vom eingeschränkten KI-Agenten als Pull Request gelöst.**

Damit sind Z2 erfüllt und die Grundlagen für Z3 und Z4 gelegt (Release MLP).

## 2. Ausgewählte Stories

| Story | Titel | Ziel | Story Points | Priorität |
| --- | --- | --- | --- | --- |
| [PM-8](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/31) | Sprint 2 Planning | PM | 2 | must |
| [PM-14](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/52) | Protokoll Besprechung 1 und Action Items | PM | 1 | must |
| [DEP-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/19) | Test-Tenant und Azure-Abo einrichten | Z2 | 3 | must |
| [DEP-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/20) | RDG in der Testumgebung installieren | Z2 | 5 | must |
| [DEP-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/21) | Login aus GitHub Actions nach Azure per OIDC | Z2 | 3 | must |
| [DEP-6](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/24) | Settings der Testumgebung in der GitHub-Umgebung | Z2 | 2 | must |
| [DEP-4](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/22) | Deploy-Workflow nach jedem Merge auf main | Z2 | 8 | must |
| [DEP-5](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/23) | Release-Workflow mit Freigabe von Hand | Z2 | 5 | must |
| [AI-9](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/48) | Agent über das Claude-Abo betreiben (OAuth-Token) | Z3 | 3 | must |
| [SEC-3](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/27) | Regelwerk für den Agenten im RDG-Repo | Z4 | 2 | must |
| [SEC-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/25) | KI-Agent nur auf Label auto-maintain und nur auf meine Issues | Z4 | 3 | must |
| [SEC-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/26) | Rechte und Grenzen des Agenten | Z4 | 3 | must |
| [AI-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/28) | Erstes einfaches Test-Issue als Durchstich | Z3 | 3 | must |
| [PM-9](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/32) | Besprechung 2 vorbereiten und protokollieren | PM | 1 | must |
| [PM-10](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/33) | Sprint 2 Review und Retrospektive | PM | 2 | must |
| [CI-6](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/49) | GitHub-Sicherheitsfunktionen aktivieren | Z1 | 2 | should |
| [DOC-2](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/30) | Projektdokumentation Kapitel 1 bis 3 | PM | 3 | should |
| [DOC-1](https://github.com/RuminahuiM/rdg-semesterarbeit/issues/29) | RDG-Doku auf GitHub Pages unter /rdg | Z1 | 3 | could |

**Summe Story Points:** 54 (must 46, should 5, could 3)  
**Verfügbare Kapazität:** ca. 42 h, davon ca. 33.5 h planbar (20 Prozent Reserve)

### Wie der Umfang festgelegt wurde

Sprint 1 hatte eine Velocity von 25 SP in ca. 16 h, also ca. 1.5 SP pro Stunde. Auf 33.5 h hochgerechnet ergibt das ca. 50 SP. Mit 54 SP ist Sprint 2 damit knapp, aber machbar geplant. Die Story Points bleiben der Richtwert ohne KI aus dem [Scrum-Setup](../../projekt/scrum-setup.md#schatzung), für den Umfang zählt die gemessene Velocity. Ob die Velocity aus Sprint 1 auch für technisch schwierigere Stories gilt, ist eine offene Frage für die Retro.

## 3. Umsetzungsplan

| Tag | Stories |
| --- | --- |
| Do 12.11. | PM-8 Planning, Start DEP-1 Tenant und Azure-Abo |
| Sa 14.11. | DEP-1 abschliessen, DEP-2 Bootstrap |
| So 15.11. | DEP-2 abschliessen, DEP-3 OIDC |
| Mo 16.11. | Besprechung 1, PM-14 Protokoll |
| Mi 18.11. | DEP-6 Settings in der GitHub-Umgebung, Start DEP-4 Deploy-Workflow |
| Sa 21.11. | DEP-4 abschliessen |
| So 22.11. | DEP-5 Release mit Freigabe, CI-6 Sicherheitsfunktionen |
| Mi 25.11. | AI-9 Token und Testlauf, SEC-3 Regelwerk |
| 26.11. bis 06.12. | Ferien |
| Mi 09.12. | SEC-1 Auslöser, SEC-2 Rechte und Grenzen |
| Sa 12.12. | AI-1 Durchstich, DOC-2 Kapitel 1 bis 3 |
| So 13.12. | DOC-1 (Stretch), Vorbereitung PM-9, Entwurf PM-10 |
| Mo 14.12. | Besprechung 2, PM-9 Protokoll, PM-10 Review und Retro |

`deploy-test` baut nach jedem Merge ein Paket mit einer Vorabversion und deployt es in die Testumgebung. Weil die Version beim Bauen ins Paket geschrieben wird, baut der Release-Workflow beim Tag sein Paket selbst mit der Tag-Version, deployt es zuerst in die Testumgebung und veröffentlicht nach der Freigabe genau dieses Paket (einmal bauen, mehrfach verwenden). Ersetzt oder löscht ein Plan Ressourcen, bricht `deploy-test` vor dem Apply ab.

Die Reihenfolge folgt den Abhängigkeiten: Testumgebung (DEP-1, DEP-2), dann Login (DEP-3), dann Settings in GitHub (DEP-6), dann Deployment (DEP-4) und Release (DEP-5). Der KI-Teil startet vor den Ferien mit dem Token-Test (AI-9), weil OAuth-Tokens in GitHub Actions laut Community nicht immer zuverlässig laufen. So bleibt über die Ferien Zeit für Plan B.

## 4. Risiken und Abhängigkeiten

| Risiko / Abhängigkeit | Wahrscheinlichkeit | Auswirkung | Massnahme |
| --- | --- | --- | --- |
| DEP-4 ist grösser als geschätzt, weil `Deploy-Rdg.ps1` für Azure DevOps und Release-Pakete gebaut ist (R-T03) | Mittel | Hoch | Früh starten, das Paket im Workflow bauen und mit `-BundlePath` übergeben |
| Die Ferien unterbrechen den Sprint, danach bleiben nur 4 Arbeitstage (R-S01) | Hoch | Mittel | Alles zu Z2 vor den Ferien, nach den Ferien nur die KI-Stories und der Abschluss |
| OAuth-Token des Abos funktioniert in GitHub Actions nicht zuverlässig (R-E02) | Mittel | Mittel | AI-9 vor den Ferien testen, Plan B: API-Key mit Kostenlimit |
| Test T-06 braucht ein Issue von einer anderen Person | Mittel | Niedrig | Die Prüfung ist zusätzlich mit automatischen Tests abgesichert; für den Test von Hand eröffnet eine andere Person ein Issue |
| Kosten für Azure und Exchange Online (R-E02) | Niedrig | Niedrig | Budget-Alarm im Azure-Abo (DEP-1), Kosten in der Doku |
| AI-1 braucht DEP-4 und SEC-1 bis SEC-3 | Mittel | Mittel | AI-1 als letzte technische Story, ohne Deployment notfalls nur bis zum Merge |

## 5. Bewusst nicht im Sprint

- Die eigentliche KI-Auswertung mit 8 Test-Issues (AI-2 bis AI-5) und der Prompt-Injection-Test (SEC-4): Sprint 3
- Optionale Ideen AI-6, AI-7, AI-10 und SEC-5: Sprint 3, nur falls vor dem Feature-Freeze Zeit bleibt

## 6. Reserve und Stretch

- **Stretch:** DOC-1 (could). Fehlt am Schluss Zeit, geht DOC-1 in Sprint 3.
- **Zuerst streichen, wenn es eng wird:** DOC-1, dann CI-6.
- **Reserve:** ca. 8.5 h, vor allem für DEP-4 und die Zeit nach den Ferien.

## 7. Definition-of-Ready-Check

- [x] Alle ausgewählten Stories haben eine Story und mindestens zwei Akzeptanzkriterien
- [x] Alle ausgewählten Stories sind geschätzt (Story Points im Issue)
- [x] Story Points im Board eingetragen, Stories auf ToDo (12.11.2026)
- [x] Abhängigkeiten geklärt (im Issue und im Umsetzungsplan)
- [x] Offene Findings (F-006, F-007), aktive Risiken und Massnahmen aus der Retro von Sprint 1 geprüft

### Massnahmen aus der Retro von Sprint 1

| Massnahme | Umsetzung in Sprint 2 |
| --- | --- |
| Experten zeitnah einbeziehen | Teams-Post nach Planning und Review mit beiden Experten markiert, Antwort auf Rückmeldungen innerhalb von 2 Tagen |
| Sofort starten | Umsetzung beginnt am Tag des Plannings (12.11.) |
| Neue Arbeit zuerst als Issue erfassen | Gilt ab heute, auch für Doku-Arbeit (DOC-2) |

## 8. Anpassungen nach dem Planning

| Datum | Änderung | Grund |
| --- | --- | --- |
| 12.11.2026 | Umsetzung beginnt am Tag des Plannings | Sofort starten (Retro Sprint 1) |
| 13.11.2026 | DEP-1: Testgruppen aus den AC genommen | Sie entstehen mit Schritt 7 des Install Guide in DEP-2 |
| 13.11.2026 | DEP-2: Stufe 1 mit `-LocalOnly`; neu Schritt 7 (Testgruppen, Dry-Run) und Kostenprüfung | Der Install Guide trennt den Weg ohne Pipeline (von Hand) und mit Pipeline (OIDC); OIDC gehört zu DEP-3 |
| 13.11.2026 | DEP-3: Stufe 1 mit OIDC, Subject mit echtem Token prüfen, Entscheid zu den eigenen Rechten | Folge der Anpassung von DEP-2 |
| 13.11.2026 | DEP-6 von should auf must, vor DEP-4; Settings als Variablen der GitHub-Umgebung | `deploy-test` kann ohne Settings in GitHub nicht laufen; echte Tenant-Daten gehören nicht ins öffentliche Repository |
| 13.11.2026 | DEP-4: Abbruch bei Replace oder Delete; Artefakt für das Release entfällt | Ohne Freigabe darf kein Plan unbemerkt Ressourcen ersetzen; das Release baut selbst |
| 13.11.2026 | DEP-5: Release baut einmal mit der Tag-Version, deployt in die Testumgebung, veröffentlicht nach Freigabe | Die Version steckt im Paket, ein Paket aus `deploy-test` kann nicht als Release-Version veröffentlicht werden |
| 13.11.2026 | AI-9: Testlauf nur per `workflow_dispatch` | Vor SEC-1 darf niemand anders den Agenten auslösen können |
| 13.11.2026 | CI-6: Kleine Funde direkt beheben, nur grössere als Issue | Arbeitsregel: reparieren statt Issues für Kleinigkeiten |
