# KI-D1 · Tokens und Kontextfenster: Warum Sprachmodelle vergessen

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D1 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du arbeitest seit einer Stunde mit einem Chat-Assistenten an deinem Praktikumsbericht. Ganz am Anfang hast du geschrieben: „Bitte durchgehend Du-Form und keine Aufzählungen." Inzwischen kommen die Antworten wieder mit Spiegelstrichen, und eine Entscheidung von vor zwanzig Nachrichten ist plötzlich wieder offen. Niemand hat etwas gelöscht. Trotzdem wirkt es, als hätte das Werkzeug vergessen, was ihr vereinbart habt.

Am Ende dieses Artikels kannst du erklären, was ein Token ist und warum Sprachmodelle in Tokens zählen. Du weißt, was das Kontextfenster begrenzt, warum lange Gespräche driften und warum langer Kontext Speicher, Rechenzeit und Geld kostet. Daraus leitest du Gewohnheiten ab, mit denen du solche Gespräche gar nicht erst entgleisen lässt.

Vorausgesetzt werden E1 (der Begriff Token), E3 (Gespräch und Kontext) und A2 (Kontext gezielt mitgeben). Aus A9 kennst du die Speicherrechnung für lokale Modelle, an die Abschnitt 5 anschließt. Mit D1 beginnt der Dahinter-Block: Hier geht es um das Warum hinter den Methoden aus dem Aufbau-Track.

---

## 1. Was ein Token ist

Frag einen Chat-Assistenten, wie viele „r" im Wort „Erdbeere" stecken. Je nach Modell bekommst du die richtige Antwort, manchmal aber auch eine falsche. Ein Werkzeug, das ganze Berichte schreibt, kann sich bei einem Wort mit acht Buchstaben verzählen. Ein Grund dafür ist, dass es Text nicht Buchstabe für Buchstabe verarbeitet.

Stell dir den Etikettendrucker einer Gärtnerei vor, der mit einem Stempelkasten arbeitet. Für häufige Wörter und Wortteile gibt es fertige Stempel: „Tom", „aten", „pflanze". Seltene Wörter setzt der Drucker aus kleineren Stempeln zusammen, im Notfall Zeichen für Zeichen. Jeder Stempel hat eine Nummer, und der Auftrag an den Drucker besteht aus diesen Nummern.

So arbeitet ein Sprachmodell. Ein **Token** ist ein Textbaustein aus einem festen Vorrat, dem **Vokabular**. Das Programm, das Text in Tokens zerlegt und jedem Token seine Nummer zuordnet, heißt **Tokenizer**. Diese Nummern heißen **Token-IDs**. Das Modell wandelt jede Token-ID zu Beginn in eine gelernte Zahlenreihe um, ein sogenanntes **Embedding**, und rechnet mit diesen Zahlenreihen weiter. Was ein Embedding ist, klärt D2. Beim Antworten sagt das Modell Token für Token voraus, wie es weitergeht (E1), und der Tokenizer übersetzt die erzeugten Token-IDs zurück in Text.

So sieht das bei einem echten Tokenizer aus, dem neueren von zwei Tokenizern eines großen Anbieters (Beispielbox am Ende des Abschnitts). Die senkrechten Striche markieren die Grenzen zwischen den Tokens:

```text
Gewächshaus      ->  Gew | äch | shaus                    (3 Tokens)
Erdbeere         ->  E | rd | be | ere                    (4 Tokens)
Tomatenpflanze   ->  Tom | aten | pfl | anze              (4 Tokens)
192.168.178.1    ->  192 | . | 168 | . | 178 | . | 1      (7 Tokens)
```

Zwei Dinge fallen auf. Die Grenzen folgen keinen Silben: „Gew | äch | shaus" würde dir kein Deutschlehrer durchgehen lassen. Und bei „Erdbeere" liegen die beiden „r" in zwei verschiedenen Tokens. Zum Zählen muss das Modell wissen, wie „rd" und „ere" geschrieben werden, und die Buchstaben über die Token-Grenzen hinweg zusammenzählen. Die Schreibweise kann es aus dem Training kennen, aber für solche exakten Zeichenaufgaben arbeitet es nicht zuverlässig genug. Sprachmodelle können deshalb bei Aufgaben auf Buchstabenebene schwächer sein, als ihr sonstiges Können vermuten lässt.

Das Bild hinkt an einer Stelle: Den Stempelkasten hat niemand nach Sprache oder Sinn sortiert. Ein Verfahren hat vor dem Training ausgezählt, welche Zeichenfolgen in großen Textmengen häufig vorkommen, und diese zu Tokens gemacht. Ein verbreitetes Verfahren dafür heißt **Byte Pair Encoding**. In der Sprachverarbeitung hat es sich mit einer Arbeit zur maschinellen Übersetzung von 2016 durchgesetzt. Es fasst schrittweise die häufigsten benachbarten Paare zu neuen Bausteinen zusammen. Häufige Zeichenfolgen werden durch dieses wiederholte Zusammenfassen zu größeren Tokens. Seltenere Wörter setzt der Tokenizer weiterhin aus kleineren Bausteinen zusammen.

Daraus folgt, dass verschiedene Modelle verschieden zählen. Der ältere Tokenizer desselben Anbieters zerlegt „Gewächshaus" in „G | ew | äch | sh | aus", also fünf statt drei Tokens, und „Tomatenpflanze" in sechs statt vier. Beide Zerlegungen sind richtig, sie stammen nur aus verschiedenen Stempelkästen. Eine Tokenzahl gilt also immer für einen bestimmten Tokenizer.

