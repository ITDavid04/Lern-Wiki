# KI-D8 · Warum Halluzinationen entstehen: Flüssig ist nicht wahr

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D8 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Eine Kundin fragt im Verkaufsraum nach der Blütezeit einer seltenen Pflanzensorte. Die Aushilfe hat den Namen noch nie gehört. Sie antwortet trotzdem sofort, freundlich und ohne Zögern: „Im Juli." Das klingt genauso sicher wie ihre Antwort zur Rose, und genau das ist das Problem.

Aus E6 weißt du, was Halluzinationen sind und wie du Antworten prüfst. Hier geht es um das Warum. Am Ende dieses Artikels kannst du erklären, warum ein Sprachmodell gerade bei seltenen Fakten erfindet, warum das Training Raten belohnen kann und warum ein Fehler sich beim Schreiben selbst verstärkt. Du kannst Fehler gegenüber der Welt von Fehlern gegenüber deinem Material unterscheiden. Und du weißt, was Retrieval und Quellenangaben verbessern und wo sie aufhören zu helfen.

Vorausgesetzt werden D1 bis D7, vor allem die Tombola aus D4, das Nachtraining aus D5 und die Gedankengänge aus D7. E6 ist die praktische Seite dieses Artikels.

---

## 1. Zwei Blickrichtungen beim Prüfen

In der Gärtnerei kann eine Auskunft auf zwei Arten falsch sein. Die Aushilfe nennt aus dem Kopf eine Blütezeit, die nicht stimmt. Oder sie hat das Pflanzenetikett in der Hand und liest es falsch vor. Beim ersten Fehler fehlte das Wissen. Beim zweiten lag die richtige Angabe direkt vor ihr.

Eine viel zitierte Übersichtsarbeit unterscheidet bei Sprachmodellen zwei Gruppen:

- **Faktenfehler** (englisch factuality hallucination): Die Antwort widerspricht überprüfbaren Tatsachen der Welt. Dazu zählen falsch wiedergegebene echte Fakten, etwa eine Erfindung, die der falschen Person zugeschrieben wird, und frei erfundene Ereignisse oder Quellen.
- **Treue- und Konsistenzfehler** (englisch faithfulness hallucination): Die Antwort hält sich nicht an ihre Vorgaben. Sie weicht von deinem Material ab, ignoriert eine Anweisung oder widerspricht sich in den eigenen Schritten.

Für den Fall, der dir im Alltag am häufigsten begegnet, die Abweichung von deinem Material, verwendet dieser Artikel das Wort **Quellentreue**. Das Wort Treue kennst du aus D7. Dort ging es darum, ob ein Gedankengang die tatsächlichen Gründe einer Antwort zeigt. Hier geht es darum, ob die Antwort zu deinem Material passt.

Die beiden Gruppen schließen sich nicht immer aus. Liest die Aushilfe das Etikett falsch ab, ist ihre Auskunft auch gegenüber der Welt falsch. Für das Prüfen hilft die Unterscheidung trotzdem. Gegen Faktenfehler hilft vor allem Material von außen (Abschnitt 5). Gegen Fehler bei der Quellentreue hilft das wenig, denn dort war das Material schon da. Dort hilft nur der Abgleich mit dem Original (E8, A8).

Wo das Bild nicht passt: Die Aushilfe weiß meist, ob sie gerade aus dem Kopf spricht oder vom Etikett abliest. Beim Modell landet beides im selben Kontext, und die Antwort entsteht in beiden Fällen auf dieselbe Weise, Token für Token (D4).

---

## 2. Seltene Fakten: das Problem der dünnen Notizen

Die Gärtnerei schickt Stammkunden zum Geburtstag einen Gutschein. Die Geburtstage stehen verstreut in alten Notizbüchern. Den von Frau Lange haben drei Kolleginnen notiert, den von Herrn Brandt nur eine. Wer aus diesen Notizen lernt, kennt Frau Langes Geburtstag sicher. Bei Herrn Brandt hängt alles an einem einzigen Eintrag.

