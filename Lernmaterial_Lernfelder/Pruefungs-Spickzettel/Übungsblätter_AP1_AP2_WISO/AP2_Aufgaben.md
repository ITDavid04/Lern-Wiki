# AP2-Übungsblatt (Anwendungsentwicklung) – Entwicklung und Umsetzung von Algorithmen

> **Zielgruppe:** Umschülerinnen und Umschüler sowie Auszubildende zum/zur Fachinformatiker/in Anwendungsentwicklung
> **Zweck:** Übungsblatt zur Vorbereitung auf den AP2-Prüfungsbereich „Entwicklung und Umsetzung von Algorithmen“, als Ergänzung zu den Spickzetteln und dem AP1-Übungsblatt. Lösungen: [Ap2.1_Lösungen.md](Ap2.1_Lösungen.md).
> **Status:** Final
> **Stand:** 2026-09-28
>
> **Hinweis zum Format:** Der Prüfungsbereich dauert 90 Minuten, die Aufgaben sind praxisbezogen und schriftlich zu bearbeiten (§ 14 FIAusbV). Dieses Übungsblatt umfasst 100 Punkte, verteilt auf vier Szenario-Aufgaben zu je 25 Punkten. Es orientiert sich strukturell an den vier Nachweisen, die § 14 FIAusbV nennt: Programmcode interpretieren und Lösungen erstellen, Algorithmen in Programmierlogik übertragen und grafisch darstellen, Testszenarien und Testdaten auswählen, Datenabfragen erstellen. Der Prüfungskatalog für diesen Bereich lag bei der Erstellung nicht vor. Aufgabenzahl, Punkteverteilung und Aufgabenformate der echten Prüfung können deshalb abweichen; eine 1:1-Simulation ist das Blatt nicht. Die Darstellungsform UML-Aktivitätsdiagramm in Aufgabe 2d dient der Übung und sagt nichts darüber aus, dass sie in der echten Prüfung verlangt wird. Der Umfang ist für eine Übung bewusst dicht; im Übungsdurchlauf ist es normal, mehr als 90 Minuten zu brauchen.
>
> **Hinweis:** Ausgangssituation, Firmennamen, Daten und Aufgaben sind frei erfunden. Keine Aufgabe ist einer realen Prüfung entnommen oder nachgebildet.

---

## Bearbeitungshinweise

- Bearbeitungszeit: 90 Minuten, Gesamtpunktzahl: 100 Punkte
- Lesen Sie den Text der Aufgaben ganz durch, bevor Sie mit der Bearbeitung beginnen.
- Programmieraufgaben dürfen in Python oder in Pseudocode gelöst werden. Auf Syntaxdetails kommt es nur dort an, wo ausdrücklich nach Fehlern gefragt wird.
- SQL-Abfragen sind in Standard-SQL zu formulieren (SQLite-Syntax genügt).
- Halten Sie sich beim Umfang der Antwort an die Vorgabe der Aufgabenstellung. Werden zwei Angaben gefordert und Sie führen vier an, zählen nur die ersten zwei.
- Erlaubtes Hilfsmittel in diesem Übungsblatt: nicht programmierbarer, netzunabhängiger Taschenrechner ohne Kommunikationsmöglichkeit mit Dritten. In der echten Prüfung gelten die Angaben in Einladung und Prüfungsunterlagen.

---

## Ausgangssituation

Sie arbeiten bei der **Küstenwerk Software GmbH** und entwickeln für den Fahrradverleih **RadHaus Nord** eine Verwaltungssoftware. Die Software ist in Python geschrieben, die Daten liegen in einer relationalen Datenbank. Kunden leihen Fahrräder für mehrere Tage aus.

Bearbeiten Sie die folgenden Aufgaben:

- Mietpreise berechnen und vorhandenen Code prüfen
- Fahrräder suchen und Abläufe darstellen
- Die Preislogik testen
- Daten mit SQL abfragen und ändern

---

