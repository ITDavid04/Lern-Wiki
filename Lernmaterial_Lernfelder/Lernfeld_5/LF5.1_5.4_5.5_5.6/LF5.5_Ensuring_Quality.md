# LF5.5 – Ensuring Quality

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 70–90 Minuten für das erste Durcharbeiten, +50–70 Minuten mit Selbsttest und Wiederholung
> **Status:** Final
> **Stand:** 2026-09-11
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie verteilen sich Testarten sinnvoll auf ein Projekt, und was ist die Testpyramide? | [→ 1. Testpyramide](#1-die-testpyramide) |
| 2 | Was unterscheidet Blackbox- von Whitebox-Testing, und wie ist ein Testfall aufgebaut? | [→ 2. Blackbox & Whitebox](#2-blackbox--und-whitebox-testing) |
| 3 | Wie funktioniert professionelles Debugging mit einem Debugger? | [→ 3. Debugging](#3-die-kunst-des-debuggings) |
| 4 | Was bedeuten CI, Continuous Delivery und Continuous Deployment, und welche Rolle spielt ein Linter? | [→ 4. CI/CD](#4-continuous-integration-delivery-und-deployment) |
| 5 | Was ist User Acceptance Testing, und warum ist das Abnahmeprotokoll rechtlich wichtig? | [→ 5. UAT](#5-user-acceptance-testing-uat) |

---

## 1. Die Testpyramide

> **Grundprinzip:** Ein Restaurant prüft nicht jeden Teller ausschließlich dadurch, dass ein Testesser jedes fertige Gericht komplett durchprobiert – zuerst werden einzelne Zutaten auf Frische geprüft (schnell, günstig, viele Male), dann das Zusammenspiel mehrerer Zutaten in einer Soße (aufwendiger), und erst ganz am Ende steht der komplette Gang auf dem Tisch (teuer, aber realitätsnah). Die Testpyramide überträgt genau diese Idee auf Software.

### 1.1 Die drei Ebenen

| Ebene | Was wird getestet | Eigenschaften | IHK-Relevanz |
| --- | --- | --- | --- |
| **Unit-Tests** (Basis) | Kleine, möglichst isolierte Codeeinheiten wie Funktionen, Methoden oder Klassen (z. B. ob `calculate_tax()` den richtigen Wert liefert) | Schnell, günstig, bilden typischerweise den größten Anteil der automatisierten Tests | 🔴 |
| **Integrationstests** (Mitte) | Zusammenspiel mehrerer Module (z. B. ob ein Skript erfolgreich die Datenbank abfragt) | Langsamer, komplexer als Unit-Tests | 🔴 |
| **System-/End-to-End-Tests** (Spitze) | Das vollständig integrierte System bzw. vollständige Geschäftsabläufe aus Anwenderperspektive | Realitätsnah, aber langsam und aufwendig zu warten, daher vergleichsweise wenige | 🔴 |

> **Begriffliche Abgrenzung:** Systemtest, End-to-End-Test und UI-Test überschneiden sich häufig, sind aber nicht identisch – ein Systemtest prüft das vollständige System gegen die Spezifikation, ein End-to-End-Test einen durchgängigen Geschäftsablauf, ein UI-Test gezielt die Benutzeroberfläche. Ein E2E-Test kann über die UI laufen, muss es aber nicht zwingend.

> **Typische Prüfungsfalle – das "Ice-Cream-Cone"-Antimuster:** Der Versuch, *alles* manuell über die grafische Oberfläche zu testen, kehrt die Pyramide um (viele langsame UI-Tests, wenige schnelle Unit-Tests). UI-Tests sind langsam und brüchig (ändert sich ein Button, bricht der Test) – der Schwerpunkt sollte auf der breiten Basis aus Unit-Tests liegen.

### 1.2 Regressionstests

**Regressionstests** prüfen nach einer Codeänderung, ob bereits funktionierende Altfunktionen weiterhin korrekt arbeiten – sie schützen davor, dass neuer Code alte Funktionalität "kaputt macht" ("regrediert").

> **IHK-Typfrage:** *"Erklären Sie anhand der Metapher eines Autobaus den Unterschied zwischen einem Unit-Test und einem Integrationstest."*
> **Musterantwort:** Ein Unit-Test entspricht der Prüfung eines einzelnen Bauteils für sich – z. B. wird eine Zündkerze isoliert getestet, ob sie zuverlässig zündet. Ein Integrationstest entspricht der Prüfung, ob mehrere Bauteile korrekt zusammenspielen – z. B. ob Motor, Zündkerze und Kraftstoffsystem gemeinsam den Motor zum Laufen bringen. Der Unit-Test prüft die isolierte Komponente, der Integrationstest prüft das Zusammenspiel mehrerer Komponenten.

---

## 2. Blackbox- und Whitebox-Testing

> **Grundprinzip:** Ein Prüfer, der ein verschlossenes Radio testet, kann nur Knöpfe drücken und beobachten, ob der richtige Sender ertönt – er sieht die Schaltung nicht (Blackbox). Ein Techniker, der das Gehäuse öffnet und jede Leiterbahn einzeln durchmisst, sieht dagegen den kompletten inneren Aufbau (Whitebox).

### 2.1 Die zwei Testmethodiken

| Methodik | Zugriff auf Quellcode | Fokus | IHK-Relevanz |
| --- | --- | --- | --- |
| **Blackbox-Testing** | Nein – nur Anforderungen bekannt | Eingaben liefern, Ausgaben mit den Anforderungen vergleichen (Nutzerperspektive) | 🔴 |
| **Whitebox-Testing** | Ja – Quellcode/innere Struktur bekannt | Tests werden unter Berücksichtigung der internen Programmlogik entwickelt, z. B. zur Anweisungs- oder Zweigüberdeckung (**Code Coverage**) | 🔴 |

> **Wichtig für die Prüfung – Code Coverage ist ein Messwert, kein Qualitätsbeweis:** Eine hohe Testabdeckung zeigt nur, welcher Code während der Tests ausgeführt wurde. Sie beweist nicht automatisch, dass alle Anforderungen, Grenzfälle oder fachlichen Regeln richtig getestet wurden – auch ein einmal durchlaufener Code kann mit einer unpassenden Prüfung (Assertion) trotzdem einen Fehler übersehen.

> **Wichtig für die Prüfung:** Entwickler:innen können durchaus Blackbox-Tests durchführen – problematisch ist nicht die Rolle an sich, sondern die fehlende Unabhängigkeit: Wer Implementierung und vorgesehene Bedienung bereits kennt, testet leicht unbewusst nur die erwarteten Pfade und übersieht ungewöhnliche Bedienwege oder unerwartete Eingaben. Ergänzende Tests durch unabhängige Personen erhöhen deshalb häufig die Fehlerfindungswahrscheinlichkeit.

### 2.2 Aufbau eines formalen Testfalls

Ein formaler Testfall muss für jede Person reproduzierbar sein und enthält:

| Element | Beispiel |
| --- | --- |
| **Test-ID & Titel** | `TC-01: Gültiger Login` |
| **Vorbedingungen** | "Nutzerkonto existiert, Datenbank läuft" |
| **Testschritte** | 1. Nutzername "admin" eingeben, 2. Passwort "1234" eingeben, 3. Auf Login klicken |
| **Erwartetes Ergebnis** | "Nutzer wird zum Dashboard weitergeleitet" |
| **Tatsächliches Ergebnis** | Wird bei der Durchführung ausgefüllt, z. B. "Bestanden" oder "Fehlgeschlagen: Fehler 500" |

> **Typische Prüfungsfalle:** Vage erwartete Ergebnisse wie "sollte funktionieren" sind unbrauchbar. Führt eine andere Person denselben Testfall aus, muss exakt klar sein, wie "funktioniert" konkret aussieht – z. B. "ein grünes Häkchen erscheint", nicht nur "es klappt".

> **IHK-Typfrage:** *"Formulieren Sie ein exaktes erwartetes Ergebnis für einen Testfall, bei dem ein Nutzer versucht, ein Konto mit einem zu kurzen Passwort anzulegen."*
> **Musterantwort:** "Das System lehnt die Kontoerstellung ab und zeigt die Fehlermeldung 'Passwort muss mindestens 8 Zeichen enthalten' unterhalb des Passwortfelds an; das Konto wird nicht in der Datenbank angelegt." Diese Formulierung ist konkret und überprüfbar – im Gegensatz zu einer vagen Aussage wie "eine Fehlermeldung erscheint", die offenlässt, welcher Text angezeigt wird und ob das Konto trotzdem (fehlerhaft) angelegt werden könnte.

---

## 3. Die Kunst des Debuggings

> **Grundprinzip:** Ein Uhrmacher, der einen Fehler in einem Uhrwerk sucht, öffnet das Gehäuse und beobachtet jedes Zahnrad einzeln bei laufendem Betrieb, statt das ganze Uhrwerk nur von außen zu schütteln und zu raten. Ein Debugger ermöglicht genau diesen Blick "ins Innere" eines laufenden Programms.

### 3.1 Vom `print()` zum Debugger

Einsteiger:innen suchen Fehler oft mit `print("hier")`-Anweisungen. Für die interaktive Untersuchung lokaler Programme bietet ein **Debugger** meist deutlich mehr Möglichkeiten – moderne IDEs (z. B. VS Code) bringen für Python integrierte Debugger mit. In produktiven, verteilten oder asynchronen Systemen bleiben strukturierte Logs und Traces aber weiterhin wichtige, teils unverzichtbare Werkzeuge der Fehlersuche.

| Konzept | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Breakpoint (Haltepunkt)** | Markierung an einer Codezeile; erreicht das Programm im Debug-Modus diese Stelle, wird die Ausführung angehalten | 🔴 |
| **Variablenansicht** | Im pausierten Zustand lassen sich die im aktuellen Kontext verfügbaren Variablen und ihre Werte einsehen | 🔴 |
| **Step Over** *(in VS Code z. B. F10)* | Führt die aktuelle Zeile inkl. Funktionsaufruf vollständig aus und pausiert bei der nächsten Zeile – taucht **nicht** in aufgerufene Funktionen ein | 🔴 |
| **Step Into** *(in VS Code z. B. F11)* | Ruft die aktuelle Zeile eine Funktion auf, springt der Debugger **hinein** und lässt sie Zeile für Zeile debuggen | 🔴 |
| **Continue/Resume** *(in VS Code z. B. F5)* | Läuft weiter bis zum nächsten Breakpoint | 🟡 |

> **Hinweis:** Die genannten Tastenkürzel sind in VS Code üblich, können aber je nach IDE (z. B. IntelliJ IDEA, PyCharm) und Betriebssystem abweichen.

> **Wichtig für die Prüfung – bedingte Breakpoints:** Ein Breakpoint in einer Schleife, die 10.000-mal durchläuft, zwingt sonst dazu, "Continue" tausendfach zu klicken. Ein **bedingter Breakpoint** (z. B. "pausiere nur, wenn `i == 9999`") löst dieses Problem gezielt.

> **IHK-Typfrage:** *"Nennen Sie einen wesentlichen Nachteil, mehrere `print()`-Anweisungen zur Fehlersuche zu verwenden statt eines IDE-Debuggers."*
> **Musterantwort:** `print()`-Anweisungen zeigen nur die Werte, die man explizit vorher hineinprogrammiert hat, und zu genau dem Zeitpunkt, an dem die Zeile im Code steht – der Programmfluss lässt sich damit nicht interaktiv erkunden. Ein Debugger erlaubt dagegen, das Programm an beliebiger Stelle anzuhalten, die im aktuellen Debugging-Kontext verfügbaren Variablen und deren Werte einzusehen und den Ablauf gezielt Schritt für Schritt (auch in aufgerufene Funktionen hinein) zu verfolgen – ohne den Code nachträglich mit temporären Ausgabezeilen zu verändern und später wieder entfernen zu müssen.

---

## 4. Continuous Integration, Delivery und Deployment

> **Grundprinzip:** Eine Fabrik, in der jedes gefertigte Teil von Hand einzeln durch einen Menschen kontrolliert wird, bevor es weiterverarbeitet werden darf, ist langsam und fehleranfällig. Eine automatisierte Prüfstraße, die jedes Teil sofort nach der Fertigung durchläuft, meldet Probleme sofort und lässt nur geprüfte Teile weiter. CI/CD ist diese automatisierte Prüfstraße für Code.

### 4.1 CI und CD im Detail

**CI/CD (Continuous Integration / Continuous Delivery / Continuous Deployment)** automatisiert Tests und Auslieferung. Plattformen wie **GitHub Actions** oder GitLab CI können je nach Workflow-Konfiguration bei Ereignissen wie Pushes, Pull Requests oder auch zeitgesteuert automatisiert Skripte ausführen.

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Continuous Integration (CI)** | Änderungen werden regelmäßig und automatisiert integriert, gebaut und geprüft – eine Pipeline kann z. B. bei jedem Push oder Pull Request gestartet werden | 🔴 |
| **Continuous Delivery** | Erfolgreich geprüfte Änderungen werden automatisiert bis zur Auslieferungsbereitschaft gebracht; die eigentliche Produktivfreigabe kann noch manuell erfolgen | 🔴 |
| **Continuous Deployment** | Geht einen Schritt weiter: Erfolgreich geprüfte Änderungen werden automatisch **ohne** manuelle Freigabe produktiv ausgerollt | 🔴 |
| **Linter** (z. B. `flake8` für Python) | Oft der erste CI-Schritt – führt eine **statische Analyse** des Quellcodes durch (mögliche Fehlerquellen, verdächtige Konstruktionen, Stilverstöße), **ohne** ihn auszuführen | 🔴 |

> **Achtung, Abkürzungsfalle:** "CD" kann sowohl **Continuous Delivery** als auch **Continuous Deployment** bedeuten – der Kontext entscheidet. Bei Delivery bleibt vor der Produktivsetzung typischerweise eine manuelle Freigabe möglich, bei Deployment automatisiert auch dieser letzte Schritt.

> **Wichtig für die Prüfung:** Dass ein fehlgeschlagener Test einen Pull Request automatisch blockiert, ist **keine Selbstverständlichkeit von CI an sich**, sondern setzt voraus, dass entsprechende Branch-/Repository-Regeln (z. B. "erforderliche Statuschecks") konfiguriert wurden. Ohne solche Regeln kann ein Merge trotz fehlgeschlagenem Test technisch möglich bleiben.

> **Wichtig für die Prüfung:** Je schneller eine CI-Pipeline Feedback liefert, desto früher lassen sich Fehler beheben – sehr lange Pipelines verzögern die Entwicklungsarbeit und werden in der Praxis eher umgangen. Deshalb werden Prüfungen häufig gestaffelt: schnelle Linter-/Unit-Tests zuerst, langsamere Integrations-/Systemtests später.

> **Ergänzend zu CI/CD – Versionsverwaltung und Bugtracking:** Systeme wie Git dokumentieren Änderungen, ermöglichen paralleles Arbeiten in Branches und helfen, konkurrierende Änderungen kontrolliert zusammenzuführen (entstehen widersprüchliche Änderungen an derselben Stelle, muss ein Mergekonflikt manuell gelöst werden) – siehe LF5.3, Development Tools & Version Control. Bugtracker/Ticket-Systeme (z. B. Jira, Mantis, Redmine) unterstützen die Dokumentation und Nachverfolgung von Aufgaben und Fehlern über definierte Statuszustände und lassen sich mit Versionsverwaltung und CI/CD-Systemen verknüpfen.

> **IHK-Typfrage:** *"Erklären Sie, wie eine CI-Pipeline verhindert, dass ein Entwickler versehentlich den `main`-Branch mit fehlerhaftem Code beschädigt."*
> **Musterantwort:** Beim Push eines neuen Branches oder beim Öffnen eines Pull Requests startet die CI-Pipeline automatisch: Sie baut den Code und führt die komplette Unit-Test-Suite (und ggf. Linter-Checks) aus. Schlägt auch nur ein Test fehl, markiert die Pipeline den zugehörigen Check als "fehlgeschlagen". Ist dieser Check im Repository als **erforderlicher Statuscheck** für den geschützten `main`-Branch konfiguriert, blockiert das den Merge, bis die Fehler behoben sind – diese Blockierung ist also keine automatische Eigenschaft von CI selbst, sondern das Ergebnis entsprechend eingerichteter Branch-Regeln. So gelangt fehlerhafter Code nicht in den zentralen, von allen genutzten Branch – die Prüfung erfolgt automatisiert und konsequent, statt sich auf die Disziplin einzelner Entwickler:innen zu verlassen.

---

## 5. User Acceptance Testing (UAT)

> **Grundprinzip:** Ein Architekt, der ein fertiges Haus nach allen technischen Normen abgenommen hat (Statik geprüft, Elektrik funktioniert), hat noch nicht sichergestellt, dass die Familie, die einziehen soll, sich darin auch tatsächlich wohlfühlt und alltagstauglich zurechtfindet. Genau diesen letzten, praktischen Schritt übernimmt beim Softwareprojekt das UAT.

### 5.1 Was UAT ist – und was nicht

Der Code kompiliert, die Unit-Tests sind grün, die CI-Pipeline läuft durch. Fertig? Nein – der letzte Schritt ist **User Acceptance Testing (UAT)**.

| Merkmal | Systemtest (QA) | User Acceptance Testing (UAT) |
| --- | --- | --- |
| **Durchgeführt von** | Entwickler:innen/QA-Team | Auftraggeber:in, Fachabteilung, Key User oder repräsentative Endnutzer:innen |
| **Prüft** | Funktioniert die Software **technisch** korrekt? | Löst die Software das **geschäftliche** Problem in der Praxis? |
| **Grundlage** | Technische Spezifikation | Vereinbarte fachliche Anforderungen und Akzeptanzkriterien, z. B. aus Lastenheft, Pflichtenheft, Vertrag oder User Stories (siehe LF5.1) |

> **Wichtig für die Prüfung:** Entwickler:innen sollten Testpersonen nicht suggestiv vorgeben, wie jeder Arbeitsschritt auszuführen ist ("klicken Sie hier, nicht dort") – sonst können echte Bedienprobleme oder missverstandene Anforderungen verdeckt bleiben. Eine neutrale Moderation, organisatorische Einweisung oder technische Unterstützung ist dagegen möglich und bei formalen Abnahmetests oft sinnvoll; UAT kann durchaus anhand vorbereiteter Szenarien und Akzeptanzkriterien ablaufen, ohne komplett frei und unangeleitet zu sein.

### 5.2 Das Abnahmeprotokoll

Besteht die UAT, unterschreibt die Kundschaft häufig ein formales **Abnahmeprotokoll (Acceptance Protocol)**, das die Abnahmeentscheidung sowie ggf. festgestellte Mängel oder Vorbehalte dokumentiert. Die Abnahme ist insbesondere bei einem **Werkvertrag** (§ 631 BGB, siehe WiSo 4) ein wichtiger rechtlicher Meilenstein: Nach § 641 BGB wird die Vergütung grundsätzlich mit der Abnahme fällig. Ein unterschriebenes Protokoll ist dabei ein wichtiges Beweismittel – die konkreten Rechtsfolgen hängen aber vom jeweiligen Vertrag und der Vertragsart ab, und eine Abnahme kann je nach Rechtslage auch auf andere Weise als durch ein unterschriebenes Protokoll zustande kommen (§ 640 BGB).

> **IHK-Typfrage:** *"Ein Softwareprojekt besteht alle automatisierten Unit-Tests, scheitert aber vollständig in der UAT-Phase beim Kunden. Wie kann das passieren?"*
> **Musterantwort:** Unit-Tests prüfen nur, ob einzelne Code-Bausteine technisch korrekt das tun, was die Entwickler:innen bei der Testerstellung *für richtig hielten* – sie testen also gegen die eigene Interpretation der Anforderungen, nicht zwingend gegen das tatsächliche Geschäftsproblem der Kundschaft. Wurde beispielsweise eine Anforderung im Lastenheft missverstanden oder eine wichtige Ausnahme im Arbeitsalltag der Nutzer:innen übersehen (z. B. ein Sonderfall, der im Testfall gar nicht vorkam), kann die Software technisch fehlerfrei laufen und trotzdem den eigentlichen Bedarf verfehlen. Das zeigt, warum Unit-Tests und UAT unterschiedliche Dinge prüfen und beide notwendig sind – die eine testtechnische, die andere die fachliche/praktische Korrektheit.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Möglichst viele End-to-End-Tests über die grafische Oberfläche sind der beste Testansatz | Das "Ice-Cream-Cone"-Antimuster – die Testpyramide sollte breit auf Unit-Tests, schmal auf E2E-Tests aufbauen, da UI-Tests langsam und brüchig sind |
| 2 | Blackbox- und Whitebox-Testing sind austauschbar, da beide "Fehler finden" | Blackbox prüft ohne Quellcode-Einsicht gegen die Anforderungen (Nutzerperspektive), Whitebox leitet Tests aus der internen Struktur/dem Kontrollfluss ab (z. B. Anweisungs-/Zweigüberdeckung) |
| 3 | Ein Entwickler ist grundsätzlich für Blackbox-Tests des eigenen Codes ungeeignet | Entwickler:innen können Blackbox-Tests durchführen – problematisch ist die fehlende Unabhängigkeit, nicht die Rolle an sich; ergänzende Tests durch unabhängige Personen erhöhen die Fehlerfindungswahrscheinlichkeit |
| 4 | Ein Breakpoint in einer 10.000-fach durchlaufenen Schleife lässt sich nur durch wiederholtes Klicken auf "Continue" überstehen | Ein bedingter Breakpoint (z. B. bei einem bestimmten Schleifenwert) löst genau dieses Problem gezielt |
| 5 | "CD" bedeutet immer Continuous Deployment, also automatisches Ausrollen auch bei fehlschlagenden Tests | "CD" kann Continuous Delivery (bis zur Auslieferungsbereitschaft, manuelle Freigabe möglich) oder Continuous Deployment (vollautomatisch, keine manuelle Freigabe) bedeuten – beide laufen nur bei erfolgreicher vorheriger Prüfung an |
| 6 | Ein fehlgeschlagener CI-Test blockiert automatisch jeden Merge | Das geschieht nur, wenn der Check durch Branch-Schutzregeln bzw. erforderliche Statuschecks entsprechend konfiguriert wurde |
| 7 | 100% Code Coverage bedeutet, dass die Software fehlerfrei ist | Coverage zeigt nur, welcher Code während der Tests ausgeführt wurde – sie beweist weder vollständige Anforderungsabdeckung noch sinnvolle Prüfungen (Assertions) noch fehlerfreie Fachlogik |
| 8 | UAT muss zwingend von echten Endnutzer:innen und völlig unangeleitet erfolgen | UAT kann auch durch Auftraggeber:in, Fachabteilung oder Key User erfolgen und anhand vorbereiteter Szenarien ablaufen – entscheidend ist die Prüfung fachlicher Akzeptanzkriterien, nicht eine bestimmte Personengruppe oder völlige Anleitungsfreiheit |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **Test-Driven Development (TDD)** (→ Abschnitt 1): Das Red-Green-Refactor-Muster – zuerst einen fehlschlagenden Test schreiben, dann minimalen Code zur Erfüllung, anschließend Code strukturieren/verbessern.
- **Äquivalenzklassenbildung** (→ Abschnitt 2.1): Wie das Testen eines repräsentativen Werts aus einem gültigen Wertebereich statt jeder einzelnen Zahl Zeit spart.
- **Code-Reviews und Pair Programming** (→ Abschnitt 2): Qualitätssicherung durch gegenseitige Codeprüfung oder gemeinsames Programmieren zu zweit, als ergänzende Methode neben automatisierten Tests.
- **Debugging von asynchronem/nebenläufigem Code** (→ Abschnitt 3): Warum das Debuggen von Multi-Threading/Async-Code deutlich schwieriger ist als bei klassischem prozeduralem Code.

> 🔍 **Hinweis zur Selbstrecherche:** Konkrete CI/CD-Tool-Konfiguration (z. B. eine GitHub-Actions-Workflow-Datei) und Bugtracker-Details (Jira, Mantis, Redmine) sind stark werkzeugabhängig und ändern sich häufig – für die praktische Anwendung lohnt sich ein Blick in die jeweils aktuelle Tool-Dokumentation.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne die drei Ebenen der Testpyramide. | Unit-Tests (Basis), Integrationstests (Mitte), System-/End-to-End-Tests (Spitze) |
| 2 | Was ist das "Ice-Cream-Cone"-Antimuster? | Eine umgekehrte Testpyramide mit zu vielen langsamen UI-Tests und zu wenigen schnellen Unit-Tests |
| 3 | Was unterscheidet Blackbox- von Whitebox-Testing? | Blackbox: kein Quellcode-Zugriff, Tests aus Anforderungen/Ein-Ausgaben abgeleitet; Whitebox: Quellcode-Zugriff, Tests aus interner Struktur/Kontrollfluss abgeleitet, z. B. zur Anweisungs- oder Zweigüberdeckung |
| 4 | Nenne die fünf Standardbestandteile eines formalen Testfalls. | Test-ID/Titel, Vorbedingungen, Testschritte, erwartetes Ergebnis, tatsächliches Ergebnis |
| 5 | Was ist ein bedingter Breakpoint? | Ein Haltepunkt, der nur unter einer bestimmten Bedingung (z. B. Schleifenwert) auslöst |
| 6 | Was ist der Unterschied zwischen "Step Over" und "Step Into"? | Step Over führt eine Zeile aus, ohne in Funktionsaufrufe einzutauchen; Step Into springt in die aufgerufene Funktion hinein |
| 7 | Was bewirkt Continuous Integration (CI)? | Automatisiertes Integrieren, Bauen und Prüfen von Änderungen (z. B. bei Push/Pull Request); eine Merge-Blockierung bei fehlgeschlagenen Tests setzt erforderliche Statuschecks/Branch-Regeln voraus |
| 8 | Was prüft ein Linter? | Führt eine statische Analyse des Quellcodes durch (mögliche Fehler, verdächtige Konstruktionen, Stilverstöße), ohne ihn auszuführen |
| 9 | Wer führt UAT durch, und wer nicht? | Auftraggeber:in, Fachabteilung, Key User oder repräsentative Endnutzer:innen – nicht die Entwickler:innen |
| 10 | Welche rechtliche Bedeutung hat ein unterschriebenes Abnahmeprotokoll? | Dokumentiert die Abnahmeentscheidung; bei einem Werkvertrag wird nach § 641 BGB die Vergütung grundsätzlich mit der Abnahme fällig – die genauen Rechtsfolgen hängen vom jeweiligen Vertrag ab |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Testpyramide** | Viele Unit-Tests, weniger Integrationstests, wenige E2E-Tests |
| **Regressionstest** | Prüft, ob neuer Code alte Funktionalität nicht beschädigt |
| **Blackbox-Testing** | Testen ohne Quellcode-Einsicht, gegen Anforderungen |
| **Whitebox-Testing** | Testen mit Quellcode-Einsicht, Tests aus interner Struktur/Kontrollfluss abgeleitet |
| **Testfall** | Test-ID, Vorbedingungen, Schritte, erwartetes/tatsächliches Ergebnis |
| **Breakpoint** | Haltepunkt, an dem der Debugger das Programm pausiert |
| **Step Over / Step Into** | Zeile ausführen ohne/mit Eintauchen in Funktionsaufrufe |
| **CI (Continuous Integration)** | Automatisierter Build + Test bei Änderungen (z. B. Push/Pull Request) |
| **Continuous Delivery** | Automatisiert bis zur Auslieferungsbereitschaft; Produktivfreigabe kann manuell erfolgen |
| **Continuous Deployment** | Automatisches Ausrollen ohne manuelle Freigabe, nach bestandener Prüfung |
| **Linter** | Statische Codeanalyse (mögliche Fehler, Stil), ohne den Code auszuführen |
| **UAT** | Fachlicher Abnahmetest durch Auftraggeber:in, Fachabteilung, Key User oder repräsentative Endnutzer:innen |
| **Abnahmeprotokoll** | Dokumentiert die Abnahmeentscheidung; kann bei einem Werkvertrag wichtige rechtliche Folgen haben (Fälligkeit der Vergütung, § 641 BGB) – Rechtsfolgen hängen vom Vertrag ab |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Testebene zuordnen | "Welche Testart passt zu Szenario X?" | Konkrete Begründung anhand von Isoliertheit/Umfang des Tests, nicht nur die Bezeichnung |
| Testfall schreiben | "Formulieren Sie einen Testfall für..." | Alle 5 Elemente (ID, Vorbedingung, Schritte, erwartetes/tatsächliches Ergebnis), konkret statt vage |
| Debugging-Szenario erklären | "Wie würden Sie Fehler X finden?" | Konkrete Debugger-Funktion (Breakpoint, Step Into/Over) nennen, nicht nur "debuggen" |
| CI/CD-Konzept erklären | "Was passiert bei X im CI/CD-Prozess?" | Reihenfolge Build → Test → (bei Erfolg) Delivery/Deployment korrekt wiedergeben, inkl. ob eine manuelle Freigabe dazwischenliegt |
| UAT einordnen | "Warum reicht Systemtest allein nicht aus?" | Unterschied technische vs. geschäftliche/praktische Korrektheit explizit benennen |

---

## 11. Merksätze für das Fachgespräch

> Die Testpyramide ist breit unten, schmal oben – viele schnelle Unit-Tests tragen mehr als wenige teure End-to-End-Tests.

> Blackbox testet von außen gegen die Anforderung, Whitebox testet von innen gegen den Code.

> Ein vages "sollte funktionieren" ist kein Testfall – erst ein konkretes, beobachtbares Ergebnis macht ihn reproduzierbar.

> Ein Debugger zeigt, was gerade wirklich passiert – `print()` zeigt nur, was man vorher zu fragen wusste.

> CI integriert, baut und prüft – Delivery hält das Ergebnis auslieferbar, Deployment rollt es automatisch aus – aber nur, wenn die vorherige Prüfung grün war.

> Entwickler prüfen, ob die Software technisch läuft; die Kundschaft prüft in der UAT, ob sie im Alltag wirklich hilft.

---

```yaml
dokument: LF5.5-wiki-artikel
themenfeld: "LF5.5 - Ensuring Quality"
titel: "Ensuring Quality"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-11
quellen_intern:
  - "LF5.5.1: The Testing Pyramid.md"
  - "LF5.5.2: Blackbox & Whitebox.md"
  - "LF5.5.3: The Art of Debugging.md"
  - "LF5.5.4: CI/CD Basics.md"
  - "LF5.5.5: User Acceptance Testing (UAT).md"
  - "Zusätzliche deutschsprachige Rechercheunterlagen vom Auftraggeber (siehe LF5.1-Historie) - insbesondere TDD/Red-Green-Refactor, Bugtracker-Systeme, Code-Reviews/Pair Programming ergänzend eingearbeitet"
quellen_fachlich:
  - titel: "Testpyramide, Blackbox/Whitebox-Testing (ISTQB-Terminologie), Debugging-Grundlagen, CI/CD-Konzepte, UAT"
    herausgeber: "Rohmaterial + Fachliteratur (etabliertes Software-Engineering-Standardwissen, u.a. ISTQB-Glossar)"
    status: "stabile, langjährig etablierte Konzepte - Grundkonzepte stabil, Terminologie/Abgrenzungen (Whitebox/Coverage, System- vs. E2E-Test) in Runde 2 extern geprüft und präzisiert"
  - titel: "§§ 640, 641 BGB (Abnahme, Fälligkeit der Vergütung beim Werkvertrag)"
    herausgeber: "Bundesministerium der Justiz (gesetze-im-internet.de)"
    status: "in Runde 2 ergänzt, da die ursprüngliche Aussage zum Abnahmeprotokoll rechtlich zu pauschal war; Rechtsdarstellung bewusst vereinfacht, keine Rechtsberatung"
  - titel: "CI/CD-Konfigurationsabhängigkeit (erforderliche Statuschecks, Branch-Schutzregeln)"
    herausgeber: "GitHub Docs (docs.github.com)"
    status: "in Runde 2 ergänzt; werkzeug-/konfigurationsabhängig, aktuelle Dokumentation bei praktischer Umsetzung prüfen"
review_historie:
  - runde: 1
    datum: 2026-09-11
    ergebnis: "Erstdraft erstellt. Rohmaterial (LF5.5.1-5, User-Story/Bloom-Format) deckte Testpyramide, Blackbox/Whitebox-Testing, Debugging, CI/CD und UAT vollständig und gut strukturiert ab. Mit der bereits vom Auftraggeber bereitgestellten deutschsprachigen Zusatzrecherche kombiniert (TDD/Red-Green-Refactor, Bugtracker-Systeme wie Jira/Mantis/Redmine, Code-Reviews/Pair Programming als ergänzende QS-Methoden neben automatisierten Tests). Anders als bei LF5.1/5.4 zunächst keine gesonderte Web-Verifikation vorgenommen, da die Kernkonzepte (Testpyramide, CI/CD-Grundprinzip, UAT) langjährig etabliertes, stabiles Software-Engineering-Wissen ohne Versions-/Datumsbezug sind - dieser Verzicht erwies sich in Runde 2 für den rechtlichen Abschnitt (Abnahmeprotokoll) als unzureichend, siehe dort. Bewusster Querverweis zu LF5.1 (Lastenheft als UAT-Grundlage) und LF5.3 (Versionsverwaltung im CI/CD-Kontext) ergänzt, um Wissen aus bereits fertigen Artikeln zu verknüpfen statt zu wiederholen. Auf Deutsch verfasst. Eigene Review nach Style-Guide-Checkliste direkt eingearbeitet: Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an vorhanden, Analogien aus mehreren Domänen (Restaurant-Testesser, verschlossenes Radio, Uhrmacher, Fabrik-Prüfstraße, Architekt/Hausabnahme)."
  - runde: 2
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (2 sehr umfangreiche Reviews) eingearbeitet, hohe Übereinstimmung bei den meisten Punkten. Wichtigster Fund, von beiden Reviews mit Gesetzeszitat bestätigt: Die Aussage zum Abnahmeprotokoll ('Projekt gilt offiziell als geliefert und kann abgerechnet werden') war rechtlich zu pauschal - nicht jedes Softwareprojekt ist automatisch ein Werkvertrag, und die rechtliche Wirkung hängt vom konkreten Vertrag ab; korrigiert mit Bezug auf §§ 640/641 BGB (Abnahme, Fälligkeit der Vergütung), nachträglich als Primärquelle im YAML ergänzt - Beleg dafür, dass der ursprüngliche Verzicht auf Web-Verifikation für den rechtlichen Abschnitt zu voreilig war. Ebenfalls von beiden Reviews bestätigt, mit ISTQB-Terminologie belegt: Whitebox-Testing war fälschlich auf 'jede if-Verzweigung/Schleife mindestens einmal durchlaufen' reduziert - das ist ein einzelnes Coverage-Kriterium, keine Definition von Whitebox-Testing; korrigiert, zusätzlich Hinweis ergänzt, dass Code Coverage ein Messwert ist, kein Qualitätsbeweis (neue Prüfungsfalle 7). Ebenfalls von beiden Reviews bestätigt, mit GitHub-Docs-Zitat: CI-Aussagen 'bei jedem Push' und 'blockiert Pull Request automatisch' stellten Konfigurationsbeispiele als zwingende Definition dar - präzisiert, dass Merge-Blockierung erforderliche Statuschecks/Branch-Regeln voraussetzt (neue Prüfungsfalle 6). Ebenfalls von beiden Reviews stark bestätigt: Continuous Delivery fehlte komplett neben Continuous Deployment - als eigene Zeile ergänzt (Tabelle, Cheatsheet, neue Prüfungsfalle 5), da die CD-Mehrdeutigkeit prüfungsrelevant ist. Ebenfalls von beiden Reviews bestätigt: UAT-Durchführung war auf 'tatsächliche Endnutzer:innen' verengt (in der Praxis auch Auftraggeber, Fachabteilung, Key User möglich) und die 'muss unangeleitet erfolgen'-Aussage war zu absolut (formale, moderierte UAT-Szenarien sind zulässig) - beide korrigiert (Tabelle, Prüfungsfalle 8, Selbsttest 9). UAT-Grundlage von 'ursprüngliches Lastenheft' auf 'vereinbarte fachliche Anforderungen, z.B. aus Lastenheft, Pflichtenheft, Vertrag oder User Stories' erweitert, da 'ursprünglich' genehmigte Änderungen ausgeschlossen hätte. Weitere Präzisierungen: Entwickler-als-Blackbox-Tester-Aussage von 'oft ungeeignet' zu 'fehlende Unabhängigkeit als eigentliches Problem' entschärft (Prüfungsfalle 3); System-/E2E-Test nicht mehr gleichgesetzt, Begriffsabgrenzung ergänzt; 'Hunderte Unit-Tests' auf 'typischerweise größter Anteil' entschärft; Linter-Beschreibung auf 'statische Analyse' präzisiert (statt pauschal 'Programmierfehler'); Debugger-Tastenkürzel F5/F10/F11 als VS-Code-Beispiele gekennzeichnet statt als Standard dargestellt; Git-Aussage 'verhindert gegenseitiges Überschreiben' korrigiert zu 'dokumentiert Änderungen, ermöglicht paralleles Arbeiten, hilft bei kontrolliertem Zusammenführen' (Mergekonflikte entstehen weiterhin); '45-Minuten-Pipeline'-Aussage mit konkreter Zahl entschärft zu allgemeinem Geschwindigkeits-/Staffelungsprinzip. YAML-Quellenblock um zwei Primärquellen ergänzt (BGB §§ 640/641, GitHub Docs zu Statuschecks). Vorschlag, 'IHK-Typfrage' durchgehend in 'prüfungsnahe Übungsfrage' umzubenennen, nicht übernommen - entspricht der durchgängigen Namenskonvention aller bisherigen Wiki-Artikel dieses Projekts (WiSo, LF4, LF8), Änderung hier hätte Inkonsistenz zur Artikelserie erzeugt."
  - runde: 3
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet. Alle drei Reviews bestätigen unabhängig dasselbe Muster: In Runde 2 wurde der Haupttext (Abschnitt 4, CI/CD) gründlich präzisiert, aber Selbsttest 7/8, Cheatsheet (UAT, Abnahmeprotokoll), Merksatz und Prüfungstaktik-Zeile wurden dabei nicht mitgezogen und widersprachen dem korrigierten Haupttext - klassischer Fall des in der Workflow-Datei beschriebenen 'Haupttext korrigiert, Nebenstelle vergessen'-Musters. Alle betroffenen Stellen jetzt nachgezogen: Selbsttest 7 (CI) und 8 (Linter) an die Abschnitt-4-Präzisierung angepasst; Selbsttest 3 (Whitebox) um 'Code Coverage als Beispielmethode statt alleiniger Fokus' präzisiert; Cheatsheet UAT und Abnahmeprotokoll konsistent zum Haupttext gemacht; Merksatz CI/CD um Delivery/Deployment-Unterscheidung erweitert; Prüfungstaktik-Zeile CI/CD um Delivery ergänzt; Abschnittstitel 4 und Kernfrage 4 im Kopf-Tableau von 'CI und CD' auf 'CI, Delivery und Deployment' erweitert (inkl. Anker-Link-Anpassung). Von zwei Reviews bestätigt: CI/CD-Einleitungssatz 'führen bei jedem Push automatisch Skripte aus' war weiterhin zu absolut, obwohl die Tabelle direkt darunter schon korrekt war - präzisiert zu 'können je nach Workflow-Konfiguration bei Pushes, Pull Requests oder zeitgesteuert' ausführen. Debugger-Musterantwort 'alle aktuell existierenden Variablenwerte gleichzeitig' auf 'im aktuellen Debugging-Kontext verfügbare Variablen' präzisiert (Debugger zeigt scope-abhängig, nicht buchstäblich alles). Eine Review behauptete umfangreiche kaputte Markdown-Strukturen (zusammengelaufene Tabellen/Blockquotes) und eine beschädigte YAML-Struktur - beim Abgleich mit der tatsächlichen Datei (grep + Python-YAML-Parser) nicht bestätigt, vollständig valide, nicht übernommen (bekanntes Muster in diesem Projekt, vermutlich Kopier-/Darstellungsartefakt bei der reviewenden KI selbst)."
  - runde: 4
    datum: 2026-09-11
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): gesamte Datei durchgelesen, mehrere echte Konsistenzreste gefunden und behoben – Prüfungsfalle 2 und Cheatsheet-Whitebox-Eintrag trugen noch die alte 'Fokus Code Coverage'-Formulierung, obwohl Abschnitt 2.1 und Selbsttest 3 bereits präzisiert waren; die Breakpoint-/Variablenansicht-Zeilen in der Konzept-Tabelle waren nicht konsistent zur bereits in Runde 3 präzisierten Musterantwort ('läuft mit voller Geschwindigkeit', 'jeder Variable im Speicher'); die Einleitung zu Abschnitt 3.1 stellte den Debugger unpräzise als grundsätzlich professioneller dar als print()/Logging, obwohl Letzteres in verteilten/produktiven Systemen weiterhin wichtig ist. Alle vier Stellen nachgezogen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-11) – Freigabe durch Autor:in bestätigt"
```