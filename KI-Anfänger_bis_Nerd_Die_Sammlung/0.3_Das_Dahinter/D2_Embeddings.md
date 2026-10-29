# KI-D2 · Embeddings: Bedeutung als Ort auf einer Karte

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D2 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du suchst in deinen Unterrichtsnotizen nach „Rechner fährt nicht hoch". Die Suche findet nichts. Dabei steht der passende Abschnitt da, nur heißt er „Laptop startet nicht". Die entscheidenden Wörter stimmen nicht überein, und eine einfache Stichwortsuche findet den Abschnitt deshalb womöglich nicht. Eine Suche, die Ähnlichkeiten in der Bedeutung berücksichtigt, kann die Stelle trotzdem finden.

Möglich machen das **Embeddings**: Zahlenreihen, die Bedeutung so ablegen, dass Ähnliches nah beieinander liegt. Am Ende dieses Artikels kannst du erklären, was ein Embedding ist und wie du Nähe zwischen zwei Embeddings misst. Du weißt, wo Embeddings im Sprachmodell stecken und wie semantische Suche damit arbeitet. Und du kennst die Stellen, an denen Nähe in die Irre führt.

Vorausgesetzt wird D1, vor allem die Token-IDs aus Abschnitt 1. Hilfreich sind A3 (Recherche mit Quellenprüfung) und E7 (Datenschutz). Python brauchst du nur, wenn du die Beispiele selbst laufen lassen willst.

---

## 1. Eine Karte für Pflanzen

In der Gärtnerei hängt eine Karte an der Wand. Nach rechts geht es von Schatten zu voller Sonne, nach oben von trocken zu nass. Jede Pflanze hat dort ihren Platz. Tomate und Gurke stehen dicht beieinander oben rechts: viel Sonne, viel Wasser. Der Farn steht oben links im feuchten Schatten, der Kaktus unten rechts in der trockenen Sonne. Wer eine Pflanze für einen bestimmten Standort sucht, schaut einfach in die passende Ecke.

So ähnlich kannst du dir ein **Embedding** vorstellen. Es ist eine Liste von Zahlen, ein **Vektor**, der einem Stück Text einen Ort in einem Raum zuweist. Die Zahlen sind gelernt, und je nach Trainingsziel liegen dort Wörter oder Texte nah beieinander, die das Modell als ähnlich gelernt hat. Die Anzahl der Zahlen heißt **Dimension**. Die Pflanzenkarte hat zwei Dimensionen, Licht und Wasser.

Wo das Bild nicht passt: Echte Embeddings haben statt zwei Dimensionen Hunderte oder Tausende. Niemand hat diese Achsen benannt oder festgelegt. Sie entstehen beim Training, und eine einzelne Achse bedeutet in der Regel nichts, was sich so sauber benennen ließe wie „Licht". Bedeutung steckt im Zusammenspiel aller Zahlen.

---

## 2. Wie sich Nähe messen lässt

Auf der Karte siehst du mit einem Blick, was nah ist. Ein Programm braucht dafür eine Rechnung, und dafür gibt es mehrere Arten. Sehr verbreitet ist die **Kosinus-Ähnlichkeit**. Sie vergleicht die Richtung zweier Vektoren, ihre Länge spielt keine Rolle. Stell dir dazu die Mitte der Karte als Nullpunkt vor, von dem aus jede Pflanze einen Pfeil bekommt. Gemessen wird der Winkel zwischen zwei Pfeilen, nicht der Abstand zwischen zwei Pflanzen.

- **1** heißt: genau dieselbe Richtung, auch wenn die Pfeile unterschiedlich lang sind.
- **0** heißt: Die Pfeile stehen im rechten Winkel.
- **−1** heißt: genau entgegengesetzte Richtung.

Was diese Werte inhaltlich bedeuten, hängt vom Modell ab. Eine 0 heißt nicht automatisch, dass zwei Dinge nichts gemeinsam haben, und ein negativer Wert macht zwei Wörter noch nicht zu Gegenteilen.

