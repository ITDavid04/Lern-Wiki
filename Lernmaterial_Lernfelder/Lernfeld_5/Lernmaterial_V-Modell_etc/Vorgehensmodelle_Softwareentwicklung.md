# Vorgehensmodelle der Softwareentwicklung: Wasserfall, V-Modell, Spiralmodell

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 35–45 Minuten
> **Status:** Final
> **Stand:** 2026

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie ist das Wasserfall-Modell aufgebaut und wann setzt man es ein? | [→ 1. Wasserfall-Modell](#1-wasserfall-modell) |
| 2 | Was unterscheidet das V-Modell vom reinen Wasserfall-Modell? | [→ 2. V-Modell](#2-v-modell) |
| 3 | Wie funktioniert das Spiralmodell und wofür steht die Spirale konkret? | [→ 3. Spiralmodell](#3-spiralmodell) |
| 4 | Woran scheitern diese drei Modelle in der Praxis typischerweise? | [→ 4. Scheitern in der Praxis](#4-woran-scheitern-die-modelle-in-der-praxis) |
| 5 | Nach welchen Kriterien wählt man das passende Vorgehensmodell aus? | [→ 5. Modellauswahl](#5-die-richtige-auswahl-eines-vorgehensmodells) |

---

## 1. Wasserfall-Modell

> Jede Phase wird vollständig abgeschlossen, bevor die nächste beginnt – es gibt keinen geplanten Rücksprung.

Das Wasserfall-Modell ist das älteste klassische Vorgehensmodell (Winston W. Royce, 1970) und arbeitet strikt **sequenziell**: Anforderungsanalyse → Entwurf → Implementierung → Test → Einführung → Wartung. Jede Phase liefert ein Dokument oder Artefakt als Übergabe an die nächste Phase.

### 1.1 Aufbau

| Phase | Inhalt | IHK-Relevanz |
|---|---|---|
| **Anforderungsanalyse** | Lastenheft/Pflichtenheft, vollständige Spezifikation | 🔴 Prüfungsstoff |
| **Entwurf (Design)** | Architektur, Datenmodell, Schnittstellen | 🔴 Prüfungsstoff |
| **Implementierung** | Codierung gemäß Entwurf | 🟡 Kontextwissen |
| **Test** | Verifikation gegen Spezifikation | 🔴 Prüfungsstoff |
| **Einführung** | Abnahme, Rollout | 🟡 Kontextwissen |
| **Wartung** | Fehlerbehebung, Pflege | 🟢 Nice to know |

### 1.2 Eigenschaften

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| **Rücksprünge** | Theoretisch keine vorgesehen – Korrekturen sind teuer | 🔴 Prüfungsstoff |
| **Dokumentation** | Sehr hoch, jede Phase erzeugt verbindliche Dokumente | 🔴 Prüfungsstoff |
| **Kundenbeteiligung** | Nur am Anfang (Anforderungen) und am Ende (Abnahme) | 🟡 Kontextwissen |
| **Planbarkeit** | Hoch – Termine, Kosten und Umfang früh festlegbar | 🔴 Prüfungsstoff |
| **Flexibilität** | Sehr gering | 🔴 Prüfungsstoff |

### 1.3 Wofür geeignet

Geeignet für Projekte mit **stabilen, vollständig bekannten Anforderungen**, geringem Innovationsgrad und hohem regulatorischem Dokumentationsbedarf – etwa Behördensoftware mit festem Lastenheft oder eingebettete Systeme mit fixer Hardware-Schnittstelle.

> **IHK-Typfrage:** *„Für welche Art von Projekt ist das Wasserfall-Modell geeignet?"*
> Für Projekte mit klar definierten, sich nicht ändernden Anforderungen, hohem Dokumentationsbedarf (z. B. Behörden, sicherheitskritische Systeme) und geringer Notwendigkeit für Kundenfeedback während der Entwicklung.

---

## 2. V-Modell

> Jeder Entwicklungsphase wird eine spiegelbildliche Testphase zugeordnet – das „V" verbindet Erstellung und Prüfung.

Das V-Modell erweitert das Wasserfall-Prinzip um den **Verifikations- und Validierungsgedanken**: Zu jeder Phase auf dem absteigenden Ast (Spezifikation) existiert eine korrespondierende Phase auf dem aufsteigenden Ast (Test), die genau diese Spezifikation prüft. In Deutschland ist das **V-Modell XT** der verbindliche Entwicklungsstandard für IT-Projekte der öffentlichen Hand.

### 2.1 Die V-Struktur

```
Anforderungsanalyse ─────────────────────────── Abnahmetest
        \                                          /
   Systementwurf ──────────────────────── Systemtest
              \                              /
        Systemarchitektur ──────── Integrationstest
                    \                  /
   Feinentwurf (Komponentenspezifikation) ── Komponententest
                          \        /
                       Implementierung
```

> Hinweis: Die Bezeichnungen folgen vereinfacht dem Aufbau des V-Modell XT. Für die Prüfung reicht dieses Schema völlig aus – im offiziellen V-Modell XT sind Produkte und Rollen je Ebene noch feiner ausdifferenziert.

### 2.2 Eigenschaften

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| **Test-Zuordnung** | Jede Entwurfsebene hat eine definierte Gegen-Testebene | 🔴 Prüfungsstoff |
| **Frühe Testplanung** | Testfälle werden parallel zur Spezifikation erstellt, nicht erst am Ende | 🔴 Prüfungsstoff |
| **Rollen & Prozesse** | V-Modell XT definiert zusätzlich Rollen, Verantwortlichkeiten, Tailoring | 🟡 Kontextwissen |
| **Qualitätssicherung** | Deutlich stärker verankert als im reinen Wasserfall-Modell | 🔴 Prüfungsstoff |
| **Flexibilität** | Gering, ähnlich wie Wasserfall – V-Modell XT erlaubt aber Projektanpassung (Tailoring) | 🟡 Kontextwissen |

### 2.3 Unterschied zum Wasserfall-Modell

| Kriterium | Wasserfall-Modell | V-Modell |
|---|---|---|
| Testverantwortung | Test als letzte Einzelphase | Test ist jeder Entwurfsphase zugeordnet |
| Fehlerentdeckung | Spät, meist erst im Test | Früher, da Testfälle parallel entstehen |
| Standardisierung | Kein fester Standard | V-Modell XT als verbindlicher Standard (öffentliche Aufträge in DE) |
| Rollenklarheit | Nicht definiert | Explizit definierte Rollen und Produkte |

### 2.4 Wofür geeignet

Geeignet für **sicherheitskritische und öffentlich ausgeschriebene Projekte**, bei denen Nachvollziehbarkeit und nachweisbare Qualitätssicherung verpflichtend sind – etwa Behörden-IT, Automotive, Luft- und Raumfahrt.

> **IHK-Typfrage:** *„Was ist der zentrale Vorteil des V-Modells gegenüber dem Wasserfall-Modell?"*
> Die feste Zuordnung von Testaktivitäten zu jeder Entwicklungsphase – Fehler werden dadurch früher und systematischer erkannt, und Qualitätssicherung ist von Anfang an Teil des Prozesses statt nur einer Endphase.

---

## 3. Spiralmodell

> Jeder Durchlauf der Spirale ist ein vollständiger Mini-Zyklus aus Risikoanalyse, Entwicklung und Bewertung – das Projekt wächst iterativ nach außen.

Das Spiralmodell (Boehm, 1986) kombiniert die strukturierten Phasen des Wasserfall-Modells mit **iterativem, risikogetriebenem Vorgehen**. Statt einmal linear durch alle Phasen zu laufen, durchläuft das Projekt mehrfach denselben Zyklus aus vier Quadranten – mit jedem Umlauf wächst der Funktionsumfang und die Spirale wird „größer".

### 3.1 Die vier Quadranten je Umlauf

| Quadrant | Inhalt | IHK-Relevanz |
|---|---|---|
| **1. Ziele festlegen** | Anforderungen und Alternativen für diesen Zyklus bestimmen | 🟡 Kontextwissen |
| **2. Risikoanalyse** | Risiken identifizieren, bewerten, Prototyp zur Risikominderung bauen | 🔴 Prüfungsstoff |
| **3. Entwicklung & Test** | Den Zyklus-Umfang implementieren und prüfen | 🟡 Kontextwissen |
| **4. Planung des nächsten Zyklus** | Review mit Auftraggeber, Entscheidung über Fortsetzung | 🔴 Prüfungsstoff |

### 3.2 Eigenschaften

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| **Risikofokus** | Risikoanalyse ist fester, wiederkehrender Bestandteil jedes Zyklus | 🔴 Prüfungsstoff |
| **Iteration** | Mehrere Durchläufe statt einmaliger linearer Ablauf | 🔴 Prüfungsstoff |
| **Prototyping** | Prototypen werden gezielt zur Risikoreduktion eingesetzt | 🟡 Kontextwissen |
| **Kosten/Aufwand** | Höher als Wasserfall, da Risikoanalysen wiederholt durchgeführt werden | 🟡 Kontextwissen |
| **Flexibilität** | Hoch – Anforderungen können sich zwischen den Zyklen ändern | 🔴 Prüfungsstoff |

### 3.3 Wofür geeignet

Geeignet für **große, risikobehaftete oder innovative Projekte** mit unklaren oder sich entwickelnden Anforderungen, bei denen frühzeitige Risikoerkennung wichtiger ist als ein fester Gesamtplan – etwa neuartige Softwareprodukte oder Forschungsprojekte mit technischer Unsicherheit.

> **IHK-Typfrage:** *„Wodurch unterscheidet sich das Spiralmodell von klassischen linearen Modellen?"*
> Durch die wiederholte, zyklische Risikoanalyse: Statt einmal alle Phasen abzuarbeiten, wird das Projekt in mehreren Umläufen entwickelt, wobei jeder Umlauf mit einer expliziten Risikobewertung beginnt, bevor weiterentwickelt wird.

> Randnotiz (kein Prüfungsstoff, aber hilfreich zum Verständnis): Das Spiralmodell ist ein **Meta-Modell** – innerhalb eines einzelnen Zyklus können je nach Risikolage andere Vorgehensweisen wie Wasserfall oder Prototyping eingesetzt werden. Es ersetzt diese Modelle also nicht zwingend, sondern kann sie in seine Zyklen integrieren.

---

## 4. Woran scheitern die Modelle in der Praxis?

| Modell | Typisches Scheitern | IHK-Relevanz |
|---|---|---|
| **Wasserfall** | Anforderungen ändern sich während der langen Laufzeit, aber das Modell sieht keine Rücksprünge vor → Spätfolgekosten explodieren, „Big Bang"-Abnahme am Ende deckt Fehler zu spät auf | 🔴 Prüfungsstoff |
| **V-Modell** | Hoher administrativer Aufwand (Dokumente, Rollen, Produkte) wirkt für kleine/agile Projekte überdimensioniert; Tailoring wird in der Praxis oft vernachlässigt, wodurch der Prozess zur reinen Formalie verkommt | 🟡 Kontextwissen |
| **Spiralmodell** | Risikoanalyse erfordert Erfahrung – wird sie unterschätzt oder fehlerhaft durchgeführt, versagt der zentrale Vorteil des Modells; ohne klares Abbruchkriterium drohen endlose, unwirtschaftliche Zyklen | 🟡 Kontextwissen |
| **Alle drei** | Gemeinsamer Schwachpunkt: Sie sind **dokumentations- und planungsintensiv** – bei sehr dynamischen Anforderungen (z. B. Start-up-Produkte) verlieren sie gegenüber agilen Ansätzen (Scrum, Kanban) an Wirtschaftlichkeit | 🔴 Prüfungsstoff |

> **IHK-Typfrage:** *„Was ist das Hauptrisiko des Wasserfall-Modells?"*
> Da Anforderungsänderungen nicht vorgesehen sind, fallen Fehler oder veraltete Anforderungen oft erst spät – meist erst im Test oder bei der Abnahme – auf. Korrekturen sind dann besonders teuer, weil bereits mehrere Phasen darauf aufgebaut haben.

---

## 5. Die richtige Auswahl eines Vorgehensmodells

### 5.1 Entscheidungskriterien

| Kriterium | Spricht für Wasserfall/V-Modell | Spricht für Spiralmodell / iterative Ansätze |
|---|---|---|
| **Anforderungsstabilität** | Vollständig bekannt, ändert sich nicht | Unklar, entwickelt sich während des Projekts |
| **Projektrisiko** | Gering, bekannte Technologie | Hoch, neue/unerprobte Technologie |
| **Regulatorik** | Verpflichtende Dokumentation (Behörde, Safety) | Keine festen Vorgaben |
| **Kundennähe** | Kunde verfügbar nur an Meilensteinen | Kunde aktiv in regelmäßige Reviews einbindbar |
| **Projektgröße (Wasserfall)** | Klein bis mittel, überschaubar | – |
| **Projektgröße (V-Modell XT)** | Skalierbar von klein bis sehr groß – durch Tailoring an Projektgröße anpassbar | Groß, komplex, mit Teilprojekten |
| **Zeit-/Budgetdruck** | Fester Termin/Budget wichtiger als Flexibilität | Lernen und Risikoreduktion wichtiger als Fixtermin |

### 5.2 Merksatz zur Auswahl

> Je unsicherer die Anforderungen und je höher das technische Risiko, desto iterativer muss das Vorgehensmodell sein. Je strikter die regulatorischen Vorgaben und je stabiler die Anforderungen, desto eher passt ein lineares Modell wie Wasserfall oder V-Modell.

> **IHK-Typfrage:** *„Nach welchem Kriterium würden Sie sich zwischen Wasserfall-Modell und Spiralmodell entscheiden?"*
> Nach der Stabilität der Anforderungen und dem Projektrisiko: Sind Anforderungen vollständig bekannt und das Risiko gering, eignet sich das Wasserfall-Modell. Bestehen Unsicherheiten oder hohe technische Risiken, ist das Spiralmodell vorzuziehen, da es Risikoanalyse fest in den Prozess integriert.

---

## Vergleichsübersicht

```
Wasserfall:   [Anforderung]→[Entwurf]→[Impl.]→[Test]→[Einführung]
              (rein linear, kein Rücksprung)

V-Modell:     [Anforderung]──────────────[Abnahmetest]
                  \                          /
              [Entwurf]──────────────[Systemtest]
                     \                    /
                  [Implementierung]
              (jede Phase ↔ zugeordnete Testphase)

Spiralmodell:        Zyklus 2
                    ╱        ╲
              Zyklus 1        Risiko-
             ╱        ╲       analyse
        Ziele      Risiko        │
          │      analyse ←───────┘
          └──────────┘
        (mehrere Umläufe, wachsender Umfang, Risiko zuerst)
```

---

## Selbsttest

| Frage | Kurzantwort |
|---|---|
| Was ist das zentrale Merkmal des Wasserfall-Modells? | Strikt sequenzieller Ablauf ohne geplante Rücksprünge |
| Was bedeutet das „V" im V-Modell? | Jeder Entwurfsphase ist eine spiegelbildliche Testphase zugeordnet |
| Welches V-Modell ist in Deutschland für öffentliche IT-Projekte verbindlich? | Das V-Modell XT |
| Was passiert in jedem Umlauf des Spiralmodells? | Ziele festlegen → Risikoanalyse → Entwicklung/Test → Planung des nächsten Zyklus |
| Welches Modell eignet sich am besten bei unklaren, sich ändernden Anforderungen? | Das Spiralmodell |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| **Wasserfall-Modell** | Lineares Vorgehensmodell mit sequenziellen, abgeschlossenen Phasen |
| **V-Modell** | Modell mit gespiegelter Test-zu-Entwurf-Zuordnung |
| **V-Modell XT** | Deutscher Standard-Entwicklungsprozess für öffentliche IT-Projekte |
| **Spiralmodell** | Iteratives, risikogetriebenes Modell mit mehreren Zyklen |
| **Lastenheft** | Anforderungsdokument des Auftraggebers (Was wird gebraucht?) |
| **Pflichtenheft** | Umsetzungsdokument des Auftragnehmers (Wie wird es umgesetzt?) |
| **Risikoanalyse** | Systematische Bewertung von Projektrisiken, zentral im Spiralmodell |
| **Tailoring** | Anpassung des V-Modell-XT-Prozesses an Projektgröße/-typ |
| **Verifikation** | Prüfung „Wurde das System richtig gebaut?" (gegen Spezifikation) |
| **Validierung** | Prüfung „Wurde das richtige System gebaut?" (gegen Kundenbedarf) |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|---|---|---|
| Modellbeschreibung | „Beschreiben Sie das Wasserfall-Modell." | Sequenzieller Ablauf, Phasen benennen, keine Rücksprünge betonen |
| Vergleich | „Unterscheiden Sie V-Modell und Wasserfall-Modell." | Konkreten Unterschied (Test-Zuordnung) nennen, nicht nur Gemeinsamkeiten |
| Eignung begründen | „Für welches Projekt eignet sich das Spiralmodell?" | Risiko/Unsicherheit als Auswahlkriterium nennen, Beispiel geben |
| Schwachstelle benennen | „Welches Risiko birgt das Wasserfall-Modell?" | Späte Fehlererkennung, hohe Korrekturkosten konkret benennen |
| Auswahl begründen | „Begründen Sie die Wahl eines Vorgehensmodells für ein Szenario." | Kriterien (Anforderungsstabilität, Risiko, Regulatorik) auf das Szenario anwenden, nicht nur Modell nennen |

---

## Merk-Sätze

> Wasserfall: einmal geplant, einmal gebaut, einmal getestet – Rücksprünge sind nicht vorgesehen.

> V-Modell: zu jedem Bauschritt gehört ein passender Prüfschritt – das „V" ist die Brücke zwischen Entwurf und Test.

> Spiralmodell: Risiko zuerst – jeder Zyklus beginnt mit der Frage „Was kann hier schiefgehen?"

> Die Wahl des Vorgehensmodells ist keine Geschmacksfrage, sondern eine Funktion aus Anforderungsstabilität, Risiko und regulatorischen Vorgaben.

---

```yaml
title: "Vorgehensmodelle der Softwareentwicklung: Wasserfall, V-Modell, Spiralmodell"
typ: "Typ A - Kompakter Prüfungswiki"
lernfeld: "Allgemein / Projektmanagement"
pruefungsrelevanz: "AP1 schriftlich, Fachgespräch"
status: "Final"
stand: "2026"
autor: "David"
```