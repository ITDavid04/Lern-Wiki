# KI-D6 · Modellfamilien und Größen: Wie groß, wie offen, wie spezialisiert

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D6 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du öffnest die Modellliste eines Programms oder eines Anbieters und liest Namen wie „8B", „70B", „Instruct", „Coder" oder „235B-A22B". Daneben stehen Lizenzen und Zahlen, die niemand erklärt. Welches Modell passt zu deiner Aufgabe, und warum gibt es überhaupt so viele?

Am Ende dieses Artikels kannst du solche Namen lesen und einordnen. Du weißt, was die Größe eines Modells kostet und warum mehr Parameter nicht automatisch bessere Antworten bedeuten. Du erkennst ein Mixture-of-Experts-Modell und verstehst, warum es mehr Gewichtsspeicher braucht als ein dichtes Modell mit gleichem Rechenaufwand pro Token. Gegenüber einem dichten Modell mit gleicher Gesamtzahl an Parametern rechnet es pro Token weniger. Außerdem kannst du geschlossene Gewichte, offene Gewichte und Open Source auseinanderhalten und weißt, worauf du bei der Lizenz achtest.

Vorausgesetzt werden D1 bis D5 und A9, vor allem die Speicherrechnung aus A9 und das Training aus D5. Aus E2 kennst du die Werkzeugtypen, hier geht es um die Modelle dahinter.

---

## 1. Eine Familie, viele Größen

Eine Gärtnerei zieht dieselbe Sorte in mehreren Größen: als Jungpflanze im kleinen Topf, als Pflanze im großen Container und als Baum, der nur noch mit dem Hänger kommt. Die Züchtung ist dieselbe. Platzbedarf, Preis und Pflegeaufwand wachsen aber mit der Größe.

Modelle werden ähnlich angeboten. Eine **Modellfamilie** ist eine Reihe von Modellen eines Anbieters mit gleicher Bauart und ähnlichem Trainingsrezept in mehreren Größen. Ein Name setzt sich meist aus diesen Teilen zusammen:

- **Familie und Generation:** der Name der Reihe, oft mit Versionsnummer. Eine neue Generation bringt in der Regel neues Training mit anderen Daten, manchmal auch eine geänderte Bauart.
- **Größe:** Die Zahl mit „B" steht für Milliarden (englisch billion) Parameter, also Gewichte (D3). „8B" sind rund 8 Milliarden, „405B" rund 405 Milliarden.
- **Variante:** Basismodell oder auf Anweisungen angepasst (D5). Das angepasste Modell trägt oft „Instruct" oder „Chat" im Namen. Dazu kommen Zusätze für Spezialisierungen (Abschnitt 6).

Wo das Bild nicht passt: Ein Setzling wächst zum Baum. Ein 8B-Modell wird nie zu einem 70B-Modell, denn jede Größe wird in der Regel eigens trainiert. Manche kleinen Modelle lernen allerdings von großen (Abschnitt 5).

---

## 2. Was Größe kostet

Die Zahl im Namen verrät, was ein Modell kostet. Über seine Qualität sagt sie weniger (Abschnitt 3). Drei Kosten hängen direkt an ihr.

**Speicher.** Die Faustformel aus A9 schätzt den Speicherbedarf der Gewichte: Dateigröße ≈ Parameter × Bits pro Gewicht ÷ 8. Mit dem Mittelwert einer 4-Bit-Stufe aus A9 ergibt das für die drei Größen einer Familie sehr verschiedene Werte. Es sind Näherungen für die Gewichte. Die echte Datei kann abweichen, und beim Betrieb kommen Zwischenspeicher und Laufzeit dazu (A9). Ein Modell mit 43 GB Gewichten läuft deshalb nicht automatisch auf einem System mit 43 GB Speicher.

**Training.** Aus der Skalierungsforschung stammt eine Näherung für den Rechenaufwand des Vortrainings dichter Modelle: etwa 6 × Parameter × Tokens Gleitkommaoperationen (englisch FLOPs). Die 6 setzt sich grob aus 2 Operationen je Parameter und Token im Vorwärtsdurchlauf und etwa 4 im Rückwärtsdurchlauf zusammen, der die Gradienten berechnet (D5). Je mehr Parameter und je mehr Trainingstext, desto mehr Aufwand. Die Formel schätzt den Rechenaufwand und keine Trainingszeit oder Kosten, denn Hardware und Auslastung fehlen darin. Bei MoE-Modellen (Abschnitt 4) rechnet sie mit den aktiven Parametern, das ist eine zusätzliche Vereinfachung.

**Betrieb.** Beim Antworten müssen die Gewichte für jedes Token aus dem Speicher gelesen werden (A9). Bei vergleichbarer Hardware, Quantisierung und Nutzung erzeugt ein größeres dichtes Modell deshalb meist weniger Tokens pro Sekunde. Wie sich das auf Antwortzeit und Preise pro Token auswirkt, hängt zusätzlich von der Laufzeitumgebung ab (P2).

Beide Rechnungen in einem kleinen Programm:

```python
bits = 4.9   # Mittelwert einer 4-Bit-Stufe, siehe A9
for mrd in (8, 70, 405):
    print(f"{mrd}B: etwa {mrd * bits / 8:.0f} GB für die Gewichte")

def flops(parameter, tokens):
    return 6 * parameter * tokens   # grobe Näherung: 6 × Parameter × Tokens

print(f"405B mit 15,6 Billionen Tokens: {flops(405e9, 15.6e12):.2e} FLOPs")
```

```text
8B: etwa 5 GB für die Gewichte
70B: etwa 43 GB für die Gewichte
405B: etwa 248 GB für die Gewichte
405B mit 15,6 Billionen Tokens: 3.79e+25 FLOPs
```

Die Näherung trifft gut: Der technische Bericht zum größten Modell einer verbreiteten Familie nennt für sein Vortraining 3,8 × 10²⁵ FLOPs bei 15,6 Billionen Tokens. Zusammen mit den 30,84 Millionen Grafikkarten-Stunden aus D5 zeigt das den Aufwand hinter einem solchen Modell.

---

## 3. Größer ist besser? Bis zu einem Punkt

Zwei Gärtnereien liefern Jungpflanzen. Die eine ist riesig und arbeitet mit billiger Erde, die andere ist klein, nimmt gute Erde und pflegt jede Pflanze sorgfältig. Wer liefert die besseren? Die Größe des Betriebs allein entscheidet das nicht.

