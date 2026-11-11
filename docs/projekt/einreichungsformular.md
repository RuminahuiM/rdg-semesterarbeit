# Einreichungsformular

| | |
| :--- | :--- |
| Name | Mannale Dodoe |
| Titel | RDG als DevOps-Projekt mit KI-Wartung: Eine Pipeline, die GitHub-Issues selbst löst |
| Themenfelder | Projektmanagement (Pflicht), DevOps |

## Versionen

| Version | Datum | Inhalt |
| --- | --- | --- |
| 1 | 21.10.2026 | Erste Einreichung im Teams-Kanal |
| 2 | 07.11.2026 | Im Teams-Thread an Corrado Parisi gesendet, am 09.11.2026 freigegeben. Überarbeitet nach dem Feedback des PM-Experten: Mindestumfang CI/CD, KI-Wartung als Versuch mit Auswertung, Kubernetes-Ausnahme, Ablauf vom Pull Request bis zum Release, Feature-Freeze, laufende Dokumentation |

Unten steht der Text der Version 2.

### Problemstellung / Ausgangslage / Potential der Semesterarbeit

**Hintergrund:** In Microsoft 365 gibt es dynamische Gruppen, die ihre Mitglieder automatisch nach Regeln füllen (z. B. alle Benutzer einer Abteilung). In der Praxis reichen sie oft nicht: Viele Funktionen akzeptieren keine dynamischen Gruppen (z. B. mail-aktivierte Gruppen, Verteilerlisten oder gewisse Defender- und Exchange-Richtlinien), man kann Regel und manuelle Ausnahmen nicht mischen und die Regel-Möglichkeiten sind begrenzt. Darum habe ich bei meiner Arbeit (HEKS) das Tool RDG (Real Dynamic Groups) gebaut. RDG wertet die Regeln selbst aus und schreibt das Resultat als normale Mitgliederliste in die Gruppe. So funktionieren die Gruppen auch dort, wo Microsoft dynamische Gruppen ablehnt.

**Ausgangslage:** RDG ist bisher ein MVP. Es läuft in Azure (PowerShell, kleine Web-App, Infrastruktur mit OpenTofu) und wird bei HEKS getestet. Das Projekt liegt aber nur in einem Ordner. Es wurde halb von Hand eingerichtet, die Pipelines sind zwar angelegt, aber nie richtig getestet worden, und das Deployment mache ich von Hand von meinem PC aus. Dazu kommt: Ich werde die Firma voraussichtlich bald verlassen, und danach gibt es niemanden, der RDG weiterpflegt. Ohne Wartung kann die Firma das Tool wahrscheinlich nicht weiter einsetzen, was schade wäre.

**Problemstellung:** Ich möchte RDG darum als Open-Source-Projekt veröffentlichen, das möglichst wenig Wartung von Hand braucht. Zuerst setze ich es sauber als DevOps-Projekt auf: mit Tests, automatischem Deployment in eine Testumgebung und einer Freigabe von Hand für jedes Release. Danach probiere ich aus, wie gut eine KI bei der Wartung helfen kann: Wenn ich auf GitHub ein Issue erfasse (z. B. einen kleinen Bug), soll ein KI-Agent (Claude) den Code ändern, Tests ergänzen und einen Pull Request eröffnen. Ich prüfe jeden Pull Request, bevor er gemergt wird, und teste die neue Version, bevor ich sie freigebe.

**Potential:** Wenn das klappt, kann RDG auch ohne mich weiterleben und von HEKS und anderen Firmen genutzt werden. Weil RDG ein kleines und klar abgegrenztes Tool ist, eignet es sich gut, um auszuprobieren, was KI-gestützte Wartung heute schon kann und wo sie an ihre Grenzen kommt. Gleichzeitig wende ich die Inhalte aus dem DevOps-Unterricht (Git, CI/CD, Tests, Deployment, Monitoring) an einem echten Projekt an.

**Kubernetes:** Für diese Arbeit darf ich ausnahmsweise ohne Kubernetes arbeiten (abgesprochen mit Thanam Pangri und Marcel Bernet am 21.10.2026), weil Kubernetes bei RDG keinen echten Nutzen hätte. Kubernetes baue ich dafür in meine 5. Semesterarbeit ein.

