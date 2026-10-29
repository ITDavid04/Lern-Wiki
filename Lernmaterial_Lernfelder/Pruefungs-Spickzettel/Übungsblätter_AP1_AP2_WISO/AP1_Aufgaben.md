# AP1-Übungsblatt – Einrichten eines IT-gestützten Arbeitsplatzes

> **Zielgruppe:** Umschülerinnen und Umschüler sowie Auszubildende in IT-Berufen, insbesondere Fachinformatiker/in Anwendungsentwicklung und Systemintegration
> **Zweck:** Übungsblatt zur Vorbereitung auf Teil 1 der Abschlussprüfung (AP1), als Ergänzung zum Wiederholungs-Spickzettel ([Spickzettel Teil 1, AP1](../Spickzettel_Teil1AP1_Einzelthemen.md)). Lösungen: [AP1.1_Lösungen.md](AP1.1_Lösungen.md).
> **Status:** Final
> **Stand:** 2026-09-28
>
> **Hinweis zum Format:** Die AP1 besteht aus vier ungebundenen Aufgaben mit zusammenhängender Ausgangssituation (90 Minuten, 100 Punkte, je Aufgabe 20 bis 30 Punkte). Dieses Übungsblatt folgt diesem Aufbau mit vier Szenario-Aufgaben und mehreren Unterpunkten. Die 100 Punkte sind dabei bewusst gleichmäßig auf vier Aufgaben zu je 25 Punkten verteilt; die echte AP1 kann sie anders auf ihre vier Aufgaben verteilen. Umfang und Schwierigkeit entsprechen einer Übungsklausur, eine 1:1-Simulation der echten Prüfung ist es nicht.
>
> **Hinweis:** Ausgangssituation, Firmennamen, Zahlen und Aufgaben sind frei erfunden. Keine Aufgabe ist einer realen Prüfung entnommen oder nachgebildet.

---

## Bearbeitungshinweise

- Bearbeitungszeit: 90 Minuten, Gesamtpunktzahl: 100 Punkte
- Lesen Sie den Text der Aufgaben ganz durch, bevor Sie mit der Bearbeitung beginnen.
- Halten Sie sich beim Umfang der Antwort an die Vorgabe der Aufgabenstellung. Werden vier Angaben gefordert und Sie führen sechs an, zählen nur die ersten vier.
- Stichwortartige Antworten sind zulässig, sofern nicht ausdrücklich ganze Sätze verlangt werden.
- Erlaubtes Hilfsmittel in diesem Übungsblatt: nicht programmierbarer, netzunabhängiger Taschenrechner ohne Kommunikationsmöglichkeit mit Dritten. In der echten Prüfung gelten die Angaben in Einladung und Prüfungsunterlagen.
- Geben Sie Rechenwege und Ergebnisse mit den geforderten Einheiten an.

---

## Ausgangssituation

Sie arbeiten bei der **Nordlicht Systemhaus GmbH** in Hamburg und betreuen die neu eröffnete **Zahnarztpraxis Lindner & Kollegen**. In der Praxis arbeiten drei Behandelnde und sechs weitere Mitarbeitende. Bisher wurde alles auf Papier und mit privaten Geräten erledigt. Sie richten nun die IT der Praxis ein.

Bearbeiten Sie die folgenden Aufgaben:

- Auswahl und Anschluss der Empfangs-PCs und Planung des Praxisnetzes
- IT-Sicherheit und Datenschutz in der Praxis
- Planung der IT-Umstellung als Projekt
- Praxissoftware, Fehlersuche und Einsatz von KI

---

## 1. Aufgabe (25 Punkte)

Am Empfang sollen mehrere Arbeitsplatzrechner aufgestellt werden. Es stehen drei Mini-PCs zur Auswahl. Die Praxisleitung hat die Kriterien gewichtet (die Gewichtungen ergeben zusammen 100 %). Die Geräte wurden mit Punkten von 1 (schlecht) bis 5 (sehr gut) bewertet.

| Kriterium | Gewichtung | Mini-PC A | Mini-PC B | Mini-PC C |
|---|---:|---:|---:|---:|
| Rechenleistung | 30 % | 4 | 5 | 3 |
| Energieeffizienz | 20 % | 5 | 3 | 4 |
| Preis | 30 % | 3 | 2 | 5 |
| Anschlussvielfalt | 20 % | 3 | 4 | 4 |
| Leistungsaufnahme im Betrieb, Mittelwert (nicht bewertet, wird nur in Teilaufgabe b benötigt) | – | 15 W | 20 W | 12 W |

