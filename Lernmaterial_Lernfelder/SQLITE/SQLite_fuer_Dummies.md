

**SQLite für Dummies – in 10 Schritten vom Nullpunkt zur eigenen Datenbank**  

(für Umschüler in Anwendungsentwicklung und Netzwerkadministration – kein Geschwafel, nur das was zählt)

---

### Schritt 1 – Was ist SQLite? (Die Analogie: Dein Notizbuch)

SQLite ist die einfachste Datenbank der Welt – eine einzige Datei, kein Server, keine Installation. Stell dir ein **Ringbuch-Notizbuch** vor, in dem du Tabellen zeichnest. Die Datei `meine_firma.db` ist dieses Notizbuch. Du kannst darin blättern, suchen, ergänzen, ändern oder löschen – alles mit Befehlen in einem Textfenster.

- Du brauchst keinen Aktenschrank (= Server), den jemand aufbauen muss.
- Kopierst du die `.db`-Datei, hast du ein vollständiges Backup. Löschst du sie, ist die Datenbank weg.
- SQLite ist ideal für Lernprojekte, Adminskripte und Programme, die eine lokale Datenablage brauchen.

---

### Schritt 2 – Erster Start und die Shell (Analogie: Terminplaner mit Spezialtasten)

Öffne dein Notizbuch mit dem Kommandozeilen-Tool `sqlite3`. Es ist unter Linux/macOS meist vorhanden; unter Windows kannst du es als einzelne `.exe` herunterladen.

**Im Terminal:**

```bash
sqlite3 meine_firma.db
```

- Existiert die Datei noch nicht, wird sie **automatisch neu angelegt**.
- Existiert sie bereits, wird sie einfach geöffnet – alle deine Tabellen sind sofort da.

Du siehst den Prompt `sqlite>`. Befehle, die mit einem Punkt beginnen, sind Steuerbefehle der Shell (kein SQL):

- `.help` – zeigt alle verfügbaren Shell-Kommandos an.
- `.quit` oder `.exit` – beendet die Shell und speichert die Datenbank.
- `.tables` – listet alle vorhandenen Tabellen auf.

**Merke:** Arbeiten ohne Server bedeutet: Deine Änderungen landen erst nach einem `COMMIT` oder beim regulären Beenden fest in der Datei.

---

### Schritt 3 – Tabellen anlegen (Analogie: Überschriften auf ein leeres Blatt)

Du nimmst ein leeres Blatt und schreibst die Spaltenköpfe. Genau das macht `CREATE TABLE`.

```sql
CREATE TABLE personen (
    id INTEGER PRIMARY KEY,   -- automatisch hochzählende ID
    name TEXT NOT NULL,        -- Text, darf nicht leer sein
    alter INTEGER,
    stadt TEXT
);
```

- **Datentypen** auf die Schnelle: `INTEGER` (Ganzzahl), `TEXT`, `REAL` (Kommazahl), `BLOB` (Binärdaten). Alles andere merkt man sich später.  
- `PRIMARY KEY` sorgt für die automatische Zeilennummer – bei `INTEGER PRIMARY KEY` wird automatisch der nächste freie Wert genommen (wie `AUTOINCREMENT`, nur effizienter). Willst du alte Lücken *nie* wiederverwenden, kannst du `INTEGER PRIMARY KEY AUTOINCREMENT` schreiben – für 99 % der Fälle reicht aber die Kurzform.  
- **Wichtig:** SQLite ist extrem flexibel mit Datentypen (»Type Affinity«). Du könntest in eine `INTEGER`-Spalte auch Text schreiben – das ist erlaubt, aber keine gute Idee. Halt dich an die gewählten Typen, dann bleiben deine Daten sauber.

Nützlicher Shellbefehl: `.schema personen` zeigt dir jederzeit die exakte Definition der Tabelle an – perfekt, wenn du später nachschauen willst, wie du sie gebaut hast.

---

### Schritt 4 – Daten einfügen (Analogie: Neue Zeile ins Notizbuch schreiben)

Jetzt trägst du eine Zeile unter die Überschriften ein.

```sql
INSERT INTO personen (name, alter, stadt) VALUES ('Anna', 28, 'Berlin');
INSERT INTO personen (name, alter, stadt) VALUES ('Bob', 35, 'Hamburg'),
                                                  ('Clara', 22, 'Berlin');
```
Die `id` musst du nicht angeben – sie wird von selbst vergeben. Du füllst einfach die Kästchen aus.