## Zielsetzung der Semesterarbeit

Das Wichtigste sind Z1, Z2 und Z4: eine funktionierende CI/CD-Pipeline mit Tests, automatischem Deployment in die Testumgebung und einer Release-Freigabe von Hand. Z3 ist ein Versuch: Ich will herausfinden und aufschreiben, was die KI schafft und was nicht.

**Z1 – Sauberes DevOps-Projekt:** RDG liegt in einem GitHub-Repository mit dokumentierter Branching-Strategie, einem Kanban-Board mit User Stories und Versionen nach SemVer. Auf main kann nur per Pull Request gemergt werden, und nur wenn die CI-Pipeline grün ist. Nachweis: Ein absichtlich fehlerhafter Pull Request wird blockiert.

**Z2 – Automatisches Deployment und Freigabe:** Jeder Merge auf main baut automatisch ein Release-Paket und deployt es ohne Handarbeit in die Testumgebung, inklusive Smoke-Test. Ich deploye nicht mehr von meinem PC aus. Ein Release gibt es erst, wenn ich die Version in der Testumgebung getestet und in der Pipeline von Hand freigegeben habe. Nachweis: mindestens 5 erfolgreiche automatische Deployments in die Testumgebung und ein Release, das erst nach meiner Freigabe erstellt wurde.

**Z3 – KI-Wartung als Versuch:** Die KI bekommt nur vier Arten von Issues: kleine Bugs, die man klar nachstellen kann, fehlende Tests, Fehler in der Dokumentation und Updates von Abhängigkeiten, welche die CI-Pipeline kaputt machen. Wenn ich ein Issue mit dem Label "auto-maintain" erfasse, erstellt ein KI-Agent einen Branch, ändert den Code, ergänzt Tests und eröffnet einen Pull Request. Ich bereite 8 Test-Issues vor (2 pro Art) und schreibe bei jedem auf: Hat es geklappt (ganz, teilweise oder gar nicht)? Wie viel Zeit musste ich selbst noch investieren? Wie lange hat es gedauert und was hat es gekostet? Nachweis: eine Auswertung der 8 Issues, die zeigt, was die KI gut kann, wo sie scheitert und wie viel Arbeit für mich bleibt. Auch wenn die KI wenig schafft, ist das ein gültiges Ergebnis.

**Z4 – Die KI bleibt eingeschränkt:** Der KI-Agent kann nicht direkt auf main pushen, hat keinen Zugriff auf Azure und die Umgebungen und reagiert nur auf Issues von mir. Nachweis: Ein Test-Issue mit einer versteckten falschen Anweisung (Prompt Injection) führt zu keiner unerlaubten Aktion.

**Optional, falls Zeit bleibt:** weitere Arten von Issues (z. B. kleine Erweiterungen), Issues automatisch aus Fehlern im Betrieb erstellen, ein KI-Helfer für Admins in der Web-App.

## Ablauf von der Änderung bis zum Release

So läuft jede Änderung ab, egal ob sie von der KI oder von mir kommt:

1.  Ich erfasse ein Issue. Hat es das Label "auto-maintain", startet der KI-Agent.

2.  Der Agent erstellt einen Branch, ändert Code und Tests und eröffnet einen Pull Request.

3.  Die CI-Pipeline testet den Pull Request. Ist sie rot, kann nicht gemergt werden.

4.  Ich schaue mir den Pull Request an und merge ihn erst, wenn er für mich in Ordnung ist.

5.  Nach dem Merge auf main wird automatisch in die Testumgebung deployt (mit Smoke-Test).

6.  Ich teste die neue Version in der Testumgebung.

7.  Erst dann gebe ich das Release in der Pipeline von Hand frei.

Ich prüfe also zweimal: den Code vor dem Merge und die fertige Version vor dem Release.

## Terminplan mit den wesentlichen Arbeitsschritten

