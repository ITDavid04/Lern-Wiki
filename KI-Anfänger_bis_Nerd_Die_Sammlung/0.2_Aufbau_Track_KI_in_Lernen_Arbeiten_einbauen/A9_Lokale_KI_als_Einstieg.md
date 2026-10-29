# KI-A9 · Lokale KI als Einstieg: Das Modell läuft bei dir

*Freiwilliger Sidequest · Reihe „KI im Wiki" · Aufbau-Track, Artikel A9 · Typ C (ausführlich) · Final · Stand 2026*

---

## Worum es geht

Du willst den Entwurf eines Praktikumsberichts überarbeiten lassen, aber im Text stehen Namen und Interna des Betriebs. Oder du sitzt im Zug ohne Netz und möchtest trotzdem eine Frage zu Subnetting klären. Oder du bist neugierig, wie sich ein Sprachmodell anfühlt, das auf deinem eigenen Rechner läuft. In allen drei Fällen lohnt ein Blick auf lokale Modelle.

Am Ende kannst du erklären, was „lokal" technisch heißt und woraus ein lokales Setup besteht. Du schätzt mit einer Rechnung ab, welche Modelle auf deinen Rechner passen und wie schnell sie im Idealfall höchstens laufen. Du machst einen ersten Versuch, vergleichst das Ergebnis mit einem Cloud-Dienst und prüfst es mit dem Verfahren aus A8. Außerdem weißt du, worauf du bei Sicherheit, Lizenz und Regeln im Betrieb achten musst.

Mit „Werkzeug" ist in diesem Artikel das Sprachmodell oder der Chat-Assistent gemeint, mit dem du arbeitest. Vorausgesetzt wird der Einsteiger-Track E1 bis E8, besonders E2 (Werkzeugtypen), E6 (Grenzen) und E7 (Datenschutz). Aus dem Aufbau-Track brauchst du A7 für die Testfälle und A8 für die Prüfung. Der Artikel ist ein Einstieg. Technik im Detail folgt später (P1 für den Betrieb, D1 für Tokens und Kontext).

---

## 1. Was „lokal" heißt

Ein Cloud-Dienst ist wie ein Lieferdienst für die Gärtnerei: Du bestellst, am Morgen steht die Ware vor der Tür, und sie kommt aus einem riesigen Großlager. Ein lokales Modell ist das eigene Gewächshaus für den Eigenbedarf. Du hast weniger Auswahl, aber die Pflanzen stehen bei dir, und was du anbaust, bleibt im Gewächshaus, solange du die Tür zulässt.

Das Bild hinkt an einer Stelle: Du ziehst das Modell für diesen Einstieg nicht selbst. Das Training ist ein gewaltiger Aufwand, den ein Anbieter betreibt. Du lädst das fertige Ergebnis als Datei herunter und rechnest damit nur noch, du trainierst es nicht.

Ein lokales Setup besteht aus drei Bausteinen:

- **Modelldatei:** die Gewichte, also die Zahlen, die das Training hinterlassen hat. Sie ist je nach Modell einige Gigabyte groß.
- **Laufzeitprogramm:** ein Programm, das die Datei lädt und daraus Antworten Token für Token berechnet.
- **Oberfläche:** das Terminal, ein Chatfenster oder eine Schnittstelle auf deinem Rechner, über die andere Programme das Modell ansprechen können (P2).

Was sich zwischen Cloud und lokal unterscheidet, zeigt die Tabelle. Die Aussagen sind typische Tendenzen und keine Naturgesetze:

| | Cloud-Dienst | Lokal auf deinem Rechner |
| --- | --- | --- |
| Wo wird gerechnet | im Rechenzentrum des Anbieters | auf deinem Rechner |
| Wohin gehen deine Eingaben | zum Anbieter (E7) | bleiben auf dem Gerät, solange das Programm rein lokal arbeitet |
| Modellgröße und Qualität | meist die größten und stärksten Modelle | durch Speicher begrenzt, meist kleinere Modelle |
| Kosten | Abo oder Bezahlung nach Nutzung | Hardware, Strom und deine Zeit |
| Ohne Internet | nein | ja, nach dem Download |
| Pflege | der Anbieter aktualisiert | du aktualisierst selbst |

Die zweite Zeile verdient einen Zusatz. Dass Eingaben auf dem Gerät bleiben, gilt nur, wenn das Programm wirklich nichts nach außen schickt. Manche Programme bieten neben lokalen auch Cloud-Modelle an, und beim Modellwechsel merkst du den Unterschied nicht immer sofort. Abschnitt 5 zeigt, wie du das prüfst.

---

## 2. Was passt auf deinen Rechner?

Ins Gewächshaus passen nur so viele Pflanzen, wie Platz ist. Der Rest steht draußen und muss mühsam versorgt werden. Beim Modell entscheidet der Speicher, ob es komplett hineinpasst oder teilweise ausgelagert werden muss, was die Antworten verlangsamen kann.

### Die Dateigröße