---

### Schritt 5 – Daten lesen (Analogie: Durch das Notizbuch blättern)

Mit `SELECT` liest du aus der Tabelle. Der Stern `*` steht für »alle Spalten«.

```sql
SELECT * FROM personen;            -- alles anzeigen
SELECT name, stadt FROM personen;  -- nur bestimmte Spalten
```

Die Ausgabe erscheint als einfache Tabelle im Terminal – ideal für schnelle Kontrollen.

---

### Schritt 6 – Filtern und Sortieren (Analogie: Mit dem Lesezeichen zu einer Seite springen)

Du willst nicht das ganze Blatt durchgehen, sondern gezielt bestimmte Zeilen sehen.

- **Filter (`WHERE`):**  

  ```sql
  SELECT * FROM personen WHERE stadt = 'Berlin';
  SELECT name, alter FROM personen WHERE alter > 25;
  ```

- **Sortierung (`ORDER BY`):**  

  ```sql
  SELECT * FROM personen ORDER BY alter DESC;   -- älteste zuerst
  SELECT * FROM personen WHERE stadt = 'Berlin' ORDER BY name ASC;
  ```

Immer zuerst mit einem `SELECT` prüfen, welche Daten du erwischst, bevor du änderst oder löschst.

---

### Schritt 7 – Ändern und Löschen (Analogie: Radiergummi und Löschtaste)

- **Ändern = Radiergummi:** `UPDATE` überschreibt vorhandene Werte.

  ```sql
  UPDATE personen SET alter = 29 WHERE name = 'Anna';
  ```

- **Löschen = komplette Zeile entfernen:** `DELETE` löscht die ganze Zeile.

  ```sql
  DELETE FROM personen WHERE id = 3;
  ```

**Achtung:** Ohne `WHERE`-Bedingung wird **alles** geändert oder gelöscht. Teste deine Bedingung immer vorher mit `SELECT`.

---

### Schritt 8 – Zwei Tabellen verknüpfen (Analogie: Zwei Registerkarten im selben Ordner)

Dein Notizbuch hat mehrere Blätter: Personen und Bestellungen. Eine Person kann mehrere Bestellungen haben. Verbunden werden sie über die Personen-ID.

```sql
CREATE TABLE bestellungen (
    id INTEGER PRIMARY KEY,
    person_id INTEGER NOT NULL,
    produkt TEXT,
    preis REAL
);

INSERT INTO bestellungen (person_id, produkt, preis) VALUES (1, 'USB-Stick', 12.99);
INSERT INTO bestellungen (person_id, produkt, preis) VALUES (1, 'Maus', 24.50);
INSERT INTO bestellungen (person_id, produkt, preis) VALUES (2, 'Tastatur', 45.00);
```

Jetzt die Verknüpfung mit `JOIN`:

```sql
SELECT personen.name, bestellungen.produkt, bestellungen.preis
FROM personen
JOIN bestellungen ON personen.id = bestellungen.person_id;
```

Du siehst sofort, wer was bestellt hat – Daten aus zwei Tabellen kombiniert, ohne Doppelt-Schreiben.

**Für stabile Daten: Fremdschlüssel (FOREIGN KEY)**  
Du kannst die Beziehung auch in der Tabellendefinition festhalten, um fehlerhafte Einträge (z. B. Bestellung für nicht existierende Person) automatisch zu verhindern:

```sql
CREATE TABLE bestellungen (
    id INTEGER PRIMARY KEY,
    person_id INTEGER NOT NULL REFERENCES personen(id),
    produkt TEXT,
    preis REAL
);
```

Damit SQLite diese Regel auch wirklich erzwingt, musst du einmalig im Terminal (oder in deinem Code) einschalten:

```sql
PRAGMA foreign_keys = ON;
```

Dann lehnt SQLite z. B. eine Bestellung mit `person_id = 99` ab, wenn es die Person nicht gibt.

---

### Schritt 9 – Transaktionen (Analogie: Banküberweisung, die erst nach Bestätigung zählt)

Eine Überweisung: Geld von Konto A weg und auf Konto B – beides muss zusammen klappen oder gar nicht. Genau das macht eine **Transaktion** mit `BEGIN`, `COMMIT` und `ROLLBACK`.

