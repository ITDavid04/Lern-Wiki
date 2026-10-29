
## 📋 Programmablaufplan (PAP) – DIN 66001 – Der Bauplan mit Pfeilen

### Worum geht’s eigentlich?

Ein Programmablaufplan (PAP), oft auch Flussdiagramm oder Flowchart genannt, ist der **Klassiker unter den Ablaufdiagrammen**. Er stellt einen Algorithmus als eine Folge von einzelnen Symbolen dar, die durch Pfeile (Ablauflinien) miteinander verbunden sind und so die zeitliche Abfolge der Operationen zeigen.

Anders als das strikte Struktogramm, das Sprünge verbietet, ist der PAP freier und ähnelt eher einer **Wegbeschreibung mit "Wenn-Dann"-Gabelungen**, bei der du den Linien folgst. Die **DIN 66001** sorgt auch hier dafür, dass alle die gleiche "Kartensprache" sprechen, ob am Whiteboard oder in der IHK-Prüfung.

---

### 🔧 Die wichtigsten Bausteine

Stell dir diese Symbole wie eine standardisierte Legende auf einem Lageplan vor. Jedes hat eine eindeutige Bedeutung:

| Symbol (nach DIN 66001) | Bedeutung | Analogie aus anderen Berufen |
| :--- | :--- | :--- |
| **Oval / Rechteck mit runden Ecken** | **Grenzstelle:** Start oder Ende des Ablaufs. | Der „Eingang“ und „Ausgang“-Stempel in einem Laufzettel. |
| **Rechteck** | **Operation / Anweisung:** Ein auszuführender Schritt. | Ein einzelner Handgriff in einer Montageanleitung, z. B. „Schraube festziehen“. |
| **Raute** | **Verzweigung / Entscheidung:** Eine Ja/Nein-Frage. Hat einen Eingang und zwei Ausgänge, die mit "ja" und "nein" beschriftet werden. | Die Qualitätsprüfung: „Teil in Ordnung? Ja → weiterleiten, Nein → Nacharbeit“. |
| **Pfeil / Linie** | **Ablauflinie:** Verbindet die Symbole in der Reihenfolge ihrer Ausführung in Pfeilrichtung. | Die Wege zwischen den Stationen auf einem Hallenplan. |
| **Parallelogramm** | **Ein- / Ausgabe:** Zeigt an, dass Daten ein- oder ausgegeben werden. | Das Formular, das du vom Kunden erhältst oder der Lieferschein, den du druckst. |
| **Rechteck mit senkrechten Doppelstrichen** | **Unterprogramm:** Aufruf eines ausgelagerten, definierten Prozesses. | Der Verweis auf eine separate Standard-Arbeitsanweisung (SOP). |

> 💡 **Agile Side-Info:** In der Praxis reichen dir oft Rechteck, Raute und Pfeile, um 90 % aller Logiken im Team zu visualisieren. Fokussiere dich darauf.

---

### 🧩 Einfaches Beispiel: Login mit drei Versuchen

Das folgende PAP-Beispiel zeigt denselben Login-Prozess, aber diesmal in der "fließenden" Darstellung des PAP. Folge einfach den Pfeilen:

```
         +---------+
         |  Start  |              ← Oval: Grenzstelle
         +----+----+
              |
              v
   +---------------------+
   | "Bitte Benutzername |      ← Parallelogramm: Ausgabe
   |  und Passwort       |
   |  eingeben:"         |
   +---------------------+
              |
              v
   +---------------------+
   | Eingabe: Benutzer, |       ← Parallelogramm: Eingabe
   | Passwort            |
   +---------------------+
              |
              v
          (Start der Schleife)
              |
              v
        +-----------+              ← Raute: Verzweigung
        | Benutzer  |  Ja
        | == "admin"?+-----+
        +-----+-----+     |
              | Nein      |
              v           |
   +---------------------+ |
   | "Benutzer unbekannt"| |      ← Rechteck: Anweisung
   +---------------------+ |
              |            |
              v            |
     +---------------+     |
     | Versuche + 1  |     |      ← Rechteck: Anweisung
     +-------+-------+     |
             |              |
             v              |
   +-----------------+      |
   | Versuche == 3 ? |      |      ← Raute: Verzweigung
   +---+----------+--+      |
       | Ja       | Nein    |
       v          v         |
   (Zum Ende)  (Zurück zur  |
                Eingabe)    |
                            |
              +<------------+
              v
        +-----------+              ← Raute: Verzweigung
        | Passwort  |  Ja
        | == "geheim"?+-----+
        +-----+-----+     |
              | Nein      |
              v           |
   +---------------------+ |
   | "Falsches Passwort" | |      ← Rechteck: Anweisung
   +---------------------+ |
              |            |
              v            |
     +---------------+     |
     | Versuche + 1  |     |
     +-------+-------+     |
             |              |
             v              |
   +-----------------+      |
   | Versuche == 3 ? |      |
   +---+----------+--+      |
       | Ja       | Nein    |
       v          v         |
   (Zum Ende)  (Zurück zur  |
                Eingabe)    |
                            |
              +<------------+
              v
   +---------------------+
   | "Erfolgreich        |       ← Parallelogramm: Ausgabe
   |  eingeloggt!"       |
   +---------------------+
              |
              v
        +---------+
        |  Ende   |              ← Oval: Grenzstelle
        +---------+
```

**Erklärung für Quereinsteiger:** Du startest oben und folgst den Pfeilen wie dem Fließband in einer Fertigung. An den Rauten wird eine Entscheidung getroffen, die dich auf unterschiedliche Wege führt. Im Gegensatz zum Struktogramm kann ein Pfeil dich auch mal "zurück" an eine frühere Stelle im Plan führen – das ist hier völlig normal und so eingeplant.

---

### 🧠 Das Warum – mit Analogien aus deinem alten Beruf

**Handwerk / Fertigung:**
Der PAP ist wie ein **Arbeits- und Laufplan für ein Werkstück**. Du siehst jeden Bearbeitungsschritt (Rechteck), jede Prüfung (Raute) und wohin das Teil als Nächstes geht (Pfeil). Ein Rücksprung ist wie ein Teil, das zur Nacharbeit an eine frühere Maschine zurückgeschickt wird. Ein Unterprogramm ist wie der Verweis "weiter nach Arbeitsplan XY".

**Kaufmännischer Bereich / Vertrieb:**
Denk an einen Prozess für die Angebotserstellung. Ein PAP zeigt, welche Schritte bei einer Kundenanfrage durchlaufen werden. Eine Raute fragt: "Ist der Kunde ein Neukunde?", und je nach Antwort führt ein anderer Pfeil den Sachbearbeiter durch die korrekten Formulare. Es ist die grafische Version eurer schriftlichen Prozessbeschreibung.

**Gastronomie / Küche:**
Ein Rezept, das bei einem Schritt „Wenn Soße zu dünn → zurück zum Reduzieren“ sagt, arbeitet mit einer klassischen PAP-Schleife. Der Pfeil führt dich einfach von der Prüfung aus zurück zum entsprechenden Topf-Symbol. Du siehst den Weg, den deine Handlung nimmt.

**Das bringt's technisch:**
- Der PAP ist **frei von Programmiersprachen-Syntax** und daher ideal, um sich mit Fachabteilungen oder Kunden über Abläufe zu verständigen.
- Er zwingt dich, **alle möglichen Pfade zu durchdenken**, bevor du eine Zeile Code schreibst.
- Er visualisiert die zeitliche Abfolge von Operationen sehr direkt und ist oft intuitiver als Pseudocode.

---

### 🏗️ Verschachtelung – dem Linienfluss folgen

Im Unterschied zum Struktogramm, das Verschachtelung durch streng ineinander geschachtelte Blöcke zeigt, regelt der PAP dies durch die **Führung der Ablauflinien**.

