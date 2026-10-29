# LLM/KI/Thinking-Modelle – Praxisleitfaden für IT, Umschulung und lokale Workflows

| **Zielgruppe** | Umschüler FIAE/FISI, 2. Lehrjahr |
|----------------|----------------------------------|
| **Kontext**    | Technologie-Überblick / Markteinordnung (kein klassischer Prüfungsstoff) |
| **Lernzeit**   | Ca. 20–25 Minuten |
| **Status**     | Final |
| **Stand**      | 07/2026 |

---

## Überblick

Der aktuelle Stand wird von drei Entwicklungen geprägt: **Reasoning-/Thinking-Modelle**, **extrem große Kontextfenster** und **lokal einsetzbare Open-Weight-Modelle**, die in vielen Standardaufgaben bereits brauchbar sind.

Gleichzeitig bleibt die Grenze zwischen Frontier-Cloudmodellen und lokalen Setups real: Die besten Ergebnisse liefern weiterhin meist die großen proprietären Modelle, während lokale Modelle durch Datenschutz, Kostenkontrolle und Offline-Nutzung punkten.

> **Grundprinzip:** Cloud liefert die höchste Qualität, lokal liefert die höchste Kontrolle. Die Kunst liegt darin, beides gezielt zu kombinieren statt sich für "die eine Lösung" zu entscheiden.

- Bei **proprietären Systemen** sind vor allem OpenAI, Anthropic und Google mit erweiterten Reasoning-Modi, Tool-Use und multimodalen Fähigkeiten relevant.
- Im **Open-Weight-Bereich** sind Modelle wie DeepSeek-R1, Qwen3-Varianten und aktuelle Llama-Ableger zentral, weil sie starke Leistung mit lokalem Betrieb kombinieren.
- **Riesige Kontextfenster** sind inzwischen möglich, aber die praktische Nutzbarkeit hängt stark von Latenz, Speicherbedarf und Kosten ab.

---

## 1. Beste Ergebnisse vs. freie Version

Wenn es um maximale Qualität geht, liefern weiterhin die großen Cloud-Modelle mit Reasoning-Fokus die besten Ergebnisse – besonders bei komplexem Code, mehrstufigen Analysen und multimodalen Aufgaben. In der freien Version hängt das Ergebnis stark davon ab, welches Modell kostenlos zugänglich ist und ob die Nutzung gedrosselt wird.

| Aspekt | Beschreibung |
|--------|-------------|
| Maximale Qualität | Große Cloud-Modelle mit explizitem Reasoning-Modus schlagen reine Chatmodelle gleicher Größe bei komplexen Denkaufgaben deutlich. |
| Freie Nutzung, hohe Qualität | Open-Weight-Modelle, lokal betrieben, sind oft die beste kostenlose Alternative. |
| Alltagsaufgaben | Kleinere freie Modelle reichen für Textarbeit und einfache Codehilfe aus, wenn der Prompt gut strukturiert ist. |

---

## 2. Open Source vs. Open Weight

Hier ist eine saubere Trennung wichtig – die Begriffe werden oft fälschlich synonym verwendet.

| Begriff | Bedeutung | Praktische Konsequenz |
|---------|-----------|----------------------|
| **Echt Open Source** | Code und Gewichte unter permissiver Lizenz (z. B. Apache-2.0, MIT), ohne problematische Zusatzklauseln | Freie Integration in eigene Produkte, Weitertraining und kommerzielle Nutzung möglich |
| **Open Weight** | Gewichte sind verfügbar, aber Nutzung kann eingeschränkt sein | Lizenzbedingungen prüfen: Umsatzschwellen, Nutzungsverbote, Regeln für Weitertraining |

> **Merksatz:** "Die Gewichte offen zu bekommen heißt nicht automatisch, dass man sie frei nutzen darf." Für Firmen ist diese Unterscheidung juristisch relevant, weil sie beeinflusst, ob ein Modell ohne Sonderprüfung in Produkte oder Kundenlösungen integriert werden kann.

---

## 3. Wann lokal Sinn macht

Lokal sinnvoll ist alles, was Datenschutz, Kostenkontrolle, Offline-Fähigkeit, Reproduzierbarkeit oder geringe Latenz braucht.

