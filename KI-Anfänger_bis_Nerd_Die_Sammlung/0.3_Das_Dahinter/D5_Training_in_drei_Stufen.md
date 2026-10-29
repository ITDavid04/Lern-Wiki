# KI-D5 · Training in drei Stufen: Vom Lückentext zum Assistenten

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Dahinter-Block, Artikel D5 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

In D2 bis D4 stand immer wieder derselbe Halbsatz: Die Zahlen sind „beim Training entstanden". Die Embedding-Tabelle, die Gewichte für Abfrage, Schlüssel und Wert, die Lose in der Tombola. Woher kommen all diese Zahlen? Niemand hat 7 Milliarden davon von Hand eingetragen.

Am Ende dieses Artikels kannst du die drei typischen Stufen beschreiben, in denen aus einem Haufen Zufallszahlen ein Chat-Assistent wird. Zuerst lernt ein Modell aus riesigen Textmengen, das nächste Token vorherzusagen. Dann lernt es an Beispielen, Anweisungen zu befolgen. Schließlich wird es mit Bewertungen nachgeschärft. Du weißt, was jede Stufe bewirkt, welche Nebenwirkungen das Feedback haben kann und was Training nicht ist. Die drei Stufen sind ein Grundschema. Nicht jeder Anbieter folgt genau diesem Ablauf, und einzelne Stufen werden oft mehrfach durchlaufen oder anders kombiniert.

Vorausgesetzt werden D1 bis D4, vor allem die Wahrscheinlichkeitsverteilung aus D4. Aus E1 kennst du den Unterschied zwischen Training und Inferenz, hier geht es um die erste Hälfte.

---

## 1. Ausgangslage: lauter Zufallszahlen

Bevor das Training beginnt, stehen in den meisten Gewichten eines Modells Zufallszahlen, einige wenige starten mit festen Werten. Das Modell hat schon seine Bauart aus D3, mit Schichten, Köpfen und Tabellen, aber die Zahlen darin bedeuten noch nichts. Fragst du es etwas, kommt Buchstabensalat heraus, denn die Tombola aus D4 verteilt ihre Lose beliebig.

**Training** heißt: Diese Zahlen werden in sehr vielen kleinen Schritten so verändert, dass das Modell eine Aufgabe besser erfüllt. Was „besser" heißt, legt die Aufgabe fest, und genau die ändert sich von Stufe zu Stufe.

Ein Bild aus der Gärtnerei begleitet dich durch den Artikel. Stell dir eine neue Kraft vor, die den Beruf in drei Abschnitten lernt. Zuerst liest sie alles, was es in der Gärtnerei zu lesen gibt. Dann lernt sie an Mustergesprächen, wie eine gute Beratung klingt. Und am Ende hört sie bei echten Beratungen zu und bekommt Rückmeldung, welche Antwort besser war.

---

## 2. Stufe 1: Vortraining, der riesige Lückentext

Die neue Kraft sitzt im Winter im Büro und liest. Fachbücher, Saatgutkataloge, alte Bestellungen, Pflegeanleitungen, Kundenbriefe, alles. Und sie macht dabei ein Spiel: Bevor sie ein Wort liest, rät sie, welches kommt. Liegt sie daneben, merkt sie es sofort und rät beim nächsten Mal ein bisschen anders.

Das ist das **Vortraining** (englisch pretraining). Das Modell bekommt sehr große Textmengen und soll an jeder Stelle das nächste Token vorhersagen. Die richtige Antwort steht schon im Text, deshalb braucht niemand die Daten von Hand zu beschriften. Das nennt sich **selbstüberwachtes Lernen**.

Wie „daneben" ein Modell lag, misst eine Zahl, der **Verlust** (englisch loss). Eine verbreitete Wahl ist der negative Logarithmus der Wahrscheinlichkeit, die das Modell dem richtigen Token gegeben hat. Mit den Losen aus D4 sieht das so aus:

```python
from math import log

# Wahrscheinlichkeiten aus D4 (T = 1,0) für "Die Tomaten brauchen mehr ..."
p = {"Wasser": 0.526, "Sonne": 0.236, "Dünger": 0.117, "Strom": 0.0035}

for richtig in ("Wasser", "Sonne", "Dünger", "Strom"):
    verlust = -log(p[richtig])
    print(f"Im Text stand '{richtig}': Verlust {verlust:.2f}")

print(f"Wasser mit 0.90 statt 0.526: Verlust {-log(0.90):.2f}")
```

```text
Im Text stand 'Wasser': Verlust 0.64
Im Text stand 'Sonne': Verlust 1.44
Im Text stand 'Dünger': Verlust 2.15
Im Text stand 'Strom': Verlust 5.65
Wasser mit 0.90 statt 0.526: Verlust 0.11
```

Stand im Trainingstext „Wasser", war das Modell mit 53 Prozent recht nah dran, der Verlust ist klein. Stand dort „Strom", hatte das Modell kaum Lose dafür vergeben, und der Verlust ist groß. Je sicherer das Modell beim richtigen Token ist, desto näher kommt der Verlust an 0. Die letzte Zeile zeigt das. Im echten Training zählt nicht ein einzelnes Token: Der Verlust wird über alle Tokens eines kleinen Datenpakets gemittelt (englisch mini-batch).

Vor jedem Änderungsschritt berechnet das Training, wie jedes einzelne Gewicht den gemittelten Verlust dieses Pakets beeinflusst. Das sind Ableitungen, wie du sie aus der Mathematik kennst, und zusammen bilden sie den **Gradienten**. Er zeigt in die Richtung, in der der Verlust am stärksten steigt. Beim einfachen Gradientenabstieg werden die Gewichte deshalb ein winziges Stück in die Gegenrichtung geschoben, also bergab. Die tatsächlich verwendeten Verfahren verfeinern dieses Grundprinzip. Danach kommt das nächste Datenpaket, und das wiederholt sich über sehr viele Trainingsschritte.

Die Größenordnung laut Herstellerangaben: Vortraining auf rund 15 bis 18 Billionen Tokens und mehrere zehn Millionen Stunden Rechenzeit auf Grafikkarten (genaue Zahlen in der Beispielbox am Ende von Abschnitt 4). Deshalb nennt A9 das Training einen gewaltigen Aufwand, den ein Anbieter betreibt.

Das Ergebnis heißt **Basismodell**. Es kann erstaunlich viel: Grammatik, Fakten, Programmiersprachen, Stile. Aber es kann vor allem eines, nämlich Text fortsetzen. Stellst du ihm eine Frage, schreibt es womöglich weitere Fragen dazu, weil in seinen Texten auf eine Frage oft die nächste folgt, etwa in einem Quiz. Eine viel zitierte Arbeit von 2022 hält dazu fest, dass ein größeres Modell nicht automatisch besser darin wird, das zu tun, was jemand von ihm will.

Wo das Bild nicht passt: Die neue Kraft versteht beim Lesen, worum es geht, und kann draußen nachsehen, ob eine Pflanze wirklich so aussieht. Ein reines Sprachmodell hat nur Text. Es lernt, welche Fortsetzungen zu welchen Mustern passen, ohne je ein Beet gesehen zu haben.

---

## 3. Stufe 2: Feinabstimmung auf Anweisungen

Im Frühjahr kommt die Ausbildung. Die Meisterin zeigt der neuen Kraft Mustergespräche: So fragt ein Kunde nach einer Hecke, so sieht eine gute Antwort aus. Wieder und wieder, mit vielen verschiedenen Fragen. Nach einer Weile antwortet die neue Kraft auf eine Frage mit einer Antwort statt mit der nächsten Frage.

Das ist die **Feinabstimmung auf Anweisungen** (englisch instruction tuning, auch supervised fine-tuning, kurz SFT). Das Basismodell bekommt Beispiele aus Anweisung und gewünschter Antwort, oft von Menschen geschrieben. Die Technik bleibt dieselbe wie im Vortraining: nächstes Token vorhersagen, Verlust berechnen, Gewichte verschieben. Nur die Texte sind jetzt ausgewählte Gespräche, und es sind sehr viel weniger. Der Bericht zum Modell aus A9 nennt für diese Stufe über eine Million Beispiele. Ein Beispiel kann eine Anweisung mit Antwort oder ein Gespräch mit mehreren Nachrichten sein und besteht selbst aus vielen Tokens. Die Einheiten sind also verschieden. Trotzdem ist der Abstand zu 18 Billionen Tokens im Vortraining gewaltig.