Die reine Größe der Gewichte lässt sich überschlagen. Die tatsächliche Datei kann etwas größer sein, weil auch Metadaten darin stehen. Ein Modell hat eine bestimmte Zahl an **Parametern**, vereinfacht gesagt den beim Training gelernten Zahlenwerten, die in diesem Artikel Gewichte heißen (Abschnitt 1). Bei einem „8B"-Modell sind es etwa 8 Milliarden. Jeder Parameter belegt Speicher, und wie viel, hängt von der Genauigkeit ab, in der er gespeichert wird. Diese Genauigkeit heißt **Quantisierung**: Die Zahlen werden mit weniger Bits abgelegt, ähnlich wie eine Waage, die nur noch auf zehn Gramm statt auf ein Gramm genau anzeigt. Die Datei wird kleiner, und je gröber die Rundung, desto eher kann die Qualität leiden. Wie stark, hängt vom Modell und vom Verfahren ab.

Die Faustformel:

```text
Dateigröße in Byte ≈ Parameter × Bits pro Gewicht ÷ 8
```

Ein kleines Python-Programm rechnet sie für ein Modell mit 8 Milliarden Parametern aus. Die Bits pro Gewicht stammen aus der Dokumentation eines verbreiteten Quantisierungswerkzeugs, gemessen an einem Modell dieser Größe. Bei den gröberen Stufen ist es ein Mittelwert, weil nicht jede Schicht gleich fein gespeichert wird:

```python
def gigabyte(milliarden, bits):
    return milliarden * 1e9 * bits / 8 / 1e9

for name, bits in [("16 Bit", 16.0), ("8 Bit (ca. 8,5)", 8.5), ("4 Bit (ca. 4,9)", 4.89)]:
    print(name, round(gigabyte(8, bits), 1), "GB")
```

Ausgabe:

```text
16 Bit 16.0 GB
8 Bit (ca. 8,5) 8.5 GB
4 Bit (ca. 4,9) 4.9 GB
```

Dasselbe Modell braucht also ungefähr 16, 8,5 oder 4,9 Gigabyte, je nachdem, wie fein es gespeichert ist. Auf Modellseiten begegnen dir dafür Kürzel wie Q8_0 (rund 8,5 Bit) und Q4_K_M (rund 4,9 Bit). Das Beispiel rechnet mit glatten 8 Milliarden Parametern, die Dokumentation nennt genauer 8,03 Milliarden. Zur Gegenprobe: Für das 16-Bit-Modell mit 8,03 Milliarden Parametern nennt die Dokumentation 14,96 GiB (Gibibyte), die Rechnung ergibt 16,06 GB (Gigabyte). Das ist dieselbe Größe in zwei Einheiten, denn 1 GiB entspricht etwa 1,074 GB. Dieser Artikel rechnet mit GB, Betriebssysteme und Modellseiten zeigen mal die eine, mal die andere Einheit.

### Der Zwischenspeicher

Die Datei ist aber nur ein Teil des Bedarfs, und sie ist keine verlässliche Angabe dafür, wie viel Speicher du wirklich brauchst. Zusätzlich braucht das Laufzeitprogramm Platz für den Rechenprozess und interne Puffer. Beim Antworten merkt sich das Modell außerdem den bisherigen Text in einem Zwischenspeicher, und der wächst mit der Länge des Gesprächs. Ein Beispiel mit den Werten eines offen dokumentierten Modells mit 7 Milliarden Parametern (28 Schichten, 4 Schlüssel-Wert-Köpfe, Kopfgröße 128, 2 Byte pro Wert):

```python
schichten, kv_koepfe, kopfgroesse, bytes_je_wert = 28, 4, 128, 2
pro_token = 2 * schichten * kv_koepfe * kopfgroesse * bytes_je_wert
print(pro_token, "Byte pro Token")
print(round(pro_token * 32768 / 2**30, 2), "GiB bei 32768 Token")
```

```text
57344 Byte pro Token
1.75 GiB bei 32768 Token
```

Bei voller Länge von rund 32.000 Token kommen bei diesem Modell also etwa 1,75 GiB dazu. Andere Modelle haben andere Werte, und die Formel selbst ist eine Vereinfachung, die für Modelle mit gruppierten Schlüssel-Wert-Köpfen gilt wie dieses. Andere Bauarten rechnen anders. Warum der Kontext diesen Speicher braucht, erklärt D1. Die Erkenntnis zählt mehr als die exakte Zahl: Ein längerer Kontext braucht zusätzlichen Speicher. Für den Einstieg reicht die Regel, über die Dateigröße hinaus Reserve einzuplanen.

### Die Geschwindigkeit

**Wo das Modell liegt, entscheidet über die Geschwindigkeit.** Passt es komplett in den schnellen Speicher der Grafikkarte, läuft es meist deutlich schneller als bei einer Aufteilung. Liegen Teile im normalen Arbeitsspeicher und werden vom Prozessor bedient, wird es langsamer. Gute Laufzeitprogramme zeigen dir an, wie die Aufteilung gerade aussieht (Beispielbox in Abschnitt 3).

