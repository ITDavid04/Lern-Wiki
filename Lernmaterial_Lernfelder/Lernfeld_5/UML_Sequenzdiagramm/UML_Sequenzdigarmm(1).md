UML-Sequenzdiagramm (1): Lebenslinie und Zeitfluss

Das Sequenzdiagramm ist der Stasi-Agent unter den UML-Diagrammen: Es zeichnet lückenlos auf, wer wann mit wem spricht – und in welcher Reihenfolge. Für IT-Umschüler ist es das wichtigste Werkzeug, um aus einer textuellen Anforderung („Der Kunde gibt eine Bestellung auf …“) eine klare zeitliche Abfolge von Nachrichten zu machen.
1. Die Analogie: Theaterbühne mit Regieanweisungen

Stell dir ein Theaterstück vor, bei dem jeder Schauspieler eine eigene Spur auf der Bühne hat. Während das Stück läuft, läuft die Zeit von oben nach unten. Jeder Satz (jede Nachricht) wird als Pfeil zwischen zwei Schauspielern notiert – und zwar exakt an der Stelle im Drehbuch, an der er fällt.

    Lebenslinie: Die Spur, auf der ein Schauspieler steht. Sie zeigt, dass er in dieser Szene existiert und ansprechbar ist.

    Zeitfluss: Die vertikale Richtung – von oben (früher) nach unten (später).

2. Aufbau eines Sequenzdiagramms (Grundgerüst)

Ein Sequenzdiagramm besteht aus drei wesentlichen Elementen:
Element	Darstellung	Bedeutung
Lebenslinie	Gestrichelte senkrechte Linie	Teilnehmer (Objekt, Komponente, Akteur)
Nachrichtenpfeil	Horizontaler Pfeil zwischen zwei Lebenslinien	Information, Methodenaufruf oder Signal
Zeitachse	Vertikale Position des Pfeils	Zeitpunkt der Nachricht (oben = früher, unten = später)
Wichtige Notationselemente

    Synchrone Nachricht: Gefüllter Pfeil – der Sender wartet auf eine Antwort.

    Rückkehr (Antwort): Gestrichelter Pfeil mit offener Spitze – optional, zeigt die Rückgabe.

    Asynchrone Nachricht: Offener Pfeil – der Sender macht sofort weiter (wird in Beitrag 3 vertieft).

3. Einfaches Beispiel: Kunde bestellt etwas
text

```mermaid
sequenceDiagram
    participant Kunde
    participant Webshop

    Kunde->>Webshop: bestellungAufgeben()
    Webshop-->>Kunde: auftragsbestätigung()
```

Interpretation: Der Kunde ruft bestellungAufgeben() auf (synchron). Der Webshop verarbeitet und sendet eine Antwort auftragsbestätigung zurück. Alles Weitere geschah später.
4. Profi-Tipps für die Prüfung

    Reihenfolge lesen: Immer von oben nach unten. Pfeile, die weiter oben stehen, passieren früher.

    Lebenslinien immer mitgestalten: Vergessen Sie nie den Kopf (Rechteck mit Name) über der Linie.

    Semantik der Pfeile: Ein gefüllter Pfeil ist ein „Aufruf“, der eine Antwort erwartet. Wird in Prüfungen häufig als Einstiegsfrage genutzt.

    Prüfungsfokus: IHK-Aufgaben zeigen oft einen Bestellablauf und fragen: „Welche Nachricht wird zuerst gesendet?“ – Halten Sie sich strikt an die vertikale Ordnung.

Beispiel-Struktur (Code-Nah)
text



(Hinweis: Die obige Textdarstellung ist didaktisch reduziert – echte UML-Werkzeuge zeichnen Lebenslinien durchgehend.)