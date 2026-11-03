# KI-P1 · Lokale Modelle betreiben: Vom Gewächshaus zum Hofladen

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Profi-Track, Artikel P1 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

In A9 hast du dein Gewächshaus für den Eigenbedarf gebaut: ein Modell auf dem eigenen Rechner, ein paar Fragen im Terminal, fertig. Jetzt wird daraus ein Hofladen. Der hat feste Öffnungszeiten, eine Theke für Kundschaft und eine Kasse, die mitzählt. Und abends schließt jemand die Tür ab.

Übersetzt heißt das: Das Modell läuft als **Dienst**, den deine Programme jederzeit ansprechen können. Als durchgehendes Projekt baust du einen kleinen Karteikarten-Dienst. Ein Skript schickt einen Abschnitt aus dem Wiki an dein lokales Modell und bekommt Lernfragen zurück, wie in A4 beschrieben.

Am Ende kannst du ein lokales Modell als Dienst starten und über eine Schnittstelle ansprechen. Du misst, wie schnell es einliest und antwortet, und teilst den Speicher bewusst zwischen Kontext und parallelen Anfragen auf. Du lässt den Dienst dauerhaft laufen, ohne ihn ins offene Netz zu stellen. Und du entscheidest mit eigenen Zahlen, ob sich neue Hardware lohnt.

Vorausgesetzt wird A9. Die Rechnungen zu Dateigröße, Zwischenspeicher und Bandbreite stehen dort und werden hier nur genutzt. Wie Mixture-of-Experts-Modelle den Speicher belegen, erklärt D6.

---

## 1. Vom Programm zum Dienst

Im Gewächshaus pflückst du selbst. Im Hofladen steht eine Theke, und wer etwas will, fragt dort nach. Genau diese Theke ist der **Server-Modus** eines Laufzeitprogramms. Das Programm lädt das Modell einmal und wartet dann auf Anfragen über eine Netzwerkadresse auf deinem Rechner.

Der Trick dabei: Viele Laufzeitprogramme bieten eine Schnittstelle in dem Format an, das auch große Cloud-Anbieter nutzen, meist als Teilmenge davon. Ein Skript, das für einen Cloud-Dienst geschrieben ist, spricht dann mit deinem lokalen Modell, wenn du nur die Basisadresse änderst. Wie solche Anfragen im Detail aufgebaut sind, mit Rollen, Streaming und Fehlerbehandlung, behandelt P2. Hier reicht eine Anfrage, die funktioniert.

> **Beispielbox, Stand 03.11.2026: llama.cpp und Ollama als Dienst.** Die Befehle sind der jeweiligen Dokumentation entnommen und nicht selbst ausgeführt. Dateinamen und Ports sind Beispiele, Standardwerte ändern sich zwischen Versionen.
>
> ```bash
> # llama.cpp: ein Platz (-np 1) mit 8.192 Token Kontext, lädt das Modell beim Start
> llama-server -m modelle/mein-modell-Q4_K_M.gguf -c 8192 -np 1
> curl http://127.0.0.1:9931/v1/chat/completions \
>   -H "Content-Type: application/json" \
>   -d '{"model": "<modellname>", "messages": [{"role": "user",
>        "content": "Stelle drei Lernfragen zu diesem Text: ..."}]}'
>
> # Ollama: läuft unter Linux meist schon als Dienst, lädt beim ersten Aufruf
> curl http://127.0.0.1:11434/v1/chat/completions \
>   -H "Content-Type: application/json" \
>   -d '{"model": "<modellname>", "messages": [{"role": "user",
>        "content": "Stelle drei Lernfragen zu diesem Text: ..."}]}'
> ```
>
> Für `<modellname>` setzt du bei Ollama den exakten Namen eines heruntergeladenen Modells ein. Bei llama.cpp mit nur einem Modell spielt der Wert laut Dokumentation keine Rolle, erst im Router-Betrieb mit mehreren Modellen wählt er das Modell aus. Programmbibliotheken für das OpenAI-Format verlangen einen API-Schlüssel, den die lokale Schnittstelle von Ollama laut Dokumentation ignoriert. Den Standard-Port 9931 nennt die aktuelle Dokumentation von llama.cpp. Selbst die Docker-Beispiele derselben Dokumentation nutzen einen anderen Port. Prüfe den Standardwert deiner Version in der Hilfe des Programms.

