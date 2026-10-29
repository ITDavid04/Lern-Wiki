# LF10a Teil 1 – Konzeption & Struktur

> **Zielgruppe:** Umschüler FIAE, 2. Lehrjahr (Aufbaustufe – ab hier trennen sich FIAE und FISI im Lernkontext)
> **Prüfungsrelevanz:** Schwerpunkt AP2 im Prüfungsbereich **"Planen eines Softwareproduktes"** (schriftlich, 90 Minuten, 10% Gewichtung) – insbesondere die dort explizit geprüften Punkte "Programmspezifikationen anwendungsgerecht festlegen", "Bedienoberflächen funktionsgerecht und ergonomisch konzipieren" sowie "Maßnahmen zur Qualitätskontrolle planen und durchführen". Einzelne Grundlagen können bereits in AP1 vorkommen; projektbezogene UI-Entscheidungen können zudem im Bereich "Planen und Umsetzen eines Softwareprojektes" und im Fachgespräch relevant werden. Nicht jedes hier behandelte Detailkonzept ist automatisch ein eigenständiger Prüfungsgegenstand.
> **Lernzeit:** Ca. 2,5–3 Stunden Lesen/Durcharbeiten, +1,5–2 Stunden für Anforderungs-/Prototyp-Übungen
> **Status:** Final
> **Stand:** 2026-09-14
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Hinweis zur Abgrenzung:** LF10a behandelt die Entwicklung von Benutzeroberflächen und ist der erste Teil einer dreiteiligen Serie (Teil 1: Konzeption & Struktur; Teil 2: Interaktion & Daten; Teil 3: Sicherheit, Test & Abnahme). Allgemeine Anforderungsanalyse-Grundlagen (Lastenheft/Pflichtenheft, Kano-Modell) wurden bereits in LF5.1 behandelt – hier geht es um die UI-spezifische Anwendung davon.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie werden aus einem Ist-Prozess und Nutzergruppen prüfbare, priorisierte UI-Anforderungen? | [→ 1. Anforderungen und Zielgruppen](#1-anforderungen-und-zielgruppen) |
| 2 | Worin liegt der Unterschied zwischen MVC, Client-Server und einer Drei-Schichten-Architektur? | [→ 2. Informationsarchitektur und Prototyp](#2-informationsarchitektur-und-prototyp) |
| 3 | Welches UX-/Usability-Testverfahren passt zu welcher Fragestellung? | [→ 2. Informationsarchitektur und Prototyp](#2-informationsarchitektur-und-prototyp) |
| 4 | Warum beschreibt HTML zuerst Bedeutung, und wann ist ARIA gerechtfertigt? | [→ 3. Semantisches HTML und Barrierefreiheit](#3-semantisches-html-und-barrierefreiheit) |
| 5 | Wie werden Breakpoints begründet, und welche WCAG-2.2-AA-Kriterien gelten für responsive Oberflächen? | [→ 4. Responsive Design und Designsystem](#4-responsive-design-und-designsystem) |

---

## 1. Anforderungen und Zielgruppen

> **Grundprinzip:** Ein Kunde, der "ein Portal" bestellt, hat schon eine Lösung im Kopf – aber noch kein beschriebenes Problem. Ein Architekt, der sofort zu bauen beginnt, ohne zu fragen, wer im Haus wohnt und wofür jeder Raum gebraucht wird, baut am Bedarf vorbei. Erst der verstandene Ablauf rechtfertigt den Entwurf.

### 1.1 Problemraum vor Lösungsraum

Zum **Problemraum** gehört alles, was heute schon da ist: der aktuelle Ablauf, die Menschen, die daran beteiligt sind, die Informationen, die sie brauchen, sichtbare Schwierigkeiten und ungeklärte Punkte. Erst wenn es um konkrete Bildschirme, Funktionen oder Techniken geht, bist du im **Lösungsraum**. Jede Aussage aus der Analyse ordnest du einer von drei Klassen zu:

| Klasse | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Belegt** | Es gibt eine Grundlage: den Auftrag, eine eigene Beobachtung, ein Prozessdokument oder eine bestätigte Aussage | 🔴 |
| **Annahme** | Plausibel, aber noch nicht bestätigt | 🔴 |
| **Offene Frage** | Für eine Entscheidung fehlt Information | 🔴 |

**Stakeholder** sind alle, die mit der Lösung zu tun haben: wer sie bestellt, bedient, betreibt oder abnimmt, und wer ihre Folgen spürt. Die Nutzer:innen sind darunter eine wichtige Gruppe, aber eben nur eine.

> **Wichtig für die Prüfung:** Was plausibel klingt, ist noch nicht belegt. Steht eine Annahme ungekennzeichnet im Konzept, bauen Anforderungen und Entwurf womöglich auf Sand. 🔴

### 1.2 Ist-Prozess, Medienbruch und Personas

Zu jedem Prozessschritt gehören: ausführende Rolle, benötigte/erzeugte Informationen, verwendetes Medium, mögliche Rückfrage/Ausnahme, sichtbares Zwischenergebnis. Ein **Medienbruch** liegt beim Wechsel zwischen nicht durchgängig verbundenen Medien/Systemen vor. Für die Anforderungsanalyse relevant wird er insbesondere dann, wenn daraus eine beobachtbare negative Folge entsteht – etwa Doppelarbeit, Verzögerung oder Übertragungsfehler.

Eine **Persona** fasst das Wissen über eine wichtige Nutzergruppe zu einem Arbeitsmodell zusammen. Eine ausgedachte Lebensgeschichte ist sie nicht. Ihre Grundlage sind Beobachtungen, Interviews oder andere Nutzungsdaten. Fehlen diese noch, nennt man sie Proto-Persona und kennzeichnet sie klar als Annahme (siehe die drei Klassen aus 1.1). Wichtig sind nur Merkmale, die den Entwurf beeinflussen: Ziele und Hauptaufgaben, wie oft und unter welchem Zeitdruck gearbeitet wird, Umgebung und Gerät, nötige Informationen, Vorerfahrung und Einschränkungen. Zum **Nutzungskontext** gehört, wo und wie die Aufgabe erledigt wird, zum Beispiel im Stehen in der Lagerhalle mit Arbeitshandschuhen oder in Ruhe am Schreibtisch.

> **Wichtig für die Prüfung:** Alter, Name oder Hobbys sind nur relevant, wenn sie nachweisbar eine UI-Entscheidung beeinflussen (Navigation, Inhalt, Bedienung, Darstellung) – sonst gehören sie nicht in die Persona. 🟡

### 1.3 User Flow, Anforderungen und Akzeptanzkriterien

Ein **User Flow** zeigt den Weg vom Ausgangspunkt einer Aufgabe bis zum sichtbaren Ergebnis: Ziel, Schritte, Entscheidungen und Rückmeldungen, dazu Fehler, Abbrüche und Wege zurück. Der **Happy Path** beschreibt nur den glatten Fall, in dem alles klappt. Er ist ein Ausschnitt des Flows und ersetzt die Fehler-, Abbruch- und Korrekturwege nicht.

**Funktionale Anforderungen** beschreiben, was ein System tun bzw. ermöglichen soll (z. B. "Nutzer können eine Anfrage erfassen"); **nichtfunktionale Anforderungen** beschreiben Qualitätsmerkmale und Randbedingungen, unter denen dies geschieht (z. B. "Das Formular muss per Tastatur bedienbar sein", "Die Antwort soll innerhalb von 2 Sekunden erfolgen"). Rechtliche/qualitative Rahmenbedingungen wie Datenschutz können dabei sowohl nichtfunktionale Anforderungen erzeugen als auch konkrete funktionale Anforderungen nach sich ziehen (z. B. "Nutzer können ihre Einwilligung widerrufen"). Priorisierung nach **Muss/Soll/Kann**:

| Stufe | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Muss** | Fehlt sie, ist das Kernziel nicht erreicht oder eine feste Vorgabe verletzt | 🔴 |
| **Soll** | Bringt viel, darf aber mit guter Begründung später kommen | 🔴 |
| **Kann** | Nettes Extra, wenn Zeit bleibt und das Risiko klein ist | 🟡 |

Mit einem **Akzeptanzkriterium** lässt sich nachprüfen, ob eine Anforderung erfüllt ist. Verbreitet ist das Muster Gegeben, Wenn, Dann (Given/When/Then): *"Gegeben ist ein bestimmter Startzustand. Wenn jemand eine bestimmte Aktion ausführt, dann zeigt das System ein Ergebnis, das man sehen und prüfen kann."* Auf den genauen Wortlaut kommt es nicht an, wohl aber darauf, dass jede Person beim Testen zum selben Urteil kommt. "Intuitiv", "modern" oder "schnell" sind keine Kriterien, solange nicht dasteht, woran man das messen oder sehen soll.

> **IHK-Typfrage:** *"Ein Kunde fordert: 'Die Anfrageerfassung soll benutzerfreundlich sein.' Formulieren Sie eine prüfbare Anforderung mit Akzeptanzkriterium."*
> **Musterantwort:** "Benutzerfreundlich" benennt weder beobachtbares Verhalten noch einen Grenzwert und ist damit kein Akzeptanzkriterium. Zunächst wird der konkrete Nutzungskontext geklärt (z. B. Erfassung unter Zeitdruck in der Werkhalle). Daraus könnte eine prüfbare Anforderung werden: "Für die vollständige Erfassung einer Standardanfrage sind höchstens fünf Pflichtfelder erforderlich." Das braucht zwei Akzeptanzkriterien, da ein einzelnes die Anforderung nicht vollständig abdeckt: (1) "Gegeben ist das leere Formular. Wenn die als Pflichtfeld gekennzeichneten Eingaben gezählt werden, dann sind höchstens fünf vorhanden." (2) "Gegeben ist das leere Formular. Wenn alle Pflichtfelder gültig ausgefüllt und abgesendet werden, dann erscheint eine Eingangsbestätigung mit sichtbarer Vorgangsnummer." Die Prüfung umfasst eine Inspektion der Pflichtfelder sowie einen positiven und negativen Akzeptanztestfall.

### 1.4 Datenbedarf und Datensparsamkeit

Zu jedem Datenfeld klärst du: Wofür wird es gebraucht und welche Entscheidung hängt daran? Wer braucht es? Ist es Pflicht oder freiwillig, wer darf es sehen, wie schutzbedürftig ist es, und wann wird es gelöscht? **Datensparsamkeit** heißt: Personenbezogene Daten werden nur erhoben, wenn der festgelegte Zweck sie wirklich verlangt. Freitextfelder sind heikel, weil Menschen dort alles Mögliche hineinschreiben.

> **Typische Prüfungsfalle:** "Ausgeblendete oder deaktivierte UI-Funktionen sind bereits eine Berechtigungsprüfung" – das stimmt nicht. Ausblenden kann Orientierung verbessern, verhindert aber keinen manipulierten Aufruf. Echte Autorisierung muss serverseitig erfolgen (vertieft in LF10a Teil 3). 🔴

---

## 2. Informationsarchitektur und Prototyp

> **Grundprinzip:** Wer die Menüpunkte einfach aus der internen Ablage einer Firma übernimmt ("Vorgänge", "Archiv", "Sonstiges"), lässt neue Nutzer:innen ratlos zurück: Wo fange ich an, wo steht mein Anliegen? Eine brauchbare Struktur entsteht erst, wenn die Inhalte nach den Aufgaben der Nutzer:innen sortiert sind.

### 2.1 Arten von Benutzerschnittstellen

Eine **Benutzerschnittstelle** ist Teil eines Mensch-Maschine-Systems (MMS). Aufgabe und Nutzungskontext entscheiden über die passende Interaktionsform:

| Kürzel | Art | Kennzeichen | IHK-Relevanz |
| --- | --- | --- | --- |
| CLI | Command Line Interface | Textbasierte Befehlseingabe, ressourcensparend, gut automatisierbar | 🟡 |
| GUI | Graphical User Interface | Grafische Elemente (Fenster, Schaltflächen, Eingabefelder) | 🔴 |
| NUI | Natural User Interface | Berührung/Geste | 🟢 |
| VUI | Voice User Interface | Sprachbasierte Ein-/Ausgabe | 🟢 |

🟢 *Randnotiz:* Weitere, seltenere Kategorien sind **OUI** (Organic User Interface, verformbare/räumliche Oberflächen) und **BCI** (Brain-Computer Interface, Steuerung über neuronale Signale, oft als assistive Schnittstelle) – für den FIAE-Schwerpunkt dieses Artikels nachrangig.

> **Wichtig für die Prüfung:** Die Einteilung sagt, wie man mit dem System arbeitet, nicht wie gut es ist. Für eine Admin-Aufgabe, die immer gleich abläuft, ist eine CLI oft die bessere Wahl als eine GUI. 🟢

### 2.2 Informationsarchitektur und Architekturmuster

Bewährt hat sich diese Reihenfolge: (1) Aufgaben und nötige Informationen der Nutzer:innen sammeln, (2) Zusammengehöriges bündeln, (3) jedem Bündel einen verständlichen Namen geben, (4) Wichtiges nach vorn sortieren, (5) erst dann Seiten und Navigation bauen. Das **Mental Model** ist das Bild, das Nutzer:innen im Kopf von einem Ablauf haben. Beschriftungen richten sich danach und nicht nach Feldnamen aus der Datenbank.

Drei häufig verwechselte Architekturmuster beantworten unterschiedliche Fragen:

| Muster | Beantwortet | Kernidee | IHK-Relevanz |
| --- | --- | --- | --- |
| **Drei-Schichten-Architektur** | Welche fachlichen Zuständigkeiten gibt es? | Trennt Präsentation, Anwendungslogik, Datenhaltung | 🔴 |
| **Client-Server-Architektur** | Wie sind Dienste auf Systeme verteilt? | Client fordert Leistung an, Server stellt sie über Schnittstelle bereit | 🔴 |
| **Model View Controller (MVC)** | Wie sind Darstellung, Eingabe und Modell strukturiert? | Model = Daten/Zustand, View = Darstellung, Controller = Interaktionsverarbeitung | 🔴 |

> **Wichtig für die Prüfung:** Die drei Begriffe sind **keine Synonyme** – wer sie austauschbar verwendet, dokumentiert eine Systemgrenze falsch. Sie schließen sich auch nicht gegenseitig aus: MVC beschreibt häufig die interne Struktur *innerhalb* der Präsentationsschicht einer Drei-Schichten-Architektur, während Client-Server zusätzlich beschreibt, wie diese Schichten auf kommunizierende Systeme verteilt sind. Rollenbezogene Navigation (unterschiedliche Menüs je Rolle) ist zudem eine Darstellungsentscheidung, **keine Sicherheitsgrenze** – die lässt sich im Browser manipulieren; echte Autorisierung bleibt Backend-Aufgabe. 🔴

### 2.3 Design Thinking, Prototypenstufen und UI-Zustände

**Design Thinking** ist ein nutzerzentrierter, iterativer Prozessrahmen (verstehen/beobachten → Problem schärfen → Ideen entwickeln → prototypisieren → testen) – keine einmalig linear abzuarbeitende Phasenfolge.

| Stufe | Detailgrad | IHK-Relevanz |
| --- | --- | --- |
| **Sketch** | Schnelle, bewusst grobe Ideenskizze | 🟡 |
| **Wireframe** | Grobe Struktur, Reihenfolge, Bedienelemente | 🔴 |
| **Mockup** | Visuell ausgearbeitet, meist noch statisch | 🟡 |
| **Prototyp** | Prüfbare Simulation eines Ablaufs | 🔴 |

Schon ein Prototyp sollte mindestens fünf Zustände zeigen, je nach Anwendung kommen weitere hinzu (etwa "deaktiviert", "keine Berechtigung", "offline"): **Normal** (die Daten und Aktionen sind da), **Leer** (nichts vorhanden, mit Grund und Hinweis, was man tun kann), **Laden** (etwas läuft, die Oberfläche zeigt es an), **Fehler** (was schiefging, was das bedeutet und wie es weitergeht), **Erfolg** (was erreicht ist und was als Nächstes möglich ist). In jedem Zustand müssen Nutzer:innen drei Dinge verstehen: was gerade los ist, was das für sie heißt und welcher Schritt jetzt möglich ist.

> **IHK-Typfrage:** *"Ein Prototyp zeigt nur den Normalzustand einer Anfrageliste. Welches Risiko birgt das, und welche Zustände fehlen mindestens?"*
> **Musterantwort:** Werden Leer-, Lade-, Fehler- und Erfolgszustand erst beim Programmieren bedacht, passt der bereits getestete Erfolgsentwurf oft nicht mehr zu ihnen, und wichtige Korrekturwege fehlen im späteren Test. Mindestens fehlen: der Leerzustand (z. B. "Noch keine Anfragen erfasst" mit einem Hinweis, wie man eine neue Anfrage anlegt), der Ladezustand (Rückmeldung, während Daten geladen werden), der Fehlerzustand (z. B. Ladefehler mit Wiederholungsoption) und der Erfolgszustand nach einer abgeschlossenen Aktion.

### 2.4 Usability, UX und die sieben Interaktionsprinzipien

**Usability** (Gebrauchstauglichkeit, nach ISO 9241-11): Erreichen bestimmte Nutzer:innen in einem bestimmten Umfeld ihr Ziel, ohne unnötigen Aufwand und mit einem guten Gefühl? **User Experience (UX)** geht weiter: Sie schließt ein, was Menschen vor, während und nach der Nutzung erwarten, empfinden und wie sie reagieren.

Die sieben Interaktionsprinzipien nach **DIN EN ISO 9241-110:2020**:

| Prinzip | Kernaussage | IHK-Relevanz |
| --- | --- | --- |
| Aufgabenangemessenheit | Unterstützt die Aufgabe ohne unnötige Schritte | 🟡 |
| Selbstbeschreibungsfähigkeit | Zustand und nächste Schritte sind verständlich | 🟡 |
| Erwartungskonformität | Begriffe/Reaktionen entsprechen dem Nutzungskontext | 🟡 |
| Erlernbarkeit | Bedienung mit vertretbarem Aufwand erschließbar | 🟡 |
| Steuerbarkeit | Ablauf, Richtung, Tempo beeinflussbar (inkl. Unterbrechbarkeit, Flexibilität, Individualisierbarkeit) | 🟡 |
| Robustheit gegen Benutzungsfehler | Fehler werden vermieden, erkannt, korrigierbar | 🟡 |
| Benutzerbindung | Fördert Vertrauen, ohne manipulative Gestaltung | 🟢 |

> **Wichtig für die Prüfung:** Die Prinzipien sind Blickwinkel für die Bewertung, keine Checkliste mit technischen Einzelregeln. Für einen konkreten Entwurf musst du sie erst in Kriterien übersetzen, die man beobachten kann. 🟡

### 2.5 UX-Testverfahren passend auswählen

Ein **Usability-Test** schaut, wie gut typische Nutzer:innen mit einem Entwurf, Prototyp oder fertigen Produkt echte Aufgaben erledigen. Getestet wird das Produkt, nicht der Mensch. Die Testaufgabe beschreibt, was erreicht werden soll, und verrät nicht, wo man klicken muss. Schlecht: "Öffne das Menü und wähle Export." Gut: "Schick deiner Kollegin die Liste der offenen Aufträge." Jeder Befund hält fest: Aufgabe, was beobachtet wurde, welches Problem dahintersteckt, welche Folgen es hat, wie dringend es ist und was entschieden wird. Was du gesehen hast und wie du es deutest, schreibst du getrennt auf.

| Verfahren | Liefert | IHK-Relevanz |
| --- | --- | --- |
| Kontextanalyse | Beobachtung/Befragung im tatsächlichen Nutzungskontext | 🟡 |
| Fokusgruppe | Moderierte Gruppendiskussion mit Zielgruppe | 🟡 |
| Online-Befragung | Rückmeldung vieler Personen, ohne Verhaltensbeobachtung | 🟡 |
| Expertenbasierte Überprüfung (z. B. heuristische Evaluation) | Fachkundige Prüfung anhand Heuristiken | 🔴 |
| Labortest | Kontrollierte Aufgabenbearbeitung, gezielte Beobachtung | 🔴 |
| Eye-Tracking | Blickverlauf als ergänzender Hinweis (erklärt Ursache nicht allein) | 🟢 |

> **Wichtig für die Prüfung:** Für einen **Usability-Test** muss die Software noch nicht fertig sein, ein Papierentwurf oder Klickprototyp reicht. Ein **Akzeptanztest** fragt etwas anderes: Sind die vorher vereinbarten Anforderungen und Akzeptanzkriterien erfüllt? Beide Tests können denselben Ablauf durchspielen, sie stellen aber andere Fragen und werten anders aus. 🔴

---

## 3. Semantisches HTML und Barrierefreiheit

> **Grundprinzip:** Ein `<button>` und ein gestaltetes `<div>` sehen auf dem Bildschirm vielleicht gleich aus. Für Tastatur und Screenreader sind sie es nicht: Der echte Button ist von Haus aus als Schaltfläche erkennbar, per Tab erreichbar und reagiert auf Enter und Leertaste, das `<div>` kann nichts davon. HTML legt zuerst fest, was etwas ist, und erst danach, wie es aussieht.

### 3.1 Elemente, Struktur und Dokumentreihenfolge

Wichtige Strukturelemente: `<header>` (Kopfbereich), `<nav>` (Navigationsgruppen), `<main>` (eindeutiger Hauptinhalt), `<section>` (thematischer Abschnitt mit Überschrift), `<aside>` (Ergänzung), `<footer>` (Abschluss). Eine `<div>` ist ein **neutraler Container** ohne automatische Semantik – für Aktionen wird grundsätzlich `<button>` verwendet, für Navigation `<a href="…">`.

Die **Dokumentreihenfolge**, also die Reihenfolge im HTML-Quelltext, bestimmt, wie vorgelesen wird, wie die Tab-Taste springt und wie die Seite ohne CSS aussieht. Überschriften-Ebenen (`<h1>` bis `<h6>`) geben die **Gliederung** wieder, nicht die gewünschte Schriftgröße. Ein Linktext muss auch allein verständlich sein, denn Screenreader listen Links oft ohne den Satz drumherum auf: "Rechnung März herunterladen" statt "hier klicken".

### 3.2 Zugängliche Formulare

```html
<div class="field">
  <label for="room-count">Personenzahl</label>
  <input id="room-count" name="roomCount" type="number"
         min="1" max="60" required
         aria-describedby="room-count-hint">
  <p id="room-count-hint">Zahl zwischen 1 und 60.</p>
</div>
```

Jedes Eingabefeld braucht einen Namen, den auch Hilfsmittel auslesen können, am einfachsten ein sichtbares `<label>`. **Ein Platzhalter ersetzt kein Label**: Er ist weg, sobald man tippt, und meist schwach im Kontrast. Optionen, die zusammengehören, fasst du mit `<fieldset>` zusammen und gibst der Gruppe mit `<legend>` eine Überschrift.

### 3.3 WCAG, ARIA und die Prüfperspektive Name/Rolle/Zustand

Die **WCAG (Web Content Accessibility Guidelines)** legen prüfbare Erfolgskriterien fest, die für jede Technik gelten. Sie sind nach vier Grundsätzen geordnet, den **POUR-Prinzipien**: **P**erceivable (wahrnehmbar), **O**perable (bedienbar), **U**nderstandable (verständlich), **R**obust (robust). Jedes Kriterium hat eine von drei Stufen: **A** (das Minimum), **AA** (das übliche Ziel, auch in diesem Artikel), **AAA** (die höchste Stufe, für viele Inhalte nicht voll erreichbar). **ARIA** kommt nur ins Spiel, wenn HTML eine Bedeutung oder einen Zustand nicht ausdrücken kann. Die wichtigste ARIA-Regel ist deshalb: Gibt es ein passendes HTML-Element, nimm das. ARIA ändert außerdem **kein** Verhalten, eine Rolle macht ein Element weder bedienbar noch per Tastatur erreichbar.

Prüfperspektive **Name, Rolle, Wert/Zustand**: Wie heißt das Element für assistive Technologien? Welche Rolle hat es (Link, Schaltfläche, Eingabe …)? Welcher Wert/Zustand ist relevant (ausgewählt, aufgeklappt …)?

Ein **Skip-Link** überspringt wiederkehrende Navigation und führt direkt zum Hauptinhalt. Eine **Live-Region** informiert über dynamische Statusänderungen ohne Fokusverschiebung – `role="status"` eignet sich für unkritische Meldungen; `role="alert"` besitzt eine dringliche, assertive Semantik und kann laufende Ausgaben unterbrechen (das genaue Verhalten hängt von Browser/assistiver Technik ab) und sollte deshalb nur für wirklich dringliche Meldungen verwendet werden.

> **IHK-Typfrage:** *"Ein Entwickler macht ein `<div>` mit `role="button"` klickbar, statt `<button>` zu verwenden. Bewerten Sie diese Entscheidung."*
> **Musterantwort:** `role="button"` ändert nur einen Teil der zugänglichen Beschreibung – die Rolle wird korrekt angekündigt. Fokussierbarkeit, Aktivierung mit Enter- und Leertaste, deaktivierter Zustand und das erwartete Tastenverhalten müssen dagegen zusätzlich manuell nachgebaut werden und werden dabei leicht vergessen oder fehlerhaft umgesetzt. Ein natives `<button>` liefert all das bereits automatisch und ist deshalb robuster – die Entscheidung sollte revidiert werden, sofern kein triftiger Grund gegen ein natives Element spricht.

### 3.4 Tastatur- und Strukturprüfung

So testest du ohne Maus: (1) Kommst du mit `Tab` und `Shift+Tab` an jedes bedienbare Element? (2) Lösen Enter und Leertaste Links und Buttons wie erwartet aus? (3) Siehst du immer, wo der Fokus gerade ist? (4) Kommst du aus Dialogen und Overlays wieder heraus? (5) Landet der Fokus nach einer Aktion an einer sinnvollen Stelle? Anschließend CSS ausschalten: Bleiben Inhalte, Überschriften, Reihenfolge verständlich?

> **Typische Prüfungsfalle:** Positive `tabindex`-Werte "reparieren" die Fokusreihenfolge nicht – sie legen eine zweite, schwer wartbare Reihenfolge über das Dokument, die bei jeder Änderung erneut von der visuellen/DOM-Reihenfolge abweicht. Besser: sinnvolle HTML-Reihenfolge ohne positive Werte. Ebenso: Ein automatisierter Accessibility-Scan ist ein **Teilnachweis**, kein Beweis vollständiger Barrierefreiheit – Verständlichkeit und vollständige Tastaturbedienung müssen manuell geprüft werden. 🔴

---

## 4. Responsive Design und Designsystem

> **Grundprinzip:** Ein Layout, das nur bei drei zufällig gewählten Bildschirmbreiten getestet wurde, ist so wenig "responsiv" wie eine Brücke, die nur bei drei zufälligen Belastungen geprüft wurde, "sicher" ist. Ein Breakpoint ist erst begründet, wenn dort tatsächlich ein Inhalts- oder Bedienproblem auftritt – nicht bei einem bekannten Gerätenamen.

### 4.1 Kaskade, Boxmodell und Einheiten

Widersprechen sich CSS-Regeln, entscheidet die **Kaskade**, welche gilt. Sie schaut auf Herkunft, `!important`, Spezifität und zuletzt auf die Reihenfolge. ID-Selektoren wiegen schwerer als Klassen und Elementnamen, taugen aber nicht als Alltagswerkzeug: Wer Konflikte immer mit noch spezifischeren Selektoren löst, hat schnell CSS, das sich kaum noch ändern lässt. Im **Boxmodell** liegen um den Inhalt eines Elements drei Schichten: `padding` innen, dann `border`, außen `margin`. Mit `box-sizing: border-box` zählen Padding und Rahmen zur angegebenen Breite, das macht Größen leichter planbar.

| Einheit | Zweck | IHK-Relevanz |
| --- | --- | --- |
| `rem` | Skalierbare Abstände/Schriftgrößen, relativ zur Basisschriftgröße des Dokuments (im Unterschied zu `em`, das relativ zum jeweiligen Elternelement skaliert und sich dadurch bei Verschachtelung aufsummieren kann) | 🔴 |
| `%`, `fr`, `minmax()`, `auto` | Flexible Verteilung | 🟡 |
| `ch` | Lesbare Textzeilen | 🟢 |
| `px` | Präzise Größenangaben für feine Details (z. B. Rahmenstärke); für responsive Hauptdimensionen nicht unnötig starr einsetzen | 🟡 |

Feste Pixelbreiten für große Bereiche gehen kaputt, sobald jemand zoomt, die Seite übersetzt wird oder der Text länger ausfällt.

### 4.2 Designsystem und Design-Tokens

Ein **Designsystem** bündelt Gestaltungsregeln, Bausteine zum Wiederverwenden und die Begründungen dahinter. Ein **Design-Token** gibt einem Gestaltungswert einen festen Namen:

```css
:root {
  --color-text: #1b1f24;
  --color-accent: #1558a6;
  --space-1: 0.5rem;
  --focus-ring: 0 0 0 0.2rem #ffbf47;
}
```

Der Name beschreibt den **Zweck**, nicht den konkreten Wert (`--color-danger` bleibt verständlicher als `--red-500`). Farbe allein darf nie einen Zustand erklären – Text, Symbol oder Struktur müssen ergänzen.

### 4.3 Layoutmodelle und Breakpoints

| Modell | Einsatz | IHK-Relevanz |
| --- | --- | --- |
| Normalfluss | Inhalte, die natürlich untereinanderstehen | 🟡 |
| Flexbox | Eindimensionale Anordnung (Zeile/Spalte) | 🔴 |
| Grid | Zweidimensionale Zeilen-/Spaltenbeziehungen | 🔴 |

**Mobile-first** heißt: Du baust zuerst eine schlichte Grundansicht und erweiterst sie, wenn mehr Platz da ist. Es heißt nicht, dass nur das Handy zählt. Einen **Breakpoint** setzt du an der Breite, an der Inhalte sich überlappen, schlecht lesbar werden oder die Bedienung unnötig mühsam wird.

> **Typische Prüfungsfalle:** CSS-`order` schiebt Elemente nur **optisch** umher. Im DOM, beim Vorlesen und beim Tabben bleibt die alte Reihenfolge, wer mit der Tastatur arbeitet, hüpft dann scheinbar kreuz und quer. Verständlich muss deshalb schon die Reihenfolge im HTML sein. 🔴

### 4.4 Ausgewählte WCAG-2.2-AA-Prüfwerte

Diese Tabelle enthält ausgewählte, modulübergreifend wiederkehrende Prüfwerte als Referenz sowohl für die Umsetzung (hier) als auch für die spätere Testphase (LF10a Teil 3) – sie ist **keine vollständige Kriterienliste**:

| Prüfgegenstand | Erfolgskriterium | Prüfwert |
| --- | --- | --- |
| Textkontrast | 1.4.3 | mind. 4,5:1 (mind. 3:1 bei großem Text) |
| Textvergrößerung | 1.4.4 | bis 200% ohne Inhalts-/Funktionsverlust |
| Reflow | 1.4.10 | bei 320 CSS-Pixel Breite alles nutzbar, ohne in zwei Richtungen scrollen zu müssen; Ausnahmen gelten nur für Inhalte, die zwingend zweidimensional sind (etwa Karten oder große Datentabellen), "ist halt breit" zählt nicht |
| Nichttextkontrast | 1.4.11 | mind. 3:1 für wesentliche grafische Objekte/Bedienelemente, soweit für Verständnis/Bedienung erforderlich |
| Sichtbarer Fokus | 2.4.7 | jedes tastaturbedienbare Element hat sichtbaren Fokusindikator |
| **Fokus nicht verdeckt** (neu in WCAG 2.2) | 2.4.11 | Ein fokussiertes Element darf durch vom Autor erstellten Inhalt (z. B. Sticky Header, Cookie-Banner) nicht vollständig verdeckt sein |
| Zielgröße | 2.5.8 | mind. 24×24 CSS-Pixel; kleinere Ziele nur über die im Kriterium definierten Ausnahmen (u. a. messbare Abstandsausnahme, Inline-Ziele) |
| Statusmeldungen | 4.1.3 | programmatisch ermittelbar, ohne dafür Fokus zu erhalten |

> **Wichtig für die Prüfung:** Wer diese Tabelle abhakt, hat noch **keine WCAG-Konformität nachgewiesen**. Für AA gehört viel mehr dazu, etwa vollständige Tastaturbedienung, eine sinnvolle Fokusreihenfolge, Beschriftungen, Fehlermeldungen, die Sprachangabe und eine einheitliche Navigation. Ein Kontrast-Tool rechnet nur. Welche Farben du gegeneinander misst und wie du Zustände wie Hover oder Fokus bewertest, entscheidest du selbst.

---

## 5. Zusammenspiel der Konzepte in LF10a Teil 1

Die vier Module bauen direkt aufeinander auf: **Anforderungen und Zielgruppen** (Abschnitt 1) liefern den belegten Ausgangspunkt – ohne verstandenen Ist-Prozess und geprüfte Datenbedarfe entsteht jede weitere Entscheidung auf unsicherem Grund. **Informationsarchitektur und Prototyp** (Abschnitt 2) übersetzen diese Anforderungen in Struktur, Navigation und testbare Entwürfe, bevor Code entsteht. **Semantisches HTML** (Abschnitt 3) macht diese Struktur für Menschen und assistive Technik tatsächlich zugänglich. **Responsive Design** (Abschnitt 4) sorgt dafür, dass diese zugängliche Struktur unter wechselnden Bedingungen (Bildschirmgröße, Zoom, Eingabemethode) verständlich bleibt. Die in Abschnitt 2.3 entworfenen UI-Zustände (Normal/Leer/Laden/Fehler/Erfolg) und die in Abschnitt 4.4 verankerte WCAG-Tabelle ziehen sich als roter Faden durch die gesamte LF10a-Serie bis zur Testphase in Teil 3.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung | IHK-Relevanz |
| --- | --- | --- | --- |
| 1 | Ein genannter Lösungsvorschlag ("ein Portal") beschreibt bereits das Problem | Problem- und Lösungsraum sind getrennt zu betrachten – erst der belegte Ist-Prozess rechtfertigt eine konkrete Lösung | 🔴 |
| 2 | Eine Persona braucht Alter, Namen und Hobbys | Relevant sind nur Merkmale, die eine nachvollziehbare UI-Entscheidung beeinflussen (Ziel, Zeitdruck, Umgebung, Endgerät, Einschränkungen) | 🟡 |
| 3 | Wer den Happy Path kennt, kennt den ganzen User Flow | Er zeigt nur den Fall, in dem alles glattgeht; zum ganzen Flow gehören auch Fehler, Abbruch und Korrektur | 🔴 |
| 4 | Drei-Schichten-Architektur, Client-Server und MVC meinen dasselbe | Sie beantworten unterschiedliche Fragen (fachliche Zuständigkeiten / Verteilung auf Systeme / Struktur innerhalb einer Anwendung) und sind keine Synonyme | 🔴 |
| 5 | Rollenbezogene Navigation ist bereits eine Sicherheitsgrenze | Sie ist eine Darstellungsentscheidung, im Browser manipulierbar – echte Autorisierung ist Backend-Aufgabe | 🔴 |
| 6 | Mehr ARIA bedeutet mehr Barrierefreiheit | Falsches ARIA verdeckt die eingebaute Rolle eines Elements oder meldet Zustände, die nicht stimmen; es ist ein Lückenfüller, kein Ersatz für das richtige HTML-Element | 🔴 |
| 7 | Positive `tabindex`-Werte reparieren die Fokusreihenfolge | Damit entsteht eine zweite Reihenfolge neben dem HTML, die kaum zu pflegen ist; richtig ist, das HTML selbst sinnvoll zu ordnen | 🟡 |
| 8 | Die Breite eines bekannten Geräts ist automatisch ein guter Breakpoint | Den Breakpoint bestimmt der Inhalt: Er gehört dorthin, wo das Layout tatsächlich bricht | 🟡 |
| 9 | CSS-`order` sorgt für die richtige Reihenfolge | `order` verändert nur die visuelle Anordnung, nicht DOM-/Lese-/Fokusreihenfolge | 🔴 |
| 10 | Ein grüner Accessibility-Scan beweist Barrierefreiheit | Automatisierte Werkzeuge sind ein Teilnachweis – Verständlichkeit und vollständige Tastaturbedienung müssen manuell geprüft werden | 🔴 |

---

## 7. Vertiefung und Ausblick (freiwillig – für den ersten Durchgang nicht erforderlich)

- **Nutzwerttabellen im Detail**: Wie Gewichtung und Bewertung von Gestaltungsvarianten nachvollziehbar dokumentiert werden, ohne eine objektive Wahrheit vorzutäuschen.
- **Weitere ARIA-Live-Region-Feinheiten**: Unterschiede zwischen `aria-live="polite"` und `aria-live="assertive"` über die Basisfälle `status`/`alert` hinaus.
- **CSS-Spezifitätsrechnung im Detail**: Wie sich die Spezifität von Selektorkombinationen exakt berechnen lässt.
- **Grid-Template-Areas**: Benannte Layoutbereiche als Alternative zu reinen Spalten-/Zeilendefinitionen.
- **Eye-Tracking-Methodik**: Wie Fixationen und Sakkaden ausgewertet werden und welche Grenzen die Methode hat.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was unterscheidet Problemraum und Lösungsraum? | Problemraum: heutiger Ablauf, Personen, Informationen, Schwierigkeiten; Lösungsraum: konkrete Oberflächen/Funktionen/Technologien |
| 2 | Was macht einen Medienbruch prüfungsrelevant? | Erst eine beobachtbare Folge (Doppelarbeit, Übertragungsfehler, Verzögerung), nicht der Wechsel allein |
| 3 | Was unterscheidet Muss/Soll/Kann? | Muss: Kernnutzen/zwingende Grenze verfehlt ohne Erfüllung; Soll: hoher Nutzen, verschiebbar; Kann: Zusatznutzen je nach Zeit/Risiko |
| 4 | Nenne mindestens fünf UI-Zustände, die früh im Prototyp entworfen werden. | Normal, Leer, Laden, Fehler, Erfolg (je nach Anwendung weitere wie deaktiviert, Berechtigung fehlt, offline) |
| 5 | Was unterscheidet Usability von User Experience? | Usability: Wirksamkeit/Effizienz/Zufriedenheit beim Zielerreichen; UX: umfasst zusätzlich Wahrnehmungen/Reaktionen vor, während und nach der Nutzung |
| 6 | Warum ist `<div role="button">` schlechter als `<button>`? | Fokus, Tastaturaktivierung und Zustand müssen manuell nachgebaut werden – `<button>` liefert das automatisch |
| 7 | Was ist der Unterschied zwischen `role="status"` und `role="alert"`? | `status` für unkritische Meldungen ohne Unterbrechung; `alert` hat dringliche, assertive Semantik und kann laufende Ausgaben unterbrechen – nur für wirklich dringliche Meldungen verwenden |
| 8 | Wann ist ein Breakpoint begründet? | Wenn das Layout an dieser Breite sichtbar Probleme macht, egal welches Gerät gerade so breit ist |
| 9 | Welchen WCAG-2.2-Prüfwert hat die Zielgröße (2.5.8)? | 24×24 CSS-Pixel als Minimum; kleiner ist nur mit einer der festgelegten Ausnahmen erlaubt, zum Beispiel genug Abstand zu Nachbarzielen oder Links im Fließtext |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Stakeholder** | Nutzt, beauftragt, betreibt, prüft oder ist betroffen – weiter als "Nutzer" |
| **Medienbruch** | Wechsel zwischen unverbundenen Medien, relevant erst durch beobachtbare Folge |
| **Akzeptanzkriterium** | Macht eine Anforderung eindeutig beobachtbar/prüfbar; häufig als Gegeben-Wenn-Dann formuliert |
| **Muss/Soll/Kann** | Priorisierung, nicht "wichtig/unwichtig" |
| **Drei-Schichten / Client-Server / MVC** | Fachliche Zuständigkeiten / Systemverteilung / App-interne Struktur – keine Synonyme |
| **Wireframe vs. Mockup vs. Prototyp** | Grobe Struktur / visuell ausgearbeitet, statisch / prüfbare Simulation |
| **Die 7 Interaktionsprinzipien (ISO 9241-110)** | Aufgabenangemessenheit, Selbstbeschreibungsfähigkeit, Erwartungskonformität, Erlernbarkeit, Steuerbarkeit, Robustheit, Benutzerbindung |
| **UI-Zustände** | Mindestens Normal, Leer, Laden, Fehler, Erfolg – je nach Anwendung mehr |
| **Semantisches HTML** | Element nach fachlicher Aufgabe wählen, nicht nach Aussehen |
| **ARIA-Grundregel** | Natives HTML nutzen, wenn es existiert – ARIA nur für echte Lücken |
| **Name, Rolle, Wert/Zustand** | Prüfperspektive für zugängliche Elemente |
| **Design-Token** | Benannter Gestaltungswert mit Zweckbezug im Namen |
| **Reflow (1.4.10)** | Bei 320px Breite kein Inhalts-/Funktionsverlust, kein 2D-Scrollen – außer bei Inhalten, die zwingend 2D-Layout erfordern |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Anforderung prüfbar formulieren | "Formulieren Sie eine prüfbare Anforderung für X" | Konkretes Gegeben-Wenn-Dann-Kriterium, keine vagen Adjektive |
| Architekturbegriffe abgrenzen | "Erläutern Sie den Unterschied zwischen X und Y" | Jeweils die beantwortete Frage benennen, nicht nur ein Beispiel |
| ARIA/HTML-Entscheidung bewerten | "Bewerten Sie diesen `<div>`-Ansatz" | Konkrete fehlende Eigenschaften (Fokus, Tastatur, Zustand) benennen, natives Element vorschlagen |
| Breakpoint begründen | "Warum liegt der Breakpoint bei X?" | Konkretes Inhalts-/Bedienproblem nennen, nicht Gerätename |
| WCAG-Kriterium anwenden | "Erfüllt dieses Layout Kriterium X?" | Konkreten Prüfwert nennen und mit dem Fall abgleichen |

---

## 11. Merksätze für das Fachgespräch

> Bevor du einen Bildschirm zeichnest, musst du wissen, wie heute wirklich gearbeitet wird und für wen.

> Die Aufgabe der Nutzer:innen und die offene Frage bestimmen Aufbau, Detailtiefe und Testmethode, nicht das Tool, das du am liebsten nutzt.

> Zuerst passendes HTML in sinnvoller Reihenfolge, ARIA nur dort, wo HTML nicht reicht.

> Responsiv ist ein Layout erst, wenn Inhalt und Bedienung bei jeder Breite, jedem Zoom und jedem Gerät verständlich bleiben.

> Ausgeblendet ist nicht geschützt – Autorisierung ist immer Backend-Aufgabe.

---

```yaml
dokument: LF10a-Teil1-wiki-artikel
lernfeld: "LF10a Teil 1 (Module 10a.1-10a.4)"
titel: "Konzeption & Struktur"
typ: "Typ A – Kompakter Prüfungs-Wiki (FIAE-fokussiert)"
status: final
stand: 2026-09-14
quellen_intern:
  - "LF10a.1-4: Anforderungen/Zielgruppen, Informationsarchitektur/Prototyp, Semantisches HTML/Barrierefreiheit, Responsive Design/Designsystem"
  - "Bewusster Querverweis zu LF5.1 (allgemeine Anforderungsanalyse) statt Wiederholung"
  - "Ausgewählte WCAG-2.2-AA-Prüfwerte ursprünglich aus dem Rohmaterial übernommen, in Runde 2 web-verifiziert und präzisiert (2.4.11 ergänzt, Reflow-/Zielgröße-Ausnahmen geschärft, Titel als Auswahl statt vollständiger Referenz gekennzeichnet) - Tabelle dient als gemeinsame Pflegegrundlage für LF10a Teil 1 und Teil 3"
quellen_fachlich:
  - titel: "WCAG 2.2 (W3C), DIN EN ISO 9241-110:2020, WHATWG HTML Living Standard"
    herausgeber: "W3C, DIN/ISO, WHATWG"
    status: "Rohmaterial verlinkt Primärquellen (W3C WCAG 2.2, WHATWG HTML); Erfolgskriterien-Nummern (1.4.3/1.4.4/1.4.10/1.4.11/2.4.7/2.4.11/2.5.8/4.1.3) in Runde 2 gezielt gegen W3C-Understanding-Dokumente web-verifiziert (nicht nur plausibilisiert), 2.4.11 als neues Kriterium bestätigt, 2.4.7-Einstufung als AA (nicht A) bestätigt"
  - titel: "Architekturmuster (Drei-Schichten/Client-Server/MVC), UX-Testverfahren, Designsystem-Grundlagen"
    herausgeber: "Rohmaterial + etabliertes Software-/UX-Engineering-Standardwissen"
    status: "stabile Konzepte, keine Web-Verifikation nötig"
review_historie:
  - runde: 1
    datum: 2026-09-14
    ergebnis: "Erstdraft erstellt aus dem recherchierten Material. Als ein zusammenhängender Artikel (Teil 1 von 3) gemäß mit Auftraggeber abgestimmter Dreiteilung verfasst. FIAE-fokussiert, mit explizitem Hinweis auf die Aufbaustufe (Trennung FIAE/FISI). WCAG-2.2-Tabelle unverändert aus Rohmaterial übernommen, da bereits korrekt und vom Auftraggeber als artikelübergreifende Referenz gekennzeichnet. Bewusster Querverweis zu LF5.1 statt Wiederholung allgemeiner Anforderungsanalyse."
  - runde: 2
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (2 Reviews, eigenständig web-verifiziert): WCAG-2.2-Tabelle fehlte das neue AA-Kriterium 2.4.11 'Focus Not Obscured' - ergänzt; Behauptung einer Review, 2.4.7 sei nur Level A statt AA, wurde gegengeprüft und als falsch verworfen (2.4.7 ist tatsächlich AA), nicht übernommen. Tabellentitel als 'Ausgewählte WCAG-2.2-AA-Prüfwerte' präzisiert (keine vollständige Kriterienliste), Reflow- und Zielgröße-Ausnahmen fachlich schärfer gefasst. Weitere Korrekturen: POUR-Prinzipien und Konformitätsstufen A/AA/AAA explizit benannt; role='alert' technisch präziser (assertive Semantik statt absolute 'erzeugt Unterbrechungen'); Usability-Test-Definition auf Entwurf/Prototyp/Produkt erweitert (nicht nur 'tatsächliche Nutzung'); Given-When-Then als häufige Form statt einzige Definition gekennzeichnet; IHK-Kernfrage 2 in zwei Fragen aufgeteilt; heuristische Evaluation als Fachbegriff ergänzt; UI-Arten-Tabelle auf FIAE-relevante Formen fokussiert (OUI/BCI in Randnotiz); UI-Zustände als Mindestmenge statt abschließende Liste gekennzeichnet; funktionale/nichtfunktionale Anforderungen allgemeiner gefasst; em/rem-Unterschied ergänzt; px-Beschreibung entschärft; Medienbruch-Definition und Relevanzbedingung begrifflich getrennt; MVC-zu-Drei-Schichten-Verhältnis ergänzt; Prüfungsrelevanz-Kopf präzisiert. Eine Review behauptete umfangreiche '[...]'-Platzhalter und abgeschnittene Textfragmente in mehreren Kapiteln - beim gezielten Abgleich (grep) nicht bestätigt, Abschnittsnummerierung 3.1-3.4 vollständig und lückenlos."
  - runde: 3
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (1 Review, web-verifiziert): Prüfungsbereich-Bezeichnung im Kopf war erfunden ('Konzeption und Umsetzung von Softwareprodukten' existiert nicht offiziell) - korrigiert zu 'Planen eines Softwareproduktes' (echter FIAE-AP2-Bereich, 90 Min., 10%), mit konkretem Bezug zu §13 Abs.1 Nr.2-4 FIAusbV (Programmspezifikationen, Bedienoberflächen, Qualitätskontrolle). YAML aktualisiert: 2.4.11 in Kriterienliste ergänzt, 'unverändert übernommen' korrigiert, Prüfquelle als 'gezielt web-verifiziert' statt 'eigenes Wissen' präzisiert. Akzeptanzkriterium-Beispiel logisch nachgebessert (ein Kriterium prüfte die 'höchstens fünf'-Anforderung nicht, jetzt zwei getrennte Kriterien). Persona-Grundlage ergänzt (Beleg vs. Proto-Persona, analog zur 1.1-Klassifikation). Kleinere Konsistenzkorrekturen: Cheatsheet-Akzeptanzkriterium und Reflow-Eintrag an präzisierte Haupttext-Formulierungen angeglichen, Selbsttest-Zielgröße-Antwort aktualisiert, doppeltes 'allein' behoben, 'selbst erzeugter Inhalt' zu normativem 'vom Autor erstellter Inhalt' präzisiert. Zum dritten Mal behauptete eine Review umfangreiche Platzhalter/abgeschnittene Fragmente - beim gezielten Abgleich erneut nicht bestätigt."
  - runde: 4
    datum: 2026-09-14
    ergebnis: "Eigene Abschlussprüfung: Usability-Test-Definition in Abschnitt 2.5 trug noch die alte, engere Formulierung ('Entwurf getestet'), während der Wichtig-Block direkt darunter bereits die erweiterte Fassung (Entwurf/Prototyp/Produkt) hatte - genau die Spannung, die eine Review in Runde 3 explizit anmerkte. Nachgezogen. Selbsttest 4 (UI-Zustände) und 7 (role=alert) trugen ebenfalls noch alte, in Runde 2/3 bereits präzisierte Formulierungen - angeglichen. Keine weiteren Fachfehler gefunden."
  - runde: 5
    datum: 2026-09-14
    ergebnis: "Nachträgliche Ergänzung auf Wunsch des Auftraggebers (Konsistenz-Nacharbeit, analog zu LF10a Teil 3): IHK-Relevanz-Markierungen (🔴/🟡/🟢) tatsächlich in den Fließtext eingebaut - alle Begriffstabellen (Belegt/Annahme/Offene-Frage, Muss/Soll/Kann, UI-Arten, Architekturmuster, Sketch/Wireframe/Mockup/Prototyp, 7 Interaktionsprinzipien, UX-Testverfahren, Einheiten, Layoutmodelle, Prüfungsfallen) sowie alle Wichtig-für-die-Prüfung-/Typische-Prüfungsfalle-Blöcke markiert. Von 2 auf 58 tatsächliche Markierungen. WCAG-Tabelle bewusst ohne Relevanz-Spalte belassen (Konsistenz mit Teil 3, das dieselbe Tabelle übernimmt). Keine inhaltlichen Änderungen, rein ergänzende Markierung."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-14) – Freigabe durch Autor:in bestätigt. Runde 5: nachträgliche Markierungs-Ergänzung, Inhalt unverändert final."
```