In dieser Stufe lernt das Modell auch das Gesprächsformat: wo eine Nachricht des Nutzers beginnt, wo die Antwort, und dass nach der Antwort Schluss ist. Dazu gehört auch zu lernen, wann es das Stopp-Token aus D4 setzen soll. Im Mittelpunkt steht das Befolgen von Anweisungen. Neues Wissen kann dabei durchaus hinzukommen, aber das breite Fundament stammt aus dem Vortraining.

---

## 4. Stufe 3: Lernen aus Feedback

Jetzt steht die neue Kraft im Verkauf. Bei manchen Kunden gibt sie zwei mögliche Antworten, und die Meisterin sagt, welche besser war. Eine Musterantwort selbst zu schreiben, ist oft schwer. Zwei Antworten zu vergleichen, fällt meist leichter.

Das ist die Idee von **Reinforcement Learning from Human Feedback**, kurz **RLHF**, auf Deutsch etwa „bestärkendes Lernen aus menschlicher Rückmeldung". Eine viel zitierte Arbeit von 2022 hat den Ablauf in drei Schritten beschrieben:

1. Menschen schreiben vorbildliche Antworten, und das Modell wird damit feinabgestimmt. Das ist Stufe 2.
2. Das Modell erzeugt zu einer Anfrage mehrere Antworten, und Menschen bringen sie in eine Rangfolge. Aus vielen solchen Vergleichen wird ein eigenes **Belohnungsmodell** trainiert, das vorhersagt, welche Antwort Menschen besser finden würden.
3. Das Sprachmodell wird dann so weitertrainiert, dass seine Antworten vom Belohnungsmodell höher bewertet werden.

Das Ergebnis war deutlich. Bei den untersuchten Anfragen wurden in den Bewertungen der Studie Antworten eines so trainierten Modells mit 1,3 Milliarden Parametern vorgezogen. Das Vergleichsmodell ohne diese Stufen hatte 175 Milliarden Parameter, also über hundertmal mehr. Die Autoren halten aber auch fest, dass das Modell weiterhin einfache Fehler macht.

Inzwischen gibt es Varianten. Ein Verfahren von 2023 (Direct Preference Optimization, kurz DPO) lernt direkt aus den Vergleichspaaren. Es braucht kein eigens trainiertes Belohnungsmodell und keinen anschließenden Schritt mit bestärkendem Lernen. Die menschlichen Vergleiche selbst braucht es weiterhin. Ein anderer Ansatz von 2022 ersetzt einen Teil der menschlichen Bewertungen durch Bewertungen eines Modells, das sich an einer Liste von Grundsätzen orientiert. Für die Ausrichtung auf Harmlosigkeit geben die Menschen dort nur diese Grundsätze vor. Welche Mischung ein Anbieter verwendet, steht nicht immer im Detail in seinen Berichten. Der Bericht zum Modell aus A9 spricht zum Beispiel von bestärkendem Lernen in mehreren Stufen.

Wo das Bild nicht passt: Die Meisterin erklärt, warum eine Antwort besser war. Das Modell bekommt meist nur das Urteil, besser oder schlechter, und muss selbst herausfinden, was den Unterschied gemacht hat. Dabei kann es auch Dinge lernen, die mit Qualität wenig zu tun haben.

> **Beispielbox, Stand 14.10.2026: Zahlen aus Herstellerangaben.** Der Technical Report zu Qwen2.5, der Familie des Modells aus A9, nennt 18 Billionen Tokens Vortraining (vorher 7 Billionen), über eine Million Beispiele für die Feinabstimmung und bestärkendes Lernen in mehreren Stufen. Die Modellkarte von Llama 3.1 (Meta) nennt rund 15 Billionen Tokens öffentlich verfügbarer Daten, Datenstand Dezember 2023. Für die drei Größen 8B, 70B und 405B zusammen nennt sie 39,3 Millionen Stunden auf Grafikkarten vom Typ H100, davon 30,84 Millionen für 405B. Die Arbeit zu InstructGPT (OpenAI, 2022) ist die oben beschriebene Studie mit 1,3 und 175 Milliarden Parametern. Herstellerangaben lassen sich von außen meist nicht nachprüfen.

