# Roadmap

Die Roadmap folgt den Releases MVP, MLP und MMP, wie es die TBZ für Semesterarbeiten empfiehlt. Jeder Sprint endet mit einem Release, danach folgen Review und Retrospektive.

| Release | Ende | Was der Release bringt |
| --- | --- | --- |
| MVP | Sprint 1, 16.11.2026 | RDG liegt sauber auf GitHub, Board steht, Branch-Schutz aktiv, CI-Pipeline läuft grün (Z1) |
| MLP | Sprint 2, 14.12.2026 | Jeder Merge deployt automatisch in die Testumgebung, Release nur nach Freigabe (Z2). Erste KI-Pipeline mit Sicherheitsregeln (Z4) |
| MMP | Sprint 3, 22.01.2027 | KI-Pipeline für vier Issue-Arten, 8 Test-Issues ausgewertet, Prompt-Injection-Test (Z3, Z4) |

## Zeitplan

```mermaid
gantt
    title Semesterarbeit 4: RDG
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m.
    section Sprints
    Sprint 1 (Z1)                  :s1, 2026-10-26, 2026-11-16
    Sprint 2 (Z2, Z4)              :s2, 2026-11-17, 2026-12-14
    Sprint 3 (Z3, Z4)              :s3, 2026-12-15, 2027-01-22
    Abschluss und Abgabe           :s4, 2027-01-23, 2027-01-27
    section Releases
    MVP                            :milestone, m1, 2026-11-16, 0d
    MLP                            :milestone, m2, 2026-12-14, 0d
    MMP                            :milestone, m3, 2027-01-22, 0d
    section Termine
    Besprechung 1                  :milestone, b1, 2026-11-16, 0d
    Besprechung 2                  :milestone, b2, 2026-12-14, 0d
    Feature-Freeze                 :crit, milestone, ff, 2027-01-09, 0d
    Besprechung 3                  :milestone, b3, 2027-01-22, 0d
    Abgabe und Präsentation        :crit, milestone, ab, 2027-01-27, 0d
```

## Feature-Freeze

Ab dem 09.01.2027 kommen keine neuen Funktionen mehr dazu. Die Zeit bis zur Abgabe ist für Tests, Fehlerbehebung, Auswertung und Dokumentation reserviert.
