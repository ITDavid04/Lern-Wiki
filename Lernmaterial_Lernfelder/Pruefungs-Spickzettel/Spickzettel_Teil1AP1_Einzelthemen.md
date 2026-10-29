# Prüfungs-Spickzettel Teil 1 – AP1-Einzelthemen

> **Zielgruppe:** Umschüler FIAE/FISI; die AP1-Prüfung enthält berufsbildübergreifende Inhalte und ist inhaltlich für alle IT-Ausbildungsberufe identisch, nicht nur für die Fachrichtungen des Fachinformatikers
> **Prüfungsrelevanz:** Teil 1 der gestreckten Abschlussprüfung ("Einrichten eines IT-gestützten Arbeitsplatzes"), 90 Minuten, 20% Gewichtung an der Gesamtnote
> **Lernzeit:** 45–60 Minuten (Wiederholungskarten, kein Erstlernen)
> **Status:** Draft
> **Stand:** 2026-09-22
>
> **Hinweis zum Format:** Dies sind kompakte Wiederholungskarten für Themen, die in keinem bestehenden Lernfeld-Artikel ausführlich behandelt werden, aber laut Katalogänderungen 2025 und/oder echten Prüfungen wiederkehrend Prüfungsstoff sind. Themen, die bereits ausführlich in einem Lernfeld- oder Mathe-Artikel stehen (z. B. Zahlensysteme, Pseudocode), werden hier bewusst nicht dupliziert.

