# KI-D4 · Wahrscheinlichkeit statt Wissen: Wie aus Zahlen Text wird

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D4 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du stellst einem Chat-Assistenten eine Frage und bekommst eine gute Antwort. Aus Neugier klickst du auf „Neu generieren". Die zweite Antwort ist anders formuliert, nennt andere Beispiele und kommt an einer Stelle sogar zu einem anderen Ergebnis. Dasselbe Modell, dieselbe Frage, zwei Antworten. Wie kann das sein, wenn doch alles nur Rechnung ist?

Die Auflösung liegt am Ende der Schichten aus D3. Dort steht noch keine fertige Antwort, nur ein Vektor. Daraus berechnet das Modell zunächst Rohwerte und über die Softmax eine Wahrscheinlichkeit für jedes mögliche nächste Token. Welches Token tatsächlich geschrieben wird, entscheidet ein eigener Schritt, und der darf würfeln. Am Ende dieses Artikels kannst du erklären, wie aus den Rechenergebnissen eine Wahrscheinlichkeitsverteilung wird und wie daraus Token für Token Text entsteht. Du weißt, was Temperatur, Top-k und Top-p bewirken, warum dieselbe Frage verschiedene Antworten bekommt und warum eine hohe Wahrscheinlichkeit noch nichts über Wahrheit sagt.

Vorausgesetzt werden D1 bis D3, vor allem die Softmax aus D3. Python brauchst du nur, wenn du das Beispiel selbst laufen lassen willst.

---

## 1. Am Ende steht eine Liste

Nach der letzten Schicht hat jedes Token einen fertig angereicherten Vektor. Für das Schreiben zählt der Vektor an der letzten Stelle, denn dort soll es weitergehen. Diesen Vektor schickt das Modell durch die Ausgangstabelle aus D2. Heraus kommt für jedes Token des Vokabulars ein **Rohwert**, im Fachjargon **Logit** genannt. Beim offen dokumentierten Modell aus A9 sind das 152.064 Rohwerte, einer pro Token im Vokabular.

Rohwerte sind beliebige Zahlen, auch negative. Daraus macht wieder die **Softmax** aus D3 Anteile, die zusammen genau 1 ergeben. Das Ergebnis ist eine **Wahrscheinlichkeitsverteilung**: eine Liste, die jedem möglichen nächsten Token eine Wahrscheinlichkeit zuordnet. Nach „Die Tomaten brauchen mehr" könnte „Wasser" weit oben stehen, „Sonne" etwas darunter, und „Strom" ganz unten.

Wichtig ist, was hier fehlt. Das Modell schlägt nirgends nach, ob Tomaten wirklich Wasser brauchen. Die Verteilung beschreibt, welche Fortsetzungen das Modell angesichts des bisherigen Textes und der beim Training gelernten Muster für wahrscheinlich hält. Sie wird für jedes neue Token frisch berechnet. Das ist der Satz aus E1, „es rechnet, was wahrscheinlich als Nächstes kommt", jetzt mit Mechanik dahinter.

---

## 2. Die Tombola beim Sommerfest

Beim Sommerfest der Gärtnerei gibt es eine Tombola. In der Lostrommel liegen Lose für verschiedene Preise, aber nicht gleich viele: Für die Tomatenpflanze liegen 53 Lose drin, für die Sonnenblume 24, für den Dünger 12 und so weiter. Wer zieht, bekommt meistens etwas Häufiges, aber nicht immer.

So wählt ein Sprachmodell sein nächstes Token, wenn es **Sampling** nutzt, also zieht statt immer den Favoriten zu nehmen. Jedes Token bekommt so viele Lose, wie seine Wahrscheinlichkeit vorgibt, dann wird gezogen. Ein kleines Python-Programm spielt das für „Die Tomaten brauchen mehr ..." durch. Die Rohwerte für die sieben Kandidaten sind ausgedacht, ein echtes Modell hätte über hunderttausend. Die Wörter stehen hier stellvertretend für Tokens, echte Tokens können auch Wortteile oder Satzzeichen sein (D1):