Ein kleines Python-Programm rechnet das für die Pflanzenkarte aus. Die Werte sind ausgedacht. Jede Koordinate liegt zwischen −1 und +1. Beim Licht reicht die Skala von Schatten bis volle Sonne, beim Wasser von trocken bis nass. Der Wert 0 bedeutet jeweils mittel:

```python
from math import sqrt

def kosinus(a, b):
    skalar = sum(x * y for x, y in zip(a, b))
    laenge_a = sqrt(sum(x * x for x in a))
    laenge_b = sqrt(sum(y * y for y in b))
    return skalar / (laenge_a * laenge_b)

# (Licht, Wasser) von -1 (Schatten, trocken) bis +1 (volle Sonne, nass), ausgedacht
pflanzen = {
    "Tomate": (0.8, 0.5),
    "Gurke":  (0.7, 0.7),
    "Farn":   (-0.7, 0.6),
    "Kaktus": (0.9, -0.8),
}

for name in ("Gurke", "Farn", "Kaktus"):
    print("Tomate und", name, round(kosinus(pflanzen["Tomate"], pflanzen[name]), 2))
```

```text
Tomate und Gurke 0.97
Tomate und Farn -0.3
Tomate und Kaktus 0.28
```

Die Gurke passt fast genau zur Tomate. Der Kaktus teilt immerhin die Sonne, der Farn zeigt in eine andere Richtung. Mit Tausenden Dimensionen bleibt die Rechnung genau dieselbe, nur die Listen werden länger.

---

## 3. Echte Wortvektoren: Nähe aus der Verwendung

Jetzt mit echten Zahlen. Für Deutsch gibt es frei verfügbare **Wortvektoren**, bei denen Wörter auf Vektoren mit 300 Dimensionen abgebildet werden. Gelernt wurden sie aus großen Textmengen aus dem Netz und aus einer Online-Enzyklopädie (Beispielbox am Ende des Abschnitts). Gemessen mit der Kosinus-Ähnlichkeit:

| Wortpaar | Ähnlichkeit |
| --- | --- |
| Tomate, Gurke | 0,56 |
| Tomate, Rose | 0,24 |
| Tomate, Laptop | 0,05 |
| Router, Switch | 0,61 |
| Hund, Katze | 0,68 |
| heiß, kalt | 0,69 |
| sicher, unsicher | 0,74 |

Die ersten Zeilen sehen aus wie erwartet: Gemüse liegt bei Gemüse, Netzwerkgeräte bei Netzwerkgeräten, und zwischen Tomate und Laptop ist fast nichts. Die letzten beiden Zeilen überraschen. „Heiß" und „kalt" liegen näher beieinander als Tomate und Gurke, „sicher" und „unsicher" sogar noch näher.

Das liegt daran, wie solche Vektoren entstehen. Das Verfahren lernt aus den Wörtern, die in den Texten um ein Wort herum stehen. Wörter, die in ähnlicher Umgebung vorkommen, bekommen ähnliche Vektoren. Dieser Leitgedanke ist in der Sprachwissenschaft schon Jahrzehnte alt: Ein Wort erkennst du an der Gesellschaft, in der es auftritt. Und Gegenteile tauchen in denselben Sätzen auf. „Das Wasser ist heiß" und „Das Wasser ist kalt" unterscheiden sich in genau einem Wort.

Daraus folgt die wichtigste Regel dieses Abschnitts: **Bei diesen Wortvektoren heißt Nähe vor allem „wird in ähnlicher Umgebung verwendet". Gleichbedeutend sind nahe Wörter deshalb noch lange nicht.** Ein Embedding weiß, dass „sicher" und „unsicher" zum selben Themenfeld gehören. Dass sie das Gegenteil voneinander sind, ist in einer einzelnen Zahl nicht zu sehen.

