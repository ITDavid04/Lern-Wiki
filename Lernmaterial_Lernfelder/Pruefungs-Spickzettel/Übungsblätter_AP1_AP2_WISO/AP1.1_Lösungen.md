# AP1-Übungsblatt – Lösungen

> **Zugehörig zu:** [AP1_Aufgaben.md](AP1_Aufgaben.md)
> **Status:** Final
> **Stand:** 2026-09-28
>
> Musterlösungen mit Punktevergabe. Bei Freitextfragen sind sinngemäß gleichwertige, fachlich richtige Antworten ebenfalls zu werten. Folgefehler werden berücksichtigt: Wurde mit einem falschen Wert aus einem früheren Unterpunkt korrekt weitergerechnet, sind die Punkte zu vergeben.

**Orientierungswert (Punkte-Noten-Schlüssel):** 100–92 Punkte = Note 1 · 91–81 = Note 2 · 80–67 = Note 3 · 66–50 = Note 4 · 49–30 = Note 5 · 29–0 = Note 6. Der Schlüssel kann je nach IHK bzw. Prüfung abweichen und ist nicht Bestandteil der echten AP1-Bewertung.

---

## 1. Aufgabe (25 Punkte)

**a) Nutzwertanalyse (7 Punkte)**

Nutzwert = Summe aus Punkte × Gewichtung. Kontrolle: Die Gewichtungen ergeben zusammen 100 %.

| Kriterium | Gewicht | A | A gewichtet | B | B gewichtet | C | C gewichtet |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rechenleistung | 30 % | 4 | 1,2 | 5 | 1,5 | 3 | 0,9 |
| Energieeffizienz | 20 % | 5 | 1,0 | 3 | 0,6 | 4 | 0,8 |
| Preis | 30 % | 3 | 0,9 | 2 | 0,6 | 5 | 1,5 |
| Anschlussvielfalt | 20 % | 3 | 0,6 | 4 | 0,8 | 4 | 0,8 |
| **Nutzwert** | | | **3,7** | | **3,5** | | **4,0** |

Entscheidung: **Mini-PC C** (höchster Nutzwert).

*Punkte: je Gerät 2 Punkte (1 Punkt für nachvollziehbaren Rechenweg bzw. richtige gewichtete Einzelwerte, 1 Punkt für die richtige Summe), Entscheidung 1 Punkt.*

**b) Stromkosten (4 Punkte)**

Rechnung für Mini-PC C (12 W):

- Jahresverbrauch: 12 W × 10 h/Tag × 250 Tage/Jahr = 30 000 Wh/Jahr = **30 kWh/Jahr** *(1 Punkt)*
- Verbrauch in 4 Jahren: 30 kWh/Jahr × 4 Jahre = **120 kWh** *(1 Punkt)*
- Kosten: 120 kWh × 0,34 EUR/kWh = **40,80 EUR** *(1 Punkt)*
- Nachvollziehbarer Rechenweg mit korrekten Einheiten *(1 Punkt)*

Bei Folgefehlern durch eine andere Geräteentscheidung: A ergibt 51,00 EUR, B ergibt 68,00 EUR.

**c) Anschlüsse (4 Punkte, je 1 Punkt)**

a → 4, b → 2, c → 1, d → 3.

**d) Subnetting 192.168.40.0/27 (7 Punkte)**

Bei /27 sind 27 Bit Netzanteil und 5 Bit Hostanteil. Das letzte Oktett der Maske lautet 11100000 = 224, die Blockgröße beträgt 32.

- da) Subnetzmaske: **255.255.255.224** *(2 Punkte)*
- db) Broadcast-Adresse: **192.168.40.31** *(2 Punkte)*
- dc) Nutzbare Adressen: 2⁵ − 2 = **30** *(1 Punkt)*
- dd) Erste nutzbare Adresse (Router): **192.168.40.1** *(1 Punkt)*
- de) Letzte nutzbare Adresse (Drucker): **192.168.40.30** *(1 Punkt)*

**e) Domäne (3 Punkte)**

