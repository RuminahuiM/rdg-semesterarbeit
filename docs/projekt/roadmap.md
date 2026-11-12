# Roadmap

Die Roadmap folgt den Releases MVP, MLP und MMP, wie es die TBZ für Semesterarbeiten empfiehlt. Jeder Sprint endet mit einem Release, danach folgen Review und Retrospektive.

| Release | Ende | Was der Release bringt |
| --- | --- | --- |
| MVP | Sprint 1, 12.11.2026 (geplant 16.11.) | RDG liegt sauber auf GitHub, Board steht, Branch-Schutz aktiv, CI-Pipeline läuft grün (Z1) |
| MLP | Sprint 2, 14.12.2026 | Jeder Merge deployt automatisch in die Testumgebung, Release nur nach Freigabe (Z2). Erste KI-Pipeline mit Sicherheitsregeln (Z4) |
| MMP | Sprint 3, 22.01.2027 | KI-Pipeline für vier Issue-Arten, 8 Test-Issues ausgewertet, Prompt-Injection-Test (Z3, Z4) |

## Zeitplan

```mermaid
---
config:
  themeCSS: |
    .mermaid-main-font, text { font-family: var(--md-text-font-family, sans-serif); }
    .titleText { fill: var(--md-default-fg-color); font-size: 17px; font-weight: 700; }
    .sectionTitle { fill: var(--md-default-fg-color--light); font-weight: 700; }
    .section, .section1, .section3 { opacity: 1; }
    .section0, .section2 { fill: var(--md-default-fg-color--lightest); }
    .section1, .section3 { fill: transparent; }
    .grid .tick { opacity: 1; }
    .grid .tick line { stroke: var(--md-default-fg-color--lighter); stroke-opacity: .5; }
    .grid .tick text { fill: var(--md-default-fg-color--light); stroke: none; font-size: 12px; }
    .today { stroke: var(--gantt-today, #6a2c91); stroke-width: 2px; stroke-dasharray: 6 4; }
    .task0, .task1, .task2, .task3 { fill: var(--gantt-task, #e3a400); stroke: var(--gantt-task, #e3a400); }
    .taskText0, .taskText1, .taskText2, .taskText3 { fill: #1a1a1a; font-weight: 600; }
    .taskTextOutsideLeft, .taskTextOutsideRight, .taskTextOutside0, .taskTextOutside1, .taskTextOutside2, .taskTextOutside3 { fill: var(--md-default-fg-color); }
    .milestone { fill: var(--gantt-milestone, #6a2c91); stroke: var(--gantt-milestone, #6a2c91); }
    .milestoneText { font-style: normal; }
    .done0, .done1, .done2, .done3 { fill: var(--md-default-fg-color--lightest); stroke: var(--md-default-fg-color--light); stroke-width: 1; }
    .doneText0, .doneText1, .doneText2, .doneText3, .doneText0.taskTextOutsideRight, .doneText1.taskTextOutsideRight, .doneText2.taskTextOutsideRight, .doneText3.taskTextOutsideRight { fill: var(--md-default-fg-color) !important; }
    .crit0, .crit1, .crit2, .crit3 { fill: var(--gantt-crit, #c8382f); stroke: var(--gantt-crit, #c8382f); }
    .critText0, .critText1, .critText2, .critText3 { fill: var(--md-default-fg-color) !important; font-weight: 600; }
---
gantt
    title Semesterarbeit 4: RDG
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m.
    tickInterval 2week
    weekday monday
    section Sprints
    Sprint 1 (Z1)                  :s1, 2026-10-26, 2026-11-12
    Sprint 2 (Z2, Z4)              :s2, 2026-11-12, 2026-12-14
    Sprint 3 (Z3, Z4)              :s3, 2026-12-15, 2027-01-22
    Abschluss und Abgabe           :s4, 2027-01-23, 2027-01-27
    section Releases
    MVP                            :milestone, m1, 2026-11-12, 0d
    MLP                            :milestone, m2, 2026-12-14, 0d
    MMP                            :milestone, m3, 2027-01-22, 0d
    section Absenzen
    Ferien                         :done, f1, 2026-11-26, 2026-12-06
    Weihnachten                    :done, f2, 2026-12-24, 2026-12-26
    Neujahr                        :done, f3, 2026-12-31, 2027-01-02
    section Termine
    Besprechung 1                  :milestone, b1, 2026-11-16, 0d
    Besprechung 2                  :milestone, b2, 2026-12-14, 0d
    Feature-Freeze                 :crit, milestone, ff, 2027-01-09, 0d
    Besprechung 3                  :milestone, b3, 2027-01-22, 0d
    Abgabe und Präsentation        :crit, milestone, ab, 2027-01-27, 0d
```

## Feature-Freeze

Ab dem 09.01.2027 kommen keine neuen Funktionen mehr dazu. Die Zeit bis zur Abgabe ist für Tests, Fehlerbehebung, Auswertung und Dokumentation reserviert.