> **Beispielbox, Stand 14.10.2026: die Wortvektoren dieses Abschnitts.** Gemessen mit dem deutschen Modell de_core_news_md 3.8.0 der Programmbibliothek spaCy. Die Vektoren wurden mit dem Verfahren fastText (cbow) aus OSCAR Common Crawl und Wikipedia gelernt. Das Modell enthält 20.000 Vektoren für 500.000 Wörter, seltenere Wörter teilen sich also einen Vektor mit einem ähnlichen Wort. „Kennwort" zum Beispiel bekommt denselben Vektor wie „Passwort", die Ähnlichkeit liegt deshalb bei genau 1. Für eigene Messungen lohnt ein Blick, ob zwei Wörter wirklich eigene Vektoren haben. Wie du Bibliothek und Modell installierst, steht in deren Dokumentation.
>
> ```python
> import spacy
>
> nlp = spacy.load("de_core_news_md")
> paare = [("Tomate", "Gurke"), ("Tomate", "Rose"), ("Tomate", "Laptop"),
>          ("Router", "Switch"), ("Hund", "Katze"),
>          ("heiß", "kalt"), ("sicher", "unsicher")]
> for a, b in paare:
>     print(a, b, round(float(nlp.vocab[a].similarity(nlp.vocab[b])), 2))
> ```

---

## 4. Wo Embeddings im Sprachmodell stecken

Erinnerst du dich an den Stempelkasten aus D1? Jeder Stempel hatte eine Nummer, die Token-ID, und das Modell wandelt jede Token-ID zu Beginn in ein Embedding um. Technisch ist das eine große Tabelle: Für jedes Token im Vokabular gibt es eine Zeile, und in jeder Zeile steht ein Vektor. Die Token-ID sagt, welche Zeile gelesen wird.

Bei dem offen dokumentierten Modell mit 7 Milliarden Parametern, das du aus A9 kennst, hat diese Tabelle 152.064 Zeilen mit je 3.584 Zahlen. Das sind rund 545 Millionen Zahlen allein für den Eingang. Das Modell hat außerdem eine zweite, gleich große Tabelle am Ausgang, mit der es aus seinen Rechenergebnissen Werte für die möglichen nächsten Tokens berechnet, aus denen dann Wahrscheinlichkeiten werden (D4). Beide Tabellen zusammen kommen nach diesen Maßen auf rund 1,09 Milliarden der insgesamt rund 7,6 Milliarden Parameter. Die Modellkarte rundet ihre eigenen Angaben etwas anders. Alle diese Zahlen sind beim Training entstanden (D5), genau wie die übrigen Gewichte.

Ein Unterschied zu den Wortvektoren aus Abschnitt 3 ist wichtig. Dort hat „Bank" genau einen Vektor, egal ob die Parkbank oder das Geldinstitut gemeint ist. Im Sprachmodell ist das Embedding aus der Tabelle nur der Startpunkt. Die folgenden Schichten verändern den Vektor jedes Tokens, je nachdem, welche Tokens drumherum stehen. Nach ein paar Schichten liegt „Bank" in „Ich sitze auf der Bank im Park" an einem anderen Ort als in „Ich zahle Geld bei der Bank ein". Wie die Tokens sich dabei gegenseitig beeinflussen, erklärt D3.

---

## 5. Embeddings für die Suche

Zurück zur Szene vom Anfang. Damit eine Suche „Rechner fährt nicht hoch" mit „Laptop startet nicht" verbindet, braucht sie ein Embedding für einen ganzen Satz oder Abschnitt.

Der naheliegende Versuch: alle Wortvektoren eines Satzes zusammenrechnen und den Mittelwert nehmen. Mit den Wortvektoren aus Abschnitt 3 sieht das so aus:

```python
import spacy

nlp = spacy.load("de_core_news_md")
frage = nlp("Wie gieße ich Tomaten richtig?")
for satz in ("Die Tomaten brauchen mehr Wasser.", "Mein Laptop startet nicht."):
    print(satz, round(float(frage.similarity(nlp(satz))), 2))
a, b = nlp("Das Passwort ist sicher."), nlp("Das Passwort ist nicht sicher.")
print("Verneinung:", round(float(a.similarity(b)), 2))
```

```text
Die Tomaten brauchen mehr Wasser. 0.29
Mein Laptop startet nicht. 0.46
Verneinung: 0.98
```