- ea) Zwei Vorteile (je 1 Punkt): zentrale Benutzer- und Rechteverwaltung; einheitliche Einstellungen über Gruppenrichtlinien; zentrale Anmeldung (ein Konto für alle PCs); einfachere Administration statt Einzelpflege jedes PCs.
- eb) Der **Verzeichnisdienst** (z. B. Active Directory Domain Services), bereitgestellt auf einem **Domänencontroller** *(1 Punkt)*. Ergänzend (nicht gefordert): Für eine Active-Directory-Domäne muss außerdem eine funktionierende DNS-Namensauflösung vorhanden sein.

---

## 2. Aufgabe (25 Punkte)

**a) Schutzziele (3 Punkte, je 1 Punkt)**

1. Integrität
2. Verfügbarkeit
3. Vertraulichkeit

**b) Technische Maßnahmen (3 Punkte, je 1 Punkt; Beispiele)**

1. Integrität: Protokollierung von Änderungen, Versionierung, Prüfsummen bzw. Hashwerte, restriktive Schreibrechte
2. Verfügbarkeit: regelmäßige Datensicherung, USV, redundante Systeme bzw. Cluster
3. Vertraulichkeit: automatische Bildschirmsperre, Sichtschutzfolie, Zugriffsrechte nach dem Least-Privilege-Prinzip, Verschlüsselung

**c) Hashwert (4 Punkte)**

- ca) Der Hashwert dient der **Integritätsprüfung**: Der selbst berechnete Wert der heruntergeladenen Datei wird mit dem veröffentlichten Wert verglichen. Stimmen sie überein, spricht das dafür, dass die Datei bei der Übertragung nicht verändert oder beschädigt wurde. *(2 Punkte)*
- cb) Die Datei **nicht installieren**, sondern verwerfen, erneut von der offiziellen Quelle herunterladen und den Hashwert erneut prüfen; bei erneuter Abweichung die Quelle prüfen bzw. den Hersteller kontaktieren. *(2 Punkte)*

Hinweis: Ein Hashvergleich prüft primär die Integrität. Er beweist die Unverändertheit nur dann zuverlässig, wenn der Vergleichswert selbst aus einer vertrauenswürdigen Quelle stammt.

**d) Zwei-Faktor-Authentifizierung (4 Punkte)**

Zwei verschiedene Faktorarten mit je einem Beispiel (je 1 Punkt für die Art, je 1 Punkt für das passende Beispiel):

- **Wissen**: Passwort, PIN
- **Besitz**: Smartphone mit Authenticator-App, Hardware-Token, Chipkarte
- **Inhärenz (Merkmal der Person)**: Fingerabdruck, Gesichtserkennung

Zwei Beispiele aus derselben Art (z. B. Passwort und PIN) zählen nicht als zwei unterschiedliche Faktorarten.

**e) Härtung (3 Punkte, je 1 Punkt; drei Maßnahmen)**

Nicht benötigte Dienste und Schnittstellen deaktivieren; Standardpasswörter ändern; Betriebssystem und Software aktuell halten (Updates einspielen); Benutzer ohne Administratorrechte arbeiten lassen; Firewall aktivieren; BIOS-/UEFI-Passwort und feste Boot-Reihenfolge; Bildschirmsperre mit Kennwort. Ergänzend, aber eher Schutzmaßnahme als Härtung: Virenschutz aktivieren.

**f) Passwort (3 Punkte)**

- fa) Das Passwort ist **schwach**: Es besteht aus einem erratbaren Wort mit angehängter Jahreszahl (vorhersehbares Muster) und enthält keine Sonderzeichen. Seine Länge von 10 Zeichen allein macht es nicht sicher. *(1 Punkt)*
- fb) Zwei Regeln (je 1 Punkt): ausreichende Mindestlänge bzw. Passphrase verwenden; keine leicht erratbaren Wörter, Muster oder persönlichen Daten verwenden; jedes Passwort nur einmal verwenden (keine Wiederverwendung); Passwortmanager nutzen. Eine Kombination aus Zeichenarten kann als Regel gewertet werden, ist aber weniger wichtig als Länge und Unvorhersehbarkeit. Zwei-Faktor-Authentifizierung ist eine zusätzliche Schutzmaßnahme, keine Passwortregel.

