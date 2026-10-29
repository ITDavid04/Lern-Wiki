
## 🛠️ SQL Grundlagen: Datenbanken und Tabellen anlegen (DDL)

### Worum geht’s eigentlich?

Du hast ein ERM gezeichnet und in ein relationales Schema überführt. Jetzt wird’s ernst: Du erstellst die Datenbank und ihre Tabellen mit **SQL – Structured Query Language**.  

Der Teil von SQL, der die Struktur baut, heißt **DDL (Data Definition Language)**. Mit ihr sagst du:  
„Hier ist eine Tabelle, so heißen die Spalten, dieser Typ von Daten kommt rein, diese Spalte darf niemals leer sein, und diese verweist auf eine andere Tabelle.“  

Ohne DDL bleibt dein ERM ein hübsches Bild. Mit DDL wird daraus eine lebendige Datenbank, die Abfragen, Auswertungen und Anwendungen ermöglicht.

> 💡 **Agile Side-Info:** In agilen Projekten entstehen DDL-Befehle häufig als *Migrationsdateien* – das Team schreibt sie im selben Sprint, in dem das ERM entsteht. Ändert sich die Anforderung, wird die Migration ergänzt oder eine neue erstellt. So bleibt die Datenbank immer synchron mit dem Code.

---

### 🔧 Die wichtigsten DDL-Befehle – Dein Werkzeugkasten

| Befehl                     | Bedeutung                                                                 | Analogie aus anderen Berufen                                           |
|----------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `CREATE DATABASE`          | Legt eine völlig neue Datenbank an.                                       | Ein neuer Aktenschrank mit eigener Bezeichnung.                         |
| `CREATE TABLE`             | Erzeugt eine Tabelle mit Spalten und Regeln (Constraints).                | Ein neuer Karteikasten in diesem Schrank, inkl. Vordruck der Karten.   |
| `ALTER TABLE`              | Ändert eine bestehende Tabelle (fügt Spalten hinzu, ändert Typen, …).     | Ein weiteres Feld auf alle vorhandenen Karteikarten nachträglich stempeln. |
| `DROP TABLE`               | Löscht eine Tabelle komplett (Daten UND Struktur weg!).                   | Den gesamten Karteikasten in den Schredder geben.                      |
| `TRUNCATE TABLE`           | Leert eine Tabelle (Daten weg, Struktur bleibt).                          | Alle Karten herausnehmen, aber den leeren Kasten behalten.             |
| `CREATE INDEX`             | Erzeugt einen Suchindex auf einer oder mehreren Spalten zur Performance-Steigerung. | Ein Registerblatt vorne im Karteikasten, das den Zugriff beschleunigt. |
| `DROP INDEX`               | Löscht einen Index wieder.                                                | Das Registerblatt entfernen.                                            |

Für die Prüfung und den Alltag reichen dir zu Beginn **CREATE TABLE** und **ALTER TABLE**. Die anderen Befehle lernst du durch Einsatz am lebenden Objekt.

> 💡 **Agile Side-Info:** In der Praxis fasst ihr alle DDL-Änderungen in nummerierten Skripten zusammen (z. B. `V01__init.sql`, `V02__add_spalte.sql`), damit das gesamte Team die Datenbank jederzeit auf den gleichen Stand bringen kann.

---

### 🧱 Datentypen – die Bausteine der Spalten

Jede Spalte bekommt einen Datentyp, der festlegt, was gespeichert werden darf. Die häufigsten Typen findest du hier:

| Typ               | Beschreibung                                 | Beispiel / Hinweis                                                   |
|-------------------|----------------------------------------------|----------------------------------------------------------------------|
| `INT / INTEGER`   | Ganze Zahlen.                                | `INTEGER PRIMARY KEY` ist der Klassiker für IDs.                     |
| `DECIMAL(p, s)`   | Festkommazahlen (p = Stellen gesamt, s = Nachkommastellen). | `DECIMAL(8,2)` für Geldbeträge wie 12345.67.                       |
| `VARCHAR(n)`      | Variable Zeichenkette bis n Zeichen.        | Für Namen, Straßen, Produktbezeichnungen. Max. Länge immer bedenken!|
| `TEXT`            | Beliebig langer Text (nicht standardisiert, aber überall verfügbar). | Für Bemerkungen, Beschreibungen. Bei großen Inhalten bedacht einsetzen. |
| `DATE`            | Datum (ohne Uhrzeit).                        | `'2026-05-04'`                                                       |
| `TIMESTAMP`       | Datum mit Uhrzeit.                           | `'2026-05-04 14:30:00'`                                              |
| `BOOLEAN`         | Wahrheitswert (`TRUE`/`FALSE`).              | PostgreSQL hat echte BOOLEAN, MySQL verwendet TINYINT(1).            |

**Prüfungstipp:** In IHK-Aufgaben werden Datentypen meist vorgegeben oder du musst sie sinnvoll wählen. Fragt die Aufgabe z. B. nach einem Geldbetrag, ist `DECIMAL(10,2)` die sicherste Wahl.