Eine Arbeit von 2025, die in E6 schon kurz vorkam, hat diesen Gedanken mathematisch gefasst. Manche Fakten folgen keinem Muster, das sich lernen ließe. Der Geburtstag eines Kunden ergibt sich aus keinem anderen Fakt, er muss schlicht bekannt sein. Für solche Fakten leitet die Arbeit unter ihren Annahmen eine Untergrenze her. Ein Basismodell nach dem Vortraining (D5) liegt mindestens ungefähr so oft falsch, wie die **Einzelnennungs-Rate** (englisch singleton rate) angibt. Gemeint ist die Zahl der Fakten, die in den Trainingsdaten genau einmal vorkommen, geteilt durch die Zahl aller Trainingsbeispiele. Als grobes Beispiel nennt die Arbeit: Kommen 20 Prozent der Geburtstagsangaben nur einmal vor, ist bei Geburtstagen mit mindestens etwa 20 Prozent Fehlern zu rechnen. Das gilt laut Arbeit sogar dann, wenn die Trainingsdaten selbst fehlerfrei sind.

Wie die Rate gezählt wird, zeigt ein kleines Programm mit den Notizen der Gärtnerei:

```python
from collections import Counter

notizen = (["Frau Lange: 12.03."] * 3 + ["Herr Okafor: 02.07."] * 2
           + ["Frau Brix: 30.09."] * 2 + ["Herr Yilmaz: 14.11."] * 2
           + ["Herr Brandt: 05.05.", "Frau Petersen: 21.01."])
zaehler = Counter(notizen)
einzeln = [fakt for fakt, anzahl in zaehler.items() if anzahl == 1]
print(f"{len(notizen)} Einträge, {len(zaehler)} Kunden, davon {len(einzeln)} nur einmal notiert")
print(f"Einzelnennungs-Rate: {len(einzeln)} von {len(notizen)} = {len(einzeln) / len(notizen):.0%}")
```

```text
11 Einträge, 6 Kunden, davon 2 nur einmal notiert
Einzelnennungs-Rate: 2 von 11 = 18%
```

In diesen Spielzeug-Notizen läge die Rate bei rund 18 Prozent. Die Rechnung zeigt nur die Zählweise. Über die Fehlerquote eines echten Modells sagt sie nichts, echte Trainingsdaten sind unvorstellbar viel größer.

Daraus folgt eine Regel aus E6, die jetzt eine Begründung hat. Je seltener ein Fakt in Texten auftaucht und je weniger er sich aus anderem ableiten lässt, desto skeptischer solltest du sein. Geburtstage, Nischenstudien, kleine Firmen, wenig bekannte Personen und Details aus deinem Betrieb sind typische Fälle.

Wo das Bild nicht passt: Notizbücher gibt es im Modell nicht. Es hat keine Einträge, die es nachschlagen könnte, nur Gewichte (D5). Ob ein Fakt einmal oder hundertmal im Training vorkam, siehst du der Antwort nicht an. Die Formulierung klingt in beiden Fällen gleich flüssig, denn Sprache und Stil hat das Modell aus Millionen Beispielen gelernt.

---

## 3. Wenn Raten sich lohnt

Bei einer Ankreuzprüfung ohne Minuspunkte lohnt sich Raten immer. Ein leeres Kästchen bringt sicher null Punkte, ein geratenes Kreuz vielleicht einen. Wer klug ist, kreuzt überall etwas an.

Die Arbeit von 2025 sieht hier die zweite Ursache, und sie betrifft das Nachtraining (D5). Modelle werden an Tests gemessen und auf gute Ergebnisse hin weiterentwickelt. Die Autoren haben verbreitete Tests durchgesehen. Die meisten bewerten **binär**: Eine richtige Antwort gibt einen Punkt, eine falsche und ein „Das weiß ich nicht" geben beide null. Nach dieser Rechnung ist ein selbstbewusster Rateversuch immer die beste Wahl, und ehrliche Unsicherheit wird bestraft.

Die Autoren schlagen vor, in Tests ausdrücklich eine Schwelle zu nennen. Antworte nur, wenn du dir sicherer als `t` bist. Eine falsche Antwort kostet dann `t / (1 − t)` Punkte, „weiß nicht" bleibt bei null. Was das ändert, rechnet ein Programm für die Schwelle 0,75 aus:

```python
def erwartung(p, abzug):
    return p * 1 - (1 - p) * abzug   # richtig +1, falsch -abzug, "weiß nicht" 0

t = 0.75
abzug = t / (1 - t)   # 3 Punkte
for p in (0.3, 0.6, 0.9):
    print(f"Sicherheit {p}: ohne Abzug {erwartung(p, 0):+.2f}, mit Abzug {erwartung(p, abzug):+.2f}")
```

