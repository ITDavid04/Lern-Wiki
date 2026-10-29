# LF3.2 – Die Kommunikation begreifen (OSI-Modell, Transportprotokolle & Dienste)

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 100–120 Min., mit Vertiefung (3-Way-Handshake, Protokoll-Stack eines Webseitenaufrufs): 140–160 Min.
> **Status:** Final
> **Stand:** 2026-09-01

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Warum gilt ein Firmennetz über mehrere Stockwerke als LAN, die Standortkopplung zweier Büros in unterschiedlichen Städten aber als WAN? | [1.1](#11-netzwerk-dimensionen) |
| 2 | Was passiert bei der Kapselung, wenn Daten die 7 OSI-Schichten von oben nach unten durchlaufen? | [1.3](#13-das-osi-referenzmodell--kapselung) |
| 3 | Was unterscheidet TCP grundlegend von UDP, und woran erkennst du, welches Protokoll für einen Dienst sinnvoll ist? | [2.1](#21-tcp-vs-udp) |
| 4 | DHCP und DNS haben offensichtlich mit IP-Adressen zu tun – warum werden sie trotzdem Layer 7 zugeordnet? | [3.1](#31-protokolle-nach-osi-schichten) |
| 5 | Was leistet ARP, und warum wird es weder Layer 2 noch Layer 3 eindeutig zugeordnet? | [3.2](#32-arp--die-brücke-zwischen-layer-2-und-3) |

---

## 1. Grenzen und Schichten

> **Grundprinzip:** Bevor man Fehler systematisch eingrenzen kann, muss klar sein, wie weit ein Netzwerk räumlich reicht (Dimension) und aus welchen Schichten die Kommunikation selbst besteht (OSI-Modell). Beides zusammen ist die Landkarte für strukturiertes Troubleshooting.

### 1.1 Netzwerk-Dimensionen

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| PAN (Personal Area Network) | Verbindet Geräte in unmittelbarer Nähe einer einzelnen Person (z. B. Smartphone ↔ Kopfhörer) | 🟡 |
| LAN (Local Area Network) | Auf einen begrenzten räumlichen Bereich beschränkt, typischerweise ein Gebäude oder Rechenzentrum | 🔴 |
| MAN (Metropolitan Area Network) | Verbindet Nutzer innerhalb eines bestimmten geografischen Bereichs (z. B. einer Stadt) | 🟡 |
| WAN (Wide Area Network) | Verbindet verschiedene Standorte über große Distanzen hinweg | 🔴 |

> **IHK-Typfrage:** *Warum gilt ein Firmennetzwerk in einem 20-stöckigen Hochhaus als LAN, während die Verbindung zwischen zwei Büros in Berlin und München als WAN bezeichnet wird?*
> **Musterantwort:** Die Klassifikation richtet sich nach der räumlichen Ausdehnung, nicht nach der Anzahl der Geräte oder Stockwerke. Ein Hochhaus liegt trotz vieler Etagen an einem einzigen Standort – das Netzwerk bleibt "lokal" (LAN). Die Verbindung zwischen zwei Städten überbrückt dagegen eine große Distanz zwischen getrennten Standorten und benötigt in der Regel angemietete oder öffentliche Übertragungswege – damit handelt es sich um ein WAN.

🔴 **Stolperstein – WLAN ist kein WAN:** Ein häufiger Verwechslungsfehler ist "Wireless LAN" (WLAN) mit "Wide Area Network" (WAN) gleichzusetzen. WLAN ist trotz des Funks geografisch stark begrenzt und zählt zu den LAN-Technologien.

### 1.2 Standardisierungsgremien

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| ISO | Entwickelte das abstrakte OSI-Referenzmodell | 🟡 |
| IETF | Entwickelt die praktisch eingesetzten Internetstandards (TCP/IP) in RFC-Dokumenten | 🟡 |
| IEEE | Standardisiert u. a. Technologien der Bitübertragungs- und Sicherungsschicht, z. B. Ethernet nach IEEE 802.3 und WLAN nach IEEE 802.11 – nicht nur "physische" Hardware, auch Übertragungsverfahren | 🟡 |

🟢 **Nice to know:** Ohne diese weltweiten Normen könnten Geräte unterschiedlicher Hersteller nicht miteinander kommunizieren – das OSI-Modell selbst ist dabei eher ein didaktisches Referenzmodell, während IETF-Standards (TCP/IP) die tatsächlich im Internet verwendeten Protokolle definieren.

### 1.3 Das OSI-Referenzmodell & Kapselung

> **Grundprinzip:** Beim Durchlaufen des Protokollstapels ergänzt jede tatsächlich beteiligte Protokollinstanz die Daten meist um einen Header mit Steuerinformationen – auf der Sicherungsschicht kommt bei Ethernet zusätzlich ein Trailer (Prüfsumme/FCS) hinzu. Dieser Vorgang heißt Kapselung. Die Schichten 5 und 6 sind in modernen TCP/IP-Stacks häufig nicht als eigenständige Schichten sichtbar. Beim Empfänger läuft der Prozess umgekehrt ab (Entkapselung): Schicht für Schicht wird der jeweils zuständige Header bzw. Trailer verarbeitet und entfernt.

| Schicht | Deutsche Bezeichnung | Aufgabe | Typische Elemente | IHK-Relevanz |
|---|---|---|---|---|
| 7 – Application | Anwendungsschicht | Anwendungsdienste für den Nutzer | Browser, HTTP | 🔴 |
| 6 – Presentation | Darstellungsschicht | Datenformat, Verschlüsselung | Verschlüsselung/Formate; TLS wird im didaktischen OSI-Schema häufig hier eingeordnet | 🔴 |
| 5 – Session | Sitzungsschicht | Sitzungsauf- und -abbau | NetBIOS, RPC (in TCP/IP-Netzen oft nicht separat ausgeprägt) | 🟡 |
| 4 – Transport | Transportschicht | Ende-zu-Ende-Transport, Ports | TCP, UDP, Segmente | 🔴 |
| 3 – Network | Vermittlungsschicht | Logische Adressierung, Routing | IP-Adressen, Router, Pakete | 🔴 |
| 2 – Data Link | Sicherungsschicht | Adressierung im lokalen Netz | MAC-Adressen, Switches, Frames | 🔴 |
| 1 – Physical | Bitübertragungsschicht | Physische Signalübertragung | Kabel, Funk, Bits (0/1) | 🔴 |

🟡 **Praxis-Tipp – TLS ist keine feste Layer-6-Tatsache:** Die Zuordnung moderner Protokolle zu OSI-Schichten ist teilweise modellabhängig. In Prüfungsaufgaben wird TLS meist Layer 6 zugeordnet, in realen Protokollstacks wird es aber oft eher als Sicherheitsschicht oberhalb von TCP betrachtet (bei TLS 1.3 über QUIC läuft es sogar über UDP). Für die AP1 reicht die didaktische Einordnung auf Layer 6. Praktisch relevant ist heute nur noch TLS – SSL gilt als veraltet und unsicher und wird in aktuellen Systemen nicht mehr eingesetzt.

> **IHK-Typfrage:** *Beschreibe anhand einer Metapher, wie ein Datenpaket beim Senden von Schicht 7 bis Schicht 1 "wächst".*
> **Musterantwort:** Vergleichbar mit einer Matroschka-Puppe oder mehreren ineinander gesteckten Briefumschlägen: Die eigentlichen Nutzdaten entstehen auf Schicht 7 (z. B. eine HTTP-Anfrage). Jede darunterliegende Schicht verpackt diese Daten in einen eigenen Umschlag mit zusätzlichen Steuerinformationen – Schicht 4 fügt z. B. Portnummern hinzu, Schicht 3 IP-Adressen, Schicht 2 MAC-Adressen. Erst auf Schicht 1 werden die so mehrfach verpackten Daten tatsächlich als Bitfolge übertragen.

🟡 **Praxis-Tipp – Der Layer-Sprung:** Ein typischer Anfängerfehler beim Troubleshooting ist, direkt auf einer höheren Schicht zu suchen (z. B. vermeintliche IP-Konflikte auf Layer 3), obwohl die Ursache viel einfacher auf Layer 1 liegt (z. B. ein lockeres Patchkabel). Der Bottom-Up-Ansatz prüft deshalb konsequent von unten nach oben: Erst Layer 1 (Kabel/Link), dann Layer 2/3 (Adressierung), dann Layer 4 (Ports/Firewall), zuletzt Layer 7 (Anwendung).

🟢 **Nice to know – TCP/IP-Modell:** In der Praxis wird oft das schlankere 4-Schichten-TCP/IP-Modell (DoD-Modell) verwendet, das mehrere OSI-Schichten zusammenfasst (u. a. Session/Presentation/Application zu einer Anwendungsschicht). Für die IHK-Prüfung bleibt das 7-Schichten-OSI-Modell die Referenz, das TCP/IP-Modell ist ergänzendes Kontextwissen.

---

## 2. Transportprotokolle und Ports

> **Grundprinzip:** Auf Layer 4 wird entschieden, *wie* Daten transportiert werden. Die IP-Adresse (Layer 3) bringt ein Paket zum richtigen Rechner, der Port bestimmt, welches Programm auf diesem Rechner die Daten erhält.

### 2.1 TCP vs. UDP

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| TCP | Verbindungsorientiert, mit 3-Way-Handshake und Empfangsbestätigung – zuverlässig, aber mit mehr Overhead. Typisch für SMB, klassisches Webvideo/On-Demand-Streaming über HTTP | 🔴 |
| UDP | Verbindungslos, ohne Empfangsbestätigung – schnell, aber ohne Zustellungsgarantie. Typisch für DNS-Anfragen (kann aber auch TCP nutzen) und Echtzeitanwendungen wie Videotelefonie | 🔴 |
| Port | Zahl von 0–65535, adressiert innerhalb eines Rechners das konkrete Programm/den Dienst; die IP-Adresse führt zum Rechner, der Port zum Dienst darauf | 🔴 |

> **IHK-Typfrage:** *Bei einer Videotelefonie-Verbindung friert das Bild kurz ein, das Gespräch geht aber weiter. Beim Download einer großen Datei vom SMB-Server dauert es lange, ist danach aber fehlerfrei. Begründe, warum für die Videotelefonie UDP und für den Dateidownload TCP verwendet wird.*
> **Musterantwort:** Bei Echtzeitkommunikation wie Videotelefonie ist geringe Verzögerung wichtiger als Vollständigkeit – ein kurzzeitig verlorenes Bildpaket würde das Gespräch nur kurz stören, ein erneutes Anfordern würde dagegen mehr Verzögerung erzeugen als das Paket schlicht zu überspringen. UDP verzichtet deshalb bewusst auf Empfangsbestätigung und erneutes Senden, um Geschwindigkeit zu maximieren. Beim Dateidownload ist dagegen jedes einzelne Byte relevant – eine fehlerhafte oder unvollständige Datei ist unbrauchbar. TCP sorgt innerhalb einer bestehenden Verbindung für eine zuverlässige, geordnete und fehlerbereinigte Übertragung: Nicht bestätigte Daten werden erneut gesendet. Bricht die Verbindung dauerhaft ab, kann aber auch TCP die Zustellung nicht garantieren.

🟡 **Praxis-Tipp – Nicht "Video = UDP":** Klassisches On-Demand-Streaming (z. B. Mediatheken) läuft heute meist über HTTP und damit über TCP, da hier Vollständigkeit wichtiger ist als minimale Latenz. UDP wird eher bei echter Echtzeitkommunikation (Videotelefonie, manche interaktiven Streams) bevorzugt – moderne Varianten wie HTTP/3 nutzen zudem QUIC über UDP, auch für gewöhnliches Webvideo. Die Pauschale "Video = UDP" ist deshalb ein beliebter, aber unpräziser Merksatz.

🟡 **Praxis-Tipp – Port vs. IP-Verwechslung:** Lässt eine Firewall den Ping (ICMP, Layer 3) durch, ein Dateizugriff scheitert aber trotzdem, liegt das Problem meist auf Layer 4: Der konkrete Port des Dienstes (z. B. TCP/445 für SMB) ist blockiert, obwohl die grundsätzliche IP-Erreichbarkeit besteht.

🟢 **Nice to know – Der 3-Way-Handshake:** Bevor TCP Nutzdaten überträgt, bauen beide Seiten die Verbindung über drei Pakete auf: SYN (Verbindungswunsch), SYN-ACK (Bestätigung + Gegen-Verbindungswunsch), ACK (finale Bestätigung). Erst danach beginnt der eigentliche Datentransfer.

| Befehl | Zweck | IHK-Relevanz |
|---|---|---|
| `ss -tuln` (Linux) | Zeigt offene/lauschende TCP- und UDP-Ports an | 🔴 |
| `netstat -ano` (Windows) | Zeigt offene Verbindungen inkl. zugehöriger Prozess-ID | 🔴 |
| `ufw allow 445/tcp` (Linux) | Öffnet gezielt einen einzelnen Port in der Ubuntu-Firewall | 🟡 |

| Port-Bereich | Beschreibung | IHK-Relevanz |
|---|---|---|
| 0–1023 | Well-Known Ports – fest vergebene Standarddienste (z. B. 80/HTTP, 443/HTTPS, 22/SSH, 53/DNS) | 🔴 |
| 1024–49151 | Registered Ports – bei der IANA registrierte Dienste (z. B. 3306/MySQL) | 🟡 |
| 49152–65535 | Dynamic/Private Ports – werden von Clients typischerweise als Quellport verwendet | 🟡 |

🟡 **Praxis-Tipp – DHCP-Ports:** DHCP nutzt für IPv4 zwei feste UDP-Ports: UDP/67 auf Serverseite (lauscht auf Anfragen) und UDP/68 auf Clientseite. Portnummern sind dabei Konventionen, keine unveränderbaren Eigenschaften eines Dienstes – ein Server kann technisch auch auf einem anderen Port betrieben werden.

🔴 **Stolperstein – Offene Ports nach außen:** Wird ein interner Dienst wie SMB (Port 445) über Port-Forwarding eines Routers direkt ins öffentliche Internet (WAN) freigegeben, ist er unmittelbar für Angreifer weltweit erreichbar – SMB ist nicht für den direkten Betrieb im offenen Internet konzipiert und war in der Vergangenheit wiederholt Ziel schwerwiegender Sicherheitslücken (z. B. WannaCry). Solche Freigaben sollten nur über ein abgesichertes VPN erfolgen, nicht per direktem Port-Forwarding.

---

## 3. Protokolle und Dienste im OSI-Modell

> **Grundprinzip:** Jede OSI-Schicht bietet ihre Dienste über konkrete Protokolle (Regelwerke) an. Ein Kommunikationsvorgang nutzt dabei Protokolle verschiedener Ebenen, die sich teilweise überlagern (TLS oder QUIC lassen sich z. B. nicht eindeutig einer einzigen Schicht zuordnen). In vereinfachten Darstellungen – und in den meisten IHK-Zuordnungsaufgaben – wird dennoch häufig ein Protokoll pro OSI-Schicht angegeben.

### 3.1 Protokolle nach OSI-Schichten

| Schicht | Beispielprotokolle | IHK-Relevanz |
|---|---|---|
| 7 – Application | HTTP/HTTPS, FTP, SMTP/IMAP, DNS, DHCP, SSH | 🔴 |
| 6 – Presentation | TLS/SSL (z. B. für HTTPS) | 🔴 |
| 4 – Transport | TCP, UDP | 🔴 |
| 3 – Network | IPv4, IPv6, ICMP, IPsec | 🔴 |
| 2 – Data Link | Ethernet (802.3), WLAN (802.11), ARP, VLAN (802.1Q) | 🔴 |
| 1 – Physical | DSL, USB (nur die physische Übertragung), Bluetooth-PHY (Bluetooth insgesamt umfasst mehrere Schichten/Profile) | 🟡 |

> **IHK-Typfrage:** *DHCP vergibt IP-Adressen, DNS wandelt Namen in IP-Adressen um – warum werden beide trotzdem Layer 7 zugeordnet und nicht Layer 3?*
> **Musterantwort:** Die OSI-Schicht eines Protokolls richtet sich nicht danach, worüber es inhaltlich Auskunft gibt, sondern danach, welche Funktion es im Kommunikationsmodell erfüllt. DHCP und DNS sind aus dieser Sicht klassische Anwendungsdienste: Sie laufen als eigenständige Client-Server-Anwendungen und nutzen für ihre Anfragen und Antworten meist UDP, DNS bei Bedarf (z. B. große Antworten, Zonentransfers) aber auch TCP – das ändert nichts an der Layer-7-Einordnung, vergleichbar mit HTTP, das ebenfalls Layer 7 zugeordnet ist, obwohl es "nur" Webseiten überträgt.

🔴 **Stolperstein – Protokoll vs. Port:** Häufig liest man verkürzt "HTTP ist Port 80". Tatsächlich ist HTTP das Regelwerk auf Layer 7, Port 80 lediglich die *übliche* Tür beim TCP-Transport (Layer 4) – ein Webserver kann technisch genauso gut so konfiguriert werden, dass er HTTP auf Port 8080 oder einem beliebigen anderen Port anbietet.

### 3.2 ARP – Die Brücke zwischen Layer 2 und 3

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| ARP (Address Resolution Protocol) | Übersetzt eine bekannte IPv4-Adresse in die im lokalen Netz benötigte MAC-Adresse. Nur für IPv4 relevant – bei IPv6 übernimmt diese Aufgabe das Neighbor Discovery Protocol (NDP) | 🔴 |
| Einordnung | Wird oft als "Brücke" bzw. Layer-2.5-Protokoll zwischen Layer 2 und Layer 3 beschrieben, da es IP-Informationen nutzt, um eine Layer-2-Adresse zu ermitteln. Es führt selbst kein Routing durch | 🟡 |
| `arp -a` | Zeigt die lokale ARP-Tabelle (bekannte IP-MAC-Zuordnungen) an | 🟡 |

> **IHK-Typfrage:** *Erkläre in eigenen Worten, wie ARP eine bekannte IP-Adresse in die im LAN benötigte MAC-Adresse umwandelt.*
> **Musterantwort:** Möchte ein Gerät ein anderes im selben LAN erreichen, kennt es meist nur dessen IP-Adresse, nicht aber dessen MAC-Adresse – für den Versand des Frames auf Layer 2 wird die MAC-Adresse jedoch zwingend benötigt. Das Gerät sendet deshalb eine ARP-Anfrage als Broadcast ins LAN: "Wer hat diese IP-Adresse? Bitte melde deine MAC-Adresse." Das gesuchte Gerät antwortet direkt mit seiner MAC-Adresse, die der Anfragende anschließend (zeitlich begrenzt) in seiner lokalen ARP-Tabelle zwischenspeichert. Liegt das Ziel dagegen in einem anderen Netz, ermittelt das Gerät stattdessen per ARP die MAC-Adresse seines Default-Gateways, nicht die des entfernten Zielsystems – das eigentliche Routing übernimmt anschließend der Router.

### 3.3 ICMP und der Protokoll-Stack eines Webseitenaufrufs

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| ICMP | Wird u. a. von `ping` für Erreichbarkeitstests genutzt und liefert Fehler-/Statusmeldungen im Netzwerk. Arbeitet auf Layer 3 – ist selbst kein Transportprotokoll und besitzt keine TCP-/UDP-Portnummern | 🔴 |

| ICMP-Typ | Bedeutung | IHK-Relevanz |
|---|---|---|
| 8 | Echo Request – Ping-Anfrage | 🔴 |
| 0 | Echo Reply – Antwort auf einen Ping | 🔴 |
| 3 | Destination Unreachable – Ziel nicht erreichbar | 🔴 |
| 11 | Time Exceeded – TTL abgelaufen (u. a. Basis von `traceroute`) | 🟡 |

> **IHK-Typfrage:** *`ping` nutzt ICMP auf Schicht 3. Warum nutzt Ping kein TCP oder UDP auf Schicht 4?*
> **Musterantwort:** ICMP ist speziell für Diagnose- und Fehlermeldungen im Netzwerk konzipiert, nicht für den Transport von Anwendungsdaten. Für eine einfache Erreichbarkeitsprüfung wird weder eine gesicherte Verbindung (TCP) noch ein Port-Konzept für ein bestimmtes Programm (wie bei UDP) benötigt – ICMP arbeitet direkt auf Layer 3 und liefert primär Informationen wie Erreichbarkeit, Antwortzeit und Fehlerursachen (Echo Request/Reply für `ping`, "Destination Unreachable", "Time Exceeded").

🟢 **Nice to know – Protokoll-Stack beim Webseitenaufruf:** Ruft ein Nutzer `https://www.beispiel.de` auf, laufen (vereinfacht, für HTTP/1.1 oder HTTP/2) mehrere Schritte ineinander verschachtelt ab: DNS löst den Hostnamen in eine IP-Adresse auf → per ARP (IPv4) bzw. NDP (IPv6) wird die MAC-Adresse des nächsten Geräts (z. B. Default-Gateway) ermittelt → TCP-Verbindungsaufbau → TLS-Handshake → HTTP-Anfrage/Antwort → IP-Adressierung → Ethernet/WLAN-Übertragung. Bei HTTP/3 entfällt der klassische TCP-Handshake, da hier QUIC über UDP verwendet wird.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Wonach richtet sich, ob ein Netzwerk als LAN oder WAN gilt? | Nach der räumlichen Ausdehnung, nicht nach der Anzahl der Geräte oder Etagen |
| 2 | Welche Standardisierungsorganisation normiert Ethernet (802.3) und WLAN (802.11)? | IEEE |
| 3 | Was passiert bei der Kapselung? | Jede beteiligte Protokollinstanz ergänzt die Daten meist um einen Header (bei Ethernet zusätzlich einen Trailer) |
| 4 | Nutzt Videostreaming immer UDP? | Nein – klassisches On-Demand-Streaming läuft oft über HTTP/TCP, UDP wird eher bei Echtzeitkommunikation (z. B. Videotelefonie) bevorzugt |
| 5 | Auf welcher Schicht werden DHCP und DNS eingeordnet – und warum nicht auf Layer 3? | Layer 7, da beide eigenständige Anwendungsdienste sind, die UDP nur als Transport nutzen |
| 6 | Was bestimmt der Port bei einer Verbindung? | Welches Programm/welcher Dienst auf dem Zielrechner die Daten erhält |
| 7 | Was leistet ARP? | Übersetzt eine bekannte IP-Adresse in die zugehörige MAC-Adresse im LAN |
| 8 | Warum arbeitet `ping` mit ICMP statt mit TCP/UDP? | ICMP ist für Diagnose-/Fehlermeldungen konzipiert, nicht für Anwendungsdatentransport |
| 9 | Was ist der Unterschied zwischen "HTTP" und "Port 80"? | HTTP ist das Layer-7-Protokoll/Regelwerk, Port 80 nur die übliche Tür beim TCP-Transport |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| LAN / MAN / WAN | Klassifikation nach räumlicher Ausdehnung: lokal / städtisch / große Distanzen |
| OSI-Modell | 7-Schichten-Referenzmodell (Physical bis Application) für Netzwerkkommunikation |
| Kapselung | Jede beteiligte Protokollinstanz ergänzt die Daten meist um einen Header (Layer 2 bei Ethernet zusätzlich um einen Trailer) |
| Bottom-Up-Troubleshooting | Fehlersuche beginnt auf Layer 1 und arbeitet sich systematisch nach oben |
| TCP | Verbindungsorientiert, mit Handshake und Empfangsbestätigung – zuverlässig |
| UDP | Verbindungslos, ohne Bestätigung – schnell, aber ohne Zustellungsgarantie |
| Port | Adressiert innerhalb eines Rechners den konkreten Dienst (0–65535) |
| ARP | Übersetzt IP-Adressen in MAC-Adressen im lokalen Netz |
| ICMP | Diagnose-/Fehlermeldungsprotokoll auf Layer 3 (u. a. Basis von `ping`) |
| DHCP/DNS-Einordnung | Beide sind Layer-7-Anwendungsdienste, nutzen UDP nur als Transportmittel |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Dimension klassifizieren | "Ist das LAN, MAN oder WAN?" | "Zwei Standorte in unterschiedlichen Städten werden verbunden." | Klassifikation nach räumlicher Ausdehnung begründen, nicht raten |
| Schicht zuordnen | "Ordne Begriff X der richtigen OSI-Schicht zu" | "MAC-Adresse, TCP-Port 80, IP-Adresse zuordnen." | Sichere, schnelle Zuordnung ohne Zögern bei Layer 2/3/4 |
| Protokollwahl begründen | "Warum TCP/UDP für Dienst X?" | "Warum kann Videotelefonie UDP nutzen, ein Dateidownload aber TCP?" | Zusammenhang zwischen Anforderung (Echtzeit vs. Vollständigkeit) und Protokolleigenschaft erklären, nicht pauschal "Video = UDP" |
| Layer-Falle erkennen | "DHCP/DNS – welche Schicht?" | "Warum ist DNS nicht Layer 3, obwohl es mit IPs arbeitet?" | Unterscheidung zwischen Funktion des Protokolls und den Daten, mit denen es arbeitet |

---

## Merk-Sätze fürs Fachgespräch

> LAN, MAN und WAN unterscheiden sich nach räumlicher Ausdehnung – nicht nach Gerätezahl, Stockwerken oder Netzwerkgröße.

> Kapselung bedeutet: Jede beteiligte Protokollinstanz verpackt die Daten der darüberliegenden Schicht meist in einen eigenen Header – erst auf Layer 1 werden daraus tatsächlich übertragene Bits.

> TCP kauft Zuverlässigkeit mit Zeit, UDP kauft Geschwindigkeit mit Unsicherheit – welches Protokoll passt, hängt davon ab, ob Vollständigkeit oder Aktualität wichtiger ist.

> Ein Protokoll wird nach seiner Funktion im Kommunikationsmodell eingeordnet, nicht danach, worüber es inhaltlich Auskunft gibt – deshalb sind DHCP und DNS trotz IP-Bezug Layer-7-Dienste.

> ARP schlägt die Brücke zwischen bekannter IP-Adresse und der im LAN zwingend benötigten MAC-Adresse.

---

```yaml
lernfeld: LF3.2
titel: Die Kommunikation begreifen (OSI-Modell, Transportprotokolle & Dienste)
status: Final
stand: 2026-09-01
review: fachliche Praezisierungen auf Basis von Fachreview eingearbeitet (Kapselung, TLS-Einordnung, TCP/UDP-Streaming-Pauschale, DNS UDP/TCP, IEEE-Beschreibung, Bluetooth, ARP/NDP, ICMP-Typen, Port-Bereiche)
quellen:
  - LF3.2 Die Kommunikation begreifen
  - LF3.2.1- Grenzen und Schichten
  - LF3.2.2- Transportprotokolle und Ports (TCP vs. UDP)
  - LF3.2.3- Protokolle und Dienste im OSI-Modell
```