Bei Modellen beschreibt die Forschung diesen Zusammenhang mit **Skalierungsgesetzen**. Eine Arbeit von 2020 fand, dass der Verlust (D5) nach einem Potenzgesetz sinkt, wenn Modellgröße, Datenmenge und Rechenaufwand wachsen, über mehr als sieben Größenordnungen hinweg. Jeder weitere Schritt bringt dabei weniger als der vorige. Die Arbeit riet, bei festem Budget vor allem das Modell zu vergrößern.

Eine Arbeit von 2022 korrigierte das. Sie trainierte ein Modell mit 70 Milliarden Parametern auf 1,4 Billionen Tokens, bei gleichem Rechenaufwand wie ein Modell mit 280 Milliarden Parametern, das nur auf 300 Milliarden Tokens trainiert war. Das kleinere Modell war laut Studie in einer breiten Auswahl von Aufgaben deutlich besser. Die Empfehlung: Modellgröße und Trainingsmenge sollten gemeinsam wachsen. Aus den Werten der Arbeit ergibt sich als grober Anhaltspunkt etwa 20 Tokens je Parameter. Der Wert beantwortet eine bestimmte Frage: Wie erreicht ein Anbieter bei festem Rechenbudget den niedrigsten Verlust? Eine Zielvorgabe für jedes Modell ist er nicht.

Wie die Verhältnisse bei aktuellen Modellen aussehen, rechnet ein kurzes Programm:

```python
for name, parameter, tokens in [("Studie von 2022", 70e9, 1.4e12),
                                ("405B", 405e9, 15.6e12),
                                ("8B", 8e9, 15e12)]:
    print(f"{name}: {tokens / parameter:.0f} Tokens je Parameter")
```

```text
Studie von 2022: 20 Tokens je Parameter
405B: 39 Tokens je Parameter
8B: 1875 Tokens je Parameter
```

Das 405B-Modell liegt mit 39 über dem Anhaltspunkt, gilt laut seinem Bericht aber trotzdem als näherungsweise rechenoptimal. Der Wert 20 ist also eine Richtung und kein Gesetz. Das 8B-Modell bekam fast 1.900 Tokens je Parameter. Aus dem Verhältnis allein folgt nichts über die Qualität, es kommt auf die Einordnung im Bericht an: Die kleineren Modelle wurden dort viel länger als rechenoptimal trainiert. Laut Bericht schneiden sie dadurch bei gleichem Inferenzbudget, also gleichem Betriebsaufwand, besser ab als rechenoptimal trainierte Modelle. Ein hoher Wert heißt also nicht, dass schlecht trainiert wurde. Der Grund: Training zahlt der Anbieter einmal, den Betrieb zahlt jeder einzelne Aufruf. Wer ein Modell millionenfach laufen lässt, steckt lieber mehr Training in ein kleineres Modell. Das bestätigt auch eine Untersuchung von 2023, die erwartete Betriebskosten in die Rechnung einbezieht.

Aus D5 kennst du ein weiteres Beispiel: Ein Modell mit 1,3 Milliarden Parametern wurde bei den untersuchten Anfragen einem mit 175 Milliarden vorgezogen, weil es nachtrainiert war. Die Größe verrät also nicht, wie viel Daten, wie gute Daten und welches Nachtraining in einem Modell stecken. Wie gut ein Modell für dich ist, zeigt dein eigener Test (A7, A8), und Benchmarks lesen lernst du in P8.

Wo das Bild nicht passt: Die Qualität einer Pflanze siehst du sofort. Die Qualität eines Modells zeigt sich nur in Tests an Aufgaben, die dir wichtig sind.

---

## 4. Mixture of Experts: viele Gewichte, wenige aktiv

Eine große Gärtnerei hat acht Fachabteilungen. Am Eingang sitzt eine Verkaufsleitung, die jede Kundenfrage an zwei Abteilungen weiterreicht und deren Antworten zusammenfasst. Der Kunde wartet nur auf zwei Abteilungen. Trotzdem müssen alle acht dastehen, denn vorher weiß niemand, welche gebraucht werden.

So funktioniert ein **Mixture-of-Experts-Modell**, kurz **MoE** (Mischung aus Experten). Jede Schicht hat neben der Attention das Feed-Forward-Netz aus D3. Bei einem MoE-Modell gibt es dieses Netz mehrfach, jede Kopie heißt **Experte**. Ein kleines Netz, der **Router**, wählt für jedes Token in jeder Schicht einige Experten aus, und nur diese rechnen. Bei einem bekannten Beispiel sind es zwei von acht. Die Attention-Teile gibt es nur einmal. Deshalb hat ein Modell namens „8x7B" laut seinem Bericht 47 Milliarden Parameter und keine 56.

Zwei Zahlen gehören deshalb zu einem MoE-Modell: die **Gesamtparameter** und die **aktiven Parameter** pro Token. Aktiv sind die Parameter, die für dieses eine Token ausgewählt und gerechnet werden, nicht alle im Modell vorhandenen. Der Bericht zu diesem Beispiel nennt 47 Milliarden gesamt und 13 Milliarden aktiv. Was daraus für Speicher und Tempo folgt, zeigt der Vergleich mit dichten Modellen, also solchen ohne Experten, einmal mit 13 und einmal mit 47 Milliarden Parametern:

```python
bits = 4.9          # Mittelwert einer 4-Bit-Stufe, siehe A9
bandbreite = 400    # GB/s, angenommener Beispielwert wie in A9

modelle = [
    ("Dicht, 13 Mrd.", 13, 13),
    ("Dicht, 47 Mrd.", 47, 47),
    ("MoE, 47 Mrd. gesamt, 13 Mrd. aktiv", 47, 13),
]
for name, gesamt, aktiv in modelle:
    speicher = gesamt * bits / 8     # Vereinfachung: nur Gewichte, ohne Zwischenspeicher und Laufzeit
    pro_token = aktiv * bits / 8     # Annahme: je Token wird nur gelesen, was aktiv ist
    print(f"{name}: {speicher:.1f} GB Gewichte, {pro_token:.1f} GB je Token, "
          f"bandbreitenbasierte Ideal-Obergrenze {bandbreite / pro_token:.0f} Token/s")
```