Das geht gründlich schief. Die Frage nach dem Gießen landet näher am Laptop als an den durstigen Tomaten. Der einfache Mittelwert berücksichtigt nicht gezielt, welche Wörter für die Frage wichtig sind. Die verwendeten Wortvektoren wurden außerdem nicht eigens für die Ähnlichkeit ganzer Sätze trainiert. Und zwei Sätze mit entgegengesetzter Aussage sind fast deckungsgleich, weil sich nur ein einziges Wort unterscheidet.

Deshalb gibt es **Embedding-Modelle**, die eigens dafür trainiert sind, ganzen Sätzen oder Abschnitten einen Vektor zu geben. Eine viel zitierte Arbeit von 2019 hat das an englischen Testdaten verglichen, bei denen Menschen die Ähnlichkeit von Satzpaaren bewertet hatten. Gemittelte klassische Wortvektoren (GloVe) erreichten dort im Schnitt rund 61 Punkte, das beste eigens trainierte Satzmodell rund 77. Gemessen wurde, wie gut die Rangfolge der Modellbewertungen mit der Rangfolge der menschlichen Bewertungen übereinstimmt. Höhere Werte sind besser. Prozentwerte sind das nicht. Auch beim Tempo lag ein großer Unterschied. Das ähnlichste Satzpaar innerhalb einer Sammlung von 10.000 Sätzen zu finden, dauerte mit dem Satzmodell etwa 5 Sekunden. Ein großes Modell, das jedes Paar gemeinsam verarbeitet, hätte nach Schätzung der Autoren rund 65 Stunden gebraucht. Das sind Werte des damaligen Vergleichs, keine Laufzeiten heutiger Modelle.

Eine **semantische Suche** läuft dann in drei Schritten:

1. **Vorbereiten.** Die Dokumente werden in Abschnitte zerlegt, jeder Abschnitt bekommt sein Embedding, und alle Vektoren werden gespeichert. Spezielle Datenbanken dafür heißen **Vektordatenbanken**.
2. **Fragen.** Die Suchanfrage bekommt mit demselben Modell ebenfalls ein Embedding.
3. **Finden.** Die Abschnitte, deren Vektoren der Anfrage am nächsten liegen, kommen als Ergebnis zurück.

Auf der Pflanzenkarte wäre das so: Jemand fragt nach einer Pflanze für feuchten Schatten, und du schaust in die Ecke oben links. Gesucht wird der Ort. Wie die Pflanze heißt, spielt dabei keine Rolle.

Eine häufige Anwendung semantischer Suche ist **RAG** (Retrieval-Augmented Generation). Dabei werden passende Abschnitte aus einer größeren Dokumentensammlung abgerufen und auf den Pflanztisch aus D1 gelegt, also ins Kontextfenster. Das Sprachmodell formuliert damit seine Antwort. Der Abruf kann über Embeddings laufen, über eine Stichwortsuche oder über eine Kombination aus beidem. Kleinere Dokumente landen dagegen oft komplett im Kontextfenster, ganz ohne Suche. Wie du das selbst baust, ist Thema von P4.

---

## 6. Wo Nähe in die Irre führt

**Gegenteile und Verneinung.** Abschnitt 3 und 5 haben es gezeigt: „Sicher" und „nicht sicher" liegen eng beieinander. Auch trainierte Embedding-Modelle haben damit zu kämpfen. Eine 2024 veröffentlichte Studie prüfte Suchsysteme mit Dokumentpaaren, die sich nur durch eine Verneinung unterscheiden. Viele Systeme, auch damals führende, ordneten diese Paare nicht besser als der Zufall. Größere und gezielt nachtrainierte Modelle schnitten besser ab, blieben aber deutlich hinter Menschen.

**Ähnlich heißt nicht richtig.** Eine semantische Suche liefert, was der Frage ähnlich ist. Ob der gefundene Abschnitt die Frage beantwortet oder überhaupt stimmt, prüft sie nicht. Das bleibt deine Aufgabe, wie in A3: Fundstelle öffnen, lesen, gegenprüfen.

