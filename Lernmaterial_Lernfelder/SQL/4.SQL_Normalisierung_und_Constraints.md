
## 🧹 Normalisierung und Constraints: Saubere Tabellen, stabile Daten

### Worum geht’s eigentlich?

Du hast ein ERM in Tabellen überführt und mit SQL-DDL eine Datenbank angelegt. Aber woher weißt du, ob dein Tabellendesign wirklich **fachlich korrekt, frei von Redundanzen und vor widersprüchlichen Daten geschützt** ist? Genau hier greifen zwei untrennbare Konzepte:

1. **Normalisierung** – ein schrittweises Verfahren, um dein relationales Schema von unnötigen Wiederholungen und Abhängigkeiten zu befreien.
2. **Constraints** – die technischen Regeln, mit denen du diese saubere Struktur in SQL erzwingst und die Datenqualität sicherstellst.

Die Normalisierung ist also der **Bauplan-Check**, die Constraints sind das **Schutzgerüst** in der Datenbank. Beides prüft die IHK gern im Zusammenhang: erst eine Tabelle in die 3. Normalform überführen, dann die SQL-Constraints angeben.

> 💡 **Agile Side-Info:** In einem Sprint erstellt das Team erst ein Minimalmodell und normalisiert es dann, sobald neue User Stories zusätzliche Attribute oder Abhängigkeiten fordern. Constraints werden direkt im `CREATE TABLE`-Skript mitgeliefert – sie sind die ausführbare Spezifikation der Geschäftsregeln.

---

### 🧱 Die drei Normalformen – Schritt für Schritt

Die Normalformen bauen aufeinander auf. Jede setzt die vorherige voraus und beseitigt eine bestimmte Art von Anomalie.

| Normalform | Kurzbeschreibung                                                                     | Woran erkenne ich sie?                                                                 |
|------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **1NF**    | Alle Attribute enthalten nur atomare Werte (keine Listen, keine wiederholten Gruppen).| Jede Zelle enthält genau einen Wert. Keine Spalte heißt `telefon1, telefon2`.          |
| **2NF**    | 1NF + jedes Nicht-Schlüssel-Attribut ist vom **gesamten** Primärschlüssel abhängig.  | Es gibt keine Teilabhängigkeiten, wenn der PK zusammengesetzt ist.                      |
| **3NF**    | 2NF + keine Nicht-Schlüssel-Attribute hängen von anderen Nicht-Schlüssel-Attributen ab (transitive Abhängigkeiten). | Keine abgeleiteten Spalten wie `gesamtpreis = menge * einzelpreis`.                    |

**Merkregel für die Prüfung:**  
- 1NF: „Weg mit den Wiederholungsgruppen!“  
- 2NF: „Teilschlüssel-Abhängigkeiten beseitigen!“  
- 3NF: „Nicht-Schlüssel-Abhängigkeiten untereinander auflösen!“

---

### 🧩 Durchgängiges Beispiel: Vom unnormalisierten Zettel zur 3NF

Stell dir vor, ein Kunde schickt dir eine Excel-Liste seiner Bestellungen:

| bestell_nr | kunden_name | artikel_1      | artikel_2      | artikel_3      |
|------------|-------------|----------------|----------------|----------------|
| 1          | Müller      | Schraube M4    | Mutter M4      |                |
| 2          | Meier       | Dübel 8        | Schraube 5x60  | Unterlegscheibe 5 |

**Verstoß gegen 1NF:** Die Spalten `artikel_1`, `artikel_2`, `artikel_3` sind eine wiederholte Gruppe. Die Tabelle ist nicht atomar.

**Lösung:** Wir ziehen die Artikel in eine eigene Tabelle und verbinden sie mit der Bestellung.

```
bestellung: bestell_nr (PK), kunden_name
bestellposition: bestell_nr (FK) + positions_nr (PK), artikel_name
```

Jetzt ist jedes Attribut atomar. 1NF ✅

**Verstoß gegen 2NF:** Die Tabelle `bestellposition` hat den zusammengesetzten PK `(bestell_nr, positions_nr)`. Wenn jetzt ein Attribut nur von `bestell_nr` abhängt, aber nicht von der ganzen Kombination, ist das eine Teilabhängigkeit. Beispiel: Würde `kunden_name` in `bestellposition` stehen, hinge er nur von `bestell_nr` ab – die 2NF wäre verletzt (der Kundenname müsste ja bereits in der `bestellung`-Tabelle stehen).

**Lösung:** Wir haben korrekterweise `kunden_name` in der `bestellung` belassen – also alles gut. In der Prüfung müsstest du solche Felder identifizieren und auslagern.

**Verstoß gegen 3NF:** Angenommen, in `bestellung` stünde neben `kunden_name` auch `kunden_rabattgruppe`. Und die Rabattgruppe hängt direkt vom Kunden ab, nicht von der Bestellung. Dann bestünde eine transitive Abhängigkeit: `bestell_nr → kunden_name → kunden_rabattgruppe`.

