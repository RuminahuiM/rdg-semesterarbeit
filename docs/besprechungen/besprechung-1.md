# Besprechung 1

**Datum:** 16.11.2026  
**Kontext:** nach Sprint 1 (abgeschlossen am 12.11.), zu Beginn von Sprint 2  
**Teilnehmende:** Dodoe Rumiñahui Mannale, Corrado Parisi (Experte Projektmanagement), Thanam Pangri (Experte DevOps)

!!! info "Vorbereitung vom 12.11.2026, Protokoll folgt nach dem Termin (PM-14)"

**Schwerpunkt:** Ich möchte vor allem die Dokumentation besprechen: Struktur, Vollständigkeit und Abgabeform.

## 1. Vorbereitung

### 1.1 Was ist seit der letzten Besprechung erledigt?

Sprint 1 ist abgeschlossen, alle 25 Story Points sind erledigt und Z1 ist nachgewiesen ([Review](../sprints/sprint-1/review.md)):

- Doku-Repository mit Website, Kanban-Board und Product Backlog
- Einreichungsformular Version 2, freigegeben am 09.11.
- RDG-Repository mit MIT-Lizenz, Arbeitsregeln (GitHub Flow, Conventional Commits, SemVer) und ADR 0001 bis 0003
- CI-Pipeline repariert: Alle 6 Jobs laufen grün, vorher waren 4 rot
- Ruleset auf `main`: Ein absichtlich fehlerhafter Pull Request wird blockiert (T-01)

### 1.2 Was läuft gerade?

Sprint 2 hat am 12.11. begonnen (bis 14.12.): Test-Tenant, automatisches Deployment mit GitHub Actions und OIDC, Release mit Freigabe von Hand (Z2) und eine erste KI-Pipeline mit Sicherheitsregeln (Z4). Das Sprint 2 Planning folgt.

### 1.3 Fragen an den Fachexperten

1. Passt die Tiefe der Theorie in [Kapitel 7](../projektdokumentation.md#7-fachlicher-kontext-und-theorie), oder fehlt ein Thema aus dem DevOps-Unterricht?
2. Ich möchte den KI-Agenten über mein Claude-Abo statt über die API betreiben (AI-9), damit keine zusätzlichen Kosten entstehen. Ist das für die Arbeit in Ordnung?

### 1.4 Fragen an den Experten Projektmanagement

1. **Struktur:** Der Bericht ist eine Datei ([Projektdokumentation](../projektdokumentation.md), Teil A und Teil B), dazu kommen Detailseiten für Sprints, Besprechungen, Register und Nachweise. Passt diese Aufteilung?
2. **Abgabeform:** Reicht der Link zur Doku und zu den Repositories? Oder soll ich eine einzelne Datei abgeben, entweder die Projektdokumentation oder das Gesamtdokument mit allen Seiten (PDF und Markdown)?
3. **Fehlt etwas** aus Sicht der Bewertung? Und gibt es Stellen mit zu viel oder doppeltem Inhalt?
4. **Definition of Done:** Ein Peer Review durch eine zweite Person gibt es im Solo-Projekt nicht. Reichen Review durch mich, grüne CI und Branch-Schutz?

### 1.5 Wichtige Entscheidungen zur Diskussion

- Sprint 1 vorzeitig abgeschlossen, Sprint 2 ab 12.11.
- Abgabeform der Dokumentation (siehe 1.4)
- Betrieb des KI-Agenten über das Claude-Abo (siehe 1.3)

### 1.6 Aktuelle Risiken

| Risiko | Score | Stand |
| --- | --- | --- |
| R-S01 Zu wenig Zeit (Ferien mitten in Sprint 2) | 6 | gesenkt nach Sprint 1 |
| R-K01 Der KI-Teil ist schwieriger als gedacht | 6 | unverändert |
| R-E01 Test-Tenant nicht rechtzeitig verfügbar | 6 | Einrichtung zu Beginn von Sprint 2 |

### 1.7 Demo-Plan (ca. 5 Minuten)

| Schritt | Was ich zeige | Dauer |
| --- | --- | --- |
| 1 | Doku: Startseite, Projektdokumentation, Sprint 1 Review | 2 min |
| 2 | Board: Sprint 1 Done, Backlog für Sprint 2 und 3 | 1 min |
| 3 | RDG-Repository: CI grün auf `main`, blockierter Pull Request #17 | 1.5 min |
| 4 | Gesamtdokument als PDF | 0.5 min |

## 2. Feedback Fachexperte

## 3. Feedback Experte Projektmanagement

## 4. Action Items

| Aktion | Wer | Bis | Status | Issue |
| --- | --- | --- | --- | --- |

## 5. Nachbereitung

- [ ] Action Items im Backlog
- [ ] Erkenntnisse in der nächsten Retro
- [ ] Betroffene Dokumente angepasst
