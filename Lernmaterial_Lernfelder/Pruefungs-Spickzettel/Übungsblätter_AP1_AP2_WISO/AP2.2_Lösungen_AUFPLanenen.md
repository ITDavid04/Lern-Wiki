# AP2-Übungsblatt (Anwendungsentwicklung) – Planen eines Softwareproduktes – Lösungen

> **Zugehörig zu:** [AP2_AUfgabenBlatt_Planen.md](AP2_AUfgabenBlatt_Planen.md)
> **Status:** Final
> **Stand:** 2026-09-28
>
> Musterlösungen mit Punktevergabe. Bei Freitext-, Zeichen- und Diagrammaufgaben sind sinngemäß gleichwertige, fachlich richtige Lösungen ebenfalls zu werten. Es genügt jeweils die geforderte Anzahl an Nennungen. Folgefehler werden berücksichtigt: Wurde mit einem falschen Wert aus einem früheren Unterpunkt korrekt weitergearbeitet, sind die Punkte zu vergeben.

**Orientierungswert (Punkte-Noten-Schlüssel):** 100–92 Punkte = Note 1 · 91–81 = Note 2 · 80–67 = Note 3 · 66–50 = Note 4 · 49–30 = Note 5 · 29–0 = Note 6. Der Schlüssel kann je nach IHK bzw. Prüfung abweichen und ist nicht Bestandteil der echten AP2-Bewertung.

---

## 1. Aufgabe (25 Punkte)

**a) Auswahl der Bibliothek (7 Punkte)**

- **aa)** Zwei Kriterien (je 1 Punkt): Lizenz und deren Vereinbarkeit mit dem Verwendungszweck; Pflege und Aktualität (regelmäßige Updates, Sicherheitskorrekturen); Qualität der Dokumentation; Community bzw. Support; Kompatibilität mit den eingesetzten Plattformen; Größe und Zahl der Abhängigkeiten; Leistungsfähigkeit; bekannte Sicherheitslücken.
- **ab)** *(3 Punkte)*
  - **Copyleft-Prinzip:** Der Code darf genutzt, verändert und weitergegeben werden, aber abgeleitete Werke müssen bei Weitergabe wieder unter denselben Lizenzbedingungen stehen, also mit Quellcode zugänglich sein. *(1 Punkt)*
  - **Folge für ScanKit:** Bei einer für die GPL relevanten Einbindung in die App kann die Weitergabe der daraus entstehenden Gesamtsoftware den GPL-Pflichten unterliegen, insbesondere der Pflicht zur Bereitstellung des Quellcodes. *(1 Punkt)*
  - **Bewertung:** Das widerspricht dem Ziel, den Quellcode nicht offenzulegen. ScanKit ist für das Vorhaben deshalb ungeeignet oder nur nach rechtlicher Prüfung nutzbar. *(1 Punkt)*
- **ac)** Empfehlung: **QuickScan** (die MIT-Lizenz erlaubt die Nutzung auch in proprietärer Software, kostenlos, ausführlich dokumentiert, gepflegt). Alternativ **CodeReader Pro**, wenn der Support wichtiger ist als die Kosten. *(1 Punkt für eine lizenzverträgliche Entscheidung, 1 Punkt für die schlüssige Begründung.)* ScanKit widerspricht der in der Ausgangssituation ausdrücklich genannten Bedingung, dass der Quellcode nicht offengelegt werden soll; eine bloße Abwägung ("die Geschwindigkeit ist es wert") reicht deshalb nicht aus. Wer ScanKit trotzdem wählt, erhält die Punkte nur, wenn die Antwort eine zusätzliche, mit der GPL vereinbare Lösung nennt (z. B. eine separate kommerzielle Lizenz beim Hersteller einholen, sofern angeboten) oder ausdrücklich klarstellt, dass sich die Geschäftsentscheidung der Deichsoft GmbH damit ändern würde.

Hinweis: Die Bewertung des Copyleft-Effekts dient der Prüfungsvorbereitung und ersetzt keine Rechtsberatung. Wann genau ein abgeleitetes Werk vorliegt, hängt von der Art der Einbindung ab.

**b) Git-Ablauf (8 Punkte)**