**Jedes Modell hat seine eigene Karte.** Vektoren aus zwei verschiedenen Embedding-Modellen sind normalerweise nicht direkt vergleichbar, so wenig wie Koordinaten von zwei Karten mit unterschiedlichen Achsen. Es gibt zwar Verfahren, die zwei solche Räume nachträglich aufeinander ausrichten. Bei einem gewöhnlichen Wechsel des Embedding-Modells werden die gespeicherten Dokumente aber neu eingebettet.

**Vorurteile stecken mit drin.** Embeddings lernen aus Texten, wie Wörter verwendet werden, und damit auch die Vorurteile in diesen Texten. Eine bekannte Studie von 2016 fand in Wortvektoren, die mit Nachrichtentexten trainiert wurden, deutliche Geschlechterklischees bei Berufen. Woher solche Verzerrungen kommen und was daraus folgt, behandelt D9.

**Embeddings sind nicht automatisch anonym.** Es liegt nahe zu denken, aus einer Zahlenreihe ließe sich der Text nicht mehr zurückgewinnen. Eine Studie von 2023 zeigte, dass das unter bestimmten Bedingungen doch geht. In ihrem Versuchsaufbau stellten die Autoren 92 Prozent der untersuchten Eingaben mit 32 Tokens exakt wieder her. In einem weiteren Versuch gewannen sie vollständige Namen aus einer Sammlung klinischer Notizen zurück. Das ist keine allgemeine Erfolgsquote für beliebige Embedding-Modelle, zeigt aber, dass Embeddings vertrauliche Angaben preisgeben können. Für dich heißt das: Vertrauliche Dokumente gehören nur in dafür freigegebene Umgebungen, auch wenn dort „nur" Embeddings gespeichert werden (E7, R1).

---

## 7. Was du daraus machst

**Bei der Suche in eigenen Dokumenten die Wörter wechseln.** Semantische Suche verzeiht Synonyme, aber nicht immer. Wenn die erste Anfrage nichts findet, formuliere sie anders, statt aufzugeben.

**Verneinungen gezielt prüfen.** Wenn deine Frage ein „nicht", „kein" oder „ohne" enthält, lies die gefundenen Stellen besonders genau. Die Suche hat womöglich das Gegenteil gefunden.

**Fundstellen öffnen.** Was eine Suche oder ein Chat-Assistent mit Dokumentenzugriff findet, ist ein Kandidat und noch kein Beleg (A3, A8).

**Stichwort und Bedeutung kombinieren.** Für genaue Begriffe wie Fehlercodes, Paragrafen oder Produktnummern ist eine klassische Stichwortsuche oft treffsicherer. Für Umschreibungen hilft die semantische Suche. Manche Werkzeuge kombinieren beides.

**Vertrauliches nur in freigegebenen Umgebungen einbetten lassen.** Embeddings können mehr über den Text verraten, als du vielleicht denkst. Es gelten dieselben Regeln wie beim Einfügen in einen Chat (E7).

---

## Häufige Fehlgriffe

- **„Nah heißt gleichbedeutend."** Bei Wortvektoren heißt nah vor allem ähnlich verwendet, und Gegenteile liegen oft dicht beieinander (Abschnitt 3).
- **Eine Achse deuten wollen.** Einzelne Dimensionen haben in der Regel keine benennbare Bedeutung (Abschnitt 1).
- **Satz-Embeddings durch Mittelwerte ersetzen.** Für Suche taugen eigens trainierte Embedding-Modelle deutlich besser (Abschnitt 5).
- **Vektoren verschiedener Modelle mischen.** Jedes Modell hat seine eigene Karte (Abschnitt 6).
- **Dem Treffer glauben, weil er passt.** Die Suche misst Nähe, nicht Wahrheit (Abschnitt 6).
- **Embeddings für anonym halten.** Unter bestimmten Bedingungen lassen sich ursprüngliche Texte oder vertrauliche Angaben daraus zurückgewinnen (Abschnitt 6).

---

## Zum Ausprobieren

