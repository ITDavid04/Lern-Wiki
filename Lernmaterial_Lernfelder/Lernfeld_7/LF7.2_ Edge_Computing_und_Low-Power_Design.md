# LF7.2 – Edge Computing & Low-Power Design

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 90–110 Minuten reines Lesen, +60–80 Minuten für das eigenständige Nachrechnen der Typfragen und Rechenbeispiele (insbesondere Batterielaufzeit-Berechnung) – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026-09-14
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was unterscheidet Edge Computing von Cloud Computing, und wann ist lokale Verarbeitung besonders vorteilhaft? | [→ 1. Edge Computing vs. Cloud Computing](#1-edge-computing-vs-cloud-computing) |
| 2 | Was passiert bei Deep Sleep eines Microcontrollers, und was unterscheidet zeitgesteuertes von ereignisgesteuertem Aufwachen? | [→ 2. Energiemanagement & Deep Sleep](#2-energiemanagement--deep-sleep) |
| 3 | Wie berechnet man die Batterielaufzeit eines Sensors mit Deep-Sleep-Zyklen? | [→ 2.4 Batterielaufzeit berechnen](#24-batterielaufzeit-berechnen) |
| 4 | Was unterscheidet Payload von Protokoll-Overhead, und warum ist eine kompakte Binärkodierung für Low-Power-IoT oft effizienter als JSON? | [→ 3. Payload-Optimierung](#3-payload-optimierung--time-on-air) |
| 5 | Wie hängen Edge Computing, Deep Sleep und Payload-Optimierung im Gesamtkonzept eines autarken Sensorknotens zusammen? | [→ 4. Zusammenspiel](#4-zusammenspiel-der-konzepte-in-lf72) |

---

## 1. Edge Computing vs. Cloud Computing

> **Grundprinzip:** Eine Gärtnerin, die tagsüber allein auf dem Feld arbeitet, kann bei einem plötzlichen Frostalarm nicht erst per Telefon die Zentrale anrufen und auf Anweisung warten – sie muss vor Ort selbst und sofort entscheiden, die Pflanzen abzudecken. Der Zentrale meldet sie später nur zusammengefasst, was passiert ist. Genau das ist die Grundidee von Edge Computing.

### 1.1 Wo werden die Daten verarbeitet?

| Aspekt | Cloud Computing | Edge Computing |
| --- | --- | --- |
| **Verarbeitungsort** | Zentraler Server/Rechenzentrum, oft weit entfernt | Direkt an der "Kante" des Netzwerks – auf dem Sensor selbst oder einem lokalen Gateway (z. B. Raspberry Pi) |
| **Latenz** | Zusätzliche Zeit für den Weg über das Internet zum Server und zurück | Reaktion in Millisekundenbereich möglich, da der Internetweg entfällt |
| **Bandbreitennutzung** | Oft werden viele/alle Rohmesswerte übertragen | Meist werden nur aggregierte Werte oder Alarme übertragen (z. B. "Temperatur zu hoch" statt 1.000 Einzelmesswerte pro Sekunde) |
| **Verhalten bei Internetausfall** | Cloud-abhängige Funktionen sind bei unterbrochener Verbindung nicht verfügbar; ohne lokale Fallback-Logik steht das System dann typischerweise still | Lokale Kernfunktionen bleiben auch ohne Internetverbindung erhalten |
| **Skalierungskosten** | Ein zentraler, leistungsstarker Server kann oft günstiger sein als viele verteilte Geräte | Viele leistungsstarke Edge-Gateways können in Anschaffung und Wartung teurer werden als ein zentraler Server |
| **Wartungs-/Update-Aufwand** | Ein zentraler Server benötigt in der Regel nur einen Satz an Updates/Firmwareständen | Viele verteilte Edge-Gateways bedeuten potenziell ebenso viele Firmwarestände, Angriffsflächen und Geräte, die überwacht und aktualisiert werden müssen (siehe Deep-Dive-Ausblick zu OTA in LF7.3) |

> **Kostenfalle:** Edge Computing verlagert Rechenleistung nach unten in die Fläche – 50 leistungsstarke Edge-Gateways sind in Anschaffung und Wartung oft teurer als ein zentraler Cloud-Server. Edge Computing ist deshalb kein genereller Kostenvorteil, sondern eine bewusste Abwägung gegen Latenz- und Autarkie-Anforderungen.

> **IHK-Typfrage:** *"Vergleichen Sie die Ausfallsicherheit eines rein cloud-basierten Systems mit der eines Edge-basierten Systems bei einem Ausfall des externen Internetanbieters (ISP)."*
> **Musterantwort:** Bei einem cloud-basierten System sind alle Funktionen, die auf den Cloud-Server angewiesen sind, bei einem ISP-Ausfall unterbrochen – das System kann weder neue Daten auswerten noch Steuerbefehle empfangen. Bei einem Edge-basierten System bleiben die lokal implementierten Kernfunktionen (z. B. Schwellenwert-Überwachung, Not-Abschaltung) auch ohne Internetverbindung funktionsfähig, da die Entscheidung direkt am Gateway getroffen wird. Nicht-zeitkritische Funktionen wie das Hochladen historischer Daten oder eine Fernwartung bleiben davon zwar auch betroffen, aber die sicherheitsrelevante Kernfunktion läuft weiter.

### 1.2 Datenreduktion durch lokale Aggregation

Ein zentraler Nutzen von Edge Computing ist die Reduktion der Datenmenge, bevor sie überhaupt gesendet wird:

```text
[ 100 Rohmesswerte/Minute ] → [ Edge-Gateway: Mittelwertbildung ] → [ 1 Durchschnittswert/Minute gesendet ]
```

Statt 100 Einzelwerte über das Netzwerk zu senden, berechnet das Gateway lokal einen einzigen Durchschnittswert und überträgt nur diesen – das spart sowohl Bandbreite als auch Sendezeit und damit Energie (siehe Abschnitt 3).

### 1.3 Welche Daten gehören auf die Kante, welche in die Cloud?

| Datentyp | Empfohlener Verarbeitungsort | Begründung | IHK-Relevanz |
| --- | --- | --- | --- |
| Sicherheitskritische Schwellenwerte (z. B. Übertemperatur, Not-Aus) | Edge | Reaktion darf nicht von Internetverfügbarkeit oder Cloud-Latenz abhängen | 🔴 |
| Kurzfristige Steuerentscheidungen (z. B. Ventil öffnen/schließen) | Edge | Millisekunden-Reaktion nötig, kein Warten auf Cloud-Antwort vertretbar | 🔴 |
| Historische Rohdaten für Langzeitanalyse/Reporting | Cloud | Nicht zeitkritisch, profitiert von zentraler Speicherung und Auswertung über viele Standorte hinweg | 🟡 |
| Machine-Learning-Training auf großen Datenmengen | Cloud | Benötigt Rechenleistung und Datenmengen, die ein einzelnes Edge-Gateway meist nicht wirtschaftlich vorhält | 🟡 |

> **IHK-Typfrage:** *"Ein Microcontroller soll ohne Internetverbindung einen Aktor auslösen, sobald ein Temperatursensor einen Grenzwert überschreitet. Skizzieren Sie die lokale Wenn-Dann-Logik."*
> **Musterantwort:**
> ```text
> WENN Temperatur > 80°C
>   DANN schalte Relais AN (Kühlung aktivieren)
>   UND sende Alarm-Nachricht, sobald Netzwerk wieder verfügbar ist
> SONST Relais AUS
> ```
> Die Kernentscheidung (Relais schalten) hängt dabei ausschließlich vom lokal gemessenen Wert ab und wartet nicht auf eine Cloud-Antwort – die Netzwerk-Meldung ist von der Aktor-Reaktion bewusst entkoppelt.

> Verwandter Begriff: **Fog Computing** ("Nebelrechnen") bezeichnet eine zusätzliche Verarbeitungsebene zwischen einzelnen Edge-Geräten und der Cloud (z. B. ein regionaler Mini-Server, der mehrere Gateways bündelt) – für die Grundlagenprüfung reicht das Wissen, dass dieser Zwischenbegriff existiert.

---

## 2. Energiemanagement & Deep Sleep

> **Grundprinzip:** Ein Handwerker, der ständig im Werkzeuggürtel nach dem nächsten Auftrag sucht, ermüdet schnell. Legt er sich zwischen den Aufträgen kurz hin und wird nur bei einem Anruf oder zur vereinbarten Uhrzeit geweckt, hält er die gesamte Schicht durch. Microcontroller in Batteriebetrieb funktionieren nach demselben Prinzip.

### 2.1 Das Energie-Problem

Ein ESP32 kann im aktiven WLAN-Betrieb – abhängig von Chipvariante, Funkphase, Sendeleistung und Board – grob **100–240 mA** aufnehmen, mit kurzzeitigen Sendespitzen teils auch darüber. Eine gängige Batterie (z. B. 2.500 mAh) wäre bei durchgehendem Betrieb rechnerisch schon nach rund 10 bis 25 Stunden leer – für einen Sensor, der über Monate wartungsfrei laufen soll, ist Dauerbetrieb also keine Option.

### 2.2 Deep Sleep: Der Tiefschlaf-Modus

Im **Deep Sleep** werden Hauptprozessor (CPU), die digitalen Peripheriegeräte, die Funkmodule (WLAN/Bluetooth) und der überwiegende Teil des regulären Arbeitsspeichers abgeschaltet. Weiterhin mit Strom versorgt bleibt lediglich die sogenannte **RTC-Domäne** (RTC = Real Time Clock) – ein Bereich aus RTC-Controller, bestimmten RTC-Peripheriefunktionen und speziellem RTC-Speicher. Innerhalb dieser Domäne kann bei manchen Architekturen zusätzlich ein kleiner **ULP-Coprozessor** (Ultra Low Power) einfache Aufgaben übernehmen – z. B. einen Sensor zyklisch abfragen –, ohne dass die Haupt-CPU dafür aufwachen muss. Der Stromverbrauch des reinen Chips sinkt dadurch auf ungefähr **10 µA (Mikroampere)** – ein Bruchteil des Normalbetriebs, wobei der genaue Wert je nach Chipvariante, genutzter Wake-up-Quelle und Konfiguration der RTC-Domäne schwankt.

> **Praxis-Hinweis:** Diese ca. 10 µA gelten für den Chip unter Datenblattbedingungen bei einer für Deep Sleep typischen, minimalen RTC-Konfiguration. Auf gewöhnlichen Entwicklungsboards ("DevKits") liegt der tatsächlich gemessene Verbrauch im Deep Sleep oft deutlich höher – von einigen zehn/hundert Mikroampere bis zu mehreren Milliampere –, weil zusätzliche Bauteile wie Spannungsregler, USB-Seriell-Wandler oder eine Power-LED weiterlaufen und selbst nichts vom Deep Sleep "wissen". Für ein echtes Batterieprojekt sind daher speziell auf Energieeffizienz ausgelegte Boards oder eine eigene, reduzierte Schaltung nötig, um in die Nähe der Datenblattwerte zu kommen.

Neben Active Mode und Deep Sleep existieren bei vielen Microcontrollern noch Zwischenstufen (z. B. Modem Sleep, bei dem nur die Funkmodule ruhen, während die CPU weiterläuft) – für die Grundlagenprüfung reicht der Kontrast zwischen "voll aktiv" und "Deep Sleep" als die beiden wichtigsten Eckpunkte.

### 2.3 Wake-Up-Trigger: Timer vs. externer Interrupt

| Trigger | Funktionsweise | Typischer Anwendungsfall | IHK-Relevanz |
| --- | --- | --- | --- |
| **Timer (zeitgesteuert)** | Der RTC-Timer (Teil der RTC-Domäne) weckt das System nach einer festgelegten Zeitspanne (z. B. alle 15 Minuten) | Regelmäßige Messungen ohne akuten Ereignisbezug (z. B. stündliche Temperaturmeldung) | 🔴 |
| **Externe Wake-up-Quelle ("Interrupt")** | Ein physischer Reiz (Tastendruck, Bewegungssensor, Reed-Kontakt an einer Tür) weckt das System – die RTC-Domäne überwacht dafür meist den Pegel eines konfigurierten GPIO-Pins, statt einen klassischen CPU-Interrupt im engeren Sinn auszulösen | Sicherheits- oder ereignisrelevante Reaktionen, bei denen Sofortigkeit zählt (z. B. Türöffnung) | 🔴 |

> **Begriffshinweis:** In vereinfachten Darstellungen (auch in diesem Artikel) wird das ereignisgesteuerte Aufwecken häufig verkürzt als "Interrupt" bezeichnet. In der Herstellerdokumentation ist die genauere Bezeichnung meist "External Wakeup" bzw. GPIO-/RTC-GPIO-Wakeup, da im Deep Sleep die RTC-Logik einen Pegel überwacht statt eines klassischen, laufenden CPU-Interrupt-Mechanismus.

> **IHK-Typfrage:** *"Erklären Sie den wesentlichen Unterschied für den Anwendungsfall, ob ein Sensor per Timer alle 10 Minuten oder per Hardware-Interrupt beim Öffnen eines Fensters geweckt wird."*
> **Musterantwort:** Ein per Timer geweckter Sensor prüft den Zustand nur zu festgelegten Zeitpunkten – eine Fensteröffnung wird deshalb nur erkannt, wenn das Fenster beim nächsten Messzeitpunkt noch geöffnet ist, und zwar verzögert um bis zu fast eine volle Zykluslänge. Wird das Fenster zwischen zwei Messzeitpunkten kurz geöffnet und vor der nächsten Messung bereits wieder geschlossen, bleibt das Ereignis sogar vollständig unbemerkt. Ein per Hardware-Interrupt (externe Wake-up-Quelle) geweckter Sensor reagiert dagegen unmittelbar beim tatsächlichen Auftreten des Ereignisses – unverzichtbar bei sicherheitsrelevanten oder seltenen, aber wichtigen Ereignissen wie einem Fenster- oder Türkontakt.

### 2.4 Batterielaufzeit berechnen

> **Rechenbeispiel:** Ein Sensor mit einer 1.000-mAh-Batterie verbraucht entweder durchgehend 100 mA, oder er verweilt zu 99 % der Zeit im Deep Sleep (0,01 mA) und ist nur die restlichen 1 % der Zeit mit 100 mA aktiv (Messen + Senden). Wie unterscheidet sich die Batterielaufzeit?
>
> **Fall 1 – Dauerbetrieb:** Batterielaufzeit = 1.000 mAh ÷ 100 mA = **10 Stunden**.
>
> **Fall 2 – 99 % Deep Sleep, 1 % aktiv:** Der durchschnittliche Stromverbrauch ergibt sich aus der zeitgewichteten Summe beider Phasen:
> $$\text{Ø-Verbrauch} = (0{,}99 \times 0{,}01\text{ mA}) + (0{,}01 \times 100\text{ mA}) = 0{,}0099\text{ mA} + 1{,}0\text{ mA} \approx 1{,}01\text{ mA}$$
> Batterielaufzeit = 1.000 mAh ÷ 1,01 mA ≈ **990 Stunden ≈ 41 Tage**.
>
> Allein durch das Schlafverhalten steigt die Batterielaufzeit hier rechnerisch um das rund 99-Fache – auch wenn die tatsächliche Laufzeit in der Praxis wegen Selbstentladung, Temperatureinflüssen, Spannungseinbrüchen bei Sendestromspitzen und den in 2.2 genannten Board-Zusatzverbräuchen niedriger ausfallen kann als der theoretische Idealwert. Für die Prüfungsrechnung wird zudem idealisierend angenommen, dass die angegebene Nennkapazität vollständig nutzbar ist.

**Allgemeines Rechenschema für beliebige Aufgaben dieser Art:**

$$I_{\text{Ø}} = \sum_i \left( I_i \times \text{Anteil}_i \right) \qquad t_{\text{Laufzeit}} = \frac{\text{Kapazität}}{I_{\text{Ø}}}$$

Der Durchschnittsstrom ergibt sich aus der Summe aller Betriebsphasen, gewichtet mit ihrem jeweiligen Zeitanteil; die Batterielaufzeit folgt daraus wie bei einer einzelnen Betriebsphase. Dieses Schema lässt sich auf jede Kombination aus Betriebsphasen anwenden, auch wenn die Aufgabe – wie in der Prüfung üblich – konkrete Zeitspannen statt Prozentanteile vorgibt (z. B. "5 Sekunden aktiv, dann 15 Minuten Deep Sleep"): Dazu zunächst beide Zeitspannen auf dieselbe Einheit bringen und daraus die jeweiligen Zeitanteile berechnen, bevor die Formel angewendet wird.

### 2.5 RAM-Verlust und RTC-Memory

Im Deep Sleep gehen die normalen Variablen im regulären Arbeitsspeicher (RAM) verloren, da dieser Bereich stromlos geschaltet wird – nach dem Aufwachen startet der Chip im Wesentlichen wie bei einem Neustart neu. Daten, die über den Schlaf hinaus erhalten bleiben sollen (z. B. ein Zähler für "Anzahl der Türöffnungen"), müssen deshalb in einem speziellen, weiterhin mit Strom versorgten **RTC-Memory-Bereich** abgelegt werden statt in normalen Programmvariablen. Dieser Bereich ist allerdings sehr klein (typischerweise wenige KB) und daher nur für einzelne Zähler oder kleine Statuswerte gedacht, nicht für größere Datenmengen.

> **Wichtige Abgrenzung:** RTC-Memory übersteht den Deep Sleep, aber nicht zwingend einen vollständigen Verlust der Versorgungsspannung (z. B. Batteriewechsel oder längerer Stromausfall). Daten, die auch das überstehen müssen, gehören in **nichtflüchtigen Speicher** (z. B. Flash/NVS) – dabei ist zu beachten, dass häufige Schreibvorgänge auf Flash-Speicher zusätzliche Energie kosten und den Speicher auf Dauer verschleißen können.

### 2.6 On-Time minimieren

Beim Aufwachen aus dem Deep Sleep geht der vorherige Ausführungszustand der CPU verloren, und der Chip durchläuft im Wesentlichen erneut seinen normalen Startpfad (Boot, Initialisierung) – besonders das Herstellen einer WLAN-Verbindung kann dabei mehrere Sekunden dauern und verbraucht unverhältnismäßig viel Energie im Vergleich zur eigentlichen Mess- und Sendezeit. Diese Phase voller Aktivität wird als **On-Time** bezeichnet und sollte so kurz wie möglich gehalten werden (z. B. durch minimalen Code im Weckzyklus, siehe Flussdiagramm unten).

> **Begriffsabgrenzung – On-Time ≠ Time-on-Air:** Die **On-Time** umfasst die gesamte aktive Phase des Geräts nach dem Aufwachen (Booten, Messen, ggf. Netzwerkaufbau, Senden). Die **Time-on-Air** (Abschnitt 3.3) bezeichnet dagegen nur die Zeitspanne, während der tatsächlich Funkdaten übertragen werden – sie ist also nur ein Teilabschnitt der On-Time.

> **IHK-Typfrage:** *"Warum eignet sich LoRaWAN für viele Deep-Sleep-Szenarien oft besser als eine klassische WLAN-Anbindung?"*
> **Musterantwort:** WLAN erfordert bei jedem Aufwachen in der Regel einen erneuten Verbindungsaufbau zu einem Access Point (Authentifizierung, IP-Vergabe usw.), was mehrere Sekunden On-Time und damit Energie kostet. Ein bereits aktiviertes (dem Netzwerk beigetretenes) LoRaWAN-Endgerät der Klasse A kann dagegen nach dem Aufwachen direkt einen Uplink senden, ohne eine dauerhafte Funkverbindung halten zu müssen, und öffnet anschließend bis zu zwei kurze Empfangsfenster für einen möglichen Downlink – das reduziert die On-Time und damit den Energieverbrauch pro Zyklus erheblich, auch wenn dafür weniger Daten pro Übertragung möglich sind (siehe LF7.1, Abschnitt 3.3). Der einmalige Netzwerkbeitritt (Join) selbst benötigt allerdings ebenfalls Zeit und Energie – bei Geräten, die nach jedem Deep Sleep ihre Sitzungsdaten verlieren und sich jedes Mal neu anmelden müssten, ginge dieser Vorteil verloren.

**Beispielhafter Sensor-Zyklus:**

```text
[ Deep Sleep ]
      │  Timer- oder Interrupt-Weckung
      ▼
[ Aufwachen / Boot ]
      │
      ▼
[ Messen ]
      │
      ▼
[ Senden (möglichst kurze On-Time, komprimierter Payload) ]
      │
      ▼
[ Zurück in Deep Sleep ]
```

---

## 3. Payload-Optimierung & Time-on-Air

> **Grundprinzip:** Eine konzentrierte Suppenwürze in einem kleinen Glas transportiert dieselbe geschmackliche Information wie ein großer Topf fertiger Brühe – nur mit einem Bruchteil des Volumens und Transportaufwands. Payload-Optimierung funktioniert nach demselben Prinzip: dieselbe Information in möglichst wenigen Bytes.

### 3.1 Payload vs. Overhead

| Begriff | Bedeutung | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Payload** | Die eigentliche Nutzinformation, die übertragen werden soll | Der reine Messwert, z. B. `22.5` für eine Temperatur | 🔴 |
| **Overhead** | Zusätzliche Metadaten des verwendeten Protokolls, die für Adressierung/Routing/Struktur nötig sind, aber keine Nutzinformation enthalten | TCP-Header, MQTT-Topic-Pfad, Routing-Informationen | 🔴 |

### 3.2 JSON vs. kompakte Binärkodierung

**JSON** ist für Menschen sehr gut lesbar, kostet aber durch Klammern, Anführungszeichen und Schlüsselnamen viele zusätzliche Bytes:

```text
{"sensor": "Temp1", "wert": 22.5}
```
Dieser Ausdruck belegt bereits über 30 Bytes reinen Text – für ein LPWAN-Gerät mit stark begrenzter Bandbreite (siehe LF7.1, Abschnitt 3.3) ein erheblicher Anteil der ohnehin knappen Übertragungskapazität.

Eine **kompakte Binärkodierung** überträgt denselben Informationsgehalt mit deutlich weniger Bytes, indem Werte direkt als Bytes statt als Text übertragen werden: eine feste 1-Byte-Sensor-ID (`0x01` für "Temp1") gefolgt von einem 2-Byte-Festkomma-Wert für die Temperatur (z. B. die Ganzzahl 225, die durch 10 geteilt `22,5` ergibt) – macht insgesamt **3 Bytes** statt über 30.

> **Wichtige Unterscheidung – Binärbytes vs. Hex-String:** Die Schreibweise `01 00 E1` ist lediglich die für Menschen lesbare **hexadezimale Darstellung** dieser 3 Binärbytes – sie wird z. B. beim Debuggen benutzt, ändert aber nichts an der tatsächlich übertragenen Bytezahl. Würde man stattdessen den Wert als **Text** übertragen, etwa als Zeichenkette `"0100E1"`, wären das bereits **6 ASCII-Zeichen/Bytes** – ein Hex-*String* als Text ist also nicht automatisch so kompakt wie die zugrunde liegenden 3 Binärbytes, da jedes Byte dabei durch zwei Textzeichen dargestellt wird. Für die Übertragung zählt deshalb die tatsächliche Binärkodierung, nicht die hexadezimale Schreibweise als solche.

Der Empfänger benötigt für die Binärkodierung allerdings einen passenden **Decoder**, der weiß, wie die Bytes zu interpretieren sind, da die Struktur nicht mehr selbsterklärend im Datenpaket steht.

> **Pflichtaufgabe – Beispiel-Umwandlung:** Ein Temperatur- und Feuchtigkeits-Datensatz liegt als JSON vor: `{"temp": 22.5, "hum": 61}`. Kodiert man Temperatur als 2-Byte-Festkommawert (225 → 22,5 °C) und Feuchtigkeit als 1-Byte-Ganzzahl (61 %), ergibt sich eine 3-Byte-Binärkodierung statt der ca. 25 Bytes des JSON-Textes – eine Reduktion um mehr als 85 %, ohne Informationsverlust bei den relevanten Nachkommastellen.
>
> **Voraussetzung:** Diese Kompaktheit funktioniert nur, wenn Sender und Empfänger vorab ein festes Datenschema vereinbart haben – welches Byte welchen Wert darstellt, welche Skalierung gilt und in welcher Byte-Reihenfolge Mehrbyte-Werte kodiert sind. Ohne dieses gemeinsame Schema wären die 3 Bytes für den Empfänger bedeutungslos.

### 3.3 Time-on-Air: Weniger Bytes, kürzere Sendezeit

Je mehr Bytes gesendet werden, desto länger muss das Funkmodul aktiv senden (**Time-on-Air**) – und eine längere Sendezeit bedeutet einen höheren Stromverbrauch pro Übertragung. Eine Reduktion des Payloads von z. B. 100 auf 10 Bytes verkürzt die Sendezeit spürbar, allerdings nicht zwingend exakt proportional: Ein Teil der Übertragung entfällt auf einen technisch bedingten Fixanteil (z. B. Präambel, Header), der auch bei sehr kleinem Payload nicht vollständig wegfällt. Zusätzlich hängt die Time-on-Air je nach Funktechnik von weiteren Übertragungsparametern ab (bei LoRa z. B. Spreizfaktor, Bandbreite und Codierungsrate) – die Payload-Größe ist also nur einer von mehreren Einflussfaktoren.

> **IHK-Typfrage:** *"Welche Konsequenzen ergeben sich für das Backend (Cloud/Server), wenn Sensoren keine strukturierten JSON-Daten, sondern kompakt binärkodierte Nachrichten senden?"*
> **Musterantwort:** Das Backend benötigt einen passenden **Decoder**, der die feste Byte-Struktur (welche Bytes stehen für welchen Wert) kennt und interpretiert – ohne diesen sind die empfangenen Rohdaten für Menschen und generische Auswertungswerkzeuge nicht direkt lesbar. Das erschwert insbesondere das Debugging, da ein Entwickler die Rohdaten nicht mehr "auf einen Blick" versteht, sondern erst durch den Decoder schicken muss (zur Fehlersuche wird die Binärnachricht dafür oft zusätzlich hexadezimal dargestellt, siehe 3.2). Zusätzlich muss die Byte-Struktur zwischen Sensor-Firmware und Backend-Decoder konsistent gehalten werden – ändert sich das Format auf einer Seite ohne die andere, entstehen Fehlinterpretationen.

### 3.4 Feingranulare Topics als versteckter Overhead-Treiber

Bei MQTT ist der Topic-Name Bestandteil jeder einzelnen PUBLISH-Nachricht. Werden Temperatur und Feuchte deshalb als zwei getrennte Nachrichten mit jeweils eigenem, langem Topic-Pfad gesendet (z. B. `fabrik/halle1/maschine3/sensor/temperatur` und separat `.../sensor/feuchte`), wird der Topic-String und der übrige MQTT-Header dabei jedes Mal erneut mitgesendet. Eine effizientere Alternative bündelt mehrere Werte in einer einzigen Nachricht auf einem gemeinsamen, kürzeren Topic (z. B. `fabrik/h1/m3` mit einem kompakten Binär-Payload, der Temperatur und Feuchte gemeinsam enthält) – das reduziert sowohl die Anzahl der Nachrichten als auch den wiederholt übertragenen Topic- und Header-Overhead. Der Overhead entsteht also nicht durch den Topic-*Baum* als Struktur an sich, sondern dadurch, dass mehr einzelne Nachrichten mit jeweils eigenem Topic-Namen verschickt werden.

> **Abwägung:** Kürzere Pakete sind bei schwachen Funkverbindungen tendenziell weniger anfällig für Paketverluste, da sie kürzer "in der Luft" sind – das ist aber keine Garantie gegen Paketverlust, sondern nur ein statistisch günstigerer Faktor neben Signalqualität, Störungen und Distanz.

---

## 4. Zusammenspiel der Konzepte in LF7.2

```text
[ Deep Sleep ] ──Timer/Interrupt──> [ Aufwachen ] ──> [ Messen ]
                                                            │
                                          (Edge-Logik: lokale Schwellenwertprüfung,
                                           ggf. sofortige Aktor-Reaktion ohne Internet)
                                                            │
                                                            ▼
                                          [ Payload komprimieren (kompakte Binärkodierung statt JSON) ]
                                                            │
                                                            ▼
                                          [ Senden – kurze Time-on-Air, kurze On-Time ]
                                                            │
                                                            ▼
                                                     [ Zurück in Deep Sleep ]
```

Ein autarker, energieeffizienter Sensorknoten kombiniert alle drei Bausteine dieses Artikels: Edge-Logik entscheidet, was überhaupt lokal behandelt und was gesendet werden muss (Abschnitt 1); Deep Sleep sorgt dafür, dass der Knoten die meiste Zeit nur einen sehr geringen Strom verbraucht (Abschnitt 2); ein kompaktes Payload-Format hält die verbleibende aktive Sendezeit so kurz wie möglich (Abschnitt 3). Alle drei Stellschrauben wirken auf dieselbe Zielgröße: die Batterielaufzeit.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Edge Computing ist immer die günstigere Lösung gegenüber Cloud Computing | Viele leistungsstarke Edge-Gateways können in Anschaffung und Wartung teurer sein als ein zentraler Cloud-Server – die Wahl ist eine Abwägung, kein genereller Kostenvorteil |
| 2 | Ein Edge-basiertes System läuft bei einem ISP-Ausfall komplett unbeeinträchtigt weiter | Nur die lokal implementierten Kernfunktionen bleiben erhalten; cloud-abhängige Funktionen (z. B. Fernwartung, Datenexport) sind auch beim Edge-System betroffen |
| 3 | Deep Sleep bedeutet, dass ein Gerät komplett ohne Strom auskommt | Die RTC-Domäne (RTC-Timer/-Peripherie/-Speicher, ggf. mit ULP-Coprozessor) bleibt aktiv, um das System per Timer oder externe Wake-up-Quelle wieder aufzuwecken – der Chip-Verbrauch sinkt auf wenige µA, ist aber nicht null |
| 4 | Die im Datenblatt genannten Deep-Sleep-Werte (µA) gelten unverändert für jedes fertige Entwicklungsboard | Auf DevKits treiben zusätzliche Bauteile (Spannungsregler, USB-Wandler, LEDs) den realen Verbrauch oft deutlich über die reinen Chip-Datenblattwerte |
| 5 | Variablen im normalen RAM überstehen den Deep Sleep problemlos | Normales RAM wird stromlos geschaltet – Daten, die den Schlaf überdauern sollen, müssen im speziellen RTC-Memory abgelegt werden (und selbst das übersteht keinen vollständigen Spannungsverlust – dafür ist nichtflüchtiger Speicher nötig) |
| 6 | JSON ist für IoT-Datenübertragung grundsätzlich ungeeignet | JSON bleibt für viele Anwendungen (z. B. mit ausreichend Bandbreite/Energie) praktikabel und gut lesbar – für extrem energiebeschränkte LPWAN-Szenarien ist eine kompakte Binärkodierung aber deutlich effizienter |
| 7 | Eine hexadezimale Darstellung ist automatisch genauso kompakt wie die zugrunde liegenden Binärdaten | Hex ist nur eine lesbare Darstellungsform. Wird der Wert als Text-Hex-String übertragen, braucht das typischerweise zwei ASCII-Zeichen pro Binärbyte – also doppelt so viele Bytes wie die reine Binärkodierung |
| 8 | Eine Halbierung des Payloads halbiert automatisch exakt die Time-on-Air | Ein Teil der Sendezeit entfällt auf einen technisch bedingten Fixanteil (Präambel, Header), der auch bei kleinerem Payload nicht vollständig verschwindet |
| 9 | Ein Timer-Wecker erkennt jedes Ereignis lediglich etwas später | Ein kurzes Ereignis, das zwischen zwei Timer-Weckzeitpunkten beginnt und endet (z. B. kurzes Öffnen und Schließen eines Fensters), kann vom Timer vollständig unbemerkt bleiben – nicht nur verzögert erkannt werden |

---

## 6. Deep-Dive-Ausblick (freiwillig)

- **Fog Computing** (→ Abschnitt 1.3): Die zusätzliche Verarbeitungsebene zwischen einzelnen Edge-Geräten und der zentralen Cloud, oft als regionaler Bündelungspunkt für mehrere Gateways.
- **Sicherheitsrisiken dezentraler Datenhaltung** (→ Abschnitt 1): Warum viele verteilte Edge-Gateways ein größeres, verteiltes Angriffsflächenrisiko darstellen können als ein zentral geschütztes Rechenzentrum – und wie das gegen die Autarkie-Vorteile abzuwägen ist.
- **Edge Computing und DSGVO** (→ Abschnitt 1): Inwiefern lokale Vorverarbeitung (z. B. Anonymisierung/Aggregation direkt am Gateway, bevor Daten die EU verlassen oder in die Cloud gelangen) datenschutzrechtliche Vorteile bieten kann.
- **Firmware-Updates für dezentrale Gateways** (→ Abschnitt 1): Strategien für Over-the-Air-Updates (OTA) an vielen verteilten Edge-Geräten ohne physischen Zugriff – wird in LF7.3 vertieft.
- **On-Device-Datenkompression** (→ Abschnitt 3.4): Kompressionsverfahren, die bereits auf dem Microcontroller selbst laufen, bevor überhaupt gesendet wird.
- **ULP-Coprozessor im Detail** (→ Abschnitt 2.2): Wie der Ultra-Low-Power-Coprozessor eigenständig einfache Messungen/Schwellenwertprüfungen durchführen kann, ohne den Hauptprozessor überhaupt aufzuwecken.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Warum ist Edge Computing nicht automatisch die kostengünstigere Wahl? | Viele leistungsstarke Edge-Gateways können in Anschaffung/Wartung teurer sein als ein zentraler Cloud-Server |
| 2 | Was passiert konkret mit CPU, RAM und Funkmodulen während des Deep Sleep? | CPU und Funkmodule werden abgeschaltet, ebenso der größte Teil des normalen RAM; nur die für das Aufwecken benötigten Teile der RTC-Domäne (ggf. mit ULP-Coprozessor) bleiben aktiv |
| 3 | Warum reicht ein Timer-Wecker nicht für sicherheitsrelevante Ereignisse wie eine Türöffnung? | Ein Timer erkennt das Ereignis erst mit Verzögerung bis zum nächsten Weckzeitpunkt (oder verpasst es ganz); eine externe Wake-up-Quelle ermöglicht eine Reaktion mit sehr geringer Verzögerung |
| 4 | Ein Sensor mit 2.000 mAh-Batterie verbraucht durchgehend 50 mA. Wie lange hält die Batterie? | 2.000 mAh ÷ 50 mA = 40 Stunden |
| 5 | Wo können Daten abgelegt werden, die einen Deep Sleep überdauern sollen? | Im speziellen RTC-Memory (nicht im normalen, stromlos geschalteten RAM) – für einen vollständigen Spannungsverlust reicht aber auch RTC-Memory nicht, dafür ist nichtflüchtiger Speicher (z. B. Flash/NVS) nötig |
| 6 | Was ist der Unterschied zwischen Payload und Overhead? | Payload ist die eigentliche Nutzinformation, Overhead sind zusätzliche Protokoll-Metadaten (z. B. Header, Topic-Pfad) |
| 7 | Warum kostet es mehr Overhead, Temperatur und Feuchte als zwei getrennte MQTT-Nachrichten statt gebündelt zu senden? | Der Topic-Name ist Bestandteil jeder einzelnen PUBLISH-Nachricht – bei getrennten Nachrichten wird Topic-String und Header doppelt übertragen, statt einmal für eine gebündelte Nachricht |
| 8 | Warum verkürzt eine Payload-Reduktion die Time-on-Air nicht immer exakt proportional? | Ein technisch bedingter Fixanteil der Übertragung (z. B. Präambel/Header) bleibt auch bei kleinerem Payload bestehen |
| 9 | Was unterscheidet On-Time von Time-on-Air? | On-Time ist die gesamte aktive Phase nach dem Aufwachen (Booten, Messen, ggf. Netzwerkaufbau, Senden); Time-on-Air ist nur die Zeitspanne der tatsächlichen Funkübertragung – also ein Teilabschnitt der On-Time |

**Transferfrage (kombiniert, für Fachgespräch/AP2):** *Ein batteriebetriebener Türsensor soll sechs Monate ohne Wartung arbeiten. Bei einer Türöffnung muss innerhalb von 500 ms lokal reagiert werden (z. B. Alarm auslösen). Die Messdaten sollen anschließend an eine Cloud übertragen werden. Welche Maßnahmen aus diesem Artikel würden Sie einsetzen und warum?*

> **Erwartete Eckpunkte einer guten Antwort:** Deep Sleep als Grundzustand für die sechsmonatige Batterielaufzeit; eine externe Wake-up-Quelle (kein Timer) für die 500-ms-Reaktionsanforderung, da ein Timer das kurze Ereignis verzögert oder komplett verpassen könnte; die Alarmroutine sollte direkt nach dem Wake-up und noch vor einer zeitaufwendigen Funkinitialisierung ausgeführt werden; die Alarmauslösung selbst als lokale Edge-Entscheidung, damit sie nicht von einer Cloud-Antwort abhängt. Wichtig: Die externe Wake-up-Quelle allein *garantiert* die 500-ms-Frist noch nicht – nach dem Aufwachen durchläuft der Controller in der Regel erneut den normalen Startpfad (Boot, Initialisierung), sodass die tatsächliche Reaktionszeit zusätzlich anhand der konkreten Boot- und Verarbeitungsdauer geprüft werden muss. Für die anschließende Cloud-Meldung: möglichst kurze On-Time und ein kompakter, binärkodierter Payload, um die verbleibende Batterie zu schonen, sowie eine für den Anwendungsfall passende, energieeffiziente Funktechnik (siehe LF7.1) für die seltene, kleine Übertragung.

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Edge Computing** | Datenverarbeitung direkt an der "Kante" des Netzwerks (Sensor/Gateway) statt in der zentralen Cloud |
| **Fog Computing** 🟢 | Zusätzliche Verarbeitungsebene zwischen Edge-Geräten und Cloud (z. B. regionaler Bündelungspunkt) |
| **Deep Sleep** | Tiefschlaf-Modus, in dem CPU, Funkmodule und der Großteil des RAM abgeschaltet sind und nur die RTC-Domäne aktiv bleibt |
| **RTC-Domäne** | Bereich aus RTC-Controller, RTC-Peripherie und RTC-Speicher, der im Deep Sleep weiterhin versorgt bleibt; kann einen optionalen ULP-Coprozessor für einfache Aufgaben enthalten |
| **RTC-Memory** | Spezieller, weiterhin mit Strom versorgter Speicherbereich, der Daten über den Deep Sleep hinweg erhält |
| **Wake-Up-Trigger** | Timer (zeitgesteuert) oder externe Wake-up-Quelle/"Interrupt" (ereignisgesteuert) als Aufweck-Methode |
| **On-Time** | Zeitspanne, in der ein Gerät nach dem Aufwachen voll aktiv ist – sollte möglichst kurz gehalten werden |
| **Payload** | Die eigentliche Nutzinformation einer Übertragung, ohne Protokoll-Metadaten |
| **Overhead** | Zusätzliche Protokoll-Metadaten (Header, Topic-Pfad, Routing-Infos) ohne eigenen Informationsgehalt für die Anwendung |
| **Time-on-Air** | Zeitspanne, in der das Funkmodul aktiv sendet – wächst tendenziell mit der Payload-Größe, aber nicht exakt proportional (Fixanteil durch Präambel/Header) |
| **Batterielaufzeit-Formel** | $I_{\text{Ø}} = \sum_i (I_i \times \text{Anteil}_i)$, danach $t = \text{Kapazität} \div I_{\text{Ø}}$ – Durchschnittsstrom aus allen Betriebsphasen bilden, dann Kapazität teilen |
| **Decoder** | Backend-seitige Logik, die eine feste Binärstruktur wieder in lesbare Werte zurückübersetzt |
| **Binärkodierung vs. Hex-String** | Binärbytes sind die tatsächlich übertragenen Daten; Hex ist nur deren lesbare Darstellung. Ein als Text übertragener Hex-String braucht ca. doppelt so viele Bytes wie die zugrunde liegenden Binärdaten |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Architekturvergleich | "Vergleichen Sie Edge und Cloud Computing hinsichtlich Latenz und Ausfallsicherheit" | Konkrete Kriterien gegenüberstellen, nicht pauschal "Edge ist besser" |
| Berechnungsaufgabe | "Berechnen Sie die Batterielaufzeit für Szenario X" | Vollständiger Rechenweg mit Einheiten, inkl. zeitgewichtetem Durchschnittsverbrauch bei gemischten Betriebsphasen |
| Format-Umwandlung | "Wandeln Sie diesen JSON-Datensatz in ein kompaktes Format um" | Konkrete Byte-Ersparnis benennen, nicht nur "ist kleiner" behaupten |
| Technologieauswahl | "Welche Daten sollten lokal verarbeitet werden, welche in der Cloud?" | Begründung anhand Zeitkritikalität/Sicherheitsrelevanz, nicht pauschale Zuordnung |

---

## 10. Merksätze für das Fachgespräch

> Edge Computing bringt die Entscheidung dahin, wo das Ereignis passiert – nicht dorthin, wo der größte Server steht.

> Deep Sleep heißt nicht "aus", sondern "fast aus" – nur die für das Aufwecken benötigten Teile der RTC-Domäne bleiben aktiv (ein ULP-Coprozessor ist dabei optional, kein fester Bestandteil).

> Batterielaufzeit entsteht aus zwei Stellschrauben: möglichst niedriger Deep-Sleep-Strom und möglichst kurze, seltene Wachphasen – bei den meisten batteriebetriebenen Sensoren ist die On-Time der Hebel mit dem größten Einsparpotenzial, weil der aktive Verbrauch den Deep-Sleep-Verbrauch oft um mehrere Größenordnungen übersteigt.

> Ein Byte, das nicht gesendet werden muss, kostet weder Sendezeit noch Batterie – Payload-Optimierung ist gesparte Batterielaufzeit.

> Lesbarkeit für Menschen (JSON) und Effizienz für Batterien (kompakte Binärkodierung) stehen in einem Zielkonflikt – die Wahl hängt vom Energiebudget des Geräts ab, nicht von einer generellen "besseren" Lösung. Hex ist dabei nur eine lesbare Darstellung von Bytes, kein eigenes kompaktes Übertragungsformat.

---

```yaml
dokument: LF7.2-wiki-artikel
lernfeld: LF7.2
titel: "Edge Computing & Low-Power Design"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-14
quellen_intern:
  - "LF7.2.1: Edge Computing Architektur.md"
  - "LF7.2.2: Energiemanagement & Deep Sleep.md"
  - "LF7.2.3: Payload-Optimierung & Latenz.md"
quellen_fachlich:
  - titel: "ESP32-Stromverbrauchsangaben (Active Mode vs. Deep Sleep)"
    herausgeber: "diverse Praxisquellen/Community-Dokumentation (u. a. Elektronik-Praxis-Umfeld), gegen mehrere unabhängige Quellen geprüft"
    status: "Rohmaterial-Angaben (100–240 mA aktiv, ca. 10 µA Deep Sleep) bestätigt; zusätzlich Praxis-Hinweis ergänzt, dass reale DevKits durch Zusatzbauteile (Spannungsregler, USB-Wandler, LED) im Deep Sleep oft deutlich höhere Werte als die reinen Chip-Datenblattangaben zeigen – dieser Nuancierungsbedarf wurde durch Web-Recherche identifiziert und ergänzt, um keine überzogene Absolutheit zu erzeugen"
  - titel: "Fog Computing / Edge Computing Grundlagen"
    herausgeber: "allgemeines Fachwissen, keine versionsgebundene Norm"
    status: "keine spezifische Normversion nötig, da Konzeptwissen ohne Versionsbezug"
  - titel: "ESP-IDF Programming Guide – Sleep Modes / Deep Sleep (ESP32)"
    herausgeber: "Espressif Systems"
    status: "web-verifiziert in Runde 2: bestätigt RTC als Power-Domain (Controller/Peripherie/Speicher) mit ULP-Coprozessor als Teil davon, nicht als eigenständiger 'RTC-Coprozessor'; bestätigt 'most of the RAM' statt vollständigem RAM-Abschaltung"
  - titel: "LoRaWAN L2 1.0.4 Specification (TS001-1.0.4), Class-A-Geräteverhalten"
    herausgeber: "LoRa Alliance"
    status: "web-verifiziert in Runde 2: Class-A-Geräte öffnen nach einem Uplink bis zu zwei Empfangsfenster; setzt vorherigen Netzwerkbeitritt (Join) voraus"
review_historie:
  - runde: 1
    datum: 2026-09-13
    ergebnis: "Erstdraft erstellt aus den drei LF7.2.x-Rohdateien. Web-Verifikation durchgeführt für ESP32-Stromverbrauchsangaben (Active/Deep-Sleep), dabei Rohmaterial-Zahlen bestätigt und um einen wichtigen Praxis-Hinweis ergänzt (DevKit-Realwerte oft höher als Chip-Datenblatt), um nicht denselben Absolutheits-Fehler wie in frühen LF7.1-Fassungen zu wiederholen. Alle 15 Pflichtaufgaben der drei Rohdateien (je 5 pro Unterthema) beim Schreiben direkt abgedeckt: Edge-vs-Cloud-Vergleich, ISP-Ausfall-Vergleich, Aggregations-Beispiel, Datentyp-Zuordnung, lokale Wenn-Dann-Logik, Deep-Sleep-Komponenten, Timer-vs-Interrupt, Batterielaufzeit-Rechnung, Sensor-Flussdiagramm, On-Time-Optimierung, Payload-vs-Overhead, JSON-vs-Binär-Vergleich, Time-on-Air-Skizze, Backend-Konsequenzen bei Hex-Strings. Aus den freiwilligen Zusatzaufgaben in den Deep-Dive-Ausblick übernommen: dezentrale Sicherheitsrisiken, DSGVO-Vorteil durch Edge, Firmware-Update-Strategie für Gateways (Rückverweis auf LF7.3), On-Device-Kompression, Packet-Loss-Risiko bei Payload-Größe (im Haupttext unter 3.4 bereits mit Abwägung versehen, nicht nur Deep-Dive), Fog Computing, ULP-Coprozessor. Vorsichtige, gehedgte Formulierungen von Anfang an verwendet (keine 'immer'/'garantiert'/'zwingend'-Absolutheiten), basierend auf den Lektionen aus der LF7.1-Review-Historie. Noch OFFEN: eigene Review gegen Style-Guide-Checkliste, externe Prüfungsrunde, finale Freigabe durch Auftraggeber."
  - runde: 2
    datum: 2026-09-13
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet, gewichtet nach fachlicher Substanz/Quellenbezug. WICHTIGSTER FUND (Review 1 und Review 2 unabhängig voneinander, Review 2 mit Espressif-Quellenbezug): Durchgängige Vermischung von 'binär' und 'hexadezimal' als vermeintlich austauschbare, gleich kompakte Formate – fachlich falsch, da ein als Text übertragener Hex-String ca. doppelt so viele Bytes benötigt wie die zugrunde liegenden Binärdaten (Hex ist nur eine lesbare Darstellung, kein eigenes kompaktes Übertragungsformat). Abschnitt 3.2 grundlegend überarbeitet (neue Überschrift 'JSON vs. kompakte Binärkodierung', expliziter Absatz zur Unterscheidung Binärbytes/Hex-Darstellung/Hex-String-als-Text mit Byte-Rechnung), alle weiteren Fundstellen (Kernfrage 4, Typfrage zu Backend-Konsequenzen, Zusammenspiel-Diagramm, Prüfungsfalle 6, neue Prüfungsfalle 8, Cheatsheet-Eintrag 'Decoder' + neuer Eintrag 'Binärkodierung vs. Hex-String', Merksatz) konsistent nachgezogen. ZWEITER WICHTIGER FUND (Review 2 und Review 3 unabhängig, Review 2 mit Espressif-ESP-IDF-Dokumentationszitat 'CPUs, most of the RAM, and all the digital peripherals ... are powered off. The only parts ... RTC controller, RTC peripherals (including ULP coprocessor), and RTC memories'): RTC fälschlich selbst als 'Coprozessor' bezeichnet und mit dem ULP-Coprozessor gleichgesetzt – korrigiert auf 'RTC-Domäne' (Controller/Peripherie/Speicher) mit optionalem ULP-Coprozessor als Teil davon; konsistent nachgezogen in 2.2, 2.3-Tabelle, Prüfungsfalle 3, Selbsttest Q2, Cheatsheet (inkl. neuem Eintrag 'RTC-Domäne'). Weitere Korrekturen aus Review 2 (hoch gewichtet, mit Quellenbezug zu Espressif/LoRa Alliance): 'External Interrupt' um Begriffshinweis ergänzt (Herstellerdokumentation spricht von External Wakeup/GPIO-Pegelüberwachung statt klassischem CPU-Interrupt); LoRaWAN-Class-A-Typfrage um Join-Voraussetzung und die tatsächlich bis zu zwei Empfangsfenster korrigiert (vorher: 'ein schmales Empfangsfenster'); Fensteröffnungs-Beispiel präzisiert (ein kurzes Öffnen+Schließen zwischen zwei Timer-Messungen kann komplett unbemerkt bleiben, nicht nur verzögert erkannt werden) – dazu neue Prüfungsfalle 9; RTC-Memory um Größenhinweis (wenige KB) und Abgrenzung zu nichtflüchtigem Speicher (übersteht Deep Sleep, aber keinen vollständigen Spannungsverlust) ergänzt; ESP32-Aktivstrom- und Deep-Sleep-Werte als modell-/konfigurationsabhängig gekennzeichnet, DevKit-Praxis-Hinweis-Bereich präzisiert (Bereich 'einige zehn/hundert µA bis mehrere mA' statt pauschal 'niedriger bis mittlerer mA-Bereich'). Aus Review 1 (hoch gewichtet) übernommen: On-Time-Merksatz von 'entscheidet mehr als die Schlafdauer' auf 'einer der Hebel mit dem größten Einsparpotenzial, weil ... oft um Größenordnungen übersteigt' entschärft; allgemeine Batterielaufzeit-Formel (I_Ø = Σ(I_i×Anteil_i), t = Kapazität/I_Ø) nach dem Rechenbeispiel und im Cheatsheet ergänzt, damit Lernende ein übertragbares Schema statt nur das Einzelbeispiel mitnehmen; MQTT-Topic-Overhead präzisiert ('nicht der Topic-Baum als Struktur, sondern dass der Topic-Name Bestandteil jeder einzelnen PUBLISH-Nachricht ist') – Selbsttest Q7 nachgezogen; Cloud-Ausfall-Zeile der Vergleichstabelle entschärft ('Cloud-abhängige Funktionen ... nicht verfügbar', nicht pauschal 'funktioniert nicht mehr'); Wartungs-/Update-Aufwand (OTA, Angriffsflächen) als zusätzliche Edge-Nachteil-Zeile in der Vergleichstabelle ergänzt, mit Rückverweis auf LF7.3; kombinierte Transferfrage (Türsensor-Szenario, alle drei Artikelbausteine) als Bonusaufgabe nach dem Selbsttest ergänzt. Lernzeit-Formulierung präzisiert (Bezug auf Typfragen/Rechenbeispiele statt unspezifisch 'Aufgaben', da kein separates Aufgabenkapitel existiert – Fund aus Review 3). NICHT ÜBERNOMMEN: Review 1s Behauptung einer Pflichtaufgaben-Zählung von 14 statt 15 – geprüft und nicht bestätigt: Abschnitt 3.2 deckt zwei Pflichtaufgaben der Rohdatei LF7.2.3 gemeinsam ab (Vergleich JSON/Binär UND konkrete Umwandlung eines Datensatzes); Letzteres war im Fließtext nicht explizit als eigene Aufgabe erkennbar – daher jetzt mit einer eigenen 'Pflichtaufgabe – Beispiel-Umwandlung'-Box in 3.2 sichtbar gemacht, damit alle 15 Pflichtaufgaben auch strukturell einzeln erkennbar sind, statt nur die Zählung in der YAML zu ändern. Sektionsüberschrift 3.4-Vorschlag ('Payload-Optimierung & energieeffiziente Übertragung' statt 'Time-on-Air') nicht übernommen, da Anchor-Links in den IHK-Kernfragen auf die bestehende Überschrift verweisen und der Mehrwert gering ist. Terminologie-Vereinheitlichung (Review 3: 'Microcontroller vs. Mikrocontroller') geprüft – im Artikel wird durchgängig nur 'Microcontroller' verwendet (konsistent mit Rohmaterial-Schreibweise), keine tatsächliche Inkonsistenz gefunden. Noch OFFEN: finale Freigabe durch Auftraggeber."
  - runde: 3
    datum: 2026-09-14
    ergebnis: "Externe Prüfung (3 Reviews) auf die Runde-2-Fassung eingearbeitet. Alle drei Reviews bestätigten Runde-2-Korrekturen (Binär/Hex, RTC-Domäne/ULP, MQTT-Topic-Overhead) als fachlich korrekt umgesetzt und fanden nur noch Restabsolutheiten sowie eine Dokumentations-Inkonsistenz. WICHTIGSTER FUND (2 von 3 Reviews unabhängig, teils mit Espressif-Quellenbezug): Trotz Runde-2-Korrektur der Haupttextstelle blieben mehrere Stellen bei der zu absoluten 'CPU/RAM/Funkmodule werden abgeschaltet'-Formulierung bzw. bei 'ein Coprozessor bleibt wach' hängen – Selbsttest Q2 präzisiert ('CPU und Funkmodule ... ebenso der größte Teil des normalen RAM'), Merksatz zu Deep Sleep korrigiert (ULP-Coprozessor als optional statt fest gekennzeichnet). Weitere Korrekturen: 'nahezu stromlos' (Abschnitt 4) auf 'nur einen sehr geringen Strom verbraucht' präzisiert; Transferfrage (Türsensor) um den Hinweis ergänzt, dass eine externe Wake-up-Quelle allein die geforderte 500-ms-Reaktion nicht garantiert, da nach dem Aufwachen weiterhin Boot-/Initialisierungszeit anfällt; Selbsttest Q5 entschärft ('können abgelegt werden' statt 'müssen', mit Abgrenzung RTC-Memory vs. nichtflüchtiger Speicher); 'gleicht einem kompletten Neustart' präzisiert auf 'CPU-Ausführungszustand geht verloren, durchläuft erneut den normalen Startpfad'; 'Hardware-Interrupt reagiert sofort' auf 'Reaktion mit sehr geringer Verzögerung' abgeschwächt (Selbsttest Q3; die ausführliche Typfrage in 2.3 nutzte bereits korrekt 'unmittelbar', war also von diesem Fund nicht betroffen). Explizite Begriffsabgrenzung 'On-Time ≠ Time-on-Air' nach 2.6 ergänzt (On-Time = gesamte aktive Phase, Time-on-Air = nur die reine Funkübertragungszeit als Teilabschnitt davon) plus neue Selbsttest-Frage 9 dazu. Binärkodierungs-Beispiel (3.2) um Voraussetzung 'festes, vorher vereinbartes Datenschema zwischen Sender und Empfänger' ergänzt. Time-on-Air-Erklärung (3.3) um Hinweis ergänzt, dass bei Funktechniken wie LoRa zusätzlich Spreizfaktor/Bandbreite/Codierungsrate die Sendezeit beeinflussen, Payload-Größe also nur ein Faktor von mehreren ist. Batterielaufzeit-Rechenbeispiel um Idealisierungshinweis ergänzt (volle Nennkapazität angenommen) und um Spannungseinbrüche bei Sendespitzen als weiteren Praxis-Einfluss erweitert. ECHTE DOKUMENTATIONS-INKONSISTENZ GEFUNDEN UND BEHOBEN (1 Review): YAML-Quellenangabe zu den ESP32-Stromwerten nannte noch '160–240 mA', während der Haupttext bereits korrekt '100–240 mA' verwendet (Rest eines vor Runde 1 überarbeiteten Zwischenstands) – YAML-Text angeglichen. Kleine Präzisierung: 'wenige Stunden bis maximal etwa einem Tag' (2.1) auf konkrete Rechenspanne 'rund 10 bis 25 Stunden' präzisiert. NICHT BESTÄTIGT (gezielt gegen die Datei geprüft, wie in vorherigen Runden): Behauptung eines LaTeX-Artefakts ('Anteil*i' statt 'Anteil_i') in der Batterielaufzeit-Formel – Formel ist korrekt (`\\text{Anteil}_i`), kein Artefakt gefunden. Ebenso nicht bestätigt: verklebte Selbsttest-Überschrift, abgeschnittene Frage 8, fehlender Zeilenumbruch nach dem letzten Cheatsheet-Eintrag – alle drei Stellen bei Sichtprüfung und grep sauber formatiert; mutmaßlich erneut Artefakte des jeweiligen Textausschnitts, nicht der Datei selbst. NICHT ÜBERNOMMEN (Abwägung): MQTT-Topic-Overhead-Abschnitt (3.4) als 🟢 statt Kernbestandteil einstufen – beibehalten als regulärer Abschnitt, da er eine der fünf Pflichtaufgaben der Rohdatei LF7.2.3 abdeckt, nicht nur optionale Vertiefung; ESP32 durchgängig zu 'ESP32-Board' umbenennen – nicht übernommen, da der Fließtext bereits 'abhängig von Chipvariante, Funkphase, Sendeleistung und Board' hedged und eine komplette Umbenennung keinen zusätzlichen fachlichen Mehrwert brächte. Nach dieser Runde keine neuen fachlichen Kernbefunde mehr, nur noch optionale/kosmetische Anmerkungen laut allen drei Reviews."
  - runde: "4 (eigener Abschluss-Selbstcheck)"
    datum: 2026-09-14
    ergebnis: "Vollständige Datei zeilenweise gelesen, YAML validiert, alle Rechenbeispiele (Fall 1: 10 Std., Fall 2: 1,01 mA Ø-Verbrauch/990 Std./41 Tage, Selbsttest Q4: 40 Std., 2.500 mAh/100-240 mA: 10-25 Std.) mit Python nachgerechnet und bestätigt. Gezielte Volltextsuche nach Absolutheits-Resten ('immer', 'garantiert', 'zwingend', 'extrem') durchgeführt – keine echten Treffer, alle Fundstellen entweder korrekt gehedgt oder bewusst die falsche Seite einer Prüfungsfalle. Ein Rest gefunden und behoben: Stand-Datum im Kopf/YAML war noch auf 2026-09-13 (Runde-2-Stand), obwohl Runde 3 bereits am 2026-09-14 stattfand - auf 2026-09-14 aktualisiert. Keine weiteren fachlichen oder strukturellen Fehler gefunden."
freigabe: "Freigegeben – Status auf Final gesetzt nach 3 Runden externer Prüfung (insgesamt 9 Reviews) + eigenem Abschluss-Selbstcheck, 2026-09-14, auf explizite Anweisung des Auftraggebers ('finalen check und wenn keine Fehler mehr final setzen')."
```