- **ba)** Richtige Reihenfolge: **c → d → a → f → e → b** *(je Schritt an richtiger Position 1 Punkt, gesamt 6 Punkte)*
  1. c: Zweig anlegen und wechseln
  2. d: Code ändern und lokal testen
  3. a: Änderungen für den Commit vormerken (`git add`)
  4. f: Commit erstellen
  5. e: Zweig zum Server hochladen (`git push -u`)
  6. b: Pull Request erstellen und Review abwarten

  Hinweis: `git checkout -b feature/qr-checkin` ist gleichwertig zu `git switch -c`. Ein `push` vor dem Commit würde nichts Neues übertragen, weil erst der Commit die Änderungen im Verlauf festhält.
- **bb)** Zwei Gründe (je 1 Punkt): Der Hauptzweig bleibt stabil und lauffähig. Mehrere Funktionen können parallel entwickelt werden, ohne sich zu stören. Die Änderungen können per Review geprüft werden, bevor sie zusammengeführt werden. Änderungen lassen sich einfacher zurücknehmen oder verwerfen.

**c) Umgebung, Versionen, Debugger (10 Punkte)**

- **ca)** Zwei Maßnahmen mit Wirkung (je 2 Punkte: 1 Punkt Maßnahme, 1 Punkt Wirkung) *(4 Punkte)*:
  - Virtuelle Umgebung oder Container: isolierte, reproduzierbare Umgebung für alle.
  - Abhängigkeitsdatei mit fixierten Versionen (z. B. `requirements.txt` oder Lock-Datei): alle verwenden dieselben Bibliotheksversionen.
  - Gemeinsame Konfiguration und Einrichtungsanleitung (Setup-Skript, README): einheitliche Einrichtung ohne Handarbeit.
  - Festgelegte Versionen von Interpreter und Werkzeugen: gleiches Verhalten bei allen.
- **cb)** *(3 Punkte)*
  - Semantische Versionierung hat die Form MAJOR.MINOR.PATCH. Eine Änderung der ersten Ziffer (MAJOR) signalisiert eine **nicht abwärtskompatible Änderung** der öffentlichen Schnittstelle. Das bedeutet nicht zwingend, dass die eigene Anwendung betroffen ist – das hängt davon ab, ob die genutzten Funktionen der Schnittstelle geändert wurden. *(1 Punkt)*
  - Das Update nicht ungeprüft einspielen, sondern zuerst Änderungsprotokoll bzw. Migrationshinweise lesen. *(1 Punkt)*
  - Den Code bei Bedarf anpassen und das Update in einem eigenen Zweig mit den vorhandenen Tests prüfen, bevor es übernommen wird. *(1 Punkt)*

  Zur Einordnung: `2.4.2` wäre nur eine Fehlerkorrektur, `2.5.0` eine kompatible neue Funktion.
- **cc)** Drei Funktionen (je 1 Punkt): Haltepunkte setzen (auch bedingt); Programm schrittweise ausführen (Einzelschritt, in Funktionen hineinspringen); Variablenwerte beobachten oder ändern; Aufrufstapel anzeigen.

---

## 2. Aufgabe (25 Punkte)

**a) Anforderungsarten (5 Punkte, je 1 Punkt)**

| Nr. | Anforderungsart |
|---:|---|
| 1 | funktional |
| 2 | nicht funktional (Leistung bzw. Effizienz) |
| 3 | funktional |
| 4 | nicht funktional (Sicherheit) |
| 5 | funktional |

Funktionale Anforderungen beschreiben, **was** das System tun soll. Nicht funktionale Anforderungen beschreiben, **wie gut** oder unter welchen Bedingungen es das tun soll (z. B. Leistung, Sicherheit, Zuverlässigkeit, Bedienbarkeit). Zu Nr. 4: Passwörter werden nicht verschlüsselt, sondern mit einem gesalzenen Hashverfahren gespeichert, weil sie sich nie wieder entschlüsseln lassen müssen; das ist eine Sicherheitsanforderung.

**b) Anwendungsfalldiagramm (8 Punkte)**