```python
import random
from math import exp

# "Die Tomaten brauchen mehr ..." Rohwerte für sieben Kandidaten, ausgedacht
rohwerte = {"Wasser": 4.0, "Sonne": 3.2, "Dünger": 2.5, "Platz": 1.8,
            "Zeit": 1.5, "Liebe": 0.5, "Strom": -1.0}

def softmax(werte, temperatur):
    skaliert = {t: w / temperatur for t, w in werte.items()}
    summe = sum(exp(w) for w in skaliert.values())
    return {t: exp(w) / summe for t, w in skaliert.items()}

for temperatur in (0.5, 1.0, 1.5):
    p = softmax(rohwerte, temperatur)
    print(f"T={temperatur}:", {t: round(w, 2) for t, w in p.items()})

random.seed(4)
p = softmax(rohwerte, 1.0)
ziehungen = random.choices(list(p), weights=list(p.values()), k=10)
print("10 Ziehungen bei T=1.0:", ziehungen)
```

```text
T=0.5: {'Wasser': 0.79, 'Sonne': 0.16, 'Dünger': 0.04, 'Platz': 0.01, 'Zeit': 0.01, 'Liebe': 0.0, 'Strom': 0.0}
T=1.0: {'Wasser': 0.53, 'Sonne': 0.24, 'Dünger': 0.12, 'Platz': 0.06, 'Zeit': 0.04, 'Liebe': 0.02, 'Strom': 0.0}
T=1.5: {'Wasser': 0.4, 'Sonne': 0.23, 'Dünger': 0.15, 'Platz': 0.09, 'Zeit': 0.08, 'Liebe': 0.04, 'Strom': 0.01}
10 Ziehungen bei T=1.0: ['Wasser', 'Wasser', 'Wasser', 'Wasser', 'Wasser', 'Wasser', 'Platz', 'Dünger', 'Dünger', 'Wasser']
```

Die Ausgabe ist auf zwei Stellen gerundet. Deshalb ergeben die Werte einer Zeile nicht immer genau 1, und „Strom" steht bei T=1.0 auf 0.0, obwohl es mit rund 0,004 eine kleine Chance hat. Schau dir die zweite Zeile und die Ziehungen an. „Wasser" kommt in sieben von zehn Zügen, „Dünger" zweimal, „Platz" einmal. „Sonne" fehlt ganz, obwohl sie fast ein Viertel der Lose hat. So ist Zufall in kleinen Stichproben. Mit `random.seed(4)` liefert das Programm jedes Mal dieselben Züge, damit du das Ergebnis nachprüfen kannst. Ohne festen Startwert können die Ziehungen bei jedem Lauf anders ausfallen.

Wo das Bild nicht passt: Die Tombola zieht einmal am Abend. Ein Sprachmodell zieht für jedes einzelne Token, bei einer längeren Antwort also Hunderte Male hintereinander. Und die Lose verteilt das Modell nach dem, was es beim Training gelernt hat. Der Wert der Preise spielt dabei keine Rolle.

---

## 3. Temperatur: wie gleichmäßig die Lose verteilt sind

Die drei oberen Zeilen der Ausgabe zeigen die Wirkung derselben Rohwerte bei unterschiedlicher **Temperatur**. Technisch werden die Rohwerte vor der Softmax durch die Temperatur geteilt. Die Wirkung siehst du an „Wasser":

- Bei **0,5** bekommt „Wasser" 79 Prozent der Lose. Das Modell wird vorhersehbarer und hält sich an den Favoriten.
- Bei **1,0** bleibt die Verteilung, wie das Modell sie berechnet hat.
- Bei **1,5** sinkt „Wasser" auf 40 Prozent, und auch „Liebe" und „Strom" bekommen ein paar Lose mehr. Das Modell wird abwechslungsreicher, aber auch eher bereit, eine schwache Fortsetzung zu wählen.

Im Tombola-Bild bleiben die Preise dieselben. Die Temperatur verändert nur, wie ungleich die Lose verteilt sind. Niedrig heißt: fast alle Lose für den Favoriten. Hoch heißt: die Lose gleichmäßiger auf alle Preise verteilen.