**g) Datenschutz (5 Punkte)**

- ga) Zwei weitere Rechte neben der Auskunft (je 1 Punkt): Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit, Widerspruch.
- gb) *(3 Punkte)*
  - **Anonymisierung:** Der Personenbezug wird so beseitigt, dass die Person mit vernünftigerweise einsetzbaren Mitteln nicht mehr identifiziert werden kann; die Daten gelten dann nicht mehr als personenbezogen. *(1 Punkt)*
  - **Pseudonymisierung:** Der direkte Personenbezug wird durch ein Kennzeichen ersetzt. Mit zusätzlichen, getrennt aufbewahrten Informationen (z. B. einer Zuordnungstabelle) bleibt die Person zuordenbar; die Daten bleiben personenbezogen. *(1 Punkt)*
  - Abgrenzung: Bei wirksamer Anonymisierung ist eine Identifizierung mit vernünftigerweise einsetzbaren Mitteln nicht mehr möglich; bei der Pseudonymisierung bleibt sie mithilfe zusätzlicher Informationen möglich. *(1 Punkt)*

---

## 3. Aufgabe (25 Punkte)

**a) Wasserfallmodell (4 Punkte, je 1 Punkt)**

Gängige Phasen in dieser Reihenfolge: Anforderungsanalyse → Entwurf → Implementierung → Test → Einführung/Betrieb. Gefordert sind **vier** typische Phasen; sie müssen nicht unmittelbar aufeinanderfolgen. Je 1 Punkt für eine richtig benannte Phase, sofern die genannten Phasen in der richtigen relativen Reihenfolge stehen. Sinngemäß gleichwertige, fachlich richtige Phasenfolgen anderer Wasserfall-Darstellungen sind ebenfalls zu werten. Werden mehr als vier Phasen genannt, zählen die ersten vier.

**b) Scrum-Rollen (2 Punkte, je 1 Punkt)**

Zwei von: Product Owner, Scrum Master, Entwicklungsteam.

**c) SMART (4 Punkte)**

- ca) Zwei Kriterien (je 1 Punkt): nicht **spezifisch** (was genau soll besser laufen?), nicht **messbar** (woran wird „besser“ gemessen?), nicht **terminiert** („bald“ ist kein Termin). SMART steht für spezifisch, messbar, attraktiv bzw. akzeptiert, realistisch und terminiert.
- cb) Beispiel *(2 Punkte)*: „Bis zum 31.10.2026 sind alle sechs Arbeitsplätze der Praxis an das neue Netzwerk angebunden, und die Praxissoftware läuft auf allen Geräten fehlerfrei.“ Je 1 Punkt für ein messbar und spezifisch formuliertes Ziel sowie für einen konkreten Termin.

**d) Netzplan (15 Punkte)**

| Nr. | Dauer | FAZ | FEZ | SAZ | SEZ | GP | FP |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 2 | 0 | 2 | 0 | 2 | 0 | 0 |
| B | 4 | 0 | 4 | 5 | 9 | 5 | 0 |
| C | 3 | 2 | 5 | 2 | 5 | 0 | 0 |
| D | 5 | 5 | 10 | 5 | 10 | 0 | 0 |
| E | 3 | 4 | 7 | 9 | 12 | 5 | 3 |
| F | 4 | 10 | 14 | 12 | 16 | 2 | 2 |
| G | 6 | 10 | 16 | 10 | 16 | 0 | 0 |
| H | 2 | 16 | 18 | 16 | 18 | 0 | 0 |
| I | 1 | 18 | 19 | 18 | 19 | 0 | 0 |

