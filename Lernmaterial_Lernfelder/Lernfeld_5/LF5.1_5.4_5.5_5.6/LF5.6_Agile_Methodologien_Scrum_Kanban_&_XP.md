# LF5.6 – Agile Methodologien: Scrum, Kanban & XP

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 70–90 Minuten für das erste Durcharbeiten, +50–70 Minuten mit Selbsttest und Wiederholung
> **Status:** Final
> **Stand:** 2026-09-12
> **Teil:** 2 von 2 – Agile Methodologien (Teil A: Wasserfall, V-Modell, Spiralmodell, bereits vorhanden im Repo)
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was besagt das Agile Manifest, und was unterscheidet "agil" von "Scrum"? | [→ 1. Agiles Manifest](#1-das-agile-manifest) |
| 2 | Welche Rollen, Artefakte und Events hat Scrum, und wie läuft ein Sprint ab? | [→ 2. Scrum](#2-das-scrum-framework) |
| 3 | Wie funktioniert Kanban, und warum sind WIP-Limits so wichtig? | [→ 3. Kanban](#3-kanban-kontinuierlicher-fluss) |
| 4 | Was sind die Kernpraktiken von Extreme Programming (XP)? | [→ 4. XP](#4-extreme-programming-xp) |

---

## 1. Das Agile Manifest

> **Grundprinzip:** Ein Restaurantkoch, der stur nach einem 50 Seiten langen Rezeptbuch kocht, obwohl der Gast am Tisch gerade sagt "eigentlich ohne Zwiebeln, bitte", reagiert schlechter auf die reale Situation als einer, der kurz nachfragt und flexibel anpasst. Genau diese Haltung – auf Veränderung reagieren statt stur einem Plan zu folgen – ist der Kern des agilen Gedankens.

### 1.1 Agil ist eine Haltung – Scrum, Kanban und XP sind konkrete Ansätze

**Agilität** bezeichnet eine an Werten und Prinzipien orientierte Arbeitsweise bzw. Haltung, keine einzelne fest vorgeschriebene Methode. **Scrum**, **Kanban** und **XP** sind unterschiedliche konkrete Ansätze, mit denen diese agile Haltung umgesetzt wird – Scrum ist ein **Framework**, Kanban eher eine **Methode zur Steuerung des Arbeitsflusses**, XP eine **agile Entwicklungsmethodik mit technischen Praktiken**. Das **Agile Manifest** (2001, von 17 Softwareentwickler:innen verfasst) formuliert vier Kernwerte:

| Wert | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Individuen und Interaktionen** vor Prozessen und Werkzeugen | Menschen und Kommunikation wichtiger als starre Abläufe | 🔴 |
| **Funktionierende Software** vor umfassender Dokumentation | Lauffähiges Ergebnis zählt mehr als perfekte Papiere | 🔴 |
| **Zusammenarbeit mit dem Kunden** vor Vertragsverhandlung | Laufender Dialog statt starrem Pflichtenheft-Abhaken | 🔴 |
| **Reagieren auf Veränderung** vor dem Befolgen eines Plans | Anpassungsfähigkeit wichtiger als Plantreue | 🔴 |

> **Wichtig für die Prüfung:** Das Manifest sagt **nicht**, dass Prozesse, Dokumentation, Verträge oder Pläne wertlos sind – die rechte Seite jedes Wertepaars ("over") wird nicht verworfen, nur geringer gewichtet als die linke. Ein Azubi, der behauptet "agile Projekte brauchen keine Dokumentation", macht einen klassischen Prüfungsfehler.

> **IHK-Typfrage:** *"Ein Kunde möchte mitten im Projekt eine neue Anforderung einbringen. Wie würde ein klassisches Wasserfall-Team reagieren, wie ein agiles Team?"*
> **Musterantwort:** In einem klassischen sequenziellen Vorgehensmodell wie Wasserfall (siehe Teil A) werden Anforderungen möglichst früh festgelegt – eine späte Änderung muss typischerweise über ein formelles Änderungsverfahren bewertet und in bereits abgeschlossene bzw. nachfolgende Phasen eingearbeitet werden, was aufwendig und teuer sein kann. Ein agiles Team arbeitet dagegen in kurzen Zyklen (z. B. Scrum-Sprints) und kann die neue Anforderung für den nächsten Zyklus in den Product Backlog aufnehmen und einordnen – "Reagieren auf Veränderung" ist hier explizit vorgesehen, nicht die Ausnahme.

---

## 2. Das Scrum-Framework

> **Grundprinzip:** Eine Bergwanderung, bei der man vorab jeden einzelnen Schritt für die gesamte Route plant, scheitert oft an unvorhergesehenem Wetter oder Gelände. Wer dagegen in Etappen wandert – nach jeder Etappe die Lage neu bewertet und den nächsten Abschnitt plant – kommt trotz Unsicherheit zuverlässiger ans Ziel. Scrum organisiert Softwareentwicklung in solchen Etappen, den **Sprints**.

### 2.1 Die drei Verantwortlichkeiten im Scrum Team

Der Scrum Guide (2020) spricht nicht mehr von "Rollen", sondern von drei **Verantwortlichkeiten (Accountabilities)** – umgangssprachlich werden sie aber weiterhin oft als Rollen bezeichnet.

| Verantwortlichkeit | Fokus | IHK-Relevanz |
| --- | --- | --- |
| **Product Owner** | Maximiert den Produktwert, verantwortet das Product-Backlog-Management | 🔴 |
| **Scrum Master** | Verantwortet die wirksame Anwendung von Scrum, coacht das Team, hilft bei der Beseitigung von Hindernissen | 🔴 |
| **Developers** | Erstellen das Increment und entscheiden **selbst**, wie die Arbeit umgesetzt wird | 🔴 |

Das Scrum Team ist **interdisziplinär und selbstmanagend** – es besitzt intern alle Fähigkeiten, die für die Wertschöpfung nötig sind, und entscheidet selbst, wer was, wann und wie macht. Das gesamte Scrum Team (Product Owner + Scrum Master + Developers zusammen) ist laut Scrum Guide typischerweise **10 oder weniger Personen**.

> **Wichtig für die Prüfung:** In Scrum gibt es **keine klassische Projektleitung**. Der Scrum Master "befiehlt" dem Team nicht, was zu tun ist – er hat keine Weisungsbefugnis, sondern eine dienende, unterstützende Funktion (auch "Servant Leadership" genannt). **Wie** die Developers ein Increment erstellen, entscheiden sie selbst – nicht der Scrum Master. Die veraltete Merkregel "Product Owner = WAS, Scrum Master = WIE" ist irreführend, weil sie den Eindruck erweckt, der Scrum Master sei für die technische Umsetzung zuständig.

### 2.2 Die drei Artefakte und ihre Commitments

| Artefakt | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Product Backlog** | Eine sich kontinuierlich weiterentwickelnde, geordnete Liste der Arbeiten, die zur Verbesserung des Produkts benötigt werden (nie vollständig "fertig") | 🔴 |
| **Sprint Backlog** | Sprint Goal + die für den Sprint ausgewählten Product-Backlog-Einträge + der Plan der Developers, wie daraus ein Increment entsteht | 🔴 |
| **Increment** | Ein nutzbarer Schritt in Richtung Product Goal, der die Definition of Done erfüllt – innerhalb eines Sprints können mehrere Increments entstehen | 🔴 |

Jedem Artefakt ist zusätzlich ein verbindliches **Commitment** zugeordnet:

| Commitment | Gehört zu | Bedeutung | IHK-Relevanz |
| --- | --- | --- | --- |
| **Product Goal** | Product Backlog | Langfristiges Ziel des Produkts | 🔴 |
| **Sprint Goal** | Sprint Backlog | Gemeinsamer Zweck des aktuellen Sprints | 🔴 |
| **Definition of Done** | Increment | Verbindliche Qualitätskriterien, wann Arbeit als fertiger Bestandteil des Increments gilt | 🔴 |

> **Praxis (kein verpflichtender Scrum-Bestandteil):** Product-Backlog-Einträge werden häufig als **User Stories** formuliert (siehe auch LF5.1, Requirements & Analysis) und z. B. mit **Story Points** relativ geschätzt; der verbleibende Aufwand lässt sich in einem **Burndown Chart** visualisieren. Diese Techniken werden oft zusammen mit Scrum verwendet, sind aber selbst **keine vorgeschriebenen Bestandteile** des Scrum-Frameworks – ein häufiger Lernfehler ist die Gleichsetzung "Scrum = User Stories + Story Points".

### 2.3 Scrum Events und Sprint

Der **Sprint** ist die Zeitbox (laut Scrum Guide **ein Monat oder weniger**, in der Praxis häufig zwei Wochen) und der Container für die vier weiteren Events:

| Event | Zweck | Typische Dauer | IHK-Relevanz |
| --- | --- | --- | --- |
| **Sprint** | Zeitbox, in der ein nutzbares Increment entsteht; Container für die anderen Events | Ein Monat oder weniger | 🔴 |
| **Sprint Planning** | Scrum Team legt gemeinsam Sprint Goal und Sprintinhalt fest; Developers erstellen den Umsetzungsplan | Zu Sprint-Beginn | 🔴 |
| **Daily Scrum** | Developers überprüfen Fortschritt auf das Sprint Goal und passen den Sprint Backlog bei Bedarf an | 15 Minuten, täglich | 🔴 |
| **Sprint Review** | Scrum Team und Stakeholder überprüfen gemeinsam Ergebnis und Umfeld, besprechen nächste Schritte – eine Arbeitssitzung, keine reine Präsentation | Am Sprint-Ende | 🔴 |
| **Sprint Retrospective** | Scrum Team untersucht den vergangenen Sprint und plant Verbesserungen an Qualität und Effektivität | Nach dem Review | 🔴 |

> **Wichtig für die Prüfung:** Der Daily Scrum ist **kein Statusbericht an eine Führungskraft**, sondern dient den Developers dazu, den Fortschritt zu überprüfen und den Plan anzupassen. Diese Verwechslung ist eine der häufigsten Prüfungsfallen zu Scrum. Der Sprint Review ist ebenfalls keine reine Abnahme-Präsentation, sondern eine gemeinsame Arbeitssitzung, bei der auch über die nächsten Schritte beraten wird.

> **IHK-Typfrage:** *"Erklären Sie den Unterschied zwischen Product Backlog und Sprint Backlog."*
> **Musterantwort:** Der Product Backlog ist die sich laufend weiterentwickelnde, geordnete Liste der aktuell bekannten Arbeiten zur Verbesserung des gesamten Produkts – er wird nie vollständig "fertig", und für sein Management ist der Product Owner verantwortlich. Der Sprint Backlog besteht dagegen aus drei Teilen: dem Sprint Goal, den für den aktuellen Sprint ausgewählten Product-Backlog-Einträgen und dem konkreten Plan der Developers, wie daraus ein Increment entstehen soll. Der Product Backlog richtet sich auf das gesamte Produkt, der Sprint Backlog nur auf den aktuellen Sprint.

---

## 3. Kanban: Kontinuierlicher Fluss

> **Grundprinzip:** Eine Kellnerin, die gleichzeitig zehn Bestellungen aufnimmt, aber immer nur drei Teller gleichzeitig zur Küche bringen kann, produziert Chaos, wenn sie versucht, alle zehn parallel zu bearbeiten. Begrenzt sie sich bewusst auf wenige gleichzeitige Aufgaben und bringt jede zu Ende, bevor sie die nächste beginnt, läuft der Ablauf ruhiger und tatsächlich schneller. Das ist die Kernidee hinter Kanban.

### 3.1 Visualisierter, kontinuierlicher Fluss

**Kanban** stammt ursprünglich aus der Fertigungsindustrie (Toyota) und visualisiert Arbeit auf einem Board mit Spalten wie "To Do", "In Arbeit", "Review", "Fertig". Anders als Scrum kennt Kanban **keine festen Sprints** – Arbeit fließt kontinuierlich.

### 3.2 WIP-Kontrolle als Kernregel

Die wichtigste Regel in Kanban ist die explizite **Kontrolle des Work in Progress (WIP)** – der begonnenen, aber noch nicht fertiggestellten Arbeit. Häufig wird das durch numerische **WIP-Limits** für einzelne Workflow-Bereiche umgesetzt (z. B. maximal 3 Aufgaben gleichzeitig in "In Arbeit"), ein Limit kann aber auch für mehrere zusammengefasste Spalten, eine Lane oder das gesamte Board gelten.

| Konzept | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **WIP-Kontrolle** | Explizite Begrenzung/Steuerung der begonnenen, aber noch nicht fertiggestellten Arbeit | 🔴 |
| **WIP-Limit** | Häufige, anschauliche Umsetzung der WIP-Kontrolle, z. B. maximal 3 Aufgaben in einem Workflow-Bereich | 🔴 |
| **Pull-Prinzip** | Neue Aufgabe wird erst begonnen, wenn Kapazität frei ist ("Stop starting, start finishing") | 🔴 |
| **Kontinuierlicher Fluss** | Kein fester Zyklus wie bei Scrum-Sprints, Arbeit fließt laufend | 🟡 |

> **Typische Prüfungsfalle:** Ein visualisiertes Board allein macht noch kein vollständiges Kanban-System – entscheidend ist eine **explizite WIP-Kontrolle**. Ein Board ganz ohne jede WIP-Kontrolle ist im Kern nur eine visualisierte To-do-Liste. Erst die Kontrolle des WIP erzeugt den entscheidenden "Pull"-Effekt, der das Team zwingt, begonnene Aufgaben zuerst fertigzustellen, bevor Neues gestartet wird.

> **IHK-Typfrage:** *"Wie hilft ein erreichtes WIP-Limit in der Spalte 'Review', ein organisatorisches Problem frühzeitig sichtbar zu machen?"*
> **Musterantwort:** Erreicht die Spalte "Review" ihr WIP-Limit (z. B. maximal 2), darf keine weitere Aufgabe dorthin verschoben werden, bis eine der beiden vorhandenen die Spalte verlässt. Stapeln sich die Aufgaben regelmäßig genau an dieser Stelle, zeigt das sehr konkret einen **Engpass (Bottleneck)** im Review-Prozess – z. B. zu wenige Reviewer:innen oder zu langsame Reviews. Auch ohne WIP-Limit wäre ein solcher Stau auf dem Board sichtbar; das Limit sorgt aber dafür, dass keine weitere Arbeit in den überlasteten Bereich gezogen wird und der Engpass nicht durch immer neue Aufgaben zusätzlich verschärft wird – vorgelagerte Teammitglieder müssen dann helfen, die Blockade aufzulösen, statt einfach weiterzuarbeiten.

---

## 4. Extreme Programming (XP)

> **Grundprinzip:** Ein Pilot und ein Co-Pilot im Cockpit überwachen sich gegenseitig ständig – Fehler eines Einzelnen werden durch die zweite Person sofort bemerkt, nicht erst Monate später bei einer Inspektion. Extreme Programming überträgt dieses Prinzip der sofortigen gegenseitigen Kontrolle auf die Softwareentwicklung.

### 4.1 Fokus auf technische Exzellenz

Während Scrum und Kanban vor allem **Organisation und Ablauf** regeln, fokussiert **XP** auf konkrete **technische Praktiken**:

| Praktik | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Pair Programming** | Zwei Entwickler:innen arbeiten gemeinsam an einer Aufgabe: Eine Person übernimmt als **Driver** die Umsetzung (tippt), die andere als **Navigator** prüft und denkt voraus – Rollen werden regelmäßig gewechselt | 🔴 |
| **Test-Driven Development (TDD)** | Automatisierter Unit-Test wird **vor** dem eigentlichen Code geschrieben (siehe auch LF5.5, Ensuring Quality) | 🔴 |
| **Kontinuierliches Refactoring** | Code wird laufend strukturell verbessert, ohne das äußere Verhalten zu ändern | 🟡 |
| **Häufige Integration** | Änderungen werden sehr oft in den gemeinsamen Code integriert, nicht erst am Ende | 🟡 |
| **Nachhaltiges Tempo (Sustainable Pace)** | Dauerhafte Überlastung/Überstunden vermeiden, damit Qualität und Leistungsfähigkeit langfristig erhalten bleiben (historische XP-Formulierung: "40-Stunden-Woche") | 🟢 |

> **Wichtig für die Prüfung:** Pair Programming wird oft fälschlich als reine Kostenverschwendung ("zwei Personen für eine Aufgabe bezahlen") kritisiert. Der eigentliche Nutzen liegt in kontinuierlichem Feedback während der Entwicklung, Wissenstransfer (keine Wissenssilos bei einzelnen Personen) und häufig früherer Fehlererkennung. Zusätzliche Code-Reviews können je nach Team und Qualitätsanforderungen trotzdem sinnvoll oder vorgeschrieben bleiben – Pair Programming ersetzt sie nicht automatisch vollständig.

> **IHK-Typfrage:** *"Beschreiben Sie den Ablauf von Test-Driven Development anhand des Red-Green-Refactor-Zyklus."*
> **Musterantwort:** TDD folgt drei wiederkehrenden Schritten: **Red** – zuerst wird ein automatisierter Test geschrieben, der die gewünschte, noch nicht existierende Funktion prüft; da die Funktion noch fehlt, schlägt der Test erwartungsgemäß fehl (rot). **Green** – anschließend wird die **minimal nötige** Codemenge geschrieben, um genau diesen Test bestehen zu lassen (grün), ohne sich um Eleganz zu kümmern. **Refactor** – erst danach wird der Code strukturell verbessert (Duplikate entfernt, Lesbarkeit erhöht), während die bereits bestandenen Tests sicherstellen, dass sich das Verhalten dabei nicht ändert. Dieser Dreischritt wiederholt sich für jede neue Funktion.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Agile Projekte brauchen keine Dokumentation und keine Pläne | Das Agile Manifest gewichtet funktionierende Software höher als umfassende Dokumentation – es verwirft Dokumentation/Pläne nicht komplett |
| 2 | Der Scrum Master ist die Projektleitung, weist dem Team Aufgaben zu und entscheidet, WIE gearbeitet wird | Der Scrum Master hat keine Weisungsbefugnis – er unterstützt die wirksame Anwendung von Scrum und hilft bei Hindernissen; WIE die Arbeit erledigt wird, entscheiden die Developers selbst |
| 3 | Der Daily Scrum ist ein Statusbericht an Vorgesetzte | Es dient den Developers zur Überprüfung des Fortschritts und Anpassung des Plans, nicht als Bericht für das Management |
| 4 | Ein Board mit Spalten ist bereits ein vollständiges Kanban-System | Entscheidend ist eine explizite Kontrolle des Work in Progress (typischerweise über WIP-Limits) – ohne diese Kontrolle ist es nur eine visualisierte To-do-Liste |
| 5 | Kanban arbeitet wie Scrum in festen Sprints | Kanban schreibt keine festen Entwicklungszyklen wie Scrum-Sprints vor – Arbeit fließt kontinuierlich, Aufgaben werden bei freier Kapazität gezogen (Pull-Prinzip) |
| 6 | Pair Programming verdoppelt einfach die Kosten ohne Mehrwert | Der Nutzen liegt in kontinuierlichem Feedback, Wissenstransfer und früherer Fehlererkennung, nicht in reiner Verdopplung der Arbeitszeit |
| 7 | Das Scrum-Team (Developers) umfasst meist 5–9 Personen, Sprints dauern 2–4 Wochen | Laut Scrum Guide ist das **gesamte** Scrum Team (PO+SM+Developers) typischerweise 10 oder weniger Personen groß; ein Sprint ist eine Zeitbox von einem Monat oder weniger |
| 8 | Ein Increment ist "fertiger Code" | Ein Increment ist ein nutzbarer Produktbestandteil, der die gemeinsam vereinbarte Definition of Done erfüllt – nicht einfach beliebiger fertiggestellter Code |

---

## 6. Deep-Dive-Ausblick (freiwillig)

- **Scrumban:** Hybrid-Ansatz aus Scrum-Struktur und Kanban-Flussprinzip, u. a. für Teams mit sowohl geplanten Projekten als auch spontanen Support-Tickets.
- **Skalierte Frameworks:** Wie SAFe oder LeSS versuchen, Scrum-Prinzipien auf mehrere zusammenarbeitende Teams in Großprojekten zu übertragen.
- **"Scrum-but"-Antimuster:** Warum das Weglassen einzelner Scrum-Elemente (z. B. "wir machen Scrum, aber ohne Retrospektiven") den Nutzen des Frameworks systematisch untergräbt.
- **Agile Schätzmethoden im Detail:** Planning Poker und relative Aufwandsschätzung mit Story Points statt absoluter Zeitangaben.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne die vier Kernwerte des Agilen Manifests. | Individuen/Interaktionen vor Prozessen/Werkzeugen; funktionierende Software vor Dokumentation; Kundenzusammenarbeit vor Vertragsverhandlung; Reagieren auf Veränderung vor Plantreue |
| 2 | Nenne die drei Verantwortlichkeiten in Scrum. | Product Owner, Scrum Master, Developers |
| 3 | Was unterscheidet Product Owner und Scrum Master? | Product Owner maximiert den Produktwert und managt den Product Backlog; Scrum Master verantwortet die wirksame Anwendung von Scrum und coacht das Team – keiner der beiden bestimmt, WIE die Developers arbeiten |
| 4 | Was unterscheidet Product Backlog und Sprint Backlog? | Product Backlog = sich weiterentwickelnde, geordnete Liste für das gesamte Produkt; Sprint Backlog = Sprint Goal + ausgewählte Einträge + Umsetzungsplan für den aktuellen Sprint |
| 5 | Was ist die Definition of Done, und wofür ist sie wichtig? | Verbindliche Qualitätskriterien, wann Arbeit als fertiger Bestandteil des Increments gilt |
| 6 | Wofür ist der Daily Scrum da, und für wen? | Synchronisation der Developers zur Überprüfung des Fortschritts, nicht als Statusbericht an das Management |
| 7 | Was ist ein WIP-Limit? | Begrenzung der gleichzeitig begonnenen, aber noch nicht fertiggestellten Arbeit in einem Workflow-Bereich |
| 8 | Was bedeutet "Pull-Prinzip"? | Eine neue Aufgabe wird erst begonnen, wenn Kapazität frei ist – "Stop starting, start finishing" |
| 9 | Was unterscheidet Scrum und Kanban bei der Zeitstruktur? | Scrum arbeitet in festen Sprints (Zeitboxen von max. einem Monat), Kanban schreibt keine festen Zyklen vor, Arbeit fließt kontinuierlich |
| 10 | Was ist Pair Programming? | Zwei Entwickler:innen arbeiten an einer Aufgabe; eine als Driver (tippt), eine als Navigator (prüft, denkt voraus) – Rollen wechseln regelmäßig |
| 11 | Nenne die drei Schritte des Red-Green-Refactor-Zyklus (TDD). | Red (fehlschlagender Test) → Green (minimaler Code zum Bestehen) → Refactor (Code strukturell verbessern) |

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Agiles Manifest** | 4 Kernwerte, 2001 formuliert – Individuen, funktionierende Software, Kundenzusammenarbeit, Reagieren auf Veränderung jeweils höher gewichtet |
| **Product Owner** | Maximiert Produktwert, verantwortet Product-Backlog-Management |
| **Scrum Master** | Verantwortet wirksame Scrum-Anwendung, coacht Team, keine Weisungsbefugnis |
| **Scrum Team** | PO + SM + Developers zusammen, typischerweise 10 oder weniger Personen |
| **Sprint** | Zeitbox von max. einem Monat, Container für die Scrum-Events |
| **Product Backlog** | Sich weiterentwickelnde, geordnete Liste für das gesamte Produkt |
| **Sprint Backlog** | Sprint Goal + ausgewählte Einträge + Umsetzungsplan für aktuellen Sprint |
| **Product Goal** | Langfristiges Ziel des Scrum Teams für einen zukünftigen Produktzustand |
| **Sprint Goal** | Gemeinsamer Zweck und Fokus des aktuellen Sprints |
| **Definition of Done** | Verbindliche Kriterien, wann Arbeit als fertiger Increment-Bestandteil gilt |
| **Daily Scrum** | 15-minütige Synchronisation der Developers, kein Statusbericht |
| **Kanban** | Visueller, kontinuierlicher Arbeitsfluss ohne feste Sprints |
| **WIP-Limit** | Begrenzung gleichzeitig begonnener, unfertiger Arbeit pro Workflow-Bereich |
| **Pull-Prinzip** | Neue Aufgabe erst bei freier Kapazität |
| **Pair Programming** | Driver (tippt) + Navigator (prüft), Rollen wechseln regelmäßig |
| **TDD (Red-Green-Refactor)** | Test zuerst schreiben, dann minimalen Code, dann strukturell verbessern |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Agiles Manifest erklären | "Was besagt Wert X des Agilen Manifests?" | Beide Seiten des Wertepaars nennen, betonen dass die rechte Seite nicht verworfen wird |
| Scrum-Rolle/Event zuordnen | "Wer macht was in Scrum?" | Konkrete Rolle/Event benennen, nicht nur "das Team macht das" |
| Scrum vs. Kanban abgrenzen | "Was unterscheidet X von Y?" | Konkreten strukturellen Unterschied nennen (Sprints vs. kontinuierlicher Fluss), nicht nur "beides ist agil" |
| XP-Praktik erklären | "Erklären Sie Praktik X" | Konkreten Ablauf/Mechanismus beschreiben, nicht nur die Praktik benennen |

---

## 10. Merksätze für das Fachgespräch

> Agil ist die Haltung – Scrum, Kanban und XP sind unterschiedliche Ansätze, sie praktisch umzusetzen.

> Der Scrum Master ist kein Projektleiter – er dient dem Team, fördert Selbstmanagement und hilft, Hindernisse zu beseitigen.

> Kanban ohne explizite WIP-Kontrolle ist nur eine hübsche To-do-Liste.

> Stop starting, start finishing – erst fertig machen, dann Neues beginnen.

> TDD dreht die Reihenfolge um: erst der Test, dann der Code, der ihn besteht.

---

```yaml
dokument: LF5.6B-wiki-artikel
themenfeld: "LF5.6 (Teil B) - Agile Methodologien"
titel: "Agile Methodologien: Scrum, Kanban & XP"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-12
quellen_intern:
  - "LF5.6.3: State of the Art (Agile Principles).md"
  - "LF5.6.4: Continuous Flow (Kanban & XP).md"
  - "Zusätzliche deutschsprachige Rechercheunterlagen vom Auftraggeber (siehe LF5.1-Historie)"
  - "Teil A (Wasserfall/V-Modell/Spiralmodell) bereits im Repo vorhanden: Vorgehensmodelle_Softwareentwicklung.md - Format/Stil daran angelehnt"
quellen_fachlich:
  - titel: "Agiles Manifest (2001), Scrum Guide (offizielle Version November 2020), Kanban Guide, Extreme Programming"
    herausgeber: "agilemanifesto.org, scrumguides.org, kanbanguides.org + Fachliteratur"
    status: "in Runde 2 gegen Primärquellen (Scrum Guide 2020, Kanban Guide) geprüft und präzisiert - siehe Review-Historie"
review_historie:
  - runde: 1
    datum: 2026-09-11
    ergebnis: "Erstdraft erstellt, Rohmaterial (LF5.6.3-4) und Zusatzrecherche vollständig eingearbeitet. An Format von Teil A angelehnt. Stabiles Wissen, keine Web-Verifikation nötig."
  - runde: 2
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (2 Reviews) eingearbeitet, beide mit Scrum-Guide-2020-Zitaten. Wichtigste Korrekturen: Scrum-Master 'verantwortet WIE' war falsch (keine Weisungsbefugnis, Developers entscheiden selbst); Teamgröße '5-9' korrigiert zu 'gesamtes Team ≤10' (bezog sich fälschlich nur auf Developers); Sprint '2-4 Wochen' zu 'max. 1 Monat'; Sprint Backlog um Sprint Goal + Plan ergänzt (war nur 'Ausschnitt'); Definition of Done, Product Goal, Sprint Goal als fehlende Commitments ergänzt; Kanban-WIP-Aussage entschärft (Kontrolle statt zwingend numerisches Limit); Logikfehler bei 'WIP-Limit macht Engpass sichtbar' korrigiert (Board macht Stau ohnehin sichtbar, Limit verhindert nur unkontrolliertes Wachsen); Scrum/Kanban/XP nicht mehr pauschal 'Frameworks' genannt; 40-Std-Woche zu Sustainable Pace; Driver/Navigator bei Pair Programming ergänzt; User Stories/Story Points als Praxis statt Scrum-Pflicht gekennzeichnet. Zwei Reviews behaupteten Claude-Links und kaputte Markdown-Tabellen - beim Abgleich mit der Datei nicht bestätigt, nicht übernommen. review_historie ab dieser Runde im neuen kompakten Format (siehe Workflow-Update)."
  - runde: 3
    datum: 2026-09-12
    ergebnis: "Externe Prüfung (2 Reviews) eingearbeitet. Kanban-Abschnitt konsistent auf 'explizite WIP-Kontrolle' statt starr 'WIP-Limit pro Spalte' umgestellt (Widerspruch zur eigenen späteren Präzisierung aufgelöst), inkl. Merksatz. Product-Backlog-Musterantwort von 'alle denkbaren Arbeiten' zu 'aktuell bekannte Arbeiten' präzisiert (emergente statt potenziell vollständige Liste). Scrum Team um 'interdisziplinär und selbstmanagend' ergänzt, Retrospective korrekt dem gesamten Scrum Team zugeordnet. Merksatz 'Werkzeuge' an die bereits im Haupttext etablierte Framework/Methode/Methodik-Unterscheidung angeglichen. Cheatsheet um Product Goal und Sprint Goal ergänzt. Zwei Reviews behaupteten erneut (bereits dritte Wiederholung in diesem Artikel), Claude-Links und kaputte Tabellen seien weiterhin vorhanden - beim erneuten, besonders gründlichen Abgleich mit der tatsächlichen Datei klar widerlegt, nicht übernommen."
  - runde: 4
    datum: 2026-09-12
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): gesamte Datei durchgelesen, einen über mehrere Runden wiederholt angemerkten Rest behoben – Deep-Dive-Pfeile '(→ Abschnitt X)' entfernt, da diese Themen dort tatsächlich nicht erklärt werden. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-11/12) – Freigabe durch Autor:in bestätigt"
```