# KI-A6 · Texte, Dokumentation, Bewerbung: Entwürfe mit KI, Stimme von dir

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Aufbau-Track, Artikel A6 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du schreibst im Chat „Mach das professioneller" und fügst deinen Absatz über das Praktikum ein. Zurück kommt ein glatter Text mit Wörtern wie „umfassend" und „nahtlos". Beim zweiten Lesen merkst du, dass die Antwort zwei Dinge enthält, die du nie geschrieben hast: eine Zahl und eine Aufwertung, die niemand belegt hat. Der Text klingt gut, aber ein Teil davon ist nicht mehr deiner. Dieser Artikel zeigt, wie du Texte mit KI entwirfst und überarbeitest, ohne Fakten zu verlieren und ohne zu klingen wie alle anderen.

Am Ende kannst du eine Überarbeitung so beauftragen, dass nichts dazugedichtet wird, und du kannst das Ergebnis Wort für Wort gegen dein Original prüfen. Du gibst dem Chat-Assistenten deine Stimme mit, statt ihn raten zu lassen. Du erzeugst Dokumentation und prüfst, ob sie zum Code passt. Und du bereitest Bewerbungsunterlagen so vor, dass jede Aussage stimmt und von dir stammt.

Vorausgesetzt wird der Einsteiger-Track E1 bis E8, besonders E4 (Prompts), E6 (Halluzinationen) und E7 (Datenschutz). Aus dem Aufbau-Track helfen A2 (Kontext) und A3 (Recherche). Für Abschnitt 4 ist A5 nützlich, aber keine Pflicht.

---

## 1. Drei Rollen der KI beim Schreiben

Stell dir deinen Text als Beet vor. Du hast gesät, es wächst etwas, und du willst, dass es ordentlich aussieht. Ein Helfer mit Harke und Gießkanne ist dabei Gold wert. Ein Helfer, der auf eigene Faust pflanzt, bringt dir nach ein paar Wochen Dinge, die du nie bestellt hast. Der Lektor harkt, der Entwurfshelfer pflanzt, und der Sparringspartner geht das Beet mit dir durch und fragt, was du überhaupt anbauen willst. Das Bild hinkt an einer Stelle: Fremde Pflanzen fallen sofort auf, fremde Behauptungen in einem Absatz oft erst, wenn jemand nachfragt.

Daraus ergeben sich drei Rollen, die du dem Chat-Assistenten geben kannst.

- **Lektor:** Du lieferst den Text, das Werkzeug glättet ihn. Es soll Rechtschreibung, Satzbau und Wortwahl verbessern, kürzen und umordnen, ohne Inhalt oder Aussage zu verändern.
- **Sparringspartner:** Das Werkzeug stellt dir Fragen, du antwortest, und aus deinen Antworten entsteht das Material. Es schreibt noch nichts, es holt etwas aus dir heraus.
- **Entwurfshelfer:** Das Werkzeug schreibt eine erste Fassung aus Stichpunkten oder Material, das du mitgibst. Das spart Zeit, kostet aber am meisten Kontrolle.

Als Faustregel gilt: Je folgenreicher falsche oder dazugedichtete Angaben wären, desto näher bleibst du am Lektor. Eine Terminabsage an den Vermieter darf der Entwurfshelfer übernehmen. Dein Anschreiben und der Absatz über dein Abschlussprojekt gehören in die Rollen Lektor und Sparringspartner, weil dort jede Aussage später im Gespräch auf dich zurückfällt.

Dahinter steht ein Effekt, den eine Untersuchung gezeigt hat. Teilnehmende schrieben argumentative Texte, einmal mit und einmal ohne Vorschläge eines Sprachmodells. Bei einem Modell, das mit menschlichen Rückmeldungen nachtrainiert war, wurden die Texte einander ähnlicher, und die Angleichung kam von den Passagen, die das Modell geliefert hatte. Beim Basismodell ohne dieses Nachtraining zeigte sich das nicht. Ob das für heutige Modelle und andere Schreibaufgaben gilt, beantwortet die Untersuchung nicht. Sie zeigt aber, wie es laufen kann: Wer viele Formulierungen ungeprüft vom selben Modell übernimmt, nähert sich leicht dessen Standardton an.