**Sprint 1 (26.10. – 16.11.2026):** Planung, Backlog und Kanban-Board, die zwei Repositories aufsetzen (RDG und Doku der Semesterarbeit), Branch-Schutz, bestehende CI-Pipeline reparieren und testen (Z1). Besprechung 1.

**Sprint 2 (17.11. – 14.12.2026):** Test-Tenant einrichten, automatisches Deployment in die Testumgebung und Release mit Freigabe (Z2). Erste einfache Version der KI-Pipeline mit den Sicherheitsregeln (Z4). Besprechung 2.

**Sprint 3 (15.12.2026 – 22.01.2027):** KI-Pipeline fertig bauen, die 8 Test-Issues und den Prompt-Injection-Test durchspielen und auswerten (Z3, Z4). Besprechung 3.

**Feature-Freeze am 09.01.2027:** Ab dann baue ich keine neuen Funktionen mehr. Die restliche Zeit ist für Tests, Fehlerbehebung, Auswertung und Dokumentation reserviert.

**23.01. – 27.01.2027:** Reflexion, Schlusspräsentation und Abgabe.

**Dokumentation:** Ich dokumentiere laufend in jedem Sprint und nicht erst am Schluss. Die KI-Issues werte ich direkt nach jedem Durchlauf aus.

## Sachmittel / Rahmenbedingungen

Mein Laptop (Windows) und meine Arbeitszeit ausserhalb des Unterrichts.

GitHub: Repository und GitHub Actions (Pipelines).

Für das Projektmanagement GitHub Projects. Die Doku der Semesterarbeit liegt in einem privaten GitHub-Repository, auf das die Experten jederzeit Zugriff haben.

Ein Azure-Abo für die Testumgebung von RDG (Kosten ca. 27 USD pro Monat) und ein Test-Tenant für Microsoft 365, damit keine produktiven Daten angefasst werden.

Zugang zu Claude (Modell Opus) für den KI-Agenten, mit einem Kostenlimit.

## Vorgaben, Methoden und Werkzeuge

**Vorgehen:** agil in 3 Sprints, Kanban-Board mit User Stories in GitHub Projects, Besprechungen mit den Experten nach jedem Sprint.

**Git:** GitHub Flow, Conventional Commits, Versionen nach SemVer.

**Werkzeuge:** GitHub Actions (CI/CD), OpenTofu (Infrastruktur), Pester und PSScriptAnalyzer (PowerShell-Tests), Vitest und ESLint (Tests und Code-Prüfung der Web-App), Trivy (Sicherheits-Scan), Claude Code in GitHub Actions (KI-Agent).

**Vorgaben:** Keine Passwörter oder echten Firmendaten im Repository. Die KI arbeitet nur über Pull Requests, und ich prüfe jeden Pull Request vor dem Merge. Ein Release gibt es nur nach meinem Test und meiner Freigabe.

## Risiken

**KI macht falsche Änderungen (hoch):** Alle Änderungen laufen durch Tests und die Pipeline. Ich prüfe jeden Pull Request vor dem Merge und teste jede Version vor dem Release.

**Zu wenig Zeit, der KI-Teil ist schwieriger als gedacht (mittel):** Zuerst Z1 und Z2 fertig machen, dann die KI-Pipeline Schritt für Schritt aufbauen und mit einfachen Issues beginnen. Ab dem Feature-Freeze am 09.01.2027 kommen keine neuen Funktionen mehr dazu.

**Die KI löst nur wenige Issues (mittel):** Das ist für die Arbeit kein Problem, weil ich das Ergebnis auswerte. Auch was nicht klappt, schreibe ich auf.

**Missbrauch über Issue-Texte oder zu viele Rechte (mittel):** Die Pipeline reagiert nur auf meine Issues, der Agent bekommt nur die nötigsten Rechte und hat keinen Zugriff auf Azure und die Umgebungen.

**Kosten für die KI steigen (niedrig):** Limit pro Durchlauf festlegen und die Kosten pro Issue aufschreiben.

**Testumgebung oder Test-Tenant nicht verfügbar (mittel):** Das kläre ich in Sprint 1. Notfalls laufen die Tests nur mit den vorhandenen Mocks.