Beide Programme lauschen standardmäßig nur auf dem eigenen Rechner. Die Adresse 127.0.0.1 (bei IPv6 ::1) heißt Loopback: Nur Programme auf demselben Gerät erreichen sie, andere Geräte im Heimnetz nicht. Das ist die abgeschlossene Ladentür, und dabei bleibt es vorerst (Abschnitt 4).

Wo das Bild nicht passt: Im Hofladen wird die Ware weniger, wenn verkauft wird. Das Modell verbraucht sich nicht, jede Anfrage bekommt dieselben Gewichte. Knapp werden andere Dinge, nämlich Rechenzeit und der Zwischenspeicher für jede laufende Anfrage. Darum geht es in den nächsten beiden Abschnitten.

---

## 2. Zwei Geschwindigkeiten und eine Wartezeit

Eine Kasse, die nur die Tagessumme kennt, hilft wenig. Du willst wissen, wo die Zeit hingeht. Bei einem Modell-Dienst gibt es dafür drei Posten:

- **Laden:** Das Modell wandert von der Festplatte in den Speicher. Je nach Programm passiert das beim Start des Dienstes oder beim ersten Aufruf und dann nach jeder Pause, in der das Modell entladen wurde.
- **Einlesen:** Das Modell verarbeitet deine Eingabe. Eine technische Beschreibung der Inferenz nennt diesen Schritt stark parallelisiert. Viele Eingabe-Tokens werden in denselben Rechenschritten gemeinsam verarbeitet.
- **Antworten:** Das Modell erzeugt Token für Token. Dieser Schritt ist speichergebunden (A9) und meist der langsamere.

Die Programme liefern Zeitangaben mit, allerdings unter verschiedenen Feldnamen und nicht immer alle drei Posten. Das folgende Programm rechnet die Felder einer Beispielantwort aus der Dokumentation eines Laufzeitprogramms aus. Auf welcher Hardware sie entstand, sagt die Dokumentation nicht:

```python
antwort = {                        # Zeitangaben in Nanosekunden
    "total_duration": 10706818083,
    "load_duration": 6338219291,
    "prompt_eval_count": 26, "prompt_eval_duration": 130079000,
    "eval_count": 259, "eval_duration": 4232710000,
}
ns = 1e9
print("Laden:   ", round(antwort["load_duration"] / ns, 1), "s")
print("Einlesen:", round(antwort["prompt_eval_count"] / antwort["prompt_eval_duration"] * ns), "Token/s")
print("Antwort: ", round(antwort["eval_count"] / antwort["eval_duration"] * ns, 1), "Token/s")
print("Anteil Laden an der Gesamtzeit:", round(antwort["load_duration"] / antwort["total_duration"] * 100), "%")
```

Ausgabe:

```text
Laden:    6.3 s
Einlesen: 200 Token/s
Antwort:  61.2 Token/s
Anteil Laden an der Gesamtzeit: 59 %
```

Drei Erkenntnisse stecken darin. Erstens war das Laden der größte Posten, mehr als die Hälfte der Zeit. Für einen Dienst, den ein Skript immer wieder aufruft, lohnt es sich deshalb, das Modell geladen zu halten. Ein verbreitetes Programm lädt beim ersten Aufruf und entlädt laut Dokumentation nach fünf Minuten ohne Anfrage, diese Zeit lässt sich verlängern. Ein anderes lädt beim Start und hält das Modell standardmäßig geladen, bis der Dienst endet.

Zweitens ist das Einlesen deutlich schneller als das Antworten. Bei nur 26 Eingabe-Tokens ist der Abstand noch moderat. Die Dokumentation eines Messwerkzeugs zeigt ihn deutlicher, in einem anderen Test auf anderer Hardware. Dort liest ein Modell mit rund 7,6 Milliarden Parametern auf einer Grafikkarte 512 Tokens mit rund 7.300 Token/s ein. 128 Tokens erzeugt es mit rund 120 Token/s. Für deinen Karteikarten-Dienst heißt das: Ein Token Eingabe ist meist viel schneller verarbeitet als ein Token Antwort. Ein langer Abschnitt kostet trotzdem Zeit und Zwischenspeicher. Begrenze vor allem die Antwortlänge, wenn Tempo zählt.

Drittens sind das Zahlen eines fremden Rechners. Sie zeigen, was du messen sollst, und ersetzen deine eigene Messung nicht.