Die Geschwindigkeit hängt beim Antworten oft stärker am Speicher als an der Rechenleistung. Eine Beschreibung der Funktionsweise von Sprachmodellen nennt die Erzeugung Token für Token einen speichergebundenen Vorgang: Die Zeit wird davon bestimmt, wie schnell die Gewichte aus dem Speicher zum Rechenwerk kommen. Daraus lässt sich ein Denkmodell ableiten. Angenommen, pro Token wird jedes Gewicht einmal gelesen und sonst kostet nichts Zeit. Dann ergibt die Speicherbandbreite (gelesene Gigabyte pro Sekunde) geteilt durch die Modellgröße die Token pro Sekunde, die unter diesen vereinfachten Annahmen im Idealfall höchstens möglich sind:

```python
modell_gb = 4.9
for bandbreite in (50, 400):
    print(bandbreite, "GB/s ->", round(bandbreite / modell_gb), "Token/s (Ideal-Obergrenze)")
```

```text
50 GB/s -> 10 Token/s (Ideal-Obergrenze)
400 GB/s -> 82 Token/s (Ideal-Obergrenze)
```

Die Bandbreiten sind angenommene Beispielwerte, keine Messungen deines Rechners. Die Rechnung ist ein eigenes Denkmodell und keine Aussage der Dokumentation. Die wirkliche Geschwindigkeit liegt meist darunter, weil auch Rechenzeit, Kontext und das Programm selbst Zeit kosten. Das Denkmodell zeigt aber, warum sich ein kleineres oder gröber gespeichertes Modell oft schneller anfühlt und warum Grafikspeicher mit hoher Bandbreite für lokale Modelle so gefragt ist. Es gibt Bauarten, bei denen pro Token nur ein Teil der Gewichte gelesen wird. Dort sieht die Rechnung anders aus (D6, P1).

---

## 3. Der erste Versuch

Für den Einstieg brauchst du keine neue Hardware. Probiere aus, was dein Rechner kann, und lerne dabei, wo seine Grenzen liegen. Die Anschaffung eines eigenen Rechners für lokale Modelle ist ein Thema für später (P1).

Ein Ablauf, der sich bewährt:

1. **Nachsehen, was du hast.** Wie viel Arbeitsspeicher ist da, und hat der Rechner eine Grafikkarte mit eigenem Speicher? Beides findest du in den Systeminformationen.
2. **Ein Laufzeitprogramm aus der offiziellen Quelle installieren.** Nicht von Download-Portalen, die nur Kopien anbieten.
3. **Ein kleines Modell wählen.** Starte mit einer Datei, die deutlich kleiner ist als dein freier Speicher, denn Kontext, Betriebssystem und andere Programme brauchen Reserve. Wie viel, hängt von Modell und Kontextlänge ab (Abschnitt 2), also beginne lieber zu klein und taste dich hoch. Parameterzahl, Dateigröße und Qualität sind keine austauschbaren Maße: Mehr Parameter heißen nicht automatisch bessere Antworten. Die Dateigröße steht auf der Seite des Modells.
4. **Ein paar Fragen stellen** und beobachten, wie schnell die Antworten kommen.
5. **Auslastung ansehen.** Läuft das Modell im Grafikspeicher, im Arbeitsspeicher oder geteilt?

Die konkrete Bedienung unterscheidet sich je nach Programm, deshalb zeigt eine Beispielbox einen Weg:

> **Beispielbox, Stand 08.10.2026: Ollama.** Die Befehle sind der Dokumentation entnommen und nicht selbst ausgeführt. Den Modellnamen gemma4 führt die Modellbibliothek des Programms, doch Namen und Verfügbarkeit ändern sich.
>
> ```bash
> ollama pull gemma4     # Modell herunterladen
> ollama run gemma4      # Modell starten und im Terminal chatten
> ollama ls              # heruntergeladene Modelle auflisten
> ollama ps              # laufende Modelle und ihre Auslastung anzeigen
> ollama stop gemma4     # Modell beenden
> ollama rm gemma4       # Modell löschen
> ```
>
> Die Standardgröße eines Modells kann deinen Rechner überfordern. Die Modellseite nennt je nach Variante unterschiedliche Größen, lies deshalb vor dem Download die konkrete Angabe zur Dateigröße. In der Spalte „Processor" von `ollama ps` siehst du, ob das Modell komplett im Grafikspeicher (GPU), komplett im Arbeitsspeicher (CPU) oder geteilt läuft. Ein Beispiel für geteilt ist die Angabe 48 % CPU und 52 % GPU. Ein Namenszusatz `:cloud` kennzeichnet laut Dokumentation Modelle, die in der Cloud des Anbieters laufen und nicht auf deinem Rechner.

Dieselbe Beispielbox zeigt, worauf du bei der Einordnung achtest: Ein Modell, das du über das Programm startest, muss nicht lokal laufen. Prüfe den Namen und die Einstellungen, bevor du etwas Vertrauliches eingibst.

---

## 4. Wie gut ist das Ergebnis?

