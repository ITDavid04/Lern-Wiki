# AP2-Übungsblatt (Anwendungsentwicklung) – Planen eines Softwareproduktes

> **Zielgruppe:** Umschülerinnen und Umschüler sowie Auszubildende zum/zur Fachinformatiker/in Anwendungsentwicklung
> **Zweck:** Zweites Übungsblatt zur Vorbereitung auf Teil 2 der Abschlussprüfung, neben [AP2_Aufgaben.md](AP2_Aufgaben.md) (Prüfungsbereich „Entwicklung und Umsetzung von Algorithmen“). Dieses Blatt behandelt den Prüfungsbereich „Planen eines Softwareproduktes“. Lösungen: [AP2.2_Lösungen_AUFPLanenen.md](AP2.2_Lösungen_AUFPLanenen.md).
> **Status:** Final
> **Stand:** 2026-09-28
>
> **Hinweis zum Format:** Der Prüfungsbereich dauert 90 Minuten, die Aufgaben sind praxisbezogen und schriftlich zu bearbeiten (§ 13 FIAusbV). Dieses Übungsblatt umfasst 100 Punkte, verteilt auf vier Szenario-Aufgaben zu je 25 Punkten. Es orientiert sich strukturell an den vier Nachweisen, die § 13 FIAusbV nennt: Entwicklungsumgebungen und -bibliotheken auswählen und einsetzen, Programmspezifikationen anwendungsgerecht festlegen, Bedienoberflächen funktionsgerecht und ergonomisch konzipieren, Maßnahmen zur Qualitätskontrolle planen und durchführen. Der Prüfungskatalog für diesen Bereich lag bei der Erstellung nicht vor. Aufgabenzahl, Punkteverteilung und Aufgabenformate der echten Prüfung können deshalb abweichen; eine 1:1-Simulation ist das Blatt nicht. Zeichenaufgaben (Wireframe, Diagramme) dienen der Übung und sagen nichts darüber aus, dass sie in dieser Form in der echten Prüfung verlangt werden. Der Umfang ist für eine Übung bewusst dicht; im Übungsdurchlauf ist es normal, mehr als 90 Minuten zu brauchen.
>
> **Hinweis:** Ausgangssituation, Firmennamen, Daten und Aufgaben sind frei erfunden. Keine Aufgabe ist einer realen Prüfung entnommen oder nachgebildet.

---

## Bearbeitungshinweise

- Bearbeitungszeit: 90 Minuten, Gesamtpunktzahl: 100 Punkte (Richtwert: etwa 20 bis 22 Minuten je Aufgabe)
- Lesen Sie den Text der Aufgaben ganz durch, bevor Sie mit der Bearbeitung beginnen.
- Stichwortartige Antworten sind zulässig, sofern nicht ausdrücklich ganze Sätze verlangt werden.
- Halten Sie sich beim Umfang der Antwort an die Vorgabe der Aufgabenstellung. Werden zwei Angaben gefordert und Sie führen vier an, zählen nur die ersten zwei.
- Diagramme und Skizzen fertigen Sie auf einem eigenen Blatt an. Auf künstlerische Qualität kommt es nicht an, wohl aber auf die Vollständigkeit der geforderten Elemente.
- Erlaubtes Hilfsmittel in diesem Übungsblatt: nicht programmierbarer, netzunabhängiger Taschenrechner ohne Kommunikationsmöglichkeit mit Dritten. In der echten Prüfung gelten die Angaben in Einladung und Prüfungsunterlagen.

---

## Ausgangssituation

Sie arbeiten bei der **Deichsoft Entwicklung GmbH**. Für die Kletterhalle **Nordwand** entwickeln Sie die Smartphone-App **NordwandBook**:

- Mitglieder buchen Plätze in Kursen und Zeitfenstern.
- Trainerinnen und Trainer legen Kurse an und sagen sie ab.
- Ist ein Kurs voll, wird den Mitgliedern die Warteliste angeboten.
- Beim Betreten der Halle wird der Eintritt per QR-Code eingecheckt.
- Für Kursbuchungen muss immer ein Zahlungsweg gewählt werden.

Die Deichsoft GmbH möchte die App später auch an weitere Kletterhallen verkaufen. Der Quellcode soll dabei nicht offengelegt werden.

Bearbeiten Sie die folgenden Aufgaben:

- Werkzeuge und Bibliotheken auswählen und einsetzen
- Anforderungen und Programmspezifikation festlegen
- Die Bedienoberfläche konzipieren
- Die Qualität kontrollieren

---

