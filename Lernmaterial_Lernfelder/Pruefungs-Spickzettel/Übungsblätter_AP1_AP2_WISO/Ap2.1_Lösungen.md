# AP2-Übungsblatt (Anwendungsentwicklung) – Lösungen

> **Zugehörig zu:** [AP2_Aufgaben.md](AP2_Aufgaben.md)
> **Status:** Final
> **Stand:** 2026-09-28
>
> Musterlösungen mit Punktevergabe. Bei Freitext-, Programmier- und SQL-Aufgaben sind sinngemäß gleichwertige, fachlich richtige Lösungen ebenfalls zu werten (andere Variablennamen, Pseudocode statt Python, andere korrekte SQL-Formulierung). Folgefehler werden berücksichtigt: Wurde mit einem falschen Wert aus einem früheren Unterpunkt korrekt weitergearbeitet, sind die Punkte zu vergeben.

**Orientierungswert (Punkte-Noten-Schlüssel):** 100–92 Punkte = Note 1 · 91–81 = Note 2 · 80–67 = Note 3 · 66–50 = Note 4 · 49–30 = Note 5 · 29–0 = Note 6. Der Schlüssel kann je nach IHK bzw. Prüfung abweichen und ist nicht Bestandteil der echten AP2-Bewertung.

---

## 1. Aufgabe (25 Punkte)

**a) Schreibtischtest `mietpreis(5, 12)` (7 Punkte)**

| tag | tag <= 3 ? | preis (nach dem Durchlauf) |
|---:|---|---:|
| 1 | ja | 12 |
| 2 | ja | 24 |
| 3 | ja | 36 |
| 4 | nein | 42 |
| 5 | nein | 48 |

Rückgabewert: **48** (technisch `48.0`).

Die Funktion berechnet den Mietpreis für die angegebene Zahl von Tagen: Die ersten drei Tage kosten den vollen Tagespreis, ab dem vierten Tag wird nur der halbe Tagespreis berechnet.

*Punkte: je Zeile 1 Punkt (Bedingung und Preis richtig) = 5 Punkte, Rückgabewert 1 Punkt, Erklärung 1 Punkt.*

**b) Fehlersuche `finde_rad` (6 Punkte)**

- **ba)** Das `return -1` steht im `else`-Zweig **innerhalb** der Schleife. Die Funktion bricht deshalb schon nach dem Vergleich mit dem ersten Element ab. „Nicht gefunden“ darf erst nach der Schleife festgestellt werden, wenn alle Elemente geprüft wurden. *(2 Punkte)*
- **bb)** Beispiel: `finde_rad([101, 105, 110], 105)`. Erwartet: `1`. Tatsächlich: `-1`. Falsch ist jede Eingabe, bei der die gesuchte Nummer nicht das erste Element ist. Zusätzlicher Fehler: Bei einer leeren Liste liefert die Funktion `None` statt `-1`. *(2 Punkte: 1 Punkt für eine passende Eingabe, 1 Punkt für erwartetes und tatsächliches Ergebnis)*
- **bc)** Korrektur *(2 Punkte)*:

```python
def finde_rad(raeder, nummer):
    for i in range(len(raeder)):
        if raeder[i] == nummer:
            return i
    return -1
```

Hinweis: Der Fehler ist ein Logikfehler. Das Programm läuft ohne Fehlermeldung und liefert trotzdem falsche Ergebnisse. Er fällt nur durch Testfälle auf, bei denen die gesuchte Nummer nicht an erster Stelle steht.

**c) Funktionen erstellen (12 Punkte)**

Musterlösung (Python):

```python
def zaehle_teure(tagespreise, grenze):
    anzahl = 0
    for preis in tagespreise:
        if preis > grenze:
            anzahl = anzahl + 1
    return anzahl


def hoechster_preis(tagespreise):
    if len(tagespreise) == 0:
        return None
    hoechster = tagespreise[0]
    for preis in tagespreise:
        if preis > hoechster:
            hoechster = preis
    return hoechster
```