```text
Dicht, 13 Mrd.: 8.0 GB Gewichte, 8.0 GB je Token, bandbreitenbasierte Ideal-Obergrenze 50 Token/s
Dicht, 47 Mrd.: 28.8 GB Gewichte, 28.8 GB je Token, bandbreitenbasierte Ideal-Obergrenze 14 Token/s
MoE, 47 Mrd. gesamt, 13 Mrd. aktiv: 28.8 GB Gewichte, 8.0 GB je Token, bandbreitenbasierte Ideal-Obergrenze 50 Token/s
```

Das ist die Ausnahme, die A9 bei der Geschwindigkeitsrechnung angekündigt hat. Bei einem lokal geladenen MoE-Modell folgt der Speicher für die Gewichte der Gesamtzahl, weil der Router erst während der Rechnung wählt und deshalb jeder Experte bereitliegen muss. Die aktiven Parameter sind ein Anhaltspunkt für den Rechenaufwand pro Token, aber keine vollständige Beschreibung: Bei langem Kontext kommt Rechenaufwand für die Attention hinzu, und die reale Rechenzeit hängt von der Umsetzung ab. Im vereinfachten Denkmodell schätzt die Rechnung damit auch, wie viele Gewichtsdaten pro Token gelesen werden. Das ist keine Messung der Speicherzugriffe einer konkreten Laufzeitumgebung.

Das MoE-Modell und das dichte 13B-Modell landen bei 50 Token/s, weil in diesem Denkmodell die Speicherbandbreite bremst und beide pro Token gleich viel lesen. Das MoE-Modell ist also nicht automatisch schneller als ein dichtes Modell mit gleicher aktiver Zahl. Gegenüber dem dichten 47B-Modell liest es pro Token etwa dreieinhalbmal weniger, beim Gewichtsspeicher liegen beide gleichauf.

Die Zahlen sind eine Rechnung und keine Messung. Wie viel wirklich gelesen wird und wie schnell das Modell antwortet, hängt auch von Hardware, Quantisierung, Programm, Routing und Batchgröße ab.

Auch beim Training lohnt der Blick auf die aktiven Parameter. Eine eigene Überschlagsrechnung mit der Näherung aus Abschnitt 2: Das sehr große MoE-Modell aus der Beispielbox unten hat 37 Milliarden aktive Parameter und wurde mit 14,8 Billionen Tokens trainiert. Das ergibt 6 × 37 × 10⁹ × 14,8 × 10¹² ≈ 3,3 × 10²⁴ FLOPs. Setzt du vereinfachend nur die aktiven Parameter in die Formel ein, kommt etwa ein Elftel des Werts für das dichte 405B-Modell aus Abschnitt 2 heraus. Daraus lässt sich kein entsprechendes Verhältnis der tatsächlichen Trainingskosten ableiten, denn Hardware, Auslastung und weitere Aufwände bleiben außen vor. Die Zahl zeigt nur eine Größenordnung. Und die aktive Größe verrät auch hier nicht alles: Das 47B-Modell erreichte laut seinem Bericht mindestens die Ergebnisse eines dichten Modells mit 70 Milliarden Parametern. Das ist eine Herstellerangabe.

| | Dichtes Modell | MoE-Modell |
| --- | --- | --- |
| Gewichte im Speicher | alle | alle Experten, also die Gesamtzahl |
| Rechnung pro Token (Anhaltspunkt) | alle Gewichte | nur die aktiven |
| Lesen pro Token (Denkmodell) | alle Gewichte | nur die aktiven |
| Gewichtsspeicher bei gleicher aktiver Rechenlast | gering | höher |
| Name verrät | Gesamtzahl | oft beide Zahlen, etwa „235B-A22B" für 235 Milliarden gesamt und 22 Milliarden aktiv |

Wo das Bild nicht passt: Die Experten sind keine Fachleute für Themen. Die Analyse im Bericht zum 47B-Modell fand keine offensichtlichen Muster, die sich nach Themen wie Biologie, Philosophie oder Mathematik richten. Die Auswahl folgt eher der Syntax, also der Form des Textes. Außerdem entscheidet der Router pro Token und pro Schicht und nicht einmal pro Frage.

---

## 5. Kleine Modelle: wie sie gut werden

Ein Lehrling in der Gärtnerei lernt nicht nur aus Büchern. Er steht neben der Meisterin und sieht, wie sie entscheidet. Sie nennt ihre Antwort „Wasser" und zeigt die Gewichte dahinter: etwas mehr als die Hälfte Wasser, ein Viertel Sonne, ein kleiner Rest Dünger.

Das ist die Idee der **Destillation**. Beim üblichen Vortraining lernt das Modell, das nächste Token des Trainingstextes vorherzusagen. Das Trainingsziel ist dabei das Token, das im Text tatsächlich folgt. Bei der Destillation bekommt das kleine Modell, der Schüler, stattdessen oder zusätzlich die Wahrscheinlichkeitsverteilung eines größeren Modells, des Lehrers (D4). Eine Gemma-Familie von 2024 mit Modellen von 2 bis 27 Milliarden Parametern setzt das ein: Die Modelle mit 2 und 9 Milliarden Parametern wurden mit Destillation trainiert, das größte ohne. Der Bericht zu einer anderen Familie schreibt, das Flaggschiff-Modell sei im Nachtraining genutzt worden, um die kleineren Modelle zu verbessern.

Insgesamt gibt es drei Hebel, mit denen kleine Modelle besser werden:

- **Mehr Training:** deutlich mehr Tokens je Parameter (Abschnitt 3).
- **Destillation:** der Schüler lernt von den Verteilungen eines größeren Modells.
- **Quantisierung:** verkleinert die Datei, kostet aber etwas Genauigkeit (A9).

Wo das Bild nicht passt: Der Lehrling lernt aus dem, was er sieht und versteht. Der Schüler im Modell bildet nach, wie der Lehrer gewichtet. Das Trainingssignal sind die Verteilungen des Lehrers, und Fehler oder Verzerrungen des Lehrers können mit übergehen. Wie viel vom Können beim Schüler ankommt, hängt unter anderem von den Daten, vom Verfahren und von der Größe des Schülers ab. Ein kleines Modell erreicht deshalb nicht garantiert die Qualität des großen, und ob es für deine Aufgabe reicht, zeigt dein Test (A9 Abschnitt 4).

---

## 6. Spezialisierte Modelle