---

## 2. Überarbeiten, ohne etwas zu verlieren

Zurück zum Praktikumsabsatz. Dein Original lautet so:

```text
Im Praktikum habe ich ein Skript geschrieben, das Logdateien auswertet. Dabei sparte das Team etwa 2 Stunden pro Woche.
```

Nach „Mach das professioneller" kommt zum Beispiel diese Fassung zurück:

```text
Im Praktikum entwickelte ich ein umfassendes Skript, das Logdateien nahtlos auswertet. Dabei sparte das Team über 5 Stunden pro Woche.
```

Beim schnellen Lesen fällt das kaum auf. Aus „etwa 2" ist „über 5" geworden, und aus einem Skript wurde ein „umfassendes" Skript. Die Zahlen sind für das Beispiel ausgedacht. Es geht darum, dass eine Zahl auftaucht, die nicht im Original steht, und dass „umfassend" eine Aufwertung ist, die dir niemand belegt hat. Solche Änderungen entstehen, weil ein Sprachmodell Texte so fortsetzt, wie sie wahrscheinlich weitergehen (E1, E6). Beeindruckender klingt eben besser.

Vier Gewohnheiten senken dieses Risiko.

**Eigenen Rohtext zuerst.** Schreib die erste Fassung selbst, auch wenn sie holprig ist. Sie hält die Fakten fest und gibt dem Werkzeug einen Anker. Alternativ reichen geprüfte Stichpunkte. Auch dann kann das Werkzeug beim Überarbeiten etwas verändern oder ergänzen, deshalb bleibt der Vergleich mit dem Original nötig (siehe unten). Wer mit „Schreib mir einen Absatz über mein Praktikum" beginnt, bekommt Fakten, die dem Werkzeug nie jemand gegeben hat.

**Enger Auftrag.** „Mach das professioneller" lässt alles offen. Besser ist ein Auftrag, der die Grenzen nennt:

```text
Überarbeite den Absatz unten sprachlich: Grammatik, Satzbau, Wortwahl.
Ändere keine Zahlen, Namen, Daten oder Zuständigkeiten.
Füge keine Aussagen hinzu, die im Original nicht stehen.
Wenn dir eine Angabe unklar ist, frag nach, statt sie zu ergänzen.
Gib danach eine Liste aller Stellen aus, an denen du inhaltlich etwas geändert hast.

Absatz:
[dein Text]
```

Die Liste am Ende hilft beim Prüfen, ersetzt den Vergleich mit dem Original aber nicht, denn das Werkzeug kann sich auch bei der Auskunft über die eigenen Änderungen irren. Deshalb gehört der nächste Punkt dazu.

**Original und Ergebnis vergleichen.** Verlass dich nicht auf dein Lesegefühl. Die meisten Textverarbeitungen haben eine Funktion, die zwei Fassungen vergleicht und Änderungen anzeigt. Ohne Programm geht es in der Shell, wenn Git installiert ist (A5):

```bash
git diff --no-index --word-diff original.txt ki.txt
```

Die Ausgabe zeigt Entferntes in `[-eckigen Klammern-]` und Neues in `{+geschweiften Klammern+}`:

```text
Im Praktikum [-habe-]{+entwickelte+} ich ein [-Skript geschrieben,-]{+umfassendes Skript,+} das Logdateien {+nahtlos+} auswertet. Dabei sparte das Team [-etwa 2-]{+über 5+} Stunden pro Woche.
```

Git beendet sich bei gefundenen Unterschieden mit dem Exit-Code 1 und bei gleichen Dateien mit 0. Der Code 1 ist hier also kein Fehler. Jetzt siehst du auf einen Blick, dass die Zahl sich geändert hat. Prüfe bei jeder Überarbeitung drei Dinge: Zahlen und Daten, Namen und Rollen, und jede Stelle, an der etwas dazugekommen ist, das ein Beleg bräuchte.