**da) Vorwärtsrechnung (4 Punkte):** FAZ = größter FEZ der Vorgänger, FEZ = FAZ + Dauer. A und B haben keinen Vorgänger und beginnen bei 0. F wartet auf D (FEZ 10) und E (FEZ 7), also FAZ 10. H wartet auf F (14) und G (16), also FAZ 16. *(2 Punkte für FAZ, 2 Punkte für FEZ; Folgefehler sind mit dem nachvollziehbaren Rechenweg angemessen zu berücksichtigen)*

**db) Rückwärtsrechnung (4 Punkte):** SEZ = kleinster SAZ der Nachfolger, SAZ = SEZ − Dauer. Der letzte Vorgang I erhält SEZ = 19. D hat die Nachfolger F (SAZ 12) und G (SAZ 10), also SEZ 10. *(2 Punkte für SEZ, 2 Punkte für SAZ)*

**dc) Puffer (3 Punkte):** GP = SAZ − FAZ; FP = kleinster FAZ der Nachfolger − eigener FEZ. *(GP 2 Punkte, FP 1 Punkt; Folgefehler sind mit dem nachvollziehbaren Rechenweg angemessen zu berücksichtigen)*

Beobachtung: B ist ein Startvorgang, hat aber SAZ = 5, weil B nicht auf dem kritischen Pfad liegt. Der SAZ eines Startvorgangs ist nur dann 0, wenn der Vorgang kritisch ist. Der FAZ jedes Startvorgangs ist dagegen immer 0.

**dd) Kritischer Pfad und Projektdauer (2 Punkte):** Der kritische Pfad besteht aus den Vorgängen mit GP = 0: **A → C → D → G → H → I**. Projektdauer: **19 Tage** (2 + 3 + 5 + 6 + 2 + 1). *(1 Punkt Pfad, 1 Punkt Dauer)*

**de) Verzug (2 Punkte):** F hat einen Gesamtpuffer von 2 Tagen. Dauert F 5 Tage länger als geplant, verschiebt sich das Projektende um 5 − 2 = **3 Tage** (auf 22 Tage), unter der Annahme, dass keine Gegenmaßnahmen erfolgen. *(1 Punkt Ergebnis, 1 Punkt Begründung)*

---

## 4. Aufgabe (25 Punkte)

**a) Schreibtischtest (6 Punkte)**

| i | dauern[i] | dauern[i] > 30 ? | gesamt (nach dem Durchlauf) |
|---|---:|---|---:|
| 0 | 20 | nein | 20 |
| 1 | 45 | ja | 50 |
| 2 | 10 | nein | 60 |
| 3 | 35 | ja | 90 |

Rückgabewert: **90** (Minuten). Die Funktion rechnet pro Patient höchstens 30 Minuten an: Werte über 30 zählen als 30 (45 → 30, 35 → 30), alle anderen zählen mit ihrem tatsächlichen Wert.

*Punkte: je Zeile 1 Punkt für den richtigen Wert von `gesamt` (4 Punkte), 1 Punkt für die vollständig richtige Spalte der Bedingung, 1 Punkt für den Rückgabewert.*

**b) Fehlerarten (4 Punkte)**

- **Ausschnitt 1: Syntaxfehler.** Hinter der Bedingung fehlt der Doppelpunkt. Korrektur: `if alter < 14:` *(1 Punkt Fehlerart, 1 Punkt Korrektur)*
- **Ausschnitt 2: Logikfehler.** Der Code ist formal gültig und läuft für den vorgesehenen Testfall mit mindestens zwei Werten, teilt aber durch `len(werte) - 1` statt durch `len(werte)`. Korrektur: `return summe / len(werte)` *(1 Punkt Fehlerart, 1 Punkt Korrektur)*

Erkennungshinweis: Ein Logikfehler zeigt sich typischerweise nicht durch einen Absturz, sondern durch das falsche Ergebnis, hier durch einen Testfall mit bekanntem Erwartungswert. In Randfällen kann derselbe Fehler auch einen Laufzeitfehler auslösen: Bei einer Liste mit genau einem Wert führt `len(werte) - 1` zur Division durch null.

**c) Klassen (3 Punkte)**