---

## 5. Nebenwirkungen des Feedbacks

Was Menschen in einem Vergleich besser finden, ist nicht immer das, was stimmt. Das hat Folgen.

**Zustimmung wird belohnt.** Eine Studie von 2023 fand bei fünf damals führenden Assistenten **Gefälligkeit** (im Englischen sycophancy). Die Modelle neigten dazu, der Meinung der Nutzer zuzustimmen. In vorhandenen Bewertungsdaten wurden Antworten, die zur Sichtweise des Nutzers passten, häufiger bevorzugt. Menschen und Belohnungsmodelle zogen überzeugend geschriebene gefällige Antworten in einem nicht vernachlässigbaren Teil der Fälle sogar korrekten vor. Die Autoren sehen menschliches Feedback deshalb als eine mögliche Ursache. In A7 hast du schon eine Untersuchung kennengelernt, in der aus früheren Gesprächen abgeleiteter Kontext diese Neigung bei drei von fünf Modellen deutlich verstärkte.

**Auch die Kalibrierung kann leiden.** Der technische Bericht zu einem großen Modell von 2023 zeigt das an einem Test mit Auswahlantworten. Vor dem Nachtraining (Stufe 2 und 3) passten die Wahrscheinlichkeiten, die das Modell den Antwortoptionen gab, gut zur tatsächlichen Trefferquote. Danach war diese Übereinstimmung deutlich schlechter. Das ist ein Befund zu einem Modell und einem Test, keine Regel für alle Assistenten. Für deinen Alltag bleibt aus D4: Ein sicherer Ton belegt keine richtige Antwort.

**Ton und Form werden mittrainiert.** Höflichkeit, Struktur mit Überschriften, bestimmte Lieblingswendungen und das Ablehnen mancher Anfragen werden unter anderem in Stufe 2 und 3 geprägt. Auch Systemanweisungen und die Einstellungen aus D4 beeinflussen, wie ein Assistent antwortet. Das erklärt mit, warum sich Assistenten verschiedener Anbieter unterschiedlich anfühlen, obwohl sie technisch ähnlich gebaut sind.

---

## 6. Was Training nicht ist

**Kein unmittelbares Lernen aus deinem Gespräch.** Im üblichen Chatbetrieb nutzt du eine fertig trainierte Modellversion. Was du im Chat schreibst, verändert deren Gewichte nicht. Erinnerungsfunktionen arbeiten mit Kontext (D1, E1). Ob ein Anbieter Gespräche für das Training künftiger Modellversionen verwendet, ist eine andere Frage, die von seinen Einstellungen und Bedingungen abhängt (E7).

**Kein laufender Nachschub.** Die Trainingsdaten haben einen Datenstand. Spätere Trainingsstufen können zwar Wissen ergänzen, aber neue Ereignisse kennt das Modell nicht automatisch, nur weil sie inzwischen passiert sind. Dafür braucht es weitere Trainingsdaten oder Informationen im Kontext, etwa aus Suche oder Dateien (E6, A3).

**Kein verlässliches Nachschlagewerk.** Beim Antworten durchsucht das Modell keine Sammlung seiner Trainingstexte, es rechnet mit seinen Gewichten. Einzelne Textstellen kann es dabei wortgetreu behalten haben, das ist in Versuchen nachgewiesen. Eine richtige oder vollständige Wiedergabe garantiert das aber nicht. Deshalb gilt weiter, was D4 gezeigt hat: wahrscheinlich ist nicht wahr.

