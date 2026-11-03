# KI-P2 · API-Nutzung: Der Bestellschein ans Modell

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Profi-Track, Artikel P2 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Eine Gärtnerei bestellt beim Großhandel nicht per Zuruf. Sie füllt einen Bestellschein aus, bekommt einen Lieferschein zurück und später eine Rechnung nach Menge. An manchen Tagen ist das Lager leer, dann heißt es: später noch einmal.

Genau so sprichst du ein Modell über eine **Schnittstelle** (API) an. Dein Programm schickt eine Anfrage, bekommt eine Antwort mit Verbrauchsangaben zurück, und abgerechnet wird nach Tokens. In P1 hast du dafür einen lokalen Dienst gebaut. Hier geht es um die Anfrage selbst, und die funktioniert bei Cloud-Diensten genauso.

Am Ende kannst du eine Anfrage mit Rollen aufbauen und erklären, warum eine zustandslose Schnittstelle den benötigten Verlauf mit jeder Anfrage braucht. Du schätzt ab, was dieser Verlauf an Tokens kostet. Du weißt, wann sich Streaming lohnt, wie du auf Fehler und Limits reagierst und wo dein Schlüssel hingehört.

Vorausgesetzt werden P1 und D1. Wie Preise pro Token zustande kommen, steht in D1 und wird hier nur genutzt. Das durchgehende Projekt bleibt der Karteikarten-Dienst aus P1.

---

## 1. Ein Bestellschein mit Rollen

Eine Anfrage an ein Chat-Modell besteht vor allem aus einer Liste von Nachrichten. Jede Nachricht trägt eine **Rolle**:

- **system:** die Systemanweisung, also Regeln für die ganze Unterhaltung. Bei manchen Anbietern steht sie in einem eigenen Feld außerhalb der Liste.
- **user:** das, was du oder dein Programm fragt.
- **assistant:** frühere Antworten des Modells.

Dazu kommen Einstellungen. Die wichtigste ist die **Höchstzahl an Ausgabe-Tokens**. Sie begrenzt, wie lang die Antwort werden darf, und damit Zeit und Kosten (P1). Ob eine Antwort deshalb abgeschnitten wurde, meldet die Antwort selbst, bei einer verbreiteten Schnittstelle im Feld `finish_reason` mit dem Wert `length`. Die Temperatur steuert, wie stark die Antworten streuen (D4).

> **Beispielbox, Stand 03.11.2026: Python-Bibliothek eines großen Anbieters.** Nach der Dokumentation, nicht selbst ausgeführt. Mit `base_url` zeigt dieselbe Bibliothek auf deinen lokalen Dienst aus P1.
>
> ```python
> from openai import OpenAI
>
> client = OpenAI(base_url="http://127.0.0.1:11434/v1/", api_key="ollama")  # lokal, Schlüssel wird ignoriert
>
> antwort = client.chat.completions.create(
>     model="<modellname>",
>     max_tokens=400,
>     messages=[
>         {"role": "system", "content": "Du erstellst drei Lernfragen mit Lösung."},
>         {"role": "user", "content": "Abschnitt: Ein Subnetz teilt ein Netz ..."},
>     ],
> )
> print(antwort.choices[0].message.content)
> print(antwort.choices[0].finish_reason)   # z. B. stop oder length
> print(antwort.usage)   # Verbrauch: Eingabe- und Ausgabe-Tokens
> ```
>
> Für einen Cloud-Dienst entfällt `base_url`, und der Schlüssel kommt aus einer Umgebungsvariablen (Abschnitt 4). Der lokale Dienst versteht `max_tokens`. In der Cloud-Schnittstelle desselben Anbieters gilt das Feld als veraltet, dort heißt es `max_completion_tokens`. Kompatibel heißt also nicht identisch.

Der entscheidende Punkt steht nicht im Code: **Das Modell merkt sich nichts zwischen zwei Anfragen.** Die klassische Chat-Schnittstelle ist zustandslos. Soll das Modell eine Nachfrage verstehen, muss dein Programm die bisherigen Nachrichten erneut mitschicken, mit den Rollen user und assistant im Wechsel. Der Chat im Browser macht das unsichtbar für dich.