Jetzt kommt der Teil, der aus dem Versuch eine Erkenntnis macht. Nimm die drei Testfälle aus A7 (Normalfall, Randfall, schwieriger Fall) und lass dieselbe Vorlage in deinem lokalen Modell und in einem Cloud-Dienst laufen. Protokolliere das Ergebnis wie in A8 beschrieben: was geprüft ist, was nicht, welche Fehler du gefunden hast.

Worauf du achtest:

- **Fakten:** Stimmen Zahlen, Namen und Begriffe? Kleine Modelle erfinden bei Faktenfragen oft mehr, aber das ist eine Erwartung und kein Gesetz. Prüfe es an deinen Aufgaben.
- **Sprache:** Schreibt das Modell sauberes Deutsch, oder rutscht es ins Englische? Das lässt sich nur ausprobieren.
- **Befolgen der Vorgaben:** Hält es Länge und Format aus der Vorlage ein?
- **Geschwindigkeit:** Ist die Antwortzeit für deine Arbeit noch brauchbar?

Zwei Dinge gelten für lokale Modelle genauso wie für Cloud-Modelle. Das Modell kennt nur den Stand seines Trainings, und ohne Suchfunktion schlägt es nichts nach (E6). Außerdem kann es dir Fehler mit sicherem Ton liefern (A8).

Als Erfahrungswert ohne Quelle eignen sich kleinere Modelle eher für kurze, klar umrissene Aufgaben: Text umformulieren, einen kurzen Abschnitt zusammenfassen, Code erklären, Einträge sortieren. Bei anspruchsvollem Faktenwissen, sehr langen Texten und Aufgaben mit mehreren Schritten stoßen sie dagegen schneller an Grenzen. Ob das für deine Aufgabe zählt, zeigt dein eigener Test mit den drei Fällen. Er ist aussagekräftiger als jede Faustregel.

Noch eine Verbindung zu A8: Ein lokales Modell kann eine Zweitmeinung liefern, wenn der Text vertraulich ist und nicht in einen Cloud-Dienst soll. Die Grenzen der Zweitmeinung bleiben aber dieselben. Auch ein lokales Modell kann ähnliche Fehler machen wie das erste, und „nichts gefunden" ist kein Freispruch.

---

## 5. Sicherheit, Lizenz und Regeln

Lokal heißt nicht automatisch sicher. Es heißt nur, dass die Verantwortung bei dir liegt.

**Den Dienst nicht ins Netz stellen.** Viele Laufzeitprogramme starten einen kleinen Server auf deinem Rechner, damit andere Programme das Modell ansprechen können. Bei einem verbreiteten Programm ist laut Dokumentation standardmäßig nur der eigene Rechner erreichbar. Das Risiko beginnt, wenn jemand das ändert, etwa um vom Handy zuzugreifen, und keinen Schutz einrichtet.

Dass so etwas vorkommt, zeigt eine Untersuchung des Sicherheitsanbieters Intruder, die die Cloud Security Alliance im Mai 2026 zusammenfasst. Von über 5.200 öffentlich auffindbaren Instanzen eines verbreiteten Laufzeitprogramms, die eine Modellliste preisgaben, antworteten 31 Prozent auf eine Testanfrage ohne Anmeldung (Authentifizierung). Die Zahl gilt nur für diese Stichprobe öffentlich erreichbarer Instanzen und nicht für alle Installationen, und der Anbieter hat ein geschäftliches Interesse an solchen Befunden. Als Warnung taugt sie trotzdem: Aus einem Lernversuch wird schnell ein offenes Tor.

Praxisregel: Lass den Dienst standardmäßig nur auf dem eigenen Rechner erreichbar. Zugriff aus dem Heimnetz oder Internet richtest du nur ein, wenn du weißt, wie du ihn absicherst, mindestens mit Anmeldung und passenden Netzwerkregeln (R3, R4).

**Software aktuell halten.** Für ein verbreitetes Laufzeitprogramm wurde im Mai 2026 die Schwachstelle CVE-2026-7482 veröffentlicht. Beim Verarbeiten einer präparierten Modelldatei konnte der Server Speicherinhalte lesen. Laut Beschreibung verlangten die betroffenen Schnittstellen keine Anmeldung. Steht ein solcher Dienst offen im Netz, kann die Schwachstelle deshalb besonders gefährlich sein, weil ein Angreifer die Schnittstelle erreichen kann, ohne sich anzumelden. Den Schweregrad 9.1 von 10 hat die meldende Stelle vergeben, eine eigene Bewertung der US-Datenbank NVD lag zuletzt nicht vor. Wer den Dienst nur lokal laufen lässt, ist weniger betroffen, weil der Angriff Zugriff auf die Schnittstelle voraussetzt. Der Fehler ist in neueren Versionen behoben. Daraus folgt: Updates einspielen und Modelle nur aus Quellen laden, die du kennst.

