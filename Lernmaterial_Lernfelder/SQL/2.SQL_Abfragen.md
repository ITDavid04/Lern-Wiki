

## 🔍 SQL Abfragen: Daten finden und auswerten (DML / DQL)

### Worum geht’s eigentlich?

Deine Datenbank steht, die Tabellen sind verknüpft und erste Daten sind eingepflegt. Jetzt kommt der Moment, für den wir den ganzen Aufwand betreiben: **Wir wollen Antworten!**

Wie viele Kunden haben diesen Monat bestellt? Welche Bücher sind überfällig? In SQL nutzt du dafür den `SELECT`-Befehl. Er ist das Schweizer Taschenmesser der IT. Du „manipulierst“ hier zwar nichts, aber du rufst Daten ab, um sie nutzbar zu machen.

> 📌 **Hinweis:** `SELECT` wird im SQL-Standard zur **DML (Data Manipulation Language)** gezählt, obwohl es nichts verändert. Du wirst daher auch oft den Begriff **DQL (Data Query Language)** hören – beides meint hier dasselbe: lesende Zugriffe.

> 💡 **Agile Side-Info:** In einem Sprint ist eine „User Story“ oft erst dann fertig, wenn die Daten nicht nur in der Datenbank liegen, sondern auch korrekt im Frontend (der App oder Webseite) angezeigt werden. Deine SQL-Abfrage ist das Bindeglied dazwischen.

---

### 🔧 Die „Heilige Dreifaltigkeit“ der Abfrage

Fast jede Abfrage besteht aus diesen drei Bausteinen. Merk dir die Reihenfolge gut – SQL ist hier sehr eigen!

| Baustein | Bedeutung                                | Analogie aus anderen Berufen                         |
|----------|-------------------------------------------|-------------------------------------------------------|
| `SELECT` | **WAS** will ich sehen? (Spaltenauswahl)  | Welche Felder auf dem Formular interessieren mich?    |
| `FROM`   | **WOHER** kommen die Daten? (Tabellenname) | In welchen Ordner im Schrank muss ich greifen?        |
| `WHERE`  | **WELCHE** Bedingungen gelten? (Filter)   | Nur die gelben Akten! Nur Rechnungen über 500 €!      |

---

### 🧱 Filter und Operatoren – Die Logik-Prüfung

Im `WHERE`-Teil entscheidest du, was wichtig ist. Hier nutzt du mathematische und logische Operatoren:

- **Vergleiche:** `=`, `<>`, `<`, `>`, `<=`, `>=` (Hinweis: `<>` bedeutet „ungleich“).
- **Bereiche:** `BETWEEN 10 AND 50` (Ideal für Preise oder Daten).
- **Listen:** `IN ('Berlin', 'Hamburg', 'München')` (Sucht nach Treffern in einer Liste).
- **Muster:** `LIKE 'A%'` (Findet alles, was mit „A“ beginnt – das `%` ist dein Joker).
- **Logik:** `AND`, `OR`, `NOT` (Verknüpfe Bedingungen).

> **🔍 Stolperfalle NULL**  
> `NULL` bedeutet „unbekannt“ oder „nicht vorhanden“.  
> - ✅ Richtig: `WHERE ausleihdatum IS NULL` (findet nicht ausgeliehene Medien).  
> - ❌ Falsch: `WHERE ausleihdatum = NULL` – das liefert **nie** ein Ergebnis.  
> - ✅ Richtig: `WHERE ausleihdatum IS NOT NULL` (findet ausgeliehene Medien).  
>
> **Prüfungstipp:** Immer wenn ein Attribut optional ist, taucht `IS NULL` / `IS NOT NULL` in der Musterlösung auf.

> **Prüfungstipp:** Die IHK liebt Aufgaben, in denen du z. B. alle Mitarbeiter finden musst, die in Abteilung X arbeiten UND mehr als Y verdienen. Achte penibel auf die Anführungszeichen bei Texten (`'Müller'`), Zahlen stehen ohne da.

---

### 📊 Sortieren und Begrenzen – Ordnung muss sein

Stell dir vor, deine Abfrage liefert 10.000 Ergebnisse. Das liest niemand. Dafür gibt es:

- **`ORDER BY`**: Sortiert die Liste. `ASC` (aufsteigend, Standard) oder `DESC` (absteigend).  
  Beispiel: `ORDER BY nachname ASC, vorname ASC`
- **`LIMIT` / `TOP`**: Zeigt nur die ersten X Zeilen an (z. B. die „Top 10“ der Bestseller).

**DBMS-Unterschiede kurz notiert:**
- PostgreSQL, MySQL, SQLite: `SELECT ... LIMIT 10;`
- MS SQL Server: `SELECT TOP 10 ...`
- Oracle: `SELECT ... FETCH FIRST 10 ROWS ONLY;`