Wo das Bild nicht passt: Ein Großhändler kennt seine Stammkunden und erinnert sich an die letzte Bestellung. Das Modell erinnert sich nicht. Jeder Bestellschein muss alles enthalten, was für diese Lieferung zählt. Manche neueren Schnittstellen können den Verlauf auf dem Server halten. Abgerechnet wird der Verlauf als Eingabe trotzdem, sobald das Modell ihn liest.

---

## 2. Was der Verlauf kostet

Weil jede Anfrage den Verlauf mitschickt, wächst die Eingabe mit jeder Runde. Das Programm rechnet ein Gespräch mit zehn Runden durch. Die Werte pro Teil sind angenommen:

```python
system, frage, antwort = 300, 150, 250        # Tokens je Teil, angenommene Werte
verlauf, summe = 0, 0
for runde in range(1, 11):
    eingabe = system + verlauf + frage           # alles, was diese Anfrage mitschickt
    summe += eingabe
    verlauf += frage + antwort                   # wächst für die nächste Runde
    if runde in (1, 5, 10):
        print(f"Runde {runde:2}: {eingabe:5} Eingabe-Tokens, bisher {summe:6} abgerechnet")
print("Ohne Verlauf wären es", 10 * (system + frage), "gewesen")
```

Ausgabe:

```text
Runde  1:   450 Eingabe-Tokens, bisher    450 abgerechnet
Runde  5:  2050 Eingabe-Tokens, bisher   6250 abgerechnet
Runde 10:  4050 Eingabe-Tokens, bisher  22500 abgerechnet
Ohne Verlauf wären es 4500 gewesen
```

Zehn Runden kosten also das Fünffache an Eingabe-Tokens, verglichen mit zehn Einzelanfragen. Die Ausgabe-Tokens kommen in beiden Fällen dazu. Die Rechnung ist vereinfacht, maßgeblich sind die Verbrauchsangaben der Antwort. Dazu kommt, dass der Verlauf irgendwann das Kontextfenster füllt (D1).

Drei Folgen für dein Projekt:

- **Einzelanfragen, wo es geht.** Der Karteikarten-Dienst braucht keinen Verlauf. Jeder Abschnitt ist eine eigene Anfrage mit derselben Systemanweisung.
- **Verlauf kürzen.** Wo du ein Gespräch brauchst, schick nur die letzten Runden mit oder lass ältere zusammenfassen.
- **Gleicher Anfang kann günstiger werden.** Viele Anbieter rechnen einen Anfang günstiger ab, der sich zwischen Anfragen exakt wiederholt, etwa eine lange Systemanweisung. Je nach Anbieter geschieht das automatisch oder über eine Markierung im Prompt. Es gibt Mindestlängen, bei einem Anbieter für neuere Modelle 1.024 Tokens. Im Gespräch ist auch der bisherige Verlauf ein solcher Anfang, im Beispiel ab Runde 3 lang genug. Das erste Anlegen kann dagegen mehr kosten als normale Eingabe. Stell das Gleichbleibende nach vorn und das Wechselnde nach hinten.

Den tatsächlichen Verbrauch liefert jede Antwort mit, getrennt nach Eingabe und Ausgabe. Bei Modellen, die vor der Antwort nachdenken, rechnen zwei große Anbieter die Denk-Tokens als Ausgabe ab, auch wenn du sie nicht siehst (D7). Protokolliere diese Zahlen, dann weißt du nach einem Testlauf, was eine echte Ausführung kostet.

---

## 3. Streaming: Ware in Teillieferungen

Ohne Streaming wartest du, bis die ganze Antwort fertig ist, und bekommst sie in einem Stück. Mit Streaming schickt der Dienst die Antwort in kleinen Teilen, sobald sie entstehen. Technisch nutzen verbreitete Programme dafür **Server-Sent Events**: Die Verbindung bleibt offen, und der Dienst schreibt Stück für Stück hinein.