---

### 🔒 Constraints – Datenqualität eingebaut

Constraints sind Regeln, die die Datenbank erzwingt. Sie sind deine erste Verteidigungslinie gegen Müll in den Tabellen.

| Constraint              | Syntax im `CREATE TABLE`           | Bedeutung                                                                 |
|-------------------------|------------------------------------|---------------------------------------------------------------------------|
| **PRIMARY KEY**         | `spalte SERIAL PRIMARY KEY`        | Eindeutige Identifikation jeder Zeile, niemals NULL.                      |
| **FOREIGN KEY**         | `spalte INT REFERENCES andere_tabelle(pk)` | Verknüpft eine Zeile mit einer anderen Tabelle (referenzielle Integrität). |
| **NOT NULL**            | `spalte VARCHAR(50) NOT NULL`      | Die Spalte muss immer einen Wert haben.                                   |
| **UNIQUE**              | `spalte VARCHAR(50) UNIQUE`        | Jeder Wert darf nur einmal vorkommen (z. B. E-Mail).                      |
| **CHECK**               | `preis DECIMAL(8,2) CHECK (preis > 0)` | Bedingung muss erfüllt sein.                                           |
| **DEFAULT**             | `erstellt_am DATE DEFAULT CURRENT_DATE` | Wird automatisch gesetzt, falls kein Wert angegeben wird.            |

> 💡 **Agile Side-Info:** Ein gut gesetzter Constraint ist wie eine automatische Qualitätskontrolle. Es verhindert, dass ein Entwickler oder eine spätere Anwendung versehentlich kaputte Daten einfügt. Nutzt sie mutig – die Datenbank wird es euch danken.

---

### 🧩 Am Bibliotheksbeispiel durchgespielt

Erinnere dich an die Transformationsregeln aus dem letzten Artikel. Aus der Entität „Leser“ wurde eine Tabelle `leser`, aus „Medien“ die Tabelle `medien` mit einem Fremdschlüssel zu `leser`. Jetzt gießen wir das in SQL DDL:

```sql
-- Tabelle Leser
CREATE TABLE leser (
    leser_id   SERIAL PRIMARY KEY,
    leser_nr   VARCHAR(20)  UNIQUE NOT NULL,
    name       VARCHAR(100) NOT NULL,
    adresse    TEXT
);

-- Tabelle Medien (inkl. 1:n-Beziehung zu Leser)
CREATE TABLE medien (
    medien_id    SERIAL PRIMARY KEY,
    titel        VARCHAR(200) NOT NULL,
    typ          VARCHAR(50),
    leser_id     INT REFERENCES leser(leser_id),   -- FK zur Leser-Tabelle
    ausleihdatum DATE
);
```

**Erläuterungen zum Code:**

- `SERIAL` ist ein PostgreSQL-Datentyp, der automatisch fortlaufende Zahlen erzeugt. In MySQL verwendest du `INT AUTO_INCREMENT`, in SQLite `INTEGER PRIMARY KEY AUTOINCREMENT`.  
- `REFERENCES leser(leser_id)` erzeugt den **FOREIGN KEY**. Das DBMS stellt nun sicher, dass du keine `leser_id` in `medien` einfügen kannst, die nicht in `leser` existiert.  
- `UNIQUE NOT NULL` bei `leser_nr` stellt sicher, dass es keine zwei Leser mit derselben Ausweisnummer gibt und jeder Leser eine Nummer hat.  
- `ausleihdatum` darf leer sein (NULL), das Medium ist dann nicht ausgeliehen.

---

### 🏗️ Komplexere Konstellationen: n:m und rekursiv umsetzen

**n:m-Beziehung auflösen:** Für „Autor (n) – schreibt – Medium (m)“ benötigst du eine Assoziationstabelle. Aus der Transformationsregel 6 wird:

```sql
CREATE TABLE autor (
    autor_id SERIAL PRIMARY KEY,
    name     VARCHAR(100) NOT NULL
);

CREATE TABLE autor_medium (
    autor_id  INT REFERENCES autor(autor_id),
    medien_id INT REFERENCES medien(medien_id),
    honorar   DECIMAL(8,2),
    PRIMARY KEY (autor_id, medien_id)   -- zusammengesetzter Primärschlüssel
);
```

**Rekursive Beziehung:** Ein Mitarbeiter hat einen Vorgesetzten, der selber Mitarbeiter ist:

```sql
CREATE TABLE mitarbeiter (
    mitarbeiter_id  SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    vorgesetzter_id INT REFERENCES mitarbeiter(mitarbeiter_id)  -- kann NULL sein
);
```

So wird aus abstrakten Regeln sofort lauffähiges SQL.

---

### 🧠 Das Warum – mit Analogien aus deinem alten Beruf