### Erst messen, dann kaufen

A9 hat die Anschaffung eigener Hardware auf später verschoben. Jetzt hast du das Werkzeug für diese Entscheidung. Miss mit deinem Rechner und deinem Modell drei Werte: Ladezeit, Einlesetempo und Antworttempo. Dann prüfe, was dein Anwendungsfall braucht.

- **Reicht das Antworttempo** für deine Aufgabe? Ein nächtliches Skript, das Karteikarten erzeugt, darf langsam sein. Ein Chat, in dem du auf jede Antwort wartest, nicht.
- **Läuft das Modell geteilt** zwischen Grafik- und Arbeitsspeicher? Dann bringt mehr Grafikspeicher oft den größten Sprung (A9).
- **Brauchst du ein größeres Modell**, weil deine Testfälle aus A7 mit dem kleinen scheitern? Erst dann zählt die Größenfrage.

Erst wenn ein Wert nicht reicht und du weißt, welcher, lohnt der Blick auf neue Hardware. Die Rechnungen aus A9 und D6 sagen dir vorher, welche Speichergröße und Bandbreite das Ziel ist.

---

## 3. Den Speicher aufteilen

Die Ladenfläche ist begrenzt. Auf ihr stehen das Modell selbst und der Zwischenspeicher aus A9, der mit dem Kontext wächst. Ein Dienst bringt eine dritte Größe ins Spiel: die Zahl der Anfragen, die gleichzeitig bedient werden. Jede davon belegt einen **Platz**. Der Zwischenspeicher heißt in Dokumentationen meist **KV-Cache**.

Die Dokumentation eines verbreiteten Programms formuliert es direkt: Der benötigte Speicher wächst mit Anzahl paralleler Anfragen mal Kontextlänge. Das Programm rechnet es mit den Werten des Modells aus A9 durch. Dort waren es 57.344 Byte pro Token:

```python
pro_token = 57344           # Byte je Token im Zwischenspeicher, Modell aus A9
for plaetze, kontext in [(1, 32768), (4, 8192), (4, 32768)]:
    gib = plaetze * kontext * pro_token / 2**30
    print(f"{plaetze} x {kontext} Token: {gib:.2f} GiB, mit 8-Bit-Zwischenspeicher etwa {gib / 2:.2f} GiB")
```

Ausgabe:

```text
1 x 32768 Token: 1.75 GiB, mit 8-Bit-Zwischenspeicher etwa 0.88 GiB
4 x 8192 Token: 1.75 GiB, mit 8-Bit-Zwischenspeicher etwa 0.88 GiB
4 x 32768 Token: 7.00 GiB, mit 8-Bit-Zwischenspeicher etwa 3.50 GiB
```

Das ist nur der Zwischenspeicher, Gewichte und Puffer des Programms kommen dazu. Vier Plätze mit je 8.192 Token kosten so viel wie ein Platz mit 32.768 Token. Du verschiebst also Fläche zwischen „lange Gespräche" und „mehrere Kunden gleichzeitig". Für den Karteikarten-Dienst reicht oft ein Platz mit mittlerem Kontext, weil das Skript die Abschnitte nacheinander schickt. Ein anderes Programm verwaltet standardmäßig einen gemeinsamen Zwischenspeicher für alle Plätze, wenn es deren Zahl selbst wählt. Die Anfragen bleiben getrennt, der Speicher wird gemeinsam verwaltet. Dort beschreibt die einfache Multiplikation den Bedarf nicht genau, prüfe die Dokumentation deines Programms.

Drei Stellschrauben hast du:

- **Kontextlänge:** Stelle sie passend zur Aufgabe ein. In den Kontext zählen Systemanweisung, bisheriger Gesprächsverlauf, Eingabe und Antwort zusammen. Manche Programme wählen sie automatisch nach Speicher. Bei einem verbreiteten Programm ist die Dokumentation hier nicht einheitlich. Eine Seite nennt pauschal 4.096 Token, eine andere je nach Grafikspeicher 4k, 32k oder 256k, unter 24 GiB also nur rund 4.000 Token. Prüfe deshalb, was dein Dienst tatsächlich eingestellt hat. Ein längerer Abschnitt passt dann nicht vollständig hinein. Je nach Programm wird gekürzt oder die Anfrage scheitert (D1).
- **Parallele Plätze:** Mehr Plätze helfen, wenn mehrere Programme gleichzeitig fragen. Laut einer technischen Beschreibung verteilt das gemeinsame Abarbeiten die Kosten für das Lesen der Gewichte auf mehrere Anfragen. Den Zwischenspeicher hat trotzdem jede Anfrage logisch für sich, wie er physisch aufgeteilt wird, hängt vom Programm ab.
- **Genauigkeit des Zwischenspeichers:** Wie bei den Gewichten lässt sich auch der Zwischenspeicher gröber speichern. Laut einer Dokumentation halbiert eine 8-Bit-Stufe den Bedarf ungefähr, mit meist kaum spürbarem Qualitätsverlust. Eine 4-Bit-Stufe viertelt ihn ungefähr, kann bei langem Kontext aber merklich schaden. Dort setzt das voraus, dass Flash Attention aktiv ist, und die Einstellung gilt für alle Modelle des Dienstes.

### Welche Quantisierung

Bei den Gewichten selbst gilt dasselbe Prinzip. Die Dokumentation eines Quantisierungswerkzeugs nennt zwei Maße für den Qualitätsverlust. Die Perplexität bewertet, wie gut ein Modell einen Referenztext vorhersagt. Die Kullback-Leibler-Divergenz vergleicht die Wahrscheinlichkeitsverteilungen von gerundetem Modell und Original. Für deinen Alltag ist dein eigener Test aussagekräftiger. Lass die Testfälle aus A7 mit zwei Stufen laufen, etwa 4 und 8 Bit, und protokolliere Tempo und Ergebnis wie in A8. Wie du solche Vergleiche sauber aufsetzt, zeigt P8.

---

## 4. Dauerbetrieb und Schutz

Ein Hofladen mit wechselnden Öffnungszeiten verliert Kundschaft. Ein Dienst, den du nach jedem Neustart von Hand starten musst, ebenso. Unter Linux übernimmt das der Dienstverwalter systemd. Ist der Dienst aktiviert, startet er das Programm beim Hochfahren und sammelt die Protokolle. Steht es in der Dienstbeschreibung, startet er es nach einem Absturz auch neu.

> **Beispielbox, Stand 03.11.2026: Ollama unter systemd.** Nach der Dokumentation, nicht selbst ausgeführt.
>
> ```bash
> sudo systemctl edit ollama.service      # Einstellungen ergänzen, z. B.:
> #   [Service]
> #   Environment="OLLAMA_KEEP_ALIVE=1h"
> #   Environment="OLLAMA_CONTEXT_LENGTH=16384"
> sudo systemctl daemon-reload && sudo systemctl restart ollama
> journalctl -e -u ollama                  # Protokoll ansehen
> ```
>
> Cloud-Modelle schaltet die Umgebungsvariable `OLLAMA_NO_CLOUD=1` ab. Bei llama.cpp aktiviert `--metrics` den Messwert-Endpunkt, `--api-key` verlangt einen Schlüssel.

Für den Dauerbetrieb gelten vier Regeln.

**Die Tür bleibt zu.** Lass den Dienst auf 127.0.0.1. Ein verbreitetes Programm verlangt für seine lokale Schnittstelle laut Dokumentation keine Anmeldung. Wer die Adresse erreicht, kann das Modell also nutzen. Welche Folgen offene Dienste haben, zeigt A9 mit Zahlen. Und eine lokale Adresse garantiert nicht, dass lokal gerechnet wird. Ein Programm kann über denselben Dienst auch Cloud-Modelle ansprechen, das lässt sich dort abschalten (Beispielbox).

**Wenn sie doch aufgeht, dann mit Schloss.** Sollen andere Geräte im Heimnetz zugreifen, brauchst du einen Anmeldeschutz und eine Firewall-Regel. Ein Laufzeitprogramm kann dafür einen API-Schlüssel verlangen. Das andere hat für seine lokale Schnittstelle keine Anmeldung, dort übernimmt ein vorgeschalteter Reverse Proxy diese Aufgabe. Für den Betrieb im Internet empfiehlt auch die erste Dokumentation einen solchen Proxy. Über reines HTTP reist ein Schlüssel unverschlüsselt. Auf Verbindungen, denen du nicht voll vertraust, gehört deshalb HTTPS dazu.