Eine Baumschule züchtet nur Gehölze und kennt sie besser als jeder Gemischtbetrieb. Dafür bekommst du dort keine Gurkenpflanzen. Auch bei Modellen gibt es Allrounder und Spezialisten.

Typische Arten von Spezialisierung:

- **Code- und Mathematikmodelle:** Anbieter veröffentlichen zur selben Familie Varianten, die auf Programmcode oder Rechenaufgaben zugeschnitten sind. Im Namen steht dann oft „Coder" oder „Math".
- **Denkmodelle (Reasoning-Modelle):** Sie sind darauf trainiert, vor der Antwort Zwischenschritte zu erzeugen. Das ist eine trainierte Fähigkeit und keine einheitliche Bauart, und die Umsetzung unterscheidet sich je nach Modell. Mehr dazu in D7.
- **Embedding-Modelle:** Sie liefern Vektoren statt Text (D2) und stehen hinter Suche und RAG (P4).
- **Multimodale Modelle:** Sie verarbeiten neben Text auch Bilder oder Audio (P10).
- **Sprachabdeckung:** Auch die Zahl der gut unterstützten Sprachen unterscheidet sich zwischen Familien und Generationen.

Die Spezialisierung entsteht an zwei Stellen. Die Auswahl der Trainingsdaten legt fest, was das Modell im Vortraining sieht. Das Nachtraining (D5) formt dann, welche Aufgaben es gut beherrscht. Wer ein Modell nachträglich auf eigene Daten anpassen will, muss nicht von vorn beginnen (P7).

Wo das Bild nicht passt: Eine Baumschule entscheidet sich bewusst für ihr Fach. Beim Modell ist die Spezialisierung eine Verschiebung der Schwerpunkte im Training, und ein Spezialmodell bleibt ein Sprachmodell mit den Grenzen aus D4. Als Faustregel, die du selbst prüfen kannst, gilt: Ein Spezialist kann bei seinem Fach vorn liegen und außerhalb davon hinter einem Allrounder zurückbleiben.

---

## 7. Offene und geschlossene Gewichte

Du willst ein Modell in ein Praktikumsprojekt einbauen. Beim einen kommst du nur über einen Dienst heran, beim anderen lädst du eine Datei herunter, und beim dritten steht in der Lizenz ein Absatz, den du zweimal lesen musst. Drei Begriffe helfen beim Sortieren.

**Geschlossene Gewichte.** Die Gewichte bleiben beim Anbieter, du nutzt das Modell über einen Dienst. Oft nennt der Anbieter weder Größe noch Aufbau. Ein viel zitierter Bericht eines Anbieters von 2023 schreibt ausdrücklich, er enthalte keine weiteren Details zur Architektur einschließlich Modellgröße. Zahlen zur Größe geschlossener Modelle, die im Netz kursieren, sind daher Schätzungen, solange der Anbieter sie nicht selbst nennt.

**Offene Gewichte** (englisch open weights). Du kannst die trainierten Gewichte herunterladen. Ob du sie lokal ausführen (A9), verändern, kommerziell einsetzen oder weitergeben darfst, hängt von der Lizenz und den technischen Voraussetzungen ab. Offene Gewichte bedeuten auch nicht, dass du Training, Daten oder Code kennst.

**Open Source im Sinne der Open Source AI Definition.** Die Open Source Initiative (OSI) verlangt neben den Parametern auch den vollständigen Quellcode für Training und Betrieb. Dazu kommen ausreichende Informationen über die Trainingsdaten, jeweils unter freien Bedingungen (A9). Ob ein bestimmtes Modell das erfüllt, prüfst du an der Lizenz und der Dokumentation des Modells. Dieser Artikel ordnet die Modelle der Beispielbox nicht danach ein.

Die Lizenzen offener Modelle räumen sehr unterschiedliche Rechte ein und legen unterschiedliche Pflichten auf. Freizügige Lizenzen wie Apache 2.0 erlauben Nutzung, Veränderung und Weitergabe in weitem Rahmen. Eigene Modell-Lizenzen regeln jedes Modell für sich. Typische Bedingungen sind eine Schwelle bei der Nutzerzahl, eine Pflicht zur Namensnennung oder eine Regel für die Namen abgeleiteter Modelle. Dazu kommt oft eine Nutzungsrichtlinie, die bestimmte Zwecke ausschließt. Die Beispielbox weiter unten zeigt einen solchen Fall.

Sechs Fragen an die Lizenz einer konkreten Modellseite:

1. Darf ich das Modell kommerziell nutzen, etwa im Betrieb?
2. Gibt es eine Schwelle, etwa bei der Zahl der Nutzer, ab der ich eine eigene Erlaubnis brauche?
3. Muss ich den Anbieter nennen, und gilt eine Namensregel für abgeleitete Modelle?
4. Verweist die Lizenz auf eine Nutzungsrichtlinie, die bestimmte Einsätze verbietet?
5. Darf ich das Modell verändern und weitergeben?
6. Gelten für Gewichte, Code und weitere Teile wie Tokenizer oder Laufzeitprogramm dieselben Bedingungen, oder hat jeder Teil eine eigene Lizenz?

Lies die Lizenz der konkreten Modellseite und nicht nur die der Familie. Das ist keine Rechtsberatung. Im Betrieb entscheidet, was dort erlaubt ist (R4, R6), und urheberrechtliche Fragen behandeln D9 und R5.

Wo das Bild nicht passt: Eine Saatguttüte kann eine Gärtnerei vermehren und verkaufen, wenn die Sorte frei ist, und sie darf es nicht, wenn Sortenschutz gilt. Bei Gewichten steht diese Regel in der Lizenz. Anders als Saatgut lässt sich die Datei ohne Verlust kopieren, deshalb zählt vor allem die Lizenz. Offene Gewichte haben außerdem ihren Preis: Du trägst Aufwand und Verantwortung selbst (A9).

---

## 8. Ein Modell auswählen

Mit diesem Wissen lässt sich eine Auswahl in sechs Fragen sortieren:

1. **Aufgabe:** Was soll das Modell tun, und reicht ein kleines (A1, A9 Abschnitt 4)?
2. **Daten:** Dürfen die Eingaben das Gerät verlassen (E7, R1)? Wenn nicht, brauchst du offene Gewichte und lokalen Betrieb (A9).
3. **Speicher:** Passt das Modell samt Zwischenspeicher für den Kontext auf deine Hardware (A9)? Bei MoE zählt die Gesamtzahl der Parameter (Abschnitt 4).
4. **Lizenz:** Ist der Einsatz erlaubt (Abschnitt 7)?
5. **Spezialisierung:** Gibt es eine Variante für dein Fach, etwa für Code (Abschnitt 6)?
6. **Betrieb:** Welche Antwortzeit und welchen Durchsatz brauchst du? Reicht deine Hardware, oder ist ein Dienst sinnvoller (P2)?

Danach entscheidet dein eigener Test mit den Fällen aus A7 und der Prüfung nach A8. Beziehe dabei ein, welche Folgen falsche Antworten hätten und was der Betrieb kostet. Wie du mehrere Modelle systematisch vergleichst, zeigt P8.

> **Beispielbox, Stand 21.10.2026: Zahlen aus Herstellerangaben.** Die Angaben stammen aus Berichten und Modellkarten der Anbieter und sind nicht unabhängig geprüft. Modellnamen und Verfügbarkeit ändern sich.
>
> - **Llama 3.1 (Meta):** dichte Modelle mit 8, 70 und 405 Milliarden Parametern, Kontext bis 128K Tokens, rund 15 Billionen Tokens Vortraining. Lizenz: eigene Community-Lizenz. Sie verlangt eine eigene Erlaubnis bei Meta, wenn die Produkte oder Dienste des Lizenznehmers und seiner verbundenen Unternehmen mehr als 700 Millionen monatlich aktive Nutzer haben. Gemessen werden die monatlich aktiven Nutzer im Kalendermonat vor dem Veröffentlichungsdatum (Abschnitt 2 der Lizenz). Dazu kommen der Hinweis „Built with Llama" und für abgeleitete Modelle ein „Llama" am Anfang des Namens. Außerdem gilt eine Nutzungsrichtlinie.
> - **Qwen2.5 und Qwen3 (Alibaba):** Qwen2.5 mit 0,5 bis 72 Milliarden Parametern, dazu Qwen2.5-Coder und Qwen2.5-Math. Die Modellkarte des 7B-Instruct-Modells nennt Apache 2.0. Die Dienstmodelle Qwen2.5-Turbo und -Plus sind MoE-Modelle ohne offene Gewichte. Qwen3 umfasst dichte und MoE-Modelle von 0,6 bis 235 Milliarden Parametern unter Apache 2.0 und nennt laut Bericht 119 Sprachen und Dialekte gegenüber 29 bei Qwen2.5. Das Modell Qwen3-235B-A22B hat 235 Milliarden Parameter gesamt, 22 Milliarden aktiv, 128 Experten, davon 8 aktiv.
> - **Mixtral 8x7B (Mistral):** 8 Experten pro Schicht, 2 davon aktiv, 47 Milliarden Parameter gesamt, 13 Milliarden aktiv, Kontext 32K, Apache 2.0.
> - **DeepSeek-V3:** MoE mit 671 Milliarden Parametern gesamt und 37 Milliarden aktiv, 14,8 Billionen Tokens Vortraining, laut Bericht 2,664 Millionen Grafikkarten-Stunden auf H800-Karten für das Vortraining. Insgesamt sind es 2,788 Millionen, mit Kontexterweiterung und Nachtraining. Die Stunden lassen sich nicht direkt mit den H100-Stunden aus D5 vergleichen.
> - **gpt-oss (OpenAI):** gpt-oss-120b hat 116,83 Milliarden Parameter gesamt und 5,13 Milliarden aktiv (128 Experten, 4 aktiv pro Token). gpt-oss-20b hat 20,91 Milliarden gesamt und 3,61 Milliarden aktiv (32 Experten, 4 aktiv). Apache 2.0. Die MoE-Gewichte sind mit 4,25 Bit gespeichert und machen laut Bericht über 90 Prozent der Parameter aus. Der Bericht nennt Checkpoint-Größen von 60,8 GiB und 12,8 GiB (1 GiB entspricht etwa 1,07 GB). Die Faustformel aus A9 über alle Parameter anzuwenden, trifft diese Größen nur grob, weil nicht alle Gewichte mit 4,25 Bit gespeichert sind. Davon zu unterscheiden ist die Angabe des Berichts, das größere Modell passe auf eine einzelne 80-GB-Karte und das kleinere auf Systeme mit 16 GB. Sie ist eine Herstellerangabe und folgt nicht allein aus der Checkpoint-Größe, denn ob ein Modell bei dir läuft, hängt zusätzlich von Laufzeit und Zwischenspeicher ab. Im Repository liegt neben der Apache-Lizenz eine Datei USAGE_POLICY, die hier nicht geprüft wurde.
> - **Gemma 2 (Google):** 2 bis 27 Milliarden Parameter. Die Modelle mit 2 und 9 Milliarden Parametern wurden mit Destillation auf 2 und 8 Billionen Tokens trainiert, das 27B-Modell ohne Destillation auf 13 Billionen.
> - **GPT-4 (OpenAI):** Der technische Bericht von 2023 nennt keine Modellgröße.

---

## Häufige Fehlgriffe

- **„Mehr Parameter heißen bessere Antworten."** Datenmenge, Datenqualität, Generation und Nachtraining spielen mit (Abschnitt 3).
- **„Ein MoE-Modell braucht nur so viel Speicher wie seine aktiven Parameter."** Alle Experten müssen bereitliegen, der Speicher folgt der Gesamtzahl (Abschnitt 4).
- **„Die Experten sind Fachleute für Themen."** Die Analyse im Bericht fand keine offensichtlichen Themenmuster (Abschnitt 4).
- **„Kleine Modelle sind abgespeckte große."** Sie werden meist eigens trainiert, oft deutlich länger, manchmal mit Destillation (Abschnitt 5).
- **„Offene Gewichte heißen: Ich darf alles."** Die Lizenz entscheidet, und sie kann Bedingungen enthalten (Abschnitt 7).
- **„Offene Gewichte sind Open Source."** Open Source im Sinne der Definition verlangt mehr als die Gewichte (Abschnitt 7, A9).
- **„Die Größe eines Cloud-Modells ist bekannt."** Bei geschlossenen Gewichten sind Angaben im Netz meist Schätzungen (Abschnitt 7).
- **„Ein Spezialmodell ist für meine Aufgabe automatisch besser."** Ob es das ist, zeigt dein Test (Abschnitt 6, A7).