- Eine **Schleife** entsteht, wenn eine Ablauflinie von einer Raute oder einem späteren Symbol zurück zu einem früheren Punkt im Diagramm führt.
- Eine **Verschachtelung von Bedingungen** siehst du daran, dass du in den "Ja"-Pfad einer Raute hineingehst und dort sofort auf eine nächste Raute triffst, die einen neuen Entscheidungsblock eröffnet.

Es ist wie eine Schnitzeljagd: Du gehst in ein Gebäude (erste Raute, „Ja“), und in diesem Gebäude findest du eine weitere Tür mit einer neuen Frage (zweite Raute). Der verschachtelte Prozess ist einfach der Weg, den du nacheinander zurücklegst.

🚨 **Wichtiger Hinweis:** Diese Freiheit kann schnell zu unübersichtlichen Plänen mit verwirrenden Pfeilen führen, dem berühmten **"Spaghetti-Code"** im Diagramm. Spätestens dann ist der Moment, über ein disziplinierteres Struktogramm nachzudenken, das solche Sprünge konstruktionsbedingt verhindert.

---

### 🚀 Im Stil des agilen Arbeitens

- **Perfekt für das Sprint-Planning:** Skizziere einen User-Story-Workflow schnell als PAP auf einem Whiteboard. Die verschiedenen Pfade (Erfolgsfall, Fehlerfall) werden sofort für Tester, Entwickler und Product Owner sichtbar.
- **Iterativ verfeinern:** Starte mit dem "Happy Path" – der geraden Linie zum Erfolg. Fehlerbehandlungen und Sonderfälle fügst du als neue Abzweigungen in den nächsten Iterationen hinzu. So wie du Backlog-Items im Refinement detaillierst.
- **Leichtgewichtig und universell:** Weil der PAP komplett ohne Code auskommt, ist er eine der besten Brücken zwischen nicht-technischen Fachexperten und dem Entwicklungsteam. Er dient als Diskussionsgrundlage, nicht als starre Dokumentation.

🎯 **Side-Info:** In der modernen Softwareentwicklung sind PAPs reine Entwurfshilfen. Für objektorientierte Architekturen haben sich Aktivitätsdiagramme der UML durchgesetzt, die konzeptionell aber stark auf dem PAP aufbauen. Du lernst hier also die Wurzel einer ganzen Visualisierungsfamilie kennen.

---

### 👣 Dein nächster Schritt

1.  Nimm dieselbe einfache Alltagslogik wie beim Struktogramm (z. B. den Kaffeeautomaten) und zeichne sie jetzt als PAP mit Ovalen, Rechtecken und Rauten. Konzentriere dich auf den Fluss der Pfeile.
2.  Vergleiche dein Ergebnis mit dem Struktogramm. Wo führt der PAP dich im Kreis? Wo hatte das Struktogramm eine klar umschlossene Schleife? Dieses Verständnis für die Unterschiede ist Gold wert.
3.  In der Prüfung: Achte auf die korrekte Pfeilrichtung und die Beschriftung der Ausgänge an den Rauten ("ja"/"nein"). Konzentriere dich darauf, den logischen Fluss glasklar darzustellen.

---

**Zusammengefasst:** Der Programmablaufplan ist dein intuitiver, pfeilbasierter Bauplan für Algorithmen und Prozesse. Er gibt dir die Freiheit, Abläufe so flexibel und verzweigt darzustellen, wie sie in der echten Welt passieren. Aus jedem Beruf kennst du das Prinzip vorgegebener Abläufe mit Entscheidungspunkten – der PAP liefert dir die genormte IT-Sprache dazu.

Quellen:

https://de.wikipedia.org/wiki/Programmablaufplan
https://de.wikipedia.org/wiki/Programmablaufplan?diff=88628160
https://akademie.123effizientdabei.de/wp-content/uploads/2023/02/DIN66001-1966.pdf
https://www.peterjohann-consulting.de/flussdiagramm/