Der Grenzfall heißt **Greedy Decoding**, auf Deutsch etwa „gieriges Auswählen": Es wird gar nicht gezogen. Das Modell nimmt immer das wahrscheinlichste Token. Wenn eine Schnittstelle eine Temperatur von 0 erlaubt, ist meist dieses Verhalten gemeint, denn durch 0 teilen lässt sich nicht.

Nicht bei jedem Modell lässt sich die Temperatur einstellen. Wo es geht, empfiehlt eine Anbieterdokumentation als Faustregel einen Wert nahe 0 für analytische Aufgaben und Auswahlfragen. Für kreative Aufgaben rät sie zu einem Wert nahe dem Höchstwert (Beispielbox am Ende von Abschnitt 6).

---

## 4. Die Lostrommel verkleinern: Top-k und Top-p

Selbst bei normaler Temperatur hat jedes Token im Vokabular ein paar Lose, auch völlig unpassende. Bei einem echten Modell mit über hunderttausend Tokens summieren sich diese winzigen Anteile. Wer oft genug zieht, kann auch eines davon erwischen, und die Antwort entgleist an dieser Stelle.

Zwei Verfahren nehmen deshalb die unwahrscheinlichsten Lose vor dem Ziehen aus der Trommel:

- **Top-k** behält nur die k wahrscheinlichsten Tokens. Mit k = 3 blieben im Beispiel „Wasser", „Sonne" und „Dünger".
- **Top-p**, auch **Nucleus Sampling** genannt, behält so viele der wahrscheinlichsten Tokens, bis ihre Wahrscheinlichkeiten zusammen mindestens p ergeben. Mit p = 0,9 und den Werten bei T = 1,0 bleiben „Wasser" (0,53), „Sonne" (0,24), „Dünger" (0,12) und „Platz" (0,06). Mit den ungerundeten Wahrscheinlichkeiten kommen die ersten drei zusammen auf rund 0,879. Erst mit „Platz" steigt die Summe auf rund 0,937 und überschreitet damit 0,9. Wer stattdessen die gerundeten Anzeigen addiert, landet bei 0,89 und 0,95, und das zeigt, warum du bei Schwellenwerten nicht mit gerundeten Zwischenwerten weiterrechnen solltest.

In der Erklärung dieses Artikels kommt zuerst die Temperatur, dann das Aussortieren mit Top-k oder Top-p. Die Wahrscheinlichkeiten der verbliebenen Tokens werden anschließend so umgerechnet, dass sie zusammen 1 ergeben, und erst dann wird gezogen. Wie ein Programm das intern genau ordnet, kann sich unterscheiden. Manche Werkzeuge kombinieren beide Verfahren.

Der Vorteil von Top-p: Die Zahl der behaltenen Tokens passt sich an. Ist sich das Modell sicher, bleiben wenige übrig, ist es unsicher, bleiben mehr. Die Arbeit, die das Verfahren 2019 vorstellte und 2020 auf einer großen Fachkonferenz veröffentlichte, begründete es auch mit dem umgekehrten Problem. Wer immer nur die wahrscheinlichste Fortsetzung nimmt, bekommt laut den Autoren oft fade und seltsam repetitive Texte. Top-p sollte die Vielfalt behalten und trotzdem den unzuverlässigen Rest abschneiden.

---

## 5. Token für Token, ohne Radiergummi

Ist ein Token gezogen, wird es an den Text angehängt. Dann beginnt alles von vorn: Das Modell rechnet mit dem verlängerten Text die nächste Verteilung aus, zieht wieder, hängt wieder an. Diese Schleife heißt **autoregressiv**, weil jedes neue Token auf den eigenen vorherigen aufbaut. Aus D3 weißt du, warum das schnell geht: Schlüssel und Werte der bisherigen Tokens liegen im Zwischenspeicher. Und aus D1 weißt du, dass jedes erzeugte Token Platz im Kontextfenster belegt.

Die Schleife endet, wenn das Modell ein besonderes **Stopp-Token** zieht, das „hier ist Schluss" bedeutet, oder wenn eine festgelegte Höchstlänge erreicht ist.