**a)** Führen Sie eine Nutzwertanalyse durch. Geben Sie die gewichteten Einzelwerte an, berechnen Sie den Nutzwert für jeden Mini-PC und nennen Sie das Gerät, für das Sie sich entscheiden. **7 Punkte**

| Gewichteter Wert | Mini-PC A | Mini-PC B | Mini-PC C |
|---|---|---|---|
| Rechenleistung | | | |
| Energieeffizienz | | | |
| Preis | | | |
| Anschlussvielfalt | | | |
| **Nutzwert (Summe)** | | | |

Entscheidung: ______________________

**b)** Der ausgewählte Mini-PC läuft an 250 Tagen im Jahr täglich 10 Stunden. Der Strompreis beträgt 0,34 EUR je kWh. Berechnen Sie die Stromkosten für die geplante Nutzungsdauer von 4 Jahren. Geben Sie den Rechenweg an. **4 Punkte**

**c)** Am Mini-PC befinden sich mehrere Anschlüsse. Ordnen Sie jedem Anschluss die passende Verwendung zu. Tragen Sie die Ziffer der Verwendung ein. **4 Punkte**

| Anschluss | Zuordnung | Verwendung |
|---|---|---|
| a) HDMI | | 1. Analoge Tonausgabe an einem Headset |
| b) RJ45 | | 2. Netzwerkkabel zum Switch |
| c) 3,5-mm-Klinke | | 3. Anschluss für Tastatur und Maus |
| d) USB-A | | 4. Digitale Übertragung von Bild und Ton zum Monitor |

**d)** Das Praxisnetz verwendet das Netz **192.168.40.0/27**. **7 Punkte**

- da) Geben Sie die Subnetzmaske in Dezimalschreibweise an. *(2 Punkte)*
- db) Geben Sie die Broadcast-Adresse des Netzes an. *(2 Punkte)*
- dc) Wie viele Geräte können in diesem Netz nutzbare Adressen erhalten? *(1 Punkt)*
- dd) Der Router erhält die erste nutzbare Adresse des Netzes. Wie lautet sie? *(1 Punkt)*
- de) Der Netzwerkdrucker erhält die letzte nutzbare Adresse. Wie lautet sie? *(1 Punkt)*

**e)** Die Praxis-PCs sollen in eine Domäne aufgenommen werden, statt in einer Arbeitsgruppe zu bleiben. **3 Punkte**

- ea) Nennen Sie zwei Vorteile. *(2 Punkte)*
- eb) Welcher zentrale Dienst verwaltet in einer Domäne die Benutzerkonten und die Anmeldung? *(1 Punkt)*

---

## 2. Aufgabe (25 Punkte)

In der Praxis werden sensible Patientendaten verarbeitet. Die Praxisleitung möchte wissen, wie diese geschützt werden.

**a)** Ordnen Sie den drei Situationen das jeweils verletzte Schutzziel zu (Vertraulichkeit, Integrität oder Verfügbarkeit). **3 Punkte**

| Situation | Schutzziel |
|---|---|
| 1. Eine Mitarbeiterin ändert versehentlich einen Behandlungstermin in der Software, ohne dass es jemand bemerkt. | |
| 2. Wegen eines Serverausfalls kann die Praxis vormittags keine Patientenakten öffnen. | |
| 3. Ein Besucher liest am Empfang Befunddaten vom unbeaufsichtigten Bildschirm ab. | |

**b)** Nennen Sie zu jeder Situation aus Aufgabe a) eine passende technische Maßnahme. **3 Punkte**

**c)** Die Praxissoftware wird als Installationsdatei zum Download angeboten. Daneben steht ein SHA-256-Hashwert. **4 Punkte**

- ca) Erläutern Sie den Zweck dieses Hashwerts. *(2 Punkte)*
- cb) Der selbst berechnete Hashwert weicht vom veröffentlichten Wert ab. Was tun Sie? *(2 Punkte)*