- ca) Attribut z. B. `name` oder `geburtsjahr`; Methode z. B. `get_name()` bzw. der Konstruktor `__init__`. *(1 Punkt)*
- cb) `public`: Teil der von außen nutzbaren Schnittstelle der Klasse. `private`: nicht für die Nutzung von außen vorgesehen, der Zugriff wird auf die Klasse selbst beschränkt. Wie streng das durchgesetzt wird, hängt von der Programmiersprache ab: In Java oder C++ verhindert der Compiler den Zugriff, in Python gilt eine Namenskonvention (führende Unterstriche, bei zwei Unterstrichen mit Namensänderung, aber ohne strikten Zugriffsschutz). *(1 Punkt)*
- cc) Kapselung: Der Zugriff soll kontrolliert über Methoden erfolgen, damit Werte nicht unkontrolliert von außen verändert werden können und die Klasse intern geändert werden kann, ohne andere Programmteile zu beeinflussen. *(1 Punkt)*

**d) Aktivitätsdiagramm (3 Punkte, je 1 Punkt)**

a → 2, b → 1, c → 3.

**e) KI-Einsatz (9 Punkte)**

- ea) Drei Schritte mit Beschreibung (je 1 Punkt; Beispiele) *(3 Punkte)*:
  - Anfrage entgegennehmen: automatische Erfassung und Vorstrukturierung der Anfrage (z. B. per Chat oder Sprache)
  - Freien Termin suchen: automatische Terminvorschläge anhand von Kalender, Behandlungsdauer und Auslastung
  - Erinnerung versenden: automatisch formulierte und rechtzeitig versendete Terminerinnerungen, ggf. Umbuchungsvorschläge bei Absagen
- eb) Zwei Risiken (je 1 Punkt; Beispiele) *(2 Punkte)*:
  - **Datenschutz:** Gesundheitsdaten gehören zu den besonderen Kategorien personenbezogener Daten. Ihre Verarbeitung unterliegt den besonderen Anforderungen des Art. 9 DSGVO und braucht eine passende Rechtsgrundlage sowie geeignete technische und organisatorische Maßnahmen; bei einem externen Anbieter ist zusätzlich ein Vertrag zur Auftragsverarbeitung zu prüfen.
  - **Fehler:** Fehlerhafte oder erfundene Ergebnisse (z. B. falsche Terminvergabe) ohne menschliche Kontrolle.
  - **Abhängigkeit:** Ausfall oder Änderungen beim Anbieter können den Praxisbetrieb beeinträchtigen.
  - **Akzeptanz:** Vorbehalte bei Patientinnen und Patienten bzw. Mitarbeitenden.
- ec) Wirtschaftliche Gesamtbelastung im ersten Jahr (Kosten plus entgangener Umsatz) *(4 Punkte)*:
  - Lizenzen: 59 EUR × 2 × 12 Monate = **1 416 EUR** *(1 Punkt)*
  - Einrichtung: **240 EUR** *(1 Punkt)*
  - Entgangener Umsatz durch Einarbeitung: 2 Personen × 5 Stunden × 90 EUR = **900 EUR** *(1 Punkt)*
  - Summe: 1 416 + 240 + 900 = **2 556 EUR** *(1 Punkt)*; davon 1 656 EUR tatsächliche Kosten (Lizenzen und Einrichtung) und 900 EUR entgangener Umsatz

---

