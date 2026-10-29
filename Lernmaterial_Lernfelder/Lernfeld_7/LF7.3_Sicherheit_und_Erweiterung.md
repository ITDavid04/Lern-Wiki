# LF7.3 – Sicherheit & Erweiterung

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen einzelner Inhalte können bereits in AP1 vorkommen. Für FISI bestehen insbesondere Anknüpfungspunkte zu AP2 (Konzeption/Administration von IT-Systemen, Netzwerke); für FIAE sind Sicherheits-, Schnittstellen- und Systemaspekte vor allem als technisches Transferwissen relevant, da die FIAE-AP2-Bereiche (Softwareprojekt, Softwareprodukt, Algorithmen, WiSo) IoT-Hardware nicht explizit als eigenen Prüfungsbereich vorsehen. Fachgesprächsbezug ist projektabhängig – insbesondere wenn IoT-/Embedded-/Security-Aspekte Teil der eigenen betrieblichen Projektarbeit sind.
> **Lernzeit:** Ca. 90–110 Minuten reines Lesen, +50–70 Minuten für Typfragen und Verdrahtungsskizzen
> **Status:** Final
> **Stand:** 2026-09-14
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Hinweis zur Abgrenzung:** Dieser Artikel baut auf LF7.1 (Architektur/MQTT) und LF7.2 (Edge Computing/Deep Sleep) auf und schließt die LF7-Reihe ab. Die im übergeordneten Projektrahmen genannte AIDA-Pitch-/Präsentationsaufgabe ist eine Kommunikations-, keine IT-Fachaufgabe und wird hier nicht behandelt.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was besagt die CIA-Triade, und warum reicht Verschlüsselung allein nicht für IoT-Sicherheit? | [→ 1. IoT-Sicherheit](#1-iot-sicherheit--verschlüsselung) |
| 2 | Wie funktioniert ein Hardware-Watchdog, und warum ist A/B-Partitioning für OTA-Updates wichtig? | [→ 2. Betriebssicherheit & OTA](#2-betriebssicherheit--ota-updates) |
| 3 | Was unterscheidet GPIO, I2C und SPI, und wann wählt man welche Schnittstelle? | [→ 3. Hardware-Schnittstellen](#3-lokale-hardware-schnittstellen-gpio-i2c-und-spi) |
| 4 | Wie hängen Verschlüsselung, Update-Sicherheit und Hardware-Anbindung im Gesamtbild eines robusten IoT-Systems zusammen? | [→ 4. Zusammenspiel](#4-zusammenspiel-der-konzepte-in-lf73) |

---

## 1. IoT-Sicherheit & Verschlüsselung

> **Grundprinzip:** Eine Bank kann den stärksten Tresor der Welt haben – wenn die Mitarbeitenden trotzdem alle dasselbe Passwort "1234" benutzen, ist der Tresor irrelevant. Die größte Schwachstelle vieler IoT-Systeme liegt nicht in kryptografischen Algorithmen, sondern in banalen organisatorischen Lücken davor.

### 1.1 Die CIA-Triade auf IoT übertragen

| Schutzziel | Bedeutung | IoT-Beispiel | IHK-Relevanz |
| --- | --- | --- | --- |
| **Confidentiality (Vertraulichkeit)** | Daten dürfen nicht mitgelesen werden | Verschlüsselung, z. B. als Bestandteil von TLS | 🔴 |
| **Integrity (Integrität)** | Daten dürfen auf dem Transportweg nicht unbemerkt manipuliert werden | Kryptografischer Integritätsschutz, z. B. ebenfalls als Bestandteil einer korrekt konfigurierten TLS-Verbindung, oder durch digitale Signaturen | 🔴 |
| **Availability (Verfügbarkeit)** | Das System muss erreichbar bleiben | Schutz vor Überlastungsangriffen (DDoS), redundante Anbindung | 🔴 |

> **Wichtig für die Prüfung:** Die CIA-Triade ist ein allgemeines Informationssicherheits-Grundmodell (nicht IoT-spezifisch entwickelt), lässt sich aber direkt auf IoT-Szenarien übertragen. **Reine Verschlüsselung ohne zusätzlichen Integritätsmechanismus** schützt nicht automatisch vor Manipulation – dafür braucht es kryptografische **MACs oder Signaturen** (einfache Prüfsummen reichen nicht, da sie nicht gegen gezielte Manipulation abgesichert sind). Ein modernes Sicherheitsprotokoll wie **TLS kombiniert jedoch Verschlüsselung mit Integritätsschutz und Authentisierung** in einem Verfahren (technisch z. B. über AEAD-Verschlüsselung) – die Trennung der beiden Schutzziele ist also konzeptionell wichtig, bedeutet aber nicht, dass man bei TLS zusätzlich einen komplett separaten Integritätsmechanismus ergänzen müsste. TLS schützt dabei nur die gesicherte Transportverbindung selbst – nicht automatisch Daten vor oder nach dieser Verbindung, kompromittierte Endgeräte oder die Verfügbarkeit des Gesamtsystems.

### 1.2 Vom Klartext zur verschlüsselten Verbindung

MQTT schreibt selbst keinen bestimmten Transport zwingend vor. Wird MQTT klassisch über eine ungesicherte TCP-Verbindung betrieben – häufig über **Port 1883** –, werden Nutzdaten und ggf. Zugangsdaten im Klartext übertragen. Ein Angreifer, der den Datenverkehr tatsächlich beobachten oder umleiten kann – etwa durch Kontrolle eines Netzwerkgeräts, einen gespiegelten Switch-Port, ein kompromittiertes Gateway oder einen erfolgreichen Man-in-the-Middle-Angriff (bloßes "gleiches WLAN" allein reicht in einem korrekt konfigurierten Netz dafür meist nicht aus) –, kann diese Daten etwa per Wireshark auslesen. **MQTT über TLS** (umgangssprachlich oft "MQTTS" genannt, üblicherweise **Port 8883**) verschlüsselt die Verbindung; ein korrekt geprüftes **Zertifikat** ermöglicht dem Client zusätzlich, die Identität des Brokers zu authentisieren – dafür müssen aber Zertifikatskette, Gültigkeitszeitraum und der erwartete Hostname tatsächlich geprüft werden, nicht nur ein Zertifikat vorhanden sein. Wird diese Prüfung übersprungen oder Fehler werden ignoriert, entfällt der Schutz vor Man-in-the-Middle-Angriffen trotz aktivierter Verschlüsselung. Im üblichen TLS-Betrieb wird dabei primär der **Server** vom Client authentisiert; eine kryptografische Authentisierung des Clients selbst erfolgt nur bei zusätzlich konfiguriertem Mutual TLS (mTLS) oder über einen separaten Mechanismus auf Anwendungsebene.

> **Wichtig für die Prüfung – Hardware-Grenzen:** Ein vollständiger TLS-Verbindungsaufbau (Handshake) kostet Rechenleistung und damit Energie – für sehr kleine, batteriebetriebene Sensoren mit Deep-Sleep-Zyklen (siehe LF7.2) kann ein TLS-Handshake **pro einzelner Nachricht** spürbar zulasten der Batterielaufzeit gehen. In der Praxis wird deshalb oft eine bestehende TLS-Verbindung über mehrere Nachrichten hinweg wiederverwendet oder eine Sitzungswiederaufnahme genutzt. In speziell entwickelten Protokollen für stark ressourcenbeschränkte Geräte können zusätzlich leichtgewichtige kryptografische Primitive eingesetzt werden (siehe Deep-Dive-Ausblick zu Lightweight Cryptography) – solche Algorithmen ersetzen aber kein vollständiges Sicherheitsprotokoll wie TLS: Schlüsselaustausch, Authentisierung, Replay-Schutz und Schlüsselverwaltung müssen weiterhin gelöst werden.

> **IHK-Typfrage:** *"Vergleichen Sie MQTT über eine ungesicherte Verbindung (Port 1883) mit MQTT über TLS (Port 8883) hinsichtlich des Schutzes vor Man-in-the-Middle-Angriffen."*
> **Musterantwort:** Über Port 1883 werden Nutzdaten und ggf. Zugangsdaten unverschlüsselt übertragen – ein Angreifer mit Zugriff auf den Übertragungsweg kann mitlesen und unter Umständen auch Nachrichten unbemerkt verändern oder einschleusen, ohne dass Sender oder Empfänger das bemerken. MQTT über TLS (Port 8883) verschlüsselt die Verbindung und ermöglicht zusätzlich die Prüfung des Server-Zertifikats durch den Client – dadurch kann der Client erkennen, ob er tatsächlich mit dem vorgesehenen Broker kommuniziert, statt unbemerkt mit einem zwischengeschalteten Angreifer. Voraussetzung dafür ist allerdings, dass Zertifikatskette, Gültigkeit und Hostname tatsächlich geprüft werden und diese Prüfung nicht bei Fehlern einfach übersprungen wird (siehe LF9.2, Abschnitt 4.3).

### 1.3 Ein besonders häufiges Risiko: organisatorisch, nicht kryptografisch

Ein besonders häufiges und folgenreiches IoT-Sicherheitsproblem sind unveränderte oder schwache Standard-Zugangsdaten statt gebrochener Kryptografie. Ein bekanntes Beispiel ist das **Mirai-Botnetz** (2016), das hunderttausende IoT-Geräte über werkseitig voreingestellte, nie geänderte Zugangsdaten kompromittierte.

> **Wichtig für die Prüfung – Zertifikats-Ablauf:** Zertifikate haben ein Ablaufdatum. Ein abgelaufenes Zertifikat ist sowohl ein **Sicherheits-** als auch ein **Betriebsproblem**: Der Kommunikationspartner kann nicht mehr regelkonform authentisiert werden, und ohne einen funktionierenden Erneuerungsmechanismus verweigert ein Sensor nach Ablauf dauerhaft den Dienst – das Gerät verliert dadurch seine Verfügbarkeit. Beide Aspekte müssen bei der Planung eines langlebigen IoT-Systems von Anfang an mitgedacht werden (siehe Deep-Dive-Ausblick zu Certificate Rotation).

> **IHK-Typfrage:** *"Warum kann eine fehlende Daten-Integrität bei einem Temperatursensor für einen industriellen Hochofen zu einem physischen Schaden führen?"*
> **Musterantwort:** Wird der übertragene Messwert auf dem Transportweg unbemerkt manipuliert (z. B. ein zu niedriger statt des tatsächlich zu hohen Wertes), reagiert die Steuerung nicht auf die reale physische Situation, sondern auf die verfälschte Information. Bleibt eine notwendige Abkühlung deshalb aus, weil das System fälschlich eine unkritische Temperatur "sieht", kann das zu Überhitzung, Materialschäden oder im schlimmsten Fall zu einer Gefährdung von Personen führen. Das zeigt, dass bei cyber-physischen Systemen eine Integritätsverletzung nicht nur ein IT-Problem ist, sondern sich direkt auf die physische Welt auswirken kann (siehe LF7.1, Abschnitt 1 zur CPS-Rückwirkung).

---

## 2. Betriebssicherheit & OTA-Updates

> **Grundprinzip:** Ein Totmannschalter in einer Lokomotive löst automatisch eine Bremsung aus, wenn der Lokführer über einen festgelegten Zeitraum kein Lebenszeichen mehr gibt – unabhängig davon, ob er eingeschlafen ist oder ein technisches Problem vorliegt. Ein Watchdog-Timer funktioniert nach genau diesem Prinzip für Software.

### 2.1 Der Hardware-Watchdog-Timer

Ein **Watchdog-Timer (WDT)** ist ein Hardware-Timer bzw. Peripheriebaustein im Microcontroller. Die laufende Software muss ihn regelmäßig zurücksetzen ("füttern"); bleibt dieses Zurücksetzen aus – etwa weil sich die Hauptschleife aufgehängt hat –, läuft der Timer ab und löst je nach Controller und Konfiguration typischerweise einen harten Hardware-Reset aus (bei manchen Architekturen zunächst auch eine andere definierte Fehlerreaktion).

> **Wichtig für die Prüfung:** Ein Watchdog schützt gezielt vor dem **dauerhaften Hängenbleiben** der Software, nicht vor jeder denkbaren Fehlerursache (z. B. keinen Schutz vor falscher Logik, die weiterhin "lebt", aber falsche Ergebnisse produziert). Wird der Watchdog fälschlich in einem von der eigentlichen Hauptschleife unabhängigen Hintergrundprozess gefüttert, verfehlt er zudem seinen Zweck vollständig – er würde dann auch bei einer abgestürzten Hauptschleife weiterhin "gefüttert" und löst keinen Reset aus. Ein automatischer Watchdog-Neustart kann zudem ein zugrunde liegendes Software-Problem verschleiern, wenn niemand die Reset-Häufigkeit auswertet: Das System scheint "wieder zu laufen", das eigentliche Problem bleibt aber unbehoben und tritt wieder auf – deshalb sollten Watchdog-Resets protokolliert und regelmäßig ausgewertet werden, statt sie als "hat sich von selbst gelöst" zu ignorieren.

### 2.2 Over-the-Air (OTA) Updates und A/B-Partitioning

**OTA-Updates** ermöglichen das Aufspielen neuer Firmware per WLAN/Mobilfunk, ohne das Gerät physisch per USB anzuschließen – bei hunderten im Feld verteilten Sensoren ist das oft die einzig praktikable Wartungsoption.

| Konzept | Funktionsweise | IHK-Relevanz |
| --- | --- | --- |
| **Ungeschütztes Update** | Neue Firmware überschreibt direkt die alte; kommt es während des Schreibvorgangs zu einem Stromausfall oder Fehler, kann die bisherige Firmware unbrauchbar werden und das Gerät nicht mehr booten ("bricking") | 🔴 |
| **A/B-Partitioning** | Der Speicher wird in zwei Partitionen geteilt: Das System läuft aus Partition A, während das Update in Partition B geladen wird. Vor dem Umschalten werden Integrität und Signatur geprüft, danach wird die neue Version testweise gebootet; bestätigt sie ihre Funktionsfähigkeit nicht innerhalb einer festgelegten Frist, fällt das System auf die weiterhin intakte Partition A zurück | 🔴 |

> **Wichtig für die Prüfung:** A/B-Partitioning reduziert das Bricking-Risiko deutlich, ist aber kein Allheilmittel – ein erfolgreicher Download allein reicht nicht: Erst wenn zusätzlich Integrität/Signatur geprüft, ein Teststart durchgeführt und dessen Erfolg bestätigt wurde (bei Ausbleiben dieser Bestätigung automatisches Rollback), ist die Absicherung vollständig – die konkrete Umsetzung dieser Schritte hängt von der jeweiligen Implementierung ab. Firmware sollte zudem **signiert** übertragen werden (siehe Deep-Dive-Ausblick), damit ein manipuliertes Update gar nicht erst installiert wird.

### 2.3 Fail-Safe-Strategien bei Verbindungsausfall

Ein robustes System definiert für jeden Aktor einen bewussten **Fail-Safe-Zustand** für den Fall, dass die Netzwerkverbindung längere Zeit ausfällt.

> **IHK-Typfrage:** *"Konstruieren Sie eine Fail-Safe-Logik für einen IoT-gesteuerten Rollladen bei einem plötzlichen Ausfall der lokalen Internetverbindung."*
> **Musterantwort:**
> ```text
> WENN keine Serververbindung seit > 10 Minuten
>   DANN wechsle in lokalen Fallback-Modus:
>        Rollladen bleibt in aktueller Position
>        (kein automatisches Schließen/Öffnen ohne Bestätigung)
>   UND protokolliere den Verbindungsverlust lokal
> SONST reguläre, serverseitig gesteuerte Automatik fortsetzen
> ```
> Ein Rollladen ist kein sicherheitskritischer Aktor wie ein Nothalt – trotzdem sollte er bei fehlender Serveranbindung nicht unkontrolliert nach zentral vorgegebenen Zeitplänen weiterlaufen, sondern in einen vorhersehbaren, dokumentierten Zustand übergehen: Ohne Serververbindung fehlen möglicherweise aktuelle Zeitpläne oder autorisierte Fernbefehle, weshalb keine neuen cloudbasierten Fahrbefehle mehr ausgeführt werden sollten. Lokale Bedienelemente und eine lokale Hinderniserkennung (die ohnehin unabhängig von der Internetverbindung arbeitet) bleiben davon unberührt aktiv. Welcher Zustand darüber hinaus als "sicher" gilt (bleiben, öffnen oder schließen), hängt vom konkreten Anwendungsfall ab (z. B. Einbruchschutz vs. Fluchtweg vs. Sturmwarnung) und muss explizit festgelegt werden – "Position halten" ist dabei kein automatischer Fail-Safe-Standardwert, sondern nur eine von mehreren möglichen, jeweils begründungsbedürftigen Entscheidungen.

> **IHK-Typfrage:** *"Vergleichen Sie den Wartungsaufwand eines 100-Geräte-Sensornetzwerks mit und ohne OTA-Fähigkeit über einen Zeitraum von 5 Jahren."*
> **Musterantwort:** Ohne OTA-Fähigkeit erfordert jedes Firmware-Update einen physischen Vor-Ort-Einsatz je Gerät – bei 100 verteilten Geräten und mehreren Updates über 5 Jahre (z. B. Sicherheitspatches) summiert sich das zu erheblichem Personal- und Reiseaufwand, besonders bei schwer zugänglichen Standorten. Mit OTA-Fähigkeit lassen sich Updates zentral und für viele Geräte gleichzeitig ausrollen, was den Wartungsaufwand drastisch reduziert – dafür entstehen höhere Anforderungen an die Update-Infrastruktur selbst (Signierung, Rollout-Steuerung, A/B-Absicherung) und ein Restrisiko durch das Update Ausfälle zu verursachen, falls die Update-Logik selbst fehlerhaft ist.

---

## 3. Lokale Hardware-Schnittstellen: GPIO, I2C und SPI

> **Grundprinzip:** Ein einzelner Lichtschalter (GPIO) kann nur "an" oder "aus". Ein gemeinsamer Hausflur-Lautsprecher, über den mehrere Wohnungen per eigener Wohnungsnummer angesprochen werden (I2C), teilt sich eine Leitung für viele Teilnehmer. Ein Postverteiler mit einem eigenen Fach pro Empfänger, aber gemeinsamer Sortiermaschine (SPI), braucht für jeden Teilnehmer eine eigene Auswahlleitung, überträgt dafür aber deutlich schneller.

### 3.1 GPIO und ADC: Die einfachste Ebene

**GPIO (General Purpose Input/Output)** sind einzelne, programmierbare Pins am Microcontroller, die digital HIGH (z. B. 3,3 V) oder LOW (0 V) sein können – geeignet zum Schalten einfacher Aktoren (LED, Relais) oder zum Auslesen einfacher digitaler Zustände. Komplexere Übertragungen wären zwar grundsätzlich auch durch softwaregesteuertes Umschalten mehrerer GPIOs realisierbar, dafür nutzt man in der Praxis aber spezialisierte Hardware-Schnittstellen wie I2C oder SPI. Ein **ADC (Analog-to-Digital Converter)** erlaubt zusätzlich das Einlesen stufenloser analoger Spannungen (z. B. von einem Potentiometer oder Lichtsensor) und deren Umwandlung in digitale Zahlenwerte.

> **Verdrahtungshinweis:** SDA und SCL bei I2C benötigen **Pull-up-Widerstände**. Viele Sensormodule bringen diese bereits mit – werden mehrere solcher Module parallel an denselben Bus gehängt, kann der resultierende Gesamtwiderstand zu klein werden, was ebenfalls zu Übertragungsfehlern führen kann.

### 3.2 I2C und SPI im Vergleich

| Merkmal | I2C (Inter-Integrated Circuit) | SPI (Serial Peripheral Interface) | IHK-Relevanz |
| --- | --- | --- | --- |
| **Benötigte Leitungen** | 2 Signalleitungen (SDA für Daten, SCL für Takt) | Bei einem Gerät typischerweise 4 (MISO, MOSI, SCK, CS); jedes weitere Gerät benötigt meist eine zusätzliche eigene CS-Leitung (3 + n Leitungen bei n Geräten) | 🔴 |
| **Topologie** | Gemeinsamer Bus – mehrere Geräte teilen sich SDA/SCL | Gemeinsame Daten-/Taktleitungen, zusätzlich meist eine eigene Chip-Select-Leitung (CS) pro Gerät vom Master | 🔴 |
| **Geräte-Identifikation** | I2C-Adresse (z. B. `0x3C`) – je nach Baustein fest vorgegeben oder über Adresspins konfigurierbar | Über die individuelle CS-Leitung, keine Adresse im Protokoll nötig | 🔴 |
| **Geschwindigkeit** | Eher langsamer | Deutlich höher | 🔴 |
| **Typischer Einsatz** | Langsamere Sensoren (Temperatur, Luftdruck, kleine OLED-Displays) | Hohe Geschwindigkeit nötig (SD-Karten, Kameras, große Farbdisplays) | 🔴 |

> **Wichtig für die Prüfung – Adresskonflikte:** Zwei baugleiche I2C-Sensoren mit identischer, aktuell eingestellter Adresse (z. B. beide `0x27`) können nicht gleichzeitig am selben Bus betrieben werden – der Microcontroller kann nicht unterscheiden, welcher Sensor gerade antwortet. Lösungen sind ein Sensor-Modell mit einstellbarer Adresse (falls vom Hersteller vorgesehen), oder ein **I2C-Multiplexer**, der mehrere gleichartige Sensoren auf separate, nacheinander ansteuerbare Kanäle verteilt.

> **Wichtig für die Prüfung – Kabellängen:** I2C und SPI sind primär für kurze Verbindungen innerhalb eines Geräts bzw. einer Baugruppe vorgesehen – "wenige Zentimeter" ist dabei eine Faustregel für typische Aufbauten, keine feste technische Grenze. Welche Leitungslänge tatsächlich noch zuverlässig funktioniert, hängt u. a. von Taktfrequenz, Leitungskapazität, Pull-up-Dimensionierung (siehe Deep-Dive-Ausblick) und Störumgebung ab; für Verbindungen über mehrere Meter ist aber in der Regel eine dafür vorgesehene, robustere Schnittstelle die bessere Wahl.

> **IHK-Typfrage:** *"Ordnen Sie folgende Bauteile dem passenden Schnittstellentyp zu: eine einfache LED-Warnlampe, ein komplexer Umweltsensor (Temperatur/Feuchtigkeit/Druck), ein Farbdisplay mit hohem Datendurchsatz."*
> **Musterantwort:** Die **LED-Warnlampe** benötigt nur ein einfaches Ein/Aus-Signal ohne komplexe Datenstruktur – dafür reicht ein einzelner **GPIO**-Pin völlig aus. Der **Umweltsensor** liefert strukturierte Messdaten, ist aber nicht zeitkritisch und wird typischerweise mit anderen langsameren Sensoren am selben Bus betrieben – dafür eignet sich **I2C** mit seiner einfachen Zwei-Leitungs-Verkabelung. Das **Farbdisplay** muss dagegen größere Datenmengen mit hoher Geschwindigkeit übertragen – hier ist **SPI** mit seiner höheren Übertragungsrate die passende Wahl, auch wenn das eine eigene CS-Leitung erfordert. Für hochauflösende Kamera-Module gilt das nur eingeschränkt: Manche einfachere Module nutzen SPI, für hochauflösende Echtzeit-Bilddaten kommen aber häufig dedizierte, schnellere Kameraschnittstellen zum Einsatz – "hohe Datenmenge" allein ist also keine verlässliche Faustregel für "automatisch SPI".

---

## 4. Zusammenspiel der Konzepte in LF7.3

Ein robustes, erweiterbares cyber-physisches System kombiniert alle drei Bausteine dieses Artikels auf unterschiedlichen Ebenen: **Verschlüsselung** (Abschnitt 1) schützt die Kommunikation nach außen, **Watchdog und A/B-sicheres OTA** (Abschnitt 2) halten das System auch bei Software-Fehlern und Updates betriebsfähig, und **passend gewählte Hardware-Schnittstellen** (Abschnitt 3) ermöglichen die physische Erweiterung um neue Sensoren, ohne bestehende Komponenten zu gefährden. Diese drei Ebenen ergänzen die in LF7.1 (Netzwerk/MQTT) und LF7.2 (Energie/Payload) behandelten Konzepte zu einem vollständigen Bild eines produktionsreifen IoT-Systems: Ein System, das zwar verschlüsselt kommuniziert, aber bei einem fehlerhaften Update ausfallen kann oder bei einem Adresskonflikt zwischen zwei Sensoren falsche Daten liefert, ist trotz guter Verschlüsselung nicht betriebssicher.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Reine Verschlüsselung ohne zusätzlichen Mechanismus schützt automatisch auch vor Datenmanipulation | Vertraulichkeit und Integrität sind unterschiedliche Schutzziele der CIA-Triade – dafür braucht es kryptografische MACs/Signaturen. Ein Protokoll wie TLS kombiniert beides, das ist aber eine Eigenschaft des Protokolls, nicht der Verschlüsselung allein |
| 2 | Das größte IoT-Sicherheitsrisiko ist immer gebrochene Kryptografie | Ein besonders häufiges und folgenreiches Problem sind unveränderte Standard-Zugangsdaten statt gebrochener Kryptografie (bekanntes Beispiel: Mirai-Botnetz) |
| 3 | Ein Watchdog-Timer verhindert jede Art von Softwarefehler | Er schützt gezielt vor dem dauerhaften Hängenbleiben der Software – nicht vor falscher, aber weiterlaufender Logik |
| 4 | Ein OTA-Update ohne A/B-Partitioning ist genauso sicher wie eines mit | Ohne A/B-Absicherung kann ein Stromausfall während des Updates dazu führen, dass das Gerät nicht mehr bootfähig ist und meist nur vor Ort repariert werden kann |
| 5 | Ein automatischer Watchdog-Neustart bedeutet, dass das Problem behoben ist | Ein Neustart beseitigt nur das Symptom (Hängenbleiben) – die zugrunde liegende Ursache kann unentdeckt bleiben und erneut auftreten |
| 6 | I2C ist grundsätzlich die bessere Wahl, weil es weniger Leitungen braucht | Weniger Leitungen bedeuten geringere Geschwindigkeit – die Wahl hängt vom Anwendungsfall ab (Datenmenge, Geschwindigkeit, Anzahl Geräte), nicht von einer generellen Überlegenheit |
| 7 | Zwei baugleiche I2C-Sensoren lassen sich ohne Weiteres am selben Bus betreiben | Zwei Geräte mit identischer, aktuell eingestellter Adresse können nicht getrennt angesprochen werden – nötig sind ggf. per Pin einstellbare Adressen oder ein I2C-Multiplexer |
| 8 | I2C/SPI eignen sich für beliebige Kabellängen | Beide sind primär für kurze On-Board-Distanzen ausgelegt; über mehrere Meter drohen Signalstörungen durch Leitungskapazität |
| 9 | TLS schützt vollständig vor allen Sicherheitsrisiken | Eine korrekt konfigurierte TLS-Verbindung bietet Vertraulichkeit, Integrität und Authentisierung – aber nicht automatisch Schutz vor kompromittierten Endgeräten, Daten außerhalb der TLS-Verbindung oder Verfügbarkeitsangriffen |

---

## 6. Deep-Dive-Ausblick (freiwillig – für den ersten Durchgang nicht erforderlich)

- **Lightweight Cryptography (aktueller Stand)**: NIST hat im August 2025 mit **SP 800-232** einen finalen Standard für ressourcenschonende Kryptografie veröffentlicht (Ascon-Familie: u. a. Ascon-AEAD128 zur authentisierten Verschlüsselung, Ascon-Hash256) – vorgesehen für ressourcenbeschränkte Geräte wie IoT-Geräte, eingebettete Systeme und Low-Power-Sensoren.
- **Firmware-Signierung** (→ Abschnitt 2.2): Wie eine kryptografische Signatur verhindert, dass ein manipuliertes OTA-Update überhaupt installiert wird, selbst wenn ein Angreifer Zugriff auf den Übertragungsweg erhält.
- **Certificate Rotation** (→ Abschnitt 1.3): Strategien für den automatisierten Austausch ablaufender Zertifikate bei hunderten autarken, im Feld verteilten Geräten.
- **Canary Deployments** (→ Abschnitt 2.2): Wie Firmware-Updates zunächst nur auf einen kleinen Teil der Geräteflotte ausgerollt werden, um Fehler frühzeitig zu erkennen, bevor die gesamte Flotte betroffen ist.
- **Pull-Up-Widerstände und lange I2C-Leitungen** (→ Abschnitt 3.2): Wie parasitäre Leitungskapazität das Signal beeinträchtigt und welche Rolle Pull-Up-Widerstände als Gegenmaßnahme spielen.
- **Logic Level Converter** (→ Abschnitt 3): Warum ein 5-V-Sensor nicht ungeschützt an einen 3,3-V-Microcontroller angeschlossen werden sollte und wie ein Pegelwandler hier vermittelt.
- **Hardware-Redundanz bei kritischen Systemen** (→ Abschnitt 2): Architekturkonzepte für den Fall, dass bei lebenserhaltenden CPS-Systemen (z. B. medizinische Kühlung) der primäre Controller physisch ausfällt.
- **Überbrückung großer Entfernungen für SPI/I2C-Sensoren** (→ Abschnitt 3.2): Wie lokale Edge-Knoten (siehe LF7.2) einen weit entfernten Sensor an das Netzwerk anbinden können, statt den Bus selbst über die gesamte Distanz zu verlängern.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne die drei Schutzziele der CIA-Triade. | Confidentiality (Vertraulichkeit), Integrity (Integrität), Availability (Verfügbarkeit) |
| 2 | Warum reicht Verschlüsselung allein nicht als vollständiges IoT-Sicherheitskonzept? | Reine Verschlüsselung schützt primär die Vertraulichkeit; für Integrität braucht es zusätzlich MACs/Signaturen (TLS kombiniert beides). Zudem war historisch oft nicht gebrochene Kryptografie, sondern unveränderte Standard-Zugangsdaten die Ursache großer Vorfälle (z. B. Mirai-Botnetz) |
| 3 | Was macht ein Hardware-Watchdog-Timer, und was schützt er nicht? | Löst einen Hardware-Reset aus, wenn die Software ihn nicht regelmäßig zurücksetzt (Schutz vor Hängenbleiben) – schützt nicht vor fehlerhafter, aber weiterlaufender Logik |
| 4 | Warum reduziert A/B-Partitioning das Risiko eines "gebrickten" Geräts, und was braucht es dafür zusätzlich? | Das System läuft während des Updates weiter aus der unveränderten Partition; volle Absicherung erfordert zusätzlich Integritäts-/Signaturprüfung, Teststart und Bestätigung der neuen Version – bleibt die Bestätigung aus, fällt das System automatisch zurück |
| 5 | Was unterscheidet I2C und SPI bei der Anzahl benötigter Leitungen und der Geschwindigkeit? | I2C: 2 Leitungen, eher langsam; SPI: bei einem Gerät 4 Leitungen, jedes weitere Gerät benötigt eine zusätzliche CS-Leitung (3+n) – dafür deutlich schneller |
| 6 | Wie löst man einen Adresskonflikt zwischen zwei baugleichen I2C-Sensoren? | Über ein Sensor-Modell mit einstellbarer Adresse (falls verfügbar) oder einen I2C-Multiplexer |
| 7 | Warum eignet sich GPIO für eine einfache LED, aber nicht für ein Farbdisplay mit hohem Datendurchsatz? | GPIO überträgt nur einfache digitale Zustände; ein Display mit hohem Datendurchsatz benötigt eine schnellere Schnittstelle wie SPI |
| 8 | Was ist ein Fail-Safe-Zustand, und warum muss er explizit festgelegt werden? | Der Zustand, in den ein Aktor bei Verbindungsverlust übergeht (z. B. Position halten statt unkontrolliert weiterlaufen) – welcher Zustand "sicher" ist, hängt vom Anwendungsfall ab und ist nicht automatisch eindeutig |

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **CIA-Triade** | Confidentiality, Integrity, Availability – die drei klassischen Schutzziele der Informationssicherheit |
| **MQTT über TLS** | Port 1883 unverschlüsselt vs. Port 8883 über TLS verschlüsselt + Zertifikatsprüfung (umgangssprachlich oft "MQTTS" genannt, technisch kein eigenständiges Protokoll) |
| **Mirai-Botnetz** | Historisches Beispiel für Kompromittierung durch unveränderte Default-Passwörter, nicht durch Kryptografie-Bruch |
| **Watchdog-Timer (WDT)** | Hardware-Komponente, löst Reset aus, wenn Software ihn nicht regelmäßig zurücksetzt |
| **OTA-Update** | Firmware-Update per Funk, ohne physischen USB-Zugriff |
| **A/B-Partitioning** | Zwei Firmwarebereiche; neue Version wird getrennt von der laufenden installiert und kann bei fehlgeschlagenem Start/Health-Check durch die alte ersetzt werden – Integritäts-/Signaturprüfung sind zusätzliche, nicht automatisch enthaltene Sicherheitsmaßnahmen |
| **Bricking** | Gerät durch fehlgeschlagenes Update (ohne A/B-Absicherung) unbrauchbar geworden |
| **Fail-Safe-Zustand** | Definierter, sicherer Aktor-Zustand bei Verbindungsverlust |
| **GPIO** | Einzelner, digital schaltbarer Pin (HIGH/LOW) |
| **ADC** | Wandelt analoge Spannung in digitalen Zahlenwert um |
| **I2C** | 2-Leitungs-Bus (SDA/SCL), Bus-Topologie, Adresse je nach Baustein fest oder konfigurierbar, eher langsam |
| **SPI** | 4 Leitungen bei einem Gerät, +1 CS-Leitung je weiterem Gerät, hohe Geschwindigkeit |
| **I2C-Multiplexer** | Löst Adresskonflikte bei baugleichen I2C-Sensoren |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Schutzziel-Zuordnung | "Welches CIA-Schutzziel wird hier verletzt?" | Konkretes Schutzziel benennen und begründen, nicht nur "Sicherheitsproblem" pauschal |
| Fail-Safe-Logik konstruieren | "Entwerfen Sie eine Fail-Safe-Routine für Aktor X" | Konkreten Wenn-Dann-Ablauf mit begründetem Zielzustand, nicht nur "System soll sicher sein" |
| Schnittstellenwahl begründen | "Welche Schnittstelle würden Sie für Sensor X wählen?" | Begründung anhand Datenmenge/Geschwindigkeit/Verkabelungsaufwand, nicht pauschal "das modernste" |
| Update-Sicherheit bewerten | "Ist Update-Konzept X ausreichend abgesichert?" | Nach A/B-Partitioning und Firmware-Signierung fragen, "Bricking"-Risiko konkret benennen |

---

## 10. Merksätze für das Fachgespräch

> Der Tresor kann noch so stark sein – ein Default-Passwort macht ihn wertlos. Die größte IoT-Schwachstelle ist meist organisatorisch, nicht kryptografisch.

> Vertraulichkeit schützt vor Mitlesen, Integrität vor unbemerkter Manipulation – zwei zu unterscheidende Schutzziele, die ein Protokoll wie TLS aber gemeinsam umsetzen kann.

> Ein Watchdog beendet das Hängenbleiben, aber nicht die Ursache dahinter.

> A/B-Partitionen schaffen einen Rückweg – sicher werden OTA-Updates erst durch Signaturprüfung, Teststart, Bestätigung und Rollback zusammen, nicht durch die zweite Partition allein.

> I2C benötigt weniger Leitungen und ist typischerweise für langsamere bis mittlere Übertragungsraten mit mehreren Teilnehmern ausgelegt; SPI bietet typischerweise höhere Datenraten, benötigt dafür aber zusätzliche Chip-Select-Leitungen. Die Wahl folgt dem Anwendungsfall, nicht einer generellen Überlegenheit.

---

```yaml
dokument: LF7.3-wiki-artikel
lernfeld: LF7.3
titel: "Sicherheit & Erweiterung"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-14
quellen_intern:
  - "LF7.3.1: IoT-Sicherheit & Verschlüsselung.md"
  - "LF7.3.2: Betriebssicherheit & OTA-Updates.md"
  - "LF7.3.3: Lokale Hardware-Schnittstellen (I2C, SPI & GPIO).md"
  - "Bewusst NICHT behandelt: AIDA-Pitch-/Präsentationsaufgabe aus der LF7.3-Epic-Übersicht - Kommunikations-, keine IT-Fachaufgabe"
  - "Bewusste Querverweise zu LF7.1 (CPS-Rückwirkung, MQTT), LF7.2 (Deep Sleep/Energiebudget, Edge-Knoten), LF9.2 (Zertifikatsprüfung-Details) statt Wiederholung"
quellen_fachlich:
  - titel: "NIST SP 800-232 (Ascon-Based Lightweight Cryptography Standards)"
    herausgeber: "National Institute of Standards and Technology (csrc.nist.gov)"
    status: "web-verifiziert: final veröffentlicht am 13.08.2025, umfasst Ascon-AEAD128/Ascon-Hash256/Ascon-XOF128/Ascon-CXOF128; Rohmaterial sprach nur vage von 'wird erforscht' - im Deep-Dive durch konkreten, aktuellen Normstand ersetzt"
  - titel: "Mirai-Botnetz (2016), CIA-Triade, Watchdog-Timer, A/B-Partitioning, I2C/SPI/GPIO-Grundlagen"
    herausgeber: "Rohmaterial + etabliertes IT-Sicherheits-/Embedded-Standardwissen"
    status: "stabile, langjährig etablierte Konzepte und historische Fakten - keine weitere Web-Verifikation nötig"
review_historie:
  - runde: 1
    datum: 2026-09-14
    ergebnis: "Erstdraft erstellt aus den drei LF7.3.x-Rohdateien (kompakteres Wissens-Briefing-Format als LF7.1/7.2, daher stärkere eigene Ausformulierung nötig). Als ein zusammenhängender Artikel gemäß etabliertem LF7.1/7.2-Muster verfasst. NIST-Lightweight-Cryptography-Stand eigenständig web-verifiziert und aktualisiert (Rohmaterial vage, jetzt konkreter SP-800-232-Stand von August 2025). Von Anfang an gehedgte Formulierungen verwendet (keine 'immer'/'garantiert'/'grundsätzlich'-Absolutheiten), basierend auf den wiederholten Lektionen aus LF7.1- und LF7.2-Review-Historien. AIDA-Pitch-Aufgabe aus der Epic-Übersicht bewusst nicht behandelt (Kommunikations-, keine IT-Fachaufgabe) und im YAML dokumentiert. Noch OFFEN: externe Prüfungsrunde, finale Freigabe."
  - runde: 2
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (alle 3 Reviews unabhängig): Verschlüsselung/Integrität-Abgrenzung bei TLS missverständlich - TLS kombiniert via AEAD Vertraulichkeit+Integrität+Authentisierung, das wurde präzisiert (CIA-Tabelle, Wichtig-Block, Prüfungsfalle 1, neue Falle 9, Selbsttest 2, Merksatz), 'Prüfsummen' zu 'MACs/Signaturen' korrigiert. Zweitwichtigster Fund (2 von 3 Reviews): Kamera-Modul-zu-SPI-Zuordnung als Faustregel zu pauschal (hochauflösende Kameras nutzen oft dedizierte Schnittstellen wie MIPI CSI-2) - Typfrage auf Display umgestellt, Kamera-Sonderfall im Fließtext eingeordnet. Weitere Korrekturen: MQTT nicht mehr als 'standardmäßig Klartext' dargestellt, 'MQTTS' zu 'MQTT über TLS' präzisiert, Zertifikat-'beweist' abgeschwächt (Kette/Gültigkeit/Hostname-Prüfung nötig); SPI-Leitungszahl bei mehreren Geräten korrigiert (3+n statt pauschal 4); I2C-Adresse als 'fest oder konfigurierbar' statt pauschal 'fest' differenziert; Kabellängen-Aussage als Faustregel statt feste Grenze gekennzeichnet; A/B-Partitioning um Verifikation/Teststart/Bestätigungslogik ergänzt (ESP-IDF-Praxis); Mirai-Aussage von 'häufigste Ursache' zu 'bekanntes Beispiel' entschärft; Zertifikatsablauf als Sicherheits- UND Betriebsproblem statt künstlich getrennt; Rollladen-Beispiel-Begründung ersetzt (Hinderniserkennung läuft ohnehin lokal, nicht von Internetverbindung abhängig); Prüfungsrelevanz-Kopf fachrichtungsabhängig (FIAE/FISI) differenziert; GPIO/Watchdog-Aussagen leicht nuanciert; Pull-up-Hinweis in Haupttext gezogen statt nur Deep-Dive."
  - runde: 3
    datum: 2026-09-14
    ergebnis: "3 Reviews eingearbeitet. Wichtigster Fund (2 von 3 Reviews): A/B-Partitioning-Absolutheit entschärft - 'bleibt defekt' zu 'kann defekt werden' (andere Recovery-Mechanismen möglich), Cheatsheet/Merksatz klargestellt dass A/B selbst keine Signaturprüfung garantiert. SPI-Topologie 'Stern-ähnlich' zu 'gemeinsame Leitungen + individuelle CS' korrigiert (2 Reviews). Merksatz 'weniger Leitungen = weniger Tempo' als falsche Kausalität entschärft (1 Review, gut begründet). WLAN-Mitlese-Beispiel präzisiert (gleiches WLAN allein reicht meist nicht, echter Verkehrszugriff nötig). Lightweight Cryptography nicht mehr als TLS-Ersatz darstellbar formuliert. TLS-Client-Authentisierung als optional (mTLS) ergänzt. Kleinere Präzisierungen: Watchdog-Reset-Protokollierung als Praxisregel ergänzt, Überschrift 1.3 an bereits entschärften Fließtext angeglichen, NIST-Zielgruppenbeschreibung näher an Originalformulierung. Eine Review behauptete erneut verklebte Blockquotes und kaputte Tabelle - widerlegt."
  - runde: 4
    datum: 2026-09-14
    ergebnis: "Eigene Abschlussprüfung: Mehrere Stellen trugen noch alte, in Runde 2/3 bereits korrigierte Formulierungen - Selbsttest 4 (A/B ohne Verifikations-/Teststart-Nuance), Selbsttest 5 und Cheatsheet-SPI-Eintrag (ohne 3+n-Präzisierung), Cheatsheet-MQTT-Eintrag (noch 'MQTTS' als eigenständiges Protokoll), Adresskonflikt-Beispiel ('fest im Chip verdrahtet' widersprach der 'fest oder konfigurierbar'-Präzisierung), Zusammenspiel-Absatz ('dauerhaft ausfällt' zu absolut). Alle nachgezogen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-14) – Freigabe durch Autor:in bestätigt"
```