## 1. Aufgabe (25 Punkte)

**a)** Für den QR-Code-Check-in soll eine Bibliothek eingesetzt werden. Drei Bibliotheken stehen zur Auswahl. **7 Punkte**

| | QuickScan | CodeReader Pro | ScanKit |
|---|---|---|---|
| Lizenz | MIT-Lizenz | proprietär (kommerziell) | GPL-3.0 |
| Kosten | kostenlos | 1 200 EUR pro Jahr | kostenlos |
| Pflege | letzte Version vor 2 Monaten | aktiv, Support-Hotline | sehr aktiv |
| Dokumentation | ausführlich | ausführlich | knapp |
| Erkennungsgeschwindigkeit | gut | gut | sehr gut |

- aa) Nennen Sie zwei Kriterien, die Sie außer den Kosten bei der Auswahl einer Bibliothek prüfen sollten. *(2 Punkte)*
- ab) Erklären Sie das Copyleft-Prinzip der GPL und beschreiben Sie, was es für den Einsatz von ScanKit in der App bedeutet. *(3 Punkte)*
- ac) Für welche Bibliothek entscheiden Sie sich? Begründen Sie Ihre Entscheidung. *(2 Punkte)*

**b)** Sie entwickeln die QR-Code-Funktion in einem eigenen Zweig (Branch). Sie beginnen auf dem aktuellen Stand des Hauptzweigs. Die folgenden Schritte sind durcheinander aufgelistet. **8 Punkte**

| Kennung | Schritt |
|---|---|
| a | `git add .` |
| b | Pull Request erstellen und Review abwarten |
| c | `git switch -c feature/qr-checkin` |
| d | Code ändern und lokal testen |
| e | `git push -u origin feature/qr-checkin` |
| f | `git commit -m "QR-Check-in ergänzt"` |

- ba) Bringen Sie die Schritte in die richtige Reihenfolge. Tragen Sie die Kennungen ein: ______ → ______ → ______ → ______ → ______ → ______ *(6 Punkte, je Schritt an richtiger Position 1 Punkt)*
- bb) Warum arbeitet man an einer neuen Funktion in einem eigenen Zweig und nicht direkt im Hauptzweig? *(2 Punkte)*

**c)** **10 Punkte**

- ca) Ein Kollege sagt: „Bei mir läuft die App aber.“ Nennen Sie zwei Maßnahmen, mit denen alle Entwickelnden dieselbe Entwicklungsumgebung verwenden, und erklären Sie jeweils kurz die Wirkung. *(4 Punkte)*
- cb) Die eingesetzte Bibliothek ist in Version 2.4.1 eingebunden. Nun erscheint Version 3.0.0. Was bedeutet die Änderung der ersten Ziffer bei semantischer Versionierung, und wie gehen Sie mit dem Update um? *(3 Punkte)*
- cc) Nennen Sie drei Funktionen eines Debuggers. *(3 Punkte)*

---

## 2. Aufgabe (25 Punkte)

**a)** Ordnen Sie die Aussagen den Anforderungsarten „funktional“ oder „nicht funktional“ zu. **5 Punkte**

| Nr. | Aussage | Anforderungsart |
|---:|---|---|
| 1 | Mitglieder können einen Kurs buchen. | |
| 2 | Die Kursliste lädt bei 200 gleichzeitigen Nutzern in höchstens 2 Sekunden. | |
| 3 | Trainerinnen und Trainer können Kurse anlegen und absagen. | |
| 4 | Passwörter werden nicht im Klartext, sondern als gesalzene Hashwerte gespeichert. | |
| 5 | Nach einer Buchung wird automatisch eine Bestätigungs-E-Mail versendet. | |

**b)** Der Funktionsumfang der App soll mit einem UML-Anwendungsfalldiagramm beschrieben werden. **8 Punkte**

- ba) Nennen Sie die beiden Akteure der App und zu jedem Akteur einen Anwendungsfall, den nur dieser Akteur auslöst. *(4 Punkte)*
- bb) Erklären Sie die Beziehungen `«include»` und `«extend»`. Ordnen Sie ihnen die folgenden beiden Sachverhalte zu: (1) „Beim Buchen muss immer ein Zahlungsweg gewählt werden.“ (2) „Ist der Kurs voll, wird zusätzlich die Warteliste angeboten.“ *(4 Punkte)*