---

## Zum Ausprobieren

1. Ändere im ersten Programm aus Abschnitt 2 die Rechnung auf 70 Milliarden Parameter und 15 Billionen Tokens. Wie verhält sich der Aufwand zu dem des 405B-Modells? Tipp: Vergleiche zuerst die Parameterzahlen der beiden Modelle.
2. Ändere das Programm aus Abschnitt 4 so, dass es ein dichtes Modell mit 70 Milliarden Parametern und ein MoE-Modell mit 235 Milliarden gesamt und 22 Milliarden aktiv vergleicht. Welches Modell braucht mehr Speicher, welches liest pro Token mehr?
3. Öffne die Modellseite eines offenen Modells und notiere Familie, Generation, Größe, Variante, Kontextlänge und Lizenz. Beantworte die sechs Lizenzfragen aus Abschnitt 7 mit dem, was dort steht, und halte fest, was offen bleibt.
4. Lass einen Testfall aus A7 von zwei Größen derselben Familie bearbeiten, lokal (A9) oder bei einem Anbieter, der mehrere Größen anbietet (E2). Protokolliere die Unterschiede nach A8.
5. Frag einen Chat-Assistenten nach seiner Parameterzahl und suche die Angabe danach beim Anbieter. Notiere, ob beides zusammenpasst und ob der Anbieter überhaupt eine Zahl nennt.

Am Ende hast du ein Gefühl dafür, wie stark Größe den Aufwand treibt. Außerdem kennst du den Unterschied zwischen Gesamt- und aktiven Parametern und hast eine Lizenz-Checkliste für jedes neue Modell.

---

## Fazit

Ein Modell kommt in einer Familie mit mehreren Größen, und die Zahl im Namen sagt, was es an Speicher, Training und Betrieb kostet. Über seine Qualität verrät sie weniger, denn Datenmenge, Nachtraining und Generation zählen mit, und kleine Modelle werden bewusst länger trainiert oder von größeren destilliert. Bei MoE-Modellen unterscheiden sich Gesamtparameter und aktive Parameter: Der Gewichtsspeicher folgt der Gesamtzahl, als Anhaltspunkt für den Rechenaufwand pro Token dienen die aktiven. Spezialisierte Varianten verschieben die Schwerpunkte, und bei offenen Gewichten entscheidet die Lizenz, was du damit darfst. Welches Modell zu dir passt, zeigt dein eigener Test. Als Nächstes geht es in D7 um Modelle, die vor ihrer Antwort eigene Denkschritte erzeugen, und darum, wo sie trotzdem scheitern.