```text
Sicherheit 0.3: ohne Abzug +0.30, mit Abzug -1.80
Sicherheit 0.6: ohne Abzug +0.60, mit Abzug -0.60
Sicherheit 0.9: ohne Abzug +0.90, mit Abzug +0.60
```

Ohne Abzug ist Antworten immer besser als „weiß nicht", auch bei 30 Prozent Sicherheit. Mit Abzug lohnt es sich erst oberhalb der Schwelle. Wer ein Modell auf Tests der ersten Art optimiert, begünstigt das Raten.

Zwei weitere Befunde passen dazu. Aus D5 kennst du den Bericht, nach dem die Wahrscheinlichkeiten eines Modells bei einem Test mit Auswahlantworten vor dem Nachtraining gut zur tatsächlichen Trefferquote passten, danach deutlich schlechter. Und eine Studie von 2024 hat Modelle in einem kontrollierten Versuch mit Fragen ohne Nachschlagen gezielt mit Fakten nachtrainiert, die sie vorher nicht kannten. Diese Beispiele lernten die Modelle langsamer. Sobald sie gelernt waren, stieg die Neigung zu Halluzinationen mit ihrem Anteil. Die Autoren schließen daraus, dass Modelle ihr Faktenwissen vor allem im Vortraining erwerben und das Nachtraining eher regelt, wie sie es einsetzen. Für diesen Versuchsaufbau heißt das: Wer im Nachtraining Antworten auf Unbekanntes verlangt, kann das Raten fördern. Ob das für jedes Nachtraining und für längere Texte gilt, lässt die Studie offen.

Wo das Bild nicht passt: Ein Prüfling entscheidet bewusst, ob er rät. Das Modell trifft keine solche Entscheidung. Das Training verschiebt nur, wie viele Lose ein „Das weiß ich nicht" in der Tombola aus D4 bekommt.

---

## 4. Beim Schreiben: der Schneeball

Die Aushilfe hat „Juli" gesagt. Die Kundin hakt nach: „Und warum gerade Juli?" Jetzt kann die Aushilfe ihren Fehler zugeben. Oder sie erfindet eine Begründung, die zur ersten Antwort passt, etwa dass die Sorte aus einer Sommerzüchtung stammt.

Beim Sprachmodell liegt der zweite Weg nahe. Aus D4 weißt du: Ein gezogenes Token bleibt stehen, und alles Weitere baut darauf auf. Steht „Juli" einmal im Text, ist eine passende Begründung die wahrscheinlichste Fortsetzung. Eine Arbeit von 2023 nennt das **Schneeballeffekt** (englisch hallucination snowballing). Die Forschenden bauten Fragen, bei denen zwei damals verbreitete Modelle oft früh eine falsche Antwort gaben und sie dann mit weiteren falschen Behauptungen begründeten. Legten sie die falschen Behauptungen den Modellen später einzeln vor, erkannte das ältere Modell 67 Prozent davon selbst als falsch, das neuere 87 Prozent.

Das zeigt zweierlei. Bei getrennter Prüfung konnten die Modelle viele ihrer eigenen Behauptungen als falsch erkennen. Im laufenden Text begünstigte das bereits Geschriebene trotzdem weitere passende, aber falsche Behauptungen. Und eine getrennte Prüfung findet mehr Fehler als die laufende Antwort. Deshalb hilft es manchmal, eine Antwort in einem neuen Gespräch prüfen zu lassen, ohne die ursprüngliche Begründung mitzugeben (A8). Eine Garantie ist das nicht, wie E6 gezeigt hat.

Auch Gedankengänge aus D7 sind kein Schutz. Ein Anbieter hat 2025 für ein neueres Denkmodell bei einem Test mit Fragen zu Personen eine höhere Halluzinationsrate gemessen als beim Vorgänger. Er erklärt das unter anderem damit, dass das Modell insgesamt mehr Behauptungen aufstellt, richtige wie falsche, und schreibt selbst, dass die Ursache weiter erforscht werden muss.