- **ca) `zaehle_teure` (6 Punkte, je 1 Punkt):** Funktion mit zwei Parametern richtig definiert; Zähler mit 0 initialisiert; Schleife über alle Preise; Vergleich mit `>` (nicht `>=`); Zähler wird nur bei Treffer erhöht; Rückgabe nach der Schleife.
- **cb) `hoechster_preis` (6 Punkte, je 1 Punkt):** sinnvoller Startwert (erstes Element oder ein sehr kleiner Wert); Schleife über die Liste; Vergleich mit dem bisherigen Höchstwert; Höchstwert wird aktualisiert; Rückgabe nach der Schleife; Umgang mit der leeren Liste festgelegt und notiert (z. B. `None` zurückgeben oder ausdrücklich die Annahme „Liste nicht leer“ festhalten).

Typischer Fehler: Startwert 0 für den Höchstwert. Das funktioniert nur, solange alle Preise positiv sind, und ist bei einer allgemeinen Funktion unsauber.

---

## 2. Aufgabe (25 Punkte)

**a) Pseudocode ergänzen (5 Punkte)**

- (1) `mitte + 1` · (2) `mitte − 1` · (3) `−1` *(3 Punkte, je 1 Punkt)*
- Voraussetzung: Die Liste muss **aufsteigend sortiert** sein. *(1 Punkt)*
- `DIV` ist die **ganzzahlige Division**: Der Nachkommaanteil entfällt, z. B. `7 DIV 2 = 3`. *(1 Punkt)*

Erläuterung: Ist der Wert in der Mitte kleiner als das Ziel, liegt das Ziel rechts davon, also beginnt die Suche bei `mitte + 1`. Ist er größer, liegt das Ziel links, also endet die Suche bei `mitte − 1`. Bleibt der Bereich leer (`links > rechts`), kommt das Ziel nicht vor: Rückgabe `−1`.

**b) Ablauf für `ziel = 142` (6 Punkte)**

| Durchlauf | links | rechts | mitte | liste[mitte] |
|---:|---:|---:|---:|---:|
| 1 | 0 | 6 | 3 | 118 |
| 2 | 4 | 6 | 5 | 130 |
| 3 | 6 | 6 | 6 | 142 |

- Tabelle: 3 Punkte (je Durchlauf 1 Punkt)
- Rückgabewert: **6** (Index der Zahl 142, gezählt ab 0) *(1 Punkt)*
- Durchläufe: **3** *(1 Punkt)*
- Lineare Suche: **7 Vergleiche**, da 142 an letzter Stelle steht *(1 Punkt)*

**c) Vergleich der Suchverfahren (4 Punkte)**

- **ca)** Lineare Suche: **O(n)**. Binäre Suche: **O(log n)**. *(je 1 Punkt)*
- **cb)** Höchstens **10 Durchläufe**. Größtmögliche Größe des Suchbereichs vor dem 1. bis 10. Durchlauf: 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1. In jedem Durchlauf entfällt das mittlere Element, und der Rest wird mindestens halbiert. Allgemein gilt: höchstens ⌊log₂ n⌋ + 1 Durchläufe, für n = 1000 also 9 + 1 = 10 (2⁹ = 512 ≤ 1000 < 1024 = 2¹⁰). Eine Begründung über das wiederholte Halbieren oder über 2¹⁰ ≥ 1000 genügt. *(1 Punkt Ergebnis, 1 Punkt Begründung)*

**d) UML-Aktivitätsdiagramm (10 Punkte)**

Musterlösung in Textform (Aktionen in spitzen Klammern, Entscheidungsknoten als Raute, Wächter in eckigen Klammern):

```text
(●) Start
 │
<Kundennummer einlesen>
 │
◇ Kunde gesperrt? ──[ja]──> <Meldung „Ausleihe nicht möglich“> ──> (◉) Ende
 │
 [nein]
 │
<Radnummer einlesen>
 │
◇ Rad verfügbar? ──[nein]──> <Meldung „Rad nicht verfügbar“> ──> (◉) Ende
 │
 [ja]
 │
<Ausleihe speichern>
 │
<Bestätigung ausgeben>
 │
(◉) Ende
```