**c)** Für die Buchungsverwaltung ist ein Klassendiagramm mit den Klassen **Mitglied** (mitgliedsnr, name, email), **Kurs** (kursnr, titel, datum, maxPlaetze) und **Buchung** (buchungsnr, zeitpunkt, status) geplant. Ein Mitglied kann beliebig viele Buchungen haben. Jede Buchung gehört zu genau einem Mitglied und zu genau einem Kurs. Ein Kurs kann beliebig viele Buchungen haben. **6 Punkte**

- ca) Geben Sie die Multiplizitäten an den vier Enden der beiden Beziehungen Mitglied–Buchung und Kurs–Buchung an. *(4 Punkte)*
- cb) Das Attribut `maxPlaetze` (Ganzzahl) soll nur innerhalb der Klasse Kurs sichtbar sein. Die Methode `istVoll()` (liefert einen Wahrheitswert) soll öffentlich sein. Notieren Sie beide Einträge in UML-Notation. *(2 Punkte)*

**d)** **6 Punkte**

- da) Erklären Sie den Unterschied zwischen Lastenheft und Pflichtenheft. *(3 Punkte)*
- db) Im Lastenheft steht die Anforderung „Die App soll schnell sein.“ Formulieren Sie sie als messbares Kriterium und nennen Sie ein weiteres Merkmal einer guten Anforderung. *(3 Punkte)*

---

## 3. Aufgabe (25 Punkte)

**a)** Ordnen Sie den Beispielen jeweils das passende Interaktionsprinzip der DIN EN ISO 9241-110 zu. Tragen Sie den Namen aus der folgenden Liste ein: Aufgabenangemessenheit, Selbstbeschreibungsfähigkeit, Steuerbarkeit, Erwartungskonformität, Fehlertoleranz, Individualisierbarkeit, Lernförderlichkeit. **5 Punkte**

*Hinweis: Die Aufgabe verwendet bewusst die aus älteren Lehrmaterialien bekannten Bezeichnungen der Norm vor der Überarbeitung von 2020. Die aktuelle Fassung DIN EN ISO 9241-110:2020 benennt einzelne Prinzipien anders oder anders zusammengefasst (z. B. „Robustheit gegen Benutzungsfehler“ statt „Fehlertoleranz“). Beide fachlich entsprechenden Bezeichnungen werden gewertet. Es kommt auf das Verständnis der Prinzipien an, nicht auf das Auswendiglernen einer bestimmten Namensliste.*

| Nr. | Beispiel | Prinzip |
|---:|---|---|
| 1 | Im Datumsfeld steht als Hilfe „TT.MM.JJJJ“. | |
| 2 | Die Buchung kann an jeder Stelle abgebrochen und ein Schritt zurückgegangen werden. | |
| 3 | Der Zurück-Pfeil oben links führt zur vorherigen Ansicht, wie in den meisten anderen Apps. | |
| 4 | Bei einer falsch geschriebenen E-Mail-Adresse erscheint ein verständlicher Hinweis mit Korrekturvorschlag, die übrigen Eingaben bleiben erhalten. | |
| 5 | Das Buchungsformular fragt nur die Angaben ab, die für die Buchung nötig sind. | |

**b)** Die App soll auch für Menschen mit Einschränkungen nutzbar sein. Nennen Sie drei geeignete Maßnahmen. **3 Punkte**

**c)** Skizzieren Sie auf einem eigenen Blatt ein Wireframe der Ansicht „Kursliste“ für das Smartphone. Die Ansicht soll folgende Elemente enthalten: **6 Punkte**

- eine Kopfzeile mit Titel
- eine Filterfunktion (nach Datum oder Kurstyp)
- eine Liste der Kurse, je Eintrag mit Titel, Uhrzeit und Zahl der freien Plätze
- je Kurs mit freien Plätzen eine Schaltfläche zum Buchen
- für ausgebuchte Kurse eine erkennbar andere Darstellung (z. B. mit Angebot der Warteliste)
- eine Navigationsleiste

*(je Element 1 Punkt)*

**d)** **6 Punkte**

- da) Welches Bedienelement verwenden Sie jeweils? Wählen Sie aus: Radiobuttons, Checkboxen, Dropdown-Liste, Datumsauswahl. *(4 Punkte)*
  1. Genau einer von drei Zahlungswegen muss gewählt werden.
  2. Mehrere Zusatzleistungen (Leihschuhe, Gurt, Magnesia) können gewählt werden.
  3. Das Land soll aus einer Liste von 40 Ländern gewählt werden.
  4. Das Geburtsdatum soll eingegeben werden.
- db) Nennen Sie zwei Regeln, die eine gute Fehlermeldung im Buchungsformular erfüllen sollte. *(2 Punkte)*

