# LF9.1 – Netze planen und adressieren

> **Zielgruppe:** Umschüler FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Schwerpunkt AP2, schriftlicher Bereich "Analyse und Entwicklung von Netzwerken" (§ 22 FIAusbV, 90 Min., 10% Gewichtung); Netzwerkgrundlagen können auch in AP1 im Rahmen des Einrichtens eines IT-gestützten Arbeitsplatzes vorkommen, sowie als Grundlage für projektbezogene Fragen im Fachgespräch, falls Netzwerkthemen im Abschlussprojekt vorkommen.
> **Lernzeit:** Ca. 2–3 Stunden Lesen/Durcharbeiten, +2–3 Stunden Rechenübungen (Subnetting/VLSM/LPM), +1–2 Stunden Wiederholung mit Selbsttest – insgesamt deutlich mehr als bei den übrigen Artikeln dieser Reihe, da sehr rechenintensiv
> **Status:** Final
> **Stand:** 2026-09-12
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Hinweis zur Abgrenzung:** Allgemeine Anforderungsanalyse-Grundlagen (Lastenheft/Pflichtenheft, funktionale/nicht-funktionale Anforderungen, Kano-Modell) wurden bereits in LF5.1 behandelt – dieser Artikel wiederholt das nicht, sondern wendet es direkt auf Netzwerkplanung an.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie werden Kundenanforderungen in prüfbare Netzwerk-, Sicherheits- und Dienstanforderungen übersetzt? | [→ 1. Anforderungen](#1-netzwerk--und-dienstanforderungen) |
| 2 | Wie sind OSI- und TCP/IP-Modell aufgebaut, und wie verläuft ein Paketweg? | [→ 2. OSI/TCP-IP](#2-ositcp-ip-und-adressierung) |
| 3 | Wie berechnet man aus einem Hostbedarf ein Subnetz, und wie funktioniert VLSM? | [→ 3. Subnetting](#3-subnetting-und-adressplanung) |
| 4 | Wie funktionieren Switching, VLANs und WLAN-Planung? | [→ 4. Ethernet/VLAN/WLAN](#4-ethernet-switching-vlan-und-wlan) |
| 5 | Wie hängen Routing, NAT und Firewall-Regeln zusammen? | [→ 5. Routing/NAT/Firewall](#5-routing-nat-und-firewall-grundlagen) |

---

## 1. Netzwerk- und Dienstanforderungen

> **Grundprinzip:** "Das WLAN soll überall funktionieren" ist für eine Netzplanung so brauchbar wie "das Auto soll schnell sein" für einen Fahrzeugkauf – erst wenn Reichweite, Nutzerzahl, Gebäudeteil und Testmethode feststehen, wird daraus eine Anforderung, die man tatsächlich planen und abnehmen kann.

### 1.1 Von der Kundenaussage zur prüfbaren Anforderung

Eine gute Netzwerkanforderung enthält vier Bestandteile: **Gegenstand** (Dienst, Nutzergruppe, Standort), **messbare Bedingung** (Verfügbarkeit, Reichweite, Kapazität), **Randbedingungen** (Budget, Datenschutz, Wachstum) und **Prüfmethode mit Abnahmekriterium**.

| Vage Aussage | Prüfbare Anforderung |
| --- | --- |
| "Das Gäste-WLAN muss sicher sein" | "Aus dem Gäste-VLAN geht es nur ins Internet. Verbindungen in die internen privaten Netze (RFC 1918) sperrt die Firewall, ein Test aus dem Gästenetz zeigt, dass sie scheitern" |

> **Wichtig für die Prüfung:** Eine Liste mit Geräten ist noch kein Anforderungskatalog. Abnehmen lässt sich eine Anforderung erst, wenn klar ist, worum es geht, woran man Erfüllung misst und wie man das prüft. Netzwerkspezifisch kommt hinzu: Anforderungen an **verschiedene Netzzonen** (Produktion, Verwaltung, Gäste, DMZ) können sich widersprechen – eine "Produktion darf nie ausfallen"-Anforderung darf z. B. nicht vom Ausfall des Gast-WLANs beeinflusst werden.

### 1.2 Dienstematrix und Variantenvergleich

Eine **Dienstematrix** verknüpft Nutzergruppe, Dienst, Datenart, Verfügbarkeitsanforderung, erlaubten Zugriff und Abhängigkeiten – sie ist die Brücke zwischen Anforderungen und späterer VLAN-/Firewall-Planung (siehe Abschnitte 4–5).

Beim Variantenvergleich werden **einmalige Investitionen** (Hardware, Lizenzen, Installation) von **laufenden Betriebskosten** (Energie, Wartung, Support) getrennt und über einen Zeitraum zur **Total Cost of Ownership (TCO)** zusammengefasst.

> **IHK-Typfrage:** *"Ein Kunde sagt: 'Die Produktion darf nicht ausfallen.' Wie wird daraus eine prüfbare Netzwerkanforderung?"*
> **Musterantwort:** Statt sofort Technik zu kaufen, fragst du nach: Wie lange darf eine Störung dauern, welche Arbeitsschritte hängen am Netz, und gibt es einen Notbetrieb? Daraus wird zum Beispiel: "Fällt das Gäste-WLAN aus, läuft der Datenverkehr der Produktion unverändert weiter. Nachweis: Während das Gästenetz gestört ist, funktioniert ein Test aus der Produktion, und ein Zugriff aus dem Gästenetz auf die Produktion schlägt fehl." Das setzt voraus, dass Produktions- und Gastzone bereits netztechnisch getrennt sind (siehe Abschnitt 4, VLANs) – die Anforderung wirkt also direkt in die Netzarchitektur hinein.

---

## 2. OSI/TCP-IP und Adressierung

> **Grundprinzip:** Ein Brief braucht eine Postadresse (wohin?), einen Umschlag mit Absender/Empfänger auf dem lokalen Verteilzentrum (wie kommt er zur nächsten Station?) und einen Inhalt in verständlicher Sprache (was steht drin?). Genau diese Trennung von Zustellung, Transport und Inhalt bilden OSI- und TCP/IP-Modell für Netzwerkkommunikation ab.

### 2.1 Die Schichten als Diagnosewerkzeug

Das **OSI-Modell** mit 7 Schichten und das schlankere **TCP/IP-Modell** mit 4 Schichten beschreiben keinen Ablauf, den ein Paket nacheinander durchläuft. Sie sind Denkhilfen: Welche Schicht ist zuständig, und wo steckt der Fehler?

| OSI-Schicht | TCP/IP-Ebene | Beispiele | IHK-Relevanz |
| --- | --- | --- | --- |
| 7 Anwendung, 6 Darstellung, 5 Sitzung | **Anwendung** | DNS, HTTP, DHCP, LDAP, NTP, TLS | 🔴 |
| 4 Transport | **Transport** | TCP, UDP | 🔴 |
| 3 Vermittlung | **Internet/Vermittlung** | IPv4, IPv6, ICMP | 🔴 |
| 2 Sicherung | **Netzzugang** | Ethernet, VLAN, MAC | 🔴 |
| 1 Bitübertragung | **Netzzugang** | Kupfer, Glasfaser, Funk | 🟡 |

> **Wichtig für die Prüfung – Schichten für die Fehlerdiagnose nutzen:** Ein ausgefallener Link lenkt die Diagnose zunächst auf Schicht 1, eine falsche VLAN-Zuordnung auf Schicht 2, eine fehlerhafte IP-/Gatewaykonfiguration auf Schicht 3. Ist ein Host per IP erreichbar, ein bestimmter TCP-/UDP-Dienst aber nicht, müssen Transport-, Filter- und Dienstebene geprüft werden – ein nicht erreichbarer Port allein beweist noch keinen Fehler ausschließlich auf einer bestimmten Schicht. Scheitert nur die Namensauflösung, ist DNS als Anwendungsdienst zu untersuchen. Ein wesentlicher Unterschied zwischen den Modellen: Das TCP/IP-Modell fasst die drei oberen OSI-Schichten (Anwendung, Darstellung, Sitzung) in einer einzigen Anwendungsebene zusammen und die beiden unteren (Sicherung, Bitübertragung) in der Netzzugangsebene.

> **Wichtig für die Prüfung:** TCP bietet einen zuverlässigen, geordneten Bytestrom – das ist **nicht dasselbe wie sicher/verschlüsselt**. Vertraulichkeit und Identitätsprüfung kommen erst durch höhere Protokolle wie TLS hinzu. UDP arbeitet dagegen ohne Verbindungsaufbau und ohne eigene Zustellgarantie. Eine Portnummer allein beweist zudem keinen Dienst – Diagnose und Firewallplanung brauchen immer Protokoll, Richtung, Quelle, Ziel, Port und Verbindungszustand gemeinsam.

### 2.2 IPv4 und IPv6 im Vergleich

Bei **IPv4** (32 Bit) legt das Präfix fest, welcher Teil der Adresse das Netz und welcher den Host bezeichnet. Die privaten Bereiche aus **RFC 1918** werden im Internet nicht weitergeleitet: 10.0.0.0/8, 172.16.0.0/12 und 192.168.0.0/16.

**IPv6** (128 Bit) schreibt man als acht Blöcke in Hexadezimal. Führende Nullen in einem Block darf man weglassen, und genau einen Abschnitt aus lauter Null-Blöcken darf man durch `::` ersetzen. Typisches LAN-Präfix: **/64**. Link-Local-Adressen beginnen mit `fe80::/10` und gelten nur am lokalen Link.

| IPv6-Präfixbereich | Verwendung | IHK-Relevanz |
| --- | --- | --- |
| `2000::/3` | Global Unicast (öffentlich routbar) | 🔴 |
| `fe80::/10` | Link-Local (nur lokaler Link) | 🔴 |
| `ff00::/8` | Multicast | 🟡 |
| `::1` | Loopback | 🟢 |

Eine Organisation erhält vom Provider oder über eine eigene Registrierung ein **Standortpräfix** – häufig als Beispiel genannt wird /48, in der Praxis kommen aber auch andere Längen wie /56 vor. Daraus werden für die einzelnen LANs üblicherweise **/64-Subnetze** gebildet (bei einem /48-Standortpräfix stehen dafür 16 Bit als Subnetz-ID zur Verfügung). Die **Interface-ID** (bei /64 die letzten 64 Bit) identifiziert die konkrete Schnittstelle, oft automatisch generiert.

> **Wichtig für die Prüfung:** IPv6 ist **mehr als IPv4 mit langen Adressen**. Neighbor Discovery ersetzt ARP, Geräte konfigurieren sich selbst, und Multicast spielt eine viel größere Rolle. Bei **Dual Stack** laufen beide Protokolle nebeneinander, und für **jedes einzeln** musst du Adressen, Routing, Firewall-Regeln und Tests planen. IPv6 bewusst abzuschalten und das zu dokumentieren ist besser, als es unbeachtet im Hintergrund laufen zu lassen.

### 2.3 Paketweg und ARP/Neighbor Discovery

Liegt das Ziel **im eigenen Subnetz**, braucht ein IPv4-Client dessen MAC-Adresse. Liegt es **woanders**, braucht er die MAC-Adresse seines Standardgateways. Im IPv4-Netz fragt er per **ARP** mit einem Broadcast danach. IPv6 nutzt **Neighbor Discovery**, das über ICMPv6 läuft und **Multicast** statt Broadcast verwendet. Beide wirken nur innerhalb des lokalen Netzsegments.

> **IHK-Typfrage:** *"Beschreiben Sie den Paketweg eines Clients, der `portal.corp.example` (Ziel in der DMZ) aufruft."*
> **Musterantwort:** (1) Der Client schickt eine DNS-Anfrage nach dem A- bzw. AAAA-Eintrag und bekommt zum Beispiel 10.40.7.150 zurück. (2) Ein Vergleich mit dem eigenen Präfix zeigt: Das Ziel liegt in einem anderen Netz. Also holt der Client per ARP oder Neighbor Discovery die MAC-Adresse seines Standardgateways. (3) Das Gateway sucht in seiner Routingtabelle die genaueste Route in die DMZ, und die Firewall entscheidet anhand von Quelle, Ziel, Protokoll, Port und Verbindungszustand. (4) Ist der Weg frei, folgen TLS-Handshake, Prüfung des Zertifikats und schließlich die HTTP-Anfrage. Ein Ping bestätigt nur ein Stück dieses Weges, DNS, Port, TLS und Anwendung testet er nicht.

---

## 3. Subnetting und Adressplanung

> **Grundprinzip:** Ein Präfix ist wie die Anzahl reservierter Sitzplätze in einem Zugabteil – je mehr Plätze für "Netz" reserviert sind (längeres Präfix), desto weniger bleiben für "Gäste" (Hostadressen) übrig. /26 reserviert mehr Netzbits als /24 – deshalb ist ein /26 das **kleinere** Netz, nicht das größere.

### 3.1 Netz-, Host- und Broadcastadresse berechnen

Ein Präfix `/n` lässt `32-n` Bits für Hosts übrig, das Subnetz umfasst also `2^(32-n)` Adressen. Zwei davon fallen im klassischen IPv4-Subnetting weg: Netzadresse und Broadcastadresse bekommt **kein** Host.

| Präfix | Subnetzmaske | Blockgröße | Typisch nutzbar |
| --- | --- | --- | --- |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /30 | 255.255.255.252 | 4 | 2 |

**So rechnest du:** (1) Wie viele Hosts brauchst du, mit Reserve? (2) Welche Zweierpotenz passt gerade so? (3) Daraus folgt das Präfix (`32 - Hostbits`). (4) Wo beginnt und endet der Block? (5) Gateway, feste Adressen, DHCP-Pool und Reserve eintragen. (6) Überschneidet sich etwas, und ist Platz zum Wachsen?

> **Wichtig für die Prüfung:** Auch wenn das Subnetz rechnerisch groß genug ist, kann der **Vergabeplan zu knapp** sein, nämlich dann, wenn feste Adressen und DHCP-Pool zusammen den Bedarf nicht abdecken. Halte außerdem zwei Zahlen auseinander: die Reserve (wie viel der zugeteilte Bereich über dem Bedarf liegt) und die Adressen, die **noch gar keinem Zweck zugeordnet** sind.

> **Rechenbeispiel (gegebene Host-Adresse → Netzgrenzen):** *"Bestimmen Sie für `192.168.20.77/27` die Netzadresse, Broadcastadresse und den nutzbaren Hostbereich."* Lösungsweg: /27 → Maske 255.255.255.224 → Blockgröße `256 − 224 = 32`. Die Blockgrenzen im letzten Oktett liegen bei 0, 32, 64, 96, … Die 77 liegt im Block 64–95. Ergebnis: **Netzadresse 192.168.20.64**, **Broadcastadresse 192.168.20.95**, **Hostbereich 192.168.20.65–192.168.20.94**.

> **Randnotiz /31:** Bei klassischen Mehrzugriffsnetzen werden Netz- und Broadcastadresse nicht an Hosts vergeben. Eine Ausnahme sind **/31-Netze auf Punkt-zu-Punkt-Verbindungen** (z. B. zwischen zwei Routern): Dort dürfen laut RFC 3021 beide Adressen als Endpunktadressen genutzt werden.

### 3.2 VLSM (Variable Length Subnet Masking)

Bei VLSM teilst du ein größeres Netz in **Subnetze unterschiedlicher Größe** auf. Du planst **mit dem größten Bedarf zuerst**, und jeder Block muss auf einer passenden Blockgrenze anfangen. Die Planungsreihenfolge muss nicht mit der Reihenfolge der Adressen übereinstimmen. Wichtig ist nur, dass jeder Block sauber auf einer Grenze startet und sich keine Bereiche überlappen. Im folgenden Beispiel entspricht die Vergabe zur besseren Nachvollziehbarkeit direkt der Planungsreihenfolge:

**Beispiel (aus 10.40.0.0/16, Planungsreihenfolge größtes zuerst):**

| Zone | Bedarf | Präfix | Block | Gateway | Statisch | DHCP |
| --- | --- | --- | --- | --- | --- | --- |
| Gäste | 300 Geräte | /23 | 10.40.0.0/23 | 10.40.0.1 | – | 10.40.0.10–10.40.1.250 |
| Produktion | 120 Geräte | /24 (bewusst statt /25, wegen getrennter Bereiche + Wachstum) | 10.40.2.0/24 | 10.40.2.1 | .2–.19 | .20–.150 |
| Server | 40 Geräte | /26 | 10.40.3.0/26 | 10.40.3.1 | .2–.56 (statisch, Server brauchen feste Adressen; Rest bewusste Reserve für Diensterweiterung) | – |

> **Wichtig für die Prüfung:** Bei Produktion zeigt sich ein Klassiker: 120 Geräte würden rechnerisch knapp in /25 (126 nutzbar) passen. Rechnet man den Bedarf mit einer geplanten Wachstumsreserve von 20% plus Gateway durch (`120 × 1,2 + 1 = 145`), reicht ein /25 schon rechnerisch nicht mehr – das nächstgrößere Netz ist /24 (254 nutzbar). Der tatsächlich vergebene Bereich (18 statische + 131 DHCP-Adressen = 149 Adressen) deckt diesen Bedarf inklusive Reserve ab; die darüber hinaus noch freien Adressen `.151–.254` bleiben bewusst unzugeordnet für spätere, noch nicht konkret geplante Erweiterung. Die rein mathematisch kleinste Lösung ist nicht immer die **betrieblich richtige**, aber jede Reserve – ob im Vergabebereich oder als unzugeordnete Fläche – sollte einem nachvollziehbaren Zweck zugeordnet werden können.

In einen Adressplan für den Betrieb gehören mindestens: Zone bzw. VLAN, IPv4-Präfix, IPv6-Präfix (oder die dokumentierte Entscheidung, kein IPv6 zu nutzen), Gateway, DHCP-Bereich, reservierte feste Adressen, DNS-Namensraum, Standort und wer zuständig ist.

> 🔍 **Hinweis zur Selbstrecherche (Typ B/Deep-Dive):** Eine vollständige, mehrzonige VLSM-Durchrechnung (z. B. acht Hauptstandort- plus drei Außenstellenzonen mit Gateway/DHCP/Reserve je Zone) sprengt den Rahmen dieses kompakten Artikels – das systematische Rechenschema aus 3.1–3.2 lässt sich aber direkt auf beliebig viele Zonen übertragen. Übungsaufgaben mit vollständigem Rechenweg (Zweierpotenzen-Tabelle, Arbeitsvorlage, Kontrollfragen) findet ihr in den Kursunterlagen.

> **IHK-Typfrage:** *"Warum plant man bei VLSM zuerst das größte Netz?"*
> **Musterantwort:** Würde man mit kleinen Netzen beginnen, könnten diese an beliebigen Adressen im Adressraum liegen und dadurch große, zusammenhängende Blöcke fragmentieren, die für später geplante größere Netze benötigt würden. Plant man dagegen zuerst die großen Bedarfe auf gültigen, großen Blockgrenzen, bleiben die verbleibenden Adressräume sauber nutzbar für die kleineren Netze – am Ende passen alle Blöcke ohne Überlappung zusammen.

---

## 4. Ethernet, Switching, VLAN und WLAN

> **Grundprinzip:** Ein Großraumbüro ohne Trennwände (ein Netz ohne VLANs) heißt: Jeder hört jeden Anruf mit (Broadcast-Domäne). Trennwände mit eigenen Türen (VLANs) schaffen getrennte Bereiche – aber eine Tür allein entscheidet noch nicht, **wer** hindurchgehen darf. Das regelt erst ein Pförtner (Routing + Firewall, siehe Abschnitt 5).

### 4.1 Switching-Grundlagen

Ein Switch merkt sich, an welchem Port welche Absender-MAC-Adresse auftaucht, und schickt Unicast-Frames dann nur noch an den richtigen Port. Broadcasts landen bei allen Geräten der Broadcast-Domäne. **Routen kann ein Switch nicht**: Wer zwischen verschiedenen IP-Netzen oder VLANs vermitteln soll, braucht ein Gerät auf Schicht 3 und eine Regel, die den Übergang erlaubt.

### 4.2 VLANs und Trunks

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Access-Port** | Transportiert typischerweise den Verkehr eines Endgeräts ungetaggt in einem zugeordneten VLAN (Sonderfälle wie Voice-VLANs möglich) | 🔴 |
| **Trunk** | Transportiert mehrere VLANs, getaggt nach **IEEE 802.1Q** | 🔴 |
| **VLAN-Matrix** | Dokumentiert VLAN-ID, Name, Zweck, Präfix, Gateway, DHCP, erlaubte Partner | 🔴 |

> **Wichtig für die Prüfung – ein VLAN ist keine Firewall:** Ein VLAN trennt nur die Layer-2-Domäne. Ob Verkehr zwischen zwei VLANs erlaubt ist, entscheiden erst Routing (Layer 3) und Firewall-Regeln (siehe Abschnitt 5). Ein Zugriff scheitert je nach fehlender Ebene aus unterschiedlichen Gründen: falsche Portzuordnung, fehlender Trunktransport, oder fehlende Firewall-Freigabe – das sind drei verschiedene Fehlerquellen.

Redundante Layer-2-Pfade können Broadcast-Stürme verursachen; **Spanning Tree** (bzw. **Rapid Spanning Tree**) blockiert dafür ausgewählte Pfade kontrolliert.

### 4.3 WLAN-Planung

Wer ein WLAN plant, muss **Funkausbreitung, Kapazität, Sicherheit und Roaming** zusammen denken. Große Reichweite allein macht noch kein gutes WLAN. Die Standards heißen **802.11**. Im 2,4-GHz-Band reicht das Signal weiter, es gibt aber nur wenige Kanäle, die sich nicht überlappen. 5 und 6 GHz bieten mehr Kapazität, verlangen aber eine sorgfältigere Planung der Funkzellen.

> **Wichtig für die Prüfung:** SSIDs müssen eindeutig Sicherheitszonen zugeordnet sein (Gäste, Beschäftigte, technische Geräte getrennt), aber nicht zwingend 1:1 mit VLANs. **WPA2** (mit AES/CCMP) ist weiterhin verbreitet, **WPA3** die neuere Sicherheitsgeneration; veraltete Verfahren wie WEP/WPA sind zu vermeiden. In Unternehmensnetzen ermöglicht **WPA2/WPA3-Enterprise** in Verbindung mit **802.1X** und EAP eine individuelle Authentisierung von Nutzenden/Geräten gegenüber einem zentralen Server (meist RADIUS) – aus diesem Authentisierungsprozess werden zugleich Schlüssel für die Funkverschlüsselung abgeleitet. Die drei Rollen dabei: **Supplicant** (Client), **Authenticator** (im WLAN der Access Point/WLAN-Controller, im kabelgebundenen LAN der Switch), **Authentication Server** (meist RADIUS). **Eine versteckte SSID oder volle Sendeleistung schützt nichts.** Wer das als Sicherheitskonzept verkauft, macht einen typischen Prüfungsfehler. Versteckte SSIDs sorgen sogar für mehr Funkverkehr, weil Clients aktiv nach ihnen rufen (Probe Requests).

> **IHK-Typfrage:** *"Ein Verwaltungsclient (Access-Port, VLAN 10, ungetaggt) soll auf einen Server in VLAN 40 zugreifen. Der Zugriff scheitert. Nennen Sie drei mögliche, unabhängige Fehlerursachen."*
> **Musterantwort:** (1) **Port:** Der Access-Port, an dem der Client hängt, steckt vielleicht im falschen VLAN statt in VLAN 10. (2) **Trunk:** Auf der Verbindung zum Layer-3-Gerät fehlt VLAN 10 womöglich in der Liste erlaubter VLANs, oder die beiden Enden sind unterschiedlich konfiguriert. (3) **Firewall:** Auch wenn beide VLANs sauber eingerichtet sind, kann eine Regel fehlen, die Verkehr von VLAN 10 nach VLAN 40 zulässt. Jede dieser drei Stellen prüfst du für sich.

---

## 5. Routing, NAT und Firewall-Grundlagen

> **Grundprinzip:** Ein Navi (Routing) sagt dir, welche Straße zum Ziel führt. Ein Dolmetscher an der Grenze (NAT) übersetzt deinen Ausweis in ein anderes Format, damit du im Ausland erkannt wirst. Ein Grenzbeamter (Firewall) entscheidet unabhängig davon, ob du überhaupt einreisen darfst. Drei getrennte Funktionen, die oft verwechselt werden.

### 5.1 Routing: Longest Prefix Match

Passen mehrere Einträge der Routingtabelle, nimmt der Router den mit dem **längsten Präfix** ("Longest Prefix Match"). Die **Default Route** kommt nur zum Zug, wenn sonst nichts passt. Statische Routen sind leicht zu überblicken, werden in großen Netzen aber mühsam. Dynamische Protokolle wie **OSPF** verteilen die Wege selbstständig, bringen dafür aber mehr Aufwand im Betrieb und bei der Absicherung.

> **Übungsbeispiel:** Routingtabelle mit `0.0.0.0/0 → Router A`, `10.0.0.0/8 → Router B`, `10.40.0.0/16 → Router C`, `10.40.7.0/24 → Router D`. Welcher nächste Hop wird für `10.40.7.150` gewählt? **Router D** (die spezifischste passende Route, /24 schlägt /16, /8 und /0). Für `10.40.9.20` gilt dagegen **Router C** (/24 passt nicht, /16 schon), für `8.8.8.8` **Router A** (nur die Default Route passt).

### 5.2 NAT/PAT

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Source NAT** | Ersetzt die Quelladresse ausgehender Verbindungen | 🔴 |
| **PAT (NAT Overload)** | Zusätzlich Portübersetzung – mehrere interne Clients teilen sich eine öffentliche IP | 🔴 |
| **Destination NAT** | Verändert das sichtbare Ziel (Portweiterleitung), veröffentlicht interne Dienste | 🟡 |

> **Wichtig für die Prüfung:** NAT ist **keine Sicherheitsfunktion**. NAT schreibt nur Adressen um. Ob der Verkehr durchdarf, entscheidet weiterhin eine Firewall-Regel, und die kann zu derselben Übersetzung erlauben oder sperren.

### 5.3 Firewall-Regeln

Zu jeder Firewall-Regel gehören mindestens: **Quelle, Ziel, Protokoll mit Port bzw. ICMP-Typ, Aktion (erlauben oder sperren), Zweck, wer sie verantwortet und ob protokolliert wird**; je nach System kommen Richtung/Zonen, Zeitbedingungen und weitere Kriterien hinzu (Richtung ist nicht bei jedem Firewall-System ein zwingend eigenständiges Feld – oft ergibt sie sich bereits aus Quelle/Ziel bzw. Interface/Zone). Grundlage ist das **Minimalprinzip (Least Privilege)**: Gesperrt ist alles, was nicht ausdrücklich und mit Grund erlaubt wurde. Pauschalregeln wie "any to any" haben als Dauerlösung nichts verloren.

Eine **zustandsbehaftete (stateful) Firewall** führt Zustandsinformationen über erlaubte Datenflüsse; bei TCP orientiert sie sich am Verbindungszustand, bei UDP und ICMP an zeitlich begrenzten Zuordnungen zusammengehöriger Pakete. Rückverkehr wird nur akzeptiert, wenn er einem zuvor erlaubten Datenfluss zugeordnet werden kann.

> **Wichtig für die Prüfung:** Zu einer neu eingerichteten oder geänderten sicherheitsrelevanten Freigabe gehören ein **Positivtest** (erlaubte Kommunikation funktioniert) **und** ein passender **Negativtest** (ähnliche, nicht erlaubte Kommunikation wird blockiert). Beispiel: Regel "IT → INFRA, TCP/443, ALLOW". Positivtest: IT-Client erreicht das Ziel. Negativtest: Ein ADMIN-Client (andere Quellzone) erreicht dasselbe Ziel **nicht** – das prüft insbesondere, dass die Freigabe nicht versehentlich weiter gefasst ist als vorgesehen. Je nach Regel kann ein Negativtest auch auf einer anderen Dimension ansetzen, z. B. derselben Quelle mit einem nicht erlaubten Zielport.

> **IHK-Typfrage:** *"Erklären Sie den Unterschied zwischen Routing, NAT und Firewall-Filterung anhand eines Datenpakets, das vom internen Netz ins Internet will."*
> **Musterantwort:** **Routing** bestimmt den geeigneten Paketweg bzw. den nächsten Hop – bei einem Internetziel typischerweise über die Default Route zum Internet-Gateway. **NAT/PAT** übersetzt bei Bedarf die private Quelladresse (z. B. 10.40.1.50) in die öffentliche IP-Adresse des Internetanschlusses, damit die Rückübersetzung anhand des angelegten NAT-/PAT-Zustands erfolgen kann – das ist reine Adressübersetzung, keine Sicherheitsprüfung. **Eine dafür konfigurierte Filterinstanz** (meist die Firewall, ggf. auch Router-ACLs oder Host-Firewalls) entscheidet unabhängig davon, ob dieser Datenfluss überhaupt erlaubt ist – anhand von Quelle, Ziel, Protokoll und Port. Alle drei Funktionen sind fachlich getrennt und werden getrennt getestet; die genaue technische Verarbeitungsreihenfolge kann je nach System und Verkehrsrichtung variieren, aber ein funktionierendes Routing oder eine korrekte NAT-Übersetzung sagt nichts darüber aus, ob der Verkehr auch tatsächlich durchgelassen wird.

---

## 6. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Ein längeres Präfix (z. B. /26) bezeichnet ein größeres Netz als ein kürzeres (z. B. /24) | Genau umgekehrt: Mehr Netzbits bedeuten weniger Hostbits – /26 ist das **kleinere** Netz |
| 2 | TCP ist "sicher", weil es zuverlässig überträgt | TCP garantiert nur geordnete, zuverlässige Zustellung – Vertraulichkeit/Identitätsprüfung kommen erst durch TLS hinzu |
| 3 | IPv6 ist einfach IPv4 mit längeren Adressen | Neighbor Discovery statt ARP, Autokonfiguration und Multicast-Nutzung unterscheiden sich grundlegend |
| 4 | Ein VLAN ist bereits eine Sicherheitsgrenze | Ein VLAN trennt nur Layer 2 – ob Verkehr zwischen VLANs erlaubt ist, entscheiden Routing und Firewall |
| 5 | Eine versteckte SSID oder maximale Sendeleistung sind Sicherheitsmaßnahmen | Beides ist keine belastbare Sicherheitsmaßnahme – entscheidend sind WPA2/WPA3 und ggf. 802.1X |
| 6 | NAT macht einen Datenfluss automatisch sicher | NAT übersetzt nur Adressen/Ports – ob der Verkehr erlaubt ist, entscheidet eine dafür konfigurierte Filterinstanz (meist die Firewall, ggf. auch Router-ACLs oder Host-Firewalls) |
| 7 | Eine erlaubende Firewall-Regel ist ausreichend getestet, wenn der Positivtest funktioniert | Ein zusätzlicher Negativtest (ähnliche, nicht erlaubte Quelle/Ziel/Port wird blockiert) prüft, dass die Freigabe nicht versehentlich weiter gefasst ist als vorgesehen |

---

## 7. Vertiefung und Ausblick (freiwillig – für den ersten Durchgang nicht erforderlich)

- **Vollständige mehrzonige VLSM-Durchrechnung** (→ Abschnitt 3.2): Das Rechenschema aus 3.1–3.2 auf alle Zonen eines realen Kundenszenarios anwenden (z. B. acht Hauptstandort- plus drei Außenstellenzonen) – Übungsmaterial mit Arbeitsvorlage und Kontrollfragen in den Kursunterlagen.
- **Präfixaggregation** (→ Abschnitt 3): Wie zusammenhängende Präfixe bei geeigneter Lage zu einem kürzeren Präfix zusammengefasst werden können, um Routingtabellen zu verkleinern.
- **IPv6-Subnetting-Rechenweg**: Wie viele /64-Netze passen in ein /56? (`2^(64-56) = 256`) – dasselbe Zweierpotenz-Prinzip wie bei IPv4, nur mit anderen Bitgrenzen.
- **Wildcard-Masken**: Inverse Schreibweise zur Subnetzmaske, u. a. bei Access Control Lists (ACLs) relevant.
- **Monitoring und Verfügbarkeit**: Erreichbarkeit (ICMP/Ping) vs. tatsächliche Dienstverfügbarkeit (Port-/Anwendungstest) sind zwei unterschiedliche Prüfebenen – ein antwortender Host beweist noch keinen funktionierenden Dienst (vgl. Abschnitt 2.3). Dazu gehören außerdem Schnittstellen-Monitoring (Traffic/Errors/Drops), SNMP, Schwellwerte/Alarme und Uptime-Nachweise – Teil des offiziellen AP2-Kompetenzrahmens (§ 22 FIAusbV).
- **Netzwerkkomponenten-Auswahl**: Switch (Layer 2), Layer-3-Switch (Routing zwischen VLANs), Router, Firewall, Access Point, WLAN-Controller – jeweils mit eigenem Einsatzzweck; ebenfalls Teil des offiziellen AP2-Kompetenzrahmens.
- **DHCP-Relay über VLAN-Grenzen**: Ein DHCP-Server in einem anderen VLAN benötigt einen Relay-Agenten (IP-Helper-Address) auf dem Layer-3-System, der die DHCP-Broadcast-Anfrage in eine gerichtete Unicast-Anfrage umsetzt.
- **Layer-2-Sicherheit**: Klassische Angriffe (MAC-Flooding, ARP-Spoofing, Rogue DHCP) und Gegenmaßnahmen (Port Security, DHCP Snooping, Dynamic ARP Inspection).
- **Redundanz über Spanning Tree hinaus**: Link Aggregation (LACP) für gebündelte Uplinks, HSRP/VRRP für redundante Gateways – relevant für Anforderungen wie "Produktion darf nicht ausfallen" (siehe Abschnitt 1).
- **Spanning Tree im Detail** (→ Abschnitt 4.2): Wie STP/RSTP redundante Layer-2-Pfade erkennt und kontrolliert blockiert, um Broadcast-Stürme zu verhindern.
- **Dynamisches Routing (OSPF) im Detail** (→ Abschnitt 5.1): Wie Router eine gemeinsame Sicht auf die Netztopologie aufbauen und daraus automatisch Routen berechnen.
- **WLAN-Planungsablauf im Detail**: Grundriss/Störquellen erfassen → Nutzer-/Gerätedichte bestimmen → AP-Positionen planen → Kanalbreiten/-belegung planen → Ausleuchtung (Site Survey) → Roaming/Kapazität testen.

> 🔍 **Hinweis zur Selbstrecherche:** Konkrete Konfigurationsbefehle (Switch-/Router-CLI, WLAN-Controller) sind stark herstellerabhängig und ändern sich – für die praktische Umsetzung immer die aktuelle Dokumentation des jeweils eingesetzten Produkts konsultieren, nicht auswendig gelernte Befehle.

---

## 8. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Was macht eine Netzwerkanforderung prüfbar? | Gegenstand, messbare Bedingung, Randbedingungen, Prüfmethode mit Abnahmekriterium |
| 2 | Nenne die vier TCP/IP-Schichten. | Anwendung, Transport, Internet/Vermittlung, Netzzugang |
| 3 | Warum ist TCP nicht automatisch sicher? | TCP garantiert nur zuverlässige Zustellung, keine Verschlüsselung/Identitätsprüfung – dafür braucht es z. B. TLS |
| 4 | Wie viele Adressen hat ein /27-Netz, wie viele nutzbar? | 32 Adressen, typisch 30 nutzbar |
| 5 | In welcher Reihenfolge plant man bei VLSM? | Vom größten zum kleinsten Bedarf, damit große Blöcke nicht fragmentiert werden |
| 6 | Was unterscheidet Access-Port und Trunk? | Access-Port: ein VLAN, ungetaggt; Trunk: mehrere VLANs, getaggt nach 802.1Q |
| 7 | Ist ein VLAN eine Sicherheitsgrenze? | Nein, nur eine Layer-2-Trennung – Sicherheit entscheiden Routing und Firewall |
| 8 | Was bedeutet "Longest Prefix Match"? | Die spezifischste passende Route in der Routingtabelle wird gewählt, nicht die Default Route |
| 9 | Was unterscheidet NAT von einer Firewall-Filterung? | NAT übersetzt nur Adressen/Ports; eine dafür konfigurierte Filterinstanz (meist die Firewall) entscheidet, ob der Verkehr erlaubt ist |
| 10 | Warum ist ein Negativtest bei einer sicherheitsrelevanten Firewall-Regel sinnvoll? | Er prüft, dass die Freigabe nicht versehentlich weiter gefasst ist als vorgesehen (z. B. andere Quellzone wird korrekt blockiert) |
| 11 | Berechnen Sie Netzadresse, Broadcastadresse und Hostbereich für `192.168.10.141/26`. | Maske 255.255.255.192, Blockgröße 64 → Block 128–191 → Netz 192.168.10.128, Broadcast 192.168.10.191, Hostbereich .129–.190 |
| 12 | Welche Route wird für `10.40.7.150` gewählt, wenn `0.0.0.0/0`, `10.0.0.0/8`, `10.40.0.0/16` und `10.40.7.0/24` in der Tabelle stehen? | Die /24-Route (spezifischste passende Route, Longest Prefix Match) |
| 13 | Ein Client hat eine IP-Adresse, erreicht aber sein Gateway nicht. Nennen Sie mögliche Ursachen auf drei verschiedenen Schichten. | Z. B. Schicht 1: Kabel/Link defekt; Schicht 2: falsche VLAN-Zuordnung des Ports; Schicht 3: falsches Gateway konfiguriert |

---

## 9. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Prüfbare Anforderung** | Gegenstand + messbare Bedingung + Randbedingungen + Prüfmethode |
| **TCP vs. UDP** | Verbindungsorientiert/zuverlässig vs. verbindungslos/ohne Zustellgarantie |
| **RFC 1918** | Private IPv4-Bereiche (10/8, 172.16/12, 192.168/16), nicht global routbar |
| **IPv6 /64** | Übliche Präfixlänge eines IPv6-LANs; verfügbare Subnetzbits hängen vom zugeteilten Standortpräfix ab (z. B. /48 oder /56) |
| **fe80::/10** | IPv6 Link-Local, nur lokaler Link |
| **VLSM** | Unterschiedlich große Präfixe im selben Netz, größtes Netz zuerst planen |
| **Access-Port / Trunk** | Ein VLAN ungetaggt / mehrere VLANs getaggt (802.1Q) |
| **VLAN ≠ Firewall** | VLAN trennt nur Layer 2, Sicherheit entscheiden Routing + Firewall |
| **Longest Prefix Match** | Spezifischste passende Route gewinnt vor Default Route |
| **NAT/PAT** | Adress-/Portübersetzung, keine Sicherheitsfunktion |
| **Firewall-Minimalprinzip** | "Verweigern, was nicht begründet erlaubt wurde" |
| **Positiv-/Negativtest** | Erlaubtes funktioniert + Ähnliches, nicht Erlaubtes wird blockiert |

---

## 10. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die Prüfung hören will |
| --- | --- | --- |
| Anforderung prüfbar formulieren | "Formen Sie Aussage X in eine prüfbare Anforderung um" | Konkrete Messgröße, Randbedingung und Prüfmethode nennen, nicht nur umformulieren |
| Subnetz berechnen | "Berechnen Sie Präfix/Blockgröße für X Hosts" | Vollständigen Rechenweg zeigen (Bedarf → Zweierpotenz → Präfix → Blockgrenze), nicht nur das Ergebnis |
| VLSM-Plan erstellen | "Planen Sie X Zonen in einem Supernetz" | Reihenfolge größtes-zuerst einhalten, Überlappungsfreiheit explizit prüfen |
| Fehlerursache eingrenzen | "Zugriff X auf Y scheitert – mögliche Ursachen?" | Mehrere unabhängige Ebenen nennen (Portzuordnung, Trunk, Routing, Firewall), nicht nur eine Vermutung |
| Firewall-Regel bewerten | "Ist Regel X ausreichend?" | Vollständigkeit der Regel (Quelle/Ziel/Protokoll/Port/Richtung) UND Positiv-/Negativtest einfordern |

---

## 11. Merksätze für das Fachgespräch

> Ein längeres Präfix ist ein kleineres Netz – mehr Netzbits bedeuten weniger Hostbits.

> TCP ist zuverlässig, nicht vertraulich – Verschlüsselung kommt von TLS, nicht vom Transportprotokoll.

> Bei VLSM zuerst die großen Netze setzen, sonst fragmentiert der Adressraum.

> Ein VLAN trennt Layer 2 – ob Verkehr durchdarf, entscheiden Routing und Firewall.

> Routing sagt wohin, NAT sagt mit welcher sichtbaren Adresse, die Firewall sagt ob überhaupt.

---

```yaml
dokument: LF9.1-wiki-artikel
themenfeld: "LF9.1 - Netze planen und adressieren"
kmk_bereich: "FISI-spezifisch: AP2 schriftlicher Bereich 2 (Analyse und Entwicklung von Netzwerken)"
titel: "Netze planen und adressieren"
typ: "Typ A – Kompakter Prüfungs-Wiki (FISI-fokussiert)"
status: final
stand: 2026-09-12
quellen_intern:
  - "LF9.1.1-5: Anforderungen, OSI/TCP-IP und Adressierung, Subnetting und Adressplanung, Switching/VLAN/WLAN, Routing und Firewall"
  - "Zusätzliche Rechercheunterlagen vom Auftraggeber: Kompetenzbereiche-Übersicht (IT-Handbuch für Fachinformatiker) und IPv6-Präfixstruktur"
  - "Research Report FISI-Abschlussprüfungsthemen (IHK-Leitfaden AO 2020) - zur AP2-Gewichtung im Kopf verwendet"
  - "Bewusster Querverweis zu LF5.1 (Requirements & Analysis) statt Wiederholung der allgemeinen Anforderungsanalyse-Grundlagen"
quellen_fachlich:
  - titel: "§ 22 FIAusbV (AP2 FISI, Analyse und Entwicklung von Netzwerken, 90 Min., 10%)"
    herausgeber: "Bundesministerium der Justiz (gesetze-im-internet.de)"
    status: "in Runde 2 ergänzt, amtliche Primärquelle für die Prüfungsrelevanz-Angabe im Kopf"
  - titel: "OSI/TCP-IP-Modell, IPv4/IPv6-Adressierung (RFC 1918, RFC 3021, RFC 4291, RFC 4861), VLSM, VLAN (IEEE 802.1Q), WLAN (IEEE 802.11)"
    herausgeber: "Rohmaterial + etabliertes Netzwerktechnik-Standardwissen"
    status: "stabile, langjährig etablierte Standards; RFC 3021 (/31-Sonderfall) und RFC 4861 (Neighbor Discovery) in Runde 2 ergänzt"
review_historie:
  - runde: 1
    datum: 2026-09-12
    ergebnis: "Erstdraft erstellt, alle fünf Themenblöcke zu LF9.1 plus Zusatzrecherche eingearbeitet. Bewusst als ein zusammenhängender Artikel (nicht 5 Einzelartikel) gemäß Auftraggeber-Vorgabe; Detailtiefe wie vollständige Mehrzonen-VLSM-Rechnung in den Deep-Dive verschoben statt im Haupttext. FISI-fokussiert (AP2 schriftlicher Bereich 2), Querverweis zu LF5.1 statt Wiederholung der Anforderungsanalyse-Grundlagen."
  - runde: 2
    datum: 2026-09-12
    ergebnis: "Externe Prüfung (4 Reviews) eingearbeitet. Wichtigster Fund, von zwei Reviews bestätigt: VLSM-Beispiel widersprach der eigenen Planungsregel (Gäste als größtes Netz lag numerisch nicht zuerst) - Blockreihenfolge an Planungsreihenfolge angeglichen (10.40.0.0/23 -> .2.0/24 -> .3.0/26), zusätzlich Klarstellung ergänzt, dass Planungsreihenfolge nicht zwingend numerische Reihenfolge sein muss. Ebenfalls behoben: Gäste-Zone ohne DHCP (unrealistisch bei 300 Geräten) - DHCP-Pool ergänzt; Produktion-Reserve war rechnerisch inkonsistent (200 statt ~150 Adressen für 120 Geräte) - auf nachvollziehbares Verhältnis (~20% Reserve) korrigiert. AP2-Einordnung im Header war durch eine Review fälschlich als 'AP3' infrage gestellt - per Gegenrecherche (§ 22 FIAusbV, zwei unabhängige Reviews mit Zitat) als korrekt bestätigt, stattdessen die zu pauschale 'AP1+AP2'-Nennung präzisiert (AP2 als Schwerpunkt). OSI-Modell tatsächlich ergänzt (Abschnitt hieß 'OSI/TCP-IP', zeigte aber nur TCP/IP) - Zuordnungstabelle OSI-Schicht zu TCP/IP-Ebene plus Diagnosebezug ergänzt. IPv6-Präfixstruktur relativiert ('meist 48 Bit' war zu pauschal, /56 als Alternative ergänzt). Vollständiges Rechenbeispiel (Host-IP -> Netz/Broadcast/Hostbereich) und LPM-Übungstabelle ergänzt, da der Artikel 'viel Rechenstoff' ankündigte, aber zu wenig davon zeigte. NAT/Routing/Firewall-Musterantwort entschärft (keine universelle Verarbeitungsreihenfolge mehr behauptet), 'Sicherheitsentscheidung ausschließlich Firewall' zu 'dafür konfigurierte Filterinstanz' präzisiert. 802.1X-Erklärung um Supplicant/Authenticator/Auth-Server-Rollen präzisiert. Firewall-Regel-Definition um ICMP-Typ ergänzt, Richtung als nicht zwingend eigenständiges Feld gekennzeichnet. Stateful-Firewall- und ARP/ND-Aussagen fachlich präzisiert (TCP-Zustand vs. UDP/ICMP-Zuordnung; IPv6 nutzt Multicast statt Broadcast). Lernzeit realistisch nach oben korrigiert (war deutlich unterschätzt für den Rechenumfang). Deep-Dive um mehrfach bestätigte Lücken erweitert (Monitoring/Verfügbarkeit und Netzwerkkomponenten-Auswahl sind Teil des offiziellen § 22-Rahmens, dazu DHCP-Relay, Layer-2-Sicherheit, Redundanz, IPv6-Subnetting-Rechenweg, Wildcard-Masken, WLAN-Planungsablauf) - bewusst als kompakte Deep-Dive-Punkte statt Haupttext-Erweiterung, gemäß Auftraggeber-Vorgabe zur Kompaktheit. YAML-Quellen um § 22 FIAusbV als Primärquelle sowie RFC 3021/4291/4861 ergänzt."
  - runde: 3
    datum: 2026-09-12
    ergebnis: "4 Reviews eingearbeitet: VLSM-Reservebegründung mathematisch sauber gemacht (Bedarf x 1,2 + Gateway statt nachträglicher Prozentangabe), Server-Reserve kommentiert, Diagnose-Formulierung repariert und weniger deterministisch gefasst, WPA2/WPA3 und 802.1X-Authenticator-Rolle präzisiert, Fachgespräch-Bezug korrigiert. Zwei Reviews behaupteten erneut abgeschnittenen Text/kaputte Markdown-Struktur - widerlegt."
  - runde: 4
    datum: 2026-09-12
    ergebnis: "Eigene Abschlussprüfung: Prüfungsfalle 7 und Selbsttest 9 trugen noch alte 'Firewall beweist/entscheidet allein'-Formulierungen, die in 5.3 bereits präzisiert waren - nachgezogen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Prüfrunden + 1 eigene Abschlussprüfung, 2026-09-12) – Freigabe durch Autor:in bestätigt"
```