**Eine Grenze für die Runden setzen.** Jede weitere Runde kann dich ein Stück vom Original entfernen. Setz dir eine Obergrenze, zum Beispiel drei Runden. Prüfe dann, ob der Text noch besser geworden ist oder nur glatter klingt. Im zweiten Fall nimm die beste Fassung, ändere den Rest von Hand und lass es dabei.

---

## 3. Die eigene Stimme behalten

Du hast zwei Mails an dieselbe Person geschrieben, eine selbst und eine mit Hilfe des Chat-Assistenten. Die Person fragt zurück: „Hast du die zweite von jemand anderem schreiben lassen?" Das passiert, wenn der Ton plötzlich wechselt. Dagegen helfen zwei Dinge, die du dem Werkzeug mitgibst.

**Eine Stilprobe.** Gib zwei bis drei Absätze mit, die du selbst geschrieben hast und die nach dir klingen (Beispiele im Prompt, E4, A2). Dazu ein Satz: „Der Ton in der Probe ist das Ziel. Übernimm Satzlänge und Wortwahl." Das wirkt stärker als jede Beschreibung wie „freundlich, aber sachlich".

**Die Stimme in Regeln.** Notiere, was zu dir gehört und was nicht. Zum Beispiel: kurze Sätze, du statt Sie, keine Ausrufezeichen, keine Wörter wie „nahtlos" oder „ganzheitlich". Verbote funktionieren besser mit Begründung: „Keine Floskeln, weil der Leser sie sofort überliest." Wie du solche Regeln als Vorlage speicherst und immer wieder einsetzt, ist Thema von A7. Bis dahin hilft eine Textdatei, in der du den engen Auftrag und deine Stilregeln zum Einkopieren aufbewahrst.

Bleibt die Frage, ob sich KI-Texte erkennen lassen. Die Untersuchungen dazu zeichnen ein vorsichtiges Bild, das an Textsorte und Zeitpunkt hängt.

- **Menschen:** In einer Untersuchung zu Selbstdarstellungstexten wie Profilen konnten Teilnehmende KI-Texte nicht zuverlässig von menschlichen unterscheiden, und ihre Faustregeln dafür führten häufig in die Irre.
- **Erkennungsprogramme, 2023:** Programme dieser Art stuften in einer Untersuchung englische Texte von Menschen mit Englisch als Fremdsprache auffällig oft fälschlich als KI-Text ein. Ob das für Deutsch genauso gilt, sagt die Untersuchung nicht.
- **Erkennungsprogramme, 2026:** Eine neuere Untersuchung testete vier Programme an Dokumenten mit bekanntem KI-Anteil. Die Trefferquoten unterschieden sich stark zwischen den Programmen, besonders bei gemischten und umformulierten KI-Texten lagen mehrere weit daneben, während ein Programm deutlich besser abschnitt. Die Autoren raten, ein Ergebnis höchstens als ersten Hinweis zu nutzen. Untersucht wurden englischsprachige wissenschaftliche Arbeiten, daraus lässt sich nichts Direktes über deutsche Bewerbungsanschreiben ableiten.

Aus Stilmerkmalen oder einem einzelnen Erkennungsergebnis lässt sich eine KI-Beteiligung also nicht zuverlässig feststellen. Im Gespräch können sich dagegen erfundene oder übertriebene Aussagen zeigen, wenn du sie nicht erklären kannst.

Aus der Praxis kennen viele trotzdem typische Spuren: gleichförmige Absatzlängen, Dreierlisten, auffällig viele große Wörter und Sätze, die Gewicht behaupten, ohne etwas zu sagen. Das ist eine Beobachtung ohne verlässliche Messung. Nutze sie als Hinweis für deine eigene Durchsicht. Einzelne Stilmerkmale sind kein Beweis für KI, denn auch Menschen schreiben so.