**Lösung:** Auslagern in eine eigene Tabelle `kunde`, die `kunden_name` und `kunden_rabattgruppe` enthält. `bestellung` bekommt nur noch den Fremdschlüssel `kunde_id`.

Ergebnis als normalisiertes Schema:

| Tabelle         | Spalten                                                     |
|-----------------|-------------------------------------------------------------|
| kunde           | kunde_id (PK), name, rabattgruppe                           |
| bestellung      | bestell_nr (PK), kunde_id (FK), bestelldatum                |
| bestellposition | bestell_nr (FK) + positions_nr (PK), artikel_id (FK), menge |
| artikel         | artikel_id (PK), artikel_name, preis                        |

> 💡 **Agile Side-Info:** Normalisiert wird nicht im stillen Kämmerlein, sondern gemeinsam im Team – oft direkt am Whiteboard. Der Product Owner sagt: „Ein Kunde hat immer genau eine Rabattgruppe.“ Du reagierst sofort: „Gut, dann trennen wir das ab – sonst ändere ich 1000 Bestellungen, wenn sich die Rabattgruppe ändert.“ Das ist effiziente Kommunikation durch Struktur.

---

### 🔒 Constraints – die normalisierte Struktur in SQL gießen

Jede Normalform beseitigt ein Problem – Constraints verhindern, dass es überhaupt entsteht.

| Normalform | Problem                               | SQL-Constraint zur Absicherung                           |
|------------|---------------------------------------|----------------------------------------------------------|
| 1NF        | Wiederholgruppen, nicht-atomare Werte | Datentyp wählen (kein komma-getrennter String), separate Tabellen mit FK |
| 2NF        | Teilabhängigkeiten                    | `PRIMARY KEY` (zusammengesetzt, wo nötig), `FOREIGN KEY` |
| 3NF        | Transitive Abhängigkeiten             | `FOREIGN KEY` in Verbindung mit `NOT NULL`               |

**Wichtige Constraints im Überblick – das war dein erstes SQL-DDL-Board:**

| Constraint       | Syntaxbeispiel                                           | Wirkung                                                                 |
|------------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| `PRIMARY KEY`    | `artikel_id SERIAL PRIMARY KEY`                          | Eindeutige Identifikation, niemals NULL                                 |
| `FOREIGN KEY`    | `kunde_id INT REFERENCES kunde(kunde_id)`                | Verknüpfung erzwingen, referenzielle Integrität                         |
| `UNIQUE`         | `email VARCHAR(200) UNIQUE`                              | Keine doppelten Werte in dieser Spalte                                  |
| `NOT NULL`       | `name VARCHAR(100) NOT NULL`                             | Attribut muss gefüllt sein                                              |
| `CHECK`          | `menge INT CHECK (menge > 0)`                            | Nur positive Mengen erlaubt                                             |
| `DEFAULT`        | `bestelldatum DATE DEFAULT CURRENT_DATE`                 | Automatischer Wert, wenn nichts angegeben wird                          |

**Am normalisierten Beispiel in SQL gegossen:**

```sql
CREATE TABLE kunde (
    kunde_id       SERIAL PRIMARY KEY,
    name           VARCHAR(100) NOT NULL,
    rabattgruppe   VARCHAR(50)
);

CREATE TABLE bestellung (
    bestell_nr     SERIAL PRIMARY KEY,
    kunde_id       INT NOT NULL REFERENCES kunde(kunde_id),
    bestelldatum   DATE DEFAULT CURRENT_DATE
);

CREATE TABLE artikel (
    artikel_id     SERIAL PRIMARY KEY,
    artikel_name   VARCHAR(200) NOT NULL,
    preis          DECIMAL(8,2) CHECK (preis >= 0)
);

CREATE TABLE bestellposition (
    bestell_nr     INT REFERENCES bestellung(bestell_nr),
    positions_nr   INT,
    artikel_id     INT REFERENCES artikel(artikel_id),
    menge          INT CHECK (menge > 0),
    PRIMARY KEY (bestell_nr, positions_nr)
);
```

Alle Constraints arbeiten zusammen: `PRIMARY KEY` und `FOREIGN KEY` sichern die 2NF und 3NF strukturell, `CHECK` verhindert unsinnige Werte, `NOT NULL` erzwingt atomare Pflichtfelder.

> **Prüfungstipp:** Wenn die IHK-Aufgabe lautet: „Überführen Sie die Tabelle in die 3. Normalform und notieren Sie die SQL-Anweisungen“, dann erwartet sie genau diese Kombination: getrennte Tabellen mit korrekten PKs, FKs und sinnvollen Constraints.

---