**Modelldateien sind keine harmlosen Dokumente.** Manche Formate können beim Laden Programmcode ausführen. Die Dokumentation einer großen Modellplattform warnt, Dateien im sogenannten Pickle-Format nicht aus unbekannten Quellen zu laden. Als Alternative nennt eine weitere Dokumentation dieser Plattform das Format safetensors, das sie als reine Daten beschreibt. Die Plattform prüft hochgeladene Dateien zwar teilweise, schreibt aber selbst, dass dies nicht hundertprozentig sicher ist. Ein Datenformat senkt dieses Risiko, macht eine Datei aus unbekannter Quelle aber nicht vertrauenswürdig. Praxisregel: Lade Modelle möglichst von der offiziellen Seite des Modellherstellers oder von einer Plattform mit nachvollziehbarer Herkunft. Bevorzuge Formate, die nur Daten enthalten, und führe unbekannte Skripte, die mit einem Modell mitgeliefert werden, nicht ungeprüft aus (A5, A7).

**Offene Gewichte sind nicht automatisch Open Source.** Viele Modelle werden als „offen" oder „Open Weights" bezeichnet, weil du die Gewichte herunterladen kannst. Die Open Source Initiative hat im Oktober 2024 eine Definition für Open-Source-KI veröffentlicht. Sie verlangt neben den Parametern auch ausreichende Informationen über die Trainingsdaten und den vollständigen Code, jeweils unter freien Bedingungen. Die Lizenzen der heruntergeladenen Modelle unterscheiden sich stark. Manche erlauben die Nutzung im Betrieb, andere schränken sie ein. Lies die Lizenz, bevor du ein Modell im Praktikum oder für eigene Projekte verwendest (D6).

**Im Betrieb gelten Regeln.** Auch ein lokales Programm ist Software, die ein Betrieb freigeben muss. Dass die Daten auf dem Gerät bleiben, ersetzt keine Prüfung der Datenschutzregeln (R1), und eigene Werkzeuge auf Firmenrechnern sind ein klassischer Fall von Schatten-KI (R4). Frag im Praktikum nach, bevor du etwas installierst (R6).

---

## Häufige Fehlgriffe

- **„Lokal heißt sicher."** Es heißt nur, dass du selbst für die Absicherung zuständig bist (Abschnitt 5).
- **Zu große Modelle laden.** Wenn die Datei kaum in den Speicher passt, bleibt kein Platz für den Kontext, und alles wird zäh. Rechne vorher (Abschnitt 2).
- **Die Datei allein vergleichen.** Parameterzahl, Dateigröße und Qualität sind keine austauschbaren Maße, und zwei Modelle derselben Größe können sehr unterschiedlich gut sein. Entscheidend ist dein eigener Test (Abschnitt 4).
- **Die Quantisierung ignorieren.** Dasselbe Modell kann in mehreren Stufen angeboten werden. Die Beschreibung auf der Modellseite sagt, welche du bekommst.
- **Den Dienst im Netz offen lassen.** Ein vergessener Zugang für das Handy ist eine mögliche Falle (Abschnitt 5).
- **Nicht merken, dass ein Cloud-Modell läuft.** Prüfe vor vertraulichen Eingaben, wo gerechnet wird.
- **Dem Ergebnis mehr trauen, weil es lokal entstand.** Ein lokales Modell erfindet genauso. Prüfen musst du trotzdem (A8).
- **Lizenz und Betriebsregeln überspringen.** Gerade im Praktikum zählt, was erlaubt ist (R4, R6).

---

## Zum Ausprobieren

1. Notiere, wie viel Arbeitsspeicher dein Rechner hat und ob er eine Grafikkarte mit eigenem Speicher besitzt. Ändere im Programm aus Abschnitt 2 die Zahlen. Wie groß wäre ein Modell mit 3, 7 und 14 Milliarden Parametern bei etwa 4,9 und bei etwa 8,5 Bit? Welche liegen deutlich unter deinem freien Speicher, sodass noch Reserve für den Kontext bleibt?
2. Installiere ein Laufzeitprogramm aus der offiziellen Quelle und lade ein kleines Modell. Stelle drei Fragen und notiere, wie schnell die Antworten kommen.
3. Sieh nach, wo das Modell läuft (Grafikspeicher, Arbeitsspeicher oder geteilt), und vergleiche mit deiner Rechnung. Passt die Größenordnung?
4. Lass die Vorlage aus A7 mit den drei Testfällen im lokalen Modell und in einem Cloud-Dienst laufen. Protokolliere die Unterschiede nach A8.
5. Prüfe in der Dokumentation deines Programms, auf welcher Adresse der Dienst standardmäßig lauscht, und sieh nach, ob du daran etwas geändert hast. Schreibe auf, was du gefunden hast. Eine Änderung nimmst du erst vor, wenn du sie absichern kannst.

Am Ende hast du ein Gefühl dafür, was ein lokales Modell kann und was nicht, und eine Rechnung, mit der du Modelle für deinen Rechner vorab einschätzt.

---

## Fazit

