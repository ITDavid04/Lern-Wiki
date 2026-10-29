# KI-E4 · Gutes Prompten

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Einsteiger-Track, Artikel E4 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Manche Antworten passen nicht zu dem, was du brauchtest. Oft fehlt der Eingabe dann etwas. Ein **Prompt** ist die Eingabe, mit der du einem Sprachmodell eine Aufgabe stellst: die Frage, mitgegebene Texte, Beispiele und Vorgaben zum Format. Die Qualität der Antwort hängt stark davon ab, wie vollständig und klar diese Eingabe ist. Dieser Artikel zeigt fünf Bausteine, die fast jeden Prompt besser machen, ein paar weitere Hebel und ein Beispiel, in dem ein schwacher Prompt in drei Schritten verbessert wird.

Vorausgesetzt werden E1 bis E3, insbesondere das Gespräch als Arbeitsform aus E3. Dort ging es darum, *wie du im Verlauf nachsteuerst*. Hier geht es darum, *wie die einzelne Anfrage von Anfang an besser wird*. Beides ergänzt sich: Ein guter Prompt spart Runden, ersetzt aber das Nachfragen nicht.

---

## 1. Warum die Formulierung zählt

Stell dir vor, du sagst einem neuen Mitarbeiter in der Gärtnerei: „Mach mal die Beete fertig." Damit bleibt alles offen. „Bis Freitag die drei Südbeete jäten, den Boden lockern und eine Schicht Kompost aufbringen, Handarbeit, keine Fräse" lässt sich dagegen ausführen. Mit Prompts ist es nicht anders.

Ein Sprachmodell greift zwar auf Muster und Wissen aus dem Training zurück, kennt aber die konkrete Situation nur, soweit sie im Kontext steht (siehe E3), und kann nicht in deinen Kopf schauen. Fehlen Ziel, Zielgruppe oder Format, rät es, was gemeint sein könnte. Das Ergebnis ist dann meist ein Durchschnitt, der selten genau passt.

Ein hilfreiches Gedankenexperiment, das etwa in der Anleitung eines großen Anbieters auftaucht: Stell dir einen **neuen Kollegen** vor, der fachlich fit ist, aber nichts von der Situation weiß. Würde er mit deinem Prompt als Arbeitsauftrag klarkommen, oder müsste er dreimal nachfragen? Wenn er nachfragen müsste, fehlt dem Prompt etwas.

---

## 2. Fünf Bausteine

Nicht jeder Prompt braucht alle fünf. Für einfache Faktenfragen reicht ein Satz. Je komplexer die Aufgabe, desto mehr lohnt es sich, die Bausteine durchzugehen.

- **Ziel:** Was soll am Ende dastehen, und wofür brauchst du es? Beispiel: „Ich brauche eine Erklärung, mit der ich morgen einem Kollegen DNS in zwei Minuten erklären kann."
- **Kontext:** Was muss das Modell über die Situation und die Zielgruppe wissen? Beispiel: „Ich bin in der Umschulung zum Fachinformatiker, kenne IP-Adressen, aber noch keine Namensauflösung."
- **Rolle / Perspektive:** Aus welchem Blickwinkel soll geantwortet oder bewertet werden? Beispiel: „Bewerte meinen Entwurf aus Sicht eines geduldigen Ausbilders."
- **Format:** Wie soll die Antwort aussehen? Beispiel: „Erkläre es in höchstens 150 Wörtern und füge danach eine Tabelle mit drei Begriffen hinzu."
- **Beispiele:** Wie sieht ein gutes Ergebnis aus? Gib ein oder mehrere Beispiele, die Ton, Aufbau und Länge zeigen.

### Ziel und Kontext

Diese beiden Bausteine bringen nach verbreiteter Erfahrung oft den größten Gewinn. Das Ziel legt fest, *wofür* die Antwort gebraucht wird, der Kontext, *auf welcher Basis*. Hilfreich ist auch, **Hintergrund oder Grund** zu nennen, statt nur Verbote auszusprechen: „Der Text wird vorgelesen, daher keine Tabellen und Aufzählungszeichen" ist für ein Modell leichter zu befolgen als ein bloßes „Keine Tabellen". Auch die Anleitung eines Anbieters empfiehlt ausdrücklich, Begründung und Rahmenbedingungen mitzugeben.

