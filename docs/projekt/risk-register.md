# Risk Register

## Methodik

- **Kategorien:** Technisch (T), Termin (S), Wissen (K), Extern (E), Persönlich (P)
- **Bewertung:** Wahrscheinlichkeit und Auswirkung je Niedrig (1), Mittel (2), Hoch (3), Score = Produkt
- **Reaktion:** pro Risiko eine Massnahme (vorbeugend) und ein Plan B (wenn es eintritt)
- **Review:** in jedem Sprint Review und vor jeder Besprechung

| Wahrscheinlichkeit \ Auswirkung | Niedrig | Mittel | Hoch |
| --- | --- | --- | --- |
| **Niedrig** | 1 | 2 | 3 |
| **Mittel** | 2 | 4 | 6 |
| **Hoch** | 3 | 6 | 9 |

Ab Score 4 wird das Risiko aktiv beobachtet, ab Score 6 hat es hohe Priorität.

## Risiko-Matrix

| ID | Risiko | Kat. | Wahrsch. | Auswirkung | Score | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R-T01 | Die KI macht falsche Änderungen | T | Hoch | Mittel | 6 | aktiv |
| R-T02 | Missbrauch über Issue-Texte (Prompt Injection) oder zu viele Rechte für den Agenten | T | Mittel | Hoch | 6 | aktiv |
| R-T03 | Die bestehenden Pipelines laufen nicht und brauchen mehr Arbeit als gedacht | T | Mittel | Mittel | 4 | aktiv |
| R-K01 | Der KI-Teil ist schwieriger als gedacht | K | Mittel | Hoch | 6 | aktiv |
| R-E01 | Testumgebung oder Test-Tenant nicht rechtzeitig verfügbar | E | Mittel | Hoch | 6 | aktiv |
| R-E02 | Die Kosten für die KI steigen | E | Niedrig | Mittel | 2 | beobachten |
| R-S01 | Zu wenig Zeit, Sprints laufen über (besonders Sprint 2, Ferien 26.11. bis 06.12.) | S | Hoch | Hoch | 9 | aktiv |
| R-S02 | Zu wenig Zeit für Doku und Auswertung am Schluss | S | Mittel | Hoch | 6 | aktiv |
| R-P01 | Berufliche oder private Belastung, Ausfall | P | Mittel | Mittel | 4 | aktiv |

## Details

### R-T01: Die KI macht falsche Änderungen

- **Massnahme:** Alle Änderungen laufen durch Tests und die CI-Pipeline. Ich prüfe jeden Pull Request vor dem Merge und teste jede Version vor dem Release.
- **Plan B:** Pull Request schliessen, Issue als "nicht gelöst" auswerten.

### R-T02: Prompt Injection oder zu viele Rechte

- **Massnahme:** Die Pipeline reagiert nur auf meine Issues. Der Agent bekommt nur die nötigsten Rechte, kann nicht auf `main` pushen und hat keinen Zugriff auf Azure und die Umgebungen. Ein eigener Test-Issue prüft das (Z4).
- **Plan B:** Pipeline sofort deaktivieren, Rechte prüfen, Vorfall dokumentieren.

### R-T03: Die bestehenden Pipelines brauchen mehr Arbeit

- **Massnahme:** CI-Pipeline als erste Story in Sprint 1. Fehler früh sichtbar machen.
- **Plan B:** Nicht nötige Prüfungen vorerst als "nicht blockierend" markieren und als Finding nachziehen.

### R-K01: Der KI-Teil ist schwieriger als gedacht

- **Massnahme:** Z1 und Z2 haben Vorrang. Der KI-Versuch ist auf vier Issue-Arten begrenzt und beginnt mit einfachen Issues.
- **Plan B:** Weniger Test-Issues, dafür sauber ausgewertet. Eine bestimmte Erfolgsquote ist kein Ziel.

### R-E01: Testumgebung oder Test-Tenant nicht verfügbar

- **Massnahme:** Test-Tenant und Azure-Abo zu Beginn von Sprint 2 einrichten.
- **Plan B:** Tests nur mit den vorhandenen Mocks, Deployment-Teil als Grenze dokumentieren.

### R-E02: Die Kosten für die KI steigen

- **Massnahme:** Limit pro Durchlauf, Kosten pro Issue aufschreiben.
- **Plan B:** Weniger Durchläufe, günstigeres Modell für einfache Issues.

### R-S01 und R-S02: Zu wenig Zeit

- **Massnahme:** Feature-Freeze am 09.01.2027. Doku und Auswertung laufend in jedem Sprint. 20 Prozent Reserve pro Sprint. Sprint 2 hat wegen der Ferien nur ca. 22 h planbare Zeit: Umfang im Sprint 2 Planning bewusst klein halten, die KI-Stories (SEC, AI-1) notfalls an den Anfang von Sprint 3 schieben.
- **Plan B:** Should- und Could-Stories streichen, Fokus auf die Must-Ziele.

### R-P01: Berufliche oder private Belastung

- **Massnahme:** Realistischer Arbeitsrhythmus, Puffer vor der Abgabe.
- **Plan B:** Umfang reduzieren und früh mit den Experten sprechen.

## Historie

| Datum | Änderung |
| --- | --- |
| 07.11.2026 | Risk Register aus den Risiken im Einreichungsformular aufgebaut und ergänzt |
| 08.11.2026 | R-S01 von 6 auf 9 erhöht: Ferien vom 26.11. bis 06.12. verkürzen Sprint 2 deutlich |