- **ba)** Akteure: **Mitglied** und **Trainer bzw. Trainerin** *(je 1 Punkt)*. Anwendungsfälle nur für diesen Akteur *(je 1 Punkt)*: Mitglied: Kurs buchen oder Warteliste nutzen. Trainer: Kurs anlegen oder Kurs absagen. Wer den QR-Code-Check-in in der Halle auslöst (Mitglied selbst oder Personal am Eingang), legt die Ausgangssituation nicht eindeutig fest; als Antwort für „Mitglied“ wird es dennoch gewertet, ein Zahlungsdienstleister wäre allenfalls ein externes System bzw. sekundärer Akteur und wird hier nicht gefordert.
- **bb)** *(4 Punkte)*
  - `«include»`: Der eingebundene Anwendungsfall wird **immer** mit ausgeführt, er ist Pflichtbestandteil. *(1 Punkt)*
  - `«extend»`: Der erweiternde Anwendungsfall wird nur **optional** und unter einer Bedingung ausgeführt. *(1 Punkt)*
  - Sachverhalt (1): **include**, „Zahlungsweg wählen“ ist immer Teil von „Kurs buchen“. *(1 Punkt)*
  - Sachverhalt (2): **extend**, „Warteliste anbieten“ erweitert „Kurs buchen“ nur, wenn der Kurs voll ist. *(1 Punkt)*

  Pfeilrichtung: Bei `«include»` zeigt der Pfeil vom Basisanwendungsfall zum eingebundenen („Kurs buchen“ → „Zahlungsweg wählen“). Bei `«extend»` zeigt er vom erweiternden zum Basisanwendungsfall („Warteliste anbieten“ → „Kurs buchen“).

**c) Klassendiagramm (6 Punkte)**

- **ca)** *(je Ende 1 Punkt, gesamt 4 Punkte)*

| Beziehung | Multiplizität am Ende der zuerst genannten Klasse | Multiplizität am Ende der Klasse Buchung |
|---|---|---|
| Mitglied – Buchung | Mitglied: **1** | Buchung: **0..\*** |
| Kurs – Buchung | Kurs: **1** | Buchung: **0..\*** |

Hinweis: „Beliebig viele“ schließt null ein. Die Angabe `1..*` wäre falsch, weil ein Mitglied oder ein Kurs auch ohne Buchung existieren kann. `*` ist als Kurzschreibweise für `0..*` zulässig.

- **cb)** `- maxPlaetze: int` (das Minuszeichen kennzeichnet `private`) *(1 Punkt)* und `+ istVoll(): boolean` (das Pluszeichen kennzeichnet `public`) *(1 Punkt)*.

**d) Lastenheft, Pflichtenheft und Anforderungsqualität (6 Punkte)**

- **da)** *(3 Punkte)*
  - **Lastenheft:** Wird typischerweise vom Auftraggeber erstellt und beschreibt, **was** die Software leisten soll und wofür (Anforderungen aus Sicht des Auftraggebers). *(1 Punkt)*
  - **Pflichtenheft:** Wird typischerweise vom Auftragnehmer erstellt und beschreibt, **wie und womit** die Anforderungen umgesetzt werden (Lösungskonzept, technische Umsetzung). *(1 Punkt)*
  - Das Pflichtenheft baut auf dem Lastenheft auf, wird mit dem Auftraggeber abgestimmt und dient als Grundlage der Umsetzung und der Abnahme. *(1 Punkt)*
- **db)** *(3 Punkte)* Beispiel: „Die Kursliste wird auf einem Smartphone der mittleren Geräteklasse (z. B. 4 GB RAM) über eine LTE-Verbindung bei 200 gleichzeitigen Nutzern in höchstens 2 Sekunden vollständig angezeigt.“ *(1 Punkt für eine Messgröße, 1 Punkt für einen Grenzwert, 1 Punkt für eine Randbedingung wie Testgerät oder Netzbedingung.)* Weiteres Merkmal einer guten Anforderung *(1 Punkt)*: eindeutig, prüfbar bzw. testbar, vollständig, widerspruchsfrei, realisierbar, verständlich, nachverfolgbar.

---

## 3. Aufgabe (25 Punkte)

**a) Interaktionsprinzipien (5 Punkte, je 1 Punkt)**

| Nr. | Prinzip |
|---:|---|
| 1 | Selbstbeschreibungsfähigkeit |
| 2 | Steuerbarkeit |
| 3 | Erwartungskonformität |
| 4 | Fehlertoleranz (Fassung 2020: Robustheit gegen Benutzungsfehler) |
| 5 | Aufgabenangemessenheit |