**Werkzeuge für Agenten aus lassen.** Manche Server können dem Modell Dateizugriff oder externe Werkzeuge freigeben. Die Dokumentation eines Programms rät ausdrücklich davon ab, das in Umgebungen einzuschalten, denen du nicht vertraust. Wie Agenten sicher mit Werkzeugen arbeiten, behandelt P5, die Angriffe darauf R3.

**Hinsehen und aktualisieren.** Lies die Protokolle, wenn etwas hakt, und spiel Updates ein (A9). Ein Programm bietet nach dem Einschalten einen Endpunkt mit Messwerten für Überwachungswerkzeuge an, etwa Tokens pro Sekunde und wartende Anfragen. Wie du daraus ein Monitoring baust, zeigt P9.

---

## Häufige Fehlgriffe

- **Nur das Antworttempo messen.** Ladezeit und Einlesen gehören dazu, sonst optimierst du am falschen Posten (Abschnitt 2).
- **Das Modell ständig neu laden lassen.** Bei Skripten mit Pausen kann das Laden mehr Zeit kosten als die Antwort.
- **Den Standardkontext übersehen.** Ein langer Text passt nicht hinein und wird je nach Programm gekürzt. Die Antwort klingt trotzdem überzeugend (Abschnitt 3).
- **Lokale Adresse mit lokaler Rechnung verwechseln.** Prüfe, ob das gewählte Modell wirklich auf deinem Gerät läuft (Abschnitt 4).
- **Plätze und Kontext gleichzeitig hochdrehen.** Der Speicher wächst mit dem Produkt aus beidem.
- **Fremde Messwerte für eigene halten.** Zahlen aus Dokumentationen zeigen das Prinzip, dein Rechner liefert andere.
- **Den Dienst für das Handy öffnen.** Ohne Schlüssel und Firewall ist das ein offenes Tor (Abschnitt 4).
- **Hardware nach Bauchgefühl kaufen.** Erst messen, welcher Wert fehlt, dann gezielt kaufen.

---

## Zum Ausprobieren

1. Starte dein Modell aus A9 als Dienst und schicke eine Anfrage im kompatiblen Format. Notiere Adresse und Port aus der Hilfe deines Programms.
2. Lies aus der Antwort die Zeitangaben ab, die dein Programm liefert. Schicke dieselbe Anfrage sofort noch einmal. Solange das Modell geladen bleibt, sollte die Ladezeit fast verschwinden.
3. Ändere immer nur eine Größe. Schicke einen kurzen und einen langen Abschnitt mit je drei Fragen und vergleiche das Einlesen. Schicke dann denselben Abschnitt mit drei und mit zwanzig Fragen und vergleiche die Antwortzeit. Notiere jeweils auch die Zahl der Tokens, dann vergleichst du Tempo statt nur Gesamtzeit.
4. Sieh nach, welchen Kontext dein Programm eingestellt hat. Passt dein längster Wiki-Abschnitt hinein?
5. Rechne mit dem Programm aus Abschnitt 3 aus, was zwei Plätze mit je 16.384 Token kosten würden. Prüfe danach, ob das in deinen freien Speicher passt.
6. Prüfe, auf welcher Adresse dein Dienst lauscht. Steht dort etwas anderes als 127.0.0.1 oder ::1, finde heraus, warum.

---

## Fazit

Aus dem Gewächshaus wird ein Hofladen, sobald das Modell als Dienst läuft und Programme es über eine Schnittstelle ansprechen. Die Zeit verteilt sich auf Laden, Einlesen und Antworten, und jede Antwort liefert die Zahlen dafür mit. Der Speicher teilt sich zwischen Modell, Kontext und parallelen Plätzen auf, und im einfachen Rechenmodell bestimmen Plätze mal Kontext den Zwischenspeicher. Für den Dauerbetrieb sorgt der Dienstverwalter, für die Sicherheit eine geschlossene Tür und, wenn nötig, ein Schloss davor. Neue Hardware kaufst du erst, wenn deine Messung zeigt, welcher Wert fehlt. Als Nächstes geht es in P2 um die Schnittstelle selbst: wie Anfragen aufgebaut sind, wie Streaming funktioniert und was bei Cloud-Diensten pro Token kostet.