**Nicht der einzige Weg zur Anpassung.** Wer ein Modell für eigene Aufgaben anpassen will, muss nicht von vorn trainieren. Welche Wege es gibt und wann sich welcher lohnt, ist Thema von P7. Woher die Trainingsdaten stammen und was daraus folgt, behandelt D9. Und wie Modelle mit eigenen Denkschritten trainiert werden, zeigt D7.

---

## 7. Was du daraus machst

**Bei Zustimmung misstrauisch werden.** Wenn ein Assistent deine Meinung bestätigt, ist das noch kein Beleg. Frag gezielt nach Gegenargumenten oder formuliere die Frage neutral, ohne deine eigene Sicht vorwegzunehmen (A8).

**Sicheren Ton nicht als Beleg werten.** Der Klang einer Antwort ist trainiert. Ob sie stimmt, zeigt die Prüfung an einer Quelle (A3).

**Den Datenstand mitdenken.** Bei allem, was sich ändert, wie Preise, Versionen oder Gesetze, rechne damit, dass das Modell einen älteren Stand kennt.

**Unterschiede zwischen Anbietern als Trainingsfrage sehen.** Wenn ein Assistent ausführlicher, vorsichtiger oder gesprächiger wirkt als ein anderer, steckt dahinter unter anderem das Training der Stufen 2 und 3. Für deine Werkzeugwahl zählt dein eigener Test (A1, A7).

---

## Häufige Fehlgriffe

- **„Das Modell lernt aus meinen Fragen."** Die Gewichte stehen fest, bevor du es nutzt (Abschnitt 6).
- **„Ein größeres Modell befolgt Anweisungen automatisch besser."** Das Befolgen von Anweisungen wird eigens trainiert (Abschnitt 3 und 4).
- **„Feedback-Training macht Modelle wahrheitsgetreuer."** Es macht sie zu dem, was Bewertende bevorzugen, und das kann auch Gefälligkeit sein (Abschnitt 5).
- **„Wenn es sicher klingt, ist es sich sicher."** Ein sicherer Ton belegt nichts, und das Nachtraining kann die Kalibrierung sogar verschlechtern (Abschnitt 5).
- **„Das Modell schlägt beim Antworten in seinen Trainingstexten nach."** Es rechnet mit Gewichten. Einzelne Stellen kann es wortgetreu wiedergeben, verlassen kannst du dich darauf nicht (Abschnitt 6, D9).
- **„Die Feinabstimmung dient vor allem dazu, neues Wissen einzufüllen."** Ihr Schwerpunkt ist, Anweisungen zu befolgen und passend zu antworten. Neues Wissen kann dabei hinzukommen, das Fundament legt das Vortraining (Abschnitt 3).

---

## Zum Ausprobieren

1. Bestimme, ab welcher Wahrscheinlichkeit für das richtige Token der Verlust größer als 1 wird. Prüfe deine Rechnung im Programm aus Abschnitt 2, indem du die Wahrscheinlichkeit für „Wasser" auf 0.99, 0.5 und 0.01 setzt. Was passiert mit dem Verlust, wenn das Modell fast alle Wahrscheinlichkeit auf ein falsches Token legt und das richtige nur noch wenig bekommt?
2. Rechne aus, wie viele Jahre 30,84 Millionen Grafikkarten-Stunden auf einer einzigen Grafikkarte vom Typ H100 im Dauerbetrieb wären. Tipp: Ein Jahr hat 8.760 Stunden.
3. Stelle einem Chat-Assistenten eine Frage zu einem Thema, bei dem du dich gut auskennst, und baue eine falsche Annahme ein, etwa „Warum ist Port 22 für HTTP zuständig?". Notiere, ob der Assistent widerspricht oder mitgeht. Frage danach neutral: „Wofür ist Port 22 zuständig?" und vergleiche.
4. Lass einen Chat-Assistenten in zwei neuen Gesprächen denselben eigenen Text bewerten, jeweils mit dem Auftrag „Bewerte diesen Text nach Verständlichkeit, Aufbau und Sprache. Nenne Stärken und Schwächen." Schreib einmal davor „Ich finde den Text richtig gut." und einmal „Ich finde den Text eher schwach." Vergleiche die Urteile.
5. Frag einen Chat-Assistenten nach einem Ereignis aus den letzten Wochen, ohne dass er im Internet suchen darf. Achte darauf, ob er seinen Datenstand nennt oder trotzdem eine Antwort formuliert. Das ist eine Beobachtung, kein Beweis: Auch die Selbstauskunft eines Assistenten über seinen Datenstand kann falsch sein.