Individualisierbarkeit und Lernförderlichkeit sind in dieser Aufgabe nicht gefragt. Beispiel 4 zählt nicht zur Selbstbeschreibungsfähigkeit, weil es nicht nur um verständliche Information geht, sondern darum, dass Eingabefehler das Arbeiten nicht behindern und die Eingaben erhalten bleiben.

**b) Barrierefreiheit (3 Punkte, je 1 Punkt; drei Maßnahmen)**

Ausreichender Farbkontrast; Alternativtexte bzw. Beschriftungen für Bilder und Symbole (für Screenreader); alternative Bedienmöglichkeiten neben präzisen Touch-Gesten, z. B. Sprachsteuerung, Bedienungshilfen des Betriebssystems oder eine sinnvolle Fokusreihenfolge für Screenreader; skalierbare Schriftgröße; Informationen nicht nur über Farbe vermitteln; ausreichend große Bedienflächen; Untertitel bei Videos.

**c) Wireframe (6 Punkte)**

Musterskizze:

```text
┌──────────────────────────────────┐
│ Kurse                            │  ← Kopfzeile
├──────────────────────────────────┤
│ [Datum ▾]  [Kurstyp ▾]           │  ← Filter
├──────────────────────────────────┤
│ Boulder-Einsteiger         18:00 │  ← Kurs: Titel, Uhrzeit,
│ 3 Plätze frei           [Buchen] │     freie Plätze, Schaltfläche Buchen
├──────────────────────────────────┤
│ Vorstieg Basis             19:30 │
│ 0 Plätze frei       [Warteliste] │  ← ausgebucht: andere Darstellung
├──────────────────────────────────┤
│ Yoga für Kletterer         20:00 │
│ 8 Plätze frei           [Buchen] │
├──────────────────────────────────┤
│ Kurse | Buchungen | Profil       │  ← Navigationsleiste
└──────────────────────────────────┘
```

*Punkte: je Element 1 Punkt (Kopfzeile mit Titel; Filter; Kursliste mit Titel, Uhrzeit und freien Plätzen je Eintrag; Buchen-Schaltfläche je Kurs; erkennbar andere Darstellung für ausgebuchte Kurse, z. B. „Warteliste“ statt „Buchen“; Navigationsleiste). Bewertet wird die Vollständigkeit und eine sinnvolle Anordnung (Kopf oben, Navigation unten, Filter oberhalb der Liste), nicht die zeichnerische Qualität.*

**d) Bedienelemente und Fehlermeldungen (6 Punkte)**

- **da)** *(4 Punkte, je 1 Punkt)*: 1 Radiobuttons · 2 Checkboxen · 3 Dropdown-Liste · 4 Datumsauswahl. Hinweis: Bei 40 Einträgen ist eine durchsuchbare Dropdown-Liste noch ergonomischer.
- **db)** Zwei Regeln (je 1 Punkt): in verständlicher Sprache ohne Fehlercodes; nennt, was falsch ist und wie es behoben werden kann; steht direkt am betroffenen Feld; bereits eingegebene Daten bleiben erhalten; sachlich und ohne Schuldzuweisung.

**e) Prototyp (5 Punkte)**

- **ea)** *(2 Punkte)* **Low-Fidelity-Prototyp:** einfache Skizze bzw. Papierprototyp mit geringem Detailgrad, schnell und günstig erstellt. **High-Fidelity-Prototyp:** detailliert, oft klickbar und nahe am späteren Aussehen und Verhalten der App.
- **eb)** Zwei Vorteile (je 1 Punkt): Missverständnisse und Fehler werden früh erkannt, wenn Änderungen noch günstig sind; Rückmeldung der Nutzer kann vor der Umsetzung eingeholt werden; gemeinsame Diskussionsgrundlage mit dem Auftraggeber; weniger Änderungsaufwand in der Entwicklung.
- **ec)** Primär die künftigen Nutzerinnen und Nutzer (Mitglieder und Trainer), um Bedienbarkeit und Verständlichkeit zu prüfen; zusätzlich kann der Auftraggeber den Prototyp auf fachliche Anforderungen prüfen. *(1 Punkt)*

---

## 4. Aufgabe (25 Punkte)