Wo das Bild nicht passt: Die Aushilfe verteidigt ihren Fehler vielleicht aus Verlegenheit. Beim Modell gibt es keine Verlegenheit, nur die Wahrscheinlichkeit der nächsten Tokens im bisherigen Kontext.

---

## 5. Was Retrieval verbessert

Die Aushilfe muss nicht aus dem Kopf antworten. Sie kann im Pflanzenlexikon nachschlagen und die Blütezeit vorlesen. Das ist langsamer, aber bei seltenen Sorten viel sicherer.

Für Sprachmodelle gibt es dieses Nachschlagen als **Retrieval** (Abruf). Vor der Antwort sucht ein System passende Textstellen heraus, etwa aus dem Netz oder aus deinen Dokumenten. Diese Stellen legt es mit in den Kontext. Die Antwort soll sich dann auf diese Stellen stützen. Die Arbeit von 2020, die den Begriff **Retrieval-Augmented Generation** (RAG) bekannt gemacht hat, unterscheidet dafür zwei Gedächtnisse. Das eine steckt in den Gewichten, das andere in einer durchsuchbaren Textsammlung. Ihr Ansatz lieferte laut Arbeit genauere und sachlich richtigere Texte als ein Modell, das nur aus seinen Gewichten schöpfte. Wie die Suche nach Bedeutung funktioniert, weißt du aus D2, den Aufbau eines eigenen RAG-Systems zeigt P4.

Retrieval setzt beim Problem aus Abschnitt 2 an der richtigen Stelle an. Seltene oder neue Fakten müssen nicht mehr in den Gewichten stecken, sie kommen über das Material. Neue Fehlerquellen bringt es aber mit:

- **Falsches Material gefunden.** Holt die Suche die falschen oder veralteten Stellen, stützt sich die Antwort sauber auf Falsches.
- **Richtiges Material, falsch wiedergegeben.** Jetzt drohen die Fehler bei der Quellentreue aus Abschnitt 1. Steht die entscheidende Stelle mitten in einem langen Kontext, wird sie leichter übersehen (D1).
- **Material und Gewichte widersprechen sich.** Dann kann sich das Modell an sein trainiertes Wissen halten statt an dein Dokument.

Wie viel trotzdem schiefgehen kann, zeigt die Auswertung von Rechtsrecherche-Werkzeugen aus E6: Trotz Quellenanbindung lag ein erheblicher Teil der Antworten daneben.

Wo das Bild nicht passt: Die Aushilfe weiß, welches Lexikon sie aufgeschlagen hat, und liest die passende Zeile. Ein Retrieval-System sucht nach Ähnlichkeit (D2). Was ähnlich klingt, ist nicht immer das, was die Frage beantwortet.

---

## 6. Was Quellenangaben verbessern

Ein Lieferschein mit Artikelnummer macht die Kontrolle leicht: Du nimmst die Nummer und schaust nach. Ob die gelieferte Pflanze wirklich die bestellte ist, erfährst du aber erst beim Nachschauen.

Mit Quellenangaben ist es genauso. Eine Studie von 2023 hat vier damals verbreitete Suchmaschinen mit Chat-Antwort untersucht. Die Antworten wirkten flüssig und informativ. Trotzdem war nur gut die Hälfte der Sätze, 51,5 Prozent, vollständig durch die angegebenen Quellen gedeckt. Und nur 74,5 Prozent der Quellenangaben stützten den Satz, an dem sie standen. Die Werte gelten für die vier damals untersuchten Dienste und den Aufbau der Studie, eine Messung heutiger Suchassistenten sind sie nicht.

Eine Quellenangabe ist also zuerst ein Werkzeug zum Prüfen. Sie sagt dir, wo du nachsehen kannst. Dass die Aussage dort steht, sagt sie nicht. Das passt zu E6: Auch die Angabe selbst ist eine Behauptung des Modells, und die Prüfung findet im Original statt (A3).

Was hilft außerdem? Aus D4 kennst du die Idee, dieselbe Frage mehrmals zu stellen. Gehen die Antworten weit auseinander, ist das ein Warnsignal für erfundene Fakten. Stimmen sie überein, ist das ein Hinweis und kein Beweis, denn dieselben Gewichte können denselben Fehler immer wieder wahrscheinlich machen (Abschnitt 2). Und die Arbeit von 2025 zeigt einen Weg, der beim Bewerten ansetzt: Wer Unsicherheit nicht bestraft, bekommt öfter ehrliche Unsicherheit (Abschnitt 3).

