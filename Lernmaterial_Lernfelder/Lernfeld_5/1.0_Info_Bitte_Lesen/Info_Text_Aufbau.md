# LF5 – Software Configuration and Data Management: Übersicht

> Diese Datei erklärt kurz, wie sich LF5 zusammensetzt und warum die Artikel aus unterschiedlichen Quellen stammen. Kein Lerninhalt, nur Orientierung.

---

## Warum die Struktur uneinheitlich aussieht

LF5 wurde **nicht komplett neu geschrieben**. Ein Teil der Unterthemen war bereits vor diesem Wiki-Projekt im Repo vorhanden (vermutlich aus einer früheren Bearbeitung), ein Teil wurde in diesem Projekt neu erstellt. Um Doppelarbeit zu vermeiden, wurde beim Start dieses Projekts zunächst der bestehende Repo-Stand gesichtet, bevor neue Artikel geschrieben wurden.

## Statusübersicht

| Unterthema | Status | Herkunft |
| --- | --- | --- |
| **LF5.1** – Requirements & Analysis | ✅ Final | Neu erstellt in diesem Projekt |
| **LF5.2** – System Design Modeling (ERM/Chen-Notation, PAP, Nassi-Shneiderman, UML Use-Case/Klasse/Sequenz) | ✅ Vorhanden | Bereits im Repo, vor diesem Projekt entstanden |
| **LF5.3** – Development Tools & Version Control (IDE/Compiler/Git, Branching-Modelle) | ✅ Vorhanden | Bereits im Repo, vor diesem Projekt entstanden |
| **LF5.4** – Writing the Logic | ✅ Final | Neu erstellt in diesem Projekt |
| **LF5.5** – Ensuring Quality | ✅ Final | Neu erstellt in diesem Projekt |
| **LF5.6 Teil A** – SDLC Frameworks (Wasserfall, V-Modell, Spiralmodell) | ✅ Vorhanden | Bereits im Repo, vor diesem Projekt entstanden ("Vorgehensmodelle_Softwareentwicklung.md") |
| **LF5.6 Teil B** – Agile Methodologies (Scrum, Kanban, XP) | ✅ Final | Neu erstellt in diesem Projekt, extern in 2 Runden geprüft |

**LF5 ist damit inhaltlich vollständig** – alle sieben Unterthemen liegen final oder in solider, bereits vor diesem Projekt geprüfter Qualität vor.

## Warum LF5.2/5.3/5.6-Teil-A nicht in diesem Projekt neu geschrieben wurden

Beim Sichten des GitHub-Repos zu Beginn der LF5-Arbeit stellte sich heraus, dass diese Themen bereits in solider, teilweise sogar als "Final" markierter Qualität vorlagen. Ein Neuschreiben hätte nur Doppelarbeit bedeutet und das Risiko widersprüchlicher Parallelversionen geschaffen. Stattdessen wurde der Fokus auf die tatsächlich fehlenden Lücken gelegt (LF5.1, LF5.4, LF5.5, LF5.6 Teil B).

## Bewusste Abgrenzung zu LF8

LF8 baut inhaltlich auf LF5 auf (nicht umgekehrt) – LF5 legt die Grundlagen (Requirements Engineering, UML-Notation, Sprachparadigmen, Python-Basics, Git, Testing), LF8 vertieft darauf aufbauend (z. B. OOP-Design-Patterns, Client-Server-Architektur). Wo sich Themen berühren (v. a. UML-Klassendiagramme, OOP-Grundlagen), verweisen die LF5-Artikel bewusst auf LF8 statt Inhalte zu duplizieren, und umgekehrt.

---

*Stand: 2026-09-16*

---

# Infoblatt: Katalog-Update 2025 – Was sich für bestehende Wiki-Artikel ändert

> **Zweck dieses Blatts:** Kurze, eigenständige Ergänzung zu Wiki-Dateien, die durch den neuen AP2-Prüfungskatalog (gültig seit Sommer 2025) fachlich überholte Prüfungsrelevanz-Aussagen enthielten. Die Originaldateien werden dadurch **nicht automatisch verändert** – dieses Blatt dient als Verweis/Anhang bzw. als Vorlage für einen späteren Einschub in die jeweilige Datei.
>
> **Stand:** 2026-09-16 – Bearbeitungsstatus der drei ursprünglich genannten Punkte siehe Tabelle unten.