**a) Qualitätsmerkmale (4 Punkte, je 1 Punkt)**

| Nr. | Qualitätsmerkmal |
|---:|---|
| 1 | Zuverlässigkeit |
| 2 | Wartbarkeit (Änderbarkeit) |
| 3 | Sicherheit |
| 4 | Effizienz (Leistung, Performance) |

Funktionalität und Benutzbarkeit sind hier nicht gefragt. Die vier gesuchten Merkmale gibt es auch in der aktuellen Fassung der ISO/IEC 25010 (2023) unter den Bezeichnungen Reliability, Maintainability, Security und Performance Efficiency. Die Auswahlliste selbst ist eine vereinfachte Auswahl und nicht die vollständige Liste der Norm.

**b) Teststufen (4 Punkte, je 1 Punkt)**

| Nr. | Teststufe |
|---:|---|
| 1 | Modultest |
| 2 | Integrationstest |
| 3 | Systemtest |
| 4 | Abnahmetest |

**c) Testfälle (6 Punkte)**

Beispiel (angenommen: `maxPlaetze` = 8):

| Nr. | Art | Vorbedingung | Aktion | erwartetes Ergebnis |
|---:|---|---|---|---|
| 1 | Normalfall | Kurs liegt in der Zukunft, 5 von 8 Plätzen durch aktive (nicht stornierte) Buchungen belegt | Mitglied bucht den Kurs | Buchung wird gespeichert, Bestätigung erscheint; vor der Buchung sind 3 Plätze frei, danach 2 |
| 2 | Grenzfall | Kurs liegt in der Zukunft, 8 von 8 Plätzen belegt | Mitglied versucht zu buchen | Es wird keine Buchung gespeichert, die Warteliste wird angeboten |
| 3 | Fehlerfall | Kurs liegt in der Vergangenheit | Mitglied versucht zu buchen | Fehlermeldung, keine Buchung gespeichert |

**Zwei gleichwertige Grenzfälle:** (a) der volle Kurs: 8 von 8 Plätzen belegt, keine Buchung, die Warteliste wird angeboten (in der Tabelle dargestellt); (b) der letzte freie Platz: 7 von 8 Plätzen belegt, die Buchung gelingt, danach ist der Kurs voll.

*Punkte: je Testfall 2 Punkte (1 Punkt für eine sinnvolle Vorbedingung und Aktion, 1 Punkt für das richtige erwartete Ergebnis).*

**d) Analytische Qualitätssicherung (6 Punkte)**

- **da)** Zwei Maßnahmen (je 1 Punkt): Code-Review, statische Codeanalyse (z. B. Linter), Inspektion bzw. Walkthrough, Review von Spezifikation und Entwurf.
- **db)** Ein Vorteil mit kurzer Begründung *(1 Punkt Nennung, 1 Punkt Begründung)*: Fehler werden früh gefunden (Vier-Augen-Prinzip); Wissen im Team wird geteilt; einheitliche Codequalität und Einhaltung von Standards.
- **dc)** Zwei Kriterien (je 1 Punkt): Code wurde geprüft (Review); alle Tests bestehen; Akzeptanzkriterien sind erfüllt; Dokumentation ist aktualisiert; keine offenen kritischen Fehler; Codestandards sind eingehalten.

**e) Regressionstest (5 Punkte)**

- **ea)** **Regressionstest** *(1 Punkt)*
- **eb)** Änderungen und Fehlerbehebungen können bestehende Funktionen unbeabsichtigt beeinträchtigen (Seiteneffekte). Der Test stellt sicher, dass Bisheriges weiter funktioniert. *(2 Punkte)*
- **ec)** Automatisierte Tests sind schnell und beliebig oft wiederholbar, z. B. bei jedem Commit in einer Continuous-Integration-Umgebung. Sie werden nicht aus Zeitdruck ausgelassen und liefern reproduzierbare Ergebnisse. *(2 Punkte)*

---