Zwei Folgen dieser Schleife sind für dich wichtig. Erstens gibt es keinen Radiergummi. Ein gezogenes Token bleibt stehen, und alles Weitere baut darauf auf. Hat das Modell früh „Nein" gezogen, gehört dieses „Nein" zum Kontext und beeinflusst die folgenden Sätze, auch wenn „Ja" fast genauso wahrscheinlich war. Das Modell kann sich später zwar ausdrücklich korrigieren, das bereits geschriebene Token aber nicht zurücknehmen. Zweitens können frühe Unterschiede besonders weitreichende Folgen haben. Ein anderer Zug im dritten Token kann die ganze Antwort in eine andere Richtung schicken. Das erklärt, warum zwei Antworten auf dieselbe Frage manchmal zu verschiedenen Ergebnissen kommen und nicht bloß anders formuliert sind.

Wo das Bild aus Abschnitt 2 nicht passt: In der gedachten Tombola bleiben die Gewinnchancen nach jeder Ziehung gleich. Beim Sprachmodell verändert jedes gezogene Token die nächste Verteilung, weil es jetzt Teil des Textes ist.

---

## 6. Warum dieselbe Frage verschiedene Antworten bekommt

Der wichtigste Grund ist das Ziehen. Viele Chat-Oberflächen und Schnittstellen nutzen Sampling, damit Antworten natürlicher klingen und sich nicht stur wiederholen. „Neu generieren" heißt dann: die ganze Tombola noch einmal. Das gilt, solange Modell, Kontext und Einstellungen gleich bleiben. In einer Chat-Oberfläche können sich auch andere Dinge ändern, etwa Suchergebnisse, Anweisungen im Hintergrund oder die Modellversion.

Aber auch ohne Ziehen sind Antworten nicht immer gleich. Eine Anbieterdokumentation weist ausdrücklich darauf hin, dass die Ergebnisse selbst bei einer Temperatur von 0 nicht vollständig deterministisch sind. Ein Forschungsbericht von 2025 ging dem nach. Rechenzentren verarbeiten oft mehrere Anfragen gemeinsam, und wie viele das gerade sind, hängt unter anderem von der Auslastung ab. Je nach Gruppengröße teilen manche Programmteile ihre Rechnungen anders auf. Dadurch entstehen winzige Unterschiede in den Zahlen. Liegen zwei mögliche nächste Tokens sehr nah beieinander, kann schon ein solcher Unterschied die Auswahl verändern. In einem Versuch mit einem offenen Modell lieferten 1.000 Durchläufe bei Temperatur 0 so 80 verschiedene Antworten. Mit eigens angepassten Programmteilen waren alle 1.000 gleich. In einem getrennten Geschwindigkeitstest mit einem anderen Modell war die angepasste Variante allerdings langsamer. Der Bericht stammt von einem KI-Unternehmen, das dieses Problem selbst lösen wollte.

Für dich heißt das: Erwarte nicht, eine Antwort exakt reproduzieren zu können. Was du später noch brauchst, speicherst du (A8).

> **Beispielbox, Stand 14.10.2026: Temperatur und Co. bei einem Anbieter.** Die Schnittstelle von Anthropic beschreibt die Temperatur mit einem Bereich von 0 bis 1 und dem Standardwert 1. Sie empfiehlt Werte nahe 0 für analytische und Auswahlaufgaben und nahe 1 für kreative Aufgaben, und sie weist darauf hin, dass auch bei 0 die Ergebnisse nicht vollständig deterministisch sind. Gleichzeitig sind Temperatur, top_p und top_k dort als veraltet markiert. Modelle, die nach Claude Opus 4.6 erschienen sind, unterstützen diese Einstellungen nicht mehr. Zur Rückwärtskompatibilität nimmt die Schnittstelle für die Temperatur noch den Wert 1 und für top_p Werte ab 0,99 an. Andere Werte sowie top_k weist sie zurück. Andere Anbieter haben andere Bereiche und Regeln, und in vielen Chat-Oberflächen gibt es den Regler gar nicht. Schau in die Dokumentation deines Werkzeugs.