1. Nimm das Programm aus Abschnitt 2 und füge zwei Pflanzen hinzu, die du kennst, zum Beispiel Basilikum und Efeu. Schätze ihre Werte für Licht und Wasser und lass die Ähnlichkeit zur Tomate ausrechnen. Passt das Ergebnis zu deiner Erfahrung?
2. Halbiere im selben Programm die Werte der Gurke, also `(0.35, 0.35)`. Auf der Karte rückt sie damit Richtung Mitte, der Abstand zur Tomate wächst. Was passiert trotzdem mit der Kosinus-Ähnlichkeit, und warum? Tipp: Die Kosinus-Ähnlichkeit misst die Richtung. Lass dabei keine Pflanze bei `(0, 0)` stehen, sonst teilt das Programm durch null.
3. Wenn du Python nutzt: Installiere die Bibliothek und das Modell aus der Beispielbox in Abschnitt 3. Miss drei eigene Wortpaare, darunter ein Paar von Gegenteilen. Notiere, welches Ergebnis dich überrascht.
4. Gib einem Chat-Assistenten mit Dokumentenzugriff (E8) ein eigenes Skript und frage nach einem Thema mit einer Umschreibung, die im Text nicht wörtlich vorkommt. Frag dann nach der genauen Fundstelle und prüfe sie im Original.
5. Stelle in derselben Unterhaltung eine Frage mit Verneinung, etwa „Welche Geräte brauchen keine feste IP-Adresse?". Prüfe, ob die gefundenen Stellen wirklich die verneinte Aussage stützen oder das Gegenteil.

Am Ende hast du eine eigene kleine Pflanzenkarte, ein paar echte Messungen und eine Beobachtung, wie gut die Suche in deinem Werkzeug mit Umschreibungen und Verneinungen umgeht.

---

## Fazit

Ein Embedding ist eine Zahlenreihe, die einem Stück Text einen Ort im Raum gibt. Was dort nah beieinander liegt, hängt davon ab, worauf das Modell trainiert wurde. Ähnlichkeit wird häufig über die Richtung gemessen, mit der Kosinus-Ähnlichkeit. Im Sprachmodell beginnt jedes Token als Zeile einer gelernten Tabelle, und für die Suche gibt es eigene Modelle, die ganzen Abschnitten einen Vektor geben. Darauf bauen semantische Suche und RAG auf. Nähe ist aber nicht Bedeutungsgleichheit: Gegenteile und Verneinungen liegen oft dicht beieinander, Vorurteile reisen mit, und Embeddings sind nicht automatisch anonym. Als Nächstes geht es in D3 um Transformer und Attention: wie aus dem Startvektor eines Tokens ein Vektor wird, der seinen Kontext kennt.