Der sicherere Maßstab liegt bei dir. Kannst du jede wichtige Aussage erklären und, wo nötig, belegen? Passt der Umfang der KI-Hilfe zu den Regeln des Zusammenhangs, in dem der Text landet? Eine rein sprachliche Überarbeitung ist etwas anderes als ein Entwurf, den das Werkzeug geschrieben hat, und manche Schulen, Betriebe und Plattformen verlangen dazu Angaben (Abschnitt 5, R6).

---

## 4. Dokumentation: Was sie beantwortet

Du schickst dein erstes Projekt in die Welt, und die README sagt: „Das Skript verarbeitet Daten effizient." Ein Leser, der das Projekt zum ersten Mal sieht, weiß danach nichts. Welche Daten? Wie startet er das Skript? Was passiert, wenn eine Datei fehlt?

Gute Dokumentation beantwortet drei Fragen: Was macht das Projekt? Wie benutze ich es? Und warum ist es so gebaut? Wie der Code im Einzelnen arbeitet, lässt sich bei lesbarem Code am Code selbst ablesen. Dokumentation liefert, was der Code nicht beantwortet. Ein Chat-Assistent kann dabei helfen, und zwar an vier Stellen:

- **Gerüst:** Abschnitte einer README anlegen, etwa Zweck, Installation, Beispielaufruf, bekannte Grenzen.
- **Docstrings und Kommentare:** Entwürfe aus einer Funktion.
- **Änderungsliste:** aus einer Folge von Git-Commits eine lesbare Zusammenfassung bauen.
- **Verständlichkeit:** Eine README gegenlesen lassen. „Was würde ein Neuling hier nicht verstehen?" ist eine gute Frage.

Die Risiken kennst du aus E6 und A5. Das Werkzeug beschreibt oft die Absicht statt des Verhaltens, erfindet Optionen, die es gar nicht gibt, und die Dokumentation veraltet, sobald sich der Code ändert. Ein Beispiel aus A5, Abschnitt 5:

```python
# rabatt.py
def preis_mit_rabatt(preis):
    if preis > 100:
        return preis * 0.9
    return preis
```

Das Werkzeug liefert dazu diesen Docstring:

```python
"""Gibt den Preis nach Rabatt zurück: ab 100 Euro 10 Prozent weniger."""
```

Das klingt richtig, ist aber falsch. Der Code gibt den Rabatt erst für Preise über 100. Bei genau 100 Euro bleibt der Preis unverändert. Der Docstring beschreibt, was die Funktion tun soll, nicht was sie tut. Ob der Code oder der Text der Fehler ist, entscheidest du anhand der Anforderung. Gilt „über 100 Euro", passt der Code, und der Docstring muss lauten: „Gibt den Preis zurück; für Preise über 100 Euro 10 Prozent weniger, bei genau 100 Euro unverändert." Gilt „ab 100 Euro", bleibt der Docstring und der Code bekommt `>=` (A5).

Zwei Prüfungen gehören deshalb zu jeder KI-Dokumentation:

1. **Docstrings gegen den Code lesen**, besonders an Grenzen: ab oder über, mindestens oder höchstens, leer oder fehlend.
2. **Jeden für die Nutzung nötigen Befehl aus der README ausführen**, in einer frischen oder geschützten Umgebung (A5, Abschnitt 4). Befehle mit möglichen Nebenwirkungen wie Löschen oder Überschreiben verstehst du vorher. Was nicht läuft, ist entweder falsch dokumentiert oder setzt eine Voraussetzung voraus, die in der Dokumentation fehlt.

Bei Dokumentation, die als Prüfungsleistung zählt, gelten die Regeln deines Ausbilders oder deiner Schule. Welche Angaben dort zur KI-Nutzung verlangt werden, klärst du vorher (R6).

---

## 5. Bewerbung: Material zuerst