### Rolle oder Perspektive

Eine Rolle wie „Du bist ein erfahrener Netzwerkadministrator" wird oft empfohlen und kann **Ton, Fachsprache und Blickwinkel** beeinflussen. Ein Wundermittel für Richtigkeit ist sie nicht. Eine Untersuchung (Preprint 2023, veröffentlicht 2024) testete 162 Personas an gut 2.400 Faktenfragen und mehreren Modellfamilien. Sie fand im Mittel keine bessere Genauigkeit, wenn eine Persona im System-Prompt stand. Die Wirkung hing von Persona und Fachgebiet ab und ließ sich schwer vorhersagen.

Sinnvoll ist eine Rolle deshalb vor allem dort, wo es um **Ton und Blickwinkel** geht („kritischer Reviewer", „geduldiger Ausbilder"), weniger als Versprechen, dass die Antwort dadurch fachlich korrekter wird. Die Zielgruppe („für Berufseinsteiger") nennst du besser direkt im Kontext.

### Format

Wenn du das Format nicht nennst, bekommst du das Format, das das Modell für üblich hält. Hilfreich sind Angaben zu **Länge**, **Struktur** (Fließtext, Tabelle, Schritte, Stichpunkte) und **Aufbau** (zuerst das Ergebnis, dann die Begründung). Dabei hilft es oft, **konkret zu sagen, was du haben möchtest** („Schreibe in zusammenhängenden Absätzen"), statt nur zu sagen, was du nicht möchtest („Keine Listen"). Klare Verbote sind trotzdem legitim, wichtig ist, dass die Anweisung eindeutig ist.

### Beispiele

Ein oder mehrere Beispiele zeigen oft schneller als jede Beschreibung, was gemeint ist. Die Technik heißt **Few-Shot-Prompting** (im Gegensatz zum Zero-Shot ohne Beispiel). Die Anleitungen mehrerer Anbieter empfehlen passende und möglichst vielfältige Beispiele als besonders hilfreiches Mittel, um Format, Ton und Struktur vorzugeben.

Zwei Dinge sind dabei zu beachten: Beispiele sollten **verschiedene Fälle** abdecken, sonst kopiert das Modell Länge und Wortwahl des einen Beispiels zu eng. Und sie sollten **dem echten Einsatz ähneln**.

---

## 3. Weitere Hebel

- **Anweisung und Material trennen.** Wenn du einen Text mitgibst, grenze ihn klar von der Aufgabe ab, etwa durch Überschriften, Trennlinien oder Markierungen wie „Text:" und „Aufgabe:". Das macht Verwechslungen weniger wahrscheinlich. Eine vollständige Sicherheitsmaßnahme ist es nicht (mehr dazu in R3).
- **Reihenfolge bei langen Texten.** Bei langen, dokumentreichen Eingaben empfiehlt die Anleitung eines Anbieters, die Dokumente an den Anfang zu setzen und die eigentliche Frage ans Ende. Das ist eine herstellerseitige Erfahrung, die sich bei eigenen Aufgaben leicht ausprobieren lässt.
- **Schrittfolge nennen.** Wenn die Reihenfolge zählt, nummerierst du die Schritte: „1. Fasse zusammen, 2. nenne drei Schwächen, 3. schlage Verbesserungen vor."
- **Unsicherheit erlauben.** Der Satz „Wenn du etwas nicht sicher weißt, sag das ausdrücklich, statt zu raten" kann erzwungene Antworten verringern. Er ersetzt aber keine Prüfung (mehr in E6).
- **Aufgaben aufteilen.** Eine große Aufgabe lässt sich oft besser in mehrere Prompts zerlegen, deren Ergebnisse du nacheinander verwendest, als in einem einzigen riesigen Prompt.
- **Auf das Modell achten.** Hersteller empfehlen für verschiedene Modelltypen unterschiedliche Stile. Modelle, die direkt auf Anweisungen reagieren, profitieren oft von präzisen Vorgaben. Sogenannte Reasoning-Modelle (Modelle, die vor der Antwort ausführlicher „nachdenken", mehr dazu in D7) profitieren eher von einem klaren Ziel und weniger Mikro-Vorgaben. Ob „Denke Schritt für Schritt" noch hilft, hängt deshalb vom Modell ab. Bei Reasoning-Modellen halten Anbieter es teils für überflüssig.

---

## 4. Beispiel: Ein schwacher Prompt in drei Verbesserungen

Ausgangslage: Du möchtest verstehen, was DNS ist.

- **Stufe 0:** „Erkläre DNS." Ausgangspunkt: Ziel, Niveau, Format und Umfang bleiben offen.
- **Stufe 1:** „Erkläre DNS für jemanden, der IP-Adressen kennt, aber noch nie von Namensauflösung gehört hat. Ich lerne für die Umschulung zum Fachinformatiker." Verbessert: **Kontext und Zielgruppe**.
- **Stufe 2:** Wie Stufe 1, dazu: „Ich brauche eine Erklärung, mit der ich das einem Kollegen in zwei Minuten erklären kann. Erkläre es in höchstens 150 Wörtern. Füge anschließend eine Tabelle mit den drei wichtigsten Begriffen hinzu." Verbessert: **Ziel, Länge, Format**.
- **Stufe 3:** Wie Stufe 2, dazu: „Ein Einstieg, der mir gefällt: ‚Ein Domainname ist wie ein Name im Adressbuch; DNS findet die passende IP-Adresse dazu.' Wenn du bei einem Punkt nicht sicher bist, kennzeichne das." Verbessert: **Beispiel und Umgang mit Unsicherheit**.

Stufe 3 muss nicht „perfekt" sein. Auf die Richtung kommt es an: Jede Stufe beantwortet eine Frage, die das Modell sonst raten müsste. Auch Stufe 3 ist ein Startpunkt, den du im Gespräch weiter anpasst (siehe E3). Die Antwort selbst musst du weiterhin prüfen, etwa gegen dein eigenes Lernmaterial.

---

## 5. Wenn der Prompt nicht das Problem ist

Ein besserer Prompt hilft nur, soweit die Ursache in der Anfrage liegt. Er löst nicht:

- **Fehlendes Wissen im Modell oder veraltete Informationen.** Hier hilft eine Quelle oder ein Dokument, das du selbst mitgibst, oder ein Werkzeug mit Websuche (siehe E2).
- **Erfundene Details.** Auch ein sorgfältiger Prompt kann Fehler nicht ausschließen. Prüfen bleibt nötig (E6).
- **Aufgaben, die das Werkzeug gar nicht kann.** Dann ist der Werkzeugtyp falsch gewählt (E2).

Hilfreich ist auch, **Prompts zu testen statt zu glauben**: Probiere dieselbe Aufgabe mit zwei Varianten aus und vergleiche die Antworten. Die Hersteller-Anleitungen empfehlen, vorab festzulegen, woran man ein gutes Ergebnis erkennt, und danach zu testen.

### Zusatz: Was „Loopen" bedeutet

Stell dir einen Code-Assistenten vor, der einen Fehler beheben soll. Er liest die Datei, ändert den Code, startet die Tests, sieht, dass ein Test fehlschlägt, ändert erneut und testet wieder. Jede Runde nutzt das Ergebnis der vorigen. Beim normalen Chat dagegen steuerst du jede Runde selbst, wie in E3 und in den Stufen aus Abschnitt 4.

Das nennt man bei KI-Werkzeugen meist **Loopen** (von englisch *loop*, Schleife): Das Werkzeug beantwortet eine Aufgabe nicht in einem Schritt, sondern arbeitet **in einer Schleife selbstständig wiederholt**. Es plant einen Schritt, führt ihn aus (etwa eine Suche, einen Programmlauf oder einen Dateizugriff), schaut sich das Ergebnis an und entscheidet dann, was als Nächstes kommt. Das wiederholt sich, bis die Aufgabe erledigt ist oder eine Grenze erreicht wird. Anbieter beschreiben Agenten (siehe E2) sinngemäß als Sprachmodelle, die auf Basis von Rückmeldungen aus ihrer Umgebung Werkzeuge in einer Schleife nutzen.

Für den Prompt hat das drei Folgen:

- **Ziel und Fertig-Kriterium angeben.** Eine Schleife braucht eine klare Aufgabe und ein Ende, etwa: „Fertig, wenn alle Tests grün sind." Ohne Ende kann sie unnötig lange laufen oder in die falsche Richtung gehen.
- **Grenzen setzen.** Hersteller empfehlen Abbruchbedingungen wie eine Höchstzahl an Durchläufen sowie Kontrollpunkte, an denen der Mensch zustimmt. Das begrenzt Kosten und verhindert, dass sich Fehler von Runde zu Runde aufschaukeln. Lege auch erlaubte Aktionen vorab fest.
- **Ergebnis selbst prüfen.** Dass das Werkzeug mehrere Runden gedreht hat, ist keine Garantie für ein richtiges Ergebnis. Am Ende bleibt die Prüfung deine Aufgabe (E6).

Wie solche Schleifen technisch aufgebaut sind, behandelt P5.

---

## 6. Häufige Fehlgriffe

- **Zauberformeln.** Sätze wie „Du bist der beste Experte der Welt" oder angebliche Geheimtricks ersetzen keine klare Aufgabe. Für ihre Wirkung gibt es keine verlässlichen Belege, für klare Anweisungen und Beispiele schon.
- **Zu knapp.** „Mach mal besser" lässt offen, was besser heißt.
- **Zu überladen.** Widersprüchliche Vorgaben („Maximal 100 Wörter, aber alle zehn Details ausführlich") führen zu Kompromissen. Setze besser eine Priorität: „Maximal 100 Wörter, nenne nur die drei wichtigsten Punkte."
- **Nur Verbote.** Konkrete Anweisungen („schreibe in Absätzen") sind oft hilfreicher als eine reine Verbotsliste.
- **Beispiel zu eng.** Das Modell übernimmt Länge und Wortwahl des einen Beispiels fast wörtlich. Mehrere unterschiedliche Beispiele helfen.
- **Material und Aufgabe vermischt.** Wenn du Text und Anweisung nicht trennst, riskierst du Verwechslungen.
- **Prompt perfektionieren statt Ergebnis prüfen.** Ein schöner Prompt ist keine Garantie für eine richtige Antwort.

---

## Zum Ausprobieren

1. Nimm eine Frage, die du in letzter Zeit an einen Chat-Assistenten gestellt hast.
2. Verbessere sie in drei Stufen wie in Abschnitt 4: erst Kontext und Zielgruppe, dann Ziel und Format, dann ein Beispiel, wie die Antwort klingen soll, oder eine Perspektive.
3. Vergleiche die vier Antworten.
4. Notiere, welche Ergänzung den größten Unterschied gemacht hat und bei welcher sich fast nichts geändert hat.

---

## Fazit

Gutes Prompten bedeutet vor allem, dem Modell das zu geben, was ein neuer Kollege auch bräuchte: ein Ziel, den Kontext, ein gewünschtes Format und bei Bedarf ein Beispiel. Eine Rolle kann Ton und Blickwinkel steuern, garantiert aber keine Fachlichkeit. Vorgaben sind oft am hilfreichsten, wenn sie konkret und begründet sind. Und ein guter Prompt ersetzt weder das Nachfragen im Gespräch (E3) noch die Prüfung der Antwort (E6). Als Nächstes zeigt E5, wie du KI gezielt zum Lernen einsetzen kannst.

```yaml
dokument: ki-e4-gutes-prompten
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-01
quellen_fachlich:
  - "Anthropic: Prompting best practices. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (Zugriff 2026-10-01)"
  - "OpenAI: Prompt engineering guide. https://developers.openai.com/api/docs/guides/prompt-engineering (Zugriff 2026-10-01)"
  - "Google: Prompt design strategies, Gemini API. https://ai.google.dev/gemini-api/docs/prompting-strategies (Zugriff 2026-10-01)"
  - "Zheng, Pei, Logeswaran, Lee, Jurgens (arXiv 2023; Findings of EMNLP 2024): When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models. arXiv:2311.10054. https://arxiv.org/abs/2311.10054 (Zugriff 2026-10-01)"
  - "OpenAI: Reasoning best practices. https://developers.openai.com/api/docs/guides/reasoning-best-practices (Zugriff 2026-10-01)"
  - "Anthropic: Building effective agents. https://www.anthropic.com/engineering/building-effective-agents (Zugriff 2026-10-01) – Definition Agent als Schleife, Abbruchbedingungen, Kontrollpunkte, Risiken"
quellen_weiterfuehrend:
  - "Brown et al. (2020): Language Models are Few-Shot Learners. arXiv:2005.14165. https://arxiv.org/abs/2005.14165 (Abstract geprüft 2026-10-01; im Text nicht direkt zitiert)"
verifikation_offen:
  - "Hinweis 'Lange Dokumente zuerst, Frage am Ende' stammt aus Herstellerdoku (Anthropic), nicht unabhängig geprüft; im Text als herstellerseitige Erfahrung gekennzeichnet"
  - "Fachliche Einordnung zu Reasoning-Modellen (weniger Mikro-Vorgaben) beruht auf OpenAI-Anleitung; modellabhängig"
review_historie:
  - runde: 0
    datum: 2026-10-01
    ergebnis: "Erster Draft nach Recherche (Kontextmaterial Abschnitt 10)."
  - runde: 1
    datum: 2026-10-01
    ergebnis: "Drei externe Reviews geprüft (Persona-Studie: Findings of EMNLP 2024, 162 Personas, 2.410 Fragen, vier Modellfamilien; Brown-Abstract; OpenAI-Reasoning-Hinweis gegen Quellen verifiziert). Übernommen: Stufe 3 mit echtem Beispiel und korrigierter Spalte, Stufe 2 eindeutig formuliert, Kontext-Aussage differenziert, positive Formulierung/Few-Shot/Material-Trennung abgeschwächt, Rolle von Zielgruppe getrennt, Reasoning-Formulierung zeitloser, Mini-Beispiel zu Widersprüchen, Prompt-Definition geschärft, Quellenblock bereinigt. Nicht übernommen: Kurzcheckliste (Typ C ohne Cheatsheet-Block), Nennung einzelner Anbieter im Fließtext (Reihenregel: Anbieter nur in YAML und Beispielboxen)."
  - runde: 2
    datum: 2026-10-01
    ergebnis: "Auf Wunsch von David Zusatz „Was Loopen bedeutet“ in Abschnitt 5 ergänzt. Nach Rückfrage gemeint: automatischer Agenten-Loop (Planen, Handeln, Beobachten), kurz abgegrenzt vom manuellen Gespräch. Definition und Hinweise zu Abbruchbedingungen/Kontrollpunkten/Fehleraufschaukelung gegen Anthropic „Building effective agents“ geprüft."
  - runde: 3
    datum: 2026-10-01
    ergebnis: "Letzter Selbstcheck (Typ-C-Regeln, Anbieternamen im Fließtext, abgeschwächte Formulierungen, Konsistenz-Sweep): ein Befund (Anbietername im Loop-Zusatz) behoben, sonst keine. Final nach ausdrücklichem OK von David. Offen bleiben nur die beiden Herstellerdoku-Hinweise unter verifikation_offen."
  - runde: 4
    datum: 2026-10-07
    ergebnis: "Sprachliche Überarbeitung durch Claude zur Angleichung der Reihe E1 bis E8: Ansprache durchgehend du, Bild vor Regel, einzelne Tabellen in Fließtext oder Liste, Querverweise und kurze Hinweise ergänzt, lange Sätze geteilt. Inhaltlich unverändert (Zahlen, Fachbegriffe, Verweise maschinell geprüft). Freigabe durch David steht aus."
  - runde: 5
    datum: 2026-10-08
    ergebnis: "Verweis nach Umnummerierung des Dahinter-Blocks angepasst (D8 wird D7, Argumentieren und Denken). Inhaltlich unverändert. Freigabe durch David steht weiterhin aus."
```