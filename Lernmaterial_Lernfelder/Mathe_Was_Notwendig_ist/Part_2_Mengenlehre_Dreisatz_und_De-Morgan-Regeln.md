# Mengenlehre, Dreisatz & De-Morgan-Regeln

> **Zielgruppe:** Umschüler FIAE/FISI, 2./3. Lehrjahr
> **Prüfungsrelevanz:** Kein eigenständiger AP2-Prüfungsbereich und kein isoliertes Schwerpunktthema – das bedeutet **nicht**, dass die Inhalte nicht drankommen können. Sie sind **Grundlagenwerkzeug**, das innerhalb prüfungsrelevanter Aufgaben gebraucht wird: Mengenlehre/Relationen v. a. für SQL/Datenbanken (§14 FIAusbV verlangt für FIAE ausdrücklich das Erstellen von "Abfragen zur Gewinnung und Manipulation von Daten" – damit direkter nutzbar als für FISI, wo es eher allgemeines mathematisch-logisches Werkzeug ist), Dreisatz/kaufmännisches Rechnen für Wirtschafts- und Sozialkunde, De-Morgan-Regeln als Ergänzung zur Booleschen Logik (vgl. LF2.1). Bewusst **kompakt** gehalten, kein eigenständiges Prüfungs-Epic.
> **Lernzeit:** 45–60 Min.
> **Status:** Final
> **Stand:** 2026-09-15