Wo das Bild nicht passt: Eine Artikelnummer auf dem Lieferschein ist selten erfunden. Eine Quellenangabe eines Modells kann es sein, mit echtem Titel, falscher Seite oder einer Seite, die es gar nicht gibt (E6).

---

## 7. Was du daraus machst

**Seltenes besonders prüfen.** Je seltener ein Fakt vermutlich in Texten vorkommt, desto wahrscheinlicher ist eine Erfindung. Daten aus deinem Betrieb, Nischenthemen und wenig bekannte Personen prüfst du immer (E6).

**Material mitgeben.** Wenn es eine verlässliche Quelle gibt, gib sie mit oder nutze ein Werkzeug mit Suche. Das senkt Faktenfehler deutlich, ersetzt aber nicht den Blick ins Original (A2, A3).

**Den Fehlertyp erkennen.** Ist eine Aussage über die Welt falsch, prüfe sie an einer verlässlichen Quelle außerhalb des Gesprächs. Ursachen können fehlendes, falsches oder falsch verarbeitetes Wissen sein. Weicht die Antwort von deinem Dokument ab, vergleiche Stelle für Stelle mit dem Original (E8).

**Unsicherheit erlauben.** Sag ausdrücklich, dass „weiß ich nicht" eine gute Antwort ist, und frage bei wichtigen Fakten nach, wie sicher das Modell ist. Die angegebene Sicherheit ist selbst eine Ausgabe des Modells und damit ein Warnsignal, kein Beweis. Du drehst aber an derselben Stellschraube wie die Tests in Abschnitt 3 (E4).

**Getrennt prüfen.** Lass eine Antwort in einem neuen Gespräch prüfen, ohne die ursprüngliche Begründung, oder vergleiche mit einem anderen Werkzeug. Das findet mehr als ein „Bist du sicher?" im selben Verlauf (E6, A8).

**Quellenangaben öffnen.** Eine Angabe ist eine Einladung zum Nachsehen, kein Beleg.

> **Beispielbox, Stand 03.11.2026: Zahlen aus Berichten und Studien.** Herstellerangaben sind nicht unabhängig geprüft, Modellnamen und Testverfahren ändern sich.
>
> - **Why Language Models Hallucinate** (OpenAI und Georgia Tech, September 2025): Herleitung der Untergrenze über Einzelnennungen, Durchsicht verbreiteter Tests mit binärer Bewertung, Vorschlag ausdrücklicher Sicherheitsschwellen in Tests.
> - **OpenAI o3 und o4-mini** (Systemkarte, April 2025): Beim Test PersonQA lag die Halluzinationsrate bei 33 Prozent für o3 und 48 Prozent für o4-mini, gegenüber 16 Prozent beim älteren o1. Beim Test SimpleQA lagen die Werte bei 51, 79 und 44 Prozent.
> - **Schneeball-Studie** (2023): untersucht wurden ChatGPT (67 Prozent eigene Fehler erkannt) und GPT-4 (87 Prozent).
> - **Generative Suchmaschinen** (Studie 2023): untersucht wurden Bing Chat, NeevaAI, perplexity.ai und YouChat, Angebote in ihrer damaligen Form.

---

## Häufige Fehlgriffe

- **„Halluzinationen sind Programmierfehler, die bald behoben sind."** Sie folgen aus Training und Bewertung. Ihre Häufigkeit lässt sich senken, aber nicht auf null bringen (Abschnitt 2 und 3, E6).
- **„Wenn es so flüssig klingt, hat das Modell den Fakt oft gesehen."** Sprache und Stil sind gut gelernt, auch wenn der Fakt nur einmal vorkam (Abschnitt 2).
- **„Saubere Trainingsdaten würden das Problem lösen."** Auch mit fehlerfreien Daten entstehen laut Arbeit Fehler bei seltenen Fakten (Abschnitt 2).
- **„Eine ausführliche Begründung macht die Antwort glaubwürdiger."** Eine Begründung kann einen frühen Fehler nur nachträglich stützen (Abschnitt 4).
- **„Denkmodelle halluzinieren weniger."** Das hängt vom Modell und vom Test ab, ein Anbieter hat bei einem neueren Denkmodell sogar mehr gemessen (Abschnitt 4, D7).
- **„Mit Suche oder RAG gibt es keine Halluzinationen mehr."** Retrieval senkt Faktenfehler, bringt aber eigene Fehlerquellen mit (Abschnitt 5).
- **„Eine Antwort mit Quellenangabe ist geprüft."** In der Studie stützte rund jede vierte Angabe ihren Satz nicht (Abschnitt 6).
- **„Wenn ich nach meinem Dokument frage, kann nichts erfunden werden."** Fehler bei der Quellentreue gibt es gerade dann (Abschnitt 1).