---

## 7. Wahrscheinlich ist nicht wahr

Zurück zur Tombola. Die Lose verteilt das Modell anhand der Muster, die es beim Training gelernt hat, und des bisherigen Textes. Eine Formulierung, die gut zu diesen Mustern passt, kann viele Lose bekommen. Ob die Aussage dahinter stimmt, ist eine andere Frage. Auch eine falsche Behauptung kann für das Modell wie eine plausible Fortsetzung aussehen. Und wenn es zu einer Frage nur wenige passende Anhaltspunkte gelernt hat, verteilt es seine Lose trotzdem, nur eben auf plausibel klingende Fortsetzungen. Heraus kommt flüssiger Text, der so klingt, als wüsste das Modell Bescheid (E1, E6). Warum das zu Halluzinationen führt und was dagegen hilft, ist Thema von D8.

Die Variation aus Abschnitt 6 lässt sich aber auch nutzen. Eine 2023 veröffentlichte Methode stellt einem Modell dieselbe Frage mehrmals und vergleicht die Antworten. Die Idee der Autoren: Kennt das Modell einen Sachverhalt, sind die gezogenen Antworten ähnlich und widerspruchsfrei. Bei erfundenen Fakten gehen sie eher auseinander und widersprechen sich. Das funktioniert ohne Zugriff auf das Innere des Modells, nur mit den Antworten.

Die Grenze: Übereinstimmung ist ein Hinweis, kein Beweis. Ein Modell kann denselben Fehler auch zehnmal hintereinander machen, wenn er in seinen Losen weit oben liegt. Bei Fakten, die zählen, bleibt die Prüfung an der Quelle (A3, A8).

---

## 8. Was du daraus machst

**„Neu generieren" bewusst einsetzen.** Für Ideen, Formulierungen und Beispiele ist Variation ein Gewinn. Lass dir mehrere Fassungen geben und nimm die beste.

**Abweichungen als Warnsignal lesen.** Wenn zwei Antworten auf dieselbe Faktenfrage verschiedene Zahlen, Namen oder Ergebnisse nennen, prüfe beide an der Quelle. Wenn sie übereinstimmen, prüfst du trotzdem, nur mit etwas mehr Ruhe.

**Temperatur passend wählen, wo es sie gibt.** Für Zusammenfassungen, Datenextraktion oder Klassifikation eher niedrig, für Brainstorming eher höher. Bei manchen neueren Modellen lässt sich der Wert nicht mehr ändern (Beispielbox in Abschnitt 6).

**Testfälle mehrmals laufen lassen.** Eine Vorlage, die einmal gut funktioniert hat, kann beim nächsten Lauf anders antworten. Lass die Testfälle aus A7 deshalb mehr als einmal laufen, bevor du dich auf eine Vorlage verlässt.

**Ergebnisse speichern statt neu erzeugen.** Was du dokumentieren oder später belegen musst, hältst du fest. Dieselbe Antwort bekommst du womöglich nie wieder.

---

## Häufige Fehlgriffe

- **„Das Modell kennt die Antwort und schreibt sie hin."** Es berechnet eine Verteilung über mögliche nächste Tokens und zieht daraus oder nimmt den Favoriten (Abschnitt 1 bis 3).
- **„Hohe Wahrscheinlichkeit heißt richtig."** Wahrscheinlich heißt: passt zu den Mustern aus dem Training (Abschnitt 7).
- **„Temperatur 0 garantiert immer dieselbe Antwort."** Auch ohne Ziehen können Antworten variieren (Abschnitt 6).
- **„Hohe Temperatur macht das Modell kreativer und klüger."** Sie verteilt die Lose gleichmäßiger, auch auf schwache Fortsetzungen (Abschnitt 3).
- **„Wenn die Antworten übereinstimmen, stimmt die Aussage."** Übereinstimmung ist ein Hinweis, kein Beweis (Abschnitt 7).
- **„Die Antwort steht fertig im Modell und wird nur abgeschrieben."** Sie entsteht Token für Token, und jedes gezogene Token prägt den Rest (Abschnitt 5).