Du sitzt vor einer Stellenanzeige und willst das Anschreiben „einmal schnell" erzeugen lassen. Ein solcher Entwurf kann freundlich und fehlerfrei klingen und trotzdem austauschbar bleiben. Dazu kommt das Risiko, dass das Werkzeug Erfahrungen ergänzt, die du nicht hast. In einer repräsentativen Umfrage eines Branchenverbands unter 602 Unternehmen ab drei Beschäftigten gaben 2026 rund 12 Prozent an, KI im Bewerbungsprozess einzusetzen. Etwa 6 Prozent nutzten sie schon zur ersten Sichtung der Unterlagen. Die Umfrage erfasst, was Unternehmen tun, und sagt über die Wirkung auf Bewerbungen oder über deine Chancen nichts. Sie zeigt, dass auf der anderen Seite ebenfalls Werkzeuge mitlaufen können.

Besser ist diese Reihenfolge: erst eigenes Material sammeln, dann entwerfen lassen, danach jede Aussage prüfen. Daraus werden vier Schritte.

**Material sammeln.** Schreib in Stichpunkten auf, was du getan hast: Stationen, Projekte, Aufgaben, Ergebnisse, Belege (Zeugnis, Repository, Zertifikat). Das ist das Rohmaterial, und es gehört dir. Hier hilft der Sparringspartner. Du kannst ihn bitten, dich zu interviewen:

```text
Ich bewerbe mich um einen Praktikumsplatz in der Anwendungsentwicklung.
Stell mir einzeln Fragen zu meinem Praktikum und meinem Abschlussprojekt,
eine Frage pro Nachricht. Bohr nach, wenn eine Antwort vage bleibt.
Ergänze nichts, ich schreibe danach selbst.
```

**Entwurf nur aus deinem Material.** Gib das Material mit der Stellenanzeige in den Chat. Der Auftrag lautet: „Schreibe einen Entwurf. Verwende nur Informationen aus meinem Material. Erfinde nichts. Markiere Lücken mit [LÜCKE] statt sie zu füllen." Für den Entwurf reichen Platzhalter statt Anschrift, Telefonnummer und Geburtsdatum, die echten Angaben trägst du zum Schluss selbst ein. Ob und welche personenbezogenen Daten du in einen Dienst eingeben darfst, hängt vom Dienst und den geltenden Vorgaben ab (E7).

**Den betriebsspezifischen Teil selbst schreiben.** Der Absatz, warum du genau zu diesem Betrieb willst, braucht Recherche (A3). Ein Werkzeug ohne Zugriff auf aktuelle Quellen füllt ihn mit Allgemeinplätzen oder erfindet Details über den Betrieb.

**Jede wichtige Aussage vertreten können.** Geh den fertigen Text Satz für Satz durch und frag dich: Kann ich das im Gespräch erklären? Habe ich einen Beleg? Das gilt besonders für Werkzeuge und Fähigkeiten, die in der Unterlage stehen. Wer „fundierte Kenntnisse in X" schreibt, wird im Gespräch zu X gefragt. Behaupte nichts, was du im Gespräch nicht vertreten kannst.

Zur Offenlegung: Ob und wie du den Einsatz von KI angibst, regeln manche Betriebe, Schulen und Plattformen verschieden. Frag nach, wenn du unsicher bist (R6). Für Texte, die du veröffentlichst oder weitergibst, kommt die Frage nach Urheberrecht und Kennzeichnung dazu (R5).

---

## Häufige Fehlgriffe

- **Eine Überarbeitung ungeprüft übernehmen.** Das Ergebnis klingt besser, und genau deshalb liest du weniger genau. Vergleiche mit dem Original (Abschnitt 2).
- **Mit „Schreib mir einen Text über mich" beginnen.** Ohne dein Material füllt das Werkzeug die Lücken mit Wahrscheinlichem. Erst Rohtext oder Stichpunkte, dann Hilfe.
- **Zu viele Runden.** Irgendwann wird der Text glatter, aber kaum besser, und er entfernt sich von deinem Original. Zurück zur besten Fassung und von Hand weiter.
- **Die Stimme nur beschreiben.** „Locker und professionell" sagt wenig. Eine echte Probe von dir sagt mehr.
- **KI-Erkennung als Beweis nehmen.** Weder ein Erkennungsprogramm noch dein Bauchgefühl liefert ein sicheres Urteil (Abschnitt 3). Es zählen Belege.
- **Docstring und README glauben.** Dokumentation aus dem Werkzeug beschreibt oft, was gemeint war. Lies sie gegen den Code und führe die nötigen Befehle geschützt aus (Abschnitt 4).
- **Personenbezogene Daten im Prompt.** Ob Anschrift, Geburtsdatum und Kontaktdaten in den Dienst dürfen, hängt von Dienst und Vorgaben ab (E7). Für Entwürfe reichen Platzhalter.
- **Fähigkeiten behaupten, die nicht da sind.** Das Werkzeug schreibt „fundierte Erfahrung", wenn du „einmal ausprobiert" gemeint hast. Frag dich bei jedem Satz, ob du ihn im Gespräch halten kannst.