Symbole: `(●)` Startknoten (ausgefüllter Kreis), `(◉)` Endknoten (Kreis mit ausgefülltem Punkt darin), `◇` Entscheidungsknoten (Raute), `<...>` Aktion (abgerundetes Rechteck), `[ja]`/`[nein]` Wächter an den ausgehenden Kanten der Entscheidungsknoten.

*Punkte:*

- Startknoten (ausgefüllter Kreis) vorhanden und mit dem ersten Schritt verbunden: 1 Punkt
- Endknoten (Kreis mit ausgefülltem Punkt) vorhanden; ein gemeinsamer Endknoten oder mehrere Endknoten sind beide zulässig: 1 Punkt
- Aktionen mit abgerundeten Rechtecken, mindestens vier richtig benannt (Kundennummer einlesen, Radnummer einlesen, Ausleihe speichern, Bestätigung ausgeben; die Meldungen zählen ebenfalls): 2 Punkte
- Zwei Entscheidungsknoten (Rauten) für „gesperrt?“ und „verfügbar?“: 2 Punkte
- Wächter (`[ja]`/`[nein]`) an allen ausgehenden Kanten der Rauten: 2 Punkte
- Kontrollfluss vollständig und in der richtigen Reihenfolge, Meldungszweige münden im Ende: 2 Punkte

---

## 3. Aufgabe (25 Punkte)

**a) Äquivalenzklassen (6 Punkte)**

| Nr. | Äquivalenzklasse (Bereich) | gültig / ungültig | Testwert (Beispiel) |
|---:|---|---|---:|
| 1 | tage < 1 (0 und kleiner) | ungültig | 0 |
| 2 | 1 ≤ tage ≤ 2 | gültig | 2 |
| 3 | 3 ≤ tage ≤ 6 | gültig | 4 |
| 4 | tage ≥ 7 | gültig | 10 |

- Tabelle: 4 Punkte (je Klasse 1 Punkt)
- Gültige Klassen enthalten Werte, für die die Funktion ein normales Ergebnis liefern soll. Ungültige Klassen enthalten Werte, bei denen eine Fehlerbehandlung erwartet wird (hier `ValueError`). *(1 Punkt)*
- Vorteil: Werte derselben Äquivalenzklasse werden hinsichtlich des erwarteten Verhaltens als gleichwertig betrachtet; deshalb genügt ein repräsentativer Testwert je Klasse. Das verringert die Zahl der Testfälle bei vergleichbarer Abdeckung. *(1 Punkt)*

**b) Grenzwertanalyse (6 Punkte)**

| Testfall | Eingabe `tage` | erwartetes Ergebnis |
|---:|---:|---|
| 1 | 0 | `ValueError` |
| 2 | 1 | 0 |
| 3 | 2 | 0 |
| 4 | 3 | 10 |
| 5 | 6 | 10 |
| 6 | 7 | 20 |

*Punkte: je Testfall 1 Punkt (richtiger Grenzwert mit richtigem erwartetem Ergebnis). Die Reihenfolge ist beliebig. Die Werte liegen beiderseits der drei Klassengrenzen (0 | 1, 2 | 3, 6 | 7). Zusätzliche Testfälle sind zulässig, gewertet werden sechs.*

**c) Testarten (4 Punkte)**

- **ca)** Beim **Black-Box-Test** wird nur anhand der Spezifikation (Eingabe und erwartetes Ergebnis) getestet, ohne den Programmcode zu kennen. Beim **White-Box-Test** wird mit Kenntnis der Codestruktur getestet, z. B. so, dass alle Zweige oder Anweisungen durchlaufen werden. *(je 1 Punkt)*
- **cb)** **Black-Box-Test**, denn Äquivalenzklassen und Grenzwerte werden aus der Anforderung abgeleitet. *(1 Punkt)*
- **cc)** Ein Modultest testet eine einzelne, kleine Programmeinheit (z. B. eine Funktion oder Klasse) isoliert vom Rest des Programms. *(1 Punkt)*