```yaml
dokument: ki-d2-embeddings
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-10-14
quellen_fachlich:
  - "Eigene Messung am 2026-10-14 mit spaCy und dem Modell de_core_news_md 3.8.0 (Installation aus den GitHub-Releases von explosion/spacy-models). Meta-Daten des Modells: Vektoren 'Explosion fastText Vectors (cbow, OSCAR Common Crawl + Wikipedia)', Lizenz CC0, Breite 300, 20.000 Vektoren für 500.000 Schlüssel. Kosinus-Ähnlichkeiten: Tomate/Gurke 0,56, Tomate/Rose 0,24, Tomate/Laptop 0,05, Router/Switch 0,61, Hund/Katze 0,68, heiß/kalt 0,69, sicher/unsicher 0,74; Passwort/Kennwort 1,0, weil beide Schlüssel auf dieselbe Vektorzeile zeigen (geprüft über key2row). Satzvektoren als Mittelwert: Gießfrage zu Tomatensatz 0,29, zu Laptopsatz 0,46; Verneinungspaar 0,98"
  - "Pflanzenkarte in Abschnitt 2: ausgedachte Werte, Programm am 2026-10-14 ausgeführt: Tomate/Gurke 0,97, Tomate/Farn -0,3, Tomate/Kaktus 0,28"
  - "Qwen2.5-7B-Instruct, config.json: vocab_size 152064, hidden_size 3584, 28 Schichten, tie_word_embeddings false. https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/raw/main/config.json; Modellkarte: 7,61 Mrd. Parameter, davon 6,53 Mrd. ohne Embedding. https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (Zugriff jeweils 2026-10-14). Eigene Rechnung: 152.064 × 3.584 = 544.997.376 je Tabelle, zwei Tabellen 1.089.994.752, also rund 1,09 Mrd.; die Differenz der gerundeten Modellkartenwerte (7,61 - 6,53 = 1,08 Mrd.) weicht nur durch Rundung ab, im Text deshalb 'rund 7,6 Milliarden' und Hinweis auf die Rundung"
  - "Reimers, Gurevych: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (2019), arXiv:1908.10084. https://arxiv.org/abs/1908.10084 (Zugriff 2026-10-14): Abstract: ähnlichstes Paar unter 10.000 Sätzen mit BERT etwa 65 Stunden, mit SBERT etwa 5 Sekunden; Tabelle 1 (STS, Spearman-Rangkorrelation × 100, Mittel): gemittelte GloVe-Vektoren 61,32, gemittelte BERT-Vektoren 54,81, bestes SBERT-Modell 76,68 (SRoBERTa-NLI-large)"
  - "Weller, Lawrie, Van Durme: NevIR: Negation in Neural Information Retrieval. EACL 2024, https://aclanthology.org/2024.eacl-long.139; arXiv:2305.07614 (Zugriff 2026-10-14): die meisten Retrieval-Modelle, auch führende, berücksichtigen Verneinung nicht und ordnen gleich gut wie oder schlechter als eine Zufallsreihenfolge; Nachtraining auf Verneinungsdaten und größere Modelle helfen, großer Abstand zu Menschen bleibt"
  - "Bolukbasi, Chang, Zou, Saligrama, Kalai: Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings (2016), arXiv:1607.06520. https://arxiv.org/abs/1607.06520 (Zugriff 2026-10-14): mit Google-News-Texten trainierte Wortvektoren zeigen Geschlechterstereotype in beunruhigendem Ausmaß"
  - "Morris, Kuleshov, Shmatikov, Rush: Text Embeddings Reveal (Almost) As Much As Text. EMNLP 2023, https://aclanthology.org/2023.emnlp-main.765; arXiv:2310.06816 (Zugriff 2026-10-14): schrittweises Verfahren stellt 92 % der 32-Token-Eingaben exakt wieder her; in einem getrennten Versuch vollständige Namen aus einem Datensatz klinischer Notizen zurückgewonnen"
  - "Eigene Artikel der Reihe: D1 (Token-IDs, Embedding als Umwandlung, Kontextfenster als Pflanztisch), A9 (offen dokumentiertes 7-Milliarden-Modell), A3 und A8 (Fundstellen prüfen), E7 (Daten-Ampel), E8 (Dokumente); Vorwärtsverweise auf D3, D4, D5, D9, P4, R1"
verifikation_offen:
  - "Leitgedanke 'Ein Wort erkennt man an der Gesellschaft, in der es auftritt' (verteilte Bedeutung, Firth 1957, Harris 1954) ist Lehrbuchwissen (W), keine Primärquelle gelesen; im Text ohne Namen und Jahr formuliert ('Jahrzehnte alt')"
  - "Ursache für das Scheitern des Mittelwerts im konkreten Beispiel nicht gemessen (zum Beispiel ohne Funktionswörter); im Text nur allgemein begründet (keine Gewichtung, nicht für Sätze trainiert), keine Einzelursache behauptet"
  - "Aussage, dass einzelne Dimensionen in der Regel keine benennbare Bedeutung haben, ist Fachwissen (W) ohne Einzelquelle; vorsichtig formuliert"
  - "Kontextabhängige Verschiebung von 'Bank' über die Schichten ist Fachwissen (W) für Transformer, nicht an einem Modell gemessen; Details in D3"
  - "Vergleichbarkeit von Vektoren verschiedener Modelle: Fachwissen (W); Verfahren zur nachträglichen Ausrichtung von Vektorräumen im Text erwähnt, keine Einzelquelle gelesen"
  - "Hinweis, dass Stichwortsuche bei Fehlercodes oft treffsicherer ist und viele Werkzeuge beides bieten, ist Praxiswissen ohne Einzelquelle; einzelne Produkte nicht geprüft"
  - "SBERT-Vergleich bezieht sich auf englische STS-Daten von 2019; heutige Modelle und Deutsch nicht geprüft. 65 Stunden ist die Schätzung der Autoren"
  - "A9-Pflegehinweis: Die Modellkarte von Qwen2.5-7B-Instruct nennt eine volle Kontextlänge von 131.072 Tokens (mit Zusatzverfahren); A9 rechnet mit max_position_embeddings 32.768 aus der config.json und schreibt 'bei voller Länge von rund 32.000 Token'. Kann in A9 präzisiert werden, Entscheidung bei David"
review_historie:
  - runde: 0
    datum: 2026-10-14
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Ähnlichkeiten mit echten deutschen Wortvektoren gemessen, Artefakt Passwort/Kennwort entdeckt und in die Beispielbox aufgenommen statt als Beleg verwendet. Studien zu Satz-Embeddings, Verneinung, Vorurteilen und Rückgewinnung an der Quelle gelesen. Modellzahlen aus config.json und Modellkarte gegengerechnet."
  - runde: 1
    datum: 2026-10-14
    ergebnis: "Eigene Reviews (Fach und Stil): Verneinungs-Gegensätze und man-Formulierungen aufgelöst, zwei lange Sätze geteilt, Rückgewinnungsstudie auf das untersuchte Modell begrenzt, SBERT-Zahlen als bestes Modell und Schätzung der Autoren präzisiert, Werkzeug-Aussage abgeschwächt, Installationsbefehl nicht ungeprüft genannt. Alle Programme aus dem Artikel erneut ausgeführt, Übung 2 nachgerechnet (verdoppelte Gurke bleibt bei 0,97). Einstieg und RAG-Satz entschärft: nicht jeder Chat-Assistent sucht per Embedding, kleinere Dokumente landen oft komplett im Kontext."
  - runde: 2
    datum: 2026-10-14
    ergebnis: "Drei externe Reviews, Behauptungen an Datei und Quellen bestätigt. Übernommen: Einstieg korrigiert (beide Sätze enthalten 'nicht'); Kosinus als Richtungsvergleich statt Kartenabstand, 0 und negative Werte nicht als 'nichts gemeinsam' bzw. Gegenteil; SBERT-Zeitvergleich als ähnlichstes Paar in einer Sammlung von 10.000 Sätzen, Werte als Übereinstimmung der Rangfolgen erklärt; Embedding-Definition und Nähe-Regel an Trainingsziel bzw. Wortvektoren gebunden; Rückgewinnungsstudie an Versuchsaufbau gebunden, Fehlgriff und Fazit angeglichen; Vektorräume 'normalerweise nicht direkt vergleichbar'; Parameterzahl einheitlich 1,09 Mrd. aus den Tabellen; Ausgangstabelle als Werte vor den Wahrscheinlichkeiten; Mittelwert ohne ungeprüfte Einzelursache; Übung 2 mit Halbierung innerhalb der Skala und Hinweis auf Nullvektor. Nicht übernommen: Quellenrubrik mit Links und Quellenverweise im Fließtext (Entscheidung zur Reihe vom 01.10.2026, wie bei D1)."
  - runde: 3
    datum: 2026-10-14
    ergebnis: "Drei Re-Reviews. Übernommen: RAG nicht an Embeddings gebunden (Abruf auch per Stichwort oder kombiniert); Rückgewinnungsquote und klinische Namen als getrennte Befunde; Datenschutzregel in Abschnitt 6 an Abschnitt 7 angeglichen (freigegebene Umgebungen); Parameterzahl mit Rundungshinweis, YAML angeglichen; GloVe als Vergleichswert benannt; Skala der Pflanzenkarte je Koordinate erklärt; Mittelwert-Erklärung präzisiert; Pointe von Übung 2 geschärft; zwei Stilglättungen. Kein Punkt abgelehnt."
  - runde: 4
    datum: 2026-10-14
    ergebnis: "Freigabe durch David am 2026-10-14 nach Runde 3. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen, darunter der A9-Pflegehinweis zur Kontextlänge."
```