## 1. Aufgabe (25 Punkte)

**a)** Die folgende Funktion berechnet den Mietpreis. Führen Sie einen Schreibtischtest für den Aufruf `mietpreis(5, 12)` durch und erklären Sie in einem Satz, was die Funktion berechnet. **7 Punkte**

```python
def mietpreis(tage, tagespreis):
    preis = 0
    for tag in range(1, tage + 1):
        if tag <= 3:
            preis = preis + tagespreis
        else:
            preis = preis + tagespreis * 0.5
    return preis
```

| tag | tag <= 3 ? | preis (nach dem Durchlauf) |
|---:|---|---:|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

Rückgabewert: ______

Die Funktion berechnet: ____________________________________________

**b)** Die folgende Funktion soll die Position einer Radnummer in einer Liste zurückgeben und `-1`, wenn die Nummer nicht vorkommt. Sie liefert aber für bestimmte Eingaben ein falsches Ergebnis. **6 Punkte**

```python
def finde_rad(raeder, nummer):
    for i in range(len(raeder)):
        if raeder[i] == nummer:
            return i
        else:
            return -1
```

- ba) Beschreiben Sie den Fehler. *(2 Punkte)*
- bb) Geben Sie eine Eingabe an, für die das Ergebnis falsch ist, und nennen Sie erwartetes und tatsächliches Ergebnis. *(2 Punkte)*
- bc) Geben Sie eine korrigierte Fassung der Funktion an. *(2 Punkte)*

**c)** Schreiben Sie die folgenden zwei Funktionen ohne Verwendung der Funktionen `max()`, `min()` und `sum()` (`len()` und `range()` dürfen Sie verwenden). **12 Punkte**

- ca) `zaehle_teure(tagespreise, grenze)` erhält eine Liste von Tagespreisen und gibt zurück, wie viele Preise **größer** als `grenze` sind. Beispiel: `zaehle_teure([12, 28.5, 18, 30, 11.5], 15)` liefert `3`. *(6 Punkte)*
- cb) `hoechster_preis(tagespreise)` gibt den höchsten Preis der Liste zurück. Beispiel: `hoechster_preis([12, 28.5, 18, 30, 11.5])` liefert `30`. Legen Sie fest und notieren Sie, wie Ihre Funktion mit einer leeren Liste umgeht; jede nachvollziehbare Festlegung genügt. *(6 Punkte)*

---

## 2. Aufgabe (25 Punkte)

Die Radnummern werden aufsteigend sortiert in einer Liste gehalten. Die Suche soll deshalb mit einer binären Suche erfolgen.

**a)** Ergänzen Sie den folgenden Pseudocode. Nennen Sie außerdem die Voraussetzung, die die Liste erfüllen muss, und erklären Sie, was der Operator `DIV` bewirkt. **5 Punkte**

```text
FUNKTION binaersuche(liste, ziel)
    links ← 0
    rechts ← LÄNGE(liste) − 1
    SOLANGE links ≤ rechts
        mitte ← (links + rechts) DIV 2
        WENN liste[mitte] = ziel DANN
            GIB mitte ZURÜCK
        SONST WENN liste[mitte] < ziel DANN
            links ← (1) ______
        SONST
            rechts ← (2) ______
        ENDE WENN
    ENDE SOLANGE
    GIB (3) ______ ZURÜCK
ENDE FUNKTION
```

- Fehlende Angaben (1) bis (3): *(3 Punkte)*
- Voraussetzung an die Liste: *(1 Punkt)*
- Wirkung von `DIV`: *(1 Punkt)*

**b)** Führen Sie den Algorithmus für `liste = [101, 105, 110, 118, 123, 130, 142]` und `ziel = 142` von Hand aus. **6 Punkte**

| Durchlauf | links | rechts | mitte | liste[mitte] |
|---:|---:|---:|---:|---:|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