### Deutsch kann mehr Tokens brauchen

Für Englisch gibt ein großer Anbieter als Faustregel an, dass ein Token etwa vier Zeichen oder drei Viertel eines Wortes entspricht. Er schreibt selbst dazu, dass andere Sprachen andere Verhältnisse haben. Ein eigener Test mit einem Satz und seiner Übersetzung zeigt, wie groß der Unterschied sein kann:

| Satz | Neuerer Tokenizer | Älterer Tokenizer |
| --- | --- | --- |
| „Die Gärtnerei liefert jeden Morgen frische Tomatenpflanzen an die Wochenmärkte in der Umgebung." | 23 Tokens | 30 Tokens |
| „The nursery delivers fresh tomato plants to the weekly markets in the area every morning." | 16 Tokens | 16 Tokens |

In diesem Satzpaar braucht Deutsch deutlich mehr Tokens. Das ist ein Beispiel, keine Statistik für alle Texte und Tokenizer. Eine Untersuchung von 2023 hat das systematisch über viele Sprachen gemessen: Derselbe Inhalt brauchte je nach Sprache bis zu 15-mal so viele Tokens. Die Autoren nennen drei Folgen, die du in den nächsten Abschnitten wiederfindest: höhere Kosten, längere Antwortzeiten und weniger Platz im Kontext. Wo genau Deutsch liegt, hängt vom Tokenizer ab.

> **Beispielbox, Stand 14.10.2026: die Tokenizer dieses Abschnitts.** Gezählt wurde mit den Tokenizern o200k_base (neuer) und cl100k_base (älter) von OpenAI über das Programmpaket gpt-tokenizer 4.0.0. Öffentliche Tokenzähler findest du bei mehreren Anbietern. Sie zeigen für dieselben Wörter je nach Modell andere Zerlegungen.

---

## 2. Das Kontextfenster: der Pflanztisch

Du stehst am Pflanztisch. Alles, womit du gerade arbeitest, muss auf der Tischplatte liegen: der Auftrag, die Töpfe, die Erde, das Etikett. Was nicht auf dem Tisch liegt, kannst du nicht verwenden, auch wenn es irgendwo im Lager steht. Und die Platte hat eine feste Größe.

Beim Sprachmodell heißt diese Tischplatte **Kontextfenster**: die größte Zahl an Tokens, die das Modell bei einem Aufruf gleichzeitig berücksichtigen kann. Auf dem Tisch liegt bei einem Chat-Assistenten deutlich mehr als deine letzte Nachricht:

- **Anweisungen des Anbieters oder Betreibers**, die du meist gar nicht siehst.
- **Deine dauerhaften Anweisungen** und Projektvorgaben (A2, A7).
- **Der bisherige Gesprächsverlauf**, also deine Nachrichten und die Antworten.
- **Mitgegebenes Material**: Dateien, Bilder, Suchergebnisse, Ergebnisse von Werkzeugen.
- **Die Antwort, die gerade entsteht.** Jedes neu erzeugte Token belegt ebenfalls Platz.

Der letzte Punkt wird gern übersehen. Die Dokumentation eines großen Anbieters zählt die erzeugte Antwort ausdrücklich zum Kontextfenster, bei Modellen mit Denkschritten auch diese Schritte (D7). Wenn du ein fast volles Fenster mit Material füllst, bleibt für die Antwort wenig Platz. Zusätzlich haben viele Modelle eine eigene Obergrenze für die Länge einer Antwort.

Die Größe des Fensters wird in Tokens angegeben und hängt vom Modell ab. Sie reicht von vergleichsweise kleinen Fenstern bis in den Millionenbereich. Ein Hersteller gibt für eines seiner Modelle sogar zehn Millionen Tokens an. Das ist die beworbene Obergrenze des Modells, und einzelne Dienste können weniger anbieten. Die genauen Werte ändern sich laufend, das Prinzip bleibt. Wie viel Text das ist, hängt vom Tokenizer und von der Sprache ab (Abschnitt 1). Das Kontextfenster ist etwas anderes als das Wissen aus dem Training (E1): Das Training hat die Gewichte geformt, das Kontextfenster ist der Arbeitsbereich für diese eine Anfrage. Ein Anbieter beschreibt es in seiner Dokumentation als eine Art Arbeitsgedächtnis.

Wo das Bild nicht passt: Am echten Pflanztisch überblickst du alles gleich gut. Das Sprachmodell nutzt nicht jede Stelle des Fensters gleich zuverlässig. Dazu mehr in Abschnitt 4.

---

## 3. Warum Modelle „vergessen"

Stell dir eine Aushilfe vor, die jeden Morgen neu anfängt und sich an nichts vom Vortag erinnert. Damit sie trotzdem weiterarbeiten kann, legt ihr jemand vor Arbeitsbeginn alle Notizen auf den Tisch: was gestern besprochen wurde, was erledigt ist, was noch fehlt. Die Aushilfe ist so gut wie die Notizen auf dem Tisch.

So funktioniert ein Gespräch mit einem Chat-Assistenten. Das Sprachmodell hat zwischen zwei Aufrufen kein eigenes Gesprächsgedächtnis. Damit es anknüpfen kann, muss die Software den nötigen Kontext bei jeder neuen Nachricht wieder bereitstellen. Im einfachen Fall schickt sie den bisherigen Verlauf zusammen mit deiner neuen Nachricht an das Modell. Die Dokumentation eines Anbieters beschreibt für seine Schnittstelle genau das: Jede Runde enthält die bisherige Unterhaltung plus die neue Nachricht. Das „Gedächtnis" im Gespräch ist also der mitgeschickte Text.