| Szenario | Lokal sinnvoll? | Begründung |
|----------|----------------|-------------|
| Interne Dokumente, vertraulicher Code | ✅ Ja | Daten verlassen das System nicht |
| Sensible Kundendaten | ✅ Ja | Datenschutzpflichten leichter einhaltbar |
| Lernumgebungen | ✅ Ja | Kostenkontrolle, Wiederholbarkeit |
| Viele kleine Anfragen | ✅ Ja | Cloud-API-Kosten summieren sich schnell |
| Anspruchsvolle Reasoning-Aufgaben | ❌ Eher nein | Hardware-Limits, Qualitätsverlust |
| Maximale Antwortqualität nötig | ❌ Eher nein | Cloud-Modelle sind meist überlegen |

---

## 4. Mindest-Hardware-Anforderungen

Die konkrete Mindesthardware hängt vom Modell, der Quantisierung und der gewünschten Geschwindigkeit ab.

| Nutzungsszenario | Empfohlene Hardware |
|------------------|----------------------|
| Einfacher Einstieg | 16 GB RAM, moderne CPU – für 7B-Modelle mit 4‑Bit-Quantisierung (z. B. Llama 3.1 8B, Qwen 2.5 7B, Q4_K_M) |
| Komfortable Alltagsarbeit (kleinere Modelle) | 32 GB RAM |
| Größere Modelle / längere Kontexte | Dedizierte Nvidia-GPU mit ausreichend VRAM |
| Effiziente Unified-Memory-Nutzung | Apple Silicon – mit 16 GB flüssig für 7B-Modelle (Q4), mit 32–64 GB auch 30B+ möglich, aber weniger flexibel bei sehr großen Modellen/Toolchains |
| Autocomplete, sehr niedrige Latenz | Kleine, speicherarme Modelle (1.5B–3B) statt "zu große" lokale Modelle |

---

## 5. Vorteile lokaler LLMs

> **Grundprinzip:** Lokale Modelle tauschen Spitzenleistung gegen Kontrolle – das ist ein bewusster Trade-off, kein Kompromiss aus Mangel.

| Vorteil | Beschreibung |
|---------|-------------|
| Datenschutz | Daten verlassen Gerät oder Netzwerk nicht |
| Kostenkontrolle | Keine laufenden API-Kosten pro Anfrage |
| Offline-Nutzbarkeit | Arbeit auch ohne Internet möglich |
| Anpassbarkeit | Eigene Prompts, RAG-Pipelines, Integrationen frei gestaltbar |
| Reproduzierbarkeit | Gleiche Modellversion + gleiche Parameter = stabile Testbedingungen |

Der wichtigste Nachteil: Lokale Modelle sind oft schwächer als Frontier-Cloudmodelle und brauchen mehr Pflege – besonders bei Updates, Quantisierung und Hardware-Abstimmung.

---

## 6. Umsetzbarkeit in der Praxis

Praktisch ist lokale Nutzung heute sehr gut umsetzbar, wenn man die Erwartungen richtig setzt.

Typische Bausteine für einen soliden Einstieg:

| Baustein | Funktion |
|----------|----------|
| **Ollama** (oder vergleichbares Backend) | Lokales Modell-Backend |
| **Open WebUI** | Browser-Oberfläche |
| **Continue.dev** | IDE-Integration |

Für lokale Wissensarbeit ist **RAG** (Retrieval-Augmented Generation) in der Regel der pragmatischere Ansatz als ein riesiger Prompt-Kontext. Für einmalige Analysen großer Textmengen kann **Long-Context** sehr stark sein, aber bei laufender Nutzung steigen Speicherbedarf, Latenz und Komplexität deutlich.

**Workflow-Vergleich:**

| RAG-Ansatz | Long-Context-Ansatz |
|---|---|
| Dokumente → Chunking | Kompletter Text |
| Embeddings → Vektor-DB | Direkt in den Prompt |
| Gezielter Abruf bei Anfrage | Gesamter Kontext wird verarbeitet |
| ✅ Skaliert gut | ✅ Einfacher Aufbau |
| ✅ Günstiger im Betrieb | ✅ Kein Retrieval-Fehler |
| ⚠️ Retrieval kann Fehler haben | ⚠️ Hohe Kosten und Latenz |
| ⚠️ Mehr Infrastruktur | ⚠️ Begrenzt bei sehr großen Datenmengen |


---

## 7. Aktuelle Meinungen von Redakteuren und Profi-Nutzern

In der Fachöffentlichkeit und unter Power-Usern dominiert ein hybrides Bild:

- **Cloud bleibt Maßstab für Spitzenqualität**, vor allem bei anspruchsvollen Denk- und Codieraufgaben.
- **Lokal bleibt Standard für Kontrolle, Datenschutz und Kosten.**
- Viele erfahrene Nutzer sehen lokale Modelle nicht als Ersatz, sondern als **zweite Schiene** neben Cloud-LLMs.

Typische Empfehlung aus der Praxis:

| Anwendungsfall | Empfohlener Modelltyp |
|----------------|----------------------|
| Alltag, interne Daten, Vorarbeit | Lokal |
| Besonders schwierige Fälle, Review, Spezialaufgaben | Cloud |

---

## 8. Kontext nutzen in einer IT-Umschulung

Für eine IT-Umschulung ist KI besonders wertvoll als **Meta-Lernwerkzeug** – nicht als Ersatz für eigenes Verständnis.

> **Grundprinzip:** KI-Ergebnisse sind ein Ausgangspunkt zur Überprüfung, kein Endpunkt zum Abschreiben.

**Sinnvoller Einsatz:**

- Erklärungen in einfacher Sprache
- Code-Review
- Fehleranalyse
- Übungsaufgaben generieren lassen
- Gegenfragen und Wissenschecks

**Didaktisch stärkste Kombination** – der Kreislauf des Lernens:

```mermaid
flowchart TD
    A["💡 Eigene Lösung erstellen"]
    B["🤖 KI analysiert und kritisiert"]
    C["📚 Mit Dokumentation vergleichen"]
    D["🔧 Refactoring und Verbesserung"]
    E["✅ Neues Verständnis"]

    A --> B
    B --> C
    C --> D
    D --> E
    E -. Wissen vertiefen .-> A
```



> **⚠️ Kritischer Umgang mit KI-Antworten**

> Sprachmodelle können Informationen überzeugend, aber falsch darstellen („halluzinieren“). Behandle jede KI-generierte Antwort als starken Vorschlag, nicht als gesicherte Wahrheit. Entwickle einen Workflow zur Verifizierung – besonders bei Code-Reviews, Sicherheitsfragen und Architekturentscheidungen. Die Fähigkeit, KI-Outputs fachlich zu validieren, ist eine der wichtigsten neuen Kernkompetenzen.

**Praxis-Tipp:** Besonders lehrreich ist es, einmal selbst eine RAG-Pipeline und einmal einen Long-Context-Workflow zu bauen, um die Unterschiede praktisch zu verstehen – Theorie über Architekturunterschiede bleibt sonst abstrakt.

---

## 9. Relevanz für den IT-Markt – realistisch betrachtet

Realistisch gesehen werden LLMs den IT-Markt nicht vollständig ersetzen, aber sie verändern viele Aufgaben dauerhaft.

**Wachsende Nachfrage bei:**

- AI-gestützter Entwicklung
- Prompt- und Workflow-Design
- RAG-Integration
- Modellbewertung
- Governance und Compliance

**Klassische IT-Rollen verschieben sich:**

- Weniger manuelle Routine
- Mehr Kontrolle, Integration, Architektur und Qualitätsprüfung

> **Merksatz:** Die wichtigste Kompetenz für Einsteiger ist nicht "das beste Modell zu kennen", sondern Modelle sinnvoll einzuordnen und sicher einzusetzen.

---

## Merk-Sätze

- **Cloud liefert die Qualität, lokal liefert die Kontrolle** – wer beides versteht, trifft die richtige Wahl je nach Situation.
- **Open Weight ist nicht gleich Open Source** – die Lizenz entscheidet, was erlaubt ist, nicht die Verfügbarkeit der Gewichte.
- **RAG skaliert, Long-Context vereinfacht** – die Wahl hängt von Datenmenge und Nutzungsfrequenz ab.
- **KI-Ergebnisse gehören geprüft, nicht kopiert** – gerade in der Ausbildung zählt der Weg zur Lösung mehr als das Ergebnis selbst.

---

```yaml
titel: "LLM/KI/Thinking-Modelle – Praxisleitfaden"
typ: "Praxisleitfaden (kein IHK-Prüfungsstoff)"
zielgruppe: "FIAE/FISI Umschüler, 2. Lehrjahr"
stand: "2026-07"
status: "final"
schlagworte:
  - LLM
  - Reasoning-Modelle
  - Open Source vs Open Weight
  - lokale Modelle
  - RAG
  - Long-Context
  - Ollama
  - Hardware-Anforderungen

quellen:
  - https://openlm.ai/chatbot-arena/ 