**d)** Für den Zugang zum Praxisserver soll eine Zwei-Faktor-Authentifizierung eingeführt werden. Nennen Sie zwei unterschiedliche Arten von Faktoren und geben Sie je ein Beispiel an. **4 Punkte**

**e)** Die Betriebssysteme der Praxis-PCs sollen gehärtet werden. Nennen Sie drei geeignete Maßnahmen. **3 Punkte**

**f)** Ein Mitarbeiter verwendet das Passwort „Praxis2026“. **3 Punkte**

- fa) Beurteilen Sie das Passwort kurz. *(1 Punkt)*
- fb) Nennen Sie zwei Regeln, die eine wirksame Passwort-Richtlinie enthalten sollte. *(2 Punkte)*

**g)** Ein Patient verlangt Auskunft darüber, welche Daten die Praxis über ihn gespeichert hat. **5 Punkte**

- ga) Nennen Sie zwei weitere Rechte betroffener Personen nach der DSGVO (neben dem Auskunftsrecht). *(2 Punkte)*
- gb) Erklären Sie den Unterschied zwischen Anonymisierung und Pseudonymisierung. *(3 Punkte)*

---

## 3. Aufgabe (25 Punkte)

Die Umstellung der Praxis auf die neue IT wird als Projekt geplant.

**a)** Nennen Sie vier typische Phasen des Wasserfallmodells in der richtigen Reihenfolge. **4 Punkte**

**b)** Nennen Sie zwei Rollen, die in Scrum vorkommen. **2 Punkte**

**c)** Das Projektziel lautet bisher: „Die neue IT soll bald besser laufen.“ **4 Punkte**

- ca) Nennen Sie zwei der SMART-Kriterien, gegen die diese Formulierung verstößt. *(2 Punkte)*
- cb) Formulieren Sie das Ziel als SMART-Ziel. *(2 Punkte)*

**d)** Für das Projekt wurden folgende Vorgänge geplant. Dauern in Tagen, das Projekt beginnt bei Zeitpunkt 0. **15 Punkte**

| Nr. | Vorgang | Dauer | Vorgänger |
|---|---|---:|---|
| A | Bedarf klären | 2 | – |
| B | Netzwerkschrank aufbauen | 4 | – |
| C | Angebote einholen | 3 | A |
| D | Hardware beschaffen | 5 | C |
| E | Netzwerk verkabeln | 3 | B |
| F | Server einrichten | 4 | D, E |
| G | Arbeitsplätze einrichten | 6 | D |
| H | Testlauf | 2 | F, G |
| I | Übergabe an die Praxis | 1 | H |

Der Knoten eines Netzplans ist wie folgt aufgebaut:

```text
FAZ   Dauer   FEZ
   Nr. / Vorgang
SAZ   GP·FP   SEZ
```

*FAZ/FEZ = frühester Anfangs-/Endzeitpunkt, SAZ/SEZ = spätester Anfangs-/Endzeitpunkt, GP = Gesamtpuffer, FP = freier Puffer.*

- da) Führen Sie die Vorwärtsrechnung durch (FAZ und FEZ). *(4 Punkte)*
- db) Führen Sie die Rückwärtsrechnung durch (SAZ und SEZ). *(4 Punkte)*
- dc) Berechnen Sie GP und FP für alle Vorgänge. *(3 Punkte)*
- dd) Geben Sie den kritischen Pfad und die Projektdauer an. *(2 Punkte)*
- de) Vorgang F dauert 5 Tage länger als geplant. Um wie viele Tage verschiebt sich das Projektende, wenn keine Gegenmaßnahmen erfolgen? Begründen Sie kurz. *(2 Punkte)*

| Nr. | FAZ | FEZ | SAZ | SEZ | GP | FP |
|---|---:|---:|---:|---:|---:|---:|
| A | | | | | | |
| B | | | | | | |
| C | | | | | | |
| D | | | | | | |
| E | | | | | | |
| F | | | | | | |
| G | | | | | | |
| H | | | | | | |
| I | | | | | | |

---

## 4. Aufgabe (25 Punkte)

Die Praxissoftware wird um kleine Auswertungen und einen KI-gestützten Terminassistenten ergänzt.

**a)** Die folgende Funktion berechnet die Wartezeit aller Patienten, wobei pro Patient höchstens 30 Minuten angerechnet werden. Führen Sie einen Schreibtischtest für den Aufruf `wartezeit_gesamt([20, 45, 10, 35])` durch. **6 Punkte**