Solange der Tisch groß genug ist, geht das gut. Irgendwann wird der Verlauf aber länger als das Kontextfenster. Dann muss etwas passieren, und was genau, entscheidet die Software um das Modell herum:

- **Ältere Teile fallen heraus.** Chat-Oberflächen können nach dem Prinzip „wer zuerst kam, geht zuerst" den Anfang des Gesprächs abschneiden. Deine Vorgabe aus der ersten Nachricht liegt dann nicht mehr auf dem Tisch.
- **Ältere Teile werden zusammengefasst.** Manche Systeme ersetzen den frühen Verlauf durch eine Zusammenfassung. Das spart Platz, kostet aber Details, und Fehler in der Zusammenfassung wandern mit (E3).
- **Es gibt eine Fehlermeldung.** Wer ein Modell direkt über eine Schnittstelle anspricht (P2), bekommt bei zu langer Eingabe je nach Anbieter einen Fehler statt einer Antwort.

Damit ist die Szene vom Anfang zum Teil erklärt. Wenn deine Vorgabe „keine Aufzählungen" aus dem Fenster gefallen ist, kann das Modell sie nicht befolgen. Sie war beim letzten Aufruf schlicht nicht mehr auf dem Tisch.

Die Grenze dieses Bildes: Erinnerungsfunktionen (Memory) und dauerhafte Anweisungen (E3, A2) wirken wie ein Notizzettel, der jeden Morgen wieder obenauf gelegt wird. Auch sie landen im Kontextfenster und belegen dort Platz. Sie sind eine Form von Kontext, die die Software für dich verwaltet, und kein Gedächtnis im Modell.

---

## 4. Warum lange Gespräche driften

Manchmal liegt deine Vorgabe noch auf dem Tisch, und das Gespräch driftet trotzdem. Dafür gibt es neben dem Herausfallen weitere Ursachen.

**Die Position macht einen Unterschied.** Die Untersuchung „Lost in the Middle" kennst du aus E3. Informationen am Anfang und am Ende langer Eingaben wurden dort besser genutzt als solche in der Mitte. Eine Vorgabe aus deiner ersten Nachricht bleibt dabei nah am Anfang, weil neue Nachrichten hinten angehängt werden. In die Mitte geraten eher Dinge, die ihr zwischendurch geklärt habt, wie die Entscheidung von vor zwanzig Nachrichten aus der Szene am Anfang. Die Studie zeigt, dass die Position die Zuverlässigkeit beeinflussen kann. Wie stark, hängt vom Modell ab.

**Mehr Text, weniger Zuverlässigkeit.** Ein technischer Bericht von 2025 testete 18 Modelle mit einfachen Aufgaben und unterschiedlich langen Eingaben. Die Ergebnisse wurden mit wachsender Länge unzuverlässiger, auch wenn die Aufgabe gleich einfach blieb. Der Bericht stammt von einem Anbieter von Suchtechnik für KI-Anwendungen, der ein geschäftliches Interesse an dem Thema hat. Er trägt den Titel **Context Rot**, und auch die Dokumentation eines Modellanbieters verwendet den Begriff: das allmähliche Nachlassen von Genauigkeit und Erinnerung, je mehr Tokens im Kontext stehen. Es ist eine Bezeichnung aus der Praxis, keine genormte Fachdefinition. Dieser Effekt hängt an der Gesamtlänge und kann deshalb auch Vorgaben vom Anfang treffen.

**Frühe Annahmen setzen sich fest.** Eine Studie, 2026 auf einer großen Fachkonferenz veröffentlicht, verglich 15 Modelle. Jede Aufgabe wurde einmal in einer einzigen vollständigen Nachricht gestellt und einmal über mehrere Nachrichten verteilt. Die Gespräche waren simuliert, die Angaben einer Aufgabe wurden schrittweise nachgereicht. In den simulierten Gesprächen schnitten alle Modelle schlechter ab, im Mittel um 39 Prozent. Die Fähigkeit sank dabei nur wenig, die Zuverlässigkeit dagegen deutlich. Als Ursache beschreiben die Autoren, dass Modelle früh Annahmen treffen, vorschnell eine Lösung liefern und sich danach zu stark auf diese eigene frühe Antwort stützen.

Das passt zu einem Mechanismus, den du aus Abschnitt 3 kennst. Die Antworten des Modells liegen ab der nächsten Runde selbst auf dem Tisch. Ein Fehler in Antwort drei ist ab Runde vier Teil des Kontexts und kann alles Weitere färben. In A7 hast du eine Untersuchung kennengelernt, in der aus früheren Gesprächen abgeleiteter Kontext bei drei von fünf Modellen die Zustimmungsneigung deutlich erhöht hat.

**Der Tisch wird voll mit Nebensachen.** Jede verworfene Idee, jede korrigierte Version und jeder Umweg bleiben im Verlauf. Das Relevante liegt zwischen immer mehr Überholtem. Das ist A2s „Auszug statt Aktenordner", nur dass der Aktenordner diesmal von selbst wächst.

---

## 5. Warum Kontext Speicher und Rechenzeit kostet

