# LF8.2: UI/UX-Engineering & Ergonomisches Prototyping

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Lernplanung — Grundlagen für AP1, mögliche Transferfragen in AP2 und Fachgespräch (keine offizielle IHK-Gewichtung)
> **Lernzeit:** Ca. 90–120 Min. reines Lesen/Wiederholen, 150–210 Min. mit Übungen (Kontrastberechnung, State-Machine-Entwurf)
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡-Markierungen sind eine didaktische Einschätzung dieses Wikis, keine offizielle IHK-Gewichtung.

## 📋 IHK-Kernfragen

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was unterscheidet UI-Design von UX-Design, und was ist der User-Centered-Design-Prozess? | [→ 1. UI/UX-Grundlagen](#1-uiux-grundlagen--user-centered-design) |
| 2 | Welche 7 Interaktionsprinzipien definiert ISO 9241-110, und was sind die POUR-Prinzipien der WCAG 2.2? | [→ 2. Ergonomie & Barrierefreiheit](#2-ergonomie-standards--barrierefreiheit) |
| 3 | Was unterscheidet Mobile-First von Desktop-First, und welche Mindestgröße gilt für Touch-Ziele? | [→ 3. Mobile-First & Responsive Layouts](#3-mobile-first--responsive-layouts) |
| 4 | Wie ist eine UML-Transition aufgebaut, und was unterscheidet einfache, zusammengesetzte und orthogonale Zustände? | [→ 4. UML State-Machine-Diagramme](#4-uml-state-machine-diagramme) |
| 5 | Was unterscheidet Low-Fidelity- von High-Fidelity-Prototyping, und wozu dient das Thinking-Aloud-Protokoll? | [→ 5. Wireframing & Prototyping](#5-interaktives-wireframing--prototyping) |

---

## 1. UI/UX-Grundlagen & User-Centered Design

> **Grundprinzip:** Eine schön gestaltete Oberfläche (UI) ist wie ein hübsches Gewächshaus mit falscher Wegführung – wenn die Besucher trotzdem nicht zur richtigen Pflanze finden, ist die Erfahrung (UX) trotzdem schlecht.

### 1.1 UI vs. UX

| Disziplin | Fokus | IHK-Relevanz |
| --- | --- | --- |
| **User Interface (UI)** | Visuelle, strukturelle und interaktive Elemente: Farben, Typografie, Grid-Layout, Buttons, Eingabefelder, Icons, Interaktionszustände | 🔴 Prüfungsstoff |
| **User Experience (UX)** | Kognitive und emotionale Gesamtreise des Nutzers: Usability, Nutzerforschung, Workflow, Informationsarchitektur | 🔴 Prüfungsstoff |

> **IHK-Typfrage:** *"Warum kann eine visuell hochwertige UI trotzdem eine schlechte UX erzeugen?"*
> **Musterantwort:** Wenn die zugrundeliegende Navigation verwirrend, langsam oder unlogisch ist, hilft die schönste Optik nichts – der Nutzer findet sein Ziel nicht oder nur mit hohem kognitivem Aufwand. UI ist ein Teilbereich von UX, aber gute UX braucht mehr als gutes UI.

### 1.2 Der User-Centered-Design-Prozess (UCD)

```text
      +-----------------------------------------+
      |                                         |
      v                                         |
[ 1. Verstehen ] -> [ 2. Spezifizieren ] -> [ 3. Entwerfen ] -> [ 4. Evaluieren ]
(Nutzer & Kontext)   (Anforderungen)         (Prototyping)      (Nutzertests)
```

| Phase | Inhalt | IHK-Relevanz |
| --- | --- | --- |
| **1. Verstehen** | Qualitative Daten zu Nutzern, Aufgaben und Nutzungsumgebung sammeln | 🔴 Prüfungsstoff |
| **2. Spezifizieren** | Nutzerbedürfnisse in konkrete, messbare Anforderungen übersetzen | 🔴 Prüfungsstoff |
| **3. Entwerfen** | Konzepte, Wireframes, Prototypen (Low- bis High-Fidelity) erstellen | 🔴 Prüfungsstoff |
| **4. Evaluieren** | Mit echten Nutzern testen, Reibungspunkte identifizieren, zurück zu Phase 3 iterieren | 🔴 Prüfungsstoff |

Der Prozess ist **iterativ** – nach der Evaluation kehrt man in der Regel in eine frühere Phase zurück, statt linear fortzuschreiten.

> **IHK-Typfrage:** *"Was ist das Ziel der Evaluationsphase im UCD-Prozess?"*
> **Musterantwort:** Prototypen werden mit echten Nutzern getestet, um Feedback zu sammeln und Reibungspunkte (Friction Points) zu identifizieren. Usability wird so anhand beobachtbarer Interaktionen und Rückmeldungen empirisch überprüft, statt ausschließlich auf Annahmen zu beruhen – die Erkenntnisse fließen in eine erneute Entwurfsiteration ein.
>
> *Hinweis:* Die Phasenbezeichnungen (Verstehen/Spezifizieren/Entwerfen/Evaluieren) sind eine vereinfachte Darstellung des UCD-Prozesses – andere Quellen verwenden teils andere Begriffe für dieselben vier wiederkehrenden Tätigkeiten.

### 1.3 Cognitive Load Theory

Das menschliche Arbeitsgedächtnis hat eine begrenzte Verarbeitungskapazität. Man unterscheidet drei Arten kognitiver Last:

| Lasttyp | Bedeutung | Ziel guten Designs | IHK-Relevanz |
| --- | --- | --- | --- |
| **Intrinsic (aufgabenbedingt)** | Schwierigkeit der Aufgabe selbst (z. B. komplexe Berechnung) | Nicht entfernbar, aber durch schrittweises Heranführen (Scaffolding) handhabbar | 🔴 Prüfungsstoff |
| **Extraneous (unnötig, layoutbedingt)** | Aufwand durch schlecht gestaltete Oberflächen (versteckte Menüs, chaotisches Layout) | Sollte **so weit wie möglich reduziert** werden, da er nicht zum Aufgabenverständnis beiträgt | 🔴 Prüfungsstoff |
| **Germane (lernförderlich)** | Aufwand, Informationen zu strukturieren und ins Langzeitgedächtnis zu integrieren | Gutes Design unterstützt den Aufbau mentaler Modelle | 🟡 Kontextwissen |

> Das klassische Modell ist für die Prüfung nützlich, wird in der Forschung aber differenzierter betrachtet.

> **IHK-Typfrage:** *"Was unterscheidet extraneous von germane cognitive load?"*
> **Musterantwort:** Extraneous Load ist verschwendeter Aufwand durch schlechtes Interface-Design (z. B. ein verstecktes Menü suchen) und sollte minimiert werden. Germane Load ist der Aufwand, mentale Modelle aufzubauen und Informationen zu verinnerlichen – dieser Aufwand ist erwünscht, weil er zum Verständnis beiträgt.

### 1.4 Informationsarchitektur

| Struktur | Beschreibung | Risiko/Nutzen | IHK-Relevanz |
| --- | --- | --- | --- |
| **Hierarchisch (tief)** | Inhalt in mehreren verschachtelten Ebenen | Hohes Risiko für extraneous Load bei zu vielen Klick-Ebenen | 🟡 Kontextwissen |
| **Flach (breit)** | Inhalt in wenigen Klicks erreichbar | Minimiert Suchzeit, erfordert aber sorgfältige visuelle Kategorisierung gegen Unübersichtlichkeit | 🟡 Kontextwissen |
| **Aufgabenorientiert** | Menüs/Aktionen nach dem, was der Nutzer *tun* will (z. B. "Bericht erstellen"), statt nach Systemstruktur | Reduziert kognitive Reibung erheblich | 🔴 Prüfungsstoff |

---

## 2. Ergonomie-Standards & Barrierefreiheit

> **Grundprinzip:** Ergonomie passt das System an den Menschen an – nicht umgekehrt. Ein Werkzeug, das man erst mühsam umlernen muss, ist schlecht gestaltet, egal wie mächtig es ist.

### 2.1 Die 7 Interaktionsprinzipien nach ISO 9241-110:2020

> Die Prinzipienliste wurde 2020 aktualisiert: **Individualisierbarkeit** ist seither in **Steuerbarkeit** integriert, neu hinzugekommen ist **Nutzerengagement**.

| # | Prinzip | Bedeutung | IHK-Relevanz |
| --- | --- | --- | --- |
| 1 | **Aufgabenangemessenheit** | Unterstützt die Aufgabe effizient, ohne unnötige Komplexität | 🔴 Prüfungsstoff |
| 2 | **Selbstbeschreibungsfähigkeit** | Jeder Dialogschritt ist durch klare Beschriftung sofort verständlich | 🔴 Prüfungsstoff |
| 3 | **Erwartungskonformität** | System verhält sich vorhersehbar gemäß etablierter Konventionen | 🔴 Prüfungsstoff |
| 4 | **Lernförderlichkeit** | Führt Einsteiger, bietet aber Shortcuts für erfahrene Nutzer | 🟡 Kontextwissen |
| 5 | **Steuerbarkeit** | Nutzer behält Kontrolle über Tempo, Reihenfolge, Konfiguration und individuelle Anpassungen (inkl. der früheren "Individualisierbarkeit") | 🔴 Prüfungsstoff |
| 6 | **Fehlertoleranz** | Trotz Fehleingabe wird das Ziel mit minimalem Korrekturaufwand erreicht, oder es gibt klare Hinweise zur Behebung | 🔴 Prüfungsstoff |
| 7 | **Nutzerengagement** | Fördert Aufmerksamkeit, Motivation und angemessene Beteiligung (neu seit der Fassung 2020) | 🟡 Kontextwissen |

> **IHK-Typfrage:** *"Welches Prinzip wird verletzt, wenn eine App per einzelnem Klick sofort Daten löscht, ohne Bestätigung?"*
> **Musterantwort:** Vor allem Fehlertoleranz und Steuerbarkeit – das System verhindert einen folgenreichen Fehlklick nicht und gibt dem Nutzer keine ausreichende Kontrolle oder Rückgriffsmöglichkeit.

> **IHK-Typfrage:** *"Welche Änderung brachte die Fassung ISO 9241-110:2020 gegenüber älteren Versionen?"*
> **Musterantwort:** Individualisierung ist nicht mehr als eigenständiges Prinzip aufgeführt, sondern in Steuerbarkeit integriert. Neu aufgenommen wurde das Prinzip Nutzerengagement.

### 2.2 WCAG 2.2 (POUR-Prinzipien) und BITV 2.0

**WCAG 2.2** (Web Content Accessibility Guidelines) ist der vom W3C entwickelte globale Standard, strukturiert in 4 Grundprinzipien:

| Prinzip | Bedeutung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **P**erceivable (Wahrnehmbar) | Informationen müssen auf verschiedene Weise wahrnehmbar sein | Textalternativen für Bilder, anpassbarer Kontrast | 🔴 Prüfungsstoff |
| **O**perable (Bedienbar) | UI-Komponenten und Navigation müssen bedienbar sein | Vollständige Tastaturbedienung, keine Navigationsfallen | 🔴 Prüfungsstoff |
| **U**nderstandable (Verständlich) | Information und Bedienung müssen verständlich sein | Klare Sprache, vorhersehbare Seitenstruktur, Eingabehilfen | 🔴 Prüfungsstoff |
| **R**obust (Robust) | Inhalte müssen mit aktuellen und zukünftigen Hilfstechnologien kompatibel sein | Kompatibilität mit Screenreadern | 🟡 Kontextwissen |

**BITV 2.0** (Barrierefreie-Informationstechnik-Verordnung) konkretisiert die Anforderungen an digitale Barrierefreiheit für bestimmte öffentliche Stellen des Bundes und verweist dazu auf einschlägige technische Standards, insbesondere die europäische Norm **EN 301 549** (die ihrerseits WCAG-Erfolgskriterien heranzieht). "BITV 2.0 = pauschal WCAG 2.2 AA" ist damit keine präzise Gleichung – und nicht jede private Website unterliegt automatisch der BITV 2.0, die Rechtslage hängt vom Anwendungsbereich ab.

### 2.3 Kontrastberechnung

WCAG unterscheidet drei Konformitätsstufen: **A** (Mindestanforderungen), **AA** (in vielen Accessibility-Projekten das praktische Ziel, weil zahlreiche wichtige Anforderungen dort liegen) und **AAA** (höchste Stufe, nicht für ganze Websites gefordert). Die konkrete rechtliche Bewertung erfolgt jeweils nach dem geltenden Rechtsrahmen und den anzuwendenden technischen Standards (insbesondere EN 301 549) – nicht pauschal über eine WCAG-Stufe allein. Für Text gelten konkrete Mindest-Kontrastverhältnisse (WCAG 1.4.3/1.4.6):

| Textgröße | Level AA | Level AAA |
| --- | --- | --- |
| Normaler Text | mind. **4,5:1** | mind. **7:1** |
| Großer Text (mind. 18pt bzw. mind. 14pt fett, ca. 24 bzw. 18,5–19 CSS-Pixel) | mind. **3:1** | mind. **4,5:1** |

Zusätzlich gilt für wichtige grafische Objekte und UI-Komponenten **WCAG 1.4.11 "Non-Text Contrast"**: grundsätzlich 3:1 gegenüber angrenzenden Farben.

> **Wichtig:** Farbe darf **niemals das einzige** Mittel sein, um Information zu vermitteln oder Zustände zu unterscheiden – zusätzlich sollten Text, Symbole, Muster, Position oder Form genutzt werden. Das hilft nicht nur Menschen mit Farbsehschwäche, sondern auch bei schlechter Beleuchtung, auf monochromen Displays oder bei eingeschränkter Farbdarstellung.

> **IHK-Typfrage:** *"Warum verstößt ein reiner grüner/roter Erfolgs-/Fehler-Icon-Code gegen Barrierefreiheit?"*
> **Musterantwort:** Nutzer mit Farbsehschwäche können die Farben nicht zuverlässig unterscheiden. Die Information muss zusätzlich über Form, Icon oder Text codiert werden (z. B. Häkchen-Symbol für Erfolg, Warndreieck für Fehler), damit sie farbunabhängig wahrnehmbar ist.

---

## 3. Mobile-First & Responsive Layouts

> **Grundprinzip:** Man plant zuerst das kleinste Beet (Smartphone) und erweitert dann – nicht umgekehrt, wo man ein großes Beet nachträglich zusammenstutzen muss und dabei Wurzeln beschädigt.

### 3.1 Mobile-First vs. Desktop-First

| Ansatz | Vorgehen | Konsequenz | IHK-Relevanz |
| --- | --- | --- | --- |
| **Desktop-First, häufig mit Graceful Degradation verbunden** | Komplexes Desktop-Layout zuerst entworfen, anschließend für kleinere/eingeschränkte Geräte angepasst (Elemente entfernt/verkleinert) | Oft aufgeblähter Code, langsame mobile Ladezeiten, kaputte Layouts | 🟡 Kontextwissen |
| **Mobile-First, häufig mit Progressive Enhancement verbunden** | Kern-UX zuerst für den kleinsten Screen umgesetzt, bei größeren Viewports schrittweise zusätzliche Features/Layouts ergänzt | Schlanke, schnell ladende mobile Seiten, gut skalierbare Interfaces | 🔴 Prüfungsstoff |

> Desktop-First/Mobile-First beschreiben die **Entwicklungsreihenfolge**; Graceful Degradation/Progressive Enhancement beschreiben das **Verhalten** des Systems auf unterschiedlich leistungsfähigen Zielumgebungen. Die Begriffspaare sind eng verbunden, aber nicht exakt deckungsgleich.

### 3.2 Responsive vs. Adaptive Design

| Ansatz | Funktionsweise | IHK-Relevanz |
| --- | --- | --- |
| **Responsive** | Fluides Grid, relative Einheiten (`%`, `vw/vh`, `em/rem`) und CSS Media Queries passen das Layout stufenlos an die Viewport-Breite an | 🔴 Prüfungsstoff |
| **Adaptive** | System erkennt Gerätekategorie und liefert separate, statisch vorbereitete Layout-Templates | 🟡 Kontextwissen |

### 3.3 Breakpoints (gängige Praxis-Richtwerte)

> Es gibt keine allgemein normierte, verbindliche Breakpoint-Größe – die folgenden Werte sind gängige Praxis-Richtwerte, keine feste ISO-/WCAG-Vorgabe.

| Kategorie | Typischer Richtwert |
| --- | --- |
| Mobile (Small) | < 576 px |
| Tablet (Medium) | 576–991 px |
| Desktop (Large) | ≥ 992 px |

### 3.4 Touch-Ziele & Fitts's Law

| Ebene | Wert | Einordnung | IHK-Relevanz |
| --- | --- | --- | --- |
| **WCAG 2.2 AA, SC 2.5.8 "Target Size (Minimum)"** | 24×24 CSS-Pixel | Grundsätzliche Mindestanforderung für Pointer-Ziele – mit definierten Ausnahmen (u. a. ausreichender Abstand zu anderen kleinen Zielen, gleichwertige größere Alternativen, Inline-Textlinks, vom User Agent bestimmte Größen, essenzielle Darstellungen) | 🔴 Prüfungsstoff |
| **WCAG 2.2 AAA, SC 2.5.5 "Target Size (Enhanced)"** | 44×44 CSS-Pixel | Grundsätzlich höhere Anforderung, ebenfalls mit definierten Ausnahmen | 🟡 Kontextwissen |
| **Praxisempfehlung** | häufig 44–48 CSS-Pixel | Gute Bedienbarkeit, besonders auf Touch-Geräten | 🟡 Kontextwissen |
| **Fitts's Law** | – | Die Zeit, ein Ziel zu erreichen, ist eine Funktion aus Distanz zum und Größe des Ziels – wichtige Buttons müssen groß und gut erreichbar platziert sein (z. B. "Daumenzone" bei Smartphones) | 🟡 Kontextwissen |
| **Hover-States** | – | Reine Touchbedienung bietet i. d. R. keinen zuverlässig verfügbaren Hover-Zustand – kritische Funktionen dürfen deshalb nicht ausschließlich über Hover erreichbar sein, sondern müssen auch per explizitem Tap, Klick oder Tastatur bedienbar sein | 🔴 Prüfungsstoff |

> **IHK-Typfrage:** *"Sind 24×24 CSS-Pixel für jedes Bedienelement ohne Ausnahme zwingend?"*
> **Musterantwort:** Nein. WCAG 2.2 SC 2.5.8 enthält mehrere Ausnahmen, z. B. ausreichenden Abstand zu benachbarten Zielen, gleichwertige größere Alternativziele oder Inline-Text-Links.

> **IHK-Typfrage:** *"Warum sind ausschließlich hover-aktivierte Dropdown-Menüs für mobile Layouts ungeeignet?"*
> **Musterantwort:** Reine Touchbedienung kennt keinen zuverlässig verfügbaren Hover-Zustand – ein Finger tippt entweder oder tippt nicht. Kritische Funktionen müssen deshalb zusätzlich per explizitem Tap, Klick oder Tastatur erreichbar sein (z. B. Akkordeon-Menü oder Tap-to-expand statt reiner Hover-Navigation).

---

## 4. UML State-Machine-Diagramme

> **Grundprinzip:** Ein Zustandsdiagramm ist wie ein Wachstumsplan für eine Pflanze – nicht was sie *ist* (Struktur), sondern wie sie sich *über die Zeit verändert* (Verhalten) unter bestimmten Auslösern (Gießen, Licht, Frost).

### 4.1 Grundlagen

State-Machine-Diagramme (Statecharts, spezifiziert in der OMG-UML-Norm) beschreiben – anders als strukturelle Diagramme wie Klassendiagramme – das **dynamische Verhalten** eines Systems: wie ein Objekt (UI-Komponente, Gerät, Prozess) auf Ereignisse reagiert und seinen Zustand wechselt. Sie sind ein zentrales Planungswerkzeug für reaktive Frontends (z. B. React-State) und asynchrone Prozesse – noch bevor Code geschrieben wird.

### 4.2 Notationselemente

| Element | Symbol/Notation | Bedeutung | IHK-Relevanz |
| --- | --- | --- | --- |
| **Einfacher/atomarer Zustand** | Abgerundetes Rechteck/Oval | Zustand **ohne** verschachtelte Unterzustände; kann `entry/`, `do/`, `exit/`-Aktionen enthalten | 🔴 Prüfungsstoff |
| **Startzustand** | Ausgefüllter schwarzer Kreis | Markiert den Beginn der State Machine | 🔴 Prüfungsstoff |
| **Endzustand** | "Bullseye"-Symbol | Markiert das Ende des Prozesses | 🔴 Prüfungsstoff |
| **Transition** | Gerichteter Pfeil | Übergang zwischen zwei Zuständen | 🔴 Prüfungsstoff |

**Transition-Syntax:** `Trigger [Guard] / Effect` (in vereinfachter Lernnotation oft auch als `/ Action` bezeichnet)

| Bestandteil | Bedeutung | Beispiel |
| --- | --- | --- |
| **Trigger** | Auslösendes Ereignis | `click`, `timeout`, `temperatureChanged` |
| **Guard** | Boolesche Bedingung in eckigen Klammern, die für den Übergang erfüllt sein muss | `[retry_count < 3]` |
| **Effect** | Verhalten (eine oder mehrere Aktionen), das beim Übergang ausgeführt wird | `resetCounter()` |

Beispiel: `submit [inputValid] / saveData()`

### 4.3 Erweiterte Konzepte

| Konzept | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Composite State (zusammengesetzt)** | Zustand mit interner Struktur aus Unterzuständen und einer oder mehreren Regionen | 🔴 Prüfungsstoff |
| **Nicht-orthogonaler Composite State** | Composite State mit **einer** Region – jeweils eine Unterzustandskonfiguration ist aktiv, die Unterzustände müssen aber nicht zwingend linear/sequenziell durchlaufen werden (Verzweigungen, Schleifen, direkte Ausgänge sind möglich) | 🔴 Prüfungsstoff |
| **Orthogonaler Composite State (parallel)** | Composite State mit **mindestens zwei** Regionen, deren Zustände **gleichzeitig** aktiv sein können (durch gestrichelte Linien getrennt) | 🔴 Prüfungsstoff |
| **History State** | Pseudo-Zustand, der eine zuvor aktive Zustandskonfiguration nach einer Unterbrechung wiederherstellt: **Shallow History (`H`)** merkt sich nur die direkt aktive Unterzustandskonfiguration, **Deep History (`H*`)** berücksichtigt auch tiefer verschachtelte Unterzustände. Ohne History wird beim erneuten Eintritt normalerweise der Initialzustand verwendet | 🟡 Kontextwissen |

> **IHK-Typfrage:** *"Was unterscheidet einen Composite State von einem orthogonalen State?"*
> **Musterantwort:** Ein Composite State enthält eine interne Zustandsstruktur. Bei einer einzelnen Region ist jeweils eine Unterzustandskonfiguration aktiv; die Unterzustände müssen dabei nicht zwingend linear durchlaufen werden. Ein orthogonaler State ist ein Composite State mit mehreren Regionen, die parallel bzw. gleichzeitig aktiv sind.

> **IHK-Typfrage:** *"Ist jeder Composite State automatisch orthogonal?"*
> **Musterantwort:** Nein. Orthogonal ist nur ein Composite State mit mehreren gleichzeitig aktiven Regionen. Ein Composite State mit nur einer Region ist nicht orthogonal.

---

## 5. Interaktives Wireframing & Prototyping

> **Grundprinzip:** Ein Papierprototyp ist wie ein Steckling – schnell und günstig herzustellen, um zu testen, ob eine Idee überhaupt Wurzeln schlägt, bevor man das ganze Beet dafür umgräbt.

### 5.1 Prototyping-Fidelity

| Stufe | Beschreibung | Vorteil | IHK-Relevanz |
| --- | --- | --- | --- |
| **Low-Fidelity** (Papier, Skizzen) | Schnell mit Papier/Karton/Markern erstellt | Günstig, flexibel, Fokus auf Struktur statt Optik; Nutzer schlagen eher drastische Änderungen vor, da wenig Aufwand investiert wirkt | 🔴 Prüfungsstoff |
| **High-Fidelity** (Figma, interaktive Klick-Dummies) | Realistische Darstellung der finalen Anwendung | Aufwendiger, aber sinnvoll, wenn visuelle Gestaltung, realistische Interaktionen oder Nähe zum späteren Produkt getestet werden sollen (z. B. finale Tests, Stakeholder-Freigaben, Entwickler-Übergabe) | 🔴 Prüfungsstoff |

> Low-Fidelity ist nicht ausschließlich für frühe Phasen reserviert – auch später eignet sie sich zum schnellen Test einzelner Abläufe. High-Fidelity ist nicht zwingend nur für die finale Testphase gedacht.

### 5.2 Interaktives Papier-Prototyping

- **"Computer"-Rolle ("Wizard-of-Oz"-Methode):** Ein Teammitglied simuliert manuell die Softwarereaktionen – tauscht Papierelemente aus, legt Overlays auf, wenn der Nutzer "klickt". Der Begriff stammt aus dem Film "Der Zauberer von Oz": Der vermeintlich mächtige Zauberer entpuppt sich als Mensch hinter einem Vorhang, der die Illusion steuert.
- **Overlays:** Dropdowns, Tooltips, Fehlermeldungen werden auf ausgeschnittenen Papierstücken dargestellt und bei Bedarf über die Basisansicht gelegt.

### 5.3 Usability-Testing-Methodik

| Schritt | Inhalt | IHK-Relevanz |
| --- | --- | --- |
| **1. Testaufgabe & Nutzungsszenario definieren** | Realistisches Aufgabenszenario formulieren, das der Nutzer selbstständig bearbeitet (z. B. "Registrieren Sie ein Konto und richten Sie einen Alarm ein") | 🔴 Prüfungsstoff |
| **2. Thinking-Aloud-Protokoll** | Nutzer denkt während der Interaktion laut – deckt kognitive Reibung und Fehlvorstellungen auf, die automatisierte Tests nicht finden | 🔴 Prüfungsstoff |
| **3. Dokumentieren & Iterieren** | Qualitative (Frustration) und quantitative Daten (Erfolgsquote, Fehleranzahl) erfassen, Design anpassen | 🟡 Kontextwissen |

**Moderiert vs. unmoderiert:** Bei **moderierten** Tests gibt ein Testleiter Aufgaben vor und fragt gezielt nach (mehr Tiefe, höherer Aufwand); bei **unmoderierten** Tests arbeitet der Nutzer eigenständig, oft remote (mehr Reichweite, weniger Kontextfragen möglich).

> **IHK-Typfrage:** *"Was unterscheidet Wireframe, Mockup und Prototyp?"*
> **Musterantwort:** Ein **Wireframe** zeigt Struktur/Layout und Informationshierarchie, meist mit geringer visueller Ausarbeitung. Ein **Mockup** ist eine statische, visuell ausgearbeitete Darstellung. Ein **Prototyp** ist ein Modell zur Überprüfung von Funktionen, Interaktionen oder Gestaltung – typischerweise (aber nicht zwingend vollständig) interaktiv.

---

## 🔄 Zusammenspiel der Konzepte in LF8.2

```text
UCD-Prozess (Verstehen → Spezifizieren → Entwerfen → Evaluieren)
        │
        ▼
  Ergonomie-Anforderungen ──────► Barrierefreiheit
   (ISO 9241-110)                  (WCAG 2.2 / BITV 2.0)
        │
        ▼
  Responsive/Mobile-First-Layout
        │
        ▼
  UML State-Machine (dynamisches Verhalten der Komponenten)
        │
        ▼
  Wireframe/Prototyp → Usability-Test → zurück zu "Evaluieren"
```

---

## ⚠️ Typische Prüfungsfallen

| Falle | Problem | Richtigstellung |
| --- | --- | --- |
| "UI und UX sind dasselbe" | Begriffe synonym verwendet | UI ist ein Teilbereich von UX; gute UX braucht mehr als gutes UI |
| "Jede kognitive Last ist schlecht" | Undifferenzierte Aussage | Nur extraneous Load soll minimiert werden; germane Load ist erwünscht |
| "WCAG schreibt feste Pixel-Breakpoints vor" | Verwechslung von Norm und Praxis-Konvention | Breakpoints sind gängige Praxis, keine normierte WCAG-Vorgabe; WCAG enthält aber sehr wohl andere konkrete Anforderungen (Kontrast, Tastaturbedienung, Touch-Zielgröße, Textvergrößerung, Reflow) |
| "Farbe allein reicht zur Statusanzeige, wenn sie kontrastreich ist" | Kontrast ≠ Farbunabhängigkeit | Auch bei gutem Kontrast braucht es zusätzlich Form/Icon/Text (Barrierefreiheit für Farbsehschwäche) |
| "Composite State = Unterzustände laufen sequenziell ab" | Zu enge Definition | Composite State mit einer Region hat Unterzustände, die nicht zwingend linear durchlaufen werden (Verzweigungen/Schleifen möglich); nur ein orthogonaler State hat mehrere gleichzeitig aktive Regionen |
| "24×24 CSS-Pixel gelten ausnahmslos für jedes Touch-Ziel" | WCAG-Ausnahmen ignoriert | SC 2.5.8 kennt definierte Ausnahmen (Abstand, gleichwertige Alternativen, Inline-Text u. a.) |
| "Ein High-Fidelity-Prototyp ist immer die bessere Wahl" | Fidelity-Stufe pauschal bewertet | Low-Fidelity ist in frühen Phasen oft überlegen (günstiger, mehr Änderungsbereitschaft bei Nutzern) |

## ✅ Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was ist der Kernunterschied zwischen UI und UX? | UI = visuelle, strukturelle und interaktive Gestaltung; UX = gesamte kognitiv-emotionale Nutzererfahrung |
| 2 | Nennen Sie die 4 Phasen des UCD-Prozesses. | Verstehen, Spezifizieren, Entwerfen, Evaluieren (iterativ) |
| 3 | Welche Art von kognitiver Last sollte so weit wie möglich reduziert werden? | Extraneous Cognitive Load |
| 4 | Nennen Sie 2 der 7 ISO-9241-110-Prinzipien. | z. B. Selbstbeschreibungsfähigkeit, Fehlertoleranz |
| 5 | Wofür steht das "O" in POUR? | Operable (bedienbar) |
| 6 | Welches Kontrastverhältnis fordert WCAG 2.2 AA für normalen Text? | Mindestens 4,5:1 |
| 7 | Was ist der Unterschied zwischen Mobile-First und Graceful Degradation? | Mobile-First entwirft zuerst für den kleinsten Screen und erweitert; Graceful Degradation entwirft zuerst komplex und kürzt danach |
| 8 | Wie lautet die vereinfachte Syntax einer UML-Transition? | `Trigger [Guard] / Effect` |
| 9 | Was unterscheidet einen History State von einem normalen Startzustand? | History State merkt sich den zuletzt aktiven Unterzustand nach einer Unterbrechung, statt immer am Anfang zu beginnen |
| 10 | Warum sind Nutzer bei Low-Fidelity-Prototypen eher bereit, radikale Änderungen vorzuschlagen? | Weil der wahrgenommene Erstellungsaufwand gering ist – Kritik fühlt sich weniger "verschwenderisch" an als bei einem aufwendigen digitalen Prototyp |
| 11 | Ist "BITV 2.0 = WCAG 2.2 AA" eine korrekte Gleichung? | Nein – BITV 2.0 ist eine deutsche Rechtsverordnung mit eigenem Anwendungsbereich, die auf technische Standards wie EN 301 549 verweist; WCAG 2.2 AA ist keine direkte 1:1-Übersetzung davon |
| 12 | Was unterscheidet Textkontrast von Nicht-Text-Kontrast? | Textkontrast betrifft Text/Bilder von Text (4,5:1 bzw. 3:1); Nicht-Text-Kontrast (WCAG 1.4.11) betrifft u. a. wichtige Bedienelemente und grafische Zustandsinformationen (3:1) |

---

## 📇 IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **UCD** | Iterativer Prozess: Verstehen → Spezifizieren → Entwerfen → Evaluieren |
| **Extraneous Cognitive Load** | Unnötiger, layoutbedingter mentaler Aufwand – sollte minimiert werden |
| **ISO 9241-110:2020** | Norm mit 7 Interaktionsprinzipien, darunter Steuerbarkeit, Fehlertoleranz, Nutzerengagement; Individualisierung ist in Steuerbarkeit integriert |
| **POUR** | Perceivable, Operable, Understandable, Robust (WCAG-2.2-Grundprinzipien) |
| **BITV 2.0** | Deutsche Verordnung zur digitalen Barrierefreiheit bestimmter öffentlicher Stellen des Bundes; verweist auf technische Standards wie EN 301 549 |
| **Kontrastverhältnis AA** | Mind. 4,5:1 (normaler Text), 3:1 (großer Text); zusätzlich 3:1 für wichtige Nicht-Text-Elemente (1.4.11) |
| **Mobile-First** | Kern-UX zuerst für kleinsten Screen, dann progressive Erweiterung |
| **Touch-/Pointer-Zielgröße** | WCAG 2.2 AA (SC 2.5.8): grundsätzlich 24×24 CSS-Pixel mit definierten Ausnahmen; AAA (SC 2.5.5): grundsätzlich 44×44 CSS-Pixel, ebenfalls mit Ausnahmen; 44–48 px verbreitete Praxisempfehlung |
| **Fitts's Law** | Zeit zum Erreichen eines Ziels hängt von dessen Distanz und Größe ab |
| **Composite State** | UML-Zustand mit verschachtelter interner Zustandsstruktur (eine oder mehrere Regionen) |
| **Orthogonal State** | Composite State mit mehreren Regionen, die gleichzeitig aktiv sein können |
| **Low-/High-Fidelity** | Grober Papier-Prototyp vs. realistischer digitaler Klick-Dummy – Wahl richtet sich nach Testziel, nicht nur nach Projektphase |
| **Thinking-Aloud-Protokoll** | Nutzer verbalisiert Gedanken während des Usability-Tests |
| **Moderiert/unmoderiert** | Test mit Testleiter und Rückfragen vs. eigenständiger (oft remote) Test ohne Moderation |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| K2 – Erklären | "Erläutern Sie den Unterschied zwischen X und Y" | Klare Abgrenzung mit Fachbegriffen, kein Beispiel als Definitionsersatz |
| K3 – Anwenden | "Gestalten Sie ein Zustandsdiagramm/Layout für…" | Konkrete Zustände/Transitionen bzw. Breakpoints, keine reine Prosa |
| K4 – Analysieren | "Analysieren Sie die Usability von…" | Konkrete Heuristik/Norm als Bewertungsraster, keine subjektive Meinung |
| K5/K6 – Bewerten/Synthetisieren | "Entwerfen Sie ein Gesamtkonzept für die Barrierefreiheit von…" | Mehrere Standards kombiniert, begründete Priorisierung |

---

## 🗣️ Merksätze fürs Fachgespräch

> "UI ist die Fassade, UX ist der gesamte Weg durchs Haus – eine schöne Fassade rettet keinen konfusen Grundriss."

> "Extraneous Load ist der Feind, germane Load ist der Freund – beide fühlen sich als 'Anstrengung' an, aber nur eine davon hilft dem Nutzer."

> "Barrierefreiheit ist kein Zusatzfeature für wenige, sondern robustes Design für alle – Kontrast und Text-Alternativen helfen auch bei schlechtem Licht oder kaputtem Lautsprecher."

> "Mobile-First heißt nicht 'nur fürs Handy', sondern 'das Wesentliche zuerst' – der Rest wird ergänzt, nicht gestrichen."

> "Ein State-Machine-Diagramm zeichnet man, bevor man den ersten `if`-Zweig schreibt – sonst entsteht das Chaos im Code statt auf dem Papier."

---

```yaml
lernfeld: LF8.2
titel: "UI/UX-Engineering & Ergonomisches Prototyping"
typ: "Kompakter Pruefungswiki (Typ A)"
quellen_intern:
  - LF8.2.1: Foundations of UI/UX Design
  - LF8.2.2: Ergonomic Standards & Accessibility
  - LF8.2.3: Mobile-First & Responsive Layouts
  - LF8.2.4: UML 2.0 State Machine Diagrams
  - LF8.2.5: Interactive Wireframing & Prototyping
quellen_fachlich:
  - "ISO 9241-110:2020 (Grundsaetze der Dialoggestaltung)"
  - "W3C Web Content Accessibility Guidelines (WCAG) 2.2"
  - "BITV 2.0 (Barrierefreie-Informationstechnik-Verordnung), EN 301 549"
  - "OMG UML 2.5.1 Specification (State Machines)"
  - "Nielsen Norman Group: Cognitive Load, Usability Heuristics, Paper Prototyping"
pruefungsrelevanz: "Grundlagen fuer AP1, Transferfragen moeglich in AP2 und Fachgespraech"
status: final
stand: 2026
optionale_deepdives:
  - "Fitts's Law mathematisch herleiten und auf konkrete Button-Groessen anwenden (Bezug: 3.4 Touch-Ziele)"
  - "WAI-ARIA Rollen/States/Properties fuer dynamische Inhalte (Bezug: 2. Barrierefreiheit)"
  - "CSS Container Queries vs. Media Queries (Bezug: 3.2 Responsive vs. Adaptive)"
  - "XState / Finite State Machines im Frontend, Guard als if-Abfrage, Effect als State-Update-Funktion (Bezug: 4. UML State Machines)"
  - "Nielsen's 10 Usability-Heuristiken (Bezug: 5.3 Usability-Testing)"
```