In den Übungen und Prüfungsbeispielen wird meist mit `LIMIT` (PostgreSQL/MySQL) gearbeitet.

---

### 🧩 Das Bibliotheks-Beispiel in Action

Wir nutzen unsere Tabellen `leser` und `medien` von vorhin.

**Szenario:** Du suchst alle Leser, die „Müller“ heißen, sortiert nach ihrem Vornamen.

```sql
SELECT vorname, nachname, leser_nr
FROM leser
WHERE nachname = 'Müller'
ORDER BY vorname ASC;
```

**Szenario:** Du willst alle Medien sehen, die zwischen dem 01.01.2024 und heute ausgeliehen wurden.

```sql
SELECT titel, ausleihdatum
FROM medien
WHERE ausleihdatum BETWEEN '2024-01-01' AND CURRENT_DATE;
```

> ⚠️ **Wichtig:** Datumsangaben in SQL immer in einfache Anführungszeichen und im Format `'JJJJ-MM-TT'` schreiben.

**Ausblick: Was kommt als Nächstes?**  
Was ist, wenn du alle Medien **samt Lesername** sehen willst? Dann musst du die Tabellen verknüpfen – das übernimmt der **JOIN**, den wir im nächsten SQL-Artikel behandeln. Als Appetitanreger:

```sql
SELECT medien.titel, leser.name
FROM medien
INNER JOIN leser ON medien.leser_id = leser.leser_id;
```

---

### 🧠 Das bringt’s dir im Alltag (Analogien)

**Handwerk / Lager:**  
Du stehst im Lager und suchst alle Schrauben (`SELECT *`), die im Regal B liegen (`FROM lager`), aber nur die mit einer Länge über 50 mm (`WHERE laenge > 50`). SQL macht genau das digital für dich.

**Kaufmännischer Bereich / Buchhaltung:**  
Du brauchst eine Liste aller offenen Rechnungen (`WHERE status = 'offen'`), die älter als 30 Tage sind (`AND rechnungsdatum < '...'`). Statt händisch zu blättern, liefert SQL dir das in Millisekunden.

**Gastronomie:**  
Ein Gast fragt nach vegetarischen Gerichten unter 15 Euro.

```sql
SELECT name, preis
FROM speisekarte
WHERE kategorie = 'vegetarisch' AND preis < 15.00;
```

**Das bringt's technisch:**  
- `SELECT` ist die Grundlage jeder Datenanalyse und jedes Berichts.  
- Mit `WHERE` filterst du präzise – das spart Bandbreite und Zeit.  
- `ORDER BY` und `LIMIT` machen Ergebnisse erst menschenlesbar und dashboardsauglich.

---

### 🚀 Agiler Workflow: „Test-Driven Querying“

In der modernen Entwicklung schreiben wir Abfragen oft erst in einem SQL-Tool (wie DBeaver), um sicherzustellen, dass die Daten stimmen, bevor wir sie fest in den Programmcode einbauen.

- **Iteratives Vorgehen:** Fang klein an (`SELECT * FROM tabelle`). Füge dann den Filter hinzu. Wenn das passt, schränke die Spalten ein.
- **Performance:** Im echten Job schreiben wir selten `SELECT *` (wähle alles), weil das bei Millionen Datensätzen das System ausbremst. Wir wählen gezielt nur die Spalten, die wir wirklich brauchen. Das ist effizient und „lean“.

---

### 👣 Dein nächster Schritt

1. **Daten füttern:** Nutze `INSERT INTO` (kommt im nächsten Artikel im Detail), um 5–10 Testzeilen in deine Tabellen zu schreiben.
2. **Experimentiere mit `WHERE`:** Versuche, alle Einträge zu finden, die ein bestimmtes Wort im Namen haben (`LIKE`).
3. **Kombiniere:** Baue eine Abfrage mit `WHERE`, `ORDER BY` und `LIMIT` gleichzeitig.
4. **NULL-Test:** Suche bewusst nach `IS NULL` und `IS NOT NULL` in deinen Testdaten.
5. **IHK-Check:** Nimm eine alte Prüfung und schau dir den Teil „Datenbanken“ an. Meistens ist die erste SQL-Aufgabe eine einfache `SELECT`-Abfrage. Kannst du sie jetzt lösen?
6. **Optional:** Probiere den JOIN-Ausblick in deinem SQL-Tool aus, um schon mal einen Vorgeschmack aufs Verknüpfen zu bekommen.

---

**Zusammengefasst:** Eine SQL-Abfrage ist wie eine präzise Bestellung beim Koch. Wenn du sagst „Ich will alles“, bekommst du alles. Wenn du sagst „Ich will das Schnitzel (Spalte), aber ohne Pommes (Bedingung)“, bekommst du genau das. Übe die `WHERE`-Logik und den Umgang mit `NULL`, denn sie sind das Herzstück jeder Datenauswertung!