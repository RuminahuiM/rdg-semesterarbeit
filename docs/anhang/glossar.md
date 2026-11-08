# Glossar

Alphabetisch sortiert, wird laufend ergänzt.

| Begriff | Erklärung |
| --- | --- |
| ADR | Architecture Decision Record: kurze Dokumentation einer Architekturentscheidung mit Kontext, Optionen, Entscheidung und Folgen |
| Agent (KI-Agent) | Sprachmodell, das in mehreren Schritten Werkzeuge benutzt, z.B. Code ändert, Tests ausführt und einen Pull Request erstellt |
| Akzeptanzkriterien | Prüfbare Bedingungen, die eine einzelne Story erfüllen muss |
| auto-maintain | Label, mit dem ich ein Issue an den KI-Agenten übergebe |
| Branch-Schutz | Regel auf GitHub, die direkte Pushes auf `main` verhindert und für einen Merge eine grüne CI verlangt |
| CI/CD | Continuous Integration und Continuous Delivery: Änderungen werden automatisch getestet, gebaut und ausgeliefert |
| Conventional Commits | Feste Form für Commit-Nachrichten, z.B. `feat: ...` oder `fix: ...` |
| Definition of Done (DoD) | Qualitäts-Checkliste, die für alle Stories gilt |
| Definition of Ready (DoR) | Bedingungen, damit eine Story in einen Sprint aufgenommen werden kann |
| Dynamische Gruppe | Gruppe in Microsoft Entra ID, deren Mitglieder automatisch nach einer Regel bestimmt werden |
| Excessive Agency | Risiko, dass ein KI-System mehr Rechte hat als nötig und dadurch Schaden anrichten kann (OWASP LLM06) |
| Feature-Freeze | Zeitpunkt, ab dem keine neuen Funktionen mehr umgesetzt werden |
| GitHub Actions | Automatisierung von GitHub, mit der Workflows bei Ereignissen wie Push, Pull Request oder Issue laufen |
| GitHub Flow | Branching-Strategie: kurzer Branch pro Änderung, Pull Request, Merge auf `main` |
| Human in the Loop | Ein Mensch prüft und entscheidet an festen Stellen eines automatischen Ablaufs |
| Increment | Summe der fertigen Stories eines Sprints, potenziell auslieferbar |
| Least Privilege | Prinzip, dass jede Komponente nur die Rechte bekommt, die sie wirklich braucht |
| MVP, MLP, MMP | Minimum Viable, Lovable und Marketable Product: Releases am Ende der drei Sprints |
| OIDC (OpenID Connect) | Verfahren, mit dem sich ein Workflow ohne gespeichertes Passwort ein kurzlebiges Token holt |
| OpenTofu | Open-Source-Werkzeug für Infrastructure as Code, Abspaltung von Terraform |
| Prompt Injection | Versteckte Anweisung in einem Text (z.B. in einem Issue), die eine KI zu einer ungewollten Aktion bringen soll |
| Pull Request | Vorschlag, Änderungen aus einem Branch in `main` zu übernehmen, mit Prüfung vor dem Merge |
| RDG | Real Dynamic Groups: das Tool, um das es in dieser Arbeit geht |
| SemVer | Semantic Versioning: Versionsnummern der Form MAJOR.MINOR.PATCH |
| Smoke-Test | Kurzer Test nach einem Deployment, ob die wichtigsten Teile laufen |
| Sprint | Feste Zeitbox, in der ein Increment entsteht |
| Test-Tenant | Eigene Microsoft-365-Umgebung nur für Tests, ohne produktive Daten |
