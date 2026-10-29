

## 🗺️ Vom ERM zum relationalen Datenbankschema – Die Bauanleitung für deine Tabellen

### Worum geht’s eigentlich?

Ein ERM (oder Chen-Diagramm) ist der fachliche Bauplan. Eine **Datenbank** besteht jedoch aus Tabellen, Spalten, Primär- und Fremdschlüsseln – dem *relationalen Schema*. Dieses Schema ist die technische Zeichnung, aus der du sofort `CREATE TABLE`-Befehle ableiten kannst.

Die Überführung vom ERM ins relationale Schema folgt einer Handvoll klarer **Transformationsregeln**. Hast du die einmal verinnerlicht, kannst du jedes noch so verschachtelte Modell in eine saubere Tabellenstruktur übersetzen – und genau das erwartet die IHK von dir.

> 💡 **Agile Side-Info:** In der Praxis passiert dieser Schritt meist im selben Sprint wie die ERM-Modellierung. Das Team einigt sich am Whiteboard auf die Entitäten, und ein*e Entwickler*in leitet daraus direkt die Migrationen für die Datenbank ab.

---

### 🔧 Die Transformationsregeln – Dein Regelkatalog

| Regel | ERM-Konstrukt | Wird zu im relationalen Schema | Notizen |
|-------|---------------|--------------------------------|---------|
| 1 | **Entität** | **Tabelle** | Tabellenname = Entitätsname im Singular (z. B. `leser`, `medien`). Alle Attribute der Entität werden zu Spalten. |
| 2 | **Primärschlüssel (PK)** | **PRIMARY KEY**-Constraint auf der Schlüsselspalte | Meist eine künstliche ID (`leser_id SERIAL PRIMARY KEY`), manchmal ein natürlicher Schlüssel (`isbn CHAR(13)`). Niemals NULL! |
| 3 | **fakultatives Attribut** | Spalte mit `NULL` erlaubt | Im ERM als nicht unterstrichenes Attribut ohne fette Markierung erkennbar. |
| 4 | **1:1-Beziehung** | Fremdschlüssel in einer der beiden Tabellen | Faustregel: FK in die Tabelle legen, die *optional* an der Beziehung teilnimmt, oder in diejenige, die funktional abhängig ist. |
| 5 | **1:n-Beziehung** | Fremdschlüssel in der Tabelle auf der „n“-Seite | *Die mit Abstand häufigste und prüfungsrelevanteste Regel.* Merksatz: „Das Kind merkt sich, wer die Eltern sind.“ |
| 6 | **n:m-Beziehung** | **Neue Assoziationstabelle** mit kombiniertem PK aus beiden FKs | Zusätzliche Attribute der Beziehungsraute (z. B. Ausleihdatum) kommen in diese Tabelle. |
| 7 | **Rekursive Beziehung (1:n)** | Fremdschlüssel in derselben Tabelle, der auf den eigenen PK verweist | Klassiker: `vorgesetzter_id` in der `mitarbeiter`-Tabelle, die auf `mitarbeiter_id` zeigt. |
| 8 | **Schwache Entität** | Tabelle mit zusammengesetztem PK (Owners FK + Teilschlüssel) | Die starke Entität wird zum Besitzer, ihr PK wandert als FK in die schwache Tabelle und wird Teil von deren PK. |
| 9 | **Generalisierung (Ist-ein)** | Drei Varianten: 1 Tabelle mit Typ-Flag, oder je eine Tabelle für Ober-/Unterklasse, oder nur Untertabellen. | Für die IHK reicht meist der Hinweis, dass man eine `typ`-Spalte einführt und optionale Attribute NULLable macht. |

> 💡 **Agile Side-Info:** Im Team klärst du am besten laut: „Ein Kunde hat *n* Aufträge – also bekommt `auftrag` die Spalte `kunde_id`. Ein Auftrag enthält *viele* Artikel und ein Artikel steckt in *vielen* Aufträgen – dafür brauchen wir eine dritte Tabelle `auftrag_position`.“ So erzwingst du gemeinsames Verständnis.

---

### 🧩 Durchgespielt am Bibliotheksbeispiel

Gegeben ist das ERM aus dem vorigen Artikel:

```
+--------------+       leiht aus    +-----------+
|   Leser      +--------------------+ Medien    |
| (LeserNr)    |1                 n | (MedienID)|
| Name         |                    | Titel     |
| Adresse      |                    | Typ       |
+--------------+                    +-----------+
```

**Schritt-für-Schritt-Überführung:**

1. Zwei starke Entitäten? → Zwei Tabellen: `leser`, `medien`.  
2. Primärschlüssel? → `leser_id SERIAL PRIMARY KEY` und `medien_id SERIAL PRIMARY KEY`.  
   - Warum nicht `LeserNr` direkt? Weil ich mich von fachlichen Nummern aus dem Altbestand unabhängig mache – die `LeserNr` wäre ein `UNIQUE`-Attribut für die Fachlichkeit, der PK bleibt technisch stabil. (Beides ist in Prüfungen akzeptiert.)
3. Beziehung `leiht aus` ist **1:n** mit `Leser (1)` zu `Medien (n)`? Stopp – genau lesen: *„Ein Medium wird zu einem Zeitpunkt von einem Leser ausgeliehen.“* Also ist die Bedeutung tatsächlich `Leser 1 --- n Medien`. Somit:  
   - Regel 5: FK in die Tabelle auf der n-Seite, also in `medien`.  
   - Neue Spalte: `leser_id INT REFERENCES leser(leser_id)`.
4. Ausleihdatum? War Attribut der Raute → kommt ebenfalls in die `medien`-Tabelle: `ausleihdatum DATE`.  
   (Alternativ: historische Ausleihen erfordern später eine n:m-Tabelle, aber für das aktuelle Ausleihmodell reicht das.)

**Ergebnis als SQL-DDL (zur Visualisierung):**

```sql
CREATE TABLE leser (
    leser_id   SERIAL PRIMARY KEY,
    leser_nr   VARCHAR(20) UNIQUE NOT NULL,
    name       VARCHAR(100) NOT NULL,
    adresse    TEXT
);

CREATE TABLE medien (
    medien_id   SERIAL PRIMARY KEY,
    titel       VARCHAR(200) NOT NULL,
    typ         VARCHAR(50),
    leser_id    INT REFERENCES leser(leser_id),
    ausleihdatum DATE
);
```

Genau so würde es in einer Prüfungsaufgabe verlangt – oft mit dem Hinweis: „Kennzeichnen Sie Primär- und Fremdschlüssel.“

---

### 🏗️ Wenn es komplexer wird – n:m und Rekursion

**n:m-Auflösung**: Ein Medium hat *mehrere* Autoren, ein Autor schreibt *mehrere* Medien. Das ERM zeigt eine Raute `schreibt` zwischen `Autor` und `Medium` mit `n` und `m`.  
- Neue Tabelle: `autor_medium`  
- Spalten: `autor_id INT REFERENCES autor(autor_id)`, `medien_id INT REFERENCES medien(medien_id)`  
- Primärschlüssel der Tabelle: `(autor_id, medien_id)` als zusammengesetzter Schlüssel.  
- Zusätzliches Attribut der Raute, z. B. `honorar DECIMAL(8,2)`, kommt in diese Assoziationstabelle.

**Rekursive Beziehung**: Ein Mitarbeiter hat einen Vorgesetzten, der selbst Mitarbeiter ist (1:n-rekursiv).  
- Eine Tabelle: `mitarbeiter` mit `mitarbeiter_id PK`.  
- Zusätzliche Spalte: `vorgesetzter_id INT REFERENCES mitarbeiter(mitarbeiter_id)` – sie darf NULL sein (der Chef hat keinen Vorgesetzten).

Diese beiden Muster sind mit Abstand die prüfungsrelevantesten Erweiterungen nach der einfachen 1:n-Beziehung.

---

### 🧠 Das Warum – mit Analogien aus deinem alten Beruf

**Handwerk / Fertigung:**  
Du hast einen Fertigungsauftrag (1) und viele Arbeitsgänge (n). Der Arbeitsgang bekommt die Auftragsnummer als FK. So weißt du immer, zu welchem Auftrag eine Bohrung gehört. Ohne FK müsstest du jedes Mal den Kundennamen im Arbeitsgang wiederholen – Fehler vorprogrammiert.