---

## 1. Betrifft: `Lernfeld_5/Programmablaufplan (PAP - DIN 66001).md`

> 🔴 **Noch offen** – die Hinweisbox unten wurde bislang **nicht** in die Datei eingefügt.

**Im Text steht sinngemäß:** "...ob am Whiteboard oder in der IHK-Prüfung."

**Aktueller Stand:** Der Programmablaufplan (PAP) wurde mit dem AP2-Prüfungskatalog 2025 aus dem Katalog für Fachinformatiker Anwendungsentwicklung **gestrichen**. Für die Darstellung von Kontrollstrukturen sind seither nur noch **Pseudocode** und das **UML-Aktivitätsdiagramm** vorgesehen.

**Vorgeschlagener Einschub** (z. B. als Hinweisbox direkt unter der Überschrift):

> ⚠️ **Hinweis zum aktuellen Prüfungsstand (2025):** Der PAP wurde aus dem AP2-Prüfungskatalog für Anwendungsentwicklung gestrichen und ist **nicht mehr Bestandteil der schriftlichen Prüfung**. Als Struktur- und Verständnishilfe (z. B. zur eigenen Vorbereitung oder im Fachgespräch) bleibt er weiterhin nützlich. Für die Prüfung selbst sind **Pseudocode** und das **UML-Aktivitätsdiagramm** die relevanten Notationen – siehe *Pseudocode & Algorithmenstrukturen*.

---

## 2. Betrifft: `Lernfeld_5/Nassi_Schneider_Diagramm.md`

> 🔴 **Noch offen** – die Hinweisbox unten wurde bislang **nicht** in die Datei eingefügt.

**Aktueller Stand:** Das Struktogramm (Nassi-Shneiderman-Diagramm) wurde ebenfalls mit dem Katalog 2025 gestrichen.

**Vorgeschlagener Einschub** (analog zu PAP):

> ⚠️ **Hinweis zum aktuellen Prüfungsstand (2025):** Das Struktogramm wurde aus dem AP2-Prüfungskatalog für Anwendungsentwicklung gestrichen und ist **nicht mehr Bestandteil der schriftlichen Prüfung**. Es bleibt als didaktisches Hilfsmittel zum Verständnis von Kontrollstrukturen wertvoll, wird aber in aktuellen Prüfungsaufgaben nicht mehr verlangt. Relevant sind seither **Pseudocode** und das **UML-Aktivitätsdiagramm**.

---

## 3. Betrifft: `SQLITE/3.SQLite_in_der_IHK_Prüfung.md`

> ✅ **Erledigt** – beide Punkte (Gewichtungsaufschlüsselung und Belegsatz-Konzept) sind in der Datei bereits eingearbeitet.

Ursprünglich zwei Punkte: Die 30%-Gewichtungsangabe war unaufgeschlüsselt (jetzt in die drei AP2-Einzelbereiche à 10% aufgeschlüsselt), und das seit 2025 gültige **Belegsatz/Beiblatt-Konzept** fehlte komplett (jetzt im Abschnitt zu SQL-Dialektunterschieden ergänzt, inkl. Entschärfung der früheren "Immer MySQL-Syntax auswendig können"-Formulierung).

---

## Zusammenfassung für schnelles Nacharbeiten

| Datei | Ein-Satz-Korrektur | Status |
|---|---|---|
| `Programmablaufplan (PAP...).md` | PAP seit 2025 nicht mehr Prüfungsstoff – Hinweisbox ergänzen | 🔴 Noch offen |
| `Nassi_Schneider_Diagramm.md` | Struktogramm seit 2025 nicht mehr Prüfungsstoff – Hinweisbox ergänzen | 🔴 Noch offen |
| `SQLITE/3.SQLite_in_der_IHK_Prüfung.md` | 30%-Angabe aufschlüsseln + Belegsatz-Konzept ergänzen | ✅ Erledigt |
| `SQLITE/5.SQLite_Cheat_Sheet.md` | Gleicher Belegsatz-Blindspot wie Punkt 3, dort ebenfalls ergänzt | ✅ Erledigt |

Die beiden noch offenen Änderungen sind reine **Ergänzungen/Hinweisboxen**, keine Umschreibung der bestehenden Inhalte – die didaktische Substanz der Originaldateien bleibt vollständig erhalten.