**Legende (redaktionelle Einschätzung, keine offizielle IHK-Gewichtung):** 🔴 unmittelbar auf typische Prüfungsaufgaben anwendbar · 🟡 wichtiges Verständnis-/Transferwissen · 🟢 vertiefendes Kontextwissen

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was sind die grundlegenden Mengenoperationen, und welche SQL-Konstrukte lassen sich sinnvoll damit in Beziehung setzen? | [1](#1-mengenlehre--relationen) |
| 2 | Wie unterscheiden sich einfacher und zusammengesetzter Dreisatz, und wann wird welcher gebraucht? | [2](#2-dreisatz--kaufmännisches-rechnen) |
| 3 | Was besagen die De-Morgan-Regeln, und wofür werden sie in der Praxis genutzt? | [3](#3-de-morgan-regeln) |

---

## 1. Mengenlehre & Relationen

> **Grundprinzip:** Relationale Datenbanken beruhen auf Konzepten der Mengenlehre. Eine sauber strukturierte Tabelle mit Kundendaten kann näherungsweise als Sammlung gleichartig aufgebauter Datensätze betrachtet werden, und jede Abfrage, die nur bestimmte Zeilen herausfiltert oder zwei Tabellen verknüpft, ist im Kern eine Mengenoperation. Wer die Grundbegriffe der Mengenlehre kennt, versteht SQL nicht nur syntaktisch, sondern auch inhaltlich – auch wenn SQL, wie im nächsten Abschnitt sichtbar wird, an einigen Stellen vom strengen mathematischen Mengenbegriff abweicht.

### 1.1 Grundlegende Mengenoperationen

| Operation | Notation | Bedeutung | SQL-Bezug |
|---|---|---|---|
| Menge | `{...}` | Eine Zusammenfassung unterscheidbarer Objekte (Elemente) ohne Wiederholung und ohne feste Reihenfolge | Eine Relation ist im mathematischen Sinn duplikatfrei; eine SQL-Tabelle ohne Primärschlüssel/Unique-Constraint kann dagegen Duplikate enthalten, und auch Abfrageergebnisse können welche liefern – SQL folgt damit oft einer Multimengenlogik. `DISTINCT` entfernt doppelte Ergebniszeilen |
| Teilmenge | `⊆` | Alle Elemente von A sind auch in B enthalten | Eine `WHERE`-Bedingung wählt aus einer Tabelle die Zeilen aus, die die Bedingung erfüllen (relationale Algebra: **Selektion**) |
| Schnittmenge | `∩` | Elemente, die in A **und** B vorkommen | Direkt: `INTERSECT`. Ein `INNER JOIN` erzeugt einen ähnlichen "nur passende Datensätze"-Effekt, ist aber **keine reine Mengen-Schnittmenge** (siehe Hinweis unten) |
| Vereinigungsmenge | `∪` | Elemente, die in A **oder** B (oder beiden) vorkommen | `UNION` (entfernt Duplikate) bzw. `UNION ALL` (behält Duplikate) – beide benötigen kompatible Spaltenanzahl/-typen in beiden Abfragen |
| Differenzmenge | `\` | Elemente, die in A, aber nicht in B vorkommen | `EXCEPT` (mengentheoretisch sauber) oder `NOT EXISTS`; `NOT IN` liefert bei `NULL`-Werten im Vergleichsergebnis leicht unerwartete Ergebnisse und ist deshalb mit Vorsicht zu verwenden |
| Kartesisches Produkt | `×` | Alle möglichen Kombinationen von Elementen aus A und B | `CROSS JOIN` bildet es direkt; theoretisch lässt sich auch ein bedingter `JOIN` als gefiltertes kartesisches Produkt verstehen (siehe Hinweis unten) |

> **Wichtig für die Prüfung:** `INNER JOIN` und Schnittmenge werden oft gleichgesetzt – das ist zu ungenau. `INTERSECT` entspricht einer echten Mengen-Schnittmenge zwischen zwei **kompatiblen** Abfrageergebnissen. Ein `INNER JOIN` dagegen kombiniert Tupel anhand einer Verknüpfungsbedingung und kann dabei **mehrere Ergebniszeilen pro Datensatz** erzeugen (z. B. wenn ein Kunde mehrere Bestellungen hat) – das ist bei einer klassischen Schnittmenge nicht der Fall. 🔴

> **Wichtig für die Prüfung (theoretisches Modell):** Man kann einen **`INNER JOIN`** (bzw. jeden bedingten JOIN) **konzeptionell** als kartesisches Produkt verstehen, das anschließend gefiltert wird – erst alle möglichen Kombinationen, dann nur die Zeilen, die die Verknüpfungsbedingung erfüllen. Das hilft, JOIN-Ergebnisse nachzuvollziehen. Diese Betrachtung passt nicht auf jeden JOIN-Typ: Ein `LEFT JOIN` behält zusätzlich auch die nicht passenden linken Datensätze, ist also kein reines "Produkt + Filter". Ein reales Datenbanksystem führt das intern zudem nicht zwingend in dieser Reihenfolge aus (Optimierer nutzen z. B. Index-Nested-Loop- oder Hash-Join-Verfahren, ohne das volle Kreuzprodukt zu bilden) – die Betrachtung ist ein Denkmodell, kein tatsächlicher Ausführungsplan. 🟡

### 1.2 Relation, Tupel, Attribut

Eine **Relation** ist in der relationalen Datenbanktheorie eine Menge gleichartig strukturierter **Tupel** (Datensätze/Zeilen). Ein Tupel ordnet jedem **Attribut** (der benannten Spalte) einen konkreten **Attributwert** zu. Näherungsweise auf eine Datenbanktabelle übertragen: Relation → Tabelle, Tupel → Zeile, Attribut → Spalte, Attributwert → einzelner Zellenwert. Eine Relation ist im strengen mathematischen Sinn duplikatfrei; eine reale SQL-Tabelle kann dagegen Duplikate enthalten und ist damit genau genommen eine Multimenge (Bag), keine Menge.

🟢 **Nice to know:** Der Name "relationale Datenbank" kommt direkt von diesem mathematischen Relationsbegriff, nicht von "Beziehungen zwischen Tabellen" (Fremdschlüssel-Beziehungen), wie man aus dem Alltagswort "Relation" vermuten könnte.

> **IHK-Typfrage:** *"Zwei Tabellen 'Kunden' und 'Bestellungen' sollen so verknüpft werden, dass nur Kunden erscheinen, die tatsächlich mindestens eine Bestellung getätigt haben. Welcher SQL-Befehl setzt das um, und was ist dabei zu beachten?"*
> **Musterantwort:** Das wird typischerweise über einen `INNER JOIN` zwischen beiden Tabellen anhand der Kunden-ID umgesetzt – dieser liefert nur die Zeilen, bei denen eine Übereinstimmung in beiden Tabellen existiert. Zu beachten: Hat ein Kunde mehrere Bestellungen, erscheint dieser Kunde im Ergebnis **mehrfach** (einmal pro Bestellung) – der JOIN liefert keine eindeutige Kundenliste. Soll jeder Kunde nur einmal erscheinen, ist ein Ansatz mit `EXISTS` passender: `SELECT * FROM Kunden k WHERE EXISTS (SELECT 1 FROM Bestellungen b WHERE b.KundenID = k.KundenID)`.

---

## 2. Dreisatz & kaufmännisches Rechnen

> **Grundprinzip:** Wenn 3 Server-Instanzen 300 Anfragen pro Sekunde verarbeiten, wie viele Instanzen braucht man für 500 Anfragen pro Sekunde? Genau solche Verhältnisrechnungen – ob bei Kapazitätsplanung, Rabatten oder Stundensätzen – sind der Alltagskern des Dreisatzes.

Ein Dreisatz ist **einfach**, wenn nur zwei Größen miteinander verknüpft sind – er kann dabei proportional oder antiproportional sein (das ist eine andere Unterscheidung, siehe 2.1/2.2). Wirken mehrere Einflussgrößen gleichzeitig, spricht man von einem **zusammengesetzten** Dreisatz (2.3).

### 2.1 Einfacher Dreisatz: proportional

Bei **proportionalem** Zusammenhang steigt eine Größe im gleichen Verhältnis wie die andere.

```text
3 Server-Instanzen  → 300 Anfragen/Sekunde
1 Server-Instanz    → 100 Anfragen/Sekunde   (÷ 3)
5 Server-Instanzen  → 500 Anfragen/Sekunde   (× 5)
```

### 2.2 Einfacher Dreisatz: antiproportional

Bei **antiproportionalem** Zusammenhang sinkt eine Größe, wenn die andere steigt (und umgekehrt) – typisch bei "je mehr, desto weniger Zeit".

```text
2 Techniker  → 8 Stunden für ein Rollout
1 Techniker  → 16 Stunden für dasselbe Rollout   (× 2)
4 Techniker  → 4 Stunden für dasselbe Rollout    (÷ 2)
```

🟡 **Modellannahme:** Die Rechnung setzt voraus, dass sich die Arbeit vollständig gleichmäßig aufteilen lässt und zusätzliches Personal keinen Koordinationsaufwand verursacht. In der Praxis gilt "doppelte Mitarbeiterzahl = halbe Zeit" deshalb nur näherungsweise – nicht jede Aufgabe lässt sich beliebig parallelisieren.

> **Wichtig für die Prüfung:** Der häufigste Fehler ist, einen antiproportionalen Zusammenhang wie einen proportionalen zu rechnen (oder umgekehrt). Vor dem Rechnen immer prüfen: Wird die gesuchte Größe **größer**, wenn die gegebene Größe größer wird (proportional) – oder **kleiner** (antiproportional)? 🔴

### 2.3 Zusammengesetzter Dreisatz

Hängt das Ergebnis von **mehreren** Einflussgrößen gleichzeitig ab, wird für jede Größe einzeln geprüft, ob sie proportional oder antiproportional wirkt – das ist eine andere Unterscheidung als proportional/antiproportional selbst (die beschreibt die Richtung, "zusammengesetzt" beschreibt die Anzahl der beteiligten Größen).

**Beispiel:** 4 Server verarbeiten in 2 Minuten 8.000 Anfragen. Wie viele Anfragen verarbeiten 6 Server in 5 Minuten?

- Mehr Server → mehr Anfragen: **proportional**
- Mehr Zeit → mehr Anfragen: **proportional**

```text
8.000 × (6 ÷ 4) × (5 ÷ 2) = 30.000
```

**Ergebnis:** 6 Server verarbeiten unter diesen Modellannahmen in 5 Minuten 30.000 Anfragen.

> **Wichtig für die Prüfung:** Beim zusammengesetzten Dreisatz jede Einflussgröße **einzeln** auf proportional/antiproportional prüfen, bevor gerechnet wird – nicht pauschal für die ganze Aufgabe. 🔴

### 2.4 Prozentrechnung

| Formel | Zweck |
|---|---|
| Prozentwert = Grundwert × Prozentsatz ÷ 100 | z. B. Rabatt in Euro berechnen |
| Grundwert = Prozentwert × 100 ÷ Prozentsatz | z. B. Ursprungspreis aus Rabattbetrag rückrechnen |
| Prozentsatz = Prozentwert × 100 ÷ Grundwert | z. B. welcher Rabatt-% wurde gewährt |

**Beispiel:** Eine Softwarelizenz kostet ursprünglich 800 €, nach Rabatt nur noch 680 €. Prozentsatz = (800 − 680) × 100 ÷ 800 = 15 % Rabatt.

### 2.5 Kalkulation (kaufmännisches Rechnen) – Kurzüberblick

🟡 **Nur als Kontext, ausführlich im WiSo-Material behandelt:**

| Begriff | Bedeutung | Bezugsgröße |
|---|---|---|
| Kalkulationszuschlag | Prozentualer Aufschlag zur Deckung von Kosten und Gewinn | **Einkaufspreis** |
| Handelsspanne | Prozentuale Differenz zwischen Verkaufs- und Einkaufspreis | **Verkaufspreis** |
| Deckungsbeitrag | Verkaufserlös abzüglich variabler Kosten | – |

> **Wichtig für die Prüfung:** Kalkulationszuschlag und Handelsspanne beziehen sich auf **unterschiedliche Bezugsgrößen** (Einkaufs- vs. Verkaufspreis) – eine klassische Verwechslungsfalle. Der Deckungsbeitrag eines einzelnen Verkaufs ist außerdem **nicht automatisch Gewinn**: Erst die Summe aller Deckungsbeiträge deckt zunächst die Fixkosten; nur der darüber hinausgehende Betrag ist tatsächlich Gewinn. 🔴

> **IHK-Typfrage:** *"Eine Serverkapazität von 4 Instanzen verarbeitet 800 Anfragen pro Minute gleichmäßig verteilt. Wie viele Instanzen werden für 1.000 Anfragen pro Minute benötigt?"*
> **Musterantwort:** Es handelt sich um einen **proportionalen** Zusammenhang (mehr Anfragen benötigen mehr Instanzen). 4 Instanzen → 800 Anfragen, also 1 Instanz → 200 Anfragen (800 ÷ 4). Für 1.000 Anfragen werden somit 1.000 ÷ 200 = **5 Instanzen** benötigt. Ergibt die Rechnung einen nicht ganzzahligen Wert (z. B. 5,5), muss bei unteilbaren Ressourcen wie Serverinstanzen auf die nächste **vollständige** Einheit aufgerundet werden.

---

## 3. De-Morgan-Regeln

> **Grundprinzip:** "Nicht (Regen UND Wind)" bedeutet dasselbe wie "Kein Regen ODER kein Wind" – diese Art der Umformung negierter logischer Verknüpfungen ist genau das, was die De-Morgan-Regeln formalisieren. Direkter Anknüpfungspunkt an die Boolesche Algebra aus **LF2.1 – Die Logik der Maschinen**.

### 3.1 Die beiden Regeln

| Regel | Formal | In Worten |
|---|---|---|
| 1. De-Morgan-Regel | `NICHT (A UND B)` = `(NICHT A) ODER (NICHT B)` | Die Negation einer UND-Verknüpfung ist die ODER-Verknüpfung der Einzelnegationen |
| 2. De-Morgan-Regel | `NICHT (A ODER B)` = `(NICHT A) UND (NICHT B)` | Die Negation einer ODER-Verknüpfung ist die UND-Verknüpfung der Einzelnegationen |

**Merkregel:** Beim "Durchschieben" der Negation durch die Klammer kippt UND zu ODER und umgekehrt.

### 3.2 Praktische Anwendung: Bedingungen umformen

```text
Ursprüngliche Bedingung:
WENN NICHT (Nutzer.istAdmin UND Nutzer.istAktiv)
    DANN Zugriff verweigern

Nach De-Morgan äquivalent umgeformt:
WENN (NICHT Nutzer.istAdmin) ODER (NICHT Nutzer.istAktiv)
    DANN Zugriff verweigern
```

Beide Varianten sind logisch **exakt äquivalent**. Welche Schreibweise im konkreten Fall besser lesbar ist, hängt vom Kontext ab – für manche ist eine Formulierung ohne äußere Verneinung eingängiger, für andere nicht.

> **Wichtig für die Prüfung:** Ein häufiger Fehler ist, beim Auflösen der Klammer den Verknüpfungsoperator **nicht** zu wechseln (also UND bleibt UND) – das Ergebnis ist dann logisch falsch, nicht nur unschön formuliert. Die Regel "Negation durchschieben = Operator kippt" muss beide Male angewendet werden: auf jedes einzelne Element **und** auf den Verknüpfungsoperator dazwischen. 🔴

> **IHK-Typfrage:** *"Formen Sie die Bedingung `NICHT (Bestellung.istBezahlt ODER Bestellung.istStorniert)` mithilfe der De-Morgan-Regel in eine Form ohne äußere Verneinung um."*
> **Musterantwort:** Nach der zweiten De-Morgan-Regel wird aus `NICHT (A ODER B)` die Form `(NICHT A) UND (NICHT B)`. Angewendet: `(NICHT Bestellung.istBezahlt) UND (NICHT Bestellung.istStorniert)` – die Bedingung ist nur dann wahr, wenn die Bestellung weder bezahlt noch storniert ist.

---

## 4. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
|---|---|---|
| 1 | `INNER JOIN` und Schnittmenge sind dasselbe | `INTERSECT` entspricht einer echten Mengen-Schnittmenge; `INNER JOIN` verknüpft Tupel anhand einer Bedingung und kann pro Datensatz mehrere Treffer erzeugen |
| 2 | Proportionaler und antiproportionaler Dreisatz werden gleich gerechnet | Bei proportionalem Zusammenhang bleibt der Quotient konstant, bei antiproportionalem das Produkt beider Größen |
| 3 | Beim Auflösen von De-Morgan bleibt der Verknüpfungsoperator unverändert | UND kippt zu ODER und umgekehrt – sonst ist das Ergebnis logisch falsch |
| 4 | "Relation" bedeutet in der Datenbanktheorie eine Beziehung zwischen Tabellen | Der Fachbegriff "Relation" bezeichnet mathematisch die Tabelle selbst (Menge von Tupeln), nicht eine Fremdschlüssel-Beziehung |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Menge | Zusammenfassung unterscheidbarer Elemente ohne Wiederholung/feste Reihenfolge |
| Schnittmenge / Vereinigung / Differenz | Elemente in A und B / in A oder B / in A ohne B |
| Kartesisches Produkt | Alle Kombinationen zweier Mengen – direkt via `CROSS JOIN`, theoretische Grundlage eines gefilterten JOINs |
| INNER JOIN ≠ Schnittmenge | JOIN verknüpft nach Bedingung und kann mehrere Treffer erzeugen; `INTERSECT` ist die echte Mengen-Schnittmenge |
| Relation/Tupel/Attribut | Tabelle/Zeile/Spalte in der relationalen Datenbanktheorie |
| Proportionaler Dreisatz | Größen steigen/fallen im gleichen Verhältnis |
| Antiproportionaler Dreisatz | Größen verhalten sich gegenläufig (mehr Techniker → weniger Zeit) |
| Zusammengesetzter Dreisatz | Mehrere Einflussgrößen gleichzeitig – jede Größe einzeln auf proportional/antiproportional prüfen |
| De-Morgan-Regel 1 | `NICHT(A UND B)` = `(NICHT A) ODER (NICHT B)` |
| De-Morgan-Regel 2 | `NICHT(A ODER B)` = `(NICHT A) UND (NICHT B)` |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|---|---|---|
| Mengenoperation zu SQL zuordnen | "Welches SQL-Konstrukt lässt sich sinnvoll mit dieser Mengenoperation in Beziehung setzen?" | Den Bezug herstellen, ohne eine strikte 1:1-Gleichsetzung zu behaupten (z. B. INNER JOIN ist keine reine Schnittmenge) |
| Dreisatz lösen | "Wie viele X werden für Y benötigt?" | Erst proportional/antiproportional bestimmen, dann rechnen – nicht umgekehrt |
| De-Morgan anwenden | "Formen Sie die Bedingung um..." | Operator UND↔ODER korrekt kippen, nicht nur die Einzelelemente negieren |

---

## Merk-Sätze fürs Fachgespräch

> Konzeptionell lässt sich ein `INNER JOIN` als gefiltertes kartesisches Produkt verstehen – real optimieren Datenbanksysteme das, ohne das volle Kreuzprodukt tatsächlich zu bilden.

> Vor dem Dreisatz-Rechnen erst die Richtung klären: mehr wovon führt zu mehr oder weniger wovon?

> Bei De-Morgan kippt beim Durchschieben der Negation nicht nur das Vorzeichen jedes Elements, sondern auch der Operator dazwischen.

---

```yaml
dokument: Mengenlehre-Dreisatz-DeMorgan-wiki-artikel
lernfeld: "Priorität-2-Themen aus Mathe-Prioritätenplan (Part 2 der Serie 'Mathe_Was_Notwendig_ist')"
titel: "Mengenlehre, Dreisatz & De-Morgan-Regeln"
typ: "Typ A – Kompakter Prüfungs-Wiki (FIAE/FISI-übergreifend)"
status: final
stand: 2026-09-15
quellen_intern:
  - "Priorität-2-Themen aus dem in vorheriger Session erarbeiteten Mathe-Prioritätenplan: bewusst kompakt statt als eigenständiges Prüfungs-Epic, da kein eigenständiger AP2-Prüfungsbereich und kein isoliertes Schwerpunktthema besteht - die Inhalte können aber als Grundlagenwerkzeug innerhalb prüfungsrelevanter Aufgaben vorkommen (SQL vgl. SQL-Ordner, Boolesche Logik vgl. LF2.1 - Die Logik der Maschinen)"
  - "Teil 1 der Serie: Pseudocode & Algorithmenstrukturen (bereits final, Mathe_Was_Notwendig_ist/Part_1)"
  - "Bewusst FIAE/FISI-übergreifend verfasst, da Mengenlehre/SQL-Bezug und kaufmännisches Rechnen für beide Fachrichtungen relevant sind, anders als der stärker FIAE-fokussierte Teil 1"
quellen_fachlich:
  - titel: "Grundlagen der Mengenlehre, relationalen Algebra, Verhältnisrechnung und Booleschen Algebra (De-Morgan-Regeln)"
    herausgeber: "Mathematisches und informatisches Standardwissen"
    status: "Die mathematischen Konzepte selbst sind stabil und unstrittig. Aussagen zu SQL-Entsprechungen (INNER JOIN vs. INTERSECT, NOT IN/NULL-Problematik, UNION/UNION ALL) wurden in Runde 2 nach externem Review präzisiert, um keine zu enge 1:1-Gleichsetzung zwischen Mengenoperation und SQL-Befehl zu suggerieren"
  - titel: "Fachinformatiker-Ausbildungsverordnung (FIAusbV), §14 (FIAE) und §21/§24 (FISI)"
    herausgeber: "Bundesministerium der Justiz (gesetze-im-internet.de)"
    status: "Web-verifiziert am 2026-09-15: §14 Abs. 1 Nr. 4 FIAusbV verlangt für FIAE das Erstellen von 'Abfragen zur Gewinnung und Manipulation von Daten' - daraus ergibt sich ein direkterer Bezug zu Datenbankabfragen als in den ausdrücklich genannten FISI-AP2-Kompetenzen (§21/§24)"
review_historie:
  - runde: 1
    datum: 2026-09-15
    ergebnis: "Erstdraft erstellt basierend auf dem in vorheriger Session erarbeiteten Mathe-Prioritätenplan (Priorität-2-Themen). Bewusst kompakter gehalten als Teil 1 (Pseudocode), da diese Themen laut Plan explizit 'kein eigenes Epic' sein sollten. SQL-Bezüge (JOIN als Mengenoperation) bewusst eingebaut, um die Grundlagenfunktion für den bestehenden SQL-Ordner sichtbar zu machen statt die Mengenlehre isoliert zu behandeln. Kein Rohmaterial vorhanden - aus eigenem Wissen erstellt."
  - runde: 2
    datum: 2026-09-15
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (alle 3 Reviews übereinstimmend): INNER JOIN wurde fälschlich mit Schnittmenge gleichgesetzt - tatsächlich erzeugt ein JOIN Kombinationen nach Bedingung und kann pro Datensatz mehrere Treffer liefern (z.B. Kunde mit mehreren Bestellungen), während INTERSECT die echte Mengen-Schnittmenge ist. Tabelle, Wichtig-Block, Musterantwort und Prüfungsfalle 1 entsprechend korrigiert. 'JOIN = kartesisches Produkt + Filter' als bewusst theoretisches Denkmodell gekennzeichnet, nicht als realer DBMS-Ausführungsplan (Optimierer nutzen Index-Nested-Loop/Hash-Join, materialisieren nicht das volle Kreuzprodukt). NOT IN/NULL-Problematik und EXCEPT-Präzisierung ergänzt, CROSS JOIN explizit benannt. Tupel/Attribut/Attributwert-Begriffe präzisiert (Tupel enthält Attributwerte, nicht Attribute), SQL-Tabelle als Multimenge statt uneingeschränkt als Menge dargestellt. Echte inhaltliche Lücke geschlossen (1 Review, gut begründet): Kernfrage 2 versprach 'einfacher vs. zusammengesetzter Dreisatz', der Artikel behandelte aber nur proportional/antiproportional (andere Unterscheidungsachse) - neuer kompakter Abschnitt 2.3 zum zusammengesetzten Dreisatz ergänzt, dafür Kalkulationsabschnitt gestrafft (passend zur eigenen 'bewusst kompakt'-Prämisse). Kalkulationszuschlag/Handelsspanne um unterschiedliche Bezugsgrößen ergänzt (Einkaufs- vs. Verkaufspreis - klassische Verwechslungsfalle), Deckungsbeitrag präzisiert (Summe deckt zuerst Fixkosten, nicht automatisch Gewinn). Antiproportionales Beispiel um Modellannahme ergänzt (ideale Parallelisierbarkeit). De-Morgan-Lesbarkeits-Werturteil neutralisiert. Prüfungsrelevanz-Kopfzeile präzisiert, damit 'kein eigener Prüfungsbereich' nicht als 'nicht prüfbar' missverstanden wird, inkl. FIAE/FISI-Differenzierung. Legende als redaktionelle Priorisierung statt Prüfungsgarantie gekennzeichnet."
  - runde: 3
    datum: 2026-09-15
    ergebnis: "3 weitere Reviews eingearbeitet (überwiegend Bestätigung von Runde 2, wenige verbleibende Punkte). Wichtigster Fund (2 Reviews): Das 'JOIN als kartesisches Produkt + Filter'-Denkmodell war auf JOIN allgemein formuliert, gilt aber nicht für LEFT JOIN (behält zusätzlich unpassende linke Datensätze) - auf INNER JOIN/bedingten JOIN präzisiert, in Wichtig-Block UND im bisher übersehenen Merksatz (der noch die alte, uneingeschränkte Formulierung trug und damit der sorgfältigen Relativierung im Haupttext widersprach). Excel-Tabelle=Menge-Aussage im Grundprinzip entschärft, da sie der später im selben Abschnitt eingeführten Multimengen-Einschränkung direkt widersprach. Menge-Zeile in der Tabelle präzisiert (Duplikate können auch in Basistabellen ohne Constraints auftreten, nicht nur in Abfrageergebnissen). Cheatsheet um 'Zusammengesetzter Dreisatz' ergänzt - fehlte dort, obwohl die Kernfrage und Abschnitt 2.3 es explizit behandeln (derselbe Selbstkonsistenz-Fehlertyp wie in den vorherigen Artikeln dieser Serie). Dreisatz-Gliederung klargestellt: 'einfacher Dreisatz' bezeichnet die Anzahl der Größen (zwei), nicht die Richtung - vorher implizierten die Überschriften 'einfach=proportional'. Antiproportional-Prüfungsfalle mathematisch präzisiert (Produkt bleibt konstant statt vager 'Rechenrichtung kehrt sich um'). §14-Zitat näher am Verordnungswortlaut ('Abfragen zur Gewinnung und Manipulation von Daten' statt pauschal 'Datenabfragen'), YAML entsprechend nachgezogen. Ein Vorschlag (YAML-Review-Historie kürzen) geprüft, aber verworfen - entspricht dem projektweiten Format aller anderen fertigen Wiki-Artikel dieser Sammlung, Änderung nur hier hätte Inkonsistenz geschaffen. Erneut fälschlich behauptete Claude-Chat-Links in einer Review - beim Abgleich wie in den vorherigen Artikeln dieser Serie nicht bestätigt."
  - runde: 4
    datum: 2026-09-15
    ergebnis: "Eigene Abschlussprüfung: Gesamtes Dokument durchgelesen, keine weiteren Selbstkonsistenz-Fehler gefunden. Kalkulationszuschlag-Bezugsgröße bewusst bei 'Einkaufspreis' belassen (eine Review schlug 'Bezugs-/Einstandspreis' vor - für diesen kompakten Artikel als unnötige Verkomplizierung bewertet, da das WiSo-Material die ausführliche Behandlung übernimmt)."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-15) – Freigabe durch Autor:in bestätigt. Part 2 der Serie Mathe_Was_Notwendig_ist."
```