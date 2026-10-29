

## 🔗 SQL JOINs und Aggregatfunktionen: Tabellen verknüpfen und Daten verdichten

### Worum geht’s eigentlich?

Die Stärke relationaler Datenbanken liegt nicht darin, eine einzelne Tabelle perfekt zu speichern – sondern **Beziehungen zwischen Tabellen** in Echtzeit auszuwerten.

Bisher hast du gelernt, mit `SELECT`, `FROM` und `WHERE` Daten aus *einer* Tabelle zu filtern. Sobald du aber wissen willst, **welcher Leser gerade welches Buch ausgeliehen hat** oder **wie viele Bücher ein Autor geschrieben hat**, brauchst du zwei mächtige Werkzeuge:

1. **JOINs** – sie verbinden Tabellen über gemeinsame Schlüssel.
2. **Aggregatfunktionen** – sie fassen viele Zeilen zu einer Kennzahl zusammen (`COUNT`, `SUM`, `AVG`, …).

Beides zusammen macht aus einzelnen Datensätzen aussagekräftige Berichte und Dashboards.

> 💡 **Agile Side-Info:** Im Sprint-Review will der Product Owner nicht wissen, ob die Tabelle `medien` existiert, sondern: „Wie viele Ausleihen hatten wir diese Woche?“ JOINs und Aggregatfunktionen sind deine Antwortmaschine.

---

### 🔧 Die JOIN-Familie – Tabellen logisch verbinden

Ein `JOIN` verknüpft zwei Tabellen, indem er für jede Zeile aus Tabelle A die passende(n) Zeile(n) aus Tabelle B nach einer Bedingung sucht – meistens über einen Fremdschlüssel.

| Join-Typ         | Symbol (oft) | Verhalten                                                                 | Analogie |
|------------------|--------------|---------------------------------------------------------------------------|----------|
| `INNER JOIN`     | ⋂            | Nur Zeilen, die in **beiden** Tabellen einen Partner haben.               | Nur Rechnungen, die auch einen Kunden haben – und umgekehrt. |
| `LEFT JOIN`      | ⟕            | Alle Zeilen aus der linken Tabelle, auch wenn rechts kein Partner existiert (dann `NULL`). | Alle Kunden, egal ob sie jemals bestellt haben. |
| `RIGHT JOIN`     | ⟖            | Alle Zeilen aus der rechten Tabelle, auch wenn links nichts passt.        | Alle Produkte, auch wenn sie noch nie bestellt wurden. |
| `FULL OUTER JOIN`| ⟗            | Alle Zeilen aus beiden Tabellen, fehlende Partner werden mit `NULL` aufgefüllt. | Eine komplette Inventur aller Verknüpfungen. |
| `CROSS JOIN`     | ×            | Jede Zeile aus A wird mit jeder aus B kombiniert (kartesisches Produkt).  | Jede Farbe mit jeder Größe – Vorsicht, explodiert schnell! |
| Self-Join        | (gleiche Tab) | Eine Tabelle wird mit sich selbst verknüpft, z. B. Mitarbeiter und Vorgesetzte. | Ein Stammbaum, der auf dieselbe Personentabelle zeigt. |

**Syntaxbeispiel (INNER JOIN):**

```sql
SELECT medien.titel, leser.name
FROM medien
INNER JOIN leser ON medien.leser_id = leser.leser_id;
```

> ⚠️ **Wichtig:** Wenn Spaltennamen in beiden Tabellen identisch sind (wie `leser_id`), musst du sie über den Tabellennamen qualifizieren: `medien.leser_id`.

> **Prüfungstipp:** Die IHK verlangt fast immer `INNER JOIN` (die klassische Verknüpfung) und gelegentlich `LEFT JOIN` für optionale Beziehungen. Das Schlüsselwort `ON` ist Pflicht – vergiss es nicht!

---

### 📊 Aggregatfunktionen – Aus vielen mach eins

Aggregatfunktionen verdichten viele Zeilen einer Spalte zu **einem einzigen Wert**. Sie werden fast immer zusammen mit `GROUP BY` verwendet.