```yaml
dokument: AP2-Uebungsblatt-Planen-Loesungen
lernfeld: "Querschnittsthema, kein einzelnes Lernfeld (Ergänzung zum Pruefungs-Spickzettel-Block)"
titel: "AP2-Übungsblatt Anwendungsentwicklung - Planen eines Softwareproduktes (Lösungen)"
typ: "Übungsaufgaben mit separatem Lösungsblatt"
status: final
stand: 2026-09-28
quellen_intern:
  - "Zweites AP2-Blatt neben AP2_Uebungsblatt.md (Entwicklung und Umsetzung von Algorithmen); vier Szenario-Aufgaben zu je 25 Punkten, das Blatt orientiert sich strukturell an den vier in § 13 FIAusbV genannten Nachweisen (je eine Aufgabe)"
  - "Inhaltliche Anknüpfung an vorhandenes Wiki-Material zu Benutzerschnittstellen (LF10a) und Barrierefreiheit (Part 1 AP1); Aufgabenstellungen und Zahlen eigenständig neu erfunden"
quellen_fachlich:
  - titel: "Fachinformatikerausbildungsverordnung (FIAusbV), § 13 Prüfungsbereich Planen eines Softwareproduktes"
    herausgeber: "Bundesministerium der Justiz, Gesetze im Internet"
    status: "Direkt eingesehen. § 13 nennt vier Nachweise (Entwicklungsumgebungen und -bibliotheken auswählen und einsetzen; Programmspezifikationen anwendungsgerecht festlegen; Bedienoberflächen funktionsgerecht und ergonomisch konzipieren; Maßnahmen zur Qualitätskontrolle planen und durchführen), praxisbezogene schriftliche Aufgaben, 90 Minuten Prüfungszeit. Das Blatt orientiert sich strukturell an diesen vier Nachweisen (je eine Aufgabe)"
  - titel: "DIN EN ISO 9241-110 (Interaktionsprinzipien bzw. Grundsätze der Dialoggestaltung)"
    herausgeber: "DIN"
    status: "Der Normtext selbst wurde nicht eingesehen. Die Norm ist in der Ausgabe 2020-10 als 'Interaktionsprinzipien' geführt (Titel über den DIN-Media-Katalog bestätigt). Die Prinzipnamen stammen aus Lehrmaterialien zu beiden Fassungen: Ältere Fassung (2006) mit Aufgabenangemessenheit, Selbstbeschreibungsfähigkeit, Steuerbarkeit, Erwartungskonformität, Fehlertoleranz, Individualisierbarkeit, Lernförderlichkeit; Fassung 2020 mit Aufgabenangemessenheit, Selbstbeschreibungsfähigkeit, Erwartungskonformität, Erlernbarkeit, Steuerbarkeit, Robustheit gegen Benutzungsfehler, Benutzerbindung. Das Blatt verwendet die ältere Benennung, weist im Aufgabentext auf die neuere hin und wertet sinngemäß gleichwertige Bezeichnungen"
  - titel: "ISO/IEC 25010 (Produktqualitätsmodell)"
    herausgeber: "ISO/IEC"
    status: "Normtext nicht eingesehen. Über Normenkatalog- und Vorschauseiten bestätigt: Die Ausgabe 2023 (November 2023) ersetzt die Ausgabe 2011 und umfasst neun Merkmale; Safety wurde ergänzt, Usability heißt Interaction Capability, Portability heißt Flexibility. Das Blatt verwendet bewusst eine vereinfachte, in der IT-Ausbildung gebräuchliche Auswahl von Merkmalen in deutscher Benennung, weist im Aufgabentext auf die aktuelle Fassung hin und wertet gleichwertige Bezeichnungen. Die vier gefragten Merkmale (Zuverlässigkeit, Wartbarkeit, Sicherheit, Effizienz) bestehen auch in der Fassung 2023"
  - titel: "Prüfungskatalog für die Fachrichtung Anwendungsentwicklung (AP2)"
    herausgeber: "ZPA Nord-West / U-Form Verlag"
    status: "Lag bei der Erstellung nicht vor. Aufgabenzahl, Punkteverteilung, Aufgabenformate und die Frage, welche Zeichen- und Diagrammaufgaben (Wireframe, Anwendungsfall- und Klassendiagramm) in der echten Prüfung vorkommen, sind daher nicht gegen den Katalog geprüft"
review_historie:
  - runde: 1
    datum: 2026-09-28
    ergebnis: "Erstdraft erstellt. Aufbau entlang der vier Nachweise aus § 13 FIAusbV, Szenario (Kletterhallen-App) bewusst abweichend von realen Prüfungsszenarien und den anderen Übungsblättern der Reihe gewählt. Die Git-Befehlsfolge der Musterlösung (switch -c, add, commit, push -u) wurde in einem echten lokalen Testrepository mit Git 2.43.0 ausgeführt; dabei bestätigt, dass ein Push vor dem Commit nichts Neues überträgt. Reihenfolge der Versionen 2.4.1 < 2.4.2 < 2.5.0 < 3.0.0 geprüft. Prinzipnamen der ISO 9241-110 in beiden Fassungen über Lehrmaterialien abgeglichen, Normtext nicht eingesehen (Quellenangabe entsprechend). Wireframe-Musterskizze programmatisch mit exakt ausgerichteten Rahmen erzeugt. Punktsummen je Aufgabe und je Unterpunkt nachgezählt (jeweils 25)."
  - runde: 2
    datum: 2026-09-28
    ergebnis: "3 Reviews eingearbeitet, alle ohne Rechen- oder Zuordnungsfehler, Punkte 4 x 25 erneut bestätigt. Wichtigster Fund (Review 3, über Normenkatalog- und Vorschauseiten selbst bestätigt): ISO/IEC 25010:2011 ist durch die Ausgabe 2023 ersetzt (neun Merkmale, Safety ergänzt, Usability heißt Interaction Capability, Portability heißt Flexibility). Die Formulierung 'die Bezeichnungen folgen der Qualitätsnorm ISO/IEC 25010' war dadurch missverständlich - jetzt als vereinfachte, in der Ausbildung gebräuchliche Auswahl gekennzeichnet, mit Hinweis auf die aktuelle Fassung; die vier gefragten Merkmale bestehen auch 2023, die Antworten blieben unverändert. Fachlicher Fehler (Review 1, berechtigt): 2a Nr. 4 'Passwörter werden verschlüsselt gespeichert' ist falsch, Passwörter werden gehasht und gesalzen gespeichert - Aufgabe und Lösung korrigiert. Aufgabe 3c verlangte 'je Kurs eine Schaltfläche zum Buchen', die Musterlösung zeigt bei ausgebuchten Kursen aber 'Warteliste' - Aufgabe angepasst. Weitere Umsetzungen: ISO-9241-110-Hinweis eindeutiger (bewusst bekannte ältere Lernbegriffe, beide Bezeichnungen gewertet, kein Auswendiglernen einer Namensliste); Barrierefreiheit statt 'Bedienbarkeit ohne Touch' jetzt alternative Bedienmöglichkeiten neben präzisen Touch-Gesten; Lastenheft/Pflichtenheft mit 'typischerweise'; Zahlungsdienstleister als externes System klargestellt; beide Grenzfälle in 4c sichtbar gleichwertig ausgewiesen; Hinweis auf durchsuchbares Dropdown bei 40 Einträgen; Zeitrichtwert je Aufgabe. Nicht übernommen: Änderung des Stand-Datums auf 2024 (Review 2 hielt das Datum für futuristisch; das Datum ist das tatsächliche heutige Datum); Ergänzung von Prüfungscheckliste und Abschnitt zu typischen Prüfungsfehlern (nicht Ziel eines Übungsblatts, der Katalog liegt nicht vor, daher wären Aussagen zu 'typischen Prüfungsfehlern' nicht belegbar); Dateinamen-Hinweis zu .txt (betrifft nur die Version des Reviewers, in den Dateien stehen durchgehend .md). Den Status setzt David."
  - runde: 3
    datum: 2026-09-28
    ergebnis: "3 Re-Reviews eingearbeitet; zwei bestätigen die Umsetzung der Runde-2-Punkte, ein Review meldete einen 'Rechenfehler' in Testfall 1 der Aufgabe 4c. Gegen die Datei geprüft: Der Wert war rechnerisch richtig (5 von 8 belegt, nach der Buchung 6 von 8 belegt, also 2 Plätze frei), aber mehrdeutig formuliert, weil '2 Plätze bleiben frei' auch auf den Zustand vor der Buchung gelesen werden konnte - jetzt 'vor der Buchung sind 3 Plätze frei, danach 2'. Zusätzlich umgesetzt: Prototyp-Test (Aufgabe 3e/ec) unterscheidet jetzt Nutzertest (primär die künftigen Nutzerinnen und Nutzer) von fachlicher Prüfung durch den Auftraggeber. Nicht übernommen: 'Optionaler' Orientierungswert beim Notenschlüssel (bleibt einheitlich zu den Blättern AP1 und AP2 Algorithmen); Ergänzung 'durchsuchbares Dropdown' in der Aufgabe selbst (würde die Lösung vorwegnehmen, steht als Hinweis im Lösungsblatt); Datum 2024 statt 2026 (tatsächliches heutiges Datum); Prüfungscheckliste und typische Prüfungsfehler (nicht belegbar, Katalog liegt nicht vor); der Hinweis auf ein angeblich fehlendes Beispiel für eine schlechte Anforderung (steht bereits in Aufgabe 2d, db: 'Die App soll schnell sein'). Den Status setzt David."
  - runde: 4
    datum: 2026-09-28
    ergebnis: "4 Reviews eingearbeitet, kein gravierender Fehler mehr gemeldet, Fokus lag auf Formulierungsschärfe. Alle Punkte gegen die tatsächliche Datei geprüft, alle bestätigten sich als real. Wichtigster Punkt: 1a/ac akzeptierte ScanKit bei 'ausdrücklich begründeter' Offenlegung des Quellcodes, obwohl die Ausgangssituation ausdrücklich verlangt, den Quellcode NICHT offenzulegen - eine bloße Abwägung reicht jetzt nicht mehr, gefordert ist entweder eine zusätzliche GPL-vereinbare Lösung oder die ausdrückliche Feststellung, dass sich die Geschäftsentscheidung ändern würde; GPL-Kernsatz zusätzlich von einer pauschalen Aussage ('müsste ... ebenfalls unter der GPL') auf eine bedingte Formulierung präzisiert. 2b/ba: Der QR-Code-Check-in als 'nur vom Mitglied ausgelöst' ist durch die Ausgangssituation nicht eindeutig gedeckt (denkbar wäre auch Personal am Eingang) - als Beispiel für 'nur dieser Akteur' durch die eindeutigere Warteliste ersetzt, der Hinweis zur Unsicherheit beim QR-Code bleibt als Kulanzregel stehen. Weitere Präzisierungen: 2d/db-Musteranforderung um Geräteklasse und Netzbedingung ergänzt, damit das Beispiel selbst prüfbar ist; 1c/cb SemVer-Erklärung stellt jetzt klar, dass ein Major-Sprung nicht zwangsläufig die eigene Anwendung betrifft; 2c/ca-Tabellenkopf eindeutiger (Ende der zuerst genannten Klasse statt 'erste/zweite Klasse'); 4c-Testfall 1 stellt klar, dass die 5 belegten Plätze aktive, nicht stornierte Buchungen sind. Nicht übernommen: ISO-9241-110-Hinweis stärker auf die aktuelle Terminologie umstellen (die jetzige Formulierung nennt bereits beide Fassungen gleichwertig, eine Verschiebung der Gewichtung ist reine Geschmacksfrage zwischen den Reviews); Dateinamen-/Endungshinweis (bereits in Runde 2 mit derselben Begründung nicht übernommen); Aufteilung der Grenzfall-Testfalltabelle in zwei Zeilen (beide Grenzfälle stehen bereits gleichwertig nebeneinander im Text unter der Tabelle). Den Status setzt David."
  - runde: 5
    datum: 2026-09-28
    ergebnis: "Abschluss-Selbstcheck, danach von David final freigegeben. Beide Dateien vollständig gelesen. Automatisiert geprüft: Punktsummen (25 je Aufgabe, 100 gesamt, alle Teilpunkte konsistent mit den Kopfzahlen), Git-Reihenfolge c->d->a->f->e->b gegen die Schritttabelle im Aufgabenblatt, Klassendiagramm-Multiplizitäten, Wireframe-Rahmenbreiten, YAML-Gültigkeit, keine unpaarigen Formatierungszeichen, keine Platzhalter- oder TODO-Reste. Keine weiteren Fehler gefunden."
naechste_review: "Bei Vorliegen des Prüfungskatalogs für die Fachrichtung Anwendungsentwicklung (Abgleich von Aufgabenzahl, Punkteverteilung und Zeichenaufgaben) oder nach Auswertung neuer AP2-Prüfungen"
```