**d) Automatisierter Test (5 Punkte)**

- (1) `0` · (2) `10` · (3) `20` *(3 Punkte, je 1 Punkt)*
- Erklärung *(2 Punkte)*: Löst `rabatt(0)` **keinen** `ValueError` aus, läuft der `try`-Block ohne Ausnahme weiter und erreicht `assert False`. Dieses lässt den Test bewusst scheitern. Ohne diese Zeile würde der Test auch dann „bestanden“ sein, wenn die Funktion den ungültigen Wert nicht abweist. Wird dagegen ein `ValueError` ausgelöst, springt das Programm in den `except`-Zweig und `assert False` wird übersprungen.

**e) Fehler in der Umsetzung (4 Punkte)**

- **ea)** Testfall 5 (`tage = 6`) schlägt fehl. Erwartet: **10**. Tatsächlich: **20**. *(2 Punkte)*
- **eb)** Ursache: Die Schwelle lautet `>= 6` statt `>= 7` (Grenzwertfehler, „Off-by-one“). Korrektur: `if tage >= 7:` *(2 Punkte)*

Beobachtung: Die Testfälle für 3 und 7 laufen trotz des Fehlers durch, ebenso ein Testwert wie 4 oder 10 aus der Äquivalenzklassenbildung. Der Fehler wird nur durch den Grenzwert 6 aufgedeckt. Deshalb ergänzen Grenzwerttests die Äquivalenzklassen sinnvoll.

---

## 4. Aufgabe (25 Punkte)

**a) E-Bikes über 29 EUR (2 Punkte)**

```sql
SELECT *
FROM rad
WHERE typ = 'E-Bike' AND tagespreis > 29;
```

Ergebnis: Rad 118, E-Bike, 30,00. *(1 Punkt SELECT/FROM, 1 Punkt WHERE mit beiden Bedingungen)* Eine explizite Spaltenauswahl (`SELECT radnr, typ, tagespreis`) ist gleichwertig und für die Praxis sauberer als `SELECT *`.

**b) Kunden aus Kiel (3 Punkte)**

```sql
SELECT name, ort
FROM kunde
WHERE ort = 'Kiel'
ORDER BY name;
```

Ergebnis: Ahlers, Clausen, Hansen (jeweils Kiel). *(1 Punkt Spaltenauswahl, 1 Punkt WHERE, 1 Punkt ORDER BY)*

**c) Ausleihen mit Kosten (5 Punkte)**

```sql
SELECT k.name, r.typ, a.tage, a.tage * r.tagespreis AS kosten
FROM ausleihe a
JOIN kunde k ON a.kundennr = k.kundennr
JOIN rad r ON a.radnr = r.radnr;
```

Ergebnis:

| name | typ | tage | kosten |
|---|---|---:|---:|
| Hansen | E-Bike | 3 | 85,50 |
| Ahlers | Citybike | 2 | 24,00 |
| Hansen | E-Bike | 7 | 210,00 |
| Petersen | Mountainbike | 1 | 18,00 |
| Ahlers | E-Bike | 4 | 114,00 |
| Clausen | Citybike | 5 | 60,00 |

*Punkte: Join mit `kunde` und richtiger Bedingung 1 Punkt, Join mit `rad` und richtiger Bedingung 1 Punkt, richtige Spaltenauswahl 1 Punkt, Berechnung `tage * tagespreis` 1 Punkt, Alias `kosten` 1 Punkt. Eine Formulierung mit Komma-Join und `WHERE` ist gleichwertig.*

**d) Kunden mit mehr als 5 Ausleihtagen (6 Punkte)**

```sql
SELECT k.name, SUM(a.tage) AS gesamttage
FROM kunde k
JOIN ausleihe a ON k.kundennr = a.kundennr
GROUP BY k.kundennr, k.name
HAVING SUM(a.tage) > 5
ORDER BY gesamttage DESC;
```