| Funktion          | Bedeutung                                   | Beispiel                   |
|-------------------|---------------------------------------------|----------------------------|
| `COUNT(*)`        | Zählt die Anzahl der Zeilen.                | Wie viele Leser?           |
| `SUM(spalte)`     | Summiert alle Werte einer numerischen Spalte.| Gesamtpreis aller Bestellungen. |
| `AVG(spalte)`     | Durchschnitt einer numerischen Spalte.      | Durchschnittlicher Lagerbestand. |
| `MIN(spalte)`     | Kleinster Wert.                             | Günstigstes Produkt.       |
| `MAX(spalte)`     | Größter Wert.                               | Letztes Ausleihdatum.      |

`GROUP BY` teilt die Daten erst in Gruppen auf, dann wird die Aggregatfunktion für jede Gruppe berechnet. `HAVING` filtert diese Gruppen (wie `WHERE` für Zeilen, aber **nach** der Aggregation).

> **Prüfungstipp:**  
> - `WHERE` filtert **vor** der Gruppierung, `HAVING` filtert **danach**. Diese Unterscheidung ist ein IHK-Klassiker.  
> - Aggregatfunktionen ignorieren `NULL`-Werte (außer `COUNT(*)`).  
> - In einer `GROUP BY`-Abfrage dürfen im `SELECT` nur Spalten stehen, die in der `GROUP BY`-Klausel auftauchen, oder Aggregatfunktionen. Alles andere gibt einen Fehler.

---

### 🧩 Das Bibliotheksbeispiel – JOIN und GROUP BY in Aktion

**Szenario 1:** Zeige alle Medien mit dem Namen des aktuellen Ausleihers, auch wenn das Medium gerade nicht ausgeliehen ist (dann soll Name leer bleiben).

```sql
SELECT medien.titel, medien.ausleihdatum, leser.name
FROM medien
LEFT JOIN leser ON medien.leser_id = leser.leser_id
ORDER BY medien.titel;
```
`LEFT JOIN` stellt sicher, dass jedes Medium erscheint – ohne Ausleiher ist `leser.name` einfach `NULL`.

**Szenario 2:** Wie viele Medien hat jeder Autor geschrieben? (n:m-Auflösung)

```sql
SELECT autor.name, COUNT(autor_medium.medien_id) AS anzahl_werke
FROM autor
INNER JOIN autor_medium ON autor.autor_id = autor_medium.autor_id
GROUP BY autor.name
ORDER BY anzahl_werke DESC;
```
Hier geht der Weg über die Assoziationstabelle `autor_medium`. `GROUP BY autor.name` bündelt alle Zeilen je Autor, `COUNT` zählt die verknüpften Medien.

**Szenario 3:** Zeige alle Leser, die mehr als 3 Medien ausgeliehen haben (Top-Leser).

```sql
SELECT leser.name, COUNT(medien.medien_id) AS ausleihen
FROM leser
INNER JOIN medien ON leser.leser_id = medien.leser_id
GROUP BY leser.name
HAVING COUNT(medien.medien_id) > 3
ORDER BY ausleihen DESC;
```
Der Unterschied: `WHERE` könnte hier nicht `COUNT()` enthalten, weil die Aggregation erst mit `GROUP BY` passiert – also filtert `HAVING` die Gruppen.

---

### 🧠 Das bringt’s dir im Alltag (Analogien)

**Handwerk / Fertigung:**  
Ein JOIN ist wie eine Stückliste: Du holst dir die Teile (Einzelteile) und verknüpfst sie über die Baugruppe mit dem Endprodukt. Mit `GROUP BY` ermittelst du, wie viele Schrauben pro Produkt verwendet werden – das ist die Grundlage für Nachbestellungen.

**Kaufmännischer Bereich / Vertrieb:**  
Ein `LEFT JOIN` zwischen Kunden und Bestellungen zeigt dir sofort, welche Kunden seit Monaten nichts mehr bestellt haben (`WHERE bestellungen.id IS NULL`). `SUM(betrag)` plus `GROUP BY kunde_id` ergibt den Umsatz pro Kunde – dein monatlicher Report ist fertig.