Die Erzeugung wird dadurch nicht schneller. Du siehst aber das erste Wort, während das Modell noch weiterarbeitet. Für einen Chat, in dem ein Mensch liest, lohnt sich das. Für den Karteikarten-Dienst, der die Antwort ohnehin erst als Ganzes weiterverarbeitet, bringt es wenig und macht den Code komplizierter.

Drei Haken: Beim Streaming setzt du die Teile selbst zusammen, und eine Verbindung kann mitten in der Antwort abreißen. Dann fehlt meist das reguläre Abschlussereignis, und daran erkennst du den Abbruch. Außerdem liefert eine verbreitete Bibliothek die Verbrauchsangaben im Stream nur mit `stream_options={"include_usage": True}`, in einem letzten zusätzlichen Teil. Sonst hast du nichts zum Protokollieren.

---

## 4. Wenn es schiefgeht

Fehler gehören zum Alltag einer Schnittstelle. Der Statuscode der Antwort verrät, wer etwas tun muss:

| Code | Bedeutung | Was du tust |
| --- | --- | --- |
| 400 | Anfrage fehlerhaft, z. B. zu lang für den Kontext | Anfrage korrigieren, nicht wiederholen |
| 401 | Schlüssel fehlt oder ist ungültig | Schlüssel prüfen |
| 403 | Zugriff nicht erlaubt | Rechte und Projektzugriff prüfen |
| 404 | Modell oder Adresse unbekannt | Modellnamen und Basisadresse prüfen |
| 429 | Limit erreicht oder Guthaben aufgebraucht | Fehlertext lesen, nur beim Limit warten und erneut versuchen |
| ab 500 | Fehler oder Überlastung beim Anbieter | warten, dann begrenzt erneut versuchen |
| 408 oder keine Antwort | Zeit abgelaufen oder Verbindung weg | wie ab 500 |

Dieselbe Zahl kann bei verschiedenen Anbietern Verschiedenes bedeuten. Lies deshalb immer auch den Fehlertext im Antwortkörper.

**Limits.** Anbieter begrenzen, wie viele Anfragen und Tokens du pro Minute oder pro Tag schicken darfst. Ein Anbieter zählt dabei nicht nur die Eingabe. Er schätzt den Bedarf einer Anfrage auch über die erlaubte Höchstzahl an Ausgabe-Tokens. Ein unnötig hoher Wert frisst also Kontingent. Die Antworten tragen Kopfzeilen, die zeigen, wie viel vom Limit noch übrig ist. Bei 429 sagt ein Anbieter in der Kopfzeile `retry-after`, wie viele Sekunden du warten sollst.

**Klug wiederholen.** Bei einem erreichten Limit und bei Fehlern ab 500 hilft ein erneuter Versuch, aber nicht sofort. Bei aufgebrauchtem Guthaben hilft er nie. Bewährt ist **exponentielles Warten mit Zufallsanteil**: Die Pause verdoppelt sich mit jedem Versuch, und ein kleiner Zufall sorgt dafür, dass nicht alle Programme gleichzeitig wiederkommen. Ein Anbieter warnt ausdrücklich, dass auch fehlgeschlagene Anfragen auf das Limit zählen. Dauerfeuer macht es also schlimmer. Das Programm zeigt die Logik mit simulierten Antworten:

```python
import random
random.seed(1)                                   # feste Zufallszahlen, damit die Ausgabe gleich bleibt
antworten = [429, 503, 200]                      # simulierte Statuscodes des Dienstes

for versuch, status in enumerate(antworten):
    if status == 200:
        print("Versuch", versuch + 1, "erfolgreich")
        break
    warten = min(2 ** versuch, 30) + random.uniform(0, 1)   # exponentiell plus Zufall
    print(f"Versuch {versuch + 1}: Status {status}, warte {warten:.1f} s")
```

Ausgabe:

```text
Versuch 1: Status 429, warte 1.1 s
Versuch 2: Status 503, warte 2.8 s
Versuch 3 erfolgreich
```