```python
def wartezeit_gesamt(dauern):
    gesamt = 0
    for i in range(len(dauern)):
        if dauern[i] > 30:
            gesamt = gesamt + 30
        else:
            gesamt = gesamt + dauern[i]
    return gesamt
```

| i | dauern[i] | dauern[i] > 30 ? | gesamt (nach dem Durchlauf) |
|---|---:|---|---:|
| 0 | | | |
| 1 | | | |
| 2 | | | |
| 3 | | | |

Rückgabewert der Funktion: ______

**b)** Zwei Kollegen haben Code geschrieben. Entscheiden Sie jeweils, ob ein Syntaxfehler oder ein Logikfehler vorliegt, und geben Sie die Korrektur an. **4 Punkte**

```python
# Ausschnitt 1
def ist_kind(alter):
    if alter < 14
        return True
    return False
```

```python
# Ausschnitt 2: durchschnitt([20, 30]) soll 25 liefern, liefert aber 50
def durchschnitt(werte):
    summe = 0
    for w in werte:
        summe = summe + w
    return summe / (len(werte) - 1)
```

**c)** Für die Patientenverwaltung wurde folgende Klasse entworfen. **3 Punkte**

```python
class Patient:
    def __init__(self, name, geburtsjahr):
        self.__name = name
        self.__geburtsjahr = geburtsjahr

    def get_name(self):
        return self.__name
```

*Hinweis: In Python kennzeichnet ein führender Unterstrich gemäß Konvention ein nicht öffentliches Attribut; zwei führende Unterstriche wie bei `__name` bewirken zusätzlich eine Namensänderung (Name-Mangling), aber keinen strikten Zugriffsschutz wie `private` in manchen anderen Sprachen. Beantworten Sie cb) und cc) allgemein für die objektorientierte Programmierung.*

- ca) Nennen Sie ein Attribut und eine Methode der Klasse. *(1 Punkt)*
- cb) Erklären Sie den Unterschied zwischen den Sichtbarkeiten `private` und `public`. *(1 Punkt)*
- cc) Warum werden Attribute wie `name` üblicherweise als `private` angelegt? *(1 Punkt)*

**d)** Der Ablauf der Terminbuchung wird als UML-Aktivitätsdiagramm dargestellt. Ordnen Sie den beschriebenen Symbolen ihre Bedeutung zu. **3 Punkte**

| Symbol | Zuordnung | Bedeutung |
|---|---|---|
| a) Ausgefüllter Kreis | | 1. Entscheidung (Verzweigung) |
| b) Raute | | 2. Startknoten |
| c) Kreis mit ausgefülltem Punkt darin | | 3. Endknoten |

**e)** Im Ablauf „Termin vereinbaren“ (Anfrage entgegennehmen, freien Termin suchen, Termin bestätigen, Erinnerung versenden) soll ein KI-Terminassistent zum Einsatz kommen. **9 Punkte**

- ea) Nennen Sie drei Schritte des Ablaufs, in denen KI sinnvoll unterstützen kann, und beschreiben Sie jeweils kurz, wie. *(3 Punkte)*
- eb) Nennen Sie zwei Risiken, die beim Einsatz der KI in der Zahnarztpraxis zu beachten sind. *(2 Punkte)*
- ec) Der Anbieter verlangt 59 EUR je Lizenz und Monat, benötigt werden 2 Lizenzen. Dazu kommt eine einmalige Einrichtungsgebühr von 240 EUR. Zwei Mitarbeitende werden je 5 Stunden eingearbeitet, in dieser Zeit entgeht der Praxis ein Umsatz von 90 EUR je Stunde und Person. Berechnen Sie die wirtschaftliche Gesamtbelastung im ersten Jahr (Kosten und entgangener Umsatz). *(4 Punkte)*

---

## Punkteübersicht

| Aufgabe | Thema | Punkte |
|---|---|---:|
| 1 | Arbeitsplätze und Praxisnetz | 25 |
| 2 | IT-Sicherheit und Datenschutz | 25 |
| 3 | Projektplanung | 25 |
| 4 | Praxissoftware, Fehlersuche und KI | 25 |
| | **Gesamt** | **100** |

*Lösungen siehe separates Lösungsblatt.*