```sql
-- Kontostände: Anna (id=1) 500 €, Bob (id=2) 200 €
CREATE TABLE konten (id INTEGER PRIMARY KEY, name TEXT, saldo REAL);
INSERT INTO konten (name, saldo) VALUES ('Anna', 500), ('Bob', 200);

BEGIN;                              -- Transaktion starten
UPDATE konten SET saldo = saldo - 50 WHERE id = 1;
UPDATE konten SET saldo = saldo + 50 WHERE id = 2;
COMMIT;                             -- Alles gut → festschreiben
```

Geht während der Transaktion etwas schief (Fehler, Stromausfall), ersetzt du `COMMIT` durch `ROLLBACK;` – beide Änderungen werden rückgängig gemacht. SQLite führt jede einzelne Anweisung standardmäßig als eigene Transaktion aus; mit `BEGIN` fasst du mehrere zu einer logischen Einheit zusammen. Für Admins Gold wert: keine halbfertigen Zustände!

---

### Schritt 10 – Praxisrezepte für Entwickler und Admins

SQLite ist dein Schweizer Taschenmesser. Hier die wichtigsten Einsatzszenarien – jetzt mit Erklärungen, die vorher zu kurz kamen.

**Für Anwendungsentwickler:**

- Lokale Speicherung in Python (Android/iOS/Desktop funktioniert analog):

  ```python
  import sqlite3
  conn = sqlite3.connect('meine_firma.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM personen WHERE stadt='Berlin'")
  for row in cursor.fetchall():
      print(row)
  conn.close()

  ```

- Konfigurationen ablegen: eine Tabelle mit Schlüssel-Wert-Paaren statt einer INI-Datei, durchsuchbar mit SQL.

**Für Netzwerkadministratoren:**

- **CSV-Logs importieren und durchsuchen** – vorher das richtige Format einstellen:

  ```sql
  .mode csv               -- die Shell erwartet jetzt Komma-getrennte Zeilen
  .import server.log logs -- die Tabelle 'logs' wird automatisch angelegt
  SELECT * FROM logs WHERE status >= 400;

  ```

  Das ist extrem schnell, weil du keine externen Tools brauchst. `.mode` und `.import` sind reine Shell-Befehle, kein SQL.

- **Sichere Backups:**  
  - **Schnelle Kopie mit `.backup`:**  

    ```sql
    .backup sicherung.db
    ```

    Das erzeugt eine konsistente Kopie, auch wenn gerade Änderungen anstehen.  
  - **Während die Datenbank offen ist, solltest du die Datei nicht einfach mit Dateimitteln kopieren** – das kann eine inkonsistente Version hinterlassen. Entweder `.backup` nutzen oder die Shell vor dem Kopieren schließen.  
  - Für Skripte im echten Leben: `sqlite3 prod.db ".backup prod_backup.db"` direkt aus der Kommandozeile aufrufbar.

- **Performance-Tipp (bei Bedarf):** Wenn du große Tabellen oft nach einer bestimmten Spalte durchsuchst (`WHERE stadt = 'Berlin'`), kannst du mit einem **Index** die Suche beschleunigen:

  ```sql
  CREATE INDEX idx_personen_stadt ON personen(stadt);
  ```

  Für die meisten Admin-Tools nicht nötig, aber gut zu wissen, falls deine Log-Tabelle mehrere 100.000 Zeilen hat.

---

### Fazit: Keep it simple (DRY)

SQLite lebt das DRY-Prinzip (Don’t Repeat Yourself) wie kaum eine andere Datenbank: kein Server, null Konfiguration, eine einzige Datei. Die Notizbuch-Analogie begleitet dich durch alle Konzepte – vom Anlegen der ersten Tabelle bis zu Transaktionen und Fremdschlüsseln. Mit den jetzt ergänzten Praxistipps zu `.schema`, Datentyp-Flexibilität, Fremdschlüsseln und konsistenten Backups bist du nicht nur für erste Gehversuche gewappnet, sondern auch für den produktiven Einsatz als Admin oder Entwickler.

Hast du die 10 Schritte einmal verinnerlicht, fühlen sich auch große Datenbanksysteme wie PostgreSQL oder MySQL sofort vertraut an – nur dass du dort zusätzlich noch den Motor (Server) starten musst.