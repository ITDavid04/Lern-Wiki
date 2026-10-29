
## 📋 Entity-Relationship-Modell (ERM) – Der Bauplan für Daten

### Worum geht’s eigentlich?

Ein ERM ist ein **strukturelles Modell**, das zeigt, welche Informationen in einem System gespeichert werden und **wie diese Informationen logisch zusammenhängen**. Es ist die Blaupause für eine Datenbank, noch bevor du an Tabellen, SQL oder gar eine Programmiersprache denkst.

Vereinfacht gesagt: Du sammelst die Dinge, über die du Daten speichern willst (z. B. Kunden, Bestellungen oder Maschinen) und definierst, wie sie zueinander in Beziehung stehen. Das Ergebnis ist eine eindeutige, grafische Übersicht – vergleichbar mit einem **Organigramm der Datenwelt**.

> 💡 **Agile Side-Info:** Ein ERM muss zu Beginn nicht perfekt sein. Du skizzierst es im Team als „gerade gut genug“, um die aktuelle User Story zu verstehen, und verfeinerst es iterativ.

---

### 🔧 Die wichtigsten Bausteine

Das ERM hat nur eine Handvoll Symbole. Ich verwende hier die klassische **Chen-Notation**, weil sie für Quereinsteiger am bildlichsten ist und in vielen Lernmaterialien vorkommt.

| Symbol                    | Bedeutung                                                                                 | Analogie aus anderen Berufen                                         |
|---------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Rechteck (Entity)**     | Ein Objekt der realen Welt, über das du Daten speichern möchtest.                         | Ein Karteikasten mit der Aufschrift „Kunden“, „Maschinen“, „Rezepte“. |
| **Raute (Relationship)**  | Eine logische Verknüpfung zwischen zwei oder mehr Entitäten. Sie wird verbal beschrieben. | Die Tätigkeit, die zwei Karteikästen verbindet, z. B. „bestellt“, „wartet“, „gehört zu“. |
| **Ellipse (Attribut)**    | Eine einzelne Eigenschaft, die zu einer Entität oder Beziehung gehört.                    | Die einzelnen Felder auf einer Karteikarte: Name, Datum, Gewicht, Farbe. |
| **Primärschlüssel (unterstrichenes Attribut)** | Das eindeutige Identifikationsmerkmal einer Entität (z. B. Kundennummer).        | Die unverwechselbare Aktenzeichen-Nummer auf einem Vorgang.          |
| **Linie (Kante)**         | Verbindet Entitäten mit ihren Beziehungen und Attributen.                                 | Die Ablageordnung, nach der die Karteikästen miteinander in Verbindung stehen. |
| **Doppeltes Rechteck (schwache Entität)** | Eine Existenz, die nur von einer anderen Entität abhängig ist (z. B. ein Positionsposten einer Bestellung). | Der Laufzettel einer Akte – ohne die Akte ergibt er keinen Sinn. |

Eine **Kardinalität** (z. B. 1:1, 1:n, n:m) zeigt dir die Mengenverhältnisse an und wird an die Linie zwischen Entität und Raute geschrieben. Sie beantwortet die Frage: „Wie viele … können mit wie vielen … in Beziehung stehen?“

> 💡 **Agile Side-Info:** In der Praxis reichen dir zu Beginn Rechteck, Raute und 1:n/m:n-Notation. Details wie Attribute kommen später – das ist ganz im Sinne von „Working Software over Comprehensive Documentation“.

---

### 🧩 Einfaches Beispiel: Bibliotheksverwaltung

Stell dir vor, du sollst eine App für eine kleine Bibliothek bauen. Du skizzierst folgendes ERM:

```
+--------------+       leiht aus    +-----------+
|   Leser      +--------------------+ Medien    |
| (LeserNr)    |        1         n | (MedienID)|
| Name         |                    | Titel     |
| Adresse      |                    | Typ       |
+--------------+                    +-----------+
```

Gelesen wird das so:
- Ein **Leser** kann **n** Medien ausleihen.  
- Ein **Medium** wird zu einem Zeitpunkt von **einem** Leser ausgeliehen (1:n-Beziehung).
- Beide Entitäten haben einen Primärschlüssel (unterstrichen). Die Attribute (Name, Titel etc.) hängen als Ellipsen dran, die hier aus Platzgründen als Liste notiert sind.

Im „ausleihen“-Prozess versteckt sich auch das Ausleihdatum – das wäre ein Attribut der Raute.

**So liest du den Plan wie eine Baustellenzeichnung:** Die Entitäten sind die Gewerke, die Beziehungen sind die Schnittstellen, und die Attribute sind die benötigten Materialien jeder Station.

---

### 🏗️ Verschachtelung und Erweiterung – komplexe Datenstrukturen beherrschen

Im ERM gibt es keine „Verschachtelung“ im Sinne von Code-Blöcken. Stattdessen entsteht Komplexität durch:

- **n:m-Beziehungen**: Ein Medium kann mehrere Autoren haben, ein Autor schreibt mehrere Medien. Diese Beziehung wird später in einer eigenen Tabelle aufgelöst (dem „Assoziationstyp“). Analogie: Eine Stückliste, in der ein Teil in mehreren Produkten steckt und ein Produkt aus vielen Teilen besteht – du brauchst eine separate Liste, um die Zuordnungen zu verwalten.

- **Rekursive Beziehungen**: Eine Entität steht mit sich selbst in Beziehung. Beispiel: Ein Mitarbeiter hat einen Vorgesetzten, der selbst auch Mitarbeiter ist. Du zeichnest die Raute so, dass die Linie von der Entität ausgeht und zur selben Entität zurückführt. Analogie: Der Stammbaum an der Wand – jede Person trägt den Verweis auf die Eltern-Personen-Nummer.