```yaml
dokument: AP1-Uebungsblatt-Loesungen
lernfeld: "Querschnittsthema, kein einzelnes Lernfeld (Ergänzung zum Pruefungs-Spickzettel-Block)"
titel: "AP1-Übungsblatt (Lösungen)"
typ: "Übungsaufgaben mit separatem Lösungsblatt"
status: final
stand: 2026-09-28
quellen_intern:
  - "Ergänzung zu Pruefungs-Spickzettel/Part_1_AP1.md - vier Szenario-Aufgaben statt 30 Einzelfragen, da die echte AP1 aus vier zusammenhängenden, ungebundenen Aufgaben besteht"
  - "Netzplan-Regeln (Vorwärts Maximum, Rückwärts Minimum, SAZ eines Startvorgangs nur bei kritischem Pfad 0) entsprechen dem finalen Part 1 des Spickzettels; das Aufgabenbeispiel enthält bewusst zwei Startvorgänge, um genau diese Regel zu üben"
quellen_fachlich:
  - titel: "FiSi-Prüfungskatalog 2. Auflage 2024 (AP1, Prüfungsbereich Einrichten eines IT-gestützten Arbeitsplatzes)"
    herausgeber: "ZPA Nord-West"
    status: "Aufbau der AP1 (vier ungebundene Aufgaben, je 20 bis 30 Punkte, 100 Punkte gesamt, 90 Minuten) direkt aus dem Katalog übernommen. Alle Aufgaben, Szenario, Namen und Zahlen eigenständig neu erfunden - keine Übernahme oder Abwandlung realer Prüfungsaufgaben"
  - titel: "Prüfungskatalog 2025 für AP1 der IT-Berufe (Änderungsvergleich 2020 zu 2025)"
    herausgeber: "U-Form Verlag / ZPA Nord-West"
    status: "Themenauswahl (Nutzwertanalyse, Domäne, Hashwert, Zwei-Faktor, Härtung, Pseudonymisierung/Anonymisierung, Schreibtischtest, Sichtbarkeit in Klassen, Aktivitätsdiagramm, KI, Netzplan) an den aktuellen Katalog angelehnt"
  - titel: "DSGVO (Art. 4 Nr. 5, Art. 5, Art. 9, Art. 15 bis 21)"
    herausgeber: "Gesetze im Internet / EUR-Lex"
    status: "Fachliche Grundlage der Musterlösungen zu Datenschutz (Aufgabe 2g und 4e); die Aussagen wurden in den Review-Runden gegen den Gesetzestext gegengeprüft. Härtungs- und Passwortmaßnahmen (Aufgabe 2e, 2f) sind allgemein üblicher Prüfungsstoff und nicht einzeln gegen eine Quelle belegt"
review_historie:
  - runde: 1
    datum: 2026-09-28
    ergebnis: "Erstdraft erstellt. Aufbau bewusst wie die echte AP1 (vier Szenario-Aufgaben zu je 25 Punkten, gesamt 100 Punkte), statt 30 Einzelfragen wie beim WiSo-Blatt. Szenario (Zahnarztpraxis) bewusst abweichend von realen Prüfungsszenarien gewählt. Alle Rechenwerte (Nutzwertanalyse, Stromkosten, Subnetting, Netzplan, Schreibtischtest, KI-Kosten) vor dem Schreiben per Skript gegengerechnet. Punktsummen je Unterpunkt und je Aufgabe nachgezählt (jeweils 25)."
  - runde: 2
    datum: 2026-09-28
    ergebnis: "3 Reviews eingearbeitet. Klarer, von allen drei Reviews gemeldeter Fehler: Bei 3a (Wasserfallmodell) standen im Lösungsblatt fünf Phasen unter der Überschrift 'Vier Phasen' - jetzt als Liste gängiger Phasen mit der Vorgabe 'vier genügen' und einer festen Bewertungsregel (je 1 Punkt für eine richtig benannte Phase in richtiger relativer Reihenfolge, bei mehr als vier zählen die ersten vier). Zweifach bestätigt und umgesetzt: 4c (private/public) war sprachunabhängig zu absolut formuliert, das Beispiel ist Python - jetzt allgemeine OOP-Definition mit Hinweis auf sprachabhängige Durchsetzung (Java/C++ Compiler, Python Namenskonvention), Hinweis in der Aufgabe entsprechend angepasst; 4b (Logikfehler) kann bei einer Liste mit genau einem Wert auch eine Division durch null auslösen - Randfall im Erkennungshinweis ergänzt; 2f (Passwort) nannte Zwei-Faktor-Authentifizierung als Passwortregel und Zeichenartenmix als Kernregel - auf Länge, Unvorhersehbarkeit und Einmaligkeit umgestellt; 1e (Domäne) setzte Domänencontroller mit Active Directory gleich - jetzt Domänencontroller mit Verzeichnisdienst (AD DS) plus DNS-Namensauflösung; Notenschlüssel lesbarer dargestellt (100-92, 91-81, 80-67, 66-50, 49-30, 29-0). Weitere Präzisierungen: Hinweis, dass die Gleichverteilung 4 x 25 Punkte nur für dieses Übungsblatt gilt und die echte AP1 anders verteilen kann; Bewertungshinweis zu Folgefehlern beim Netzplan durch allgemeine Formulierung ersetzt (konkrete Abzugsregeln sind Sache des jeweiligen Erwartungshorizonts); 3de präzisiert (F dauert 5 Tage länger, keine Gegenmaßnahmen); 4a um die zugrunde liegende Regel (maximal 30 Minuten pro Patient) ergänzt; 4e-Risiko zu Gesundheitsdaten an Art. 9 DSGVO angepasst (Rechtsgrundlage, TOM, Auftragsverarbeitung zu prüfen statt pauschal gefordert); Härtungsliste geordnet (Virenschutz als ergänzend); SMART ohne Variantenmix; Hashwert-Formulierung vorsichtiger ('spricht dafür'); Hinweis zur Gewichtssumme 100 % in Aufgabe 1a. Nicht übernommen: der Hinweis, die Zuordnungen in 1c und 4d seien ohne das Übungsblatt nicht prüfbar (die Prüfung erfolgte nur am Lösungsblatt, die Zuordnungen wurden gegen das Aufgabenblatt kreuzgeprüft); der Hinweis zu nicht verifizierten Katalogaussagen bezieht sich auf die Prüfung des Reviewers, die Katalogstruktur der AP1 wurde direkt im Katalog gelesen."
  - runde: 3
    datum: 2026-09-28
    ergebnis: "3 Reviews eingearbeitet, Schwerpunkt Aufgabenblatt. Eine Meldung wurde gegen die Datei geprüft und verworfen: Eine Review sah in Aufgabe 4a ein falsch eingerücktes 'else:'. Der Code wurde extrahiert und ausgeführt - if und else stehen auf gleicher Ebene, die Funktion kompiliert und liefert für den Aufruf 90; es war ein Darstellungsartefakt beim Review. Zweifach bestätigt und umgesetzt: 1e/eb fragte 'welcher zentrale Dienst' im Singular, die Musterlösung erwartete aber Domänencontroller und DNS zusammen - Frage jetzt eindeutig auf den Verzeichnisdienst für Benutzerkonten und Anmeldung bezogen, DNS in der Lösung als nicht geforderter Zusatz; 4c-Hinweis nannte nur 'führende Unterstriche', der Code verwendet aber zwei (Name-Mangling) - Hinweis präzisiert (Konvention, Name-Mangling, kein strikter Zugriffsschutz), cb/cc weiterhin allgemein für OOP zu beantworten. Weitere Umsetzungen: 3a jetzt 'vier typische Phasen', Lösung erlaubt ausdrücklich nicht aufeinanderfolgende Phasen und gleichwertige Wasserfall-Darstellungen; 1a-Tabelle: Zeile Leistungsaufnahme als 'nicht bewertet, nur für b)' gekennzeichnet, Antworttabelle um gewichtete Einzelwerte erweitert (passend zur Punktvergabe in der Lösung); 2f-Lösung stellt das erratbare Muster in den Vordergrund statt 'kurz'; 2ga fragt nach zwei weiteren Rechten neben dem Auskunftsrecht, das die Situation bereits vorgibt; Bearbeitungshinweise: Rundungsregel entfernt (keine relevanten Rundungen im Blatt, als allgemeine Regel fragwürdig), Hilfsmittel um 'ohne Kommunikationsmöglichkeit mit Dritten' und Verweis auf die Angaben in Einladung und Prüfungsunterlagen ergänzt; Gewichtssumme 100 % in der Lösung zu 1a als Kontrolle vermerkt. Nicht übernommen: zusätzlicher Grenzwert 30 in der Eingabe des Schreibtischtests (optional, würde Aufgabe und Lösung ändern, kein Fehler); Kommentar, die Aussage zur Stichwortantwort sei keine allgemeine IHK-Regel (steht bereits ausdrücklich als Hinweis dieses Übungsblatts)."
  - runde: 4
    datum: 2026-09-28
    ergebnis: "2 Re-Reviews eingearbeitet, beide ohne verbliebenen Rechen- oder Fachfehler. Eine Meldung geprüft und verworfen: Ein Review sah den YAML-Block mitten im Eintrag abgeschnitten (ungültig) - die Datei wurde geprüft, der Block ist vollständig und gültig, das Abschneiden geschah beim Einfügen ins Review. Umgesetzt: 2g-Abgrenzung der Anonymisierung weniger absolut ('bei wirksamer Anonymisierung ist eine Identifizierung mit vernünftigerweise einsetzbaren Mitteln nicht mehr möglich'); 4e/ec unterscheidet jetzt zwischen tatsächlichen Kosten (1 656 EUR) und entgangenem Umsatz (900 EUR), Frage und Lösung sprechen von wirtschaftlicher Gesamtbelastung; 4e/eb Risiken in der Lösung in vier Stichpunkte gegliedert; Einheiten ergänzt (1b mit h/Tag und Tage/Jahr, 4a Rückgabewert in Minuten), passend zum Hinweis, Ergebnisse mit Einheiten anzugeben; 1e/eb-Formulierung präzisiert (Verzeichnisdienst, bereitgestellt auf einem Domänencontroller). Nicht geändert: 3a-Lösung nennt weiterhin fünf gängige Phasen mit dem ausdrücklichen Hinweis, dass vier gefordert sind und gleichwertige Darstellungen zählen - eine Review bewertet das als sauber gelöst, die andere als minimale Unschärfe, beides vertretbar. Nicht übernommen: Vorschlag, die Review-Historie aus der Lernfassung zu entfernen (entspricht der in der gesamten Wiki-Sammlung durchgängigen Konvention). Den Status setzt David."
  - runde: 5
    datum: 2026-09-28
    ergebnis: "Abschluss-Selbstcheck, danach von David final freigegeben. Alle Lösungswerte unabhängig aus den Tabellen der Dateien neu berechnet und mit dem Lösungsblatt abgeglichen (Netzplan inkl. kritischem Pfad und Verzug, Nutzwertanalyse, Stromkosten, Subnetting, Schreibtischtest, Zuordnungen 1c und 4d, KI-Kosten); Python-Ausschnitte kompiliert und ausgeführt, Ausschnitt 1 ist wie vorgesehen fehlerhaft. Punktsummen je Aufgabe 25, gesamt 100. Drei Kleinigkeiten behoben: nicht geschlossene Klammer in der Tabellenzeile zur Leistungsaufnahme, doppelte Aussage zur 4 x 25-Punkte-Verteilung im Formathinweis, und die YAML-Quellenangabe nannte 'BSI Grundlagen zur Härtung', obwohl diese Quelle nicht eingesehen wurde - auf die tatsächlich gegengeprüfte DSGVO-Grundlage begrenzt, Härtungs- und Passwortmaßnahmen ausdrücklich als allgemein üblicher Prüfungsstoff ohne Einzelbeleg gekennzeichnet."
  - runde: 6
    datum: 2026-09-28
    ergebnis: "Redaktionelle Änderung nach Freigabe, auf Wunsch von David bei weiterhin gültigem Status Final: Der Punkte-Noten-Schlüssel ist jetzt als Orientierungswert gekennzeichnet (kann je nach IHK bzw. Prüfung abweichen, nicht Bestandteil der echten AP1-Bewertung) statt als 'übliches IHK-Schema'. Angleichung an das AP2-Blatt; Zahlen des Schlüssels unverändert. Aufgaben, Lösungen und Punkte unverändert."
naechste_review: "Bei Änderung des Prüfungskatalogs oder nach Auswertung neuer AP1-Prüfungen"
```