---

## Zum Ausprobieren

1. Schreib einen Absatz über ein Projekt oder Praktikum von dir, mit mindestens einer Zahl, einem Namen und einem Datum. Lass ihn mit dem Auftrag aus Abschnitt 2 überarbeiten und vergleiche beide Fassungen mit einer Änderungsanzeige. Notiere jede inhaltliche Abweichung.
2. Gib dem Werkzeug zwei eigene Absätze als Stilprobe und lass einen dritten Text in diesem Ton überarbeiten. Lies das Ergebnis laut vor. Wo klingt es nicht nach dir? Ergänze eine Regel, die das künftig verhindert.
3. Lass dir für eine kleine Funktion von dir einen Docstring schreiben. Prüfe jede Aussage gegen den Code, besonders die Grenzfälle. Notiere, was nicht stimmt.
4. Lass dir eine README für ein Übungsprojekt entwerfen. Führe jeden für die Nutzung nötigen Befehl darin selbst aus, in einer frischen oder geschützten Umgebung. Markiere, was nicht funktioniert.
5. Sammle Stichpunkte für eine Bewerbung und lass dich vom Chat-Assistenten interviewen. Schreib danach die erste Fassung selbst. Gib sie zur Überarbeitung mit dem engen Auftrag ab und prüfe jede wichtige Aussage: im Gespräch erklärbar, Beleg vorhanden, wo nötig?

Am Ende hast du eine Arbeitsweise für Texte, bei der das Werkzeug glättet und fragt, während Fakten und Stimme bei dir bleiben.

---

## Fazit

Bei Texten mit KI zählen drei Fragen. Kann ich jede wichtige Aussage erklären und, wo nötig, belegen? Habe ich das Ergebnis gegen das Original verglichen? Passt der Umfang der KI-Hilfe zu den Regeln des Zusammenhangs, in dem der Text landet? Gib dem Werkzeug deinen Rohtext, eine Stilprobe und einen engen Auftrag, und behalte Zahlen, Namen und Aussagen in der Hand. Dokumentation prüfst du wie Code: lesen und ausführen. Bei Bewerbungen kommt erst das Material, dann der Entwurf. Als Nächstes geht es in A7 darum, wie du Anweisungen und Stilregeln als Vorlagen speicherst, damit du sie nicht jedes Mal neu schreiben musst.