- **Schwache Entitäten**: Eine Bestellposition existiert nur innerhalb einer Bestellung. Ihre Identität setzt sich aus dem Schlüssel der Bestellung und einer eigenen Teilnummer zusammen. Analogie: Die nummerierten Seiten in einem Vertrag – Seite 2 von Vertrag 42.

- **Ist-ein-Beziehung (Spezialisierung/Generalisierung)**: Eine Entität „Fahrzeug“ kann sich in „PKW“ und „LKW“ spezialisieren. Die unteren Entitäten erben alle Attribute der oberen und ergänzen eigene. Analogie: Ein Standardformular mit Zusatzblättern für bestimmte Fälle.

Diese Konzepte sind dein Werkzeugkasten, um auch scheinbar komplizierte Zusammenhänge sauber abzubilden.

---

### 🧠 Das Warum – mit Analogien aus deinem alten Beruf

**Handwerk / Fertigung:**  
Du hast einen Materiallagerort, der mit den Werkstücken über einen „gehört zu“-Zettel verbunden ist. Ein Werkstück kann an genau einem Lagerort liegen (1:n). Du verhinderst, dass ein Teil doppelt im System liegt oder ein Ort plötzlich mit drei nicht existenten Teilen verknüpft ist. Das ERM ist dein **normierter Lagerverwaltungsplan**.

**Kaufmännischer Bereich / Vertrieb:**  
Eine Rechnung hat einen Kunden, ein Kunde hat mehrere Rechnungen. Eine Rechnung kann viele Positionen enthalten, eine Position gehört zu genau einer Rechnung. Das ERM zwingt dich, diese Abhängigkeiten sauber zu definieren. Ohne ERM riskierst du eine Excel-Hölle, in der die Kundendresse in jeder Rechnungszeile neu geschrieben wird – und irgendwann abweicht. Das ERM ist deine **Stammdaten- und Bewegungsdaten-Ordnung**.

**Gastronomie / Küche:**  
Ein Gericht besteht aus vielen Zutaten, eine Zutat steckt in vielen Gerichten (n:m). Ohne ein ERM wüsstest du nicht, ob du die Allergene korrekt zuordnen kannst. Das ERM ist deine **Rezeptdatenbank**, die aus Einkaufsliste und Speisekarte eine logische Brücke baut.

**Das bringt's technisch:**  
- Du vermeidest Redundanzen und widersprüchliche Daten (Anomalien).  
- Die Datenbank wird so gebaut, dass sie später performant abfragbar ist.  
- Änderungen an den Anforderungen lassen sich leichter einarbeiten, wenn das Datenmodell tragfähig ist.

---

### 🚀 Im Stil des agilen Arbeitens

- **Nicht alles auf einmal modellieren:** Nimm dir nur den Teil des ERM vor, der für das aktuelle Sprint-Ziel relevant ist. Ein Minimal-ERM für den „Login“-User reicht völlig, bevor du an die Bestellhistorie denkst.
- **Mit allen Beteiligten am Whiteboard:** Product Owner, Tester und Entwickler können ein einfaches ERM sofort verstehen und diskutieren – es braucht keine SQL-Kenntnisse. Du fragst: „Kann ein Kunde mehrere Adressen haben?“, die Antwort fließt direkt als Kardinalität ein.
- **Iterativ härten:** Aus dem ERM wird im nächsten Schritt das relationale Datenbankschema abgeleitet. Kommt eine neue User Story, wird das ERM erweitert und das Team prüft gemeinsam, ob die bisherige Struktur der neuen Logik standhält (Refactoring am Modell).

🎯 **Side-Info:** In modernen Projekten wird oft direkt die UML (Klassendiagramm) verwendet, die konzeptionell auf dem ERM aufbaut, aber um Methoden und Vererbung erweitert ist. Das ERM ist dein Einstieg in diese Welt und bleibt für rein datenbanklastige Aufgaben das Mittel der Wahl.

---

### 👣 Dein nächster Schritt

1. Nimm eine einfache Alltagsdomäne, die du gut kennst (z. B. Kundenverwaltung vom Handwerksbetrieb: Kunde – Auftrag – Material). Identifiziere die Entitäten und ihre Beziehungen. Zeichne ein simples ERM mit Rechtecken und Rauten, noch ohne Attribute.
2. Notiere dir zu jeder Beziehung die Kardinalitätsfragen: „Ein Kunde hat wie viele Aufträge? Ein Auftrag enthält wie viele Materialpositionen? Ein Material kann in wie vielen Aufträgen vorkommen?“
3. Tausche dich mit einem Lernpartner aus: Erklärt euch gegenseitig, warum eine Beziehung 1:n oder n:m ist und welche Attribute ihr wo sehen wollt. So werden Denkfehler schnell sichtbar.
4. Später überträgst du das ERM in SQL-Tabellen – du wirst merken, dass jede Entität zur Tabelle und jede Raute zur Fremdschlüsselbeziehung wird.

---

**Zusammengefasst:** Das ERM ist deine Datenlandkarte, bevor du die erste Datenbank anlegst. Es übersetzt betriebliche Begriffe in logische Strukturen, die das gesamte Entwicklungsteam versteht. Aus jedem Beruf bringst du das Wissen um Stamm- und Bewegungsdaten mit – das ERM ordnet sie so, dass die Software später stabil darauf aufbauen kann.