Am Ende hast du ein Gefühl dafür, wie der Verlust Fehler bestraft, eine Vorstellung vom Aufwand des Vortrainings und zwei eigene Beobachtungen zur Gefälligkeit und zum Datenstand deines Werkzeugs.

---

## Fazit

Der Weg zum Chat-Assistenten lässt sich in drei typische Stufen gliedern. Im Vortraining lernt das Modell aus Billionen Tokens, das nächste Token vorherzusagen. Der Verlust zeigt dabei, wie wenig Wahrscheinlichkeit es dem richtigen Token gegeben hat. Das Ergebnis ist ein Basismodell, das Text fortsetzt. In der Feinabstimmung lernt es an Beispielen, auf Anweisungen zu antworten. Im Lernen aus Feedback wird es auf das ausgerichtet, was Bewertende bevorzugen. Das macht Assistenten deutlich nützlicher, kann aber Gefälligkeit fördern und die Kalibrierung verschlechtern. Während der normalen Nutzung bleiben die Gewichte der eingesetzten Modellversion unverändert, und dein Gespräch ändert sie nicht. Als Nächstes geht es in D6 darum, wie unterschiedlich die Ergebnisse dieses Trainings aussehen: große und kleine Modelle, offene und geschlossene Gewichte und spezialisierte Modelle.