**e)** Vor der Umsetzung soll ein Prototyp der Oberfläche erstellt werden. **5 Punkte**

- ea) Erklären Sie den Unterschied zwischen einem Low-Fidelity- und einem High-Fidelity-Prototyp. *(2 Punkte)*
- eb) Nennen Sie zwei Vorteile eines frühen Prototyps. *(2 Punkte)*
- ec) Wer sollte den Prototyp testen? *(1 Punkt)*

---

## 4. Aufgabe (25 Punkte)

**a)** Ordnen Sie den Aussagen das passende Qualitätsmerkmal zu. Wählen Sie aus: Funktionalität, Effizienz, Zuverlässigkeit, Wartbarkeit, Sicherheit, Benutzbarkeit. **4 Punkte**

*Hinweis: Es handelt sich um eine vereinfachte, in der IT-Ausbildung häufig verwendete Auswahl von Qualitätsmerkmalen in gebräuchlicher deutscher Benennung, angelehnt an das Qualitätsmodell der ISO/IEC 25010. Die aktuelle Fassung der Norm (2023) umfasst neun Merkmale und benennt einzelne anders, z. B. Benutzbarkeit als „Interaction Capability“. Sinngemäß gleichwertige Bezeichnungen werden gewertet.*

| Nr. | Aussage | Qualitätsmerkmal |
|---:|---|---|
| 1 | Fällt der Server aus, stellt das System nach dem Neustart alle bestätigten Buchungen wieder her. | |
| 2 | Neue Kurstypen lassen sich mit geringem Aufwand ergänzen, ohne den restlichen Code umzubauen. | |
| 3 | Nur Trainerinnen und Trainer dürfen Kurse löschen. | |
| 4 | Die Kursliste lädt auch bei 200 gleichzeitigen Nutzern in unter 2 Sekunden. | |

**b)** Ordnen Sie den Beschreibungen die passende Teststufe zu. Wählen Sie aus: Modultest, Integrationstest, Systemtest, Abnahmetest. **4 Punkte**

| Nr. | Beschreibung | Teststufe |
|---:|---|---|
| 1 | Die Methode `istVoll()` wird isoliert getestet. | |
| 2 | Das Zusammenspiel von App-Server und Datenbank wird geprüft. | |
| 3 | Die komplette App wird in einer produktionsnahen Umgebung gegen die Gesamtanforderungen geprüft. | |
| 4 | Die Kletterhalle prüft die App vor der Übernahme anhand ihrer eigenen Anforderungen. | |

**c)** Für die Buchungsfunktion gilt: Buchen ist möglich, solange freie Plätze vorhanden sind. Ist der Kurs voll, wird die Warteliste angeboten. Kurse in der Vergangenheit können nicht gebucht werden, es erscheint eine Fehlermeldung. Erstellen Sie drei Testfälle: einen Normalfall, einen Grenzfall und einen Fehlerfall. **6 Punkte**

| Nr. | Art | Vorbedingung | Aktion | erwartetes Ergebnis |
|---:|---|---|---|---|
| 1 | Normalfall | | | |
| 2 | Grenzfall | | | |
| 3 | Fehlerfall | | | |

*(je Testfall 2 Punkte: 1 Punkt für eine sinnvolle Vorbedingung und Aktion, 1 Punkt für das richtige erwartete Ergebnis)*

**d)** **6 Punkte**

- da) Nennen Sie zwei Maßnahmen der analytischen Qualitätssicherung, die ohne Ausführen des Programms auskommen. *(2 Punkte)*
- db) Nennen Sie einen Vorteil eines Code-Reviews. *(2 Punkte)*
- dc) In der „Definition of Done“ des Teams sollen Qualitätskriterien stehen. Nennen Sie zwei geeignete Kriterien. *(2 Punkte)*

**e)** Nach einer Fehlerbehebung werden die vorhandenen Tests erneut ausgeführt. **5 Punkte**

- ea) Wie heißt dieses Vorgehen? *(1 Punkt)*
- eb) Warum ist es sinnvoll? *(2 Punkte)*
- ec) Warum sollte es automatisiert werden? *(2 Punkte)*

---

## Punkteübersicht

| Aufgabe | Thema | Punkte |
|---|---|---:|
| 1 | Entwicklungsumgebung und Bibliotheken | 25 |
| 2 | Anforderungen und Programmspezifikation | 25 |
| 3 | Bedienoberfläche | 25 |
| 4 | Qualitätskontrolle | 25 |
| | **Gesamt** | **100** |

*Lösungen siehe separates Lösungsblatt.*