**Legende (redaktionelle Einschätzung, keine offizielle IHK-Gewichtung):** 🔴 unmittelbar auf typische Prüfungsaufgaben anwendbar · 🟡 wichtiges Verständnis-/Transferwissen · 🟢 vertiefendes Kontextwissen

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie berechnet man Netzplantechnik (FAZ/FEZ/SAZ/SEZ, Puffer, kritischer Pfad)? | [→ 1](#1-netzplantechnik) |
| 2 | Wie bewertet man Angebote systematisch mit einer Nutzwertanalyse? | [→ 2](#2-nutzwertanalyse) |
| 3 | Wofür wird Künstliche Intelligenz im betrieblichen Alltag sinnvoll eingesetzt? | [→ 3](#3-künstliche-intelligenz-im-betrieblichen-einsatz) |
| 4 | Was unterscheidet einen Syntaxfehler von einem Logikfehler? | [→ 4](#4-syntaxfehler-vs-logikfehler) |
| 5 | Was bedeutet Barrierefreiheit konkret bei IT-Systemen und Websites? | [→ 5](#5-barrierefreiheit) |

---

## 1. Netzplantechnik

> **Grundprinzip:** Ein Netzplan ist wie eine Staffel: Der nächste Läufer kann erst starten, wenn der langsamste seiner Vorgänger angekommen ist. Vier Fragen beantwortet die Rechnung: Wie lange dauert das Projekt insgesamt? Welche Vorgänge dürfen sich auf keinen Fall verspäten? Wie viel Luft haben die anderen – für sich allein, und bis zum nächsten Nachbarn?

### 1.1 Der Knoten

```text
FAZ   Dauer   FEZ
   Nr. / Bezeichnung
SAZ    GP·FP   SEZ
```

| Kürzel | Bedeutung | Frage dahinter |
|---|---|---|
| FAZ | Frühester Anfangszeitpunkt | Wann kann ich frühestens loslegen? |
| FEZ | Frühester Endzeitpunkt | Wann bin ich frühestens fertig? |
| SAZ | Spätester Anfangszeitpunkt | Wann muss ich spätestens loslegen? |
| SEZ | Spätester Endzeitpunkt | Wann muss ich spätestens fertig sein? |
| GP | Gesamtpuffer = SAZ − FAZ | Wie viel Luft habe ich bis zum Projektende? |
| FP | Freier Puffer = kleinster FAZ der Nachfolger − eigener FEZ | Wie viel Luft habe ich, bevor mein direkter Nachfolger warten muss? |

### 1.2 Die drei Durchläufe

1. **Vorwärtsrechnung** (links → rechts): FEZ = FAZ + Dauer. Startvorgang: FAZ = 0. Bei mehreren Vorgängern ist der FAZ eines Vorgangs das **Maximum** der FEZ aller Vorgänger.
2. **Rückwärtsrechnung** (rechts → links): SAZ = SEZ − Dauer. Bei einem einzigen Endvorgang gilt SEZ = FEZ. Gibt es **mehrere Endvorgänge**, erhalten alle denselben SEZ – den gemeinsamen Projektendtermin, also das Maximum der FEZ aller Endvorgänge (alternativ: ein gemeinsamer Endknoten). Bei mehreren Nachfolgern ist der SEZ eines Vorgangs das **Minimum** der SAZ aller Nachfolger.
3. **Puffer**: GP = SAZ − FAZ (entspricht auch SEZ − FEZ). FP = kleinster FAZ der Nachfolger − eigener FEZ. Bei Endvorgängen ohne regulären Nachfolger wird dafür der gemeinsame Projektendtermin (bzw. ein gedachter Endknoten) als Nachfolger betrachtet.

**Kritischer Pfad:** eine lückenlose Kette von Vorgängen mit GP = 0, vom Start bis zum Ende. Die Summe ihrer Dauern ergibt die Projektdauer. Bei komplexeren Netzplänen kann es **mehrere** kritische Pfade parallel geben.

> **Wichtig für die Prüfung:** Vorwärts wird maximiert, rückwärts minimiert – wer das vertauscht, berechnet die Rückwärtsrechnung und damit die Puffer falsch, was oft erst am Ende auffällt. Kontrolle: Der **FAZ** jedes Startvorgangs (ohne Vorgänger) ist 0 – das gilt immer. Der **SAZ** eines Startvorgangs ist dagegen nur dann 0, wenn dieser Vorgang auf dem kritischen Pfad liegt. Gibt es mehrere Startvorgänge mit unterschiedlicher Dauer, hat nur der kritische darunter SAZ = 0 – die anderen haben Puffer und damit SAZ > 0. 🔴

🔴 **Stolperstein:** FP wird mit dem **FAZ** des Nachfolgers berechnet, nicht mit dessen SAZ – nimmt man versehentlich den SAZ, kommt rechnerisch plausibel wieder der GP heraus, was den Fehler unauffällig macht. FP ist außerdem nie größer als GP; auf dem kritischen Pfad sind beide 0.

> **IHK-Typfrage:** *"Ein Vorgang hat einen Gesamtpuffer von 3 Tagen und verzögert sich um 5 Tage. Um wie viele Tage verschiebt sich das Projektende?"*
> **Musterantwort:** Für einen einzelnen Vorgang gilt (unter der üblichen Prüfungsannahme, dass keine weiteren Abhängigkeiten oder Gegenmaßnahmen berücksichtigt werden): max(0, Verzögerung − Gesamtpuffer). Hier: 5 − 3 = **2 Tage** Verschiebung des Projektendes.

🟡 **Kontextwissen:** Beim Zeichnen als Gantt-Diagramm werden die Vorgänge als Balken auf einer Zeitachse dargestellt (Balkenlänge = Dauer, beginnend bei FAZ), der Puffer als gestrichelter/schraffierter Balken rechts angehängt, der kritische Pfad farblich hervorgehoben. Der Netzplan berechnet die Abhängigkeiten, der Gantt macht die Zeitplanung sichtbar – Prüfungsaufgaben verlangen oft beides nacheinander.

---

## 2. Nutzwertanalyse

> **Grundprinzip:** Bei mehreren Angeboten mit unterschiedlich wichtigen Kriterien (Preis, Leistung, Service) hilft reines Bauchgefühl nicht weiter. Die Nutzwertanalyse macht die Bewertung nachvollziehbar: Jedes Kriterium bekommt ein Gewicht, jede Option pro Kriterium eine Punktzahl – am Ende gewinnt die höchste gewichtete Summe.

### 2.1 Rechenschema

| Kriterium | Gewicht | Option A (Punkte) | A gewichtet | Option B (Punkte) | B gewichtet |
|---|---|---|---|---|---|
| Preis | 40% | 8 | 3,2 | 6 | 2,4 |
| Leistung | 35% | 6 | 2,1 | 9 | 3,15 |
| Service | 25% | 7 | 1,75 | 7 | 1,75 |
| **Summe** | 100% | | **7,05** | | **7,3** |

Gewichteter Wert = Punktzahl × Gewicht. Summe aller gewichteten Werte je Option ergibt den Nutzwert – die Option mit der höchsten Nutzwertsumme schneidet nach diesem Bewertungsmodell am besten ab (hier: Option B).

> **Wichtig für die Prüfung:** Gewichte werden üblicherweise so festgelegt, dass ihre Summe 100% (bzw. 1,0) ergibt – rechnet die Aufgabe mit deutlich abweichenden Summen, Aufgabenstellung genau prüfen und ggf. normieren; kleine Abweichungen können auch nur Rundung sein. Sind die Punktwerte pro Kriterium nicht bereits vorgegeben, müssen sie anhand nachvollziehbarer Kriterien vergeben und ggf. begründet werden. 🔴

🟡 **Kontextwissen:** Auch bekannt als Entscheidungsmatrix oder Punktbewertungsverfahren – der Name in der Aufgabenstellung kann variieren, das Rechenschema bleibt gleich.

---

## 3. Künstliche Intelligenz im betrieblichen Einsatz

> **Grundprinzip:** In den für diesen Spickzettel ausgewerteten AP1-Aufgaben steht bei KI die Fähigkeit im Vordergrund, sinnvolle Einsatzfelder in einem gegebenen Geschäftsprozess zu erkennen und wirtschaftlich zu bewerten – nicht technisches ML-Wissen.

### 3.1 Typische Einsatzfelder in einem Kundenprozess

| Prozessschritt | Mögliche KI-Unterstützung |
|---|---|
| Datenerfassung/-aktualisierung | Recherche und Aktualisierung zulässig nutzbarer Kunden-/Firmendaten unter Beachtung von Datenschutz und Datenqualität |
| Kategorisierung/Vorstrukturierung | KI-gestützte Analyse und Einordnung von Eingaben |
| Terminfindung | Automatische Terminvorschläge, Kalenderabgleich |
| Recherche | Automatisches Auffinden ähnlicher Fälle, passender Unterlagen |
| Kundenkontakt (einfache Fälle) | Chatbot für Standardanfragen |

> **IHK-Typfrage:** *"Nennen Sie einen möglichen Vorteil des KI-Einsatzes für Mitarbeitende."*
> **Musterantwort:** Entlastung von wiederkehrenden Routineaufgaben – dadurch bleibt mehr Zeit für anspruchsvollere, nicht automatisierbare Tätigkeiten.

🔴 **Stolperstein:** Bei Kosten-Nutzen-Aufgaben zu KI-Tools wird oft nicht nur der direkte Anschaffungs-/Lizenzpreis verglichen, sondern zusätzlich der **entgangene Umsatz** durch Einarbeitungs-/Schulungszeit eingerechnet – beides zusammenzählen, nicht nur die Lizenzkosten.

🟡 **Kontextwissen:** Auch Nachteile/Risiken können gefragt sein: fehlerhafte oder erfundene Ergebnisse, unzulässige Verarbeitung personenbezogener bzw. vertraulicher Daten, mögliche Verzerrungen in den Ergebnissen, Akzeptanzprobleme bei Mitarbeitenden, Anbieterabhängigkeit sowie laufende Lizenz-/Integrations-/Kontrollkosten. KI-Ergebnisse sollten grundsätzlich nicht ungeprüft übernommen werden.

---

## 4. Syntaxfehler vs. Logikfehler

> **Grundprinzip:** Ein Syntaxfehler verletzt die grammatischen Regeln der Programmiersprache – der Code kann an dieser Stelle nicht korrekt übersetzt bzw. interpretiert werden. Ein Logikfehler liegt vor, wenn der Code formal gültig ist und ausgeführt werden kann, aber nicht das beabsichtigte Ergebnis liefert.

| | Syntaxfehler | Logikfehler |
|---|---|---|
| Was ist falsch? | Verstößt gegen die Grammatik der Sprache | Code ist formal gültig, bildet aber die gewünschte Logik falsch ab |
| Beispiel | Fehlende schließende Klammer, fehlendes Semikolon, ungültige Anweisungsstruktur | Ergebnis wird in der falschen Variable gespeichert (z. B. `umfang` statt `flaeche`), Addition statt Multiplikation, falsche Vergleichsrichtung |
| Erkennung | Durch Compiler/Interpreter, meist vor der Ausführung | Meist erst durch Tests, Debugging oder Schreibtischtest |

🟡 **Begriffshinweis:** In der Informatik wird der Gegensatz zum Syntaxfehler nicht einheitlich benannt – neben "Logikfehler" ist auch "Semantikfehler" gebräuchlich. In AP1-Aufgaben ist damit meist genau der oben beschriebene inhaltliche Fehler gemeint. Manche formal-semantischen Fehler (z. B. Typfehler in statisch typisierten Sprachen: `int x = "Text"`) sind davon zu unterscheiden – die erkennt bereits der Compiler, sie sind also kein Logikfehler im hier beschriebenen Sinn.

🔴 **Stolperstein:** Ein Logikfehler lässt sich nicht am "Programm startet nicht" erkennen – das Programm läuft in der Regel, liefert aber ein falsches Ergebnis. Erkennbar meist nur durch **Schreibtischtest oder Testfälle mit bekanntem Erwartungswert** – deshalb sind Testkonzepte so wichtig.

---

## 5. Barrierefreiheit

> **Grundprinzip:** Barrierefreiheit bedeutet, dass IT-Systeme, Software und Websites von möglichst vielen Menschen selbstständig genutzt werden können – insbesondere auch bei motorischen, visuellen, auditiven oder kognitiven Einschränkungen.

### 5.1 Konkrete Maßnahmen

| Bereich | Beispielmaßnahmen |
|---|---|
| Arbeitsplatz | Höhenverstellbarer Tisch, alternative Tastatur/Maus, großer Monitor, Braillezeile, Spracheingabe |
| Website | Alternativtexte für Bilder, ausreichender Farbkontrast, vollständige Tastaturbedienbarkeit, verständliche Überschriftenstruktur, Screenreader-Kompatibilität |
| Software allgemein | Vergrößerbare Schrift, anpassbare Darstellung/Farbschemata, Untertitel, klare Beschriftungen statt reiner Symbole, sichtbarer Tastaturfokus |

🟡 **Kontextwissen:** In Deutschland gelten nach dem Barrierefreiheitsstärkungsgesetz (BFSG) seit dem **28. Juni 2025** Barrierefreiheitsanforderungen für bestimmte Produkte und verbraucherbezogene Dienstleistungen, darunter unter bestimmten Voraussetzungen auch Teile des E-Commerce – für die Prüfung reicht das Grundverständnis der technischen Maßnahmen, nicht die Gesetzesdetails zum genauen Anwendungsbereich.

---

## 6. Weitere Kurzthemen – kompakte Einzelabfragen

> Kompakt gehalten, da seltener mit hoher Punktzahl geprüft, aber wiederkehrend als Einzelfrage.

**Domäneneinbindung:** Ein Client wird in eine zentral verwaltete Domäne aufgenommen (z. B. eine Active-Directory-Domäne), statt in einer lokalen Arbeitsgruppe zu bleiben. Dadurch werden zentrale Authentifizierung, Benutzer-/Gruppenverwaltung und die Verteilung einheitlicher Richtlinien (Group Policies) über einen Domänencontroller möglich, statt jeden PC einzeln zu pflegen. Voraussetzung sind erreichbare Domänendienste und eine passende Netzwerkkonfiguration, insbesondere funktionierendes DNS.

**Statische vs. dynamische Website:** Eine statische Website liefert vorbereitete Dateien aus, deren Inhalt beim Aufruf nicht erst individuell erzeugt wird. Eine dynamische Website erzeugt oder verändert Inhalte zur Laufzeit – serverseitig (z. B. aus einer Datenbank), clientseitig (z. B. per JavaScript) oder durch nachgeladene Daten über APIs. Typische serverseitige Technologien: PHP, Python, Java, JavaScript mit Node.js, C#/.NET.

**IMAP vs. POP3:** IMAP verwaltet und synchronisiert E-Mails auf dem Server, sodass mehrere Geräte denselben Ordner- und Nachrichtenstand sehen – deshalb bei mehreren Geräten meist die geeignetere Wahl. POP3 lädt Nachrichten primär zur lokalen Speicherung herunter; ob sie danach auf dem Server verbleiben oder gelöscht werden, hängt von der Konfiguration des Mailprogramms ab, nicht zwingend von einer festen Standardeinstellung.

**Open-Source vs. proprietäre Software:** Open Source beschreibt zunächst ein **Lizenzmodell**, nicht den Preis – der Quellcode ist gemäß Lizenz einsehbar und darf häufig verändert/weitergegeben werden (kann aber kostenpflichtig sein). Mögliche Vorteile: Anpassbarkeit, Transparenz, oft geringere Herstellerabhängigkeit. Bei proprietärer Software kontrolliert der Rechteinhaber Quellcode und Nutzungsrechte; mögliche Vorteile: zentraler Ansprechpartner, verbindliche Supportverträge, einheitliche Produktverantwortung. Preis, Qualität und Dokumentationsgüte hängen nicht allein vom Lizenzmodell ab.

**Hashwert beim Softwaredownload:** Dient der **Integritätsprüfung** – der Hashwert der heruntergeladenen Datei wird mit dem vom Anbieter veröffentlichten Wert verglichen. Stimmen sie überein, wurde die Datei nicht verändert oder beschädigt. Das prüft primär Integrität, nicht automatisch Authentizität: Ein passender Hash beweist die Unverändertheit nur zuverlässig, wenn der Vergleichswert selbst aus einer vertrauenswürdigen Quelle stammt.

---

## Typische Prüfungsfallen

| # | Falle | Richtigstellung |
|---|---|---|
| 1 | Beim Netzplan rückwärts wieder das Maximum nehmen | Vorwärts Maximum, rückwärts Minimum – sonst ist die ganze Rückwärtskette falsch |
| 2 | Freier Puffer wird mit dem SAZ des Nachfolgers berechnet | FP nutzt den FAZ des Nachfolgers, nicht den SAZ |
| 3 | Nutzwertanalyse-Gewichte summieren sich nicht auf 100% | Vor dem Rechnen prüfen, ggf. normieren |
| 4 | Ein Programm ohne Fehlermeldung ist automatisch korrekt | Logikfehler zeigen sich nicht als Absturz, sondern als falsches Ergebnis |
| 5 | IMAP und POP3 seien bei mehreren Geräten gleich gut geeignet | IMAP synchronisiert den serverseitigen Nachrichten-/Ordnerstand; POP3 ist primär auf lokales Herunterladen ausgerichtet |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Netzplan – FAZ/FEZ/SAZ/SEZ | Frühester/spätester Anfangs-/Endzeitpunkt eines Vorgangs |
| Kritischer Pfad | Lückenlose Kette von Vorgängen mit Gesamtpuffer = 0 vom Start bis zum Ende; mehrere kritische Pfade möglich |
| Nutzwertanalyse | Gewichtete Kriterien × Punktzahl je Option; höchste Nutzwertsumme schneidet im Modell am besten ab |
| Syntaxfehler | Verstößt gegen die Grammatik der Sprache; kann so nicht korrekt übersetzt/interpretiert werden |
| Logikfehler | Code ist formal gültig, liefert aber ein falsches Ergebnis |
| Barrierefreiheit | Nutzbarkeit für möglichst viele Menschen, unabhängig von motorischen, visuellen, auditiven oder kognitiven Einschränkungen |
| Domäneneinbindung | Zentrale Verwaltung von Benutzern/Richtlinien statt lokaler Einzelkonfiguration |
| Hashwert (Download) | Prüft Integrität der heruntergeladenen Datei gegen den Originalwert |

---

## Merksätze für die Prüfung

> Vorwärts das Maximum, rückwärts das Minimum – wer das vertauscht, verliert nicht einen Wert, sondern die ganze Kette.

> Freier Puffer schaut auf den Nachbarn, Gesamtpuffer schaut aufs Projektende.

> Syntaxfehler verletzt die Regel der Sprache. Logikfehler: Das Programm läuft, tut aber das Falsche.

---

```yaml
dokument: Pruefungs-Spickzettel-Teil1-AP1
lernfeld: "Querschnittsthema, kein einzelnes Lernfeld (analog zu Mathe_Was_Notwendig_ist)"
titel: "Prüfungs-Spickzettel Teil 1 – AP1-Einzelthemen"
typ: "Typ A – Kompakte Wiederholungskarten"
status: draft
stand: 2026-09-22
quellen_intern:
  - "Teil 1 einer dreiteiligen Serie (AP1 / WiSo-Multiple-Choice / AP2), analog zur Mathe_Was_Notwendig_ist-Serie als eigener Querschnitts-Ordner angelegt"
  - "Themenauswahl basiert auf einem Gesamtaudit des Wiki-Repos gegen echtes IHK-Prüfungsmaterial in vorheriger Session"
quellen_fachlich:
  - titel: "Prüfungskatalog 2025 für AP1 der IT-Berufe (Änderungsvergleich 2020→2025)"
    herausgeber: "U-Form Verlag / ZPA Nord-West"
    status: "Web-verifiziert, bestätigt u.a. Aufnahme von KI, Barrierefreiheit, Domäneneinbindung, Urheberschutz-Grundlagen in den AP1-Katalog"
  - titel: "AP1 Frühjahr 2025 (echte Prüfung mit Lösungen)"
    herausgeber: "ZPA Nord-West"
    status: "Direkt eingesehen - bestätigt Netzplantechnik (10 von 100 Punkten), KI-Aufgabe (25 von 100 Punkten), Nutzwertanalyse-artige Entscheidungsmatrix, Hashwert-Zweck, IMAP-Begründung, statische/dynamische Website"
  - titel: "AP2 Winter 2023/24 FISI (echte Prüfung)"
    herausgeber: "ZPA Nord-West"
    status: "Bestätigt Netzplantechnik als wiederkehrendes, nicht auf einen Prüfungstermin beschränktes Thema"
  - titel: "Community-Lernzettel AP1 (Reddit, u/DeFyuseOW, 01.03.2025)"
    herausgeber: "Öffentlich geteilt, Pseudonym"
    status: "Als Sekundärquelle zur Bestätigung der Katalog-Themen herangezogen, nicht wörtlich übernommen"
review_historie:
  - runde: 1
    datum: 2026-09-22
    ergebnis: "Erstdraft erstellt. Themenauswahl bewusst auf Einzelthemen begrenzt, die in keinem bestehenden Lernfeld-Artikel ausführlich stehen - Zahlensysteme, Pseudocode, Grundlagen-Netzwerktechnik etc. werden bewusst NICHT dupliziert, sondern bleiben in ihren jeweiligen Lernfeld-Artikeln. Netzplantechnik als umfangreichstes Einzelthema mit eigenem Abschnitt, da in zwei unabhängigen echten Prüfungen mit signifikantem Punktgewicht bestätigt. Bewusst keine wörtliche Übernahme von internem Kursmaterial - alle Aussagen eigenständig formuliert und gegen die oben genannten öffentlichen Quellen verifiziert."
  - runde: 2
    datum: 2026-09-22
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (eine Review, mit konkretem Gegenbeispiel bewiesen): Der Netzplan-Kontrollsatz 'SAZ des allerersten Vorgangs muss 0 ergeben' war schlicht falsch - gilt nur, wenn der Startvorgang auf dem kritischen Pfad liegt. Gegenbeispiel: zwei Startvorgänge A (Dauer 1) und B (Dauer 5) ergeben SAZ(A)=4, nicht 0. Korrigiert auf 'FAZ des Startvorgangs ist immer 0, SAZ nur dann, wenn er auf dem kritischen Pfad liegt'. Von allen drei Reviews unabhängig gefordert: Syntax-/Semantikfehler-Abschnitt war zu absolut (Semantikfehler werden nicht grundsätzlich erst zur Laufzeit erkannt, z.B. Typfehler in statisch typisierten Sprachen) - umbenannt zu 'Logik-/Semantikfehler', Formulierungen durchgängig entschärft, Cheatsheet/Merksatz/Prüfungsfalle nachgezogen, Anker-Link an geänderte Überschrift angepasst. Von zwei Reviews bestätigt: POP3 entfernt Mails nicht grundsätzlich standardmäßig vom Server (konfigurationsabhängig); Open Source ist primär ein Lizenz-/Quellcode-Konzept, nicht primär ein Preis-Konzept ('kostenlos' als Hauptmerkmal entfernt); dynamische Website nicht auf serverseitige Generierung bei jedem Aufruf begrenzt (auch clientseitig/API-basiert möglich); Barrierefreiheit von 'körperliche Einschränkungen' auf motorisch/visuell/auditiv/kognitiv erweitert; BFSG-Datum auf 28. Juni 2025 präzisiert. KI-Grundprinzip von pauschaler 'aktuelle AP1'-Aussage auf 'in den ausgewerteten AP1-Aufgaben' bezogen, Risikoliste um Datenschutz/Verzerrungen/Anbieterabhängigkeit erweitert. Nutzwertanalyse: Normierungspflicht und 'höchste Summe gewinnt' als Modellaussage statt objektive Tatsache entschärft. Zielgruppen-Angabe korrigiert (FIAE/FISI sind selbst bereits Fachrichtungen, 'alle Fachrichtungen' war widersprüchlich; AP1 gilt für alle IT-Ausbildungsberufe). 'Merksätze für das Fachgespräch' zu 'Merksätze für die Prüfung' korrigiert, da AP1 eine rein schriftliche Prüfung ohne Fachgespräch-Komponente ist. Ein Vorschlag ('IHK-Kernfragen'/'IHK-Typfrage' umbenennen) bewusst nicht übernommen - feste, projektweite Konvention über alle anderen Wiki-Artikel hinweg (bereits in früheren Runden anderer Artikel mit derselben Begründung abgelehnt)."
  - runde: 3
    datum: 2026-09-22
    ergebnis: "3 Re-Reviews eingearbeitet. Wichtigster neuer Fund (zwei Reviews, mit Gegenbeispiel belegt): Die Aussage 'Endvorgang: SEZ = FEZ' galt nur für einen einzelnen Endvorgang - bei mehreren Endvorgängen mit unterschiedlichem FEZ hätte diese Regel alle Endvorgänge künstlich kritisch gemacht. Korrigiert: Bei mehreren Endvorgängen erhalten alle denselben SEZ (das Maximum aller FEZ = gemeinsamer Projektendtermin). FP-Definition um Hinweis auf gemeinsamen Endknoten bei Endvorgängen ergänzt. Zweiter Fund (eine Review, gut begründet): Der kombinierte Titel 'Logik-/Semantikfehler' stand im Widerspruch zum eigenen Typfehler-Beispiel (Typfehler sind formal-semantische, aber keine Logikfehler im beschriebenen Sinn) - Abschnitt auf 'Logikfehler' als durchgängigen Primärbegriff umgestellt, uneinheitliche Verwendung von 'Semantikfehler' in einen eigenen Begriffshinweis ausgelagert statt in der Haupttabelle vermischt. Alle Folgestellen (Kernfrage, Anker, Cheatsheet, Prüfungsfalle) konsistent nachgezogen, dabei einen durch die Umstellung entstandenen doppelten Cheatsheet-Eintrag beseitigt. Drei weitere Cheatsheet-Zeilen (Kritischer Pfad, Nutzwertanalyse, Syntaxfehler, Barrierefreiheit) standen noch mit der alten, bereits im Haupttext entschärften Formulierung da - synchronisiert. Kleinere Präzisierungen: statische Website (auch statische Seiten variieren je URL, entscheidend ist Nicht-Erzeugung pro Aufruf), KI-Datenerfassung um Datenschutz-Einschränkung ergänzt, Einleitungssatz zu Lernfeld-Verweisen abgeschwächt (versprach konkrete Links, die im Dokument nicht existierten). Eine vermeintliche Tippfehler-Meldung ('entgangene' statt 'entgangener Umsatz') geprüft und verworfen - 'der entgangene Umsatz' ist mit schwacher Adjektivendung nach bestimmtem Artikel grammatikalisch korrekt, keine Änderung nötig. Zwei Vorschläge (Prozentzeichen mit Leerzeichen, geschlechtergerechte Sprache) bewusst nicht übernommen - beides würde von der im gesamten übrigen Wiki durchgängig verwendeten Schreibweise abweichen."
naechste_review: "Externe Prüfung ausstehend"
```