---

## Zum Ausprobieren

1. Setze im Programm aus Abschnitt 2 die Temperatur auf 0.1 und auf 3.0. Notiere, wie viel Prozent „Wasser" und „Strom" jeweils bekommen. Was würde eine Temperatur von 0 bedeuten, und warum rechnet das Programm sie nicht aus?
2. Ändere den Startwert in `random.seed(4)` auf drei andere Zahlen und notiere jeweils, wie oft „Wasser" unter den zehn Ziehungen ist. Erhöhe danach `k=10` auf `k=1000`. Wie nah kommt der Anteil von „Wasser" jetzt an die 0,53?
3. Bestimme mit der Ausgabe für T = 1,5, welche Tokens bei Top-p mit p = 0,9 in der Trommel bleiben. Addiere dazu die Wahrscheinlichkeiten von oben nach unten, bis du 0,9 erreichst.
4. Stelle einem Chat-Assistenten in drei neuen Gesprächen dieselbe Faktenfrage aus deinem Fachgebiet, etwa nach einer Portnummer oder einem Fachbegriff. Vergleiche die Antworten. Prüfe die Aussage danach an einer Quelle, auch wenn alle drei übereinstimmen.
5. Bitte in drei neuen Gesprächen um denselben kreativen Text, zum Beispiel drei Ideen für den Namen eines Gärtnerei-Newsletters. Notiere, wie stark die Antworten voneinander abweichen, und vergleiche mit Übung 4.

Am Ende hast du ein Gefühl dafür, wie Temperatur und Zufall eine Verteilung verändern, und eine eigene Beobachtung, wie stark dein Werkzeug bei Fakten und bei kreativen Aufgaben schwankt.

---

## Fazit

Am Ende aller Schichten steht für jedes mögliche nächste Token ein Rohwert, und die Softmax macht daraus eine Wahrscheinlichkeitsverteilung. Daraus wird gezogen oder der Favorit genommen. Die Temperatur verändert, wie gleichmäßig die Lose verteilt sind. Top-k und Top-p begrenzen, welche Tokens für die nächste Ziehung überhaupt infrage kommen. Das gezogene Token wird angehängt, und die Schleife beginnt von vorn, ohne Radiergummi. Deshalb fallen Antworten auf dieselbe Frage unterschiedlich aus, und selbst bei Temperatur 0 ist das nicht ganz ausgeschlossen. Eine hohe Wahrscheinlichkeit sagt, was zu den gelernten Mustern passt, nicht, was wahr ist. Als Nächstes geht es in D5 darum, woher diese Muster kommen: wie ein Modell in drei Stufen trainiert wird.

