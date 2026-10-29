# LF3.4 – WLAN & VLAN (Funknetze und logische Segmentierung)

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 100–120 Min., mit Vertiefung (EIRP-Berechnung, 802.1Q-Detailaufbau, Client-Troubleshooting): 140–160 Min.
> **Status:** Final
> **Stand:** 2026-09-03

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Warum bricht 5-GHz-WLAN eine Wand weiter oft stärker ein als 2,4-GHz-WLAN, obwohl 5 GHz mehr Bandbreite bietet? | [1.1](#11-24-ghz-vs-5-ghz-reichweite-vs-bandbreite) |
| 2 | Was ist DFS, und warum kann ein Access Point das WLAN plötzlich für mehrere Minuten abschalten? | [1.2](#12-sendeleistung-eirp-und-regulatorik) |
| 3 | Warum ist der "WPA2/WPA3 Mixed Mode" ein beliebter, aber unsicherer Kompromiss? | [2.2](#22-verschlüsselung-von-wep-bis-wpa3) |
| 4 | Was unterscheidet einen Untagged- (Access-) von einem Tagged-Port (Trunk) nach 802.1Q fachlich? | [3.2](#32-access-vs-trunk--8021q) |
| 5 | Warum braucht die Kommunikation zwischen zwei VLANs zwingend einen Router, obwohl beide am selben Switch hängen? | [3.3](#33-vlan--subnetz-kopplung-und-inter-vlan-routing) |

---

## 1. Funkphysik, Regulatorik und Client-Diagnose

> **Grundprinzip:** WLAN überträgt Daten per Funkwelle statt per Kabel – das bringt physikalische Rahmenbedingungen (Dämpfung, geteiltes Medium) und gesetzliche Grenzen (Sendeleistung) mit sich, die es bei Kupfer/Glasfaser so nicht gibt.

### 1.1 2,4 GHz vs. 5 GHz: Reichweite vs. Bandbreite

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| 2,4 GHz | Längere Funkwellen, dringen vergleichsweise gut durch Wände (geringere Dämpfung), gleichzeitig störanfälliger; bei klassischer 20-MHz-Kanalplanung werden häufig nur die Kanäle 1, 6 und 11 überlappungsfrei genutzt (verbreitete Prüfungs-Vereinfachung – je nach Region und Kanalmaske sind auch andere Kombinationen möglich) | 🔴 |
| 5 GHz | Kürzere Funkwellen, werden von Wänden deutlich stärker gedämpft, bieten dafür wesentlich mehr nutzbare Kanäle und Bandbreite | 🔴 |

> **IHK-Typfrage:** *Ein Mitarbeiter hat im Konferenzraum perfekten 5-GHz-Empfang, eine Wand weiter im Flur bricht das Signal massiv ein. Wie erklärst du das physikalisch?*
> **Musterantwort:** Kurzwellige 5-GHz-Signale werden von Hindernissen wie Wänden deutlich stärker gedämpft (abgeschwächt bzw. teilweise absorbiert/reflektiert) als die längerwelligen 2,4-GHz-Signale. Direkt im Raum mit Sichtverbindung zum Access Point ist die Signalqualität deshalb sehr gut, nach der nächsten Wand nimmt die Signalstärke aber überproportional stark ab. Die höhere Bandbreite von 5 GHz liegt dabei nicht an der Wellenlänge selbst, sondern vor allem an mehr verfügbaren Kanälen, größeren möglichen Kanalbreiten und geringerer Belegung durch Nachbarnetze – das ist der klassische Kompromiss von 5 GHz: mehr Bandbreite und weniger Störungen, dafür spürbar geringere Reichweite durch Hindernisse als bei 2,4 GHz.

🟡 **Praxis-Tipp – Kanalwahl als Prüfungsvereinfachung:** Bei 20-MHz-Kanalbreite überlappen sich die 2,4-GHz-Kanäle so stark, dass in der klassischen Planung meist nur die Kanäle 1, 6 und 11 gleichzeitig überlappungsfrei genutzt werden – das ist eine verbreitete Merkregel, keine feste physikalische Grenze. Werden mehrere Access Points in Reichweite zueinander betrieben, sollten sie nach dieser Regel möglichst auf diese drei Kanäle verteilt werden, um gegenseitige Störungen (Interferenz) zu minimieren.

### 1.2 Sendeleistung, EIRP und Regulatorik

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| EIRP | Equivalent Isotropically Radiated Power – die tatsächlich effektiv abgestrahlte Sendeleistung, angegeben in Milliwatt (mW) oder logarithmisch in dBm; ergibt sich aus Sendeleistung des Geräts plus Antennengewinn (dBi) minus eventueller Kabel-/Steckerverluste zwischen Gerät und Antenne. Bei AP mit integrierter Antenne ist die vereinfachte Rechnung (Sendeleistung + Antennengewinn) meist ausreichend, bei externer Antenne müssen Leitungsverluste zusätzlich berücksichtigt werden | 🔴 |
| Zulässige Sendeleistung | In Deutschland/EU nach ETSI-Vorgaben aktuell für 2,4 GHz bei bis zu 100 mW (20 dBm) EIRP; für bestimmte 5-GHz-Kanalbereiche deutlich höher (bis zu 1000 mW/30 dBm), dort aber an Zusatzauflagen wie DFS gekoppelt – die genauen Grenzwerte hängen vom konkreten Kanalbereich und Land ab | 🔴 |
| DFS (Dynamic Frequency Selection) | Pflichtmechanismus für bestimmte höhere 5-GHz-Kanäle: Erkennt der Access Point ein Radarsignal (z. B. von Wetterstationen oder Flugsicherung), muss er den Kanal umgehend räumen | 🔴 |

> **IHK-Typfrage:** *Ein Access Point sendet mit 15 dBm, die Antenne hat einen Gewinn von +5 dBi. Liegt die resultierende EIRP innerhalb des in Deutschland für 2,4 GHz erlaubten Limits von 20 dBm (100 mW)?*
> **Musterantwort:** Bei einer Link-Budget-Berechnung wird der Sendeleistung in dBm der relative Antennengewinn in dBi hinzuaddiert und ein eventueller Leitungsverlust in dB abgezogen. Unter der Annahme, dass zwischen Sender und Antenne keine Kabel- oder Steckerverluste auftreten (z. B. bei integrierter Antenne), ergeben 15 dBm Sendeleistung plus 5 dBi Antennengewinn 20 dBm EIRP. Das entspricht 100 mW und damit exakt der in Deutschland für 2,4 GHz zulässigen Obergrenze – die Konfiguration ist damit gerade noch zulässig. Träten zusätzlich z. B. 2 dB Leitungsverluste auf (etwa bei externer Antenne mit Kabel), läge die tatsächliche EIRP nur bei 18 dBm und damit unterhalb der Grenze.

🔴 **Stolperstein – Der DFS-Schock:** Erkennt der AP auf einem DFS-pflichtigen 5-GHz-Kanal ein Radarsignal, muss er die Übertragung auf diesem Kanal einstellen und wechseln. Vor der Nutzung eines neuen DFS-Kanals kann zusätzlich ein Channel Availability Check nötig sein – typischerweise rund 60 Sekunden, in bestimmten radarrelevanten Frequenzbereichen auch bis zu 10 Minuten. Ein als radarbelastet erkannter Kanal darf zudem häufig für einen längeren Zeitraum (z. B. rund 30 Minuten) nicht erneut genutzt werden. Kann der AP direkt auf einen bereits geprüften oder nicht DFS-pflichtigen Kanal ausweichen, fällt die sichtbare Unterbrechung entsprechend kürzer aus. Ein vorbeifliegender Rettungshubschrauber ist dabei nur ein mögliches Beispiel für einen Auslöser, nicht die typische Regelursache. Nutzer erleben das als plötzlichen, scheinbar grundlosen WLAN-Ausfall – die Ursache liegt aber in der gesetzlich vorgeschriebenen Radarerkennung, nicht in einem Defekt.

🟡 **Praxis-Tipp – Asymmetrische Sendeleistung:** Ein Access Point kann – abhängig vom verwendeten Frequenzbereich und den dort geltenden regulatorischen Vorgaben – mit deutlich höherer EIRP senden als ein mobiles Endgerät (im 2,4-GHz-Band z. B. bis zu 100 mW, in bestimmten 5-GHz-Bereichen unter Zusatzauflagen wie DFS auch deutlich mehr). Ein Smartphone sendet mit seinem kleinen Akku dagegen oft nur mit wenigen Milliwatt zurück. Ergebnis: Der Client empfängt das AP-Signal augenscheinlich einwandfrei (volle Balken), Webseiten laden aber dennoch schlecht oder gar nicht – weil die Rückrichtung (Client → AP) die schwächere Verbindung ist.

### 1.3 Kollisionsvermeidung: CSMA/CA

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| CSMA/CA | Carrier Sense Multiple Access/Collision **Avoidance** – bevor ein Gerät sendet, hört es den Kanal ab und wartet bei Belegung eine zufällige Zeitspanne, um Kollisionen von vornherein zu vermeiden | 🔴 |

> **IHK-Typfrage:** *Zwei Smartphones wollen gleichzeitig über denselben Access Point Daten senden. Wie verhindert CSMA/CA, dass sich die Funksignale gegenseitig stören?*
> **Musterantwort:** Bevor ein Gerät sendet, prüft es zunächst, ob der Funkkanal gerade frei ist ("Carrier Sense"). Ist der Kanal belegt, wartet das Gerät eine zufällige Zeitspanne (Backoff) ab, bevor es den Kanal erneut prüft. Anders als beim kabelgebundenen Ethernet (CSMA/CD) kann ein WLAN-Gerät während des Sendens nicht gleichzeitig zuhören, ob eine Kollision auftritt – deshalb setzt WLAN konsequent auf Vermeidung statt auf nachträgliche Erkennung von Kollisionen.

### 1.4 Client-seitige Diagnose unter Linux

| Befehl | Zweck | IHK-Relevanz |
|---|---|---|
| `nmcli dev wifi list` | Zeigt sichtbare WLANs mit Signalstärke, Kanal und Datenrate | 🟡 |
| `nmcli dev wifi connect "SSID" password "..."` | Verbindet sich per Kommandozeile mit einem WLAN | 🟡 |
| `iw dev` / `iw dev wlan0 link` | Zeigt Details zur aktiven Verbindung, u. a. die BSSID (die MAC-Adresse des Funkmoduls des Access Points – zu unterscheiden von der SSID, dem sichtbaren Netzwerknamen; ein AP mit mehreren SSIDs hat für jede SSID i. d. R. eine eigene BSSID) und die Signalqualität – moderner Nachfolger des veralteten `iwconfig` (nutzt die aktuelle nl80211-Schnittstelle statt der veralteten Wireless Extensions) | 🟡 |
| `journalctl -u NetworkManager -f` | Live-Verfolgung der NetworkManager-Logs – zeigt Authentifizierung und DHCP-Ablauf in Echtzeit | 🟡 |
| `rfkill list` | Zeigt, ob ein Hardware- oder Software-Killswitch das WLAN blockiert | 🔴 |

🔴 **Stolperstein – Der Hardware-Killswitch:** Viele Laptops besitzen einen physischen Flugmodus-Schalter oder eine Tastenkombination. Ist dieser aktiv, zeigt `nmcli` unter Umständen gar keine Netzwerke an – bevor eine Treiber- oder Konfigurationsursache vermutet wird, lohnt sich immer zuerst der Blick auf `rfkill list`.

🟡 **Praxis-Tipp – Lautlose Zertifikatsfehler bei 802.1X:** Scheitert die Verbindung zu einem Enterprise-WLAN (802.1X) an einem abgelehnten RADIUS-Zertifikat, fragt die grafische Oberfläche oft einfach wiederholt nach dem Passwort, ohne den eigentlichen Grund zu nennen. Der tatsächliche Fehler findet sich meist nur im System-Log (`journalctl`), nicht in der GUI-Fehlermeldung.

🟢 **Nice to know – WLAN in der VM:** Startet man unter einem per WLAN verbundenen Linux-Host eine virtuelle Maschine, zeigt diese in der Regel kein eigenes WLAN-Menü, obwohl der Host online ist. Der Grund: Die VM erhält meist eine virtuelle Netzwerkkarte (vNIC), die sich wie eine gewöhnliche kabelgebundene Ethernet-Karte verhält – nicht wie ein echter WLAN-Adapter. Nur mit direktem PCI-Passthrough der physischen WLAN-Hardware an die VM würde diese eine eigene WLAN-Schnittstelle mit eigenem Menü sehen.

---

## 2. Access Points, WLAN-Standards und Sicherheit

> **Grundprinzip:** Auf der Sender-Seite (Access Point) werden die physikalischen Rahmenbedingungen aus Abschnitt 1 in konkrete Einstellungen übersetzt: welche Netze (SSID) auf welchem Band mit welcher Verschlüsselung angeboten werden.

### 2.1 SSID, Bänder und Kanalbreite

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| SSID | Name eines WLANs; ein Access Point kann mehrere SSIDs gleichzeitig ausstrahlen (z. B. "Firma-Intern" und "Firma-Gast") | 🔴 |
| Kanalbreite | Bestimmt die verfügbare Bandbreite eines Kanals (typisch 20/40/80/160 MHz) – mehr Breite bedeutet mehr Geschwindigkeit, aber auch mehr Anfälligkeit für Störungen und weniger gleichzeitig nutzbare, überlappungsfreie Kanäle | 🟡 |
| Auto-Kanal | Werksseitige Voreinstellung bei den meisten APs; in professionellen Umgebungen wird der Kanalplan häufig manuell festgelegt oder über eine zentrale Controller-Lösung dynamisch gesteuert, um Interferenzen zwischen benachbarten APs zu vermeiden | 🟡 |

🟡 **Praxis-Tipp – Funktion statt Knopfname suchen:** Jeder AP-Hersteller ordnet seine Weboberfläche anders an. Statt nach einem exakten Menüpunkt zu suchen, ist es zielführender, nach der gesuchten Funktion zu suchen (z. B. "Wireless", "WLAN" oder "Radio Settings") – die Begriffe unterscheiden sich zwischen Herstellern, die enthaltenen Funktionen sind meist ähnlich.

### 2.2 Verschlüsselung: von WEP bis WPA3

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| WEP | Historischer, heute als unsicher geltender Standard – gilt in der Praxis als gebrochen und sollte nicht mehr eingesetzt werden | 🔴 |
| WPA2-CCMP (AES) | Lange Zeit Standard, gilt bei korrekter Konfiguration (CCMP/AES statt des veralteten TKIP) weiterhin als grundsätzlich sicher, ist aber anfälliger für Offline-Wörterbuchangriffe auf schwache Passwörter als WPA3 | 🔴 |
| WPA3 (SAE) | Aktueller Standard, erschwert Offline-Wörterbuchangriffe auf das Passwort durch ein verändertes Schlüsselaushandlungsverfahren (SAE) deutlich gegenüber WPA2 | 🔴 |
| Personal (PSK) vs. Enterprise (802.1X) | Bei PSK teilen sich alle Nutzer ein gemeinsames Passwort; bei Enterprise/802.1X meldet sich jede Person mit individuellen Zugangsdaten über einen RADIUS-Server an | 🔴 |

> **IHK-Typfrage:** *Ein Administrator aktiviert im AP "WPA2/WPA3 Mixed Mode", damit ältere Geräte weiter funktionieren. Warum ist das ein Sicherheitskompromiss?*
> **Musterantwort:** Im Mixed Mode (Transition Mode) unterstützt das WLAN gleichzeitig WPA2-PSK und WPA3-SAE. Moderne Geräte können weiterhin WPA3 nutzen, ältere Clients bleiben dagegen über WPA2 verbunden. Die WPA2-spezifischen Risiken – insbesondere bei schwachen Passwörtern – verschwinden dadurch für diese Legacy-Verbindungen nicht vollständig, auch wenn ein Angreifer ohne Kenntnis des Passworts nicht einfach "beitreten" kann: Er kann aber weiterhin den WPA2-Handshake mitschneiden und offline gegen ein schwaches Passwort angreifen. Ein rein passiv aufgezeichneter SAE-Schlüsselaustausch (WPA3) ermöglicht diesen klassischen Offline-Wörterbuchangriff dagegen nicht in gleicher Form – WPA3 macht ein schwaches Passwort dadurch aber nicht automatisch sicher, aktive (Online-)Angriffsversuche bleiben grundsätzlich möglich. Der Mischbetrieb ist deshalb ein Kompromiss zwischen Abwärtskompatibilität und konsequenter WPA3-Sicherheit, kein automatischer Sicherheitsgewinn für das gesamte Netz.

🟡 **Praxis-Tipp – "WPA3 Only" hat eine Kehrseite:** Wird ein Netz konsequent auf "WPA3 Only" gestellt, werden ältere Geräte (z. B. alte Etikettendrucker oder Scanner ohne WPA3-Unterstützung) vollständig ausgesperrt. Vor einer solchen Umstellung sollte deshalb geprüft werden, welche vorhandene Hardware WPA3 tatsächlich unterstützt.

### 2.3 Hardware und Performance-Technologien

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Access Point vs. Repeater | Ein AP ist per Kabel an den Switch angebunden. Ein klassischer Single-Radio-Repeater muss dagegen auf demselben Funkkanal empfangen und die Daten anschließend erneut senden (nacheinander, nicht gleichzeitig) – dadurch sinkt die nutzbare Bandbreite für angeschlossene Clients häufig auf etwa die Hälfte. Systeme mit separatem Funk- oder Kabel-Backhaul (z. B. viele Mesh-Systeme) können diesen Effekt deutlich reduzieren | 🔴 |
| MU-MIMO | Multi-User Multiple Input Multiple Output – ein AP mit mehreren Antennen kann dank dieser Technik mehrere Clients weitgehend parallel statt strikt nacheinander bedienen; der tatsächliche Nutzen hängt zusätzlich von WLAN-Generation, Senderichtung, Clientanzahl und Funkbedingungen ab | 🟡 |
| Beamforming | Der AP bündelt die Funkwelle gezielt in Richtung eines bestimmten Clients, statt gleichmäßig in alle Richtungen zu senden | 🟡 |
| Wi-Fi 5 / Wi-Fi 6 | Marketingbezeichnungen für die technischen IEEE-Standards 802.11ac (Wi-Fi 5) bzw. 802.11ax (Wi-Fi 6) | 🔴 |

> **IHK-Typfrage:** *Der Geschäftsführer möchte für die neue Etage günstige Consumer-Repeater statt echter Access Points kaufen. Wie begründest du fachlich, warum das in einem Unternehmensnetz problematisch ist?*
> **Musterantwort:** Ein klassischer Single-Radio-Repeater muss dieselbe Funkverbindung nutzen, um Daten zu empfangen und anschließend erneut zu senden – die Ursache ist dabei keine technisch festgeschriebene Halbierung, sondern der zusätzliche Airtime-Verbrauch: Jedes Nutzdatenpaket belegt den Funkkanal doppelt, einmal beim Empfang vom Client bzw. AP und einmal beim erneuten Senden. Dadurch steht effektiv oft nur noch etwa die Hälfte der ursprünglichen Bandbreite für die angeschlossenen Clients zur Verfügung. Ein echter, per Kabel angebundener Access Point hat dieses Problem nicht, da Empfang (WLAN) und Anbindung ans restliche Netz (Kabel) über getrennte Medien laufen. In einem Unternehmen mit vielen gleichzeitigen Nutzern summiert sich der Bandbreitenverlust durch einfache Repeater deutlich stärker als im privaten Umfeld – Systeme mit separatem Funk- oder Kabel-Backhaul umgehen dieses Problem allerdings weitgehend, weshalb pauschal "Repeater" und "Halbierung" nicht in jedem Fall gleichzusetzen sind.

### 2.4 Gastnetz-Sicherheit: Captive Portal & Client Isolation

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Captive Portal | Leitet neue Nutzer eines (oft offenen) Gast-WLANs automatisch auf eine Webseite um, auf der Nutzungsbedingungen akzeptiert oder ein Zugangscode eingegeben werden muss | 🔴 |
| Client Isolation | Verhindert – abhängig von Hersteller und Implementierung – in erster Linie die direkte Kommunikation zwischen WLAN-Clients desselben Access Points bzw. derselben WLAN-Infrastruktur. Garantiert für sich allein aber weder Trennung vom internen Firmennetz noch von kabelgebundenen Geräten im selben VLAN | 🔴 |

> **IHK-Typfrage:** *Warum reicht ein Captive Portal allein nicht aus, um ein Gastnetz sicher zu machen?*
> **Musterantwort:** Ein Captive Portal regelt lediglich den Zugang zum Netz (Anmeldung/Zustimmung) und bietet für sich allein keine Netzwerkisolation. Ist das zugrunde liegende WLAN offen (ohne WPA2/WPA3), besitzt die Funkstrecke selbst keine WLAN-seitige Verschlüsselung – unverschlüsselte Anwendungsprotokolle können dann mitgelesen werden. HTTPS schützt zwar die übertragenen Inhalte auf Anwendungsebene, ersetzt aber weder eine verschlüsselte WLAN-Verbindung noch Netzwerksegmentierung und Client Isolation. Bei HTTPS-Aufrufen kann das Portal die ursprünglich angefragte Seite zudem technisch nicht transparent umleiten, weshalb Betriebssysteme Captive Portals meist über spezielle, dafür vorgesehene HTTP-Testanfragen im Hintergrund erkennen und dem Nutzer aktiv die Anmeldeseite anzeigen. Für ein wirklich sicheres Gastnetz braucht es deshalb mehrere zusammenwirkende Maßnahmen: Client Isolation erschwert die direkte Kommunikation zwischen WLAN-Clients, ein eigenes Gast-VLAN trennt das Gastnetz logisch vom Unternehmensnetz, und Firewall-Regeln legen fest, dass Gäste nur notwendige Dienste (DHCP, DNS, Internet) erreichen dürfen. Captive Portal, Client Isolation, VLAN und Firewall erfüllen also unterschiedliche Aufgaben und ersetzen sich nicht gegenseitig.

---

## 3. VLAN – Logische Segmentierung

> **Grundprinzip:** Ein VLAN teilt einen physischen Switch logisch in mehrere getrennte Netze auf – ohne dass dafür zusätzliche Kabel oder Switches nötig wären. Das begrenzt Broadcast-Verkehr und trennt Netzbereiche auch dort, wo alle Geräte am selben physischen Switch hängen.

### 3.1 Broadcast-Domänen und der Zweck von VLANs

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Broadcast-Domäne | Die Menge aller Geräte, die einen Broadcast eines beliebigen Mitglieds direkt empfangen – in einem "flachen" Layer-2-Netz ohne VLANs umfasst das alle miteinander verbundenen Switch-Ports, gegebenenfalls über mehrere Switches hinweg | 🔴 |
| VLAN | Virtual Local Area Network – unterteilt Switch-Ports logisch in mehrere kleinere Broadcast-Domänen, jede mit eigener VLAN-ID | 🔴 |

> **IHK-Typfrage:** *Warum ist es für Performance und Sicherheit kritisch, eine große Broadcast-Domäne mithilfe von VLANs zu unterteilen?*
> **Musterantwort:** In einer großen, ungeteilten Broadcast-Domäne erreicht jeder Broadcast (z. B. ARP-Anfragen, DHCP-Discover) grundsätzlich alle angeschlossenen Geräte, unabhängig davon, ob sie fachlich etwas miteinander zu tun haben – bei vielen Geräten erzeugt das unnötigen Broadcast-Verkehr und bremst das Netz spürbar aus. Sicherheitshalber ist es zudem unerwünscht, dass ein Gäste-Gerät denselben Broadcast-Verkehr sieht wie ein internes Firmen-Server: In einem VLAN-getrennten Netz erreicht der Broadcast eines Gastes ausschließlich andere Geräte im selben VLAN, nicht die davon logisch getrennten internen Netze.

### 3.2 Access vs. Trunk & 802.1Q

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Untagged Port (Access) | Hier hängt ein normales Endgerät (PC, Drucker), das selbst nichts von VLANs weiß. Der Switch ordnet eingehende, ungetaggte Ethernet-Frames anhand der Portkonfiguration (PVID) einem VLAN zu; ob intern tatsächlich ein vollständiges 802.1Q-Tag gespeichert wird, ist implementierungsabhängig – für ausgehende Frames an diesem Port wird ein eventuelles Tag jedenfalls wieder entfernt | 🔴 |
| Tagged Port (Trunk) | Für Verbindungen zwischen Switches oder zu VLAN-fähigen Access Points. Frames verlassen den Port inklusive VLAN-Tag, damit das Zielgerät die zugehörigen Netze weiterhin unterscheiden kann; ein Trunk kann daneben je nach Konfiguration zusätzlich ein ungetaggtes Native VLAN (PVID) führen | 🔴 |
| IEEE 802.1Q | Der Standard, der die VLAN-ID direkt in den Ethernet-Frame einfügt (Layer 2) – Herstellerbezeichnungen variieren: Cisco spricht von "Access"/"Trunk", andere Hersteller (z. B. TP-Link, HP) von "Untagged"/"Tagged" | 🔴 |

> **IHK-Typfrage:** *Was unterscheidet einen Untagged- von einem Tagged-Port fachlich, und welchen Typ konfigurierst du für den Port eines einfachen Abteilungsdruckers?*
> **Musterantwort:** Ein Untagged-Port (Access) ist für Endgeräte gedacht, die selbst kein VLAN-Tagging verstehen – der Switch übernimmt das Hinzufügen und Entfernen des VLAN-Tags intern, das Endgerät sieht davon nichts. Ein Tagged-Port (Trunk) überträgt dagegen Frames eines oder mehrerer VLANs mit 802.1Q-Tag über eine einzige physische Verbindung; typischerweise wird ein Trunk verwendet, um mehrere VLANs gleichzeitig zwischen zwei Switches oder zu einem VLAN-fähigen Access Point zu transportieren, zwingend ist das aber nicht – auch ein Port mit nur einem einzigen getaggten VLAN ist technisch ein Trunk. Ein einfacher Abteilungsdrucker versteht kein VLAN-Tagging und wird deshalb an einem Untagged-Port (Access) im entsprechenden VLAN angeschlossen.

🔴 **Stolperstein – Unterschiedliche Herstellerbegriffe:** Cisco verwendet die Begriffe "Access" und "Trunk", andere Hersteller wie TP-Link oder HP sprechen stattdessen von "Untagged" und "Tagged". Beide Begriffspaare beschreiben dasselbe Konzept – wer nur eine der beiden Terminologien kennt, sollte in der Prüfung beide zuordnen können.

🔴 **Stolperstein – Native VLAN auf VLAN 1:** Auf einem Trunk kann ein VLAN als Native VLAN bzw. ungetaggtes VLAN definiert sein – werksseitig häufig VLAN 1. Die PVID bestimmt dabei grundsätzlich, welchem VLAN ungetaggt eingehende Frames zugeordnet werden; je nach Hersteller werden Native VLAN, PVID sowie die getaggte/ungetaggte Portmitgliedschaft technisch etwas unterschiedlich dargestellt und konfiguriert, hängen im Ergebnis aber eng zusammen. Da VLAN 1 bei vielen Herstellern gleichzeitig als Default- und häufig auch als Management-VLAN dient, ist es aus Sicherheitssicht empfehlenswert, das Native VLAN bewusst auf eine andere, ungenutzte VLAN-ID zu legen. Wichtig dabei: Beide Seiten eines Trunks müssen hinsichtlich Native VLAN/PVID und erlaubter VLANs konsistent konfiguriert sein – unterschiedliche Einstellungen an beiden Enden sind eine reale Fehlerquelle und ein bekannter Ansatzpunkt für VLAN-Hopping-Angriffe.

### 3.3 VLAN + Subnetz-Kopplung und Inter-VLAN-Routing

🔴 **Stolperstein – VLAN ohne eigenes Subnetz:** VLANs trennen Geräte vollständig auf Layer 2 – das bleibt auch bei falscher IP-Planung bestehen. Problematisch wird es, wenn die IP-Konfiguration nicht zur Layer-2-Topologie passt: Erhalten Geräte in VLAN 10 und VLAN 20 IP-Adressen aus demselben IP-Subnetz, gehen die Hosts anhand ihrer Subnetzmaske von direkter Layer-2-Erreichbarkeit aus und senden entsprechende ARP-Anfragen – diese werden aber nicht über die VLAN-Grenze hinweg weitergeleitet, da die VLAN-Trennung ja gerade bestehen bleibt. Die Kommunikation funktioniert dann ohne Sonderlösung schlicht nicht. Die Zuordnung "1 VLAN = 1 IP-Subnetz" ist dabei keine physikalische Pflicht, sondern eine etablierte Designregel: Technisch könnten mehrere IP-Subnetze in einem VLAN existieren, ein einzelnes IP-Subnetz sollte im normalen Netzwerkdesign aber nicht über mehrere getrennte VLANs verteilt werden. In der Praxis wird deshalb normalerweise jedem VLAN ein eigenes IP-Subnetz zugeordnet (ein gemeinsamer DHCP-Server ist dabei kein Problem, sofern er per DHCP-Relay unterschiedliche Adressbereiche für die jeweiligen VLANs bereitstellt).

> **IHK-Typfrage:** *Ein Laptop in VLAN 10 soll einen Server in VLAN 20 anpingen. Warum reicht der Switch dafür nicht aus, obwohl beide Geräte am selben Gerät angeschlossen sind?*
> **Musterantwort:** Der Switch trennt VLANs bewusst auf Layer 2 – Geräte in unterschiedlichen VLANs gelten als unterschiedliche logische Netze, genau wie physisch getrennte Netze mit unterschiedlicher Subnetzmaske. Damit ein Paket von VLAN 10 zu VLAN 20 gelangt, muss es deshalb dieselbe Route nehmen wie jede andere Kommunikation zwischen zwei unterschiedlichen IP-Netzen: über einen Router (bzw. einen Layer-3-Switch mit Routing-Funktion), der beide VLAN-Subnetze kennt. Der Datenweg führt logisch vom Client über den Switch (VLAN 10) hoch zum Router und von dort zurück über den Switch (VLAN 20) zum Zielserver – auch wenn physisch alles über denselben Switch läuft.

🟡 **Praxis-Tipp – Das Management-VLAN kann dich aussperren:** Der administrative Zugriff auf einen Switch läuft bei vielen Herstellern werksseitig über VLAN 1. Wird die Portkonfiguration geändert und dabei versehentlich der Port umkonfiguriert, an dem der eigene Verwaltungsrechner hängt, kann man sich selbst vom Switch aussperren. Änderungen an der VLAN-Konfiguration sollten deshalb mit Bedacht und nach Möglichkeit mit einem physischen Rückfallweg zum Gerät geplant werden.

🟢 **Nice to know – Router-on-a-Stick:** Eine einfache Methode für Inter-VLAN-Routing ohne dedizierten Layer-3-Switch ist "Router-on-a-Stick": Ein einzelner Router-Port wird als Trunk an den Switch angeschlossen und intern in mehrere logische Subschnittstellen unterteilt – eine pro VLAN. Der Router routet dann zwischen diesen Subschnittstellen, obwohl physisch nur ein einziges Kabel zwischen Switch und Router liegt.

🟢 **Nice to know – Voice-VLAN:** Auf vielen modernen Schreibtischen steckt nur ein Netzwerkkabel, das zunächst in ein IP-Telefon geht; der PC steckt dahinter wiederum im Telefon. Damit Sprach- und Datenverkehr trotz gemeinsamer physischer Leitung getrennt bleiben, weist ein "Voice-VLAN" dem Telefon ein eigenes, getaggtes VLAN zu, während der PC dahinter weiterhin ungetaggt im normalen Daten-VLAN läuft – beide Datenströme laufen über dasselbe Kabel, bleiben aber durch 802.1Q logisch getrennt.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Warum hat 2,4 GHz mehr Reichweite durch Wände, aber weniger Bandbreite als 5 GHz? | Längere Funkwellen werden von Hindernissen schwächer gedämpft, bieten dafür aber weniger nutzbare Kanäle/Bandbreite |
| 2 | Wie viele überlappungsfreie 2,4-GHz-Kanäle werden in der klassischen 20-MHz-Planung meist genutzt? | 3 (Kanäle 1, 6, 11) – eine verbreitete Vereinfachung, keine feste physikalische Grenze |
| 3 | Was ist EIRP? | Die effektiv abgestrahlte Sendeleistung (Sendeleistung + Antennengewinn, abzüglich eventueller Kabelverluste) |
| 4 | Was macht DFS, und wann greift es? | Erkennt Radarsignale auf bestimmten 5-GHz-Kanälen und zwingt den AP, den Kanal zu räumen; die Ausfalldauer reicht von Sekunden bis mehreren Minuten |
| 5 | Wodurch unterscheidet sich CSMA/CA von CSMA/CD? | CSMA/CA vermeidet Kollisionen aktiv (Backoff vor dem Senden), da ein sendendes WLAN-Gerät währenddessen nicht gleichzeitig auf Kollisionen lauschen kann |
| 6 | Warum sinkt bei einem klassischen Single-Radio-Repeater die nutzbare Bandbreite oft auf die Hälfte? | Er muss über denselben Funkkanal nacheinander empfangen und erneut senden (Systeme mit separatem Backhaul sind davon weniger betroffen) |
| 7 | Warum ist "WPA2/WPA3 Mixed Mode" riskant? | Das Netz ist nur so sicher wie der schwächste akzeptierte Modus (WPA2), nicht wie WPA3 |
| 8 | Was unterscheidet Untagged- von Tagged-Ports? | Untagged (Access) für Endgeräte ohne VLAN-Wissen, Tagged (Trunk) transportiert mehrere VLANs über eine Verbindung |
| 9 | Warum braucht Inter-VLAN-Kommunikation einen Router? | VLANs trennen auf Layer 2; für die Kommunikation zwischen unterschiedlichen (Sub-)Netzen ist immer Layer-3-Routing nötig |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Dämpfung (WLAN) | 5 GHz wird von Wänden stärker geschwächt als 2,4 GHz, dafür mehr Bandbreite |
| EIRP | Effektiv abgestrahlte Sendeleistung = Sendeleistung + Antennengewinn − Kabelverluste |
| DFS | Pflicht-Radarerkennung auf bestimmten 5-GHz-Kanälen, erzwingt bei Erkennung Kanalwechsel (Dauer: Sekunden bis Minuten) |
| CSMA/CA | Kollisionsvermeidung durch Kanalabhören + zufälliges Warten vor dem Senden |
| WPA3 (SAE) | Aktueller WLAN-Verschlüsselungsstandard, erschwert Offline-Wörterbuchangriffe deutlich gegenüber WPA2 |
| Personal vs. Enterprise | Gemeinsames Passwort (PSK) vs. individuelle Anmeldung über RADIUS (802.1X) |
| Captive Portal | Zwangsweiterleitung neuer Gäste-WLAN-Nutzer auf eine Anmelde-/Zustimmungsseite – verschlüsselt die Funkstrecke selbst nicht |
| Single-Radio-Repeater | Halbiert oft die nutzbare Bandbreite, da er auf demselben Kanal nacheinander empfängt und sendet |
| VLAN | Logische Trennung von Switch-Ports in mehrere Broadcast-Domänen ohne zusätzliche Verkabelung |
| Untagged/Access vs. Tagged/Trunk | Endgeräteport ohne VLAN-Tag (PVID-Zuordnung) vs. Verbindung zwischen Switches/APs mit VLAN-Tag (802.1Q) |
| Native VLAN | Ungetaggtes VLAN auf einem Trunk-Port (oft werksseitig VLAN 1) – aus Sicherheitsgründen empfehlenswert zu ändern |
| 1 VLAN = 1 Subnetz | VLAN trennt vollständig auf Layer 2; ohne eigenes IP-Subnetz pro VLAN funktioniert die IP-Kommunikation trotzdem nicht sauber (ARP überschreitet keine VLAN-Grenze) |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Physikalisch begründen | "Warum bricht das Signal hier stärker ein?" | "5-GHz-Empfang bricht hinter der Wand ein." | Bezug auf Dämpfung und Frequenz/Wellenlänge, nicht nur "schlechter Empfang" |
| Sendeleistung berechnen | "Liegt die EIRP im erlaubten Rahmen?" | "15 dBm Sendeleistung + 5 dBi Antennengewinn." | dBm-Werte korrekt logarithmisch addieren, Ergebnis mit Grenzwert vergleichen |
| Sicherheitsrisiko einordnen | "Warum ist Konfiguration X unsicher?" | "WPA2/WPA3 Mixed Mode." | Schwächstes akzeptiertes Verfahren als tatsächliches Sicherheitsniveau erkennen |
| VLAN-Konzept anwenden | "Welcher Port-Typ für Gerät X?" | "Uplink zwischen zwei Switches vs. PC-Anschluss." | Tagged/Trunk für Switch-Switch- oder Switch-AP-Verbindungen, Untagged/Access für Endgeräte |
| Inter-VLAN-Kommunikation erklären | "Warum erreicht Gerät A Gerät B in VLAN X nicht?" | "Laptop in VLAN 10 pingt Server in VLAN 20 nicht an." | Layer-2-Trennung durch VLANs erkennen, Router/Layer-3-Instanz als Lösung nennen |

---

## Merk-Sätze fürs Fachgespräch

> 5 GHz bietet typischerweise mehr nutzbare Kanäle und größere Kanalbreiten und wird durch viele Hindernisse stärker gedämpft als 2,4 GHz – dadurch steht häufig mehr Bandbreite, aber eine geringere Reichweite durch Wände zur Verfügung.

> EIRP ist die Summe aus Sendeleistung und Antennengewinn, abzüglich eventueller Kabelverluste – nicht nur die reine Senderleistung des Geräts.

> DFS ist kein Fehler, sondern Gesetz: Der AP räumt den Kanal, weil er ein Radarsignal erkennt, nicht weil er kaputt ist.

> Mixed Mode ermöglicht WPA3 für moderne Clients, lässt aus Kompatibilitätsgründen aber weiterhin schwächer geschützte WPA2-Verbindungen zu – ein Kompromiss, kein automatischer Sicherheitsgewinn.

> VLANs trennen vollständig auf Layer 2 – das Problem bei fehlendem eigenem Subnetz pro VLAN ist nicht die VLAN-Trennung selbst, sondern dass ARP-Anfragen diese Grenze nicht überschreiten und die IP-Kommunikation deshalb ohne Router zwischen den VLANs nicht funktioniert.

---

```yaml
lernfeld: LF3.4
titel: WLAN & VLAN (Funknetze und logische Segmentierung)
status: Final
stand: 2026-09-03
review: fachliche Praezisierungen in zwei Runden eingearbeitet (DFS-Ausfalldauer strukturiert, EIRP-Leitungsverluste inkl. Rechenbeispiel, 1000mW-Beispiel frequenzabhaengig eingeschraenkt, WPA2-CCMP/TKIP-Ausschluss, WPA3-SAE-Offline-Praezisierung, Repeater-Airtime-Begruendung, Client-Isolation nicht als absolute Trennung, Captive-Portal/VLAN/Firewall-Zusammenspiel, Tagged-Port ohne Multi-VLAN-Zwang, PVID/Native-VLAN-Trennung inkl. Trunk-Konsistenz, 1-VLAN-1-Subnetz als Designregel, BSSID/SSID-Klaerung, 5-GHz-Merksatz entschaerft); ergaenzt um PoE-Standards, VLAN-Kurzeinordnung, Layer-Typfrage
quellen:
  - LF3.4- WLAN & VLAN
  - LF3.4.1- WLAN-Praxis mit Linux & Windows
  - LF3.4.2- Access Point Konfiguration (Simulation)
  - LF3.4.3- Elektrik, Funkphysik und Regulatorik
  - LF3.4.4- WLAN-Komponenten, Standards und Sicherheit
  - LF3.4.5- VLAN-Grundlagen und Enterprise-Simulation
```