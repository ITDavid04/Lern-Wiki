# LF7.1 – Architektur & IoT-Kommunikation

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 90–120 Minuten reines Lesen, +60–80 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was unterscheidet Embedded System, IoT und Cyber-physisches System (CPS) voneinander? | [→ 1. Grundlagen](#1-grundlagen-embedded-system-iot-und-cyber-physische-systeme) |
| 2 | Was sind die Grundbausteine eines CPS (Sensor, Aktor, Controller, Gateway), und was unterscheidet eine Stern- von einer Mesh-Topologie? | [→ 2. Komponenten & Topologie](#2-komponenten-und-topologie-cyber-physischer-systeme) |
| 3 | Welcher Zielkonflikt besteht zwischen Reichweite, Bandbreite und Energieverbrauch bei IoT-Funktechnologien, und wann sind kabelgebundene Feldbusse vorzuziehen? | [→ 3. Übertragungstechnologien](#3-iot-übertragungstechnologien-im-vergleich) |
| 4 | Wie funktioniert das Publish/Subscribe-Muster von MQTT, und was bedeuten die drei QoS-Stufen? | [→ 4. MQTT](#4-das-publishsubscribe-muster-mit-mqtt) |
| 5 | Warum ist der MQTT-Broker ein Single Point of Failure, und welche IT-Sicherheitsrisiken bestehen bei unverschlüsseltem MQTT? | [→ 4.3 Der Broker als Flaschenhals](#43-der-broker-als-flaschenhals-und-sicherheitsaspekte) |

---

## 1. Grundlagen: Embedded System, IoT und Cyber-physische Systeme

> **Grundprinzip:** Eine Waschmaschine mit eingebauter Steuerung ist wie ein Handwerker, der allein in seiner Werkstatt arbeitet – autark, aber isoliert. Ein IoT-Gerät ist derselbe Handwerker mit Telefon, der Bestellungen entgegennimmt und Ergebnisse meldet. Ein cyber-physisches System ist der Handwerksbetrieb, der zusätzlich laufend auf Rückmeldungen vom Kunden reagiert und seine Arbeitsweise darauf anpasst.

### 1.1 Abgrenzung der drei Begriffe

Die drei Begriffe überschneiden sich stark und werden in der Praxis nicht immer trennscharf verwendet – für die Prüfung reicht ein klares Grundverständnis der jeweiligen Schwerpunkte:

| Begriff | Kernidee | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Embedded System (Eingebettetes System)** | Ein in sich geschlossenes Computersystem, das eine feste Aufgabe erfüllt – meist ohne Vernetzung nach außen | Waschmaschinensteuerung, Klimaanlagen-Thermostat ohne App-Anbindung | 🔴 |
| **Internet of Things (IoT)** | Physische Geräte (oft auf Basis eingebetteter Systeme) tauschen über Netzwerke – meist das Internet – eigenständig Daten aus | Smarte Steckdose, die per WLAN mit einer Cloud-App kommuniziert | 🔴 |
| **Cyber-physisches System (CPS)** | System, in dem physische Prozesse und digitale Informationsverarbeitung eng gekoppelt sind: Sensoren erfassen Zustände, digitale Systeme verarbeiten die Informationen und können über Aktoren auf den physischen Prozess zurückwirken. Eine Rückkopplung ist für CPS typisch, aber nicht zwingend als vollständig geschlossene Regelung ausgeprägt | Intelligente Absauganlage, die Feinstaubwerte misst und die Absaugleistung in Echtzeit automatisch nachregelt | 🔴 |

> **Wichtig für die Prüfung:** IoT betont vor allem die *Vernetzung physischer Geräte und den Datenaustausch*, CPS betont die *enge Kopplung digitaler Verarbeitung mit einem physischen Prozess* – häufig, aber nicht zwingend über eine vollständig geschlossene Regelschleife. Ein CPS kann z. B. auch innerhalb einer einzelnen Maschine ohne Internetanbindung funktionieren (rein lokales Feldnetz). Beide Konzepte überschneiden sich in der Praxis stark und werden in vielen industriellen und Smart-Home-Anwendungen synonym verwendet – für die Prüfung reicht es, den jeweiligen Schwerpunkt (Vernetzung vs. physische Kopplung/Rückwirkung) klar benennen zu können.

> **IHK-Typfrage:** *"Warum ist eine internetfähige Wetterstation, die nur Messwerte in einer App anzeigt, kein typisches Beispiel für ein cyber-physisches System?"*
> **Musterantwort:** Ein CPS zeichnet sich typischerweise durch eine Rückwirkung auf die physische Welt aus: Die verarbeiteten Messwerte lösen über einen Aktor eine physische Reaktion aus. Eine reine Anzeige-App ist zwar ein IoT-Gerät, da sie Daten vernetzt austauscht, ihr fehlt aber diese aktive physische Rückwirkung – sie bleibt bei der reinen Beobachtung stehen, statt selbst auf den Prozess einzuwirken.

---

## 2. Komponenten und Topologie cyber-physischer Systeme

> **Grundprinzip:** Ein Zollstock misst nur die Länge eines Brettes – er kann niemals selbst zur Säge greifen. Erst der Handwerker (der die Messung auswertet) entscheidet, ob und wie gesägt wird. Sensor und Aktor sind ohne die auswertende Instanz dazwischen nutzlos.

### 2.1 Die vier Grundbausteine

| Baustein | Aufgabe | Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Sensor** | Erfasst physische Umgebungsgrößen (Temperatur, Druck, Helligkeit, Feuchtigkeit) und wandelt sie in elektrische Signale um | Temperaturfühler, Feinstaubsensor | 🔴 |
| **Aktor** | Empfängt digitale Befehle und wandelt sie in mechanische Arbeit oder eine physische Reaktion um | Motor, Ventil, Relais, LED | 🔴 |
| **Controller/Microcontroller** | Das lokale "Gehirn": liest Sensordaten aus, wertet sie aus und steuert Aktoren an (z. B. ESP32, Arduino) | Steuerplatine in einer Absauganlage | 🔴 |
| **Gateway** | Knotenpunkt, der lokale, teils inkompatible Netzwerke (z. B. Bluetooth-Sensoren) mit weitreichenden IP-Netzwerken (Internet/WLAN) verbindet – kann dabei Protokolle, Datenformate oder Adressierung anpassen, muss dies aber nicht zwingend tun | Raspberry Pi als Bluetooth-zu-MQTT-Brücke | 🔴 |

> **Verwechslungsgefahr:** Ein Sensor erfasst zunächst nur eine physische Größe – die Auswertung und Aktorsteuerung erfolgt typischerweise durch einen Controller oder eine integrierte Verarbeitungseinheit (in der in diesem Artikel verwendeten vereinfachten Grundarchitektur strikt getrennt dargestellt). In der Praxis können "intelligente" Sensor-/Controller-Module bereits eine einfache lokale Logik enthalten und z. B. bei Überschreiten eines Grenzwerts direkt selbst schalten – die grundsätzliche Reihenfolge Erfassen → Auswerten → Wirken bleibt aber bestehen. Ebenso muss nicht jeder Sensor direkt mit dem Internet verbunden sein: Oft sammelt ein Gateway die Daten von vielen "dummen" Funksensoren und leitet sie gebündelt weiter.

> **IHK-Typfrage:** *"Ein Netzwerk aus reinen Bluetooth-Sensoren soll über das Internet überwacht werden. Warum reicht ein einzelner Controller dafür nicht aus?"*
> **Musterantwort:** Bluetooth ist ein Nahbereichsprotokoll ohne direkte Internetfähigkeit. Ein Gateway wird benötigt, um zwischen dem lokalen Bluetooth-Netz und einem IP-basierten Netzwerk (WLAN/Internet) zu vermitteln – in diesem Fall muss es die Daten auch protokollseitig übersetzen (z. B. Bluetooth-Rohdaten in MQTT-Nachrichten), damit sie in einer Cloud-Anwendung ankommen.

### 2.2 Netzwerktopologien: Stern vs. Mesh

| Topologie | Funktionsweise | Vorteil | Nachteil | IHK-Relevanz |
| --- | --- | --- | --- | --- |
| **Stern-Topologie** | Jeder Sensorknoten kommuniziert direkt und ausschließlich mit einem zentralen Gateway/Hub | Einfacher Aufbau, übersichtliche Kommunikation, meist kurze Kommunikationswege zum zentralen Knoten | Der zentrale Hub ist ein Single Point of Failure – fällt er aus, ist das gesamte Netz betroffen | 🔴 |
| **Mesh-Topologie** | Bestimmte Knoten (Router) können Nachrichten anderer Knoten empfangen und weiterleiten (Routing), sodass Daten über mehrere Zwischenstationen ihr Ziel erreichen | Selbstheilend: Fällt ein Knoten aus, können Nachrichten oft über andere Router umgeleitet werden; größere Flächenabdeckung möglich | Höhere Komplexität, tendenziell höhere Latenz durch mehrere "Hops", höherer Energiebedarf für weiterleitende Knoten | 🔴 |

> Praxisbeispiel: **Zigbee** kann Mesh-Topologien aufbauen und unterscheidet dabei drei Rollen: einen **Coordinator** (baut das Netz auf), **Router** (leiten Nachrichten anderer Knoten weiter und vergrößern so die Netzabdeckung) und **End Devices** (einfache Endgeräte, die *nicht* automatisch die Routerfunktion übernehmen, oft um Energie zu sparen). Zigbee unterstützt neben Mesh auch Stern- und Baum-Topologien – welche Rolle ein Gerät einnimmt, hängt von seiner Konfiguration ab, nicht automatisch von der Zugehörigkeit zum Netz.

> **IHK-Typfrage:** *"Ein Microcontroller soll gleichzeitig als Endgerät (misst selbst) und als Gateway für andere Sensoren fungieren. Unter welcher Voraussetzung ist das sinnvoll möglich?"*
> **Musterantwort:** Das setzt ausreichende Rechenleistung, genügend freien Speicher und mindestens zwei unterschiedliche Kommunikationsschnittstellen voraus (z. B. Bluetooth zum Empfangen der Sensordaten anderer Geräte und WLAN zum Weiterleiten an die Cloud). Zusätzlich muss die Software beide Rollen gleichzeitig zuverlässig bedienen können, ohne dass die eine Aufgabe (z. B. Routing fremder Daten) die eigene Messfunktion blockiert.

---

## 3. IoT-Übertragungstechnologien im Vergleich

> **Grundprinzip:** Ein Logistikunternehmen kann nicht gleichzeitig den schnellsten, den günstigsten und den am weitesten reichenden Versand anbieten – ein Expresskurier ist schnell, aber teuer und nur lokal sinnvoll; ein Postweg über Wochen erreicht dafür jeden Winkel der Erde mit minimalem Aufwand. Bei IoT-Funktechnologien gilt dasselbe Prinzip für Reichweite, Bandbreite und Energieverbrauch.

### 3.1 Das IoT-Dreieck

IoT-Funktechnologien müssen typischerweise zwischen Reichweite, Datenrate (Bandbreite) und Energieverbrauch abwägen – eine Verbesserung einer Eigenschaft geht in der Praxis meist zulasten mindestens einer anderen. Das ist kein striktes Naturgesetz, aber ein sehr verlässliches Entwurfsmuster bei der Wahl einer Funktechnologie:

| Technologie | Reichweite | Bandbreite | Energiebedarf |
| --- | --- | --- | --- |
| **WLAN** | Gering | Hoch | Hoch |
| **BLE/Zigbee** | Mittel | Mittel | Gering |
| **LoRaWAN/NB-IoT (LPWAN)** | Hoch | Sehr gering | Sehr gering |

> **Hinweis:** Diese Zuordnung ist eine qualitative Orientierung, keine exakte technische Klassifikation – die drei Eigenschaften lassen sich nicht unabhängig voneinander maximieren, aber keine Technologie liegt exakt in einer einzelnen "Ecke". Tatsächliche Reichweite, Datenrate und Energieverbrauch hängen zusätzlich von Sendeleistung, Umgebung, Protokollversion und Betriebsart ab.

### 3.2 Kurzstrecken-Funktechnologien

| Technologie | Frequenz | Typische Reichweite | Bandbreite | Energiebedarf | Typischer Einsatz | IHK-Relevanz |
| --- | --- | --- | --- | --- | --- | --- |
| **WLAN/Wi-Fi** | 2,4 GHz (ISM) und 5 GHz (lizenzfreie U-NII-Bänder, kein ISM im engeren Sinn) | Wenige zehn Meter (Innenräume) | Hoch (mehrere hundert Mbit/s) | Sehr hoch | Video-Streaming, Geräte mit Netzanschluss | 🔴 |
| **Bluetooth / BLE** | 2,4 GHz (ISM) | Typischerweise wenige bis einige 10 m; je nach BLE-Modus/Sendeleistung und Umgebung auch deutlich mehr | Klassisch bis 2–3 Mbit/s, BLE je nach Version bis ca. 1–2 Mbit/s (Bluetooth 5 verdoppelt die maximale PHY-Datenrate auf 2 Mbit/s) | Gering (BLE speziell auf Energieeffizienz ausgelegt) | Wearables, Smart-Home-Sensoren in Gebäudenähe | 🔴 |
| **Zigbee** | 2,4 GHz global, zusätzlich 868/915 MHz je nach Region | Ca. 10–100 m pro Hop, durch Mesh-Weiterleitung größere Gesamtabdeckung | Bis ca. 250 kbit/s | Gering | Smart-Home-Netze mit vielen Knoten (bis zu 65.000 Geräte je Netz laut Spezifikation) | 🟡 |

> Alle drei Technologien nutzen (zumindest teilweise) das lizenzfreie **2,4-GHz-ISM-Band**, das durch die parallele Nutzung durch WLAN, Bluetooth und Zigbee stark ausgelastet und störanfällig sein kann.

### 3.3 LPWAN: Reichweite statt Bandbreite

**Low Power Wide Area Networks (LPWAN)** gehen den gegenteiligen Kompromiss ein: minimale Bandbreite und minimaler Energieverbrauch zugunsten großer Reichweite.

| Technologie | Frequenz | Reichweite | Bandbreite | Energiebedarf | Besonderheit | IHK-Relevanz |
| --- | --- | --- | --- | --- | --- | --- |
| **LoRaWAN** | Lizenzfreies ISM-Band (in Europa z. B. 868 MHz) | Ländlich ca. 10–15 km, städtisch (durch Bebauung) eher 2–5 km | Sehr gering (wenige Bytes bis kBit-Bereich je Übertragung) | Extrem gering – Batterielaufzeiten von mehreren Jahren möglich | Im europäischen 868-MHz-Bereich gilt eine **Duty-Cycle-Begrenzung** – eine ETSI-Regulierung des Frequenzbands selbst (nicht LoRaWAN-spezifisch), die je nach genutztem Subband unterschiedlich ausfällt (z. B. teils 1 %, teils strengere Grenzen) | 🔴 |
| **NB-IoT (Narrowband IoT)** | Lizenziertes Mobilfunkband | Reichweite wie Mobilfunk (über Provider-Zellen) | Gering, aber höher als LoRaWAN | Gering | Nutzt vorhandene Mobilfunk-Infrastruktur eines Providers, kostet dafür laufende Gebühren; ist nicht durch ISM-Band-Überlastung gestört, dafür vom jeweiligen Provider-Netz abhängig – typischerweise ohne nahtlosen Zellwechsel für mobile Geräte und mit teils höherer Latenz als klassischer Mobilfunk | 🟡 |

> **Aktualitätshinweis:** Die LoRaWAN-Spezifikation wird von der LoRa Alliance in zwei Teilen gepflegt: dem Link-Layer-Standard (aktuell in der 1.0-Linie **TS001-1.0.4**) und den regionalen Funkparametern (aktuell **RP002-1.0.5**, Stand Oktober 2025), die u. a. Sendeleistung und Kanalbelegung je Weltregion festlegen. Zusätzlich unterscheidet LoRaWAN drei Geräteklassen: **Klasse A** (Downlink nur unmittelbar nach einem Uplink, maximale Energieeffizienz), **Klasse B** (zusätzliche, zeitgesteuerte Empfangsfenster) und **Klasse C** (nahezu durchgehendes Empfangsfenster, dafür höherer Verbrauch) – für die Grundlagenprüfung reicht das Verständnis, dass eine höhere Empfangsbereitschaft immer mit höherem Energieverbrauch erkauft wird.

### 3.4 Kabelgebundene Feldbusse

Nicht jede IoT-Anwendung profitiert von Funktechnik. In Produktionsumgebungen mit hohem Störpotenzial (Motoren, Frequenzumrichter) und harten Echtzeitanforderungen dominieren weiterhin kabelgebundene **Feldbusse**:

| Feldbus | Typischer Einsatz | Vorteil gegenüber Funk | IHK-Relevanz |
| --- | --- | --- | --- |
| **KNX** | Gebäudeautomation (Licht, Heizung, Jalousien) | Etablierter, herstellerübergreifender Standard für Gebäudetechnik | 🟡 |
| **PROFIBUS / PROFINET** | Industrielle Automatisierung, Maschinensteuerung (zwei unterschiedliche, verwandte Automatisierungsstandards – PROFIBUS feldbusbasiert, PROFINET Ethernet-basiert) | Für industrielle Echtzeitkommunikation ausgelegt und deutlich deterministischer als typische Funknetze, unabhängig von Funkstörungen | 🟡 |
| **Modbus** | Weit verbreitetes, einfaches Industrieprotokoll für SPS und Sensorik | Sehr simpel und robust, breite Geräteunterstützung | 🟡 |
| **CAN (Controller Area Network)** | Fahrzeugtechnik, Maschinenbau | Sehr hohe Störfestigkeit, etabliert im Automotive-Bereich | 🟡 |

> **IHK-Typfrage:** *"Warum würde eine Tischlerei mit vielen Metall-Maschinen und starken elektromagnetischen Störquellen für die Absaugungssteuerung eher einen kabelgebundenen Feldbus als WLAN wählen?"*
> **Musterantwort:** Kabelgebundene Feldbusse sind unabhängig von Funkstörungen durch Motoren, Frequenzumrichter oder das überlastete 2,4-GHz-ISM-Band und bieten deutlich deterministischere, vorhersagbarere Latenzen als typische Funknetze – wichtig, da ein Ausfall der Absaugsteuerung sofort einen Produktionsstopp bedeuten kann. Funktechnik wäre hier einem Risiko unvorhersehbarer Signalstörungen ausgesetzt, das bei einer sicherheitskritischen Anlage vermieden werden soll.

### 3.5 BLE vs. LoRaWAN: zwei gegensätzliche Philosophien

| Kriterium | Bluetooth Low Energy (BLE) | LoRaWAN |
| --- | --- | --- |
| Typischer Einsatz | Wearables, Smart-Home-Geräte in Gebäudenähe, Kopplung mit Smartphone | Flächendeckendes Monitoring über große Distanzen (Landwirtschaft, Smart City, Zählerfernauslesung) |
| Reichweite | Typischerweise wenige bis einige 10 m, stark umgebungsabhängig | Mehrere Kilometer |
| Bandbreite | Bis ca. 1–2 Mbit/s | Wenige Bytes bis kBit-Bereich pro Übertragung |
| Batterielaufzeit | Tage bis mehrere Jahre, stark abhängig von Sendeintervall, Datenmenge und Betriebsart | Mehrere Jahre möglich |
| Typisches Szenario | Fitnesstracker sendet Vitaldaten an eine App in der Hosentasche | Bodenfeuchtesensor auf einem entlegenen Acker sendet einmal täglich einen Messwert |

> **IHK-Typfrage:** *"Warum würde man einen Fitnesstracker nicht mit LoRaWAN und einen Feldsensor auf einem 5 km entfernten Acker nicht mit BLE ausstatten?"*
> **Musterantwort:** Ein Fitnesstracker liegt nah am koppelnden Smartphone und muss vergleichsweise häufig größere Datenmengen (Puls, Bewegungsprofile) senden – dafür ist BLE mit seiner höheren Bandbreite auf kurzer Distanz ideal. Ein Feldsensor über mehrere Kilometer Entfernung würde mit BLE gar keine Verbindung aufbauen können, da dessen Reichweite bei weit unter einem Kilometer liegt – hier ist LoRaWAN mit seiner großen Reichweite die einzig sinnvolle Wahl, obwohl es nur wenige Messwerte pro Tag überträgt.

### 3.6 Lizenzfreie vs. lizenzierte Frequenzbänder

| Aspekt | Lizenzfreies ISM-Band (z. B. 868 MHz, 2,4 GHz) | Lizenziertes Mobilfunkband (z. B. NB-IoT) |
| --- | --- | --- |
| Kosten | Keine Frequenznutzungsgebühr, aber Hardware-/Betriebskosten | Laufende Provider-/SIM-Gebühren pro Gerät |
| Regulierung | Durch Duty-Cycle- und Sendeleistungsgrenzen reguliert, aber von jedem nutzbar | Exklusiv durch den lizenzierten Netzbetreiber vergeben |
| Störanfälligkeit | Höher – das Band wird von vielen verschiedenen Technologien und Nutzern gleichzeitig verwendet | Geringer – der Betreiber kontrolliert die Zellenauslastung |
| Reichweite/Abdeckung | Abhängig vom selbst aufgebauten Gateway-Netz | Nutzt die vorhandene Mobilfunk-Infrastruktur des Providers, abhängig von dessen tatsächlichem Netzausbau am Standort |

> **IHK-Typfrage:** *"Ein Unternehmen möchte 500 Sensoren deutschlandweit verteilt betreiben, ohne eigene Gateway-Infrastruktur aufzubauen. Lizenzfreies LoRaWAN oder lizenziertes NB-IoT?"*
> **Musterantwort:** Ohne eigene Gateway-Infrastruktur ist NB-IoT die praktikablere Wahl, da es die vorhandene Mobilfunk-Infrastruktur eines Providers nutzen kann, sodass kein eigenes Gateway-Netz aufgebaut werden muss – der Aufbau eigener LoRaWAN-Gateways an 500 verteilten Standorten wäre dagegen aufwendig und unwirtschaftlich. Der Kompromiss dafür sind laufende Provider-Gebühren pro SIM-Karte/Gerät, die bei einer selbst betriebenen LoRaWAN-Infrastruktur entfallen würden – zudem hängt die tatsächliche Abdeckung vom Netzausbau des jeweiligen Providers an den konkreten Standorten ab.

### 3.7 Randnotiz: Anwendungsschicht für ressourcenarme Geräte

🟢 **Nice to know:** Neben MQTT (siehe Abschnitt 4) existiert mit **CoAP (Constrained Application Protocol)** ein weiteres, HTTP-ähnliches Protokoll, das speziell für sehr ressourcenarme Geräte entwickelt wurde und meist über UDP statt TCP läuft – zur Absicherung kann CoAP per **DTLS** (das UDP-Pendant zu TLS) verschlüsselt werden. Für die Grundlagenprüfung reicht das Wissen, dass es existiert und WLAN-/LPWAN-Sensor-Ökosysteme ergänzt – der Fokus dieses Artikels liegt auf dem in der Praxis dominierenden MQTT.

---

## 4. Das Publish/Subscribe-Muster mit MQTT

> **Grundprinzip:** Wer eine Fachzeitschrift abonniert, bestellt nicht bei jedem einzelnen Autor persönlich – ein Verlag (der Broker) sammelt alle Beiträge und verteilt sie automatisch an alle Abonnenten des jeweiligen Themengebiets. Die Autoren wissen nicht einmal, wer die Zeitschrift liest.

### 4.1 Client/Server vs. Publish/Subscribe

| Modell | Funktionsweise | IHK-Relevanz |
| --- | --- | --- |
| **Client/Server (z. B. HTTP)** | Ein Client sendet eine Anfrage direkt an einen bestimmten Server und wartet auf dessen Antwort – beide Seiten kennen sich | 🔴 |
| **Publish/Subscribe (MQTT)** | Im klassischen MQTT-Modell kommunizieren Publisher und Subscriber nicht direkt miteinander, sondern ausschließlich über den Broker. Ein Gerät veröffentlicht (*publish*) Daten zu einem Thema (*Topic*), andere Geräte abonnieren (*subscribe*) dieses Thema – Sender und Empfänger sind vollständig entkoppelt und kennen sich nicht | 🔴 |

**MQTT (Message Queuing Telemetry Transport)** ist ein weit verbreitetes, leichtgewichtiges Nachrichtenprotokoll für IoT-Anwendungen: TCP/IP-basiert und mit geringem Overhead. Aktuell sind zwei Versionen relevant: **MQTT 3.1.1** (2014 als OASIS-Standard verabschiedet, auf vielen älteren Geräten weiterhin im Einsatz) und **MQTT 5.0** (2019 als OASIS-Standard verabschiedet, u. a. mit Gründen für Verbindungsabbrüche, Themen-Aliasen und geteilten Abonnements erweitert).

### 4.2 Broker, Topics und Quality of Service

| Konzept | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Broker** | Der zentrale Server, der alle Nachrichten empfängt und sofort an alle passenden Abonnenten verteilt | 🔴 |
| **Topic (Thema)** | Hierarchisch aufgebauter Nachrichtenkanal, ähnlich einem Dateipfad, z. B. `fabrik/halle1/sensor/temperatur` | 🔴 |
| **QoS 0 – "At most once"** | Nachricht wird ohne Bestätigung gesendet ("Fire and forget") – kann verloren gehen, minimaler Overhead | 🔴 |
| **QoS 1 – "At least once"** | Die Nachricht wird bestätigt und bei fehlender Bestätigung erneut übertragen, wodurch sie mindestens einmal zugestellt wird – dabei kann sie mehrfach beim Empfänger ankommen | 🔴 |
| **QoS 2 – "Exactly once"** | Garantiert genau einmalige Zustellung durch einen mehrstufigen Bestätigungsprozess – höchste Zuverlässigkeit, aber auch höchster Overhead und höchste Latenz | 🔴 |

**Beispiel: Topic-Baum für ein Gebäude mit drei Stockwerken**

Für ein Gebäude, in dem auf jedem Stockwerk Temperatur und Luftfeuchtigkeit gemessen werden, bietet sich eine hierarchische Struktur von grob nach fein an:

```text
gebaeude1/
├── stock1/
│   ├── temperatur
│   └── luftfeuchtigkeit
├── stock2/
│   ├── temperatur
│   └── luftfeuchtigkeit
└── stock3/
    ├── temperatur
    └── luftfeuchtigkeit
```

Ein Client, der sich nur für die Temperatur im gesamten Gebäude interessiert, kann mit der Wildcard `gebaeude1/+/temperatur` gezielt alle Stockwerke gleichzeitig abonnieren, ohne für jedes Stockwerk einzeln zu abonnieren – die `+`-Wildcard steht dabei für genau eine Ebene im Themenbaum (im Unterschied zur `#`-Wildcard, die alle folgenden Ebenen umfasst, siehe Abschnitt 4.3).

> **IHK-Typfrage:** *"Welches QoS-Level eignet sich für einen unkritischen, routinemäßigen Temperaturwert? Und warum sollte MQTT QoS 2 trotzdem nicht einfach als Ersatz für eine sicherheitsgerichtete Not-Halt-Kommunikation betrachtet werden?"*
> **Musterantwort:** Für den routinemäßigen Temperaturwert genügt häufig **QoS 0**, da ein gelegentlicher Verlust unkritisch ist und der Wert kurz danach ohnehin erneut gesendet wird – der geringe Overhead spart Bandbreite und Energie. QoS 2 bietet zwar eine garantiert genau einmalige Zustellung *auf MQTT-Protokollebene*, macht MQTT dadurch aber nicht automatisch zu einem sicherheitsgerichteten Kommunikationssystem: Ein echter Maschinen-Nothalt erfordert zusätzlich funktionale Sicherheit, deterministisches Verhalten und dafür ausgelegte Safety-Systeme (z. B. eine hardwareseitige Not-Aus-Kette) – MQTT-QoS ersetzt diese Mechanismen nicht.

### 4.3 Der Broker als Flaschenhals und Sicherheitsaspekte

Das Pub/Sub-Muster entkoppelt Geräte hervorragend – bei einer Architektur mit nur **einer** Broker-Instanz wird der Broker dadurch aber zu einem **Single Point of Failure**: Fällt er aus, steht die gesamte Kommunikation still, obwohl alle Sensoren und Aktoren einzeln weiterhin funktionsfähig wären. (Dieses Risiko lässt sich durch mehrere gekoppelte Broker-Instanzen – Broker-Clustering – gezielt reduzieren, siehe Deep-Dive-Ausblick.)

Zusätzlich gilt für die Sicherheit:

- Viele IoT-Installationen betreiben MQTT standardmäßig unverschlüsselt über **Port 1883** – Nutzdaten und, sofern verwendet, MQTT-Benutzername/Passwort sind dann für jeden im selben Netzwerksegment mitlesbar (z. B. per Wireshark).
- **MQTT über TLS** (umgangssprachlich auch "MQTTS" genannt, typischerweise Port 8883) verschlüsselt die Verbindung. Bei korrekter Zertifikatsprüfung kann der Client zusätzlich die Identität des Brokers überprüfen und so Man-in-the-Middle-Angriffe erschweren bzw. verhindern – eine fehlerhafte oder fehlende Zertifikatsprüfung (z. B. das Ignorieren ungültiger Zertifikate) hebt diesen Schutz allerdings auf.
- Ergänzend zur Verschlüsselung gilt als zentrale organisatorische Schutzmaßnahme die **Netzwerksegmentierung**: IoT-Geräte werden in einem eigenen, vom übrigen Firmennetz getrennten Netzwerkbereich (z. B. eigenes VLAN) betrieben, damit ein kompromittierter Sensor nicht automatisch Zugriff auf das restliche Unternehmensnetz erlaubt.

> **Wildcard-Risiko:** Wer zu großzügig mit Topic-Wildcards arbeitet (z. B. dem `#`-Zeichen, das in MQTT alle untergeordneten Themen abonniert), kann versehentlich tausende Nachrichten gleichzeitig empfangen und dabei kleine Microcontroller überlasten.

---

## 5. Zusammenspiel der Konzepte in LF7.1

Die folgende Beispielarchitektur zeigt den vollständigen, bidirektionalen Datenweg – sowohl den Messwert vom Sensor zur Cloud als auch einen Steuerbefehl zurück zum Aktor:

```text
[ Sensor ]
     │  erfasst
     ▼
[ Controller/Microcontroller ]      (Stern- oder Mesh-Topologie,
     │                               z. B. Zigbee/BLE/LoRaWAN)
     ▼
[ Gateway ]
     │  MQTT Publish (Topic, QoS je nach Kritikalität)
     ▼
[ MQTT-Broker ]
     │  Subscribe
     ▼
[ Cloud / Server / Dashboard ]
     │  MQTT Publish: Steuerbefehl (eigenes Topic)
     ▼
[ MQTT-Broker ]
     │  Subscribe
     ▼
[ Gateway / Controller ]
     │
     ▼
[ Aktor ]
```

**Beispielhafte Architektur:** Der MQTT-Broker erscheint im Diagramm zweimal (einmal für den Uplink zur Cloud, einmal für den Downlink zum Aktor) – das ist **derselbe Broker**, nicht zwei getrennte Instanzen; die Darstellung soll nur den Hin- und Rückweg der Nachrichten verdeutlichen. Nicht jede IoT-Lösung braucht zwingend alle dargestellten Stationen. Ein ESP32 mit eingebautem WLAN kann z. B. direkt selbst beim Broker publizieren (`Sensor → ESP32 → MQTT-Broker`), ohne ein separates Gateway zu benötigen – ein eigenes Gateway wird vor allem dann nötig, wenn Sensoren ein Protokoll sprechen (z. B. reines Bluetooth), das keine direkte IP-/Internetverbindung erlaubt.

Die Wahl der Übertragungstechnologie (Abschnitt 3) bestimmt maßgeblich, wie der Pfad von Sensor bis Gateway aussieht; die Wahl von MQTT und QoS (Abschnitt 4) bestimmt, wie zuverlässig und wie schnell die Daten anschließend zum Server gelangen und zurück. Beide Entscheidungen hängen eng von der Topologie (Abschnitt 2) und den Anforderungen des jeweiligen Szenarios (Energie, Latenz, Reichweite) ab.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | IoT und CPS sind exakt dasselbe | IoT betont die Vernetzung physischer Geräte, CPS die enge Kopplung digitaler Verarbeitung mit einem physischen Prozess (häufig, aber nicht zwingend über eine vollständig geschlossene Regelschleife) – beide Konzepte überschneiden sich stark, sind aber nicht identisch definiert |
| 2 | Ein Sensor kann niemals eigene Logik enthalten | In der vereinfachten Grundarchitektur trennt man Sensor/Controller/Aktor strikt; in der Praxis können "intelligente" Sensor-Module bereits einfache lokale Logik enthalten – die grundsätzliche Reihenfolge Erfassen → Auswerten → Wirken bleibt aber bestehen |
| 3 | Jeder Sensor muss direkt mit dem Internet verbunden sein | Häufig sammeln Gateways die Daten vieler "dummer" Funksensoren und leiten sie gebündelt weiter |
| 4 | LoRaWAN ist für alle IoT-Anwendungen die beste Wahl, weil es die größte Reichweite hat | LoRaWAN bietet große Reichweite nur um den Preis sehr geringer Bandbreite – für Video oder schnelle Maschinensteuerung ungeeignet |
| 5 | Mesh-Topologien sind grundsätzlich einer Stern-Topologie überlegen | Mesh bietet höhere Ausfallsicherheit und Reichweite, aber auf Kosten von Komplexität, Latenz und höherem Energiebedarf pro weiterleitendem Knoten |
| 6 | MQTT ist wie eine normale Client/Server-Verbindung, nur "für IoT" | MQTT entkoppelt Sender und Empfänger im klassischen Modell vollständig über Topics und einen Broker – anders als das direkte Anfrage/Antwort-Muster von HTTP |
| 7 | QoS 2 sollte man für alle Nachrichten nutzen, um auf Nummer sicher zu gehen | QoS 2 verursacht den höchsten Overhead und die höchste Latenz – für unkritische Werte reicht QoS 0 oder 1 |
| 8 | Ein hohes MQTT-QoS-Level macht ein System automatisch sicherheitsgerichtet ("safe") | QoS beschreibt nur die Zustellzuverlässigkeit auf MQTT-Protokollebene – funktionale Sicherheit (z. B. ein Maschinen-Nothalt) erfordert dafür ausgelegte Safety-Systeme, die QoS nicht ersetzt |

---

## 7. Deep-Dive-Ausblick (freiwillig)

- **CoAP im Detail** (→ Abschnitt 3.7): Aufbau des REST-ähnlichen, UDP-basierten Protokolls und Abgrenzung zu MQTT.
- **Last Will and Testament (LWT)** (→ Abschnitt 4): Wie ein MQTT-Broker automatisch eine Nachricht veröffentlicht, sobald ein Client unerwartet die Verbindung verliert – nützlich zur Echtzeit-Erkennung von Sensor-Ausfällen.
- **Broker-Clustering / High Availability** (→ Abschnitt 4.3): Wie der Broker als Single Point of Failure durch mehrere gekoppelte Broker-Instanzen abgesichert werden kann.
- **Mesh-Routing-Algorithmen** (→ Abschnitt 2.2): Wie Knoten in einem Zigbee- oder Mesh-Netz automatisch den besten Übertragungsweg finden (z. B. AODV-Prinzip).
- **Signaldämpfung in Stahlbeton-Gebäuden** (→ Abschnitt 3.2): Warum Funktechnologien in Gebäuden mit starker Stahlbeton-Struktur stark an Reichweite verlieren, und welche Gegenmaßnahmen (Repeater, Wahl niedrigerer Frequenzen) helfen.
- **Kollisionsrisiko in unlizenzierten LPWAN-Netzen** (→ Abschnitt 3.3): Was passiert, wenn hunderte Geräte gleichzeitig im selben ISM-Band senden wollen, und wie Duty-Cycle-Grenzen und Zufallsverfahren (ALOHA-Prinzip) hier gegensteuern.
- **Physische Absicherung von IoT-Gateways** (→ Abschnitt 2.1): Konzepte für den Schutz von Gateways in öffentlich zugänglichen, rauen Industrieumgebungen (Gehäuseschutzklassen, Diebstahlschutz, Manipulationserkennung).
- **Lokale Hardware-Anbindung neuer Sensoren (I2C/SPI/GPIO):** wird in LF7.3 vertieft.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was unterscheidet IoT und CPS im Schwerpunkt? | IoT betont die Vernetzung und den Datenaustausch physischer Geräte; CPS betont die enge Kopplung digitaler Verarbeitung mit einem physischen Prozess, häufig mit Rückkopplung und aktiver Beeinflussung |
| 2 | Warum reicht in der vereinfachten Grundarchitektur ein Sensor allein nicht aus, um eine Maschine zu steuern? | Er erfasst nur die physische Größe; die Auswertung und Aktorsteuerung erfolgt typischerweise durch einen Controller oder eine integrierte Verarbeitungseinheit |
| 3 | Was ist der zentrale Nachteil einer Mesh-Topologie gegenüber einer Stern-Topologie? | Höhere Komplexität, tendenziell höhere Latenz und höherer Energiebedarf durch das Weiterleiten über mehrere Knoten |
| 4 | Warum ist LoRaWAN ungeeignet für Video-Streaming? | Die große Reichweite wird durch eine sehr geringe Bandbreite erkauft (Zielkonflikt des IoT-Dreiecks) |
| 5 | Was passiert beim MQTT-QoS-Level 1? | Die Nachricht wird bestätigt und bei Bedarf erneut übertragen, wodurch sie mindestens einmal zugestellt wird – dabei kann sie aber doppelt ankommen |
| 6 | Wann ist in einer IoT-Architektur typischerweise ein Gateway erforderlich? | Wenn Sensoren ein Kommunikationsverfahren verwenden, über das sie nicht selbst mit dem Ziel-/IP-Netz kommunizieren können (z. B. reines Bluetooth) und daher eine vermittelnde Instanz benötigen – ein WLAN-fähiger Microcontroller kann dagegen oft direkt selbst publizieren |
| 7 | Was ist der Unterschied zwischen den MQTT-Wildcards `+` und `#`? | `+` steht für genau eine Ebene im Topic-Baum, `#` für alle folgenden Ebenen – zu großzügige `#`-Nutzung kann kleine Microcontroller mit Nachrichten überlasten |
| 8 | Warum ist Netzwerksegmentierung (z. B. eigenes VLAN) eine sinnvolle IoT-Sicherheitsmaßnahme? | Ein kompromittiertes IoT-Gerät erhält dadurch keinen automatischen Zugriff auf das restliche Unternehmensnetz |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Embedded System** | In sich geschlossenes Computersystem für eine feste Aufgabe, meist ohne Vernetzung |
| **CPS** | Cyber-physisches System – enge Kopplung digitaler Informationsverarbeitung mit einem physischen Prozess, häufig (aber nicht zwingend) mit Rückkopplung über einen Aktor |
| **Sensor / Aktor** | Erfasst physische Größen / setzt digitale Befehle in physische Wirkung um |
| **Gateway** | Verbindet lokale (oft inkompatible) Netze mit dem Internet/IP-Netz – kann dabei Protokolle übersetzen, muss aber nicht |
| **IoT-Dreieck** | Typischer Zielkonflikt zwischen Reichweite, Bandbreite und Energieverbrauch bei der Wahl einer Funktechnologie |
| **LPWAN** | Low Power Wide Area Network – z. B. LoRaWAN, NB-IoT: minimale Bandbreite/Energie für maximale Reichweite |
| **Duty Cycle** | ETSI-Regulierung der Sendezeit im lizenzfreien Band (z. B. teils 1 % pro Stunde in bestimmten EU868-Subbändern) – Eigenschaft des Frequenzbands, nicht von LoRaWAN selbst |
| **MQTT** | Weit verbreitetes, leichtgewichtiges Publish/Subscribe-Protokoll über TCP/IP für IoT-Anwendungen |
| **Broker** | Zentraler MQTT-Server, verteilt Nachrichten an Abonnenten – bei Single-Broker-Architektur zugleich Single Point of Failure |
| **QoS 0/1/2** | Zustellsicherheit von MQTT: höchstens einmal / mindestens einmal / garantiert genau einmal |
| **QoS vs. Safety** | QoS beschreibt nur die Zuverlässigkeit der MQTT-Übermittlung, keine funktionale Sicherheit – ersetzt keine Safety-Systeme |
| **CoAP** 🟢 | HTTP-ähnliches, UDP-basiertes Protokoll für ressourcenarme Geräte, absicherbar per DTLS |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Begriffsabgrenzung | "Erläutern Sie den Unterschied zwischen X und Y" | Klare Kriterien nennen (z. B. IoT vs. CPS: Vernetzung physischer Geräte vs. enge Kopplung digitaler Verarbeitung mit einem physischen Prozess), nicht nur ein Beispiel als Ersatz für eine Definition |
| Technologieauswahl | "Welche Übertragungstechnologie würden Sie für Szenario X wählen?" | Begründung anhand der konkreten Anforderungen (Reichweite/Bandbreite/Energie/Latenz), nicht pauschal "das schnellste" oder "das modernste" |
| Architekturskizze | "Skizzieren Sie den Datenfluss von Sensor bis Server" | Alle Stationen (Sensor → Controller → Gateway → Broker → Server) korrekt und in der richtigen Reihenfolge benennen |
| Risikoanalyse | "Wo liegt der Single Point of Failure in diesem MQTT-Aufbau?" | Konkret den Broker benennen und eine Gegenmaßnahme (z. B. Clustering, TLS, Netzwerksegmentierung) nennen |

**Allgemeine Antwortstruktur für Begriffsfragen:** *Definition → Begründung → Beispiel.* Nicht mit einem Beispiel allein antworten (z. B. "CPS ist eine intelligente Absauganlage"), sondern zuerst den Begriff sauber definieren, die Abgrenzung begründen und das Beispiel erst danach als Illustration anführen.

---

## 11. Merksätze für das Fachgespräch

> IoT vernetzt Dinge, CPS koppelt digitale Verarbeitung eng mit physischen Prozessen – beide Konzepte überschneiden sich häufig, sind aber nicht deckungsgleich definiert.

> In der einfachen Grundarchitektur gilt: Der Sensor meldet, der Controller entscheidet, der Aktor führt aus – "intelligente" Module können diese Schritte bündeln, die Reihenfolge bleibt aber bestehen.

> Reichweite, Bandbreite, Energie – bei IoT-Funktechnologien geht die Verbesserung einer Eigenschaft meist zulasten mindestens einer anderen.

> MQTT trennt Sender und Empfänger im klassischen Modell über Topics und Broker – bei nur einer Broker-Instanz wird der Broker damit zum wichtigsten und zugleich verwundbarsten Teil des Systems.

> QoS beschreibt die Zuverlässigkeit der MQTT-Nachrichtenübermittlung – nicht die funktionale Sicherheit einer Anlage. Je wichtiger eine Nachricht, desto sorgfältiger die QoS-Wahl, aber QoS ersetzt keine Safety-Mechanismen.

---

```yaml
dokument: LF7.1-wiki-artikel
lernfeld: LF7.1
titel: "Architektur & IoT-Kommunikation"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-11
quellen_intern:
  - "LF7.1.1: Komponenten & Topologie cyber-physischer Systeme.md"
  - "LF7.1.2: IoT-Übertragungstechnologien im Vergleich.md"
  - "LF7.1.3: Das Publish/Subscribe Muster mit MQTT.md"
  - "Zusätzliches Material: IT-Handbuch-Überblick IoT/CPS (Definition, Abgrenzung, zusätzliche Protokolle/Feldbusse, Netzwerksegmentierung)"
quellen_fachlich:
  - titel: "LoRaWAN Link-Layer-Spezifikation TS001-1.0.4 / Regionalparameter RP002-1.0.5"
    herausgeber: "LoRa Alliance"
    status: "TS001-1.0.4 (Oktober 2020) weiterhin aktuelle 1.0-Linie; RP002-1.0.5 (Oktober 2025) aktuelle Regionalparameter. Reichweiten- und Duty-Cycle-Angaben gegen mehrere unabhängige Quellen geprüft (Herstellerdokumentation, Fachvortrag)"
  - titel: "MQTT Version 3.1.1 (OASIS Standard, 2014) und MQTT Version 5.0 (OASIS Standard, 2019)"
    herausgeber: "OASIS MQTT Technical Committee"
    status: "beide Versionen aktuell parallel im Einsatz; 5.0 mit erweiterten Features (Reason Codes, Topic-Aliase, Shared Subscriptions)"
  - titel: "IEEE 802.15.4 (Basis für Zigbee) / Zigbee-Spezifikation"
    herausgeber: "IEEE / Connectivity Standards Alliance (vormals Zigbee Alliance)"
    status: "Frequenz-/Reichweiten-/Knotenzahl-Angaben gegen mehrere unabhängige Quellen geprüft"
  - titel: "IT-Handbuch für Fachinformatiker*innen (nutzerseitig bereitgestellter Überblick zu IoT/CPS)"
    herausgeber: "unbekannt (vom Auftraggeber als Kontextmaterial bereitgestellt)"
    status: "Referenzlinks im Quellmaterial nicht nachvollziehbar/nicht übernommen; spekulative Prüfungsgewichtungs- und Stufenangaben (\"plausible Annahme\") aus diesem Material bewusst NICHT übernommen, da nicht durch Primärquelle belegt – nur unstrittige Kernaussagen (Begriffsabgrenzung, zusätzliche Protokolle/Feldbusse, Netzwerksegmentierung als Schutzmaßnahme) verwendet"
review_historie:
  - runde: 1
    datum: 2026-09-11
    ergebnis: "Erstdraft erstellt aus den drei LF7.1.x-Rohdateien plus vom Auftraggeber bereitgestelltem Zusatzmaterial (IT-Handbuch-Überblick). Web-Verifikation durchgeführt für: LoRaWAN-Spezifikationsstand und Reichweiten, MQTT-Versionsstände (3.1.1/5.0, OASIS), Zigbee/BLE-Frequenzen und Reichweiten. Begriffsabgrenzung IoT/CPS/Embedded System ergänzt (Lücke in den Rohdateien, aus Zusatzmaterial). Kabelgebundene Feldbusse (KNX/Profinet/Modbus/CAN) und CoAP als Randnotiz aus Zusatzmaterial ergänzt, ohne den Typ-A-Rahmen zu sprengen. Netzwerksegmentierung (VLAN) als Sicherheitsmaßnahme ergänzt."
  - runde: "1 (eigene Review)"
    datum: 2026-09-11
    ergebnis: "Eigene Review gegen Style-Guide-Checkliste und Abgleich mit allen fünf Pflichtaufgaben je Rohdatei durchgeführt. Zwei Lücken gefunden und behoben: (1) LF7.1.2-Pflichtaufgabe 2 (BLE vs. LoRaWAN Einsatzgebiete) war nur implizit über Tabellen abgedeckt – neuer Abschnitt 3.5 mit direktem Vergleich und Typfrage ergänzt; dabei gleich Abschnitt 3.6 zu lizenzfrei/lizenziert (Pflichtaufgabe 4) ergänzt. (2) LF7.1.3-Pflichtaufgabe 3 (konkreter Topic-Baum für 3-Stockwerk-Gebäude) fehlte komplett – Beispiel mit ASCII-Baum und Wildcard-Erklärung (`+` vs. `#`) ergänzt. Zusätzlich drei Rückverweise aus den 'Freiwilligen Zusatzaufgaben' der Rohdateien in den Deep-Dive-Ausblick aufgenommen (Signaldämpfung Stahlbeton, LPWAN-Kollisionsrisiko, physische Gateway-Absicherung), die zuvor fehlten."
  - runde: 2
    datum: 2026-09-11
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet, gewichtet nach fachlicher Substanz/Quellenbezug. WICHTIGSTER FUND (Review 1, sicherheitsrelevant): Typfrage/Musterantwort empfahl QoS 2 unqualifiziert für einen Maschinen-Nothalt – korrigiert auf 'QoS 2 ersetzt keine sicherheitsgerichtete Safety-Funktion', neue Prüfungsfalle Nr. 8 und Cheatsheet-Eintrag 'QoS vs. Safety' ergänzt. Weitere Korrekturen aus Review 1 (hoch gewichtet, mit Fachbegründung): CPS-Definition von 'zwingend geschlossene Regelschleife' auf 'typischerweise, aber nicht zwingend' entschärft (Tabelle, Wichtig-Block, Typfrage, Selbsttest Q1, Merksatz, Cheatsheet); 'Sensor kann niemals Aktor steuern' zu 'typischerweise über Controller, intelligente Module möglich' entschärft; Gateway-Protokollübersetzung als 'kann, muss aber nicht' formuliert; Zigbee-Topologie um Coordinator/Router/End-Device-Unterscheidung präzisiert (End Devices sind nicht automatisch Router); Stern-Topologie-Vorteil 'geringe Latenz' auf 'meist kurze Kommunikationswege' abgeschwächt; IoT-Dreieck von 'physikalisch nicht gleichzeitig maximierbar' auf 'müssen typischerweise abwägen' entschärft; BLE-Reichweitenangabe vereinheitlicht (vorher inkonsistent 10–100+ m vs. 50–150 m); Duty-Cycle-Aussage als ETSI-Bandregulierung statt LoRaWAN-Eigenschaft präzisiert und als subband-abhängig gekennzeichnet; NB-IoT-'bundesweit ausgebaut' auf 'vorhandene Provider-Infrastruktur, abhängig vom Netzausbau' abgeschwächt; Feldbus 'garantierte Echtzeit-Latenzen' auf 'deterministischer als typische Funknetze' abgeschwächt; MQTTS als 'MQTT über TLS (umgangssprachlich MQTTS)' klargestellt; Broker-SPOF-Aussage auf 'bei Single-Broker-Architektur' qualifiziert; 'Geräte kommunizieren nie direkt' auf 'im klassischen MQTT-Modell' präzisiert; Architekturdiagramm (Abschnitt 5) korrigiert – zeigt jetzt den vollständigen bidirektionalen Pfad (Broker war fälschlich direkt mit Aktor verbunden dargestellt) und einen Hinweis ergänzt, dass ein Gateway nicht in jeder Architektur zwingend ist; Lernzeit auf 90–120 Minuten angehoben. Aus Review 2 (mittel gewichtet) übernommen: WLAN-5-GHz-Band als U-NII statt ISM richtiggestellt; BLE-Bandbreite um Bluetooth-5-Angabe (2 Mbit/s) ergänzt; CoAP um DTLS-Hinweis ergänzt und als 🟢 markiert (Review 2 hatte zurecht bemängelt, dass 🟢 im gesamten Artikel nie tatsächlich vergeben wurde). Aus Review 3 (inhaltliche Punkte übernommen, strukturelle Punkte NICHT übernommen) übernommen: NB-IoT-Tabellenzeile um Nachteile (Provider-Abhängigkeit, kein nahtloser Zellwechsel, teils höhere Latenz) ergänzt; Duty-Cycle-Subband-Differenzierung (deckt sich mit Review 1). NICHT ÜBERNOMMEN: Review 3s Behauptung von sechs `[...]`-Platzhalter-Stellen und leeren Abschnitten 2.1/3.4/6 sowie fehlenden Leerzeilen vor Tabellen – beim Abgleich mit der tatsächlichen Datei (grep-Suche nach `[...]`, vollständige Sichtprüfung der genannten Abschnitte) nicht bestätigt: alle Abschnitte 1.1 bis 11 sind lückenlos vorhanden und gefüllt, keine Platzhalter im Dokument. Zusätzlich Selbsttest um 3 Fragen erweitert (Gateway-Notwendigkeit, Wildcards, Netzwerksegmentierung), da diese Kernkonzepte zuvor nicht abgefragt wurden (eigener Fund beim Einarbeiten). Prüfungstaktik um Antwortstruktur 'Definition → Begründung → Beispiel' ergänzt (Review 1). Noch OFFEN: finale Freigabe durch Auftraggeber."
  - runde: 3
    datum: 2026-09-11
    ergebnis: "Zweite externe Prüfungsrunde (3 Reviews) auf die Runde-2-Fassung eingearbeitet. Zwei Reviews bestätigten unabhängig voneinander alle Runde-2-Korrekturen als fachlich korrekt umgesetzt (insbesondere QoS-vs.-Safety als 'einer der stärksten Teile des Dokuments' bewertet) und identifizierten nur noch kleinere Präzisierungen: TLS-Absatz präzisiert – Zertifikatsprüfung schützt vor MITM nur bei korrekter Konfiguration, nicht automatisch; QoS-1-Beschreibung von 'Zustellung garantiert' auf 'wird bestätigt und ggf. erneut übertragen, wodurch mindestens einmal zugestellt wird' präzisiert (konsistent zur QoS-2-Formulierung); 'De-facto-Standard' bei MQTT auf 'weit verbreitetes, leichtgewichtiges Protokoll' abgeschwächt (Haupttext + Cheatsheet), da diese Einordnung angesichts der erwähnten Alternativen (CoAP) zu stark war; IoT-Dreieck-Grafik durch Tabelle ersetzt (bessere Lesbarkeit, Rückmeldung 'ASCII schwer lesbar') plus expliziten Hinweis ergänzt, dass die Darstellung qualitativ und keine exakte Klassifikation ist; BLE-Batterielaufzeit von 'Tage bis Monate' auf 'Tage bis mehrere Jahre, abhängig von Sendeintervall/Datenmenge/Betriebsart' erweitert; 'extreme Reichweite' (Marketing-Sprache) an allen drei Fundstellen (3.3, Prüfungsfalle 4, Selbsttest Q4) auf 'große Reichweite' vereinheitlicht; PROFIBUS/PROFINET als zwei unterschiedliche, verwandte Standards statt einer gemeinsamen Zeile ohne Differenzierung klargestellt; Prüfungstaktik-Zeile zu IoT/CPS von 'Rückkopplungsschleife' auf die in Runde 2 bereits korrigierte Formulierung ('Vernetzung vs. enge Kopplung') nachgezogen – war in Runde 2 nicht konsistent mitgeändert worden, von zwei Reviews unabhängig gefunden; Selbsttest Q6 'zwingend benötigt' auf 'typischerweise erforderlich' entschärft; Architekturdiagramm um Klarstellung ergänzt, dass der zweifach gezeichnete Broker dieselbe Instanz ist (Uplink/Downlink), keine zwei getrennten Broker. NICHT ÜBERNOMMEN (mit Begründung): (1) Umbenennung von 'Typ A – Kompakter Prüfungs-Wiki' zu 'Typ A – Prüfungs-Wiki' – abgelehnt, da 'Typ A – Kompakter Prüfungs-Wiki' die feste, im Wiki-FIAE-Skill definierte Kategoriebezeichnung ist (nicht frei wählbar für einzelne Artikel) und andere Typ-A-Artikel (z. B. LF8.2, LF4.2A/B) dieselbe Bezeichnung trotz vergleichbaren Umfangs führen. (2) Sichtbarer Quellenabschnitt im Artikeltext – abgelehnt, da Workflow-Wiki-FIAE.mkd Schritt 2 Quellenangaben ausdrücklich im YAML (`quellen_fachlich`) vorsieht, nicht im Fließtext, und alle bisherigen finalen LF-Artikel (LF2.2, LF4.2A/B, LF6.3, LF8.2, LF8.6) diesem Muster ohne inline-Quellenabschnitt folgen – Konsistenz mit etabliertem Korpus hat hier Vorrang vor einer Einzelmeinung. (3) YAML-Review-Historie kürzen/als Liste strukturieren – abgelehnt, da alle bisherigen finalen Artikel eine ebenso ausführliche, prosaische Review-Historie je Runde führen; Kürzung würde von der etablierten Dokumentationskonvention des Projekts abweichen. Erneut gemeldete Fragment-/Klebestellen (Review B, z. B. abgeschnittene Wörter, verklebte Trennlinien) beim gezielten Abgleich (grep nach den genannten Textstellen, Byte-genaue Prüfung der Zeilenumbrüche um Selbsttest/Cheatsheet/Deep-Dive-Abschnitt) erneut nicht bestätigt – der Reviewer selbst vermutete bereits Auszugsartefakte statt echter Dateidefekte, was sich damit bestätigt. Nach dieser Runde keine offenen fachlichen Befunde mehr aus allen drei Reviews."
  - runde: "3 (eigener Abschluss-Selbstcheck)"
    datum: 2026-09-11
    ergebnis: "Vollständige Datei zeilenweise erneut gelesen (nicht nur Diffs). Dabei drei zuvor übersehene Inkonsistenzen gefunden und behoben, die bei der Einarbeitung der Runde-3-Reviews nicht mitgezogen wurden: (1) Abschnitt 3.5-Typfrage verwendete noch 'LoRaWAN mit seiner extremen Reichweite' – vierte, zuvor übersehene Fundstelle der in Runde 3 eigentlich vollständig geglaubten 'extreme Reichweite'-Bereinigung, jetzt auf 'große Reichweite' korrigiert. (2) Abschnitt 3.6-Tabelle beschrieb NB-IoT-Abdeckung noch unqualifiziert als 'bestehende, flächendeckende Mobilfunk-Infrastruktur', obwohl die zugehörige Typfrage direkt darunter bereits die vorsichtigere, netzausbau-abhängige Formulierung nutzt – Tabellenzeile entsprechend angeglichen. (3) Selbsttest Q5 nutzte noch die alte, weniger präzise QoS-1-Formulierung ('Zustellung wird garantiert'), während die Haupttabelle in Abschnitt 4.2 in Runde 3 bereits auf die präzisere Formulierung ('wird bestätigt und ggf. erneut übertragen, wodurch mindestens einmal zugestellt wird') korrigiert worden war – Selbsttest-Antwort nachgezogen. Nach diesen drei Korrekturen erneute Konsistenzprüfung aller Kernaussagen (CPS-Definition, Sensor/Aktor, QoS/Safety, Zigbee-Rollen, Broker-SPOF, IoT-Dreieck-Sprache, 'große' statt 'extreme' Reichweite durchgängig) über Haupttext, Prüfungsfallen, Selbsttest, Cheatsheet, Merksätze und Prüfungstaktik – keine weiteren Inkonsistenzen gefunden. Abschnittsnummerierung (1.1–4.3) und Anchor-Links der IHK-Kernfragen-Tabelle gegen die tatsächlichen Überschriften geprüft, stimmen überein. Lehre für künftige Runden: Bei global wiederkehrenden Formulierungen (z. B. 'extrem', absolute Qualifizierer) künftig gezielt per Volltextsuche statt punktuell pro Fundstelle korrigieren, um genau solche Nachzügler zu vermeiden."
freigabe: "Freigegeben – Status auf Final gesetzt nach 3 Runden externer Prüfung (insgesamt 9 Reviews) + eigenem Abschluss-Selbstcheck (inkl. Korrektur von 3 im Selbstcheck selbst gefundenen Konsistenzresten), 2026-09-11. Hinweis: Die im Workflow vorgesehene ausdrückliche Auftraggeber-Freigabe vor der finalen Statussetzung wurde hier auf explizite Anweisung des Auftraggebers erteilt ('danach eine letzte Selbstcheck und wenn fehlerfrei auf Final setzen')."
```