Ergebnis:

| name | gesamttage |
|---|---:|
| Hansen | 10 |
| Ahlers | 6 |

*Punkte: Join 1 Punkt, `SUM` mit Alias 1 Punkt, `GROUP BY` 1 Punkt, Bedingung im `HAVING` 2 Punkte, `ORDER BY ... DESC` 1 Punkt.*

Typischer Fehler: Die Bedingung auf die Summe steht im `WHERE`. Das ist nicht zulässig, weil `WHERE` vor der Gruppierung auswertet. Bedingungen auf Aggregatfunktionen gehören in `HAVING`.

**e) Kunden ohne Ausleihe (4 Punkte)**

```sql
SELECT k.name
FROM kunde k
LEFT JOIN ausleihe a ON k.kundennr = a.kundennr
WHERE a.ausleihnr IS NULL;
```

Gleichwertige Lösungen mit Unterabfrage:

```sql
SELECT name
FROM kunde
WHERE kundennr NOT IN (SELECT kundennr FROM ausleihe);
```

```sql
SELECT name
FROM kunde k
WHERE NOT EXISTS (SELECT 1 FROM ausleihe a WHERE a.kundennr = k.kundennr);
```

Ergebnis: Brandt. *(2 Punkte für einen richtigen Ansatz mit `LEFT JOIN` oder Unterabfrage, 1 Punkt für die korrekte Erkennung von Kunden ohne passende Ausleihe, 1 Punkt für die richtige Spalte)*

Hinweis: Die Variante mit `NOT IN` gilt für die gezeigten Daten. Enthielte `ausleihe.kundennr` einen `NULL`-Wert, würde `NOT IN` gar kein Ergebnis liefern. `NOT EXISTS` und `LEFT JOIN ... IS NULL` sind davon nicht betroffen.

Typischer Fehler: Ein `INNER JOIN` liefert nur Kunden **mit** Ausleihen und kann die gesuchten Kunden gar nicht enthalten.

**f) Daten ändern (5 Punkte)**

```sql
UPDATE rad
SET tagespreis = tagespreis * 1.10
WHERE typ = 'E-Bike';
```

*(3 Punkte: `UPDATE`/`SET` 1 Punkt, Berechnung 1 Punkt, `WHERE` 1 Punkt.)* Ergebnis: Rad 105 kostet danach 31,35 EUR, Rad 118 kostet 33,00 EUR. Ohne `WHERE` würden alle Fahrräder teurer.

```sql
INSERT INTO kunde (kundennr, name, ort, stammkunde)
VALUES (6, 'Dietz', 'Kiel', 0);
```

*(2 Punkte: Tabelle und Spalten 1 Punkt, Werte in der richtigen Reihenfolge und mit Textwerten in Anführungszeichen 1 Punkt.)*

---