---

## Zum Ausprobieren

1. Ändere das Programm aus Abschnitt 2 so, dass Herr Brandt und Frau Petersen je dreimal notiert sind. Wie ändert sich die Einzelnennungs-Rate? Ergänze danach drei neue Kunden mit je einem Eintrag und rechne erneut.
2. Ändere das Programm aus Abschnitt 3 auf die Schwelle 0,5 und dann auf 0,9. Wie hoch ist der Abzug jeweils, und was ergibt sich genau an der Schwelle? Ab welcher Sicherheit lohnt sich Antworten also?
3. Frage einen Chat-Assistenten ohne Suche nach der Blütezeit einer bekannten und einer sehr seltenen Pflanzensorte. Prüfe beide Antworten an einer verlässlichen Quelle und notiere, ob die Antwort zur seltenen Sorte weniger sicher klang.
4. Gib einem Chat-Assistenten einen kurzen Text, etwa eine Pflegeanleitung, und lass ihn zusammenfassen. Vergleiche jede Aussage der Zusammenfassung mit dem Text und markiere, was dort nicht steht. Das ist ein Test der Quellentreue.
5. Nutze ein Werkzeug mit Suche und Quellenangaben für eine Sachfrage. Öffne drei der angegebenen Quellen und prüfe, ob der jeweilige Satz dort tatsächlich gedeckt ist.

Am Ende kannst du an eigenen Beispielen zeigen, wo Faktenfehler und Fehler bei der Quellentreue entstehen und was Suche und Quellenangaben daran ändern.

---

## Fazit

Halluzinationen sind keine Absicht. Sie entstehen aus den Grenzen von Daten, Training und Generierung. Bei Fakten ohne lernbares Muster liegt ein Basismodell nach der Arbeit von 2025 mindestens ungefähr so oft falsch, wie die Einzelnennungs-Rate angibt. Das Nachtraining auf Tests ohne Abzug für falsche Antworten belohnt das Raten zusätzlich. Beim Schreiben kann ein früher Fehler weitere nach sich ziehen, und auch Gedankengänge schützen davor nicht sicher. Retrieval setzt bei fehlendem Wissen an der richtigen Stelle an, bringt aber Fehler bei Suche und Quellentreue mit. Quellenangaben machen Prüfen leicht, ersetzen es aber nicht. Flüssig ist nicht wahr, und die Prüfung findet im Original statt. Woher die Trainingsdaten stammen und welche Verzerrungen und Rechtsfragen daraus folgen, zeigt D9.