Ein echtes Programm würde zwischen den Versuchen tatsächlich warten, einen vorhandenen `retry-after`-Wert bevorzugen und nach wenigen Versuchen aufgeben. Die offizielle Bibliothek eines großen Anbieters erledigt das selbst. Sie wiederholt laut Dokumentation standardmäßig zweimal mit kurzem exponentiellem Warten, bei Verbindungsfehlern, 408, 409, 429 und Fehlern ab 500. Schreibst du eine eigene Schleife, schalte die eingebaute ab (dort `max_retries=0`). Sonst multiplizieren sich die Versuche.

**Der Schlüssel gehört nicht in den Code.** Wer den API-Schlüssel hat, bestellt auf deine Rechnung. Lies ihn aus einer Umgebungsvariablen. Eine Bibliothek empfiehlt dafür eine Datei `.env`, damit der Schlüssel nicht in der Versionsverwaltung landet. Trag diese Datei in `.gitignore` ein. Ist ein Schlüssel doch einmal in einem Repository gelandet, widerruf ihn sofort beim Anbieter. Ihn nur zu löschen reicht nicht, die Git-Historie behält ihn.

---

## Häufige Fehlgriffe

- **Glauben, das Modell erinnere sich.** Ohne mitgeschickten Verlauf kennt es die letzte Frage nicht (Abschnitt 1).
- **Den Verlauf endlos mitschleppen.** Die Eingabe wächst mit jeder Runde und mit ihr die Rechnung (Abschnitt 2).
- **Keine Höchstzahl an Ausgabe-Tokens setzen.** Oder eine viel zu hohe, die das Limit unnötig belastet.
- **Bei 429 sofort erneut senden.** Auch Fehlversuche zählen. Warte exponentiell, und prüfe vorher, ob nur das Guthaben fehlt (Abschnitt 4).
- **Einen 400er wiederholen.** Die Anfrage selbst ist falsch, Wiederholen ändert nichts.
- **Streaming ohne Vollständigkeitsprüfung.** Eine abgebrochene Antwort sieht oft aus wie eine fertige.
- **Den Schlüssel ins Repository schreiben.** Widerrufen ist dann Pflicht, Löschen reicht nicht.

---

## Zum Ausprobieren

1. Schicke an deinen Dienst aus P1 eine Frage und danach eine Nachfrage ohne Verlauf, etwa „Und warum?". Wiederhole die Nachfrage mit Verlauf. Vergleiche beide Antworten.
2. Ändere im Programm aus Abschnitt 2 die Antwortlänge auf 500 Tokens. Wie viele Eingabe-Tokens braucht die zehnte Anfrage, und wie viele werden über alle zehn Runden abgerechnet?
3. Lies aus einer Antwort die Verbrauchsangaben ab. Rechne mit einer Preisliste aus, was hundert Karteikarten-Anfragen kosten würden.
4. Setze die Höchstzahl an Ausgabe-Tokens bewusst zu niedrig. Woran erkennst du in der Antwort, dass sie abgeschnitten wurde?
5. Prüfe deine eigenen Repositories mit der Suche nach `api_key` und `sk-`. Steht dort ein Schlüssel, widerrufe ihn.

---

## Fazit

Eine Anfrage an ein Modell ist ein Bestellschein: eine Liste von Nachrichten mit Rollen, dazu Einstellungen wie die Höchstzahl an Ausgabe-Tokens. Das Modell merkt sich nichts, deshalb schickt jede Anfrage den nötigen Verlauf mit, und die Eingabe wächst mit jeder Runde. Einzelanfragen, gekürzte Verläufe und ein gleichbleibender Anfang halten die Kosten im Rahmen. Streaming verkürzt die Wartezeit bis zum ersten Wort, nicht die Erzeugung selbst. Bei Limits und Serverfehlern wartest du exponentiell mit Zufall, fehlerhafte Anfragen korrigierst du, und bei aufgebrauchtem Guthaben hilft kein Warten. Der Schlüssel gehört in eine Umgebungsvariable und nie ins Repository. Als Nächstes geht es in P3 darum, wie du das Modell dazu bringst, in einem festen Format zu antworten und Werkzeuge aufzurufen.