**Kaufmännischer Bereich / Vertrieb:**  
Eine Rechnung (1) und Rechnungspositionen (n). Die Positionstabelle erhält die `rechnung_id` als FK. Die n:m-Regel greift bei „Artikel (n) – Lieferschein (m)“: Du baust eine Positions- oder Zuordnungstabelle, die als Brücke dient und auch Mengen und Preise trägt. Das ist das Herzstück jedes Warenwirtschaftssystems.

**Gastronomie / Küche:**  
Gericht (1) und Zutaten (n) sind eine n:m-Beziehung, aufgelöst über die Tabelle `zutat_gericht` mit Angabe der Gramm-Menge. Genau so bist du in der Lage, Allergenlisten automatisch zu generieren und die Lagerbestände nachzukalkulieren.

**Das bringt's technisch:**  
- Du hast eine **normalisierte** Datenstruktur, die Anomalien beim Einfügen, Ändern und Löschen verhindert.  
- Abfragen werden logisch und performant, weil du über Schlüssel joinsen kannst.  
- Neue Anforderungen (z. B. „Wir brauchen jetzt auch noch das Rückgabedatum“) landen in genau der richtigen Tabelle, ohne das ganze System umzubauen.

---

### 🚀 Im Stil des agilen Arbeitens

- **Nicht alle Regeln auf einmal lernen:** Beherrsche zuerst 1:n und n:m. 90% der Praxis und 100% der Basis-Prüfungsaufgaben lassen sich damit lösen. Rekursion und Generalisierung kommen mit der Erfahrung.
- **Schlüssel ableiten als Teamritual:** Sobald der Product Owner eine neue User Story einbringt („Wir müssen Lieferanten zu Artikeln verknüpfen können“), fragt das Team: „Kann ein Artikel mehrere Lieferanten haben? Kann ein Lieferant viele Artikel liefern?“ Aus der Antwort folgt sofort, ob ein FK reicht oder eine Assoziationstabelle her muss.
- **Refactoring des Schemas:** Genau wie Code gehört auch ein Datenmodell gepflegt. Wenn aus einer 1:n-Beziehung später eine n:m-Beziehung wird (z. B. ein Kunde darf plötzlich mehrere Adressen haben), wird der FK aufgelöst und eine neue Tabelle eingeführt. Das ist kein Fehler, sondern Evolution.

🎯 **Side-Info:** Moderne ORM-Frameworks (z. B. Entity Framework, Hibernate) generieren das relationale Schema aus Klassenmodellen. Dahinter stecken exakt diese Transformationsregeln. Wer sie verstanden hat, kann die automatisch erzeugten Tabellen prüfen und eingreifen, wenn es nötig ist.

---

### 👣 Dein nächster Schritt

1. Nimm das Bibliotheks-ERM von oben und baue es manuell nach: Zeichne die Tabellen zeilenweise auf Papier. Schreibe Spaltennamen, unterstreiche den PK und markiere den FK.
2. Erweitere um eine n:m-Beziehung: Führe eine Entität `Autor` ein, verknüpfe sie mit `Medien` und leite die Assoziationstabelle ab. Notiere dir die DDL.
3. Such dir eine alte IHK-Prüfungsaufgabe (z. B. aus dem Bereich „Projektmanagement und Datenmodell“) – die stellen fast immer ein ERM und fragen: „Überführen Sie das Modell in ein relationales Schema.“ Löse sie und vergleiche mit der Musterlösung.
4. Tausche dein Ergebnis mit einem Lernpartner: Erklärt euch gegenseitig, warum der FK auf der n-Seite steht und wie der zusammengesetzte Schlüssel gebildet wird. So wird das Regelwissen zu echtem Verständnis.

---

**Zusammengefasst:** Die Überführung vom ERM ins relationale Schema ist kein Hexenwerk, sondern eine präzise Ableitung nach wenigen Regeln. Aus Rechtecken werden Tabellen, aus Rauten Fremdschlüssel oder Brückentabellen. Diese Regeln zu beherrschen bedeutet, den Schritt von der Fachlichkeit zur Technik sauber zu gehen – und genau das bewertet die IHK.