- Tabelle ausfüllen: *(3 Punkte, je Durchlauf 1 Punkt)*
- Rückgabewert der Funktion: *(1 Punkt)*
- Wie viele Durchläufe der Schleife waren nötig? *(1 Punkt)*
- Wie viele Vergleiche hätte eine lineare Suche von vorn nach hinten für dieselbe Suche gebraucht? *(1 Punkt)*

**c)** Vergleichen Sie die lineare mit der binären Suche. **4 Punkte**

- ca) Geben Sie die Laufzeitklasse (O-Notation) der linearen und der binären Suche an. *(2 Punkte)*
- cb) Wie viele Schleifendurchläufe braucht die binäre Suche bei 1000 Einträgen höchstens? Begründen Sie kurz. *(2 Punkte)*

**d)** Der folgende Ablauf der Ausleihe soll dokumentiert werden. Stellen Sie ihn als UML-Aktivitätsdiagramm dar (auf einem eigenen Blatt). **10 Punkte**

Ablauf:

1. Der Ablauf beginnt mit dem Einlesen der Kundennummer.
2. Ist der Kunde gesperrt, wird die Meldung „Ausleihe nicht möglich“ ausgegeben und der Ablauf endet.
3. Andernfalls wird die Radnummer eingelesen.
4. Ist das Rad nicht verfügbar, wird die Meldung „Rad nicht verfügbar“ ausgegeben und der Ablauf endet.
5. Andernfalls wird die Ausleihe gespeichert und eine Bestätigung ausgegeben. Danach endet der Ablauf.

---

## 3. Aufgabe (25 Punkte)

Die Funktion `rabatt(tage)` liefert den Rabatt in Prozent auf den Mietpreis. Der Parameter `tage` ist eine ganze Zahl. Anforderung:

| Mietdauer in Tagen | Rabatt |
|---|---:|
| 1 bis 2 | 0 % |
| 3 bis 6 | 10 % |
| 7 und mehr | 20 % |
| kleiner als 1 | ungültig, die Funktion löst einen `ValueError` aus |

**a)** Bilden Sie Äquivalenzklassen für den Parameter `tage`. **6 Punkte**

| Nr. | Äquivalenzklasse (Bereich) | gültig / ungültig | Testwert |
|---:|---|---|---:|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

- Tabelle: *(4 Punkte, je Klasse 1 Punkt für die vollständig richtige Zeile mit Bereich, Einordnung und passendem Testwert)*
- Erklären Sie den Unterschied zwischen gültigen und ungültigen Äquivalenzklassen. *(1 Punkt)*
- Welchen Vorteil hat die Bildung von Äquivalenzklassen beim Testen? *(1 Punkt)*

**b)** Führen Sie eine Grenzwertanalyse durch: Geben Sie für jede der drei Grenzen zwischen den Klassen die beiden Werte unmittelbar unterhalb und oberhalb der Grenze als Testfälle an (insgesamt sechs Testfälle) und tragen Sie das erwartete Ergebnis ein. **6 Punkte**

| Testfall | Eingabe `tage` | erwartetes Ergebnis |
|---:|---:|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |

**c)** **4 Punkte**

- ca) Erklären Sie den Unterschied zwischen einem Black-Box-Test und einem White-Box-Test. *(2 Punkte)*
- cb) Welche Testart wenden Sie in den Aufgaben a) und b) an? *(1 Punkt)*
- cc) Was ist ein Modultest (Unit-Test)? *(1 Punkt)*

**d)** Ergänzen Sie den automatisierten Test. Erklären Sie außerdem, warum hinter dem Aufruf `rabatt(0)` die Zeile `assert False` steht. **5 Punkte**

```python
def test_rabatt():
    assert rabatt(2) == (1) ____
    assert rabatt(3) == (2) ____
    assert rabatt(7) == (3) ____
    # ungültiger Wert muss einen ValueError auslösen
    try:
        rabatt(0)
        assert False
    except ValueError:
        pass
```

- Fehlende Werte (1) bis (3): *(3 Punkte)*
- Erklärung zu `assert False`: *(2 Punkte)*

