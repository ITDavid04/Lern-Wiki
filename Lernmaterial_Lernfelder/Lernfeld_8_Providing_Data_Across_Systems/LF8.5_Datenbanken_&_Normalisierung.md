# LF8.5 – Datenbanken & Normalisierung

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 110–140 Minuten reines Lesen, +90–120 Minuten mit Aufgaben (insbesondere Normalisierung auf Papier) – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wann wählt man ein relationales oder ein NoSQL-Datenbanksystem, und welche Rolle spielen dabei Transaktionssicherheit, Konsistenz und Skalierbarkeit? Wie werden Kardinalitäten physisch abgebildet? | [→ 1. Datenmodell-Wahl](#1-datenmodell-wahl-und-relationales-schema-design) |
| 2 | Wie normalisiert man ein Schema Schritt für Schritt von 0NF bis 3NF, und welche Anomalien werden dadurch verhindert? | [→ 2. Normalisierung](#2-normalisierung-von-0nf-bis-3nf) |
| 3 | Wie funktionieren mehrfache Joins, `GROUP BY`/`HAVING` und Subqueries mit `IN`/`EXISTS` in PostgreSQL? | [→ 3. Erweiterte SQL-Abfragen](#3-erweiterte-sql-abfragen-und-aggregationen) |
| 4 | Wie schützen Views und rollenbasierte Rechtevergabe (RBAC) eine Datenbank nach dem Prinzip der minimalen Rechtevergabe? | [→ 4. Views & Rechteverwaltung](#4-views-und-rechteverwaltung-rbac) |
| 5 | Welche NoSQL-Kategorien gibt es, und wie unterscheiden sich die vier DBaaS-Betriebsmodelle in der Cloud? | [→ 5. NoSQL & Cloud-Datenbanken](#5-nosql-datenbanken-und-cloud-datenbanken-dbaas) |

---

## 1. Datenmodell-Wahl und relationales Schema-Design

> **Grundprinzip:** Eine relationale Datenbank ist wie eine Werkstatt mit fest beschrifteten Schubladen – jedes Teil hat seinen festen Platz, dafür findet man es garantiert wieder. Eine NoSQL-Datenbank ist wie eine flexible Werkzeugkiste, in der auch mal ein neues, unerwartetes Werkzeug ohne Umbau Platz findet.

### 1.1 Relationale vs. nicht-relationale Datenbanken

| Modell | Struktur | Transaktionsmodell | IHK-Relevanz |
| --- | --- | --- | --- |
| **Relational (RDBMS)** | Feste, zweidimensionale Tabellen mit Zeilen/Spalten, Beziehungen über Primär-/Fremdschlüssel | Häufig starke Transaktionsunterstützung nach **ACID** (Atomicity, Consistency, Isolation, Durability) | 🔴 |
| **Nicht-relational (NoSQL)** | Flexible, schemaflexible Formate: Dokumente, Key-Value, Column-Family, Graph | Häufig **BASE**-Ansatz (Basically Available, Soft State, Eventually Consistent), Konsistenzmodell aber produktabhängig | 🔴 |

> **Wichtig:** "Relational" bedeutet nicht automatisch ACID, und "NoSQL" bedeutet nicht automatisch BASE. Viele NoSQL-Datenbanken unterstützen mittlerweile ACID-Transaktionen (z. B. innerhalb eines Dokuments), und relationale Systeme in verteilten Setups arbeiten teils mit Replikation und zeitweise veralteten Lesewerten. Die Zuordnung in der Tabelle beschreibt den **typischen**, nicht den zwingenden Fall – die konkrete Datenbank und ihre Konfiguration entscheiden.

**Wann welches Modell?** Relationale Datenbanken eignen sich, wenn Daten stark strukturiert sind und Transaktionssicherheit im Vordergrund steht (z. B. Finanzbuchungen). NoSQL eignet sich, wenn Daten semi-/unstrukturiert sind, sich das Schema häufig ändert oder horizontale Skalierbarkeit bei sehr hohem Datenvolumen wichtiger ist als sofortige Konsistenz. Beide Modelle schließen sich in der Praxis nicht aus – viele Systeme kombinieren beide (siehe Abschnitt 5).

### 1.2 ERM-zu-Tabellen-Mapping

Ein Entity-Relationship-Modell (ERM) wird nach einem standardisierten Verfahren in physische Tabellen überführt:

- **Entitäten** → **Tabellen**
- **Attribute** → **Spalten** mit konkretem Datentyp (`VARCHAR`, `INTEGER`, `TIMESTAMP`, …)
- **Beziehungen** werden je nach Kardinalität unterschiedlich abgebildet:

| Kardinalität | Umsetzung | IHK-Relevanz |
| --- | --- | --- |
| **1:1** | Primärschlüssel der einen Tabelle wird als Fremdschlüssel in die andere Tabelle übernommen und dort mit `UNIQUE` versehen (bei verpflichtender Teilnahme zusätzlich `NOT NULL`); alternativ können beide Tabellen zusammengelegt werden, wenn die Trennung keinen fachlichen Vorteil bringt | 🟡 |
| **1:n** | Primärschlüssel der "1"-Seite wird als Fremdschlüssel in die "n"-Seite übernommen | 🔴 |
| **m:n** | Neue **Verbindungstabelle (Junction Table)** mit je einem Fremdschlüssel auf beide beteiligten Tabellen – häufig bilden beide Fremdschlüssel gemeinsam den Primärschlüssel, alternativ ist ein Surrogatschlüssel mit `UNIQUE`-Bedingung auf beide Fremdschlüssel möglich | 🔴 |

> **IHK-Typfrage:** *"Warum kann eine m:n-Beziehung nicht direkt zwischen zwei Tabellen abgebildet werden, und wie löst eine Verbindungstabelle das Problem?"*
> **Musterantwort:** Eine Fremdschlüssel-Spalte kann nur einen einzigen Wert referenzieren – bei m:n müsste eine Tabelle aber mehrere Werte der anderen Seite gleichzeitig referenzieren, was das relationale Modell nicht direkt vorsieht. Eine Verbindungstabelle löst das, indem sie pro tatsächlich existierender Verknüpfung eine eigene Zeile mit beiden Fremdschlüsseln anlegt – so kann jede Kombination beliebig oft vorkommen, ohne dass eine der Ursprungstabellen mehrwertige Spalten benötigt.

### 1.3 Datenbank-Anomalien

Ein unnormalisiertes oder schlecht entworfenes Schema ist anfällig für drei Arten von Anomalien:

| Anomalie | Beschreibung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Einfügeanomalie (Insert)** | Ein neuer Datensatz kann nicht angelegt werden, weil eigentlich unabhängige Pflichtdaten fehlen | Ein neuer Kurs kann nicht erfasst werden, solange kein Student eingeschrieben ist | 🔴 |
| **Änderungsanomalie (Update)** | Redundante Daten werden an einer Stelle geändert, an anderen aber nicht – Inkonsistenz entsteht | Die Adresse eines Kunden wird in einem Datensatz aktualisiert, in einem anderen bleibt die alte stehen | 🔴 |
| **Löschanomalie (Delete)** | Das Löschen eines Datensatzes vernichtet unbeabsichtigt weitere, eigentlich unabhängige Informationen | Der letzte Student meldet sich vom Kurs ab – dabei verschwinden auch alle Informationen über den Kurs selbst | 🔴 |

---

## 2. Normalisierung von 0NF bis 3NF

> **Grundprinzip:** Normalisierung ist wie das Aufräumen eines Lagers, in dem bisher jede Palette einen eigenen, redundanten Aufkleber mit den vollständigen Produktstammdaten trägt – am Ende steht jede Information nur noch an einer einzigen Stelle, referenziert statt kopiert.

### 2.1 Ziel und Grenzen der Normalisierung

Normalisierung ist ein systematisches, mathematisch fundiertes Verfahren zur Umstrukturierung relationaler Schemata mit zwei Zielen: **Redundanz reduzieren** und **Konsistenz erhöhen**, indem Update-, Insert- und Delete-Anomalien beseitigt werden. In der Praxis wird meist bis zur **3. Normalform (3NF)** normalisiert – eine weitere Normalisierung (Boyce-Codd, 4NF, 5NF) ist selten nötig und kann zu **Übernormalisierung** führen: zu viele Tabellen-Joins verschlechtern dann die Abfrageperformance.

### 2.2 Schritt für Schritt: 0NF → 1NF → 2NF → 3NF

```text
[ UNF/0NF: Unnormalisierte Ausgangsdaten – ggf. mit Wiederholungsgruppen
  oder mehrwertigen Attributen ]
       |  (mehrwertige Felder/Wiederholungsgruppen auflösen)
       v
[ 1NF: Nur noch atomare Spaltenwerte, keine Wiederholungsgruppen ]
       |  (partielle Abhängigkeiten von zusammengesetzten Schlüsseln entfernen)
       v
[ 2NF: Jedes Nicht-Schlüssel-Attribut hängt vom GESAMTEN Schlüssel ab ]
       |  (transitive Abhängigkeiten zwischen Nicht-Schlüssel-Spalten entfernen)
       v
[ 3NF: Keine transitiven Abhängigkeiten mehr – bereinigt ]
```

| Normalform | Anforderung | Typische Aktion | IHK-Relevanz |
| --- | --- | --- | --- |
| **1NF** | Jede Tabellenzelle enthält genau einen Wert aus dem vorgesehenen Wertebereich – keine Listen oder Wiederholungsgruppen in einzelnen Spalten | Mehrwertige Felder (z. B. `Telefonnummern = "040-1234, 0176-5678"`) in einzelne Zeilen bzw. eine eigene Tabelle überführen, Primärschlüssel festlegen | 🔴 |
| **2NF** | Tabelle ist in 1NF, und jedes Nicht-Schlüssel-Attribut hängt vom **gesamten** Schlüssel ab (keine partiellen Abhängigkeiten) | Bei zusammengesetzten Schlüsseln: Attribute, die nur von einem Teil des Schlüssels abhängen, in eine eigene Tabelle auslagern | 🔴 |
| **3NF** | Tabelle ist in 2NF, und kein Nicht-Schlüssel-Attribut hängt **transitiv** von einem anderen Nicht-Schlüssel-Attribut ab | Transitiv abhängige Spalten in eine eigene Tabelle auslagern | 🔴 |

> **Hinweis zur Vereinfachung:** Formal beziehen sich die Normalform-Definitionen auf **funktionale Abhängigkeiten und Kandidatenschlüssel**, nicht nur auf "den" Primärschlüssel. Für die meisten IHK-Aufgaben reicht die Betrachtung des Primärschlüssels aus – wichtig ist aber: Ein Feld wie eine Adresse ist nicht *automatisch* eine 1NF-Verletzung. Ob ein Wert als "atomar" gilt, hängt vom Verwendungszweck ab (muss die Anwendung z. B. gezielt nach PLZ suchen können?). Eine eindeutige 1NF-Verletzung liegt vor, wenn eine Spalte mehrere gleichartige Werte enthält (Wiederholungsgruppe).

> **IHK-Typfrage:** *"Erklären Sie den Begriff der transitiven Abhängigkeit anhand eines Beispiels und wie sie 3NF verletzt."*
> **Musterantwort:** Eine transitive Abhängigkeit liegt vor, wenn ein Nicht-Schlüssel-Attribut nicht direkt vom Schlüssel abhängt, sondern über ein anderes Nicht-Schlüssel-Attribut. Beispiel: In `Mitarbeiter(MitarbeiterID, Name, AbteilungsID, AbteilungsName)` bestimmt `MitarbeiterID` die `AbteilungsID`, und `AbteilungsID` bestimmt den `AbteilungsName` – also hängt `AbteilungsName` transitiv, über den Umweg `AbteilungsID`, vom Primärschlüssel `MitarbeiterID` ab. Das verletzt 3NF, weil sich bei einer Abteilungsumbenennung mehrere Zeilen inkonsistent zueinander verhalten könnten. Lösung: `AbteilungsID` und `AbteilungsName` in eine eigene Tabelle `Abteilung` auslagern und per Fremdschlüssel referenzieren.

### 2.3 Beispiel: Von einer 1NF-konformen Relation zur 3NF

Das folgende Beispiel startet bewusst nicht bei 0NF/UNF (Wiederholungsgruppen), sondern bei einer bereits atomaren, aber noch nicht vollständig normalisierten Relation – so wie viele IHK-Aufgaben direkt mit einer 1NF-Tabelle beginnen und die 2NF-/3NF-Prüfung verlangen.

Ausgangsrelation, bereits in 1NF (alle Werte atomar, ein Wert pro Zelle – wiederholte Zeilen pro `BestellID` sind hier keine 1NF-Verletzung, sondern normale relationale Struktur; problematisch sind die *Abhängigkeiten*, nicht die Zeilenwiederholung):

```text
Bestellposition(BestellID, Bestelldatum, KundenID, KundenName,
                 ProduktID, ProduktName, Einzelpreis, Menge)

Angenommener Schlüssel: (BestellID, ProduktID)
Annahme: Ein Produkt kommt innerhalb derselben Bestellung höchstens einmal vor
         (sonst wäre z. B. eine zusätzliche Positionsnummer nötig).

Funktionale Abhängigkeiten:
BestellID              → Bestelldatum, KundenID
KundenID                → KundenName
ProduktID               → ProduktName, Einzelpreis
(BestellID, ProduktID)  → Menge
```

**1NF:** Wie oben begründet bereits erfüllt.

**2NF:** `Bestelldatum` und `KundenID` hängen nur von `BestellID` ab (Teil des Schlüssels), `ProduktName`/`Einzelpreis` nur von `ProduktID` (ebenfalls nur ein Teil) – das sind **partielle Abhängigkeiten**. Auslagern:

```text
Bestellung(BestellID PK, Bestelldatum, KundenID, KundenName)
Produkt(ProduktID PK, ProduktName, Einzelpreis)
Bestellposition(BestellID PK/FK, ProduktID PK/FK, Menge)
```

**3NF:** In `Bestellung` hängt `KundenName` transitiv über `KundenID` vom Primärschlüssel `BestellID` ab. Auslagern:

```text
Kunde(KundenID PK, KundenName)
Bestellung(BestellID PK, Bestelldatum, KundenID FK)
Produkt(ProduktID PK, ProduktName, Einzelpreis)
Bestellposition(BestellID PK/FK, ProduktID PK/FK, Menge)
```

Vier Tabellen, deutlich weniger vermeidbare Redundanz und klare Zuständigkeiten für die einzelnen Daten – jede fachliche Information wird an der dafür vorgesehenen Stelle gepflegt (Fremdschlüssel-Werte selbst sind naturgemäß weiterhin an mehreren Stellen vorhanden, das ist kein Normalisierungsfehler).

### 2.4 Denormalisierung als bewusster Gegenentwurf

Nicht jede Datenbank soll bis 3NF normalisiert bleiben: In analytischen Systemen wie Data Warehouses oder Reporting-Datenbanken werden Daten häufig bewusst in Stern- oder Schneeflockenschemata organisiert oder um Aggregationen/materialisierte Ergebnisse ergänzt (siehe Materialized Views, Kapitel 4), um typische Leseabfragen zu vereinfachen und zu beschleunigen – nicht zwingend eine "Rückkehr" zu 2NF/1NF im formalen Sinn, sondern oft gezielt eingeführte Redundanz. Das ist ein bewusster Kompromiss zwischen Redundanzfreiheit und Lesegeschwindigkeit, keine "falsche" Normalisierung – und eine hohe Normalform ist umgekehrt nicht automatisch ein Performance-Nachteil.

---

## 3. Erweiterte SQL-Abfragen und Aggregationen

> **Grundprinzip:** Ein normalisiertes Schema verteilt Informationen wie Bestand auf verschiedene Lagerabschnitte – erst über Joins wird daraus wieder eine vollständige Kommissionierliste zusammengestellt.

### 3.1 SQL-Sprachfamilien

| Sprachfamilie | Zweck | Beispielbefehle | IHK-Relevanz |
| --- | --- | --- | --- |
| **DDL** (Data Definition Language) | Struktur definieren | `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` | 🔴 |
| **DML** (Data Manipulation Language) | Datensätze verändern | `INSERT`, `UPDATE`, `DELETE` | 🔴 |
| **DQL** (Data Query Language) | Daten abfragen | `SELECT` | 🔴 |

> Je nach Lehrbuch wird `SELECT` entweder einer eigenen Kategorie DQL zugeordnet (wie in diesem Artikel) oder als Teil der DML behandelt – beide Sichtweisen sind gebräuchlich.

Zwei häufig verwendete DQL-Zusätze: `DISTINCT` entfernt doppelte Ergebniszeilen, `ORDER BY` sortiert das Ergebnis:

```sql
SELECT DISTINCT country_id FROM cities ORDER BY country_id;
```

### 3.2 Mehrfache Joins

| Join-Typ | Verhalten | IHK-Relevanz |
| --- | --- | --- |
| `INNER JOIN` | Nur Datensätze mit Übereinstimmung in **beiden** Tabellen | 🔴 |
| `LEFT JOIN` | Alle Datensätze der linken Tabelle; für Zeilen ohne Treffer in der rechten Tabelle enthalten deren Spalten `NULL` | 🔴 |
| `RIGHT JOIN` | Alle Datensätze der rechten Tabelle, passende der linken (sonst `NULL`) | 🟡 |
| `FULL JOIN` (in PostgreSQL: `FULL OUTER JOIN`) | Alle Datensätze aus beiden Tabellen, unabhängig von einer Übereinstimmung | 🟡 |

### 3.3 Aggregationen, GROUP BY und HAVING

```sql
SELECT country_id, COUNT(city_id) AS city_count
FROM cities
GROUP BY country_id
HAVING COUNT(city_id) > 5;
```

**`WHERE` vs. `HAVING`:** `WHERE` filtert einzelne Zeilen **vor** der Gruppierung, `HAVING` filtert bereits gebildete Gruppen **nach** der Aggregation. Aggregatfunktionen wie `COUNT()` oder `SUM()` können deshalb nicht direkt in der `WHERE`-Klausel **derselben Abfrageebene** verwendet werden – innerhalb einer Subquery, die dann in `WHERE` referenziert wird, sind Aggregatfunktionen dagegen problemlos möglich:

```sql
-- Aggregatfunktion in einer Subquery innerhalb von WHERE ist erlaubt
SELECT product_id, product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

> `COUNT(*)` zählt alle Zeilen, `COUNT(spalte)` zählt nur Zeilen mit einem Wert ungleich `NULL` in dieser Spalte – ein häufiger Prüfungsstolperstein.

### 3.4 Subqueries (Unterabfragen)

Eine Subquery ist eine SQL-Abfrage, die in eine andere Abfrage eingebettet ist.

| Operator | Verhalten | IHK-Relevanz |
| --- | --- | --- |
| `IN` | Prüft, ob ein Wert in der Ergebnisliste der Subquery enthalten ist | 🔴 |
| `EXISTS` | Liefert `true`, sobald die Subquery mindestens einen Treffer liefert – bricht früh ab | 🔴 |
| `ANY` / `ALL` | Vergleicht einen Wert mit einem beliebigen bzw. allen Werten der Subquery-Liste | 🟡 |

> **IHK-Typfrage:** *"Unter welchen Umständen ist `EXISTS` einer `IN`-Subquery vorzuziehen?"*
> **Musterantwort:** `EXISTS` drückt semantisch eine reine Existenzprüfung aus und kann bei korrelierten Unterabfragen beim ersten Treffer abbrechen. `IN` vergleicht einen Wert gegen eine Ergebnismenge. Moderne Datenbank-Optimierer können beide Formen häufig in ähnliche Ausführungspläne überführen – die Wahl sollte deshalb primär nach Lesbarkeit/Semantik erfolgen und bei Performance-Zweifeln mit `EXPLAIN ANALYZE` überprüft werden, nicht pauschal nach der Faustregel "EXISTS ist schneller".

> **Prüfungsfalle NULL bei `NOT IN`:** Enthält die Ergebnisliste einer `NOT IN`-Subquery einen `NULL`-Wert, wird der Vergleich mit diesem Wert wegen der dreiwertigen SQL-Logik (`TRUE`/`FALSE`/`UNKNOWN`) zu `UNKNOWN` – betroffene Zeilen werden dadurch von der `WHERE`-Klausel nicht ausgewählt, auch wenn man ein anderes Ergebnis erwarten würde. Für reine Nichtexistenzprüfungen ist `NOT EXISTS` deshalb häufig robuster als `NOT IN`.

---

## 4. Views und Rechteverwaltung (RBAC)

> **Grundprinzip:** Eine View ist wie ein Schaufenster in einer Werkstatt – Kund:innen sehen nur die fertigen, ausgewählten Stücke, nicht das komplette, unsortierte Lager dahinter. Rechteverwaltung ist wie ein Werkstatt-Schlüsselsystem: Jede Mitarbeiterin bekommt nur die Schlüssel zu den Räumen, die sie für ihre Arbeit tatsächlich braucht.

### 4.1 Datenbank-Views

Eine **View** ist eine virtuelle Tabelle auf Basis des Ergebnisses eines SQL-Statements – sie speichert keine eigenen Daten, sondern führt ihre zugrunde liegende Abfrage bei jedem Zugriff dynamisch aus.

```text
[ Client-Anwendung / Nutzer:in ]
              |
              v (fragt ab)
    +-------------------+
    |   Datenbank-View   |  (zeigt nur unkritische, bereits verknüpfte Spalten)
    +-------------------+
              |
              v (fragt dynamisch ab)
+-----------------------------------+
| Rohtabelle A | Rohtabelle B | ... |  (hochsensible physische Tabellen)
+-----------------------------------+
```

| Nutzen | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **Abstraktion** | Komplexe Mehrfach-Joins werden hinter einer einfachen, tabellenähnlichen Schnittstelle versteckt | 🔴 |
| **Sicherheit** | Nur ausgewählte, unkritische Spalten werden sichtbar gemacht (z. B. keine Passwort-Hashes, Gehälter, interne Schlüssel) | 🔴 |

> **Wichtig:** Eine View erhöht die Sicherheit nicht allein durch ihre Existenz. Sie wirkt nur dann als Zugriffsschranke, wenn die Nutzerrolle **keine direkten Rechte** auf die zugrunde liegenden Basistabellen besitzt und stattdessen ausschließlich Rechte auf die View erhält (siehe 4.2).

> **Materialized View (Vorgriff, Details siehe Deep-Dive):** Anders als eine gewöhnliche View speichert eine **Materialized View** das Abfrageergebnis physisch und muss per `REFRESH MATERIALIZED VIEW` aktualisiert werden. Sie wird eingesetzt, wenn Abfragegeschwindigkeit wichtiger ist als sofortige Aktualität (z. B. Reporting-Dashboards).

### 4.2 Rollenbasierte Rechtevergabe (RBAC)

Um das **Prinzip der minimalen Rechtevergabe** (Least Privilege) durchzusetzen, werden Rechte typischerweise nicht direkt an einzelne Nutzerkonten, sondern an fachliche **Rollen** vergeben, denen dann Nutzerkonten zugeordnet werden:

```sql
-- 1. Fachliche Rolle mit den benötigten Rechten anlegen
CREATE ROLE reporting_readonly NOLOGIN;
GRANT USAGE ON SCHEMA public TO reporting_readonly;
GRANT SELECT ON public.public_department_roster TO reporting_readonly;

-- 2. Login-fähiges Nutzerkonto anlegen und der Rolle zuordnen
CREATE USER reporting_user WITH PASSWORD 'PLATZHALTER_niemals_im_Klartext';
GRANT reporting_readonly TO reporting_user;
```

> In Produktivsystemen gehören Passwörter nicht als Klartext ins SQL-Skript oder in den Quellcode – üblich sind Secret Stores, Umgebungsvariablen oder vergleichbare geschützte Bereitstellungsverfahren. Das Muster `Berechtigung → Rolle → Nutzerkonto` erleichtert außerdem die spätere Pflege: Ändert sich der Aufgabenbereich, wird die Rollenzuordnung angepasst statt einzelner Nutzerrechte.

Neu angelegte Rollen besitzen nicht automatisch Zugriffsrechte auf bestehende Tabellen und Views. PostgreSQL gewährt jedoch für einige Objekttypen standardmäßig Rechte an die Pseudo-Rolle `PUBLIC` (z. B. `CONNECT` auf Datenbanken oder `EXECUTE` auf Funktionen) – auf Tabellen bestehen von Haus aus keine `PUBLIC`-Rechte. Für Tabellen/Views müssen Rechte also explizit für konkrete Aktionen (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) vergeben werden.

> **IHK-Typfrage:** *"Warum gilt es als Sicherheitsrisiko, eine Backend-Anwendung mit dem `postgres`-Superuser-Konto zu verbinden?"*
> **Musterantwort:** Das Superuser-Konto besitzt uneingeschränkte Rechte – bei einer erfolgreichen Injection-Attacke oder einem kompromittierten Anwendungsserver hätte ein Angreifer damit vollen Zugriff auf alle Tabellen, könnte Schemata verändern oder Nutzer:innen anlegen. Ein Konto mit minimal notwendigen Rechten (Least Privilege) begrenzt den möglichen Schaden auf genau die Aktionen, die die Anwendung tatsächlich benötigt.

---

## 5. NoSQL-Datenbanken und Cloud-Datenbanken (DBaaS)

> **Grundprinzip:** ACID ist wie ein exaktes Rezept, das Schritt für Schritt fehlerfrei durchlaufen werden muss – gelingt ein Schritt nicht, wird das ganze Gericht verworfen. BASE ist eher wie ein Buffet, das durchgehend geöffnet bleibt, auch wenn einzelne Schüsseln gerade nachgefüllt werden – irgendwann sind wieder alle Schüsseln synchron voll.

### 5.1 Vier NoSQL-Kategorien

| Kategorie | Datenmodell | Beispiel-Software | IHK-Relevanz |
| --- | --- | --- | --- |
| **Dokumentenorientiert** | Flexible, selbstbeschreibende Dokumente (JSON/BSON) | MongoDB, CouchDB | 🔴 |
| **Key-Value** | Einfachstes Modell: eindeutige Schlüssel-Wert-Paare | Redis, DynamoDB | 🔴 |
| **Column-Family** | Optimiert für große, verteilte Spaltenmengen | Apache Cassandra, HBase | 🟡 |
| **Graph** | Optimiert für stark vernetzte Beziehungen (Knoten, Kanten, Eigenschaften) | Neo4j, Neptune | 🟢 |

> Der Begriff "schemalos" ist verbreitet, aber ungenau: Die meisten NoSQL-Systeme haben kein starres Datenbankschema, das Schema wird aber häufig implizit durch die Anwendung, durch Validierungsregeln oder durch bestehende Dokumente vorgegeben. Treffender ist **"schemaflexibel"**.

### 5.2 ACID vs. BASE im Detail

| Eigenschaft (BASE) | Bedeutung |
| --- | --- |
| **Basically Available** | Das System bleibt auch bei teilweisen Knotenausfällen grundsätzlich betriebsbereit |
| **Soft State** | Der Datenzustand kann sich über Zeit ändern, auch ohne aktive Nutzerinteraktion (Hintergrund-Synchronisation) |
| **Eventually Consistent** | Wenn keine neuen Änderungen mehr hinzukommen und die Kommunikation zwischen den Replikaten funktioniert, konvergieren alle Replikate mit der Zeit zum selben Stand – zwischenzeitlich inkonsistente Zustände werden toleriert |

> **Vorgriff CAP-Theorem (Details siehe Deep-Dive):** Tritt in einem verteilten System eine Netzwerkpartition auf, kann es für deren Dauer nicht gleichzeitig vollständige Konsistenz **und** vollständige Verfügbarkeit garantieren – das System muss zwischen beiden abwägen. Die verbreitete Kurzformel "2 von 3 (C, A, P)" ist eine Vereinfachung: Partition Tolerance ist in echten verteilten Systemen praktisch gesetzt, die eigentliche Abwägung findet zwischen C und A statt.

### 5.3 Cloud-Datenbank-Betriebsmodelle (DBaaS)

> Die folgenden vier Stufen sind ein **didaktisches Modell** zur Einordnung des Administrationsaufwands – die Bezeichnungen sind nicht herstellerübergreifend einheitlich standardisiert, und eine selbstverwaltete Datenbank auf einer Cloud-VM wird in mancher Literatur eher als "IaaS plus selbstbetriebene Datenbank" denn als eigentliches DBaaS bezeichnet.

| Modell | OS-Zugriff | Administrationsaufwand | IHK-Relevanz |
| --- | --- | --- | --- |
| **Self-Managed Cloud DB** | Voller Zugriff (nur virtuelle Hardware vom Anbieter) | Hoch – Installation, Patching, Administration liegen beim Unternehmen | 🟡 |
| **Automated Cloud DB** | Voller OS-/Konfigurationszugriff | Mittel – Backups/Skalierung automatisiert, Rest manuell | 🟡 |
| **Managed Cloud DB** | Kein OS-Zugriff, nur DB-Ebene konfigurierbar | Niedrig – Anbieter patcht und sichert vollständig | 🔴 |
| **Autonomous Cloud DB** | Kein Zugriff | Sehr niedrig – automatisierte Selbstoptimierung, Patching, Backup, Recovery (Begriff stark durch einzelne Anbieterprodukte geprägt, z. B. Oracle Autonomous Database) | 🟡 |

### 5.4 PyMongo – Python-Anbindung an MongoDB

```python
from pymongo import MongoClient

# Verbindung aufbauen
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
collection = db["items"]

# Dokument einfügen
item = {"item_id": 1024, "name": "Tablet", "specs": {"ram": "8GB"}}
collection.insert_one(item)

# Dokumente nach Kriterium abfragen
# find() liefert einen Cursor zurück, über den iteriert wird – keine fertige Liste
for result in collection.find({"specs.ram": "8GB"}):
    print(result)
```

> **IHK-Typfrage:** *"Warum kann bei einer eventual-konsistenten NoSQL-Datenbank eine Leseanfrage kurz nach dem Schreiben noch einen veralteten Wert liefern?"*
> **Musterantwort:** Bei BASE-Systemen wird eine Schreiboperation zunächst auf einem Knoten bestätigt, die Synchronisation auf alle anderen Replikate erfolgt aber asynchron im Hintergrund. Trifft eine Leseanfrage in diesem kurzen Zeitfenster auf ein noch nicht aktualisiertes Replikat, erhält man den alten Wert. Unter normalen Betriebsbedingungen (keine neuen Änderungen, funktionierende Kommunikation) konvergieren die Replikate mit der Zeit zum selben Stand – eine sofortige Konsistenz wird aber nicht garantiert.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Normalisierung sollte immer möglichst weit getrieben werden (5NF, BCNF etc.) | In der Praxis reicht meist 3NF – weitergehende Normalisierung kann zu Übernormalisierung und schlechterer Join-Performance führen |
| 2 | 2NF-Prüfung ist bei jeder Tabelle gleichermaßen relevant | Partielle Abhängigkeiten (2NF-Verletzung) können nur bei **zusammengesetzten** Schlüsseln auftreten – bei einem einfachen Kandidatenschlüssel ist eine Tabelle nach Erreichen der 1NF in typischen IHK-Aufgaben automatisch auch in 2NF |
| 3 | `WHERE` und `HAVING` sind austauschbar | `WHERE` filtert Zeilen vor der Gruppierung, `HAVING` filtert Gruppen nach der Aggregation – Aggregatfunktionen in der `WHERE`-Klausel derselben Abfrageebene funktionieren nicht (in einer Subquery innerhalb von `WHERE` aber schon) |
| 4 | `EXISTS` ist immer schneller als `IN` | Moderne Optimierer überführen beide Formen oft in ähnliche Ausführungspläne – die Wahl sollte primär nach Semantik erfolgen, nicht nach einer pauschalen Performance-Faustregel |
| 5 | Eine View speichert eine eigene Kopie der Daten | Eine (einfache) View speichert keine eigenen Daten, sondern führt ihre Abfrage bei jedem Zugriff dynamisch aus – anders bei einer **Materialized View**, die tatsächlich physisch Daten vorhält |
| 6 | NoSQL bedeutet automatisch "schneller" oder "besser skalierbar" als relational | NoSQL optimiert primär für Verfügbarkeit/Skalierbarkeit bei semi-/unstrukturierten Daten – für stark strukturierte, transaktionskritische Daten ist relational oft die bessere Wahl |
| 7 | ACID und BASE schließen sich in einer Systemarchitektur gegenseitig aus, und relational=ACID/NoSQL=BASE ist zwingend | Viele Architekturen kombinieren beide bewusst; auch die Zuordnung ACID↔relational und BASE↔NoSQL ist nur der typische, nicht der zwingende Fall |
| 8 | Eine m:n-Beziehung kann mit einem einzelnen Fremdschlüssel in einer der beteiligten Tabellen abgebildet werden | m:n erfordert eine separate Verbindungstabelle, da eine Fremdschlüssel-Spalte nur einen einzigen Wert referenzieren kann |
| 9 | Das CAP-Theorem bedeutet, dass ein System sich dauerhaft für nur zwei von drei Eigenschaften entscheiden muss | Die Abwägung gilt nur **für die Dauer einer Netzwerkpartition** zwischen Konsistenz und Verfügbarkeit – Partition Tolerance ist in verteilten Systemen praktisch gesetzt, keine gleichrangige dritte Wahloption |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **UUIDs vs. Auto-Increment-Integer** (→ Kapitel 1.2, Primärschlüssel): Sicherheits- und Performance-Trade-offs von UUIDs als Primärschlüssel gegenüber fortlaufenden Integern – UUIDs verhindern vorhersagbares URL-Scanning, erhöhen aber Speicherbedarf und B-Tree-Indexierungsaufwand.
- **PostgreSQL `EXPLAIN ANALYZE`** (→ Kapitel 3, SQL-Abfragen): Wie sich mit `EXPLAIN`/`EXPLAIN ANALYZE` der tatsächliche Ausführungsplan einer Abfrage untersuchen und z. B. fehlende Indizes (volle Tabellenscans) identifizieren lassen.
- **Materialized Views – Aktualisierungsstrategien** (→ Kapitel 4.1, Views): Über die im Haupttext genannte Grundidee hinaus: `REFRESH MATERIALIZED VIEW CONCURRENTLY` erlaubt die Aktualisierung, ohne die View währenddessen für lesende Zugriffe zu sperren (benötigt einen `UNIQUE`-Index auf der View) – relevant, wenn Reporting-Views auch während des Refreshs abfragbar bleiben müssen.
- **CAP-Theorem – CP- vs. AP-Verhalten** (→ Kapitel 5.2, ACID/BASE): Die im Haupttext beschriebene Abwägung während einer Netzwerkpartition betrifft genau genommen **starke (linearisierbare) Konsistenz** – nicht jede denkbare Konsistenzdefinition. CP/AP beschreibt dabei das Verhalten und die Konfiguration eines konkreten Systems in der Partitionssituation, nicht pauschal seine Produktkategorie: Ein **CP-orientiertes** Verhalten lehnt eine Anfrage lieber ab, statt möglicherweise veraltete Daten zu liefern; ein **AP-orientiertes** Verhalten beantwortet Anfragen weiterhin, kann dafür aber vorübergehend unterschiedliche oder veraltete Werte liefern. Viele Datenbanken lassen sich je nach Konfiguration in beide Richtungen betreiben.
- **Boyce-Codd-Normalform (BCNF)** (→ Kapitel 2, Normalisierung): Wie BCNF strenger als 3NF ist und bei sich überschneidenden zusammengesetzten Kandidatenschlüsseln auch 3NF-konforme Tabellen noch verletzen kann.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Welches Transaktionsmodell priorisiert Konsistenz, welches Verfügbarkeit? | ACID priorisiert Konsistenz, BASE priorisiert Verfügbarkeit/Skalierbarkeit – typischerweise (nicht zwingend) verbunden mit relational bzw. NoSQL |
| 2 | Wie wird eine m:n-Beziehung physisch abgebildet? | Über eine Verbindungstabelle mit je einem Fremdschlüssel auf beide beteiligten Tabellen – beide Fremdschlüssel bilden häufig gemeinsam den zusammengesetzten Primärschlüssel |
| 3 | Nenne die drei Arten von Datenbank-Anomalien. | Einfüge-, Änderungs- und Löschanomalie |
| 4 | Was ist die Anforderung von 1NF? | Alle Attribute enthalten atomare Werte, keine Wiederholungsgruppen |
| 5 | Was unterscheidet eine partielle von einer transitiven Abhängigkeit? | Partiell: Abhängigkeit von nur einem Teil eines zusammengesetzten Primärschlüssels (2NF-Verletzung). Transitiv: Abhängigkeit über ein anderes Nicht-Schlüssel-Attribut (3NF-Verletzung) |
| 6 | Warum kann `SUM()` nicht in einer `WHERE`-Klausel verwendet werden? | `WHERE` wird vor der Gruppierung ausgewertet – zu diesem Zeitpunkt existiert der Aggregat-Wert der Gruppe noch nicht |
| 7 | Was liefert ein `LEFT JOIN` für Zeilen der rechten Tabelle ohne Treffer? | `NULL`-Werte in den entsprechenden Spalten |
| 8 | Wofür steht das "S" in BASE? | Soft State – der Datenzustand kann sich ohne Nutzerinteraktion ändern |
| 9 | Welches DBaaS-Modell bietet keinen OS-Zugriff, aber volle datenbankseitige Konfiguration? | Managed Cloud DB |
| 10 | Warum ist es riskant, eine Anwendung mit einem Superuser-Datenbankkonto zu verbinden? | Ein kompromittiertes Konto hätte dann uneingeschränkten Zugriff statt nur der minimal nötigen Rechte (Verstoß gegen Least Privilege) |
| 11 | Gegeben: `Bestellposition(BestellID, ProduktID, Bestelldatum, KundenID, KundenName, ProduktName, Einzelpreis, Menge)` mit Primärschlüssel `(BestellID, ProduktID)`. Es gilt `BestellID → Bestelldatum, KundenID`, `KundenID → KundenName`, `ProduktID → ProduktName, Einzelpreis`. Welche Normalform-Verletzungen liegen vor? | `Bestelldatum`, `KundenID`, `ProduktName`, `Einzelpreis` hängen nur von einem Teil des zusammengesetzten Schlüssels ab → 2NF-Verletzung (partielle Abhängigkeit). Nach deren Behebung hängt `KundenName` noch transitiv über `KundenID` vom Schlüssel ab → 3NF-Verletzung |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **ACID** | Eigenschaften zuverlässiger Transaktionen: Atomicity, Consistency, Isolation, Durability – häufig bei relationalen DBMS, aber nicht ausschließlich dort |
| **BASE** | Verfügbarkeits- und verteilungsorientierter Ansatz, bei dem zeitweise unterschiedliche Replikatstände toleriert werden – häufig bei NoSQL-Systemen, aber nicht zwingend |
| **Junction Table** | Verbindungstabelle zur Abbildung einer m:n-Beziehung |
| **Transitive Abhängigkeit** | Nicht-Schlüssel-Attribut hängt über ein anderes Nicht-Schlüssel-Attribut vom Primärschlüssel ab (3NF-Verletzung) |
| **Übernormalisierung** | Zu viele Tabellen-Joins durch übermäßige Normalisierung, verschlechtert Leseperformance |
| **View** | Virtuelle Tabelle auf Basis einer gespeicherten Abfrage, speichert selbst keine Daten |
| **Least Privilege** | Prinzip, Nutzer:innen nur die minimal notwendigen Rechte zu gewähren |
| **Eventual Consistency** | Garantie, dass Replikate irgendwann konsistent werden, nicht sofort |
| **CAP-Theorem** | Bei einer Netzwerkpartition kann ein verteiltes System nicht gleichzeitig vollständige Konsistenz und vollständige Verfügbarkeit garantieren – es muss für deren Dauer abwägen |
| **DBaaS** | Database as a Service – Datenbankbetrieb als Cloud-Dienst; Verantwortungs-/Automatisierungsgrad hängt vom Anbieter und Dienstmodell ab (die vier Stufen in diesem Artikel sind ein didaktisches Modell, kein Branchenstandard) |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Normalisierung auf Papier | "Normalisieren Sie folgende Tabelle bis 3NF" | Alle Zwischenschritte (1NF, 2NF) dokumentieren, nicht nur das Endergebnis – PK/FK explizit markieren |
| Anomalie-Identifikation | "Nennen Sie ein Beispiel für eine Einfügeanomalie in diesem Schema" | Konkretes, aus der Aufgabenstellung abgeleitetes Beispiel, keine allgemeine Definition |
| SQL-Abfrage schreiben | "Schreiben Sie eine Abfrage, die …" | Syntaktisch korrektes SQL, sinnvolle Join-Wahl, `HAVING` nur bei Aggregatbedingungen |
| Architekturentscheidung | "Relational oder NoSQL für Szenario X?" | Abwägung mit mind. zwei Kriterien (Strukturgrad der Daten, Transaktionsanforderung, Skalierungsbedarf), begründete Entscheidung |
| Sicherheitsbegründung | "Warum sollte die Anwendung nicht mit dem Superuser verbunden werden?" | Bezug auf Least Privilege und Schadensbegrenzung bei Kompromittierung, nicht nur "ist unsicher" |

---

## 11. Merksätze für das Fachgespräch

> Normalisierung entfernt keine Daten – sie verschiebt sie an die eine Stelle, an der sie hingehören, und verknüpft den Rest per Fremdschlüssel.

> Eine transitive Abhängigkeit ist ein Umweg: Nicht-Schlüssel-Attribut A hängt nicht direkt vom Primärschlüssel ab, sondern über ein anderes Nicht-Schlüssel-Attribut B.

> `WHERE` filtert, bevor gruppiert wird – `HAVING` filtert, nachdem gruppiert wurde. Deshalb gehören Aggregatfunktionen nur in `HAVING`.

> Eine View ist Abstraktion und Sicherheit in einem: Sie zeigt nur, was gezeigt werden soll – nicht, was technisch alles dahintersteckt.

> ACID und BASE sind keine Wertung, sondern unterschiedliche Schwerpunkte – und typischerweise, nicht zwingend, mit relational bzw. NoSQL verbunden. Das CAP-Theorem betrifft speziell verteilte Systeme während einer Netzwerkpartition: Dann lassen sich vollständige Konsistenz und vollständige Verfügbarkeit nicht gleichzeitig garantieren.

---

```yaml
dokument: LF8.5-wiki-artikel
lernfeld: LF8.5
titel: "Datenbanken & Normalisierung"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-07
quellen_intern:
  - "LF8.5.1: Data Model Selection & Relational Schema Design.md"
  - "LF8.5.2: Relational Schema Normalization.md"
  - "LF8.5.3: Advanced Relational SQL Queries & Aggregations.md"
  - "LF8.5.4: Database Views & Rights Management.md"
  - "LF8.5.5: NoSQL Database Paradigms & Cloud Databases (DBaaS).md"
quellen_fachlich:
  - titel: "PostgreSQL Release Notes"
    herausgeber: "PostgreSQL Global Development Group"
    status: "PostgreSQL 18.x aktuelle Hauptversion (Stand: 07.09.2026), Version 19 in Beta-Phase"
  - titel: "PyMongo Dokumentation"
    herausgeber: "MongoDB Inc."
    status: "offizieller Python-Treiber für MongoDB"
  - titel: "CAP-Theorem (Brewer's Theorem)"
    herausgeber: "Eric Brewer / akademische Standardliteratur"
    status: "etabliertes, unverändertes Grundlagenkonzept verteilter Systeme"
review_historie:
  - runde: 1
    datum: 2026-09-07
    ergebnis: "Erstdraft mit integrierter Web-Verifikation (PostgreSQL-Versionsstand) und eigener Review nach Style-Guide-Checkliste erstellt – inkl. Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an, Analogien aus Logistik/Handwerk/Kochen statt Vertragsrecht (Lehre aus LF8.4-Review)"
  - runde: 2
    datum: 2026-09-07
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet: ACID/BASE nicht mehr starr an relational/NoSQL gebunden, vollständiges durchgerechnetes Normalisierungsbeispiel (0NF-3NF mit funktionalen Abhängigkeiten) ergänzt, PLZ→Ort durch robusteres FD-Beispiel (MitarbeiterID→AbteilungsID→AbteilungsName) ersetzt, Adresse nicht mehr als automatische 1NF-Verletzung dargestellt, Normalform-Definitionen um Kandidatenschlüssel-Hinweis ergänzt, RBAC-Beispiel auf echtes Rollen-Muster umgestellt (Rolle→Nutzerkonto statt direkter Rechtevergabe) und unsicheres Passwort-Beispiel ersetzt, Views als nicht automatisch sichere Grenze klargestellt, Materialized View in Haupttext vorgezogen, CAP-Theorem präzisiert ('nur während einer Partition', nicht dauerhaft 2-von-3), DBaaS-Vierstufenmodell als didaktisches statt standardisiertes Modell gekennzeichnet, schemalos→schemaflexibel, NOT-IN-NULL-Falle und WHERE-Aggregat-Subquery-Ausnahme ergänzt, DISTINCT/ORDER BY ergänzt, Selbsttest 11 durch eindeutig lösbare FD-basierte Frage ersetzt, Analogie in Kapitel 3 auf Logistik gewechselt (Wiederholung der Werkstatt-Metapher vermieden), PostgreSQL-Versionsangabe unverändert belassen (durch zwei Quellen mit Beleg bestätigt, abweichende dritte Review nicht übernommen)"
  - runde: 3
    datum: 2026-09-07
    ergebnis: "Finale Review (3 Reviews) geprüft: echten Konzeptfehler behoben – 'Wiederholung ganzer Zeilen' war fälschlich als 1NF-Verletzung bezeichnet, jetzt korrekt als bereits 1NF-konforme Relation mit 2NF/3NF-Problemen eingeführt, explizite Schlüssel-Annahme ergänzt; 'keine Redundanz mehr' entschärft; Denormalisierung um Stern-/Schneeflockenschema-Bezug präzisiert; Selbsttest 2 an präzisierte Junction-Table-Formulierung nachgezogen; CAP-Theorem-Deep-Dive um 'starke Konsistenz' und CP/AP-Unterscheidung geschärft (statt Wiederholung des Haupttexts); Materialized-View-Deep-Dive um REFRESH CONCURRENTLY als echte Zusatztiefe ergänzt; NOT-IN-Formulierung präzisiert. Hinweis: Eine Review meldete erneut Markdown-Beschädigungen (fehlende Leerzeilen, abgeschnittene Tabelle) und eine falsche PostgreSQL-Version – beides beim Abgleich mit der tatsächlichen Datei nicht bestätigt (PostgreSQL-Version deckt sich mit zwei unabhängigen, quellenbelegten Reviews), daher nicht übernommen"
  - runde: 4
    datum: 2026-09-07
    ergebnis: "Finaler Feinschliff (2 Reviews): Kernfrage 1 entkoppelt Datenmodell (relational/NoSQL) von Transaktionseigenschaft (ACID/BASE) statt sie gleichzusetzen, BASE-Musterantwort 'garantiert...irgendwann' entschärft, CAP-Deep-Dive CP/AP nicht mehr pauschal an Produktkategorie gekoppelt sondern als Konfigurationsfrage dargestellt, 1:1-Mapping um UNIQUE/NOT NULL ergänzt, Abschnittsüberschrift '0NF bis 3NF' zu 'Von 1NF zu 3NF' korrigiert (Beispiel startet faktisch bei 1NF) mit erklärendem Hinweis, Cheatsheet-Einträge ACID/BASE/DBaaS von 'X ist Transaktionsmodell von Y' auf 'häufig bei Y, aber nicht ausschließlich' umgestellt. Erneut gemeldete Datei-Beschädigung (abgeschnittene Tabellen, ungültiges YAML) beim Abgleich mit der tatsächlichen Datei nicht bestätigt (453 Zeilen, YAML valide geparst) – vom Nutzer als Übertragungsartefakt eingeordnet und bestätigt, keine Korrektur nötig"
freigabe: "Final gesetzt nach 4 Review-Runden (2026-09-07) – Freigabe durch Autor:in bestätigt"
```