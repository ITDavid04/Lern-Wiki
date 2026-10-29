# UML-Klassendiagramm: Der Bauplan der Software

Das Klassendiagramm ist das Herzstück der **objektorientierten Analyse und Design (OOAD)**. Für IT-Umschüler ist es oft die größte Hürde, da es den Übergang vom reinen "Code-Schreiben" zum "System-Design" markiert.

## 1. Die Analogie: Backform vs. Kuchen

Stell dir eine Klasse wie eine Backform vor. Die Backform selbst kann man nicht essen, aber sie legt fest, welche Form, Größe und Muster der Kuchen später haben wird. Der Kuchen, den du aus dem Ofen holst, ist das **Objekt** (oder die **Instanz**).

- **Klasse**: Der abstrakte Bauplan (z. B. "Auto").
- **Objekt**: Das reale Ding auf der Straße (z. B. "Dein blauer VW Golf").

## 2. Aufbau einer Klasse (Die "Drei-Box-Regel")

In UML wird eine Klasse immer als Rechteck mit drei Etagen dargestellt:

| Sektion          | Inhalt                                         | Analogie                                |
|------------------|------------------------------------------------|-----------------------------------------|
| **Oben: Name**   | Der Name der Klasse (Singular, Großbuchstabe)  | "Was ist das?" (z.B. Konto)             |
| **Mitte: Attribute** | Eigenschaften / Datenfelder                | "Was hat es?" (z.B. kontostand)         |
| **Unten: Methoden**  | Fähigkeiten / Funktionen                   | "Was kann es?" (z.B. einzahlen())       |

### Sichtbarkeiten (Modifikatoren)

Wichtig für die IHK-Prüfung sind die Symbole vor den Namen:

- **+** (public): Jeder darf es sehen/benutzen.
- **-** (private): Nur die Klasse selbst darf es nutzen (Geheimnisprinzip/Kapselung).
- **#** (protected): Nur die Klasse und ihre Kinder (Vererbung) dürfen ran.

## 3. Beziehungen: Wie Klassen miteinander sprechen

Klassen sind keine Inseln. Sie stehen in Beziehung zueinander:

- **Vererbung (Generalisierung)**: Ein "Hund" ist ein "Tier". Dargestellt durch einen Pfeil mit leerer Spitze zum Elternteil.
- **Assoziation**: Ein "Kunde" kennt ein "Konto". Eine einfache Linie.
- **Aggregation**: Ein "Team" besteht aus "Mitarbeitern". Wenn das Team gelöscht wird, existieren die Mitarbeiter weiter. (Leere Raute).
- **Komposition**: Ein "Haus" besteht aus "Zimmern". Wenn das Haus abgerissen wird, sind auch die Zimmer weg. (Gefüllte Raute – "Existenzabhängigkeit").

## 4. Profi-Tipps für die Prüfung

- **Pfeilrichtung**: Bei der Vererbung zeigt der Pfeil immer von der Spezialisierung (Kind) zur Generalisierung (Eltern). *"Das Kind schaut zu den Eltern auf."*
- **Multiplizitäten**: Vergiss nie die Zahlen an den Enden (z. B. `1..*`). Sie sagen aus, wie viele Objekte beteiligt sind.
- **Attribute vs. Methoden**: Wenn du ein Wort hast, frag dich: Ist es ein Nomen (Attribut) oder ein Verb (Methode)?
- **Prüfungsfokus**: In der IHK-Prüfung wird oft die **Unterscheidung zwischen Aggregation (leere Raute)** und **Komposition (gefüllte Raute)** sowie die korrekte Pfeilrichtung bei Vererbung abgefragt. Merke: Bei Komposition lebt das Teil nicht ohne das Ganze.

## Beispiel-Struktur (Code-Nah)

```text
-----------------------
|       Konto         |  <-- Klassenname
-----------------------
| - kontostand: double |  <-- Attribut (private)
| - inhaber: String    |
-----------------------
| + einzahlen(betrag)  |  <-- Methode (public)
| + abheben(betrag)    |
-----------------------


5. Der Profi-Schliff: Strenge UML-Normen und Details

Wenn es in die Abschlussprüfung geht, schauen die Korrektoren oft sehr genau auf die formale Syntax. Hier sind die letzten Feinheiten, die ein Klassendiagramm zu 100 % wasserdicht machen:
5.1 Die exakte Schreibweise (Syntax)

In der UML gilt für die Beschriftung eine feste Reihenfolge. Merke dir: Erst der Name, dann der Doppelpunkt, dann der Datentyp.

    Attribute: Sichtbarkeit name : Datentyp

        Beispiel: - kontostand : double

    Methoden: Sichtbarkeit name(parameterName : Datentyp) : Rückgabetyp

        Beispiel: + abheben(betrag : double) : boolean (Gibt z. B. true oder false zurück, je nachdem, ob das Konto gedeckt war). Ist kein Rückgabewert vorhanden, nutzt man void.

5.2 Abstrakte Klassen und Interfaces

Nicht jede Klasse ist eine direkt nutzbare Backform. Manchmal ist es nur ein Entwurf oder ein Vertrag:

    Abstrakte Klasse: Der Klassenname wird kursiv geschrieben. Das bedeutet: Von dieser Klasse können keine direkten Objekte (Instanzen) erstellt werden. Sie existiert nur, damit andere Klassen ihre Eigenschaften erben können (z. B. eine abstrakte Klasse Fahrzeug, von der Auto und Motorrad erben).

    Interface (Schnittstelle): Wird mit dem Schlagwort <<interface>> über dem Namen markiert. Es enthält in der Regel nur leere Methoden (ohne Programmcode). Ein Interface ist wie ein Vertrag, den andere Klassen unterschreiben und erfüllen müssen.

5.3 Wer kennt wen? (Navigierbarkeit bei Assoziationen)

Bei Assoziationen (der simplen Verbindungslinie) ist das Ende der Linie entscheidend, da es die Datenflussrichtung angibt:

    Linie ohne Pfeile: Beide Klassen kennen sich (bidirektional).

    Linie mit offener Pfeilspitze (z. B. Kunde -> Konto): Der Kunde kennt sein Konto und kann darauf zugreifen. Das Konto weiß aber nicht, wem es gehört (unidirektional).

Das normgerechte Beispiel (Code-Nah)

Hier ist unsere Konto-Klasse noch einmal – diesmal inklusive Parameter, Datentypen und Rückgabewerten nach strenger UML-Syntax:
Plaintext

-------------------------------------------------------
|                        Konto                        |
-------------------------------------------------------
| - kontostand : double                               |
| - inhaber : String                                  |
-------------------------------------------------------
| + einzahlen(betrag : double) : void                 |
| + abheben(betrag : double) : boolean                |
-------------------------------------------------------