```yaml
dokument: AP2-Uebungsblatt-Loesungen
lernfeld: "Querschnittsthema, kein einzelnes Lernfeld (Ergänzung zum Pruefungs-Spickzettel-Block)"
titel: "AP2-Übungsblatt Anwendungsentwicklung - Entwicklung und Umsetzung von Algorithmen (Lösungen)"
typ: "Übungsaufgaben mit separatem Lösungsblatt"
status: final
stand: 2026-09-28
quellen_intern:
  - "Ergänzung zu Pruefungs-Spickzettel/Part_3_AP2.md und dem AP1-Übungsblatt - vier Szenario-Aufgaben zu je 25 Punkten; das Blatt orientiert sich strukturell an den vier in § 14 FIAusbV genannten Nachweisen (je eine Aufgabe)"
  - "Der AP2-Teil deckt bewusst die Anwendungsentwicklung ab (Prüfungsbereich Entwicklung und Umsetzung von Algorithmen); der Prüfungsbereich Planen eines Softwareproduktes (§ 13 FIAusbV) ist nicht Teil dieses Blatts"
quellen_fachlich:
  - titel: "Fachinformatikerausbildungsverordnung (FIAusbV), § 14 Prüfungsbereich Entwicklung und Umsetzung von Algorithmen"
    herausgeber: "Bundesministerium der Justiz, Gesetze im Internet"
    status: "Direkt eingesehen. § 14 nennt vier Nachweise (Programmcode interpretieren und Lösung in einer Programmiersprache erstellen; Algorithmen in Programmierlogik übertragen und grafisch darstellen; Testszenarien auswählen und Testdaten generieren; Abfragen zur Gewinnung und Manipulation von Daten erstellen), praxisbezogene schriftliche Aufgaben, 90 Minuten Prüfungszeit. Das Blatt orientiert sich strukturell an diesen vier Nachweisen (je eine Aufgabe)"
  - titel: "Prüfungskatalog für die Fachrichtung Anwendungsentwicklung (AP2)"
    herausgeber: "ZPA Nord-West / U-Form Verlag"
    status: "Lag bei der Erstellung nicht vor. Konkrete Aufgabenzahl, Punkteverteilung, Aufgabenformate und die Frage, welche Darstellungsformen bei 'grafisch darstellen' verlangt werden, sind daher nicht gegen den Katalog geprüft. Gewählt wurde das UML-Aktivitätsdiagramm als Übungsentscheidung, nicht als Aussage über die echte Prüfung"
review_historie:
  - runde: 1
    datum: 2026-09-28
    ergebnis: "Erstdraft erstellt. Aufbau entlang der vier Nachweise aus § 14 FIAusbV, Szenario (Fahrradverleih) bewusst abweichend von realen Prüfungsszenarien gewählt. Vor dem Schreiben wurden alle Programmierlösungen ausgeführt (Schreibtischtest mietpreis, Fehler in finde_rad, Hilfsfunktionen, binäre Suche inkl. Ablauf für ziel 142 und maximaler Durchlaufzahl bei 1000 Einträgen per Durchprobieren aller Ziele, fehlerhafte und korrekte rabatt-Funktion mit allen sechs Grenzwerten) und alle SQL-Lösungen auf einer echten SQLite-Datenbank mit den im Aufgabenblatt abgedruckten Daten ausgeführt; die Ergebnistabellen im Lösungsblatt stammen aus diesen Läufen. Punktsummen je Aufgabe nachgezählt (jeweils 25)."
  - runde: 2
    datum: 2026-09-28
    ergebnis: "3 Reviews eingearbeitet, alle ohne verbliebenen fachlichen Fehler in den Lösungen. Vor dem Umsetzen gegen die Dateien geprüft: Die gemeldete verlorene Einrückung in den Codeblöcken existiert nicht (if und else stehen in der Datei auf gleicher Ebene, alle Blöcke außer dem bewusst lückenhaften Lückentest 3d kompilieren). Die im Review vorgeschlagene 'korrigierte' Halbierungsfolge für 2c (aufgerundet, 11 Werte) wäre falsch, sie ergäbe 11 statt der tatsächlichen 10 Durchläufe - die Folge im Lösungsblatt war richtig, sie zeigt die Größe des Suchbereichs vor jedem Durchlauf; nur die Formulierung wurde präzisiert (Suchbereich vor dem 1. bis 10. Durchlauf, Formel floor(log2 n) + 1, 2^9 = 512 <= 1000 < 1024). Zweifach bestätigt und umgesetzt: Parameter tage ist jetzt ausdrücklich eine ganze Zahl; Notenschlüssel als Orientierungswert gekennzeichnet (kann je nach IHK bzw. Prüfung abweichen, nicht Bestandteil der echten AP2-Bewertung). Weitere Umsetzungen: Punktevergabe 3a eindeutig (je Klasse 1 Punkt für die vollständig richtige Zeile); Aufgabe 3b verlangt die beiden Werte beiderseits jeder der drei Klassengrenzen, damit die sechs Grenzwerte eindeutig sind; UML-Aktivitätsdiagramm ausdrücklich als Übungsentscheidung gekennzeichnet (Hinweis im Aufgabenblatt und in den Quellenangaben); Formulierung 'orientiert sich strukturell an den vier Nachweisen' statt 'folgt den Nachweisen'; Hinweis, dass der Umfang für eine Übung bewusst dicht ist; 1c erlaubt ausdrücklich len() und range() und verbietet max(), min(), sum(), leere-Liste-Festlegung 'jede nachvollziehbare Festlegung genügt'; Symbolerklärung zur Textskizze des Aktivitätsdiagramms; 4a mit Hinweis auf explizite Spaltenauswahl; 4e um NOT EXISTS ergänzt und Hinweis, dass NOT IN bei NULL-Werten in der Unterabfrage kein Ergebnis liefert (per Test bestätigt), Punktebeschreibung allgemeiner gefasst. Nicht übernommen: YAML aus dem Lösungsblatt entfernen (entspricht der Konvention der Sammlung); Wiederholung der Voraussetzung 'sortiert' in 2a (bewusst als Verständnisfrage beibehalten). Den Status setzt David."
  - runde: 3
    datum: 2026-09-28
    ergebnis: "2 Re-Reviews eingearbeitet, beide ohne fachlichen Fehler in Aufgaben oder Lösungen, Punkte 4 x 25 erneut bestätigt. Umgesetzt: Die Textskizze des Aktivitätsdiagramms verwendete eckige Klammern sowohl für Aktionen als auch für die Wächter [ja]/[nein] und war dadurch verwechselbar - Aktionen jetzt in spitzen Klammern, Entscheidungsknoten als Raute, Wächter in eckigen Klammern, Symbolerklärung angepasst; 3a-Vorteil von Äquivalenzklassen weniger absolut formuliert ('werden hinsichtlich des erwarteten Verhaltens als gleichwertig betrachtet' statt 'verhält sich gleich'); 2c-Formulierung auf 'größtmögliche Größe des Suchbereichs' präzisiert (die Folge selbst war richtig und zeigt die obere Schranke je Durchlauf). Nicht geändert: Notenschlüssel bleibt als Orientierungswert im Blatt (Review nennt ihn nach der Kennzeichnung nicht mehr als Fehler); YAML bleibt in der Lösungsdatei. Den Status setzt David."
  - runde: 4
    datum: 2026-09-28
    ergebnis: "Abschluss-Selbstcheck, danach von David final freigegeben. Beide Dateien vollständig gelesen. Zwei Fehler gefunden und behoben: Im Aufgabenblatt standen die drei Tabellenschemata (kunde, rad, ausleihe) ohne Leerzeilen untereinander und wären in Markdown zu einem Absatz zusammengeflossen, außerdem war die Primärschlüssel-Kennzeichnung per HTML-Unterstreichung nicht überall darstellbar - jetzt als Aufzählung mit (PK); im YAML des Lösungsblatts stand noch 'folgen diesen vier Nachweisen', was der bereits geänderten Formulierung 'orientiert sich strukturell' widersprach. Endlauf: Punktsummen (25 je Aufgabe, 100 gesamt, Teilpunkte je Unterpunkt), alle SQL-Lösungen auf einer aus den Tabellen des Aufgabenblatts gebauten SQLite-Datenbank, alle Python-Lösungen, Grenzwert-Tabelle gegen korrekte und fehlerhafte rabatt-Funktion (nur Grenzwert 6 deckt den Fehler auf), Schreibtischtest 48, binäre Suche für 142, YAML und Markdown. Die Aussagen zum fehlenden FIAE-AP2-Katalog bleiben ausdrücklich im Blatt und in den Quellenangaben stehen."
naechste_review: "Bei Vorliegen des Prüfungskatalogs für die Fachrichtung Anwendungsentwicklung (Abgleich von Aufgabenzahl, Punkteverteilung und Darstellungsformen) oder nach Auswertung neuer AP2-Prüfungen"
```