```yaml
dokument: ki-d5-training-in-drei-stufen
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: dahinter
status: final
stand: 2026-10-14
quellen_fachlich:
  - "Ouyang u. a.: Training language models to follow instructions with human feedback (NeurIPS 2022), arXiv:2203.02155. https://arxiv.org/abs/2203.02155 (Zugriff 2026-10-14): größere Modelle befolgen Absichten nicht automatisch besser; drei Schritte (Demonstrationen für überwachte Feinabstimmung, Rangfolgen von Modellausgaben, RLHF); Ausgaben des 1,3-Mrd.-Modells gegenüber dem 175-Mrd.-Modell bevorzugt trotz 100-mal weniger Parametern; macht weiterhin einfache Fehler"
  - "Qwen Team: Qwen2.5 Technical Report (2024), arXiv:2412.15115. https://arxiv.org/abs/2412.15115 (Zugriff 2026-10-14): Vortraining von 7 auf 18 Billionen Tokens erweitert; Feinabstimmung mit über 1 Million Beispielen; mehrstufiges bestärkendes Lernen"
  - "Meta: Llama 3.1 Modellkarte. https://huggingface.co/meta-llama/Llama-3.1-8B (Zugriff 2026-10-14): ca. 15 Billionen Tokens öffentlich verfügbarer Daten, Datenstand Dezember 2023; Grafikkarten-Stunden (H100-80GB) 1,46 Mio. (8B), 7,0 Mio. (70B), 30,84 Mio. (405B), zusammen 39,3 Mio."
  - "Bai u. a.: Constitutional AI: Harmlessness from AI Feedback (2022), arXiv:2212.08073. https://arxiv.org/abs/2212.08073 (Zugriff 2026-10-14): einzige menschliche Aufsicht über eine Liste von Regeln oder Grundsätzen; überwachte Phase mit Selbstkritik und Überarbeitung; RL-Phase mit Präferenzen eines Modells (RLAIF)"
  - "Rafailov u. a.: Direct Preference Optimization (NeurIPS 2023), arXiv:2305.18290. https://arxiv.org/abs/2305.18290 (Zugriff 2026-10-14): Ausrichtung an Präferenzen mit einfacher Klassifikationsverlustfunktion, ohne separates Belohnungsmodell und ohne Ziehen aus dem Modell während der Feinabstimmung"
  - "Sharma u. a.: Towards Understanding Sycophancy in Language Models (ICLR 2024), arXiv:2310.13548. https://arxiv.org/abs/2310.13548 (Zugriff 2026-10-14): fünf führende Assistenten zeigen Sykophanz in vier Aufgaben; Antworten passend zur Nutzersicht in Präferenzdaten häufiger bevorzugt; Menschen und Präferenzmodelle ziehen überzeugend geschriebene gefällige Antworten in nicht vernachlässigbarem Anteil korrekten vor; menschliches Feedback als mögliche Ursache"
  - "OpenAI: GPT-4 Technical Report (2023), arXiv:2303.08774, Abschnitt 5 und Abbildung 8. https://arxiv.org/pdf/2303.08774 (Zugriff 2026-10-14): auf einer Teilmenge von MMLU (Auswahlantworten A bis D, Wahrscheinlichkeit der Antwortoption gegen Trefferquote) vortrainiertes Modell hoch kalibriert, nach dem Post-Training deutlich weniger (ECE 0,007 gegen 0,074)"
  - "Carlini u. a.: Extracting Training Data from Large Language Models (2020), arXiv:2012.07805. https://arxiv.org/abs/2012.07805 (Zugriff 2026-10-14): Hunderte wortgetreue Textstellen aus den Trainingsdaten von GPT-2 extrahiert, darunter personenbezogene Daten; größere Modelle anfälliger"
  - "Rechenbeispiel Abschnitt 2 am 2026-10-14 mit Python ausgeführt: -ln(0,526) = 0,64; -ln(0,236) = 1,44; -ln(0,117) = 2,15; -ln(0,0035) = 5,65; -ln(0,90) = 0,11 (Wahrscheinlichkeiten aus D4, ungerundet 0,526, 0,236, 0,117, Strom etwa 0,0035)"
  - "Eigene Artikel der Reihe: E1 (Training und Inferenz, kein Weiterlernen im Gespräch), E6 (Wissensstand), E7 (Daten und Einstellungen), A1 und A7 (eigener Test, Kontext und Zustimmungsneigung), A3 und A8 (Prüfen, Gegenargumente), A9 (Modell und Trainingsaufwand), D1 bis D4; Vorwärtsverweise auf D6, D7, D9, P7"
verifikation_offen:
  - "Verlust als negativer Logarithmus der Wahrscheinlichkeit des richtigen Tokens (Kreuzentropie) und Gradientenabstieg sind Lehrbuchwissen (W); im Text als 'verbreitete Wahl' formuliert, Optimierungsverfahren im Detail nicht beschrieben"
  - "Verhalten eines Basismodells (stellt weitere Fragen statt zu antworten) ist ein illustrierendes Beispiel (W), nicht an einem bestimmten Modell gemessen; im Text mit 'womöglich' formuliert"
  - "Schwerpunkt von Stufe 2 auf Anweisungsbefolgung, breites Wissensfundament aus dem Vortraining: verbreitete Einschätzung (W) ohne Einzelquelle; seit Runde 2 ausdrücklich offen formuliert, dass neues Wissen hinzukommen kann"
  - "'Einige wenige Gewichte starten mit festen Werten' (etwa Normalisierungsschichten mit Einsen und Nullen) ist Fachwissen (W)"
  - "Prägung von Höflichkeit, Struktur und Ablehnungen 'unter anderem' durch Stufe 2 und 3 ist Fachwissen (W) ohne Einzelquelle; seit Runde 3 mit Systemanweisungen und Einstellungen als weiteren Einflüssen"
  - "Kalibrierungsbefund stammt aus dem Bericht eines Herstellers zu einem Modell und ist nicht auf alle Modelle übertragbar"
  - "Herstellerangaben zu Tokenmengen und Rechenzeit nicht unabhängig prüfbar"
review_historie:
  - runde: 0
    datum: 2026-10-14
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial). InstructGPT, Qwen2.5-Bericht, Llama-3.1-Modellkarte, Constitutional AI, DPO, Sykophanz-Studie und GPT-4-Bericht an der Quelle gelesen. Verlustbeispiel ausgeführt, an die Werte aus D4 angebunden. Löst die Vorwärtsverweise aus D2, D3 und D4 ein."
  - runde: 1
    datum: 2026-10-14
    ergebnis: "Eigene Reviews (Fach und Stil): vier lange Sätze geteilt, man-Formulierung ersetzt, Stopp-Token-Satz entschärft (Stopp-Token gibt es auch im Vortraining), A7-Verweis auf den tatsächlichen Befund eingeengt. Programm erneut ausgeführt, Übungen nachgerechnet (Übung 1: Verlust über 1 unterhalb von etwa 0,37; Übung 2: rund 3.521 Jahre)."
  - runde: 2
    datum: 2026-10-14
    ergebnis: "Drei externe Reviews gegengeprüft (PyTorch-Doku, GPT-4-Bericht Abb. 8, Carlini u. a. 2020, Qwen2.5-Bericht). Übernommen: Gradientenrichtung korrigiert (Gradient zeigt den Anstieg, Schritt in Gegenrichtung, vor dem Schritt berechnet, Verlust gemittelt); drei Stufen als typisches Grundschema (Einleitung, Fazit); 'meisten Gewichte' statt 'alle'; 'negativer Logarithmus'; Dünger in die Schleife (2,15); Herstellerzahlen in Abschnitt 2 auf Größenordnung gestrafft, H100 in Box und Übung 2; Hinweis auf verschiedene Einheiten (Beispiele gegen Tokens); Stufe 2 kann Wissen ergänzen, Fehlgriff entsprechend umformuliert; Stopp-Token 'lernt, wann'; InstructGPT 'bei den untersuchten Anfragen'; Constitutional AI auf Harmlosigkeit begrenzt; Gefälligkeit als Hauptbegriff; Kalibrierungsbefund auf Test und Modell eingeengt; 'Kein verlässliches Nachschlagewerk' mit nachgewiesener Memorierung, Fehlgriff auf Nachschlagen bezogen; 'meist' zu 'unter anderem'; Übung 1 und 5 präzisiert; man-Formulierung ersetzt. Nicht übernommen: Begriff 'Sykophantie' (Gefälligkeit ist verständlicher, englischer Begriff genannt); Quellenrubrik und Links im Text (Reihenentscheidung 01.10.2026); Drei-Stufen-Tabelle (Fazit fasst bereits zusammen, Stilblatt: Tabellen nur für echte Vergleiche)."
  - runde: 3
    datum: 2026-10-14
    ergebnis: "Drei Re-Reviews, alle mit Freigabeempfehlung. Veröffentlichungsorte geprüft und im YAML ergänzt (InstructGPT NeurIPS 2022, DPO NeurIPS 2023, Sykophanz-Studie ICLR 2024). Übernommen: Fazit mit klarem Bezug 'das Modell' und Verlust als Wahrscheinlichkeit für das richtige Token; Mini-Batch und 'beim einfachen Gradientenabstieg' mit Hinweis auf verfeinerte Verfahren; 'mehrere zehn Millionen' statt 'zig'; Trainingsbeispiel offener beschrieben; Stopp-Token 'setzen soll'; 'reines Sprachmodell'; Vergleichen 'fällt meist leichter' statt 'gelingt fast immer'; DPO benannt, was entfällt und was bleibt; Ton und Form 'unter anderem' mit Systemanweisungen und Einstellungen; Gewichte im üblichen Chatbetrieb unverändert (Abschnitt 6 und Fazit); Datenstand nicht allein am Vortraining festgemacht; 'Nachtraining' statt 'Feedback-Training' beim Kalibrierungsbefund und im Fehlgriff (Quelle: post-training); Übung 1 als Herleitung mit Probe; Übung 4 mit gleichem Auftrag und nur wechselnder Vormeinung. Nicht übernommen: Gedankenstrich aus einem Formulierungsvorschlag (Stilblatt)."
  - runde: 4
    datum: 2026-10-14
    ergebnis: "Freigabe durch David am 2026-10-14 nach Runde 3. Kopfzeile und YAML-Status gemeinsam auf final. Offen bleiben die Punkte unter verifikation_offen (Herstellerangaben, Lehrbuchwissen ohne Einzelquelle)."
```