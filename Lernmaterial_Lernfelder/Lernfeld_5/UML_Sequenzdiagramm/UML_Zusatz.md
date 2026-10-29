UML-Sequenzdiagramm (4): Kombinierte Fragmente – Logik in den Zeitfluss bringen

Nicht jeder Programmablauf ist eine Einbahnstraße. Mal muss man auf Fehler reagieren, mal etwas wiederholen, mal nur unter einer Bedingung ausführen. Mit Kombinierten Fragmenten bekommt das Sequenzdiagramm Kontrollstrukturen – fast wie eine visuelle Programmiersprache.
1. Die Analogie: Die Rezeptkarte mit Entscheidungsfeldern

Ein Kochrezept enthält oft Anweisungen wie „Wenn der Teig zu flüssig ist, Mehl hinzufügen“ oder „Den Vorgang wiederholen, bis die Masse glatt ist“. Genau solche Anweisungen packt man in einen rechteckigen Rahmen mit einem Etikett in der linken oberen Ecke. Alles, was innerhalb des Rahmens passiert, steht unter dieser Regel.
2. Aufbau und Notation

Ein kombiniertes Fragment ist ein Rechteck, das eine oder mehrere Nachrichten umschließt. Links oben steht ein Operator (z. B. alt, loop, opt, par, break). Der Rahmen kann in mehrere Operanden unterteilt sein – getrennt durch eine gestrichelte Linie, die die Bedingung beschriftet.
Operator	Bedeutung (Alltag)	Darstellung
alt	Wenn-Dann / Sonst (if/else)	Rahmen mit zwei oder mehr Abschnitten, z. B. [Erfolg] und [Fehler]
opt	Optionaler Schritt (if ohne else)	Rahmen mit einem Abschnitt
loop	Wiederholung (for/while), oft mit Abbruchbedingung	Rahmen mit Bedingung (z. B. [für alle Artikel])
par	Gleichzeitige Abläufe (parallel)	Rahmen mit zwei Abschnitten, die gleichzeitig ausgeführt werden
break	Sofortiger Abbruch des umschließenden Fragments, meist bei Fehler	Rahmen mit einem Abschnitt, der das äußere Fragment unterbricht
3. Komplettes Beispiel: Bestellung mit Prüfung, Wiederholung und Fehlerbehandlung
text

```mermaid
sequenceDiagram
    participant Kunde
    participant Webshop
    participant Zahlungsdienst

    Kunde->>Webshop: bestellungAufgeben()
    loop für jeden Artikel
        Webshop->>Webshop: prüfeLager()
        alt Artikel verfügbar
            Webshop->>Webshop: reserviere()
        else nicht verfügbar
            Webshop->>Webshop: artikelStornieren()
        end
    end
    Webshop->>Zahlungsdienst: zahlungAnfordern()
    Zahlungsdienst-->>Webshop: bestätigung()
    Webshop-->>Kunde: auftragsbestätigung()
```
  │  ...     ...

Interpretation:

    Die äußere Schleife (loop) wird für jeden Artikel der Bestellung durchlaufen.

    Innerhalb der Schleife wird eine Fallunterscheidung (alt) getroffen: Entweder der Artikel ist verfügbar und wird reserviert, oder er ist nicht verfügbar und die Position wird storniert.

    Erst nachdem alle Artikel geprüft sind, geht es mit der Zahlungsaufforderung weiter. Das verhindert eine Bezahlung nicht lieferbarer Ware.

(Die Darstellung ist durch Text etwas gedrängt; in einem UML-Werkzeug sitzt jeder Operand in einem eigenen, sauber getrennten Abschnitt.)
4. Profi-Tipps für den Arbeitsalltag

    Operator merken mit Eselsbrücke: alt für Alternative, opt für optional, loop für Schleife. Das a und o sind die einzigen Operatoren mit drei Buchstaben – so lassen sie sich schnell ablesen.

    Bedingungen in eckigen Klammern: Jeder Operand braucht eine [Bedingung], sonst ist das Fragment syntaktisch unvollständig. Bei loop genügt oft ein Kommentar wie [bis Abbruchbedingung]; in der Prüfung wird die exakte Klammerung toleranter gesehen, aber in der Praxis macht sie das Diagramm lesbar.

    Saubere Verschachtelung: Nie eine Nachricht außerhalb eines Fragments kreuzen – sie muss entweder ganz innerhalb oder ganz außerhalb sein. Falsche Einrückung ist der häufigste Anfängerfehler.

    Ausnahmen mit break: Wenn ein Fehler auftritt und der komplette umgebende Ablauf gestoppt werden soll, kann ein break-Fragment die sonst nötigen, komplizierten alt-Verschachtelungen ersetzen.

    Nicht alles ausmodellieren: Sie müssen nicht jede triviale Verzweigung als Fragment zeichnen. Nutzen Sie kombinierte Fragmente gezielt für die Stellen, die das Systemverständnis fördern – sonst wird das Diagramm unübersichtlich.

5. Warum ist das für Umschüler wichtig?

Auch wenn die IHK-Prüfung oft nur lineare Szenarien abfragt: Real existierende Software kommuniziert nie linear. Kombinierte Fragmente sind die Brücke zwischen „Ablauf verstehen“ und „Ablauf entwerfen“. Sie helfen, Spezifikationen von Senior-Entwicklern zu lesen, und schulen das algorithmische Denken – eine Kernkompetenz für den Beruf.