```yaml
dokument: ki-d6-modellfamilien-und-groessen
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-10-21
quellen_fachlich:
  - "Kaplan u. a.: Scaling Laws for Neural Language Models (2020), arXiv:2001.08361. https://arxiv.org/abs/2001.08361 (Zugriff 2026-10-21): Verlust sinkt nach Potenzgesetz mit Modellgröße, Datenmenge und Rechenaufwand über mehr als sieben Größenordnungen; bei festem Budget sehr große Modelle mit moderater Datenmenge, Training vor der Konvergenz beenden. Abschnitt 2.1: Vorwärtsdurchlauf C_forward ≈ 2N (Gleichung 2.2), C ≈ 6N Gleitkommaoperationen je Trainingstoken; C ≈ 6NBS in Abschnitt 1.3"
  - "Hoffmann u. a.: Training Compute-Optimal Large Language Models (2022), arXiv:2203.15556. https://arxiv.org/abs/2203.15556 (Zugriff 2026-10-21): 70 Mrd. Parameter, 1,4 Billionen Tokens, gegenüber 280 Mrd. Parametern und 300 Mrd. Tokens, gleiches Rechenbudget, 4-mal mehr Daten; Modellgröße und Tokens gemeinsam skalieren; Näherung FLOPs(N, D) ≈ 6ND (Abschnitt 3.3); etwa 20 Tokens je Parameter aus Tabelle 3 abgeleitet (im Text nicht ausdrücklich genannt)"
  - "Sardana u. a.: Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws (2023), arXiv:2401.00448. https://arxiv.org/abs/2401.00448 (Zugriff 2026-10-21): Betriebskosten in die Skalierungsrechnung einbezogen; bei hohem erwartetem Inferenzbedarf kleinere, länger trainierte Modelle"
  - "Meta (Llama Team): The Llama 3 Herd of Models (2024), arXiv:2407.21783. https://arxiv.org/abs/2407.21783 (Zugriff 2026-10-21): dichter Transformer mit 405B, Kontext bis 128K; Flaggschiff mit 3,8 × 10^25 FLOPs und 15,6 Billionen Tokens vortrainiert, näherungsweise rechenoptimal (Extrapolation 402B bei 16,55T Tokens); kleinere Modelle 'much longer than compute-optimal' trainiert, besser bei gleichem Inferenzbudget; Flaggschiff verbessert die kleineren im Nachtraining; H100-Karten, Auslastung 38 bis 43 Prozent"
  - "Meta: Llama 3.1 Community License. https://huggingface.co/meta-llama/Llama-3.1-8B/blob/main/LICENSE (Zugriff 2026-10-21): Erlaubnis bei Meta, wenn zum Veröffentlichungsdatum (23.07.2024) die monatlich aktiven Nutzer der Produkte oder Dienste von Lizenznehmer oder verbundenen Unternehmen im vorangegangenen Kalendermonat über 700 Mio. liegen (Abschnitt 2, Wortlaut 'made available by or for Licensee, or Licensee's affiliates'); 'Built with Llama' (Abschnitt 1.b.i); 'Llama' am Anfang des Namens abgeleiteter Modelle; Verweis auf Acceptable Use Policy (Abschnitt 1.b.iv)"
  - "Jiang u. a.: Mixtral of Experts (2024), arXiv:2401.04088. https://arxiv.org/abs/2401.04088 (Zugriff 2026-10-21): 8 Feed-Forward-Blöcke (Experten) je Schicht, Router wählt je Token zwei; 47 Mrd. Parameter, 13 Mrd. aktiv; Kontext 32k; Apache 2.0; laut Bericht auf Augenhöhe mit oder besser als Llama 2 70B und GPT-3.5 (Herstellerangabe). Abschnitt 5 (Routing-Analyse): 'we do not observe obvious patterns in the assignment of experts based on the topic', Auswahl eher an der Syntax ausgerichtet (Abbildung 8)"
  - "DeepSeek-AI: DeepSeek-V3 Technical Report (2024), arXiv:2412.19437. https://arxiv.org/abs/2412.19437 (Zugriff 2026-10-21): 671 Mrd. Parameter gesamt, 37 Mrd. aktiv pro Token, 14,8 Billionen Tokens, MoE und Multi-head Latent Attention; Tabelle 1: Pre-Training 2664K, Context Extension 119K, Post-Training 5K, gesamt 2788K H800-GPU-Stunden (bei angenommenem Mietpreis von 2 Dollar je Stunde)"
  - "OpenAI: gpt-oss-120b & gpt-oss-20b Model Card (2025), arXiv:2508.10925. https://arxiv.org/abs/2508.10925 (Zugriff 2026-10-21): 116,83 Mrd. gesamt und 5,13 Mrd. aktiv (120b), 20,91 Mrd. gesamt und 3,61 Mrd. aktiv (20b); 128 bzw. 32 Experten, je 4 pro Token; MoE-Gewichte in MXFP4 (4,25 Bit je Parameter), laut Abschnitt 2.1 über 90 Prozent der Parameter; Tabelle 1: Checkpoint-Größe 60,8 GiB (120b) und 12,8 GiB (20b); 80-GB-Karte bzw. 16 GB Speicher; Apache 2.0"
  - "Qwen Team: Qwen3 Technical Report (2025), arXiv:2505.09388. https://arxiv.org/abs/2505.09388 (Zugriff 2026-10-21): dichte und MoE-Modelle von 0,6 bis 235 Mrd. Parametern, 119 Sprachen und Dialekte gegenüber 29 bei Qwen2.5 (Abstract und Abschnitt 3.1: 'increased from 29 to 119'), Apache 2.0. Modellkarte https://huggingface.co/Qwen/Qwen3-235B-A22B (Zugriff 2026-10-21): 235 Mrd. gesamt, 22 Mrd. aktiv, 128 Experten, 8 aktiv, Apache-2.0"
  - "Qwen Team: Qwen2.5 Technical Report (2024), arXiv:2412.15115. https://arxiv.org/abs/2412.15115 (Zugriff 2026-10-21): spezialisierte Modelle Qwen2.5-Math, Qwen2.5-Coder, QwQ und multimodale Modelle; Qwen2.5-Turbo und -Plus als nicht offene MoE-Dienstmodelle. Modellkarte Qwen2.5-7B-Instruct https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (Zugriff 2026-10-21): Apache 2.0, Familie von 0,5 bis 72 Mrd. Parametern"
  - "Gemma Team: Gemma 2: Improving Open Language Models at a Practical Size (2024), arXiv:2408.00118. https://arxiv.org/abs/2408.00118 (Zugriff 2026-10-21): 2 bis 27 Mrd. Parameter; Destillation ersetzt den One-Hot-Vektor je Token durch die Verteilung möglicher nächster Tokens (Abschnitt 1); 2B auf 2T, 9B auf 8T Tokens mit Destillation, 27B auf 13T Tokens ohne Destillation (Abschnitte 3.1 und 6.1)"
  - "OpenAI: GPT-4 Technical Report (2023), arXiv:2303.08774, Abschnitt 2. https://arxiv.org/abs/2303.08774 (Zugriff 2026-10-21): 'this report contains no further details about the architecture (including model size), hardware, training compute, ...'"
  - "Ouyang u. a.: Training language models to follow instructions with human feedback (NeurIPS 2022), arXiv:2203.02155 (siehe D5): 1,3-Mrd.-Modell bei den untersuchten Anfragen dem 175-Mrd.-Modell vorgezogen"
  - "Open Source Initiative: The Open Source AI Definition 1.0 (2024-10-28). https://opensource.org/ai/open-source-ai-definition (siehe A9): Parameter, vollständiger Code für Training und Betrieb, ausreichende Informationen über die Trainingsdaten"
  - "Rechnungen in Abschnitt 2 bis 4 am 2026-10-21 mit Python ausgeführt: 8B, 70B, 405B bei 4,9 Bit = 4,9, 42,9, 248,1 GB; 6 × 405e9 × 15,6e12 = 3,79e25 FLOPs (Bericht 3,8e25); Tokens je Parameter 20, 39, 1875; dichtes 13B, dichtes 47B und MoE 47B/13B bei 4,9 Bit und 400 GB/s: 8,0, 28,8 und 28,8 GB Gewichte, 8,0, 28,8 und 8,0 GB je Token, 50, 14 und 50 Token/s; Überschlag MoE-Training 6 × 37e9 × 14,8e12 = 3,29e24 FLOPs, Verhältnis zu 3,79e25 etwa 11,5; 60,8 GiB × 1,0737 = 65,3 GB und 12,8 GiB = 13,7 GB (Umrechnung der Checkpoint-Größen)"
  - "Eigene Artikel der Reihe: D1 bis D5 (Parameter, Feed-Forward-Netz, Verteilung, Training, Nachtraining), A9 (Speicherformel, Geschwindigkeits-Denkmodell mit Ausnahme für MoE, Open Weights gegenüber Open Source), A1, A7, A8, E2, E7; Vorwärtsverweise auf D7, D9, P2, P4, P7, P8, P10, R1, R4, R5, R6"
verifikation_offen:
  - "Näherung 6ND (Chinchilla Abschnitt 3.3, verweist auf Kaplan) ist eine grobe Faustregel; für MoE-Modelle mit aktiven Parametern angewendet ist sie eine eigene Überschlagsrechnung (W), nicht aus einer Quelle und im Text als solche gekennzeichnet; Hardware und Auslastung der beiden Läufe nicht gleichgesetzt"
  - "Aufteilung der 6 in 2 (Vorwärts) und etwa 4 (Rückwärts) Operationen je Parameter und Token: Vorwärtsdurchlauf 2N und C ≈ 6N sind bei Kaplan Abschnitt 2.1 belegt, dass der Rückwärtsdurchlauf etwa doppelt so aufwendig ist, ist Lehrbuchwissen (W) und im Text als 'grob' formuliert"
  - "Etwa 20 Tokens je Parameter ist aus Tabelle 3 der Chinchilla-Arbeit abgeleitet, nicht wörtlich dort; das 405B-Modell liegt bei 39 und gilt laut Bericht trotzdem als näherungsweise rechenoptimal; im Text als Richtung formuliert"
  - "'Jeder weitere Schritt bringt weniger' folgt aus der Potenzgesetz-Form (W); der Abstract nennt nur das Potenzgesetz"
  - "Aussage, bei MoE müssten alle Experten bereitliegen, weil der Router erst zur Laufzeit entscheidet, ist eine Schlussfolgerung (W) aus der Bauart und gilt für lokal geladene Modelle; die Geschwindigkeitsrechnung bleibt ein Denkmodell mit angenommener Bandbreite (Begriff 'Ideal-Obergrenze' wie in A9, im Text als bandbreitenbasiert und als Rechnung ohne Messung gekennzeichnet), bei mehreren gleichzeitigen Anfragen werden mehr Experten gebraucht; Aussage zum Tempo gegenüber dem dichten 47B-Modell (etwa dreieinhalbfach weniger Lesen pro Token) folgt aus dem Denkmodell"
  - "Ergebnis 'hielt mit einem dichten 70B-Modell mit' ist die Herstellerangabe des Mixtral-Berichts (Benchmarks nicht selbst nachgeprüft)"
  - "Destillation: Aussage, Fehler und Verzerrungen des Lehrers könnten mit übergehen und das Ergebnis hänge von Daten, Verfahren und Schülergröße ab, ist eine Schlussfolgerung (W) ohne Einzelquelle und im Text eingeschränkt formuliert; Lehrermodell bei Gemma 2 im Bericht nur teilweise genannt und im Text nicht genannt"
  - "gpt-oss: Aussage, dass nicht alle Gewichte mit 4,25 Bit gespeichert sind, ist eine Schlussfolgerung (W) aus 'MoE-Gewichte in MXFP4'; das Format der übrigen Tensoren (ein Review nennt BF16) steht in Abschnitt 2.1 und Tabelle 1 des Berichts nicht und wird im Text nicht genannt; Checkpoint-Größen als Herstellerangabe"
  - "Faustregel zu Spezialmodellen (vorn im Fach, hinter Allroundern außerhalb) ist eine Praxiserwartung ohne Einzelquelle und im Text als Faustregel gekennzeichnet"
  - "Hinweis, dass 'A22B' die aktiven Parameter angibt, stützt sich auf die Modellkarte von Qwen3-235B-A22B; andere Anbieter benennen anders, im Text als 'oft' formuliert"
  - "Lizenzbedingungen nur für die Llama-3.1-Lizenz gelesen; Lizenzen von Qwen3, Mixtral und gpt-oss nur als 'Apache 2.0' laut Bericht oder Modellkarte, Lizenztexte selbst nicht gelesen. Qwen2.5: nur die Karte des 7B-Instruct-Modells gelesen, Lizenzen der übrigen Größen nicht geprüft"
  - "Einordnung einzelner Modelle nach der OSI-Definition bewusst nicht vorgenommen (wie in A9); sechste Lizenzfrage (Gewichte, Code, Tokenizer, Laufzeitprogramm) ist eine eigene Ergänzung ohne Einzelquelle; gpt-oss: Modellkarte (Hugging Face) nennt Apache 2.0 ohne Nutzungsrichtlinie, im GitHub-Repository liegt eine Datei USAGE_POLICY, Inhalt nicht gelesen; Mixtral-8x7B-v0.1: Modellkarte nennt apache-2.0 (Zugriff 2026-10-21)"
  - "Herstellerangaben zu Tokens, Rechenzeit, Parametern und Kontextlängen nicht unabhängig prüfbar; Beispielbox mit Datum 2026-10-21, Modellnamen und Verfügbarkeit ändern sich"
  - "Rechtsfragen zu Gewichten und Ausgaben bewusst nicht behandelt (D9, R5)"
  - "Vorwärtsverweise auf D7, D9, P2, P4, P7, P8, P10, R1, R4, R5, R6 beim Anlegen dieser Artikel abgleichen; A9-Verweise auf D6 (MoE-Ausnahme, Lizenzen) sind eingelöst"
review_historie:
  - runde: 0
    datum: 2026-10-21
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Skalierungsarbeiten, Llama-3-Bericht und Lizenz, Mixtral, DeepSeek-V3, gpt-oss, Qwen2.5 und Qwen3, Gemma 2 und GPT-4-Bericht an der Quelle gelesen. Alle Rechenbeispiele ausgeführt. Löst die Vorwärtsverweise aus A9 (MoE-Ausnahme, Lizenzen) und D5 (Modellvielfalt) ein."
  - runde: 1
    datum: 2026-10-21
    ergebnis: "Drei externe Reviews gegen Quellen geprüft. Übernommen: Gewichteschätzung, 6 erklärt, FLOPs-Grenze, 20-Tokens-Einordnung, MoE-Wortlaut und Zeile für dichtes 47B, Trainings-Überschlag als eigene Rechnung, Destillation, Denkmodelle, Lizenz (sechste Frage, Llama-Schwelle), Betriebsfrage, gpt-oss-Checkpoints, DeepSeek-Stunden. Nicht übernommen: BF16 (nicht belegt), Produktname im Fließtext, Quellenlinks im Text, Umbenennung Ideal-Obergrenze (A9-Begriff)."
  - runde: 2
    datum: 2026-10-21
    ergebnis: "Drei Re-Reviews, Llama-Lizenz, gpt-oss-Karte und Repository, Mixtral-Karte geprüft. Übernommen: Betriebssatz abgeschwächt, Trainingsvergleich enger begrenzt, Denkmodell-Satz, Attention-Hinweis, Tabellenzeile geteilt, Destillation, OSI-Bezug, Llama-Messzeitraum, gpt-oss-Angaben getrennt, Python-Label. Nicht übernommen: Kopfzeile mit Tagesdatum (Reihenformat), YAML aus dem Artikel nehmen, Tabelle nur mit Expertengewichten."
  - runde: 3
    datum: 2026-10-21
    ergebnis: "Freigabe durch David am 2026-10-21 nach Runde 2. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen (Herstellerangaben, Lehrbuchwissen ohne Einzelquelle, Lizenztexte außer Llama nicht vollständig gelesen, USAGE_POLICY von gpt-oss, Vorwärtsverweise)."
```