**Handwerk / Fertigung:**  
Stell dir vor, du willst eine Werkzeugdatenbank bauen. Jeder Werkzeugtyp (z. B. Hammer, Säge) bekommt eine Tabelle `werkzeuge` mit Name und Gewicht, und eine Tabelle `lagerorte` mit Regal und Fach. Über einen FK `lagerort_id` in `werkzeuge` weißt du immer, ob der Hammer im Regal A3 liegt. Ohne den FK könnte jemand „Regal Z99“ eintragen, was es gar nicht gibt – spätestens beim Suchen wird’s teuer.

**Kaufmännischer Bereich / Vertrieb:**  
Deine `rechnung`-Tabelle hat `kunde_id INT REFERENCES kunde(kunde_id) NOT NULL`. Das verhindert, dass Rechnungen ohne Kunden existieren – eine elementare Geschäftsregel, die das System automatisch prüft. Genau so vermeidest du die klassische „Rechnungsleiche“ ohne Rechnungsempfänger.

**Gastronomie / Küche:**  
Eine Allergen-Zuordnungstabelle mit `gericht_id` und `allergen_id` setzt du mit `PRIMARY KEY (gericht_id, allergen_id)` um. So kann ein Gericht nicht zweimal dasselbe Allergen bekommen, und ein Fremdschlüssel stellt sicher, dass nur definierte Allergene eingetragen werden. Das ist der digitale Schutz für Gäste mit Lebensmittelunverträglichkeiten.

**Das bringt’s technisch:**  
- Constraints sorgen dafür, dass deine Datenbank immer einen konsistenten Zustand behält – ohne dass die Anwendungslogik jeden Einzelfall absichern muss.  
- `PRIMARY KEY` und `FOREIGN KEY` sind die Voraussetzung, dass Abfragen über mehrere Tabellen (JOINs) funktionieren und performant sind.  
- Datentypen erzwingen die richtige Art von Werten; ein Preis bleibt numerisch und wird nicht plötzlich „bitte überweisen“ als Text.

---

### 🚀 Im Stil des agilen Arbeitens

- **DDL ist nicht in Stein gemeißelt.** Sobald eine User Story neue Felder benötigt, schreibst du ein `ALTER TABLE` -Skript, testest es lokal und spielst es auf die Entwicklungsdatenbank ein. Jeder im Team kann das gleiche Skript ausführen.  
- **Migration statt Excel.** Statt eine Tabelle manuell zu verändern („Stell doch bitte Spalte dazu“), existiert jede Änderung als nummerierte Migrationsdatei in der Versionsverwaltung. So kann der Zustand der Datenbank jederzeit nachvollzogen und reproduziert werden – ein zentraler DevOps-Gedanke.  
- **Beginne mit dem Minimum.** Für den ersten Sprint brauchst du vielleicht nur die `leser`-Tabelle und einen Login. Erst später kommen `medien` und Ausleihen dazu. Dein DDL wächst iterativ, genau wie dein ERM.

🎯 **Side-Info:** Moderne Datenbank-Frameworks wie Flyway oder Liquibase verwalten genau solche inkrementellen Änderungen. Das Grundprinzip ist aber immer dasselbe: Du schreibst SQL DDL in einer kontrollierten, wiederholbaren Art.

---

### 👣 Dein nächster Schritt

1. Installiere dir ein lokales Datenbankwerkzeug (z. B. DBeaver, pgAdmin oder SQLite Browser) und lege eine Übungsdatenbank an.  
2. Schreibe die obigen `CREATE TABLE`-Anweisungen ab und führe sie aus. Füge ein paar Testdaten ein (per GUI oder `INSERT`). Verletze bewusst einen FOREIGN KEY – was passiert?  
3. Nimm dein eigenes ERM aus der letzten Übung und übersetze es komplett in DDL. Achte auf Datentypen und Constraints.  
4. Tausche dich mit deinem Lernpartner aus: Lasst eure Skripte gegenseitig prüfen, ob alle Beziehungen und Regeln korrekt abgebildet sind.  
5. Schaut euch eine alte IHK-Prüfungsaufgabe an, in der ein ERM oder ein relationales Schema vorgegeben ist und DDL-Anweisungen verlangt werden. Schreibt die Lösung und vergleicht sie mit der Musterlösung.

---

**Zusammengefasst:** SQL DDL ist deine direkte Umsetzung des relationalen Schemas in eine echte Datenbank. Mit wenigen Befehlen erschaffst du Tabellen, definierst Schlüssel und baust Qualitätsregeln ein. Für die IHK-Prüfung musst du `CREATE TABLE` mit allen Constraints aus dem Effeff beherrschen – und das lernst du am besten durch Tippen und Testen.

💡 Ein kleiner Bonus-Tipp für deine Umschüler:

Am Ende vielleicht noch ein „Cheat Sheet“ für die Syntax-Reihenfolge bei CREATE TABLE, da viele Anfänger oft die Kommas vergessen oder die Reihenfolge von Datentyp und Constraint vertauschen:

    Syntax-Formel: Spaltenname + Datentyp + Constraints + , (außer bei der letzten Spalte!)