### 🧠 Das bringt’s dir im Alltag (Analogien)

**Handwerk / Fertigung:**  
Ein unnormalisierter Auftragszettel enthält Kunde, Material 1, Material 2, Material 3. Nachher hast du eine saubere Stückliste mit Fremdschlüsseln zu Artikeln. Der `CHECK`-Constraint `menge > 0` verhindert, dass jemand versehentlich „-5 Schrauben“ einträgt.

**Kaufmännischer Bereich / Vertrieb:**  
Ohne 3NF stünde die Adresse des Kunden in jeder Rechnung. Zieht der Kunde um, müsstest du alle Rechnungen ändern – keine Chance auf Konsistenz. Mit normalisiertem Schema und `FOREIGN KEY` änderst du genau einen Datensatz in der `kunde`-Tabelle. Das ist die Basis für Stammdatenpflege.

**Gastronomie / Küche:**  
Ein Gericht hat Zutaten mit Mengen. Ohne 1NF würdest du eine Zutatenliste als komma-getrennten String in eine Zelle stopfen – unmöglich, daraus die Allergene zu zählen. Nachher hast du pro Position eine Zeile. Ein `UNIQUE`-Constraint auf `(gericht_id, allergen_id)` verhindert doppelte Einträge.

**Das bringt's technisch:**  
- Keine Einfüge-Anomalie: Du kannst einen neuen Kunden anlegen, noch bevor er eine Bestellung hat.  
- Keine Änderungs-Anomalie: Die Rabattgruppe änderst du einmal, nicht in jeder Bestellung.  
- Keine Lösch-Anomalie: Löschst du die letzte Bestellung eines Kunden, bleiben seine Stammdaten erhalten.

---

### 🚀 Agiler Workflow: Normalisierung als Team-Refactoring

- **User Story gibt den Takt:** „Ein Kunde kann jetzt mehrere Lieferadressen haben.“ Dein bisheriges 1:n-Gefüge muss auf n:m erweitert werden – du normalisierst praktisch eine Stufe weiter.
- **Migration statt manuellem Umbau:** Das Team schreibt ein `ALTER TABLE`-Skript, das die neue Tabelle `lieferadresse` anlegt, den FK setzt und bestehende Daten umzieht. Das wird zusammen mit dem Code deployed.
- **Constraints schützen vor Fehlern im Sprint:** Auch wenn das Backend-Team einen Bug hat, der versucht, eine Bestellung ohne `kunde_id` zu speichern – die Datenbank lehnt dank `NOT NULL` einfach ab. Das ist dein letztes Sicherheitsnetz.

🎯 **Side-Info:** In modernen DevOps-Umgebungen werden Datenbankänderungen in Migrations-Frameworks (wie Flyway oder Liquibase) versioniert. Dadurch sind Normalisierungs-Refactorings nachvollziehbar und rückrollbar – genau wie Code-Refactorings.

---

### 👣 Dein nächster Schritt

1. **Normalisierungs-Workout:** Nimm die unnormalisierte Excel-Tabelle von oben und führe sie handschriftlich in 3NF über. Zeichne das Ergebnis als ERM auf.
2. **SQL-Skript schreiben:** Setze dein normalisiertes Modell in vollständige `CREATE TABLE`-Anweisungen mit allen Constraints um.
3. **Testdaten einfügen und Fehler provozieren:** Probier ein `INSERT`, das den `CHECK`-Constraint verletzt, und beobachte die Fehlermeldung. So verstehst du die Schutzwirkung.
4. **Alte IHK-Aufgabe lösen:** Viele Prüfungen geben eine „unschöne“ Tabelle und verlangen: „Normalisieren Sie bis zur 3. Normalform und begründen Sie die Schritte.“ Trainiere besonders, Teilabhängigkeiten und transitive Abhängigkeiten zu erkennen und klar zu benennen.
5. **Zusatzaufgabe:** Entwirf selbst einen kleinen Fall: Ein Getränkemarkt verwaltet Kisten, Flaschen und Pfandbons. Normalisiere, schreibe die SQL-DDL und überlege, welche Constraints sinnvoll sind.

---

**Zusammengefasst:** Normalisierung ist nicht abstrakte Theorie – sie ist dein Handwerkszeug, um Tabellenstrukturen von Redundanzen und logischen Fallstricken zu befreien. Constraints sind der in SQL gegossene Schutz, dass diese saubere Struktur auch unter realen Bedingungen bestehen bleibt. Für die IHK-Prüfung musst du beide Konzepte im Zusammenspiel beherrschen: erkennen, was nicht normalisiert ist, es beheben und das Ergebnis als harten SQL-Code mit Schlüsseln und Prüfregeln abliefern. Mit diesem letzten Baustein ist euer Wiki nun eine vollständige Prüfungsvorbereitung für das Datenbank-Thema in Lernfeld 5.