```yaml
dokument: ki-a6-texte-dokumentation-bewerbung
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-08
quellen_fachlich:
  - "Padmakumar, He: Does Writing with Language Models Reduce Content Diversity? arXiv:2309.05196, ICLR 2024. https://arxiv.org/abs/2309.05196 (Abstract gelesen, 2026-10-08): argumentative Essays mit GPT3, InstructGPT oder ohne Modell; statistisch signifikante Verringerung der Vielfalt nur mit InstructGPT, nicht mit GPT3; Effekt geht auf die von InstructGPT beigesteuerten Textteile zurück, nicht auf die der Schreibenden. Teilnehmerzahl im Abstract nicht genannt und im Text nicht verwendet"
  - "Jakesch, French, Ma, Hancock, Naaman: Human heuristics for AI-generated language are flawed. PNAS 2023, arXiv:2206.07271, DOI 10.1073/pnas.2208839120: sechs Experimente, 4.600 Teilnehmende, Selbstdarstellungstexte, Menschen unterscheiden KI- und Menschentexte nicht verlässlich, ihre Faustregeln sind fehlerhaft"
  - "Liang, Yuksekgonul, Mao, Wu, Zou: GPT detectors are biased against non-native English writers. Patterns 2023, arXiv:2304.02819: Detektoren stufen Texte von Nicht-Muttersprachlern häufiger fälschlich als KI-Text ein (Zahlen im Text nicht verwendet)"
  - "Bitkom: Pressemitteilung vom 2026-09-28 zu KI im Bewerbungsprozess. https://www.bitkom.org/Presse/Presseinformation/Fuehrt-kuenftig-KI-Bewerbungsgespraech (Zugriff 2026-10-08): 602 Unternehmen ab 3 Beschäftigten in Deutschland, telefonisch, repräsentativ, KW 18 bis 25/2026; 12 % nutzen KI im Bewerbungsprozess, 6 % für die erste Sichtung eingehender Bewerbungen, 9 % für Stellenanzeigen; keine Angaben zur KI-Nutzung durch Bewerbende"
  - "Van Vlasselaer, Van Droogenbroeck, Spruyt: Who wrote this? Evaluating the reliability of AI detection tools in higher education. International Journal for Educational Integrity 22, Art. 16 (online 2026-06-29), DOI 10.1007/s40979-026-00226-w (Zugriff 2026-10-08, Seitentext bis Zeichen 100.000 von 100.597 gelesen): vier Detektoren (GPTZero, Pangram, Copyleaks, Turnitin), 160 synthetische Dokumente zu je 40 menschlich, vollständig KI, hybrid, humanisiert; große Unterschiede zwischen Programmen, Pangram klar am besten; Autoren: Ergebnisse nicht als alleinigen Beleg bei folgenreichen Entscheidungen verwenden. Zahlen im Text nicht verwendet"
  - "Beispiel Praktikumsabsatz in Abschnitt 2: Befehl git diff --no-index --word-diff am 2026-10-08 mit Git ausgeführt, Ausgabe im Text unverändert wiedergegeben; Exit-Code 1 bei Unterschieden und 0 bei gleichen Dateien getestet"
  - "Eigene Artikel der Reihe: E1, E4, E6, E7, A2, A3, A5 (Rabatt-Beispiel, Abschnitte 4 und 5); Vorwärtsverweise auf A7, R5, R6"
verifikation_offen:
  - "Typische KI-Stilspuren (gleichförmige Absätze, Dreierlisten, große Wörter, leere Gewichtungssätze) sind eine Praxisbeobachtung ohne Einzelquelle; die Wikipedia-Seite 'Signs of AI writing' war nicht abrufbar und wurde nicht herangezogen"
  - "Padmakumar und He: Effekt nur bei einem Modell (InstructGPT), nicht beim Basismodell; Übertragbarkeit auf aktuelle Modelle und andere Schreibaufgaben offen, im Text ausdrücklich so benannt. Die in einem Review genannte Zahl von 38 Teilnehmenden (Upwork) steht nicht im Abstract und wurde nicht übernommen"
  - "Bitkom-Zahlen sind eine Unternehmensbefragung zur Nutzung, keine Aussage zur Wirkung auf Bewerbungen; der Verband wird im Fließtext nach Reihenregel nicht namentlich genannt"
  - "Regeln zur Kennzeichnung von KI-Nutzung beim jeweiligen Bildungsträger sind nicht geprüft; der Text verweist allgemein auf Nachfrage und R6"
  - "Faustregeln (Rohtext zuerst, Rundengrenze zum Beispiel drei, Stilprobe mit zwei bis drei Absätzen) sind didaktische Empfehlungen ohne Einzelquelle"
  - "Van Vlasselaer et al. 2026: letzte 597 Zeichen der Seite nicht gelesen; die Studie widerspricht sich intern bei Falsch-Positiv-Raten (Tabelle: alle 40 menschlichen Texte korrekt, Text: geringe Rate bei einem Programm); zudem Korrektur zur Arbeit am 2026-10-06 veröffentlicht, Inhalt nicht geprüft. Deshalb im Text nur qualitative Aussagen. Stichprobe synthetisch; Methodik: 160 englischsprachige wissenschaftliche Arbeiten (mindestens 4.000 Wörter), menschliche Texte von nicht-muttersprachlichen Masterstudierenden, 1.163 Masterarbeiten (Sprache nicht angegeben, nur mit einem Programm geprüft). Korrektur vom 2026-10-06 (DOI 10.1007/s40979-026-00236-8) konnte nicht abgerufen werden (Abruf abgelehnt), Inhalt offen"
  - "Vorwärtsverweise A7, R5, R6 beim Anlegen dieser Artikel abgleichen; der frühere Rechtshinweis zu falschen Angaben in Bewerbungen wurde gestrichen (ohne Quelle, nicht nötig für die Lernbotschaft)"
review_historie:
  - runde: 0
    datum: 2026-10-08
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial) nach Websuche zu Studien über Schreiben mit Sprachmodellen, Erkennbarkeit von KI-Texten und Bitkom-Umfrage 2026. Word-Diff-Beispiel ausgeführt. Externe Reviews stehen aus."
  - runde: 1
    datum: 2026-10-08
    ergebnis: "Drei externe Reviews gegen Quellen und Lauf geprüft (Padmakumar-Abstract, Bitkom-Seite, Springer-Studie 2026, git-Exit-Code). Übernommen: Fazit und Abschnitt 3 ohne 'dein Text' als Kriterium, Studienaussagen eng an die untersuchten Bedingungen gebunden, neue Quelle zu Erkennungsprogrammen 2026, Rohtext-Satz abgeschwächt, Rundengrenze als Faustregel, Datenschutzsatz relativiert, Rechtssatz gestrichen, Befehle nur nötige und mit Vorsicht, Personaler-Satz neutralisiert, Exit-Code-Hinweis, korrigierter Docstring, Was-Wie-Warum, Kopiervorlage bis A7. Nicht übernommen: Produktnamen im Fließtext (Reihenregel), Barrierefreiheitssatz (außerhalb des Umfangs), Bitkom-Zeile mit 'Struktur für maschinelle Sichtung' (unbelegt), Umbau der Beet-Metapher (nur Rollenzuordnung ergänzt)."
  - runde: 2
    datum: 2026-10-08
    ergebnis: "Drei Re-Reviews geprüft; Sprache der 160 Dokumente (Englisch, wissenschaftlich) an der Studienseite bestätigt, Korrektur nicht abrufbar. Übernommen: Einstieg 'Zahl und Aufwertung' (Widerspruch zum Beispiel behoben), Lektor als Auftrag statt Garantie, 'senken dieses Risiko', Effekt statt Risiko, Sparringspartner aktiver, Bild-Satz gekürzt, Reichweite der Erkennungsstudie (englische Arbeiten) benannt, Aussage zur Erkennung auf Stilmerkmale und Einzelergebnisse begrenzt, Gespräch 'kann sich zeigen', 'wichtige Aussage erklären und, wo nötig, belegen', README-Fehlschlag mit fehlender Voraussetzung, geschlechtsneutrales Bewerbungsbeispiel (Praktikumsplatz). Nicht übernommen: Zusammenlegen der beiden Erkennungs-Punkte (Chronologie bleibt), Schritt 3 als Unterpunkt (Reihenfolge bleibt), Barrierefreiheit (außerhalb des Umfangs). Offen: Inhalt der Korrektur zur Studie, Vorwärtsverweise A7, R5, R6."
  - runde: 3
    datum: 2026-10-08
    ergebnis: "Freigabe durch David am 2026-10-08. Kopfzeile und YAML-Status gemeinsam auf final gesetzt. Von der Korrektur zur Erkennungsstudie ist nur bekannt, dass sie am 2026-10-06 erschien (DOI 10.1007/s40979-026-00236-8); der Inhalt blieb unlesbar. Der Text nutzt aus der Studie nur qualitative Aussagen, die Prüfung bleibt in verifikation_offen."
```