Ein lokales Modell besteht aus Modelldatei, Laufzeitprogramm und Oberfläche und rechnet, sofern das Setup wirklich lokal konfiguriert ist, auf deinem eigenen Gerät. Ob es passt, schätzt du mit Parametern mal Bits pro Gewicht geteilt durch 8 plus Reserve für den Kontext ab, und die Geschwindigkeit hängt oft an der Speicherbandbreite. Der Gewinn liegt bei Kontrolle, Unabhängigkeit vom Netz und der Möglichkeit, vertrauliche Texte auf dem Gerät zu halten. Dem stehen kleinere Modelle, eigener Aufwand und eigene Verantwortung für Sicherheit, Lizenz und Regeln gegenüber. Ob ein lokales Modell für deine Aufgabe reicht, zeigt nur dein eigener Test mit anschließender Prüfung nach A8. Als Nächstes geht es im Dahinter-Block in D1 um Tokens und Kontextfenster: warum Modelle vergessen, warum lange Chats driften und warum Kontext Speicher kostet.

```yaml
dokument: ki-a9-lokale-ki-als-einstieg
typ: C
ausfuehrung: ausfuehrlich
reihe: ki-im-wiki
status: final
stand: 2026-10-08
quellen_fachlich:
  - "llama.cpp: Quantize README (Bits pro Gewicht und Dateigrößen am Beispiel eines 8-Milliarden-Modells; F16 16,0005 bpw 14,96 GiB, Q8_0 8,5008 bpw 7,95 GiB, Q4_K_M 4,8944 bpw 4,58 GiB). https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md (Zugriff 2026-10-08): Quantisierung senkt Genauigkeit der Gewichte, verkleinert und kann beschleunigen, kann Genauigkeit kosten; Requantisieren schon quantisierter Modelle kann Qualität stark senken"
  - "NVIDIA Developer Blog: Mastering LLM Techniques: Inference Optimization. https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ (Zugriff 2026-10-08): Decode-Phase erzeugt Token einzeln und ist speichergebunden ('memory-bound'); Geschwindigkeit wird von der Übertragung der Daten aus dem Speicher dominiert; Modellausführung häufig durch Speicherbandbreite der Gewichte begrenzt"
  - "Qwen2.5-7B-Instruct, config.json: 28 Schichten, 28 Attention-Köpfe, 4 Key-Value-Köpfe, hidden_size 3584 (Kopfgröße 3584/28 = 128), max_position_embeddings 32768, bfloat16. https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/raw/main/config.json (Zugriff 2026-10-08)"
  - "Cloud Security Alliance, AI Safety Initiative: Exposed AI Infrastructure: Self-Hosted Services Under Attack (Research Note, 2026-05-07, geändert 2026-05-20). https://labs.cloudsecurityalliance.org/research/csa-research-note-exposed-ai-infrastructure-selfhosted-secur/ (Zugriff 2026-10-08): Zusammenfassung einer Untersuchung von Intruder (ca. eine Million exponierte KI-Endpunkte, aufgefunden über Zertifikatstransparenz-Logs und OSINT); bei Ollama 31 % (1.652 von über 5.200 abgefragten Instanzen) beantworteten Testanfragen ohne Anmeldung; Empfehlung Bindung an localhost bzw. private Schnittstelle"
  - "The Hacker News: We Scanned 1 Million Exposed AI Services (2026-05-05). https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html (Zugriff 2026-10-08): Bericht über die Intruder-Untersuchung; Zählung von über 5.200 Servern, die eine Modellliste preisgaben, davon 31 % ohne Anmeldung; Anbieter hat kommerzielles Interesse an solchen Befunden (Sicherheitsprodukt)"
  - "NVD: CVE-2026-7482. https://nvd.nist.gov/vuln/detail/CVE-2026-7482 (Zugriff 2026-10-08, veröffentlicht 2026-05-04): Ollama vor 0.17.1, Heap-Out-of-bounds-Lesezugriff beim Verarbeiten einer präparierten GGUF-Datei über /api/create, Abfluss über /api/push, diese Endpunkte laut Beschreibung ohne Authentifizierung; CVSS 3.1 9.1 von der meldenden CNA (Echo), NVD-eigene Bewertung zum Zugriffszeitpunkt ausstehend"
  - "Ollama-Dokumentation: FAQ https://docs.ollama.com/faq (Standardbindung 127.0.0.1:11434, Änderung über OLLAMA_HOST, Prozessor-Spalte von 'ollama ps' mit CPU/GPU-Anteilen, Speicherorte), CLI https://docs.ollama.com/cli (pull, run, ls, ps, rm, stop), Cloud https://docs.ollama.com/cloud (Cloud-Modelle mit Suffix ':cloud', laufen in der Cloud des Anbieters, Cloud-Funktionen abschaltbar), README https://github.com/ollama/ollama (Zugriff jeweils 2026-10-08). Modellseite https://ollama.com/library/gemma4 (Zugriff 2026-10-08): Modell vorhanden, Größenangaben je Variante (Standard-Tag etwa 6,6 bis 9,5 GB, kleinere Variante e2b etwa 4,6 bis 7,5 GB), Cloud-Tags vorhanden, Lizenz auf der Seite nicht angegeben"
  - "Hugging Face Hub Docs: Pickle Scanning. https://huggingface.co/docs/hub/security-pickle (Zugriff 2026-10-08): beim Laden von Pickle-Dateien kann beliebiger Code ausgeführt werden; 'do not unpickle data from untrusted sources'; Alternativen u. a. safetensors; Hub-Scan 'nicht 100 % narrensicher'. Hugging Face Text Generation Inference, Safetensors-Sicherheit https://huggingface.co/docs/text-generation-inference/main/en/basic_tutorials/safety (Zugriff 2026-10-08): safetensors als reines Datenformat ('pure data') beschrieben"
  - "Open Source Initiative: The Open Source AI Definition 1.0 (2024-10-28). https://opensource.org/ai/open-source-ai-definition (Zugriff 2026-10-08): vier Freiheiten; verlangt Dateninformationen, vollständigen Code und Parameter unter OSI-konformen Bedingungen"
  - "Eigene Artikel der Reihe: E2 (Werkzeugtypen lokal und Cloud), E6 (Grenzen, Wissensstand), E7 (Daten-Ampel), A5 (geprüfte Ausführung), A7 (Testfälle, Vorlagen), A8 (Prüfung, Zweitmeinung, Protokoll); Vorwärtsverweise auf P1, P2, D1, D6, R1, R3, R4, R6"
  - "Rechnungen in Abschnitt 2 am 2026-10-08 mit Python ausgeführt: 8 Mrd. Parameter bei 16, 8,5 und 4,89 Bit = 16,0, 8,5, 4,9 GB; Gegenprobe mit 8,03 Mrd.: 16,06 GB = 14,96 GiB (16 Bit) und 4,58 GiB (4,8944 Bit), deckungsgleich mit der Dokumentation; Zwischenspeicher 57.344 Byte pro Token, 1,75 GiB bei 32.768 Token; Ideal-Obergrenze Token/s 10 bei 50 GB/s und 82 bei 400 GB/s (Modell 4,9 GB)"
verifikation_offen:
  - "Intruder-Untersuchung selbst nicht geöffnet; die Zahlen (31 %, über 5.200 Instanzen) stammen aus der CSA-Zusammenfassung und dem Bericht der Hacker News, beide abgeglichen. Stichprobe öffentlich auffindbarer Instanzen mit Modellliste, nicht auf alle Installationen übertragbar; Anbieter mit kommerziellem Interesse. Methodik (Zertifikatstransparenz-Logs) nur aus Sekundärquellen"
  - "CVE-2026-7482: NVD-Eintrag gelesen; Schweregrad von der meldenden Stelle, NVD-Bewertung ausstehend (Stand 2026-10-08, vor Final erneut prüfen). Das geringere Risiko bei reiner lokaler Nutzung ist eine Schlussfolgerung aus der Voraussetzung 'Zugriff auf die Schnittstelle', keine Aussage der Quelle"
  - "Ollama-Befehle der Beispielbox aus der Dokumentation abgeglichen, nicht selbst ausgeführt (kein passender Rechner); Größenangaben der Modellseite gemma4 nur als Spanne über Varianten gelesen und im Text bewusst nicht genannt (Standard-Tag 6,6 bis 9,5 GB, e2b 4,6 bis 7,5 GB, Stand 2026-10-08); Modellnamen und Verfügbarkeit ändern sich"
  - "Denkmodell Token/s ≈ Bandbreite ÷ Modellgröße ist eine eigene Herleitung aus der Aussage 'speichergebunden', nicht wörtlich in der NVIDIA-Quelle; im Text als Denkmodell mit angenommenen Beispielwerten gekennzeichnet; gilt nicht für Bauarten, die pro Token nur Teile der Gewichte lesen. Auch bei dichten Modellen ist die Rechnung nur eine idealisierte Obergrenze; tatsächliche Token/s hängen von Programm, Hardware, Rechenoperationen, Kontext und Speicherzugriffen ab"
  - "Formel für den Zwischenspeicher (2 × Schichten × KV-Köpfe × Kopfgröße × Bytes) ist Fachwissen und in den abgerufenen Quellen nicht wörtlich belegt; Eingangswerte aus der config.json des genannten Modells. Gilt für dichte Aufmerksamkeit mit Gruppierung der KV-Köpfe, nicht für alle Bauarten. Im Text als Vereinfachung gekennzeichnet"
  - "Bits pro Gewicht gemessen an einem 8-Milliarden-Modell; für andere Modelle weichen die Werte leicht ab. Im Text als Mittelwerte bezeichnet. Übung 1 rechnet deshalb nur als Größenordnung"
  - "Aussagen zu Stärken und Schwächen kleinerer Modelle, zum Erfinden von Fakten und zur Sprachqualität sind Praxiserwartungen ohne Einzelquelle und im Text als Faustregel gekennzeichnet; keine Studie dazu gelesen"
  - "Safetensors: Die Aussage 'reine Daten' stammt aus der TGI-Dokumentation; der Hub-Dokumentation allein ist sie nicht zu entnehmen. Im Text als Beschreibung dieser Plattform formuliert"
  - "Offene Gewichte gegenüber Open Source: OSI-Definition gelesen, die Einordnung einzelner Modelle bewusst nicht vorgenommen; Lizenzen einzelner Modelle nicht geprüft"
  - "Hinweis auf Cloud-Modelle in lokalen Programmen stützt sich auf die Dokumentation eines Programms; im Text allgemein formuliert, andere Programme nicht geprüft"
  - "Vorwärtsverweise auf P1, P2, D1, D6, R1, R3, R4, R6 beim Anlegen dieser Artikel abgleichen"
review_historie:
  - runde: 0
    datum: 2026-10-08
    ergebnis: "Erster Draft in der Zielstimme (Stilblatt und lockeres-lernmaterial) nach Lektüre der Dokumentation zu Quantisierung, Ollama, Pickle-Risiko, Open-Source-AI-Definition und der Zusammenfassung zu frei erreichbaren KI-Diensten. Rechenbeispiele per Python ausgeführt und mit der Dokumentation gegengeprüft."
  - runde: 1
    datum: 2026-10-08
    ergebnis: "Drei externe Reviews, Aussagen gegen Quellen geprüft (gemma4-Modellseite, NVD-Eintrag, Hacker-News-Bericht, TGI-Sicherheitsdokumentation). Übernommen: Erklärung GB gegen GiB mit Rechnung 16,06 GB = 14,96 GiB; Faustregel 'Hälfte des Speichers' ohne Quelle ersetzt durch Reserve-Formulierung und Hinweis, dass Parameterzahl, Dateigröße und Qualität keine austauschbaren Maße sind; Geschwindigkeitsrechnung als Denkmodell mit Ideal-Obergrenze gekennzeichnet; Sicherheitsabschnitt präzisiert (Standardbindung nur lokal, Stichprobe und kommerzielles Interesse der Untersuchung, CVE mit Voraussetzung und Bewertungsstand); Abschnitt 2 in drei Unterabschnitte gegliedert; Beispielbox mit Größenspanne der Modellseite; 'häufigste Falle' zu 'mögliche Falle'; 'niemand sieht' abgeschwächt; Übungen 1 und 5 konkretisiert; 'man' im Open-Weights-Absatz entfernt. Ebenfalls übernommen: Hinweis auf Metadaten in der Datei, Satz zu Laufzeit und internen Puffern, Quantisierungskürzel Q8_0 und Q4_K_M, Begriff Open Weights, Hinweis dass ein Datenformat eine Quelle nicht vertrauenswürdig macht, entschärfte Aussage zu kleineren Modellen. Nicht übernommen: konkrete Lizenzbeispiele (nicht geprüft), Satz zur Quantisierung des Zwischenspeichers (ohne Quelle), Hinweise zu Stromverbrauch und Lautstärke sowie Glossar (außerhalb des Umfangs eines Einstiegs), generisches Beispiel statt gemma4 (stattdessen auf der Modellseite geprüft)."
  - runde: 2
    datum: 2026-10-08
    ergebnis: "Drei Re-Reviews. Übernommen: Satzfehler in Abschnitt 4 (entstand bei meiner Überarbeitung, korrigiert); Hinweis 8,0 gegen 8,03 Milliarden Parameter; Parameter als gelernte Zahlenwerte, in diesem Artikel Gewichte genannt; GPU-Satz mit Vergleich zur Aufteilung; vereinfachte Annahmen bei der Ideal-Obergrenze benannt; Gültigkeit der Zwischenspeicher-Formel direkt an der Formel; Verweis auf D1 weniger absolut; gemma4-Größen im Text entfernt, nur Hinweis auf die Modellseite; Sicherheitsregel mit klarer Norm (standardmäßig nur lokal, Netzzugriff als abzusichernde Ausnahme); CVE-Satz enger an die Voraussetzung der erreichbaren Schnittstelle gebunden; Herkunft von Modellen präziser (Modellhersteller oder vertrauenswürdige Plattform); Fazit mit Hinweis auf lokales Setup; vorsichtigerer Wortlaut bei Qualität und Auslagerung. Nicht übernommen: Programmname im CVE-Absatz (Stilentscheidung: Produktnamen nur in YAML und Beispielbox); Vorwärtsverweis-Abgleich bleibt bis Final offen."
  - runde: 3
    datum: 2026-10-08
    ergebnis: "Freigabe durch David am 2026-10-08 nach Runde 2. Offene Punkte aus verifikation_offen bleiben bestehen (Ollama-Befehle nicht selbst ausgeführt, Intruder-Untersuchung nicht geöffnet, Vorwärtsverweise auf P1, P2, D1, D6, R1, R3, R4, R6 beim Anlegen dieser Artikel abgleichen)."
  - runde: 4
    datum: 2026-10-08
    ergebnis: "Verweise nach Umnummerierung des Dahinter-Blocks angepasst (D7 wird D6, Modellfamilien und Größen). Inhaltlich unverändert, Status bleibt final."
```