```yaml
dokument: ki-p2-api-nutzung
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: profi
status: final
stand: 2026-11-03
quellen_fachlich:
  - "openai-python, README.md (Commit 4bc7f90 vom 2026-11-03, Zugriff 2026-11-03): Schlüssel über OPENAI_API_KEY, Empfehlung python-dotenv und .env, 'so that your API key is not stored in source control'; Streaming mit stream=True; Fehlertabelle 400 BadRequest, 401 Authentication, 403 PermissionDenied, 404 NotFound, 422, 429 RateLimit, >=500 InternalServer, APIConnectionError; Retries: 'automatically retried 2 times by default, with a short exponential backoff', bei Verbindungsfehlern, 408, 409, 429, >=500, nur wenn der Body sicher erneut gesendet werden kann; Timeout Standard 10 Minuten"
  - "anthropic-sdk-python, README.md (Commit 5752c13 vom 2026-11-02, Zugriff 2026-11-03): Schlüssel über ANTHROPIC_API_KEY, messages mit role user, max_tokens als Pflichtangabe im Beispiel"
  - "OpenAI Developers: Rate limits. https://developers.openai.com/api/docs/guides/rate-limits (Zugriff 2026-11-03): RPM, RPD, TPM, TPD, IPM; Limits je Organisation und Projekt; Kopfzeilen x-ratelimit-remaining-requests u. a.; exponentielles Warten mit 'random jitter'; 'unsuccessful requests contribute to your per-minute limit'; Limit berechnet aus dem Maximum von max_tokens und geschätzten Tokens"
  - "AWS: Claude Platform on AWS, Rate limits and quotas. https://docs.aws.amazon.com/claude-platform/latest/userguide/rate-limits.md (Zugriff 2026-11-03): RPM, ITPM, OTPM wie bei der direkten Claude API; Kopfzeilen anthropic-ratelimit-*; bei 429 rate_limit_error und retry-after in Sekunden; exponentielles Warten mit Jitter"
  - "llama.cpp, tools/server/README.md (Commit 20a51f2, Zugriff 2026-11-03): Streaming per Server-sent events; messages im ChatML-Format; keine strengen Kompatibilitätszusagen. Ollama docs/api/openai-compatibility.mdx (Commit 355eaee): lokale base_url http://localhost:11434/v1/, Schlüssel nötig, aber ignoriert; Responses API dort nur zustandslos, ohne previous_response_id und conversation (es gibt also zustandsbehaftete Varianten)"
  - "OpenAI Developers: Prompt caching. https://developers.openai.com/api/docs/guides/prompt-caching (Zugriff 2026-11-03): standardmäßig aktiv, optional explizite Breakpoints; Mindestlänge 1.024 sichtbare Eingabe-Tokens bei GPT-5.6 und später, bei älteren Modellen abweichend; Schreiben in den Zwischenspeicher 1,25-fach (30 Minuten) bzw. 2,5-fach (12 Stunden), Treffer meist 0,1-fach; 'the entire rendered prefix' muss übereinstimmen; Rabatt modellabhängig bis 95 %"
  - "OpenAI Developers: Error codes. https://developers.openai.com/docs/guides/error-codes (Zugriff 2026-11-03): 429 'Rate limit reached' (langsamer senden, Retry-After beachten) und 429 credit_balance_exhausted (Wiederholen hilft nicht); 503 server_is_overloaded; 500 kurz warten und wiederholen"
  - "openai-python, src/openai/types/chat (Commit 4bc7f90): max_tokens 'now deprecated in favor of max_completion_tokens'; stream_options.include_usage liefert usage in einem zusätzlichen Chunk; finish_reason stop, length, tool_calls, content_filter. Ollama openai-compatibility.mdx: max_tokens und stream_options unterstützt"
  - "Eigene Artikel der Reihe: P1 (lokaler Dienst, Karteikarten-Dienst, Antwortlänge), D1 (Kontextfenster, Preise pro Token, Fehler bei zu langer Eingabe), D4 (Temperatur), D7 (Denk-Tokens laut Dokumentation zweier großer Anbieter als Ausgabe abgerechnet); Vorwärtsverweis auf P3"
  - "Rechnungen am 2026-11-03 mit Python ausgeführt: Verlauf 450, 2.050, 4.050 Eingabe-Tokens in Runde 1, 5, 10, Summe 22.500 gegenüber 4.500; Warteschleife mit random.seed(1): 1,1 s und 2,8 s"
verifikation_offen:
  - "Beispielbox nach der Dokumentation, nicht selbst ausgeführt (kein Modellzugriff in der Arbeitsumgebung)"
  - "Seiten von platform.claude.com waren aus der Arbeitsumgebung nicht abrufbar; Anthropic-Limits über die AWS-Seite (Claude Platform on AWS) belegt, die auf diese Seiten als maßgeblich verweist. Code 529 nicht eigens aufgenommen, die Zeile 'ab 500' deckt ihn ab"
  - "Dass ein Anbieter das Zwischenspeichern nur nach Markierung im Prompt anbietet, stammt aus einem Review und ist nicht an der Primärquelle geprüft; im Text deshalb als 'je nach Anbieter automatisch oder über eine Markierung' formuliert"
  - "Rabatte für wiederholte Anfänge bei einem Anbieter geprüft (modellabhängig bis 95 %), beim anderen nicht; im Text deshalb ohne Prozentzahl"
  - "Vorwärtsverweis auf P3 beim Anlegen abgleichen"
review_historie:
  - runde: 0
    datum: 2026-11-03
    ergebnis: "Erster Draft nach den Regeln für Welle 3. Quellen aus den aktuellen SDK-Repositories und Anbieterdokumentationen gelesen, Rechnungen mit Python ausgeführt."
  - runde: 1
    datum: 2026-11-03
    ergebnis: "Drei Reviews, gegen Quellen geprüft. Übernommen: max_tokens im Cloud-Dienst veraltet; finish_reason length schon in Abschnitt 1; Verbindungsabbruch ohne Abbruchgrund; Verbrauch im Stream nur auf Anforderung; Erzeugung durch Streaming nicht schneller; Rechnung als vereinfacht, Ausgabe kommt dazu; Zwischenspeichern mit exaktem Anfang und Mindestlänge; 429 auch bei aufgebrauchtem Guthaben; 408 und Verbindungsfehler; Fehlertext lesen; eigene Schleife nur mit max_retries=0 und Obergrenze; Retry-Aussage auf eine Bibliothek begrenzt; Übung 2 eindeutig. Nicht übernommen: Einwand gegen die Daten (Stand 2026-11-03 ist korrekt); Übersichtstabelle, Secret-Manager, Rolle developer und Struktur-Tokens (Umfang)."
  - runde: 2
    datum: 2026-11-03
    ergebnis: "Drei Re-Reviews. Übernommen: Verlauf als zwischenspeicherbarer Anfang (ab Runde 3 über 1.024 Tokens, nachgerechnet); Kosten für das erste Anlegen; Drei Haken, fehlendes Abschlussereignis; include_usage benannt; 401 und 403 getrennt; Limits pro Minute oder Tag; 429 im Fließtext an Limit und Guthaben angepasst, auch im Fazit; Lernziel 'benötigter Verlauf'; finish_reason in der Beispielbox; Widerspruch zu Rabatten im YAML aufgelöst. Nicht übernommen: Einwand gegen die Daten (Stand 2026-11-03 korrekt); weitere Anthropic-Quellen (aus der Arbeitsumgebung nicht abrufbar)."
  - runde: 3
    datum: 2026-11-03
    ergebnis: "Freigabe durch David am 2026-11-03 nach Runde 2. Kopfzeile und YAML-Status gemeinsam auf final; offene Punkte unter verifikation_offen bleiben."
```