Zurück an den Pflanztisch. Bei jedem neuen Etikett müsste die Aushilfe eigentlich alle Notizen noch einmal von vorn lesen. Das dauert. Also schreibt sie sich beim ersten Lesen zu jedem Zettel eine kurze Randnotiz und schaut beim nächsten Etikett nur noch auf die Randnotizen. Das spart Zeit, aber die Randnotizen brauchen Platz, und für jeden neuen Zettel kommt eine dazu.

Ein Sprachmodell macht es genauso. Beim Einlesen berechnet es für jedes Token Zwischenergebnisse, die es beim Erzeugen jedes weiteren Tokens wieder braucht. Damit es sie nicht ständig neu berechnen muss, legt es sie in einem **Zwischenspeicher** ab. In technischen Texten heißt er **KV-Cache**, nach den beiden Arten von Zwischenwerten, Schlüssel und Werte (englisch keys und values). Die Begriffe klärt D3.

In A9 hast du diesen Zwischenspeicher für das dortige Beispielmodell schon ausgerechnet: 57.344 Byte pro Token, also rund 1,75 GiB bei 32.768 Token. Andere Modelle kommen auf andere Werte, weil Schichten, Köpfe, Kopfgröße und Speicherformat in die Rechnung eingehen. Ein technischer Fachartikel eines Grafikkartenherstellers beschreibt die Formel dahinter und hält fest, dass der Bedarf linear mit der Länge der Eingabe wächst. Doppelt so viel Text heißt doppelt so viele Randnotizen. Dieser Speicher kommt zu den Gewichten des Modells hinzu, und das gilt im Rechenzentrum genauso wie auf deinem Rechner.

Beim Rechnen ist es noch etwas teurer. Beim Einlesen setzt das Modell jedes Token mit allen Tokens davor in Beziehung. Für diese Berechnung, die Self-Attention, gibt die Originalarbeit zur heute üblichen Bauart den Aufwand pro Schicht mit dem Quadrat der Länge an. Verdoppelst du die Eingabe, wächst dieser Teil der Arbeit grob auf das Vierfache. Wie diese Beziehungen zustande kommen, ist Thema von D3.

Der Unterschied zum Bild: Die Randnotizen der Aushilfe sind kurze Stichworte. Der Zwischenspeicher besteht dagegen aus Zahlen, und zwar aus einer ganzen Reihe für jedes Token in jeder Schicht. Er erspart Rechenarbeit, fasst den Inhalt aber nicht zusammen. Zunächst hilft er beim Erzeugen einer einzelnen Antwort. Ob Zwischenwerte auch zwischen getrennten Aufrufen wiederverwendet werden, hängt von der eingesetzten Software ab.

---

## 6. Warum Tokens Geld kosten

Wenn du ein Modell über eine Schnittstelle nutzt (P2), rechnet der Anbieter meist pro Token ab. Die Preise stehen meist pro Million Tokens, getrennt nach Eingabe und Ausgabe. In der Preisliste aus der Beispielbox ist die Ausgabe teurer als die Eingabe, das genaue Verhältnis hängt aber von Anbieter und Modell ab.

Jetzt kommt Abschnitt 3 ins Spiel. Weil der gesamte Verlauf bei jeder Runde neu mitgeschickt wird, bezahlst du ihn auch jedes Mal neu als Eingabe. Ein kleines Python-Programm rechnet ein Gespräch mit 20 Runden durch. Angenommen sind 500 Token Anweisungen, 200 Token pro Frage und 400 Token pro Antwort. Jede Runde enthält den vollständigen bisherigen Verlauf, Prompt Caching wird nicht genutzt. Die Preise entsprechen dem Modell aus der Beispielbox am Ende des Abschnitts:

```python
system, frage, antwort, runden = 500, 200, 400, 20
eingabe_gesamt = 0
for runde in range(1, runden + 1):
    eingabe = system + (runde - 1) * (frage + antwort) + frage
    eingabe_gesamt += eingabe
    if runde in (1, 10, 20):
        print("Runde", runde, "->", eingabe, "Token Eingabe")
ausgabe_gesamt = runden * antwort
print("Eingabe gesamt:", eingabe_gesamt, "Token")
print("Ausgabe gesamt:", ausgabe_gesamt, "Token")
preis_ein, preis_aus = 2.00, 10.00   # Dollar pro 1 Million Token
kosten = eingabe_gesamt / 1e6 * preis_ein + ausgabe_gesamt / 1e6 * preis_aus
print("Kosten:", round(kosten, 2), "Dollar")
```

```text
Runde 1 -> 700 Token Eingabe
Runde 10 -> 6100 Token Eingabe
Runde 20 -> 12100 Token Eingabe
Eingabe gesamt: 128000 Token
Ausgabe gesamt: 8000 Token
Kosten: 0.34 Dollar
```

Geschrieben wurden in diesem Gespräch nur 12.500 Token neuer Text: Anweisungen, 20 Fragen und 20 Antworten. Als Eingabe abgerechnet wurden 128.000 Token, also gut das Zehnfache des neu geschriebenen Textes. Die Ausgabe kommt zu ihrem eigenen Preis noch dazu. Die Eingabe der letzten Runde ist siebzehnmal so lang wie die der ersten. In diesem Beispiel sind das rund 34 US-Cent, aber das Muster zählt: Die Gesamtmenge wächst mit jeder Runde schneller, weil der Verlauf jedes Mal wieder mitfährt.