```yaml
dokument: ki-p1-lokale-modelle-betreiben
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
block: profi
status: final
stand: 2026-11-03
quellen_fachlich:
  - "llama.cpp, tools/server/README.md (Commit 20a51f2 vom 2026-11-03, Zugriff 2026-11-03): Standard-Host 127.0.0.1, Standard-Port 9931 (Docker-Beispiel derselben Datei mit 8080); -c Kontext (0 = aus dem Modell), -ngl Standard auto, -np Standard auto, --fit Standard on; --api-key; --metrics (Prometheus, u. a. Token/s und requests_deferred); /health ohne API-Schlüssel; OpenAI-kompatibel /v1/chat/completions; timings-Objekt mit prompt_per_second und predicted_per_second; CORS-Tabelle: öffentlich API-Schlüssel und Reverse Proxy; --tools, --agent, MCP-Optionen 'do not enable in untrusted environments'; --sleep-idle-seconds Standard -1 (deaktiviert), Modell bleibt also geladen; -kvu gemeinsamer Zwischenspeicher, standardmäßig an, wenn die Zahl der Plätze auf auto steht; --kv-unified-per-slot als Grenze je Platz; -a/--alias setzt den Modellnamen für die API; model-Feld im Einzelmodellbetrieb laut Abschnitt zu /v1/chat/completions/control ignoriert, im Router-Betrieb zur Auswahl genutzt; zu /v1/chat/completions 'no strong claims of compatibility with OpenAI API spec'"
  - "llama.cpp, tools/llama-bench/README.md (Zugriff 2026-11-03): Beispiel qwen2 7B Q4_K - Medium, CUDA: pp512 7340,20 t/s, tg128 120,60 t/s"
  - "llama.cpp, tools/quantize/README.md (Zugriff 2026-11-03): Genauigkeitsverlust gemessen über Perplexität und KL-Divergenz, durch imatrix verringerbar"
  - "Ollama-Dokumentation im Repo ollama/ollama, docs/ (Commit 355eaee vom 2026-11-03, Zugriff 2026-11-03): faq.mdx (Bindung 127.0.0.1:11434, keep_alive Standard 5 Minuten, OLLAMA_KEEP_ALIVE, OLLAMA_NUM_PARALLEL Standard 1, 'Required RAM will scale by OLLAMA_NUM_PARALLEL * OLLAMA_CONTEXT_LENGTH', OLLAMA_MAX_QUEUE 512 und 503 bei Überlast, OLLAMA_KV_CACHE_TYPE f16/q8_0 etwa halb, q4_0 etwa ein Viertel, nur bei aktivem Flash Attention, globale Einstellung; Einstellung per systemctl edit; OLLAMA_NO_CLOUD=1 schaltet Cloud-Funktionen ab; Zeile 25 nennt pauschal 4096 Token Standardkontext); context-length.mdx (Standardkontext nach VRAM: unter 24 GiB 4k, 24 bis 48 GiB 32k, ab 48 GiB 256k); api.md (eval_count, eval_duration in ns, Beispielantwort mit total_duration 10706818083, load_duration 6338219291, prompt_eval_count 26, prompt_eval_duration 130079000, eval_count 259, eval_duration 4232710000); api/openai-compatibility.mdx (lokal unter http://localhost:11434/v1/, API-Schlüssel nötig, aber ignoriert); api/authentication.mdx (lokale API ohne Anmeldung); linux.mdx (systemd-Dienst mit Restart=always, journalctl -e -u ollama)"
  - "NVIDIA Developer Blog: Mastering LLM Techniques: Inference Optimization. https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization (Zugriff 2026-11-03): Prefill als 'matrix-matrix operation that's highly parallelized', Decode 'memory-bound'; Batching verteilt die Speicherkosten der Gewichte, KV-Cache je Anfrage separat"
  - "Eigene Artikel der Reihe: A4 (Karteikarten), A7 (Testfälle), A8 (Prüfung), A9 (Dateigröße, Zwischenspeicher 57.344 Byte pro Token, Bandbreiten-Denkmodell, Sicherheit, CVE, offene Instanzen), D1 (Kontext), D6 (MoE); Vorwärtsverweise auf P2, P5, P8, P9, R3"
  - "Rechnungen am 2026-11-03 mit Python ausgeführt: Beispielantwort 6,3 s Laden, 200 Token/s Einlesen, 61,2 Token/s Antwort, 59 % Ladeanteil; Zwischenspeicher 1,75 GiB (1 x 32.768 und 4 x 8.192), 7,00 GiB (4 x 32.768), jeweils halbiert bei 8 Bit"
verifikation_offen:
  - "Befehle beider Beispielboxen aus der Dokumentation, nicht selbst ausgeführt (kein Modellzugriff in der Arbeitsumgebung). Ports und Standardwerte vor Final erneut gegen die Dokumentation prüfen"
  - "Die Beispielantwort der Dokumentation nennt keine Hardware; die Werte zeigen das Prinzip, keine typische Leistung"
  - "Halbierung des Zwischenspeichers bei 8 Bit nach der Ollama-Dokumentation ('approximately 1/2'), in der Rechnung vereinfacht als exakt halb"
  - "Dass Ollama den Speicherbedarf als Plätze mal Kontext beschreibt, ist dokumentiert; llama.cpp nutzt standardmäßig einen gemeinsamen Zwischenspeicher für alle Plätze, die Aufteilung kann dort anders aussehen"
  - "Ollama-Dokumentation widersprüchlich zum Standardkontext: context-length.mdx nach Grafikspeicher (unter 24 GiB 4k), faq.mdx pauschal 4096 Token; im Text als 'laut einer Seite der Dokumentation' formuliert"
  - "Zeitfelder je Programm verschieden: Ladezeit stammt aus der Ollama-Antwort, llama.cpp liefert ein timings-Objekt ohne Ladezeit; bei Prompt-Cache zählt prompt_eval_duration nur die nicht zwischengespeicherten Tokens"
  - "Dass das model-Feld im Einzelmodellbetrieb ignoriert wird, steht wörtlich nur beim Steuer-Endpunkt; für /v1/chat/completions abgeleitet aus dem Beispiel der Dokumentation mit beliebigem Namen und der Router-Beschreibung"
  - "Vorwärtsverweise auf P2, P5, P8, P9, R3 beim Anlegen dieser Artikel abgleichen"
review_historie:
  - runde: 0
    datum: 2026-11-03
    ergebnis: "Erster Draft nach den schlankeren Regeln für Welle 3. Quellen aus den aktuellen Repos von llama.cpp und Ollama gelesen, Rechnungen mit Python ausgeführt."
  - runde: 1
    datum: 2026-11-03
    ergebnis: "Drei Reviews, gegen die Dokumentation geprüft. Übernommen: Beispiele für beide Programme getrennt mit Platzhalter für den Modellnamen und -np 1; Zeitfelder je Programm; Entladeverhalten beider Programme; Plätze mal Kontext als Rechenmodell eines Programms, gemeinsamer Zwischenspeicher beim anderen; KV-Cache benannt; Halbierung als ungefähr; Flash Attention und globale Einstellung; Perplexität und KL-Divergenz getrennt erklärt; Loopback mit ::1; fehlende Anmeldung bei einem Programm, HTTPS, Cloud-Modelle über lokalen Dienst; systemd-Neustart nur laut Dienstbeschreibung; --metrics; Übung 3 mit je einer Größe; A8 im Text. Nicht übernommen: Einwand gegen 57.344 Byte pro Token (passt zum A9-Modell mit 4 Schlüssel-Wert-Köpfen); Satz, -c reserviere Speicher ohne ihn zu verbrauchen (nicht belegt); abstraktere Formulierung der Kasse."
  - runde: 2
    datum: 2026-11-03
    ergebnis: "Drei Re-Reviews, gegen die Dokumentation geprüft. Übernommen: Laden je Programm beim Start oder beim ersten Aufruf; model-Feld bei llama.cpp im Einzelmodellbetrieb ohne Rolle; gemeinsamer Zwischenspeicher genauer, logisch getrennt je Anfrage; Widerspruch der Ollama-Dokumentation zum Standardkontext offen benannt; Anmeldeschutz statt Schlüssel für beide Programme; HTTPS auf nicht vertrauenswürdigen Verbindungen; Gesprächsverlauf im Kontext; Tokens in Übung 3; Teilmenge des Formats; aktivierter Dienst bei systemd; Fazit an das Rechenmodell gebunden. Nicht übernommen: Authorization-Header im curl-Beispiel (stattdessen Satz auf Programmbibliotheken eingegrenzt); Semikolon bei Perplexität (Stilblatt kurze Sätze)."
  - runde: 3
    datum: 2026-11-03
    ergebnis: "Freigabe durch David am 2026-11-03 nach Runde 2. Kopfzeile und YAML-Status gemeinsam auf final; offene Punkte unter verifikation_offen bleiben."
```