```yaml
dokument: ki-d4-wahrscheinlichkeit-statt-wissen
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-10-14
quellen_fachlich:
  - "Rechenbeispiel Abschnitt 2 am 2026-10-14 mit Python ausgeführt (ausgedachte Rohwerte, Softmax mit Temperatur, random.seed(4), random.choices): T=0,5 Wasser 0,79; T=1,0 Wasser 0,53, Sonne 0,24, Dünger 0,12, Platz 0,06, Zeit 0,04, Liebe 0,02, Strom 0,00; T=1,5 Wasser 0,40; zehn Ziehungen 7x Wasser, 2x Dünger, 1x Platz. Kumulierte Werte bei T=1,0: 0,526, 0,762, 0,879, 0,937 (Top-p 0,9 behält vier Tokens)"
  - "Holtzman, Buys, Du, Forbes, Choi: The Curious Case of Neural Text Degeneration. ICLR 2020, https://iclr.cc/virtual/2020/poster/1428; arXiv:1904.09751 (Zugriff 2026-10-14): Wahrscheinlichkeitsmaximierung als Dekodierziel führt zu fadem, seltsam repetitivem Text; Dekodierstrategie verändert Textqualität stark; Nucleus Sampling zieht aus dem dynamischen Kern der Verteilung und schneidet den unzuverlässigen Rest ab"
  - "Anthropic API-Referenz, Create a Message. https://platform.claude.com/docs/en/api/messages/create (Zugriff 2026-10-14): temperature 0,0 bis 1,0, Standard 1,0, nahe 0 für analytische und Auswahlaufgaben, nahe 1 für kreative; auch bei 0,0 nicht vollständig deterministisch; temperature, top_k und top_p als veraltet markiert, Modelle nach Claude Opus 4.6 akzeptieren temperature nur 1,0, top_p nur ab 0,99 und top_k gar nicht (Fehler 400); top_k entfernt den langen Rest mit geringer Wahrscheinlichkeit; top_p beschreibt Nucleus Sampling über die kumulierte Verteilung"
  - "He u. a. (Thinking Machines Lab): Defeating Nondeterminism in LLM Inference (2025-09-10). https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ (Zugriff 2026-10-14): Hauptursache ist fehlende Batch-Invarianz, die Last und damit die Batchgröße schwankt; Versuch mit einem offenen Modell (Qwen3-235B-A22B-Instruct-2507) bei Temperatur 0: 1.000 Durchläufe, 80 verschiedene Ausgaben, erste Abweichung beim 103. Token; mit batch-invarianten Kernels alle identisch; getrennter Geschwindigkeitstest mit Qwen3-8B: 26 s Standard, 55 s unoptimiert deterministisch, 42 s mit verbessertem Attention-Kernel"
  - "Manakul, Liusie, Gales: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. EMNLP 2023, S. 9004-9017. https://aclanthology.org/2023.emnlp-main.557/ (Zugriff 2026-10-14): Kennt ein Modell ein Konzept, sind gezogene Antworten ähnlich und konsistent; bei halluzinierten Fakten gehen sie auseinander und widersprechen sich; funktioniert ohne Zugriff auf das Modellinnere"
  - "Qwen2.5-7B-Instruct, config.json: vocab_size 152064 (bereits in D2 geprüft)"
  - "Eigene Artikel der Reihe: E1 (rechnet, was wahrscheinlich als Nächstes kommt), E6 (Grenzen), D1 (Ausgabe belegt Kontextfenster), D2 (Ausgangstabelle), D3 (Softmax, Zwischenspeicher, Maske), A3 und A8 (Prüfen, Protokoll), A7 (Testfälle); Vorwärtsverweise auf D5, D8"
verifikation_offen:
  - "Begriff 'Rohwert' als Eindeutschung von Logit eigene Wortwahl; Temperatur als Teilung der Rohwerte vor der Softmax ist Lehrbuchwissen (W) und im Programm umgesetzt"
  - "'Temperatur 0 heißt in der Praxis meist Greedy' ist eine verbreitete Umsetzung (W), nicht für alle Anbieter geprüft; im Text mit 'meist' formuliert"
  - "'Viele Chat-Oberflächen und Schnittstellen nutzen Sampling' (im Text als Beobachtung gekennzeichnet) und 'in vielen Chat-Oberflächen gibt es den Regler nicht' sind Praxisbeobachtungen ohne Zählung; einzelne Produkte nicht geprüft"
  - "Stopp-Token und Höchstlänge als Ende der Schleife: Lehrbuchwissen (W)"
  - "Aussagen in Abschnitt 7 (passende Muster statt bloßer Häufigkeit, falsche Behauptungen können plausibel wirken, Verteilung auch bei dünner Lage) sind vereinfachte Erklärungen (W); Vertiefung in D8"
  - "Renormierung nach Top-k/Top-p und Reihenfolge Temperatur vor Aussortieren sind Lehrbuchwissen (W) und im Text als Lehrschema gekennzeichnet; die Anthropic-Dokumentation beschreibt top_p als Schnitt der kumulierten Verteilung. Strahlsuche nach Runde 3 wieder aus dem Text genommen"
  - "Pflegehinweis: Beispielbox in Abschnitt 6 ist stark anbieter- und versionsabhängig (Abkündigung von temperature, top_p, top_k ab Modellen nach Claude Opus 4.6). Vor jeder Veröffentlichung oder Überarbeitung erneut gegen die API-Referenz prüfen"
  - "Thinking-Machines-Bericht: Unternehmen mit eigenem Interesse an der Lösung; Ergebnis an einem Modell und einem Programm gemessen, nicht auf alle Anbieter übertragbar; im Text als Versuch mit einem offenen Modell formuliert"
  - "Holtzman et al.: Abstract nennt fade und repetitive Texte bei Wahrscheinlichkeitsmaximierung; Strahlsuche (Beam Search) im Text nicht erwähnt"
review_historie:
  - runde: 0
    datum: 2026-10-14
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Anbieterdokumentation, Nucleus-Sampling-Arbeit, SelfCheckGPT und Bericht zur Nichtdeterminiertheit an der Quelle gelesen. Rechenbeispiel ausgeführt. Löst die Vorwärtsverweise aus D2 (Ausgangstabelle, Wahrscheinlichkeiten) und D3 (Fazit) ein."
  - runde: 1
    datum: 2026-10-14
    ergebnis: "Eigene Reviews (Fach und Stil): fünf Verneinungs-Gegensätze aufgelöst, ein langer Satz geteilt, Fehlgriff zur fertigen Antwort so formuliert, dass er keine Aussage über interne Planung trifft. Programm erneut ausgeführt, Übungen nachgerechnet (Übung 1: T=0,1 Wasser 1,00, T=3,0 Wasser 0,26 und Strom 0,05; Übung 2: Startwerte 1, 2, 3 ergeben 6, 3, 6 mal Wasser, bei 1.000 Zügen 0,507; Übung 3: bei T=1,5 behält Top-p 0,9 fünf Tokens bis einschließlich Zeit)."
  - runde: 2
    datum: 2026-10-14
    ergebnis: "Drei externe Reviews, Behauptungen an Datei und Quellen bestätigt. Übernommen: Abschnitt 7 ohne Gleichsetzung von Trainingshäufigkeit und Wahrscheinlichkeit; Renormierung nach Top-k/Top-p und Reihenfolge nach der Temperatur; Verteilung an den Kontext gebunden; Einleitung mit Zwischenschritt Vektor; Rundungshinweis zur Ausgabe (Strom bei T=1 rund 0,004); Top-p-Summe ausgeschrieben; Strahlsuche erwähnt; Kombination von Top-k und Top-p; Nichtdeterminismus präziser (Aufteilung der Rechnungen, knappe Kandidaten); gleiche Frage nicht gleich gleicher Kontext; Tokens nicht immer ganze Wörter; Sampling-Aussage als Beobachtung; Box-Formulierung zu top_k; Pflegehinweis zur Box. Nicht übernommen: Änderung des Datums (Reviewer ging von einem anderen Zeitstand aus, Stand 14.10.2026 ist korrekt), Quellenliste mit Links (Entscheidung zur Reihe)."
  - runde: 3
    datum: 2026-10-14
    ergebnis: "Drei Re-Reviews, alle Punkte an Datei und Quellen geprüft. Übernommen: Beispielbox trennt Akzeptanz zur Rückwärtskompatibilität von Unterstützung; 'ohne Radiergummi' ohne Zwangsfolge, frühe Unterschiede als Möglichkeit; Top-p mit ungerundeten Summen (0,879 und 0,937); Reihenfolge Temperatur und Aussortieren als Lehrschema; getrennte Versuche im Thinking-Machines-Bericht (Geschwindigkeit mit anderem Modell); Einleitung mit Rohwerten und Softmax; Temperatur-Empfehlung auf einstellbare Modelle begrenzt; Fazit trennt Temperatur und Top-k/Top-p; Tombola-Regel, Startwert-Satz und Fehlgriff präzisiert; Strahlsuche wieder gestrichen (für das Lernziel nicht nötig). Nicht übernommen: neuer Titel ('Wahrscheinlich ist nicht wahr'), weil der Titel aus der Themenübersicht der Reihe stammt; Entscheidung bei David."
  - runde: 4
    datum: 2026-10-14
    ergebnis: "Freigabe durch David am 2026-10-14 nach Runde 3, Titel bleibt wie in der Themenübersicht. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen, insbesondere der Pflegehinweis zur Beispielbox."
```