**e)** Ein Kollege hat die Funktion wie folgt umgesetzt. **4 Punkte**

```python
def rabatt(tage):
    if tage < 1:
        raise ValueError("ungültige Tage")
    if tage >= 6:
        return 20
    elif tage >= 3:
        return 10
    return 0
```

- ea) Welcher Ihrer Testfälle aus Aufgabe b) schlägt fehl? Nennen Sie erwartetes und tatsächliches Ergebnis. *(2 Punkte)*
- eb) Nennen Sie die Ursache und die Korrektur. *(2 Punkte)*

---

## 4. Aufgabe (25 Punkte)

Die Daten des Verleihs liegen in drei Tabellen. Primärschlüssel sind mit (PK) gekennzeichnet.

- **kunde** (kundennr (PK), name, ort, stammkunde)
- **rad** (radnr (PK), typ, tagespreis)
- **ausleihe** (ausleihnr (PK), kundennr, radnr, ausleihdatum, tage) mit den Fremdschlüsseln `kundennr` → kunde und `radnr` → rad

Auszug aus den Daten:

| kundennr | name | ort | stammkunde |
|---:|---|---|---:|
| 1 | Hansen | Kiel | 1 |
| 2 | Petersen | Flensburg | 0 |
| 3 | Ahlers | Kiel | 1 |
| 4 | Brandt | Lübeck | 0 |
| 5 | Clausen | Kiel | 0 |

| radnr | typ | tagespreis |
|---:|---|---:|
| 101 | Citybike | 12,00 |
| 105 | E-Bike | 28,50 |
| 110 | Mountainbike | 18,00 |
| 118 | E-Bike | 30,00 |
| 123 | Citybike | 11,50 |

| ausleihnr | kundennr | radnr | ausleihdatum | tage |
|---:|---:|---:|---|---:|
| 1 | 1 | 105 | 2026-06-02 | 3 |
| 2 | 3 | 101 | 2026-06-05 | 2 |
| 3 | 1 | 118 | 2026-06-10 | 7 |
| 4 | 2 | 110 | 2026-06-11 | 1 |
| 5 | 3 | 105 | 2026-06-14 | 4 |
| 6 | 5 | 101 | 2026-06-20 | 5 |

Formulieren Sie die folgenden SQL-Anweisungen.

**a)** Alle Fahrräder vom Typ „E-Bike“ mit einem Tagespreis von mehr als 29 EUR. **2 Punkte**

**b)** Name und Ort aller Kunden aus Kiel, alphabetisch nach dem Namen sortiert. **3 Punkte**

**c)** Für jede Ausleihe der Name des Kunden, der Typ des Fahrrads, die Anzahl der Tage und die Kosten (Tage mal Tagespreis, als Spalte `kosten`). **5 Punkte**

**d)** Der Name jedes Kunden mit der Summe seiner Ausleihtage (Spalte `gesamttage`), aber nur für Kunden mit mehr als 5 Tagen insgesamt. Sortieren Sie absteigend nach `gesamttage`. **6 Punkte**

**e)** Die Namen aller Kunden, die noch nie ein Fahrrad ausgeliehen haben. **4 Punkte**

**f)** **5 Punkte**

- fa) Der Tagespreis aller E-Bikes soll um 10 % erhöht werden. *(3 Punkte)*
- fb) Ein neuer Kunde soll angelegt werden: Kundennummer 6, Name Dietz, Ort Kiel, kein Stammkunde. *(2 Punkte)*

---

## Punkteübersicht

| Aufgabe | Thema | Punkte |
|---|---|---:|
| 1 | Programmcode interpretieren und erstellen | 25 |
| 2 | Algorithmen in Programmierlogik übertragen und darstellen | 25 |
| 3 | Testszenarien und Testdaten | 25 |
| 4 | Datenabfragen mit SQL | 25 |
| | **Gesamt** | **100** |

*Lösungen siehe separates Lösungsblatt.*