```yaml
dokument: ki-d8-warum-halluzinationen-entstehen
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-11-03
quellen_fachlich:
  - "Huang u. a.: A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions, ACM Transactions on Information Systems, online November 2024, DOI 10.1145/3703155, arXiv:2311.05232. https://arxiv.org/html/2311.05232v2 (Zugriff 2026-11-03): Factuality Hallucination (factual contradiction, factual fabrication) gegenüber Faithfulness Hallucination (instruction, context, logical inconsistency); Ursachen in Daten, Training und Inferenz"
  - "Kalai, Nachum, Vempala, Zhang (OpenAI, Georgia Tech): Why Language Models Hallucinate (2025-09-04), arXiv:2509.04664. https://arxiv.org/abs/2509.04664 und https://www.alphaxiv.org/abs/2509.04664.md (Zugriff 2026-11-03): Rückführung auf binäre Klassifikation (Is-It-Valid); Fakten ohne lernbares Muster (Geburtstage); Einzelnennungs-Rate sr = |S|/N (Zahl der genau einmal vorkommenden Anfragen geteilt durch alle N Trainingsbeispiele, Good-Turing) als Untergrenze der Halluzinationsrate von Basismodellen unter den Annahmen der Arbeit; informelles Beispiel 20 Prozent Einzelnennungen gleich mindestens 20 Prozent Halluzination; Fehler auch bei fehlerfreien Trainingsdaten; Tabelle verbreiteter Tests überwiegend binär ohne Punkte für weiß nicht; Vorschlag ausdrücklicher Schwellen t mit Abzug t/(1-t)"
  - "Zhang, Press, Merrill, Liu, Smith: How Language Model Hallucinations Can Snowball (2023), arXiv:2305.13534. https://arxiv.org/abs/2305.13534v1 (Zugriff 2026-11-03): früher Fehler wird mit weiteren falschen Behauptungen begründet; drei Frage-Datensätze; einzeln vorgelegt erkennen ChatGPT 67 Prozent und GPT-4 87 Prozent der eigenen Fehler"
  - "Gekhman u. a.: Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations? (2024, v3 2024-10-01), arXiv:2405.05904. https://arxiv.org/abs/2405.05904 (Zugriff 2026-11-03): kontrolliertes Closed-Book-Frage-Antwort-Setup; Beispiele mit neuem Wissen werden langsamer gelernt; sobald gelernt, steigt die Halluzinationsneigung linear; Wissen vor allem aus dem Vortraining, Feinabstimmung lehrt effizientere Nutzung"
  - "Lewis u. a.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020), arXiv:2005.11401. https://arxiv.org/abs/2005.11401v4 (Zugriff 2026-11-03): parametrisches Gedächtnis (seq2seq) und nicht-parametrisches Gedächtnis (dichter Vektorindex von Wikipedia); 'more specific, diverse and factual language' als ein rein parametrisches Basismodell; Herkunftsangaben und Aktualisierung als offene Probleme"
  - "Liu, Zhang, Liang: Evaluating Verifiability in Generative Search Engines (2023, v2 2023-10-23), arXiv:2304.09848. https://arxiv.org/abs/2304.09848 (Zugriff 2026-11-03): Bing Chat, NeevaAI, perplexity.ai, YouChat; Antworten flüssig und informativ wirkend; nur 51,5 Prozent der Sätze vollständig durch Zitate gedeckt, nur 74,5 Prozent der Zitate stützen ihren Satz"
  - "OpenAI: o3 and o4-mini System Card (2025-04-16). https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf (Zugriff 2026-11-03): Tabelle 4, PersonQA Halluzinationsrate o3 0,33, o4-mini 0,48, o1 0,16; SimpleQA 0,51, 0,79, 0,44; o3 macht insgesamt mehr Behauptungen; 'More research is needed to understand the cause'"
  - "OpenAI: GPT-4 Technical Report (2023), Abschnitt 5 und Abbildung 8 (siehe D5): Kalibrierung vor und nach dem Nachtraining"
  - "Rechnungen am 2026-11-03 mit Python ausgeführt: Notizen mit 11 Einträgen, 6 Kunden, 2 Einzelnennungen, Rate 2/11 = 18 Prozent (nach sr = |S|/N); Erwartungswert bei Schwelle 0,75 und Abzug 3 nach t/(1-t): Sicherheit 0,3 ohne Abzug +0,30, mit Abzug -1,80; 0,6 +0,60 und -0,60; 0,9 +0,90 und +0,60; Übung 2: t=0,5 Abzug 1, t=0,9 Abzug 9, genau an der Schwelle Erwartungswert 0"
  - "Eigene Artikel der Reihe: E6 (Halluzinationen, Prüfen, Rechtsrecherche-Werkzeuge 17 bis 33 Prozent), E4, E8, A2, A3, A8, D1 (Lost in the Middle), D2 (Suche nach Ähnlichkeit), D4 (Tombola, kein Radiergummi, mehrfach fragen), D5 (Gewichte, Kalibrierung nach dem Nachtraining), D7 (Treue von Gedankengängen, Denkmodelle); Vorwärtsverweise auf D9 und P4"
verifikation_offen:
  - "Einzelnennungs-Rate im Text nach der formalen Definition (|S|/N) gezählt; das informelle 20-Prozent-Beispiel der Arbeit ist sprachlich auf Fakten bezogen und im Text als grobes Beispiel gekennzeichnet; Nebenterme der Schranke nicht wiedergegeben; Untergrenze gilt unter den Annahmen der Arbeit für Basismodelle nach dem Vortraining und für Fakten ohne lernbares Muster"
  - "Abzug t/(1-t): Die Beispielreihe der Arbeit nennt für t=0,75 einen Abzug von 2, die eigene Formel ergibt 3 (bei t=0,5 und 0,9 passen Beispiel und Formel); Widerspruch im Original, Programm folgt der Formel"
  - "Spielzeug-Notizen sind eine eigene Veranschaulichung (W), keine Messung; Geburtstage statt Blütezeiten, weil Blütezeiten teils aus anderen Merkmalen ableitbar sind"
  - "Aussage, Sprache und Stil würden zuverlässiger gelernt als Einzelfakten, ist an E6 und die Arbeit von 2025 angelehnt (Rechtschreibung als Muster), im Text als Erklärung formuliert"
  - "Drei Fehlerquellen von Retrieval (falsches Material, Wiedergabe, Widerspruch zum Gewichtswissen) sind verbreitetes Fachwissen (W), die Übersichtsarbeit nennt schwache Aufmerksamkeit auf den Kontext; Widerspruch Material gegen Gewichte nicht mit eigener Studie belegt"
  - "Schneeballeffekt: im Text auf den Befund begrenzt (getrennte Prüfung erkennt viele eigene Fehler), keine Aussage über inneres Wissen"
  - "o3-Befund: Herstellerangabe zu einem Test (PersonQA); Ursache laut Anbieter nicht geklärt; keine allgemeine Aussage über Denkmodelle"
  - "Ratschlag, getrennt in neuem Gespräch prüfen zu lassen, ist eine Ableitung (W) aus der Schneeball-Arbeit, keine dort getestete Empfehlung"
  - "Vorwärtsverweise auf D9 und P4 beim Anlegen abgleichen"
review_historie:
  - runde: 0
    datum: 2026-11-03
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). Übersichtsarbeit, Arbeit von 2025 zu Ursachen, Schneeball-Arbeit, Studie zum Nachtraining mit neuem Wissen, RAG-Arbeit, Studie zu generativen Suchmaschinen und Systemkarte o3/o4-mini an der Quelle gelesen. Rechenbeispiele ausgeführt. Löst die Vorwärtsverweise aus D3, D4 und D7 ein, ergänzt E6 um die Mechanik."
  - runde: 1
    datum: 2026-11-03
    ergebnis: "Eigene Reviews (Fach und Stil, Prüf-Sweep). Verneinungs-Gegensatz und man-Formulierung aufgelöst, vier lange Sätze geteilt; Kalibrierungsbefund aus D5 ohne Vermenschlichung; Fazit auf 'mindestens ungefähr' angeglichen. Programme erneut ausgeführt."
  - runde: 2
    datum: 2026-11-03
    ergebnis: "Drei externe Reviews, strittige Punkte am Original geprüft. Übernommen: Einzelnennungs-Rate nach formaler Definition (2 von 11 statt 2 von 6), Beispiel auf Geburtstage umgestellt; Widerspruch der Arbeit bei t=0,75 dokumentiert; Oberbegriff Treue- und Konsistenzfehler, Quellentreue als Teilfall, Überschneidung erwähnt; Nachtraining-Studie auf Versuchsaufbau begrenzt; Schneeball ohne Aussage über inneres Wissen; Kalibrierung auf Auswahltest begrenzt; RAG soll sich stützen; Fehlertyp-Absatz, Selbsteinschätzung als Warnsignal, Begrenzung der Suchmaschinen-Studie, Mehrfach-Fragen begründet, Grammatik, Fazit-Einstieg, Übung 2. Nicht bestätigt: Jahr 2025 der Übersichtsarbeit (Katalog nennt 2024). Nicht übernommen: Studien- und Modellnamen im Fließtext (Reihenregel, Modellzuordnung 67/87 in der Box), Status reviewed (gibt es in der Reihe nicht), unbelegte Aussage zum Verschwinden der Suchdienste."
  - runde: 3
    datum: 2026-11-03
    ergebnis: "Freigabe durch David am 2026-11-03 nach Runde 2. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen (Lehrbuchwissen ohne Einzelquelle, Herstellerangaben, Widerspruch in der Arbeit von 2025, Vorwärtsverweise auf D9 und P4)."
```
