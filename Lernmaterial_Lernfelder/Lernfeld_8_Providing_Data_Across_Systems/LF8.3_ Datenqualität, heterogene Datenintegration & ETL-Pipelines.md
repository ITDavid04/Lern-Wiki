# LF8.3 – Datenqualität, heterogene Datenintegration & ETL-Pipelines

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 90–120 Minuten reines Lesen, +60–90 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie berechnet man Completeness und Uniqueness eines Datensatzes, und welche Rolle spielt Data Profiling davor? | [→ 1. Datenqualität](#1-datenqualität-messen-und-verbessern) |
| 2 | Was unterscheidet technische, strukturelle und semantische Heterogenität? | [→ 2. Heterogene Integration](#2-heterogene-datenintegration-und-open-data) |
| 3 | Wie liest man ein UML-Aktivitätsdiagramm – speziell den Unterschied zwischen Decision/Merge und Fork/Join? | [→ 3. Aktivitätsdiagramme](#3-uml-aktivitätsdiagramme) |
| 4 | Was passiert in den drei Phasen einer ETL-Pipeline, und wann wählt man stattdessen Datenvirtualisierung? | [→ 4. ETL & Integrationsarchitekturen](#4-etl-pipelines-und-integrationsarchitekturen) |
| 5 | Was bedeuten die 5 Vs von Big Data, und warum reichen klassische Pipelines bei hoher Velocity/Volume nicht mehr aus? | [→ 5. Big Data](#5-big-data-die-5-vs) |

---

## 1. Datenqualität messen und verbessern

> **Grundprinzip:** Datenqualität ist kein Bauchgefühl, sondern eine messbare Eigenschaft – "fit for purpose", belegt durch Kennzahlen statt durch Eindruck.

### 1.1 Dimensionen der Datenqualität

Es gibt **keine einzige kanonische Liste** von Datenqualitätsdimensionen. In vielen Darstellungen (u. a. DAMA-DMBOK) werden **sechs häufig verwendete Kerndimensionen** genannt (Accuracy, Completeness, Consistency, Timeliness, Uniqueness, Validity) – die genaue Auswahl variiert aber je nach Ausgabe und Quelle; andere Quellen erweitern auf 8, 12 oder mehr, je nach Anwendungsfall. Die folgenden 12 Dimensionen bilden die im Kurs verwendete, erweiterte Lernbasis:

| Dimension | Beschreibung | IHK-Relevanz |
| --- | --- | --- |
| **Completeness** (Vollständigkeit) | Anteil der Pflichtfelder, die einen **vorhandenen** (nicht fehlenden) Wert enthalten – unabhängig davon, ob der Wert korrekt oder im richtigen Format ist | 🔴 |
| **Uniqueness** (Eindeutigkeit) | Jede reale Entität bzw. jeder fachlich erwartete Datensatz kommt nur einmal vor | 🔴 |
| **Correctness** (Korrektheit) | Der vorhandene Wert stimmt mit dem realen Sachverhalt überein (z. B. die gespeicherte PLZ ist tatsächlich die PLZ des Kunden) | 🔴 |
| **Timeliness** (Aktualität) | Daten spiegeln den aktuellen Stand der Realität wider (Gegenteil: **Data Decay**) | 🔴 |
| **Accuracy** (Genauigkeit) | ⚠️ *Kursspezifische Definition* (weicht von der Fachliteratur ab, siehe Hinweis unten): Präzisionsgrad eines Werts, z. B. Anzahl korrekter Nachkommastellen | 🟡 |
| **Consistency** (Konsistenz) | Keine Widersprüche innerhalb eines Datensatzes oder zwischen Datenquellen | 🔴 |
| **Non-redundancy** (Redundanzfreiheit) | Keine doppelte Speicherung derselben Information | 🟡 |
| **Relevancy** (Relevanz) | Daten erfüllen den konkreten Informationsbedarf (kein Datenmüll) | 🟢 |
| **Uniformity** (Einheitlichkeit) | Einheitliche Formate, z. B. Datumsangaben konsequent nach ISO 8601 (`YYYY-MM-DD`) | 🔴 |
| **Reliability** (Zuverlässigkeit) | Herkunft und Erhebung der Daten sind nachvollziehbar und verifiziert | 🟡 |
| **Understandability** (Verständlichkeit) | Bezeichnungen und Struktur entsprechen den Erwartungen der Nutzenden | 🟢 |
| **Accessibility** (Zugänglichkeit) | Daten sind für berechtigte Systeme/Personen leicht abrufbar | 🟢 |

> **Begriffshinweis Accuracy/Precision/Correctness:** In der allgemeinen Datenqualitäts-Fachliteratur (z. B. DAMA-DMBOK) wird *Accuracy* meist mit *Correctness* gleichgesetzt (Realitätsnähe eines Werts), während die Anzahl möglicher Nachkommastellen eher als *Precision* bezeichnet wird. Dieser Kurs verwendet *Accuracy* abweichend im Sinne von Präzisionsgrad – für die Prüfung reicht die Definition oben, in der Fachpraxis lohnt sich aber die Unterscheidung.
>
> **Lücke im 12-Dimensionen-Modell – Validity:** Viele Fachquellen führen zusätzlich eine eigene Dimension *Validity* (Formatgültigkeit, unabhängig vom Wahrheitsgehalt – z. B. ist `"ABCDE"` als PLZ-Wert *vorhanden*, aber weder *valide* noch *korrekt*). Das hier verwendete Kursmodell hat keine eigene Validity-Dimension; Formatprüfungen werden implizit unter Correctness oder Consistency mitgedacht. Für Berechnungsaufgaben in der Prüfung reicht das aus, in einer echten Datenqualitäts-Pipeline würde man Validity meist separat prüfen (vor Correctness, da eine ungültige PLZ gar nicht erst gegen die Realität abgeglichen werden kann).

**Berechnungsformeln (K3 = Anwenden/Berechnen in konkreten Aufgabenstellungen):**

$$\text{Completeness (\%)} = \frac{\text{vorhandene Pflichtfeldwerte}}{\text{erwartete Pflichtfeldwerte}} \times 100$$

$$\text{Uniqueness (\%)} = \frac{\text{eindeutige Datensätze}}{\text{Datensätze gesamt}} \times 100$$

> **IHK-Typfrage:** *"Ein Datensatz mit 500 Kundenadressen enthält 40 zusätzliche Duplikat-Zeilen (d. h. 460 Datensätze sind eindeutig) und 25 Zeilen mit fehlender Postleitzahl. Berechnen Sie Completeness und Uniqueness."*
> **Musterantwort:** Completeness (bezogen auf das Pflichtfeld PLZ) = (500 − 25) / 500 × 100 = **95 %**. Uniqueness = 460 / 500 × 100 = **92 %**. Wichtig: "Duplikate" muss immer konkret definiert werden (zusätzliche Kopien vs. Datensatzpaare vs. Duplikatgruppen) – in der Prüfung steht diese Definition meist in der Aufgabenstellung. Beide Kennzahlen sind getrennt zu betrachten, da sie unterschiedliche Fehlerarten messen – ein hoher Completeness-Wert sagt nichts über Duplikate aus und umgekehrt.

### 1.2 Der Datenqualitäts-Verbesserungsprozess

Datenqualität ist kein einmaliges Projekt, sondern ein kontinuierlicher Kreislauf aus drei Phasen:

```text
[ 1. Data Profiling ] ---> [ 2. Data Cleaning ] ---> [ 3. Data Monitoring ]
 (Analysieren,                (Bereinigen,              (Kontinuierlich
  Muster/Anomalien              Duplikate/Fehler          überwachen, Decay
  entdecken)                    algorithmisch lösen)      verhindern)
```

| Phase | Was passiert | IHK-Relevanz |
| --- | --- | --- |
| **Data Profiling** | Programmatische Exploration von Rohdaten: Muster, Anomalien, Widersprüche, statistische Verteilungen aufdecken | 🔴 |
| **Data Cleaning** | Aktive Bereinigung: erkannte Fehler, Duplikate und fehlende Werte werden nach festgelegten Regeln behoben | 🔴 |
| **Data Monitoring** | Fortlaufende, automatisierte Prüfung der Datenqualität über die Zeit, um Data Decay zu verhindern | 🟡 |

**Warum muss Profiling vor Cleaning stehen?** Ohne vorherige Analyse weiß man nicht, *welche* Bereinigungsregeln überhaupt nötig sind – man würde blind Regeln anwenden, die im schlimmsten Fall korrekte Daten verfälschen oder tatsächliche Fehler übersehen.

**Data Decay (Datenalterung):** Daten verlieren mit der Zeit an Aktualität – Personen ziehen um, Preise ändern sich, Kontaktdaten veralten. Ohne kontinuierliches Monitoring sinkt die Timeliness schleichend, auch wenn die Daten beim Import einwandfrei waren.

---

## 2. Heterogene Datenintegration und Open Data

> **Grundprinzip:** Bevor Daten aus mehreren Quellen zusammengeführt werden können, müssen Unterschiede in Zugriff, Struktur und Bedeutung aufgelöst werden – nicht nur die Formate.

### 2.1 Open Data vs. Closed Data

| Aspekt | Open Data | Closed Data | IHK-Relevanz |
| --- | --- | --- | --- |
| Zugänglichkeit | Frei zugänglich **und** unter einer offenen Lizenz nutzbar, veränderbar, weiterverbreitbar | Nicht offen lizenziert und/oder zugriffsbeschränkt – umfasst kommerzielle Lizenzen, urheberrechtlich geschützte oder personenbezogene Daten | 🟡 |
| Typische Herkunft | Open Government Data (Wetter-, Geo-, Fahrplandaten) | Kommerzielle Produkte, urheberrechtlich geschützte Inhalte, personenbezogene Daten (DSGVO) | 🟡 |
| Format-Anforderung | Sollte maschinenlesbar & offen sein (CSV, JSON, XML statt gescannter PDFs) – Maschinenlesbarkeit allein macht Daten aber noch nicht zu Open Data, die Lizenz entscheidet | Format meist proprietär oder vertraglich geregelt | 🟢 |

> Personenbezogene Daten sind nicht automatisch "Closed Data" im engeren Sinn – sie können aber wegen Datenschutz, Zweckbindung oder fehlender Einwilligung nicht ohne Weiteres als Open Data veröffentlicht werden.

### 2.2 Drei Formen der Heterogenität

Beim Zusammenführen mehrerer Datenquellen treten drei unterschiedliche, klar zu trennende Heterogenitätsebenen auf:

```text
                        [ Data Heterogeneity ]
                       /          |            \
          [ Technisch ]     [ Strukturell ]     [ Semantisch ]
          (Zugriff/API)     (Schema/Tabellen)   (Bedeutung/Naming)
```

| Ebene | Beschreibung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Technisch (syntaktisch)** | Zugriffsschnittstellen/Dateiformate unterscheiden sich | Ein System liefert SOAP/XML, ein anderes CSV, ein drittes REST/JSON | 🔴 |
| **Strukturell** | Gleicher Sachverhalt, aber unterschiedliches Datenbankschema | Adresse als ein Textfeld vs. normalisiert in `cities`/`streets`-Tabellen | 🔴 |
| **Semantisch** | Bedeutung, Bezugsart oder Einheit weichen ab, nicht nur der Feldname | System A: `price_net_eur` = Nettopreis in Euro; System B: `item_cost` = Einkaufspreis in US-Dollar | 🔴 |

> Je nach Fachquelle werden technische und syntaktische Heterogenität zusammengefasst (wie in diesem Artikel) oder als zwei getrennte Ebenen behandelt (Zugriffsprotokoll vs. Dateiformat). Für die Prüfung reicht die Dreiteilung technisch/strukturell/semantisch.

> **IHK-Typfrage:** *"Ein System speichert Preise als `item_cost` (USD, Einkaufspreis), ein anderes als `price_net_eur` (EUR, Nettoverkaufspreis). Um welche Form der Heterogenität handelt es sich?"*
> **Musterantwort:** Semantische Heterogenität – die Felder unterscheiden sich nicht nur im Namen, sondern in Bedeutung (Einkaufs- vs. Verkaufspreis), Bezugsart (netto/brutto) und Einheit (USD/EUR). Eine reine Umbenennung würde das Problem nicht lösen; nötig ist eine gemeinsame Mapping-/Metadaten-Ebene mit Umrechnung.

### 2.3 Ingestions-Formate im Vergleich

| Format | Struktur | Stärken | Schwächen | IHK-Relevanz |
| --- | --- | --- | --- | --- |
| **CSV** | Flach, tabellarisch, Trennzeichen-basiert (`,` `;` Tab) | Einfach, kompakt, universell lesbar | Keine verschachtelten Strukturen, keine standardisierte Typsicherheit im Format selbst | 🔴 |
| **XML** | Hierarchisch, Tag-basiert, mit Attributen | Sehr robust, formal validierbar (XSD) | Umfangreich (viel Markup-Overhead), rechenintensiv beim Parsen | 🟡 |
| **JSON** | Schlüssel-Wert-Paare, Arrays, leichtgewichtig | De-facto-Standard moderner APIs, native Nähe zu JS/TS-Objekten und Python-Dicts | Weniger robuste Typprüfung als XSD ohne zusätzliches JSON Schema | 🔴 |

---

## 3. UML-Aktivitätsdiagramme

> **Grundprinzip:** Während Zustandsdiagramme den Lebenszyklus *eines* Objekts zeigen, modellieren Aktivitätsdiagramme den *Kontroll- und Datenfluss* eines gesamten Prozesses über mehrere Beteiligte hinweg.

Aktivitätsdiagramme sind Teil der UML-Spezifikation des OMG (aktuell **UML 2.5.1**, formal seit 2017, weiterhin die gültige Fassung – keine neuere UML-3.0-Version veröffentlicht). Sie eignen sich als standardisierte Alternative zu klassischen Flowcharts/Nassi-Shneiderman-Diagrammen und können zusätzlich Verantwortlichkeiten (Partitionen), parallele Abläufe und Datenflüsse abbilden – besonders relevant für dieses Lernfeld beim Modellieren von ETL-Pipelines.

### 3.1 Notationselemente

| Element | Symbol | Bedeutung | IHK-Relevanz |
| --- | --- | --- | --- |
| **Startknoten** | Ausgefüllter schwarzer Kreis | Einstiegspunkt des Ablaufs | 🔴 |
| **Endknoten (Activity Final)** | Kreis mit Punkt ("Bullseye") | Beendet den *gesamten* Ablauf | 🔴 |
| **Ablaufende (Flow Final)** | Kreis mit "X" | Beendet nur *einen* parallelen Pfad, andere laufen weiter | 🟡 |
| **Aktion** | Abgerundetes Rechteck | Ein atomarer Verarbeitungsschritt | 🔴 |
| **Kontrollfluss** | Durchgezogener Pfeil | Sequenzieller Ausführungspfad | 🔴 |
| **Verzweigung (Decision)** | Raute, 1 rein / mehrere raus | Genau **ein** Pfad wird abhängig von Bedingung (`[guard]`) ausgeführt | 🔴 |
| **Zusammenführung (Merge)** | Raute, mehrere rein / 1 raus | Führt alternative Zweige wieder zusammen – **keine** Synchronisation | 🔴 |
| **Aufspaltung (Fork)** | Balken, 1 rein / mehrere raus | Aktiviert mehrere **nebenläufige** Pfade unabhängig voneinander | 🔴 |
| **Synchronisation (Join)** | Balken, mehrere rein / 1 raus | Wartet, bis **alle** eingehenden Pfade abgeschlossen sind | 🔴 |

### 3.2 Verzweigung/Zusammenführung vs. Parallelität – die häufigste Verwechslung

Decision/Merge und Fork/Join sehen in Diagrammen ähnlich aus (je zwei Knoten mit mehreren Pfeilen), unterscheiden sich aber grundlegend in der Ausführungssemantik:

| Aspekt | Decision → Merge | Fork → Join |
| --- | --- | --- |
| Ausgeführte Pfade | **Genau ein** Pfad (abhängig von Guard-Bedingung) | **Alle** Pfade nebenläufig |
| Symbol | Raute (◇) | Balken (▬) |
| Was passiert am Gegenstück | Merge führt Pfade zusammen, ohne zu warten | Join wartet, bis **alle** parallelen Pfade fertig sind |
| Typischer Fehler | Merge mit Synchronisation verwechseln | Fehlender Join führt zu unkontrolliert vervielfachtem Kontrollfluss |

> **IHK-Typfrage:** *"Warum kann ein fehlendes Join-Element in einem Aktivitätsdiagramm zu einem Fehler im modellierten System führen?"*
> **Musterantwort:** Ohne Join wird der nachfolgende Ablauf nicht auf die Beendigung aller parallelen Pfade synchronisiert – ein nachfolgender Schritt könnte starten, bevor alle notwendigen Vorgänger-Aktionen (z. B. alle drei parallelen Extraktionen) abgeschlossen sind. Je nach System kann das zu unvollständigen Ergebnissen, falscher Reihenfolge oder Race Conditions führen.

### 3.3 Partitionen (Swimlanes)

**Partitionen** gruppieren Aktionen danach, *wer oder was* sie ausführt – z. B. `Client`, `API Gateway`, `Datenbank`. Sie können vertikal oder horizontal gezeichnet werden und machen auf einen Blick sichtbar, an welchen Stellen Kommunikation zwischen Systemgrenzen nötig ist (z. B. zwischen Ingestion-Engine und Zieldatenbank in einer ETL-Pipeline).

---

## 4. ETL-Pipelines und Integrationsarchitekturen

> **Grundprinzip:** Es gibt zwei grundsätzlich verschiedene Strategien, heterogene Datenquellen nutzbar zu machen: Daten physisch kopieren und aufbereiten (ETL) oder sie an der Quelle belassen und zur Laufzeit abfragen (Virtualisierung).

### 4.1 Der ETL-Prozess

```text
 [ Extract ] ------------> [ Transform ] ------------> [ Load ]
 (Rohdaten lesen:          (Bereinigen, formatieren,    (In Zielsystem
  CSV, JSON, XML)           verknüpfen, normalisieren)   schreiben: SQL/NoSQL)
```

| Phase | Inhalt | IHK-Relevanz |
| --- | --- | --- |
| **Extract** | Rohdaten aus heterogenen Quellen lesen (CSV, verschachteltes JSON, relationale Legacy-Tabellen, XML) | 🔴 |
| **Transform** | Bereinigen und vereinheitlichen: Einheitenumrechnung, Datumsstandardisierung (ISO 8601), Deduplizierung, Schemaanpassung (z. B. Normalisierung für ein operatives Zielsystem **oder** bewusste Denormalisierung/Sternschema für analytische Abfragen), Ausreißerfilterung | 🔴 |
| **Load** | Bereinigte, vereinheitlichte Daten ins Zielsystem schreiben (z. B. PostgreSQL oder eine MongoDB-Collection) | 🔴 |

> Hinweis zur Aktualität: In modernen Cloud-Architekturen verschiebt sich der Ablauf teils zu **ELT** (Extract-Load-Transform) – Rohdaten werden zuerst geladen, die Transformation läuft dann direkt in leistungsfähigen Cloud-Data-Warehouses. Für die Grundlagenprüfung bleibt ETL das Referenzmodell.

### 4.2 Materialisierte vs. virtuelle Integration

| Kriterium | Materialisiert (Data Warehouse / Data Lake) | Virtuell (Data Virtualization) | IHK-Relevanz |
| --- | --- | --- | --- |
| Datenspeicherung | Physisch kopiert ins Zielsystem | Verbleibt in den Ursprungssystemen | 🔴 |
| Aktualität | Typischerweise nur periodisch aktuell, sofern klassisches Batch-ETL verwendet wird | Potenziell sehr aktuell, da zur Laufzeit aus den Quellen gelesen wird – tatsächliche Frische hängt aber von Caches, Replikationsverzögerungen und Quellsystemen ab | 🔴 |
| Abfrageperformance | Hoch (optimiert für Analysen) | Tendenziell geringer und stärker schwankend bei komplexen Abfragen über mehrere Quellen | 🔴 |
| Laufzeitlast auf Quellsysteme | Keine | Hoch, da jede Abfrage die Quellsysteme belastet | 🟡 |
| Speicherkosten | Hoch (Duplikation) | Keine zusätzliche Speicherung nötig | 🟡 |
| Datenqualität im Zielsystem | In der Regel höher (Bereinigung vor dem Laden) | Abhängig von Qualität der Quellsysteme zur Laufzeit | 🟡 |

**Data Warehouse vs. Data Lake** (beide materialisiert): Ein Data Warehouse ist auf strukturierte, relationale, SQL-basierte Analysen optimiert. Ein Data Lake speichert strukturierte, semi-strukturierte und unstrukturierte Daten meist in möglichst ursprünglicher Form (**Schema-on-Read**: das Schema wird erst bei der späteren Nutzung/Analyse angewendet, nicht zwingend beim Schreiben festgelegt).

> **IHK-Typfrage:** *"Warum kann Datenvirtualisierung aktuellere Daten liefern, leidet aber tendenziell bei großen Datenmengen unter schlechterer Abfrageperformance?"*
> **Musterantwort:** Da bei Virtualisierung keine Kopie existiert, greift jede Abfrage live auf die Originalquelle zu – Änderungen sind potenziell sofort sichtbar (die tatsächliche Frische hängt aber von Caches und Quellsystemen ab). Gleichzeitig muss die Middleware bei jeder Anfrage neu auf potenziell langsame oder viele Quellsysteme zugreifen und deren Ergebnisse zur Laufzeit zusammenführen, was bei großen Datenmengen tendenziell zu spürbaren Latenzen führt – im Gegensatz zu vorab optimierten, indizierten Kopien im Data Warehouse.

---

## 5. Big Data: die 5 Vs

> **Grundprinzip:** Klassische, einzelthread-basierte Pipelines und relationale Datenbanken stoßen an Grenzen, sobald eine oder mehrere der 5 Vs extrem ausgeprägt sind.

| V | Bedeutung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Volume** (Datenmenge) | Massives Datenvolumen | Terabyte bis Petabyte an täglichen Logdaten | 🔴 |
| **Variety** (Datenvielfalt) | Strukturierte, semi-strukturierte und unstrukturierte Formate gemischt | Tabellen, JSON/XML, Video/Audio/Text | 🔴 |
| **Velocity** (Geschwindigkeit) | Hohe Erzeugungs- und Verarbeitungsgeschwindigkeit | Echtzeit-Sensordatenströme (IoT) | 🔴 |
| **Veracity** (Glaubwürdigkeit) | Vertrauenswürdigkeit angesichts Rauschen, Fehlern, fehlenden Werten | Verrauschte Sensordaten mit Ausreißern | 🟡 |
| **Value** (Mehrwert) | Tatsächlicher geschäftlicher Nutzen aus den Analysen | Ableitung von Handlungsempfehlungen aus Massendaten | 🟢 |

**Skalierungsstrategien je nach V:** Die passende Maßnahme hängt davon ab, *welches* V das Problem verursacht – "einfach NoSQL nehmen" ist kein Automatismus, sondern eine von mehreren möglichen Antworten:

| Problem | Typische Maßnahmen | IHK-Relevanz |
| --- | --- | --- |
| Hohe **Volume** | Verteilte Speicherung/Partitionierung, Cluster, **MapReduce**-Batchverarbeitung (große Aufgabe in parallele "Map"-Schritte aufteilen, im "Reduce"-Schritt zusammenführen), ggf. NoSQL | 🟡 |
| Hohe **Velocity** | Message Broker/Event Streaming (z. B. MQTT als leichtgewichtiges IoT-Protokoll), Stream Processing, horizontale Skalierung – **nicht** primär MapReduce, das für Batch statt Echtzeit ausgelegt ist | 🟡 |
| Hohe **Variety** | Flexible Datenmodelle, Schema-on-Read, Data Lake | 🟢 |
| Niedrige **Veracity** | Validierung, Bereinigung, Quarantäne auffälliger Datensätze, kontinuierliches Monitoring | 🟡 |

Die Wahl zwischen relationalen und NoSQL-Systemen hängt zusätzlich von Konsistenzanforderungen und Abfragemustern ab, nicht allein vom Datenvolumen.

---

## 6. Typische Prüfungsfallen

Diese Verwechslungen tauchen in Prüfungen und Fachgesprächen erfahrungsgemäß immer wieder auf:

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Completeness = "Werte sind korrekt" | Completeness prüft nur, ob ein Wert *vorhanden* ist – nicht, ob er richtig oder gültig ist |
| 2 | Accuracy = Nachkommastellen-Genauigkeit (allgemein) | Nur im Kurskontext so definiert; in der Fachliteratur ist Accuracy meist gleichbedeutend mit Correctness (Realitätsnähe), nicht mit Precision |
| 3 | "40 Duplikate" ist eine eindeutige Zahl | Ohne Definition (zusätzliche Kopien? Datensatzpaare? Gruppen?) ist die Uniqueness-Berechnung nicht eindeutig – Definition immer aus der Aufgabenstellung übernehmen |
| 4 | Merge synchronisiert wie Join | Merge führt Pfade nur zusammen, **ohne** zu warten; nur Join wartet auf alle eingehenden Pfade |
| 5 | Technische und semantische Heterogenität werden vermischt | Unterschiedliches Dateiformat (technisch) ist etwas anderes als unterschiedliche Bedeutung/Einheit desselben Felds (semantisch) – ein Format-Konverter löst kein Bedeutungsproblem |
| 6 | ETL und ELT sind dasselbe | Reihenfolge und Ort der Transformation unterscheiden sich: ETL transformiert vor dem Laden, ELT lädt zuerst und transformiert danach im Zielsystem |
| 7 | Data Warehouse und Data Lake sind austauschbar | DWH: strukturiert, Schema-on-Write, analyseoptimiert. Data Lake: auch semi-/unstrukturiert, Schema-on-Read |
| 8 | Datenvirtualisierung ist automatisch "in Echtzeit" | Sie *ermöglicht* aktuelle Zugriffe, garantiert aber keine Echtzeit-Frische (Caches, langsame Quellsysteme) |
| 9 | MapReduce löst jedes Big-Data-Problem | MapReduce ist für Batch-Verarbeitung großer Volumina gedacht, nicht für Echtzeit-Velocity – dafür sind Streaming-Ansätze zuständig |

---

## 7. Deep-Dive-Ausblick (freiwillig)

Diese Themen vertiefen einzelne Kapitel dieses Artikels und sind für die Grundlagenprüfung nicht zwingend, aber gute Transferbasis für AP2/Fachgespräch:

- **Fuzzy-Match-Algorithmen** (→ Kapitel 1, Data Cleaning): Wie Levenshtein-Distanz oder Soundex helfen, Duplikate wie "Frank Miller" und "Frank Müller" als dieselbe Entität zu erkennen.
- **XSD und JSON Schema** (→ Kapitel 2.3, Ingestions-Formate): Wie XML- bzw. JSON-Payloads bereits vor der Verarbeitung formal gegen ein Schema validiert werden können.
- **Token-Flow-Semantik** (→ Kapitel 3, Aktivitätsdiagramme): Wie Tokens am Startknoten entstehen, durch Fork-Balken aufgeteilt und durch Join-Balken konsumiert werden – und wie ein Fork/Join-Ungleichgewicht zu einem "Token Trap" (dauerhaft wartender Join) führen kann.
- **ELT statt ETL** (→ Kapitel 4.1, ETL-Prozess): Wie moderne Cloud-Data-Warehouses (z. B. Snowflake, BigQuery) Rohdaten zuerst laden und die Transformation direkt in der Datenbank ausführen.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne zwei Datenqualitätsdimensionen, die *nicht* zu den 6 DAMA-Kerndimensionen gehören. | z. B. Non-redundancy, Relevancy, Reliability, Understandability, Accessibility |
| 2 | Warum muss Data Profiling vor Data Cleaning stattfinden? | Ohne Analyse der tatsächlichen Fehlerarten würden Bereinigungsregeln blind angewendet |
| 3 | Ein Datensatz hat 200 Zeilen, davon sind 15 zusätzliche Duplikat-Zeilen (185 eindeutig). Wie hoch ist die Uniqueness? | 185/200 × 100 = 92,5 % |
| 4 | Nenne ein Beispiel für semantische Heterogenität. | z. B. `price_net_eur` (Nettopreis, EUR) vs. `item_cost` (Einkaufspreis, USD) für verwandte, aber unterschiedliche Preisbegriffe |
| 5 | Welches Format bietet native Typsicherheit über XSD/JSON Schema hinaus am wenigsten? | CSV (keine formale Typprüfung vorgesehen) |
| 6 | Was unterscheidet einen Merge-Knoten strukturell von einem Join-Knoten? | Merge führt zusammen ohne zu warten; Join synchronisiert und wartet auf alle Pfade |
| 7 | Wofür stehen Partitionen/Swimlanes in einem Aktivitätsdiagramm? | Gruppierung von Aktionen nach ausführendem System/Akteur |
| 8 | Nenne die drei Phasen von ETL in der richtigen Reihenfolge. | Extract → Transform → Load |
| 9 | Welcher Integrationsansatz hat höhere Datenaktualität, aber schlechtere Performance bei großen Datenmengen? | Virtuelle Integration (Data Virtualization) |
| 10 | Welches der 5 Vs beschreibt die Vertrauenswürdigkeit der Daten? | Veracity |
| 11 | Warum ist MapReduce für hohe Velocity (Echtzeitströme) weniger geeignet als für hohes Volume? | MapReduce ist auf Batch-Verarbeitung großer, bereits vorliegender Datenmengen ausgelegt; für Echtzeitanforderungen sind Stream-Processing/Message-Broker-Ansätze passender |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Completeness** | Anteil der Pflichtfelder mit vorhandenem (nicht fehlendem) Wert – Gültigkeit ist eine separate Frage |
| **Uniqueness** | Jede reale Entität kommt nur einmal im Datensatz vor |
| **Data Profiling** | Analysephase: Muster/Anomalien in Rohdaten entdecken |
| **Data Decay** | Schleichender Aktualitätsverlust von Daten über die Zeit |
| **Technische Heterogenität** | Unterschiedliche Zugriffsschnittstellen/Dateiformate |
| **Semantische Heterogenität** | Unterschiedliche Bedeutung, Einheit oder fachliche Interpretation – unterschiedliche Benennung kann ein Hinweis sein, ist aber nicht zwingend |
| **Fork/Join** | Nebenläufige Ausführung mehrerer Pfade + Synchronisationspunkt (Join wartet auf alle) |
| **Decision/Merge** | Genau ein Pfad wird gewählt, später ohne Wartezeit zusammengeführt |
| **ETL** | Daten extrahieren, transformieren und ins Zielsystem laden – dabei entsteht meist eine materialisierte (physische) Integration |
| **Data Virtualization** | Logische Integration: Abfrage der Quellen zur Laufzeit ohne Kopie |
| **5 Vs** | Volume, Variety, Velocity, Veracity, Value |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Berechnung | "Berechnen Sie Completeness/Uniqueness für …" | Korrekte Formel **und** Rechenweg, nicht nur das Endergebnis |
| Begriffsabgrenzung | "Erläutern Sie den Unterschied zwischen X und Y" | Klare Trennung + konkretes Beispiel, keine Synonym-Behandlung |
| Architekturentscheidung | "Welche Integrationsstrategie empfehlen Sie und warum?" | Abwägung mit mind. zwei Kriterien (z. B. Aktualität vs. Performance), begründete Entscheidung |
| Diagrammlesen/-zeichnen | "Modellieren Sie den Ablauf als Aktivitätsdiagramm" | Korrekte Notation (Fork/Join vs. Decision/Merge), sinnvolle Partitionierung |
| Transferfrage | "Wie würden Sie das System bei 1000-facher Datenmenge anpassen?" | Konkrete, zum betroffenen V passende Maßnahme benennen (z. B. MapReduce/Partitionierung bei Volume, Stream Processing bei Velocity), nicht nur "mehr Server" |

---

## 11. Merksätze für das Fachgespräch

> Datenqualität ist keine Meinung, sondern eine Prozentzahl – jede Dimension braucht eine Formel oder ein klares Kriterium.

> Heterogenität hat drei Ebenen: Technik, Struktur, Bedeutung – ein Format-Fix löst nicht automatisch ein Namens- oder Schemaproblem.

> Fork/Join heißt "alle nebenläufig, dann warten" – Decision/Merge heißt "nur einer, dann sofort weiter".

> ETL kopiert und bereinigt, Virtualisierung lässt die Daten dort, wo sie sind – die Wahl ist immer ein Kompromiss zwischen Aktualität und Performance.

> Die 5 Vs sind kein Selbstzweck – stark ausgeprägte Vs können dazu führen, dass ein Einzelserver-Skript durch skalierbare, verteilte Verarbeitung ergänzt oder ersetzt werden muss.

---

```yaml
dokument: LF8.3-wiki-artikel
lernfeld: LF8.3
titel: "Datenqualität, heterogene Datenintegration & ETL-Pipelines"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-04
quellen_intern:
  - "LF8.3.1: Data Quality Metrics & Evaluation.md"
  - "LF8.3.2: Heterogeneous Data Ingestion & Open Data.md"
  - "LF8.3.3: UML 2.0 Activity Diagrams.md"
  - "LF8.3.4: ETL Data Pipelines & Big Data Concepts.md"
quellen_fachlich:
  - titel: "DAMA-DMBOK2 (Data Management Body of Knowledge)"
    herausgeber: "DAMA International"
    status: "Fachrahmenwerk, in vielen Ausgaben werden sechs häufig verwendete Kerndimensionen genannt"
  - titel: "OMG Unified Modeling Language Specification 2.5.1"
    herausgeber: "Object Management Group (OMG)"
    status: "formale Spezifikation, 2017, weiterhin aktuell (Stand 2026)"
  - titel: "ISO 8601-1:2019 (Datums-/Zeitformat)"
    herausgeber: "ISO"
    status: "internationaler Standard, aktuelle Ausgabe"
  - titel: "The Data Warehouse Toolkit"
    autoren: "Kimball/Ross"
    status: "ETL-Referenzwerk"
review_historie:
  - runde: 1
    datum: 2026-09-04
    ergebnis: "Fachliche Nachschärfung: Completeness/Validity, Accuracy/Precision, Uniqueness-Annahmen, Heterogenitäts-Beispiel, Open-Data-Lizenzaspekt, Data-Lake/Schema-on-Read, MapReduce vs. Streaming präzisiert"
  - runde: 2
    datum: 2026-09-04
    ergebnis: "Style-Guide-Checkliste gegengeprüft: fehlenden Pflichtabschnitt 'Typische Prüfungsfallen' ergänzt, fehlenden Deep-Dive-Ausblick mit Kapitel-Rückverweisen ergänzt, Cheatsheet-Inkonsistenz Fork/Join behoben, Validity-Lücke im 12-Dimensionen-Modell explizit gemacht statt in Correctness versteckt"
  - runde: 3
    datum: 2026-09-04
    ergebnis: "Feinschliff: Accuracy-Widerspruch zwischen Tabelle und Fußnote direkt in der Tabellenzelle aufgelöst, DAMA-Aussage vorsichtiger formuliert, Closed-Data/CSV/DWH-Aussagen entschärft, Kapitelüberschrift UML an Textinhalt (2.5.1) angeglichen, Cheatsheet-Einträge Semantik/ETL präzisiert, Merksatz Einzelserver entschärft, ISO-8601-Ausgabejahr ergänzt"
freigabe: "Final gesetzt nach 3 Review-Runden (2026-09-04) – Freigabe durch Autor:in bestätigt"
```