**Gastronomie / Küche:**  
Du verknüpfst Gerichte mit Allergenen (n:m über `gericht_allergen`) und zählst, wie viele Gerichte ein bestimmtes Allergen enthalten. Ein `HAVING COUNT(*) > 5` zeigt dir die häufigsten Allergene, die du in der Karte markieren musst.

**Das bringt’s technisch:**  
- JOINs machen aus dem relationalen Schema erst ein lebendiges Informationsnetz.  
- Aggregatfunktionen liefern Kennzahlen – ohne sie wäre SQL nur ein besseres Karteikasten-Suchprogramm.  
- `GROUP BY` + `HAVING` sind das Fundament für jedes Reporting und Data-Warehouse-System.

---

### 🚀 Agiler Workflow: Inkrementelles Berichtebauen

- **Backlog-Item „Top-Kunden-Report“:** Du schreibst erst die Basistabelle (`FROM kunden`), fügst den JOIN zu `bestellungen` hinzu, testest im SQL-Tool, dann die Aggregation, dann das `HAVING`. Jeder Schritt liefert ein sichtbares Zwischenergebnis – wie ein Mini-Sprint.
- **Pair Querying:** Komplexe Abfragen mit JOINs über mehrere Tabellen entstehen im Team am Beamer. Einer tippt, der andere hinterfragt: „Brauchen wir hier `LEFT` oder `INNER`? Was passiert mit NULL?“
- **Refactoring von Views:** Wenn eine Abfrage öfter gebraucht wird, legen Entwickler eine **View** an – eine gespeicherte Abfrage, die wie eine virtuelle Tabelle wirkt. Das ist Agilität auf Datenbankebene.

🎯 **Side-Info:** In der Praxis werden große `GROUP BY`-Abfragen oft als **View** definiert, sodass Anwendungen sie wie eine Tabelle nutzen können. Das spart Code und sorgt für eine zentrale Definition der Geschäftslogik.

---

### 👣 Dein nächster Schritt

1. **JOIN-Experiment:** Führe alle JOIN-Typen an deinen Testdaten aus und beobachte die Unterschiede in der Ergebnismenge. Besonders `LEFT JOIN` mit `IS NULL` ist aufschlussreich.
2. **Aggregation üben:** Zähle, summiere und gruppiere nach Herzenslust. Nutze die Bibliotheksdatenbank: Wie viele Medien hat jeder Leser ausgeliehen? Welches Medium wurde am häufigsten ausgeliehen?
3. **HAVING nicht vergessen:** Filtere die Gruppen: Welche Autoren haben mehr als 2 Bücher? Welche Leser hatten noch nie ein Buch ausgeliehen (`COUNT = 0`)?
4. **IHK-Check:** Such dir eine alte Prüfungsaufgabe mit JOIN und GROUP BY heraus – oft verlangt die Aufgabe: „Ermitteln Sie die Anzahl der Bestellungen pro Kunde“ oder „Listen Sie alle Produkte mit dem Namen des Lieferanten auf“. Versuche, die Lösung selbstständig zu schreiben, und vergleiche dann.
5. **Zusatzaufgabe:** Wie könntest du mit einem Self-Join herausfinden, welcher Leser denselben Nachnamen hat wie ein anderer Leser? (Denk an `leser AS a JOIN leser AS b ON a.nachname = b.nachname AND a.leser_id <> b.leser_id`)

---

**Zusammengefasst:** JOINs und Aggregatfunktionen sind das Herzstück jeder praxisrelevanten SQL-Abfrage. JOINs knüpfen das Beziehungsnetz, das du im ERM entworfen hast, und Aggregatfunktionen berechnen daraus Werte, die Entscheidungen ermöglichen. Für die IHK-Prüfung solltest du `INNER JOIN`, `LEFT JOIN`, `GROUP BY` und `HAVING` sicher beherrschen – und vor allem verstehen, wann du sie einsetzt.