Anbieter können das mit **Prompt Caching** dämpfen. Dabei wird ein unveränderter Anfangsteil der Eingabe zwischengespeichert, sofern die Bedingungen des jeweiligen Verfahrens erfüllt sind, zum Beispiel ein exakt gleicher Anfang und eine begrenzte Lebensdauer. Bei einem späteren Treffer wird dieser Teil günstiger abgerechnet. Das senkt die Kosten, ändert aber nichts am Platz. Zwischengespeicherte Tokens belegen das Kontextfenster genauso.

Und wenn du ein Abo nutzt statt einer Schnittstelle? Dann zahlst du nicht pro Token, aber auch Abos haben Nutzungsgrenzen. Wie sie berechnet werden, legt jeder Anbieter selbst fest. Dass lange Gespräche mit großen Dateien mehr Rechenarbeit verursachen als kurze, gilt in jedem Fall (Abschnitt 5).

> **Beispielbox, Stand 14.10.2026: Preise und Fenster eines Anbieters.** Anthropic nennt für Claude Sonnet 5.5 pro Million Tokens 2 Dollar für die Eingabe und 10 Dollar für die Ausgabe. Eingabe aus dem Zwischenspeicher kostet 0,10 Dollar, das Kontextfenster umfasst 1 Million Tokens zum Standardpreis. Das Zehn-Millionen-Fenster aus Abschnitt 2 nennt Meta für Llama 4 Scout als Obergrenze des Modells. Preise, Modelle und Fenstergrößen ändern sich häufig. Schau vor einer Rechnung in die aktuelle Preisliste.

---

## 7. Was du daraus machst

Aus den Abschnitten 1 bis 6 ergeben sich ein paar Gewohnheiten. Einige kennst du schon aus E3 und A2, jetzt weißt du, warum sie wirken.

**Neues Thema, neues Gespräch.** Ein frisches Gespräch hat einen leeren Tisch. Nimm mit, was du brauchst, als kurze, selbst geprüfte Zusammenfassung (E3, A2).

**Wichtiges nach vorn oder ans Ende.** Vorgaben, die durchgehend gelten sollen, gehören an den Anfang oder in dauerhafte Anweisungen. Wird eine Entscheidung von zwischendurch später wieder wichtig, wiederhole sie kurz vor der Frage. In der Mitte eines langen Verlaufs wird so etwas häufig weniger zuverlässig berücksichtigt (Abschnitt 4).

**Vollständig fragen statt stückweise.** Wenn du die Aufgabe schon kennst, gib sie in einer Nachricht mit allen Angaben. Das verringert die Gefahr, dass sich frühe Annahmen festsetzen (Abschnitt 4, A2).

**Falsches nicht stehen lassen.** Ein Fehler im Verlauf wirkt weiter. Wenn eine Antwort auf einem Irrtum aufbaut, ist ein Neustart mit korrigiertem Startkontext oft besser als die dritte Korrektur. Konkret: neues Gespräch öffnen, eine korrigierte Zusammenfassung und die aktuelle Frage einfügen. Manche Werkzeuge erlauben es auch, eine frühere Nachricht zu bearbeiten und von dort neu anzusetzen.

**Auszug statt Aktenordner.** Jede Seite Material belegt Platz, kostet Rechenzeit und bei Bezahlung pro Token auch Geld (A2, Abschnitt 5 und 6).

**Ausgaben begrenzen, wo es passt.** Eine Antwort von fünf Sätzen braucht weniger Platz und ist schneller als eine von fünf Seiten. Für eine Übersicht reichen oft wenige Zeilen.

**Nachzählen statt raten.** Viele Anbieter stellen Tokenzähler bereit, und über eine Schnittstelle steht der Verbrauch in jeder Antwort. Ein Blick darauf zeigt dir schneller als jede Faustregel, wie voll der Tisch ist.

---

## Häufige Fehlgriffe

- **„Das Modell erinnert sich an unser Gespräch."** Es bekommt den Verlauf bei jeder Runde neu vorgelegt, und nur, solange er ins Fenster passt (Abschnitt 3).
- **„Ein großes Kontextfenster löst das Problem."** Mehr Platz verhindert das Herausfallen, aber nicht das Nachlassen der Genauigkeit bei langem Kontext (Abschnitt 4).
- **Token mit Wort oder Silbe gleichsetzen.** Tokens sind statistische Bausteine, und jeder Tokenizer schneidet anders (Abschnitt 1).
- **Die englische Faustregel auf Deutsch übertragen.** Deutsch kann deutlich mehr Tokens brauchen als Englisch (Abschnitt 1).
- **Die Antwort beim Platz vergessen.** Auch die Ausgabe und Denkschritte belegen das Kontextfenster (Abschnitt 2).
- **Bei Schnittstellen nur auf den Preis pro Token schauen.** Lange Gespräche schicken den Verlauf jedes Mal wieder mit, die Menge wächst mit jeder Runde (Abschnitt 6).
- **Vom Modell verlässliches Buchstabenzählen erwarten.** Text wird in Tokens verarbeitet, nicht Buchstabe für Buchstabe. Für genaue Zählaufgaben ist ein kleines Programm verlässlicher, und A5 zeigt, wie du solchen Code prüfst.

---

## Zum Ausprobieren

1. Öffne einen öffentlichen Tokenzähler eines Anbieters und gib „Gewächshaus", „Erdbeere" und den Namen deines Wohnorts ein. Notiere, wie viele Tokens jedes Wort braucht und wo die Grenzen liegen. Vergleiche mit Abschnitt 1. Welches deiner Wörter zerfällt am stärksten?
2. Nimm einen Absatz aus einem deiner Texte und seine Übersetzung ins Englische, die du selbst oder ein Werkzeug erstellst. Zähle beide im selben Tokenzähler. Schreibe das Verhältnis Deutsch zu Englisch auf.
3. Ändere im Programm aus Abschnitt 6 zuerst nur die Zahl der Runden von 20 auf 40 und notiere die gesamte Eingabe. Setze die Runden danach zurück auf 20 und ändere nur die Antwortlänge von 400 auf 100 Token. Was verändert die Summe stärker, und warum?
4. Führe mit einem Chat-Assistenten ein Gespräch mit mindestens 15 Nachrichten zu einem Thema deiner Wahl. Gib in der ersten Nachricht eine klare Formatvorgabe, zum Beispiel „Antworte immer in höchstens drei Sätzen". Notiere, ob und ab welcher Nachricht die Vorgabe nachlässt. Es kann gut sein, dass sie durchgehend eingehalten wird, und ein einzelner Verstoß zeigt noch nicht, dass das Kontextfenster voll war. Stelle danach dieselbe letzte Frage in einem neuen Gespräch mit kurzer Zusammenfassung und der Vorgabe am Anfang. Vergleiche beide Antworten.
5. Halte dein Ergebnis aus Übung 4 in drei Sätzen fest: was du beobachtet hast, welche Erklärungen aus Abschnitt 3 oder 4 infrage kommen und was du künftig anders ausprobieren möchtest.

Am Ende hast du eigene Tokenzählungen, eine Beobachtung zum Verhalten deines Werkzeugs in langen Gesprächen und eine kleine Rechnung, mit der du Kosten über eine Schnittstelle vorab abschätzt.

---

## Fazit

Ein Sprachmodell verarbeitet Text in Tokens, und alles, was es für eine Antwort nutzen soll, muss gleichzeitig ins Kontextfenster passen, die Antwort eingeschlossen. Ein eigenes Gesprächsgedächtnis hat es nicht, deshalb wird der Verlauf jedes Mal neu bereitgestellt, bis ältere Teile herausfallen oder zusammengefasst werden. Dass etwas im Fenster steht, heißt noch nicht, dass es zuverlässig genutzt wird, und langer Kontext kostet Speicher, Rechenzeit und Geld. Für dich heißt das: kurze, saubere Gespräche, Wichtiges an den Anfang, Neustart statt Dauerkorrektur. Als Nächstes geht es in D2 um Embeddings, die Zahlenreihen, in die ein Modell jedes Token übersetzt, und warum sie die Grundlage für Suche und RAG sind.

```yaml
dokument: ki-d1-tokens-und-kontextfenster
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-10-14
quellen_fachlich:
  - "Eigene Tokenzählung am 2026-10-14 mit dem npm-Paket gpt-tokenizer 4.0.0 (Tokenizer o200k_base und cl100k_base, Vokabular im Paket enthalten). o200k_base: Gewächshaus 3 (Gew|äch|shaus), Erdbeere 4 (E|rd|be|ere), Tomatenpflanze 4 (Tom|aten|pfl|anze), 192.168.178.1 7; cl100k_base: Gewächshaus 5 (G|ew|äch|sh|aus), Erdbeere 4, Tomatenpflanze 6 (Tom|aten|p|fl|an|ze). Satzpaar DE/EN: o200k 23/16, cl100k 30/16"
  - "OpenAI Help Center: What are tokens and how to count them. https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them (Zugriff 2026-10-14): Englisch etwa 4 Zeichen bzw. drei Viertel Wort pro Token, Schätzwerte; andere Sprachen haben andere Verhältnisse; Kontextfenster begrenzt Tokens pro Anfrage, zusätzlich eigene Ausgabegrenze"
  - "Petrov, La Malfa, Torr, Bibi: Language Model Tokenizers Introduce Unfairness Between Languages. NeurIPS 2023, arXiv:2305.15425. https://arxiv.org/abs/2305.15425 (Zugriff 2026-10-14): Tokenisierungslänge desselben Inhalts unterscheidet sich je nach Sprache bis zum 15-Fachen; Folgen für Kosten, Verarbeitungszeit und Menge an Kontext"
  - "Anthropic Docs: Context windows. https://platform.claude.com/docs/en/build-with-claude/context-windows (Zugriff 2026-10-14): Kontextfenster umfasst allen Text inkl. der Antwort selbst und der Denkschritte; Arbeitsgedächtnis, verschieden vom Trainingskorpus; jede Runde enthält den gesamten bisherigen Verlauf; Chat-Oberflächen können nach 'first in, first out' verwalten; zu lange Eingabe über die API ergibt Fehler; Compaction fasst frühere Teile zusammen; 'context rot': Genauigkeit und Erinnerung lassen mit wachsender Tokenzahl nach; zwischengespeicherte Präfixe belegen weiterhin das Kontextfenster"
  - "Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang: Lost in the Middle: How Language Models Use Long Contexts. TACL 12 (2024), S. 157-173, DOI 10.1162/tacl_a_00638 (Zugriff 2026-10-14): Leistung oft am höchsten bei relevanter Information am Anfang oder Ende, deutlich schlechter in der Mitte langer Kontexte, auch bei Langkontext-Modellen"
  - "Hong, Troynikov, Huber (Chroma): Context Rot: How Increasing Input Tokens Impacts LLM Performance (2025-07-14). https://www.trychroma.com/research/context-rot (Zugriff 2026-10-14): 18 Modelle, Leistung mit wachsender Eingabelänge zunehmend unzuverlässig, auch bei einfachen Aufgaben; Anbieter mit geschäftlichem Interesse; Bewertung teils durch Sprachmodell als Richter"
  - "Laban, Hayashi, Zhou, Neville: LLMs Get Lost In Multi-Turn Conversation. ICLR 2026 (Oral), https://iclr.cc/virtual/2026/oral/10009147; zuvor arXiv:2505.06120 (2025-05-09), https://arxiv.org/abs/2505.06120 (Zugriff jeweils 2026-10-14): großangelegte Simulationsexperimente mit schrittweise nachgereichten Aufgabenangaben; 15 Modelle, mehrrundige Aufgaben im Mittel 39 % schlechter als einrundige über sechs Aufgabentypen; geringer Verlust an Fähigkeit, deutlicher Anstieg der Unzuverlässigkeit; frühe Annahmen und vorschnelle Lösungen, auf die sich Modelle danach zu stark stützen"
  - "NVIDIA Developer Blog: Mastering LLM Techniques: Inference Optimization. https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ (Zugriff 2026-10-14): Formel KV-Cache pro Token = 2 × Schichten × (Köpfe × Kopfgröße) × Bytes; Bedarf wächst linear mit Batchgröße und Sequenzlänge; Prefill verarbeitet Eingabe parallel, Decode erzeugt Tokens einzeln und ist speichergebunden"
  - "Sennrich, Haddow, Birch: Neural Machine Translation of Rare Words with Subword Units. ACL 2016, S. 1715-1725. https://aclanthology.org/P16-1162/ (Zugriff 2026-10-14): Metadaten gelesen; Teilwort-Tokenisierung mit Byte Pair Encoding für seltene Wörter, laut ACL-Würdigung (Test of Time Award 2026) heute Standard-Tokenisierung vieler großer Sprachmodelle. Abstract selbst nicht auf der Seite, Beschreibung im Text bewusst vereinfacht"
  - "Meta AI Blog: The Llama 4 herd (2025-04-05). https://ai.meta.com/blog/llama-4-multimodal-intelligence/ (Zugriff 2026-10-14): Llama 4 Scout mit Kontextfenster von 10 Millionen Tokens (Herstellerangabe)"
  - "Vaswani et al.: Attention Is All You Need (2017), arXiv:1706.03762, Tabelle 1. https://arxiv.org/html/1706.03762v7 (Zugriff 2026-10-14): Komplexität pro Schicht Self-Attention O(n²·d), n = Sequenzlänge; Umwandlung der Tokens in gelernte Embeddings vor der Verarbeitung"
  - "Anthropic Docs: Pricing. https://platform.claude.com/docs/en/about-claude/pricing (Zugriff 2026-10-14): Claude Sonnet 5.5 Eingabe 2 $/MTok, Cache-Lesen 0,10 $/MTok, Ausgabe 10 $/MTok, 1M Kontext zum Standardpreis; Ausgabe bei allen gelisteten Modellen das Fünffache der Eingabe, auch bei Claude Haiku 5.5 über 100.000 Tokens (0,50 $ Eingabe, 2,50 $ Ausgabe)"
  - "Anthropic Docs: Prompt caching. https://platform.claude.com/docs/en/build-with-claude/prompt-caching (Zugriff 2026-10-14): Cache-Lesen 0,1-fach des Eingabepreises (modellabhängige Ausnahmen), Standard-Lebensdauer 5 Minuten, Treffer nur bei identischem Präfix"
  - "Eigene Artikel der Reihe: E1 (Token, Training und Inferenz), E3 (Kontext, Kontextfenster, Lost in the Middle, Memory), A2 (Kontext-Paket, Auszug statt Aktenordner, Gespräch pflegen), A5 (Code prüfen), A7 (aus früheren Gesprächen abgeleiteter Kontext erhöhte Zustimmungsneigung bei drei von fünf Modellen), A9 (Zwischenspeicher 57.344 Byte pro Token, 1,75 GiB bei 32.768 Token); Vorwärtsverweise auf D2, D3, D7, P2"
  - "Rechnung in Abschnitt 6 am 2026-10-14 mit Python ausgeführt: 20 Runden, 500/200/400 Token: Eingabe Runde 1 700, Runde 10 6.100, Runde 20 12.100, gesamt 128.000; Ausgabe 8.000; 0,34 $ bei 2 $ und 10 $ pro Million; neuer Text 12.500 Token"
verifikation_offen:
  - "Tokenzählungen gelten nur für die zwei genannten Tokenizer; andere Anbieter zählen anders. Satzpaar ist eine Einzelmessung mit eigener Übersetzung, keine Statistik; die Aussage zum Aufschlag für Deutsch stützt sich auf diese Messung und die Petrov-Studie, deren deutsche Einzelwerte (Repo-CSV) nicht gelesen wurden"
  - "Aussage zu Buchstabenzählen ('Erdbeere') ist eine Erklärung aus der Tokenisierung, keine gemessene Fehlerquote; im Text vorsichtig formuliert ('je nach Modell', 'oft schwächer')"
  - "Spanne der Fenstergrößen: A9-Beispielmodell (32.768), Anthropic (1M), Meta Llama 4 Scout (10M, Herstellerangabe als Obergrenze des Modells, Angebote einzelner Dienste nicht geprüft); untere Grenze im Text bewusst ohne Zahl ('vergleichsweise kleine Fenster')"
  - "Verhalten bei vollem Fenster (Abschneiden, Zusammenfassen, Fehler) aus der Dokumentation eines Anbieters; andere Chat-Oberflächen nicht geprüft, im Text als 'kann' und 'je nach Anbieter' formuliert"
  - "NVIDIA-Formel nutzt die Zahl der Köpfe; bei gruppierten Schlüssel-Wert-Köpfen (A9-Beispiel) stehen dort die KV-Köpfe. Rechenaufwand quadratisch gilt für die Self-Attention pro Schicht laut Originalarbeit; 'grob auf das Vierfache' bezieht sich nur auf diesen Teil, nicht auf die gesamte Rechenzeit"
  - "Preisangabe 'Ausgabe das Fünffache der Eingabe' an der Anthropic-Preisliste geprüft (alle gelisteten Modelle); eine weitere Preisliste eines zweiten Anbieters wurde abgerufen, ließ sich aber nicht unabhängig bestätigen und wird nicht zitiert"
  - "Tipp 'frühere Nachricht bearbeiten' ist allgemein formuliert ('manche Werkzeuge'), einzelne Produkte nicht geprüft"
  - "A9-Pflegehinweis: In A9 steht die Zwischenspeicher-Formel unter verifikation_offen als 'nicht wörtlich belegt'. Der NVIDIA-Blog nennt sie wörtlich (Zugriff 2026-10-14). Kann in A9 nachgetragen werden, Entscheidung bei David"
review_historie:
  - runde: 0
    datum: 2026-10-14
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Tokenzählungen mit echtem Tokenizer gemessen, Kostenrechnung per Python ausgeführt, Studien und Anbieterdokumentation an der Quelle gelesen. Abgrenzung: E3 und A2 liefern die Praxis, D1 das Warum."
  - runde: 1
    datum: 2026-10-14
    ergebnis: "Eigene Reviews (Fach und Stil): drei Verneinungs-Gegensätze aufgelöst, zwei lange Sätze geteilt, A7-Verweis auf den tatsächlichen Befund eingeengt (drei von fünf Modellen, abgeleiteter Kontext), Buchstabenebene und Preisvergleich vorsichtiger bzw. konkret formuliert. Code aus dem Artikel erneut ausgeführt, Ausgabe identisch. Beim Gegenlesen korrigiert: 'Erdbeere' enthält zwei r, nicht drei (per Python gezählt); unbelegte Einordnung von Deutsch im Sprachvergleich durch Verweis auf den eigenen Test ersetzt."
  - runde: 2
    datum: 2026-10-14
    ergebnis: "Drei externe Reviews, Behauptungen gegengeprüft. Übernommen: Token-IDs werden vor der Verarbeitung zu Embeddings (Vorbereitung D2), Buchstaben-Erklärung entschärft; 'kein eigenes Gesprächsgedächtnis' statt 'behält nichts'; Fenstergrößen bis in den Millionenbereich (Meta nennt 10 Mio. für Llama 4 Scout); Mehrrunden-Studie inzwischen ICLR 2026, simulierte Gespräche benannt; Kostenrechnung ohne Caching und mit vollständigem Verlauf gekennzeichnet; Tokenizer-Box in Abschnitt 1, Preisbox ans Ende von Abschnitt 6; Überschrift 'Deutsch kann mehr Tokens brauchen'; Übungen 3 bis 5 entflochten und vorsichtiger ausgewertet; Fazit gekürzt; BPE-Quelle ergänzt. Nicht übernommen: Haiku-5.5-Preise als Gegenbeispiel zum Preisverhältnis (nicht bestätigt, Reviewer mischte zwei Preisstufen; Text trotzdem an die Beispielbox gebunden), Größenvergleich KV-Cache mit Foto (neues, unbelegtes Bild), Tokenizer-Namen im Fließtext (Stilregel: Produktnamen nur in Beispielboxen, stattdessen eigene Box in Abschnitt 1)."
  - runde: 3
    datum: 2026-10-14
    ergebnis: "Drei Re-Reviews. Übernommen: Abschnitt 4 trennt Positionseffekt (Lost in the Middle, betrifft eher zwischendurch Geklärtes, da neue Nachrichten hinten angehängt werden) und Längeneffekt (Context Rot); Abschnitt 7 entsprechend abgeschwächt; BPE-Satz präzisiert; Fenstergrößen ohne unbelegte Untergrenze, Scout als Modellobergrenze; KV-Cache gegen Prompt Caching abgegrenzt, Caching an Bedingungen gebunden; Haiku-Satz aus der Box gestrichen (wirkte wie Gegenbeispiel). Haiku- und Scout-Angaben waren in Runde 2 an den Originalquellen bestätigt; ein Reviewer hat seine Haiku-Beanstandung zurückgenommen. Nicht übernommen: Tokenizer-Namen und Konferenzname im Fließtext sowie eigener Quellenabschnitt mit Links (Entscheidung zur Reihe vom 01.10.2026: Typ C ohne Quellenzitate im Fließtext und ohne Linkliste, Quellen im YAML)."
  - runde: 4
    datum: 2026-10-14
    ergebnis: "Freigabe durch David am 2026-10-14 nach Runde 3. Kopfzeile und YAML-Status gemeinsam auf final. Abschluss-Sweep ohne Befund. Offen bleiben die Punkte unter verifikation_offen, darunter der A9-Pflegehinweis zur Zwischenspeicher-Formel."
```