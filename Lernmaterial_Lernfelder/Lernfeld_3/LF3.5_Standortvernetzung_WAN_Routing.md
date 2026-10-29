# LF3.5 – Standortvernetzung (WAN & Routing)

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 100–120 Min., mit Vertiefung (statische Routen, Split-Tunneling, Shared-Responsibility-Details): 140–160 Min.
> **Status:** Final
> **Stand:** 2026-09-04

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Warum braucht ein Client für Ziele im eigenen Subnetz kein Gateway, für alle anderen Ziele aber schon? | [1.1](#11-lokale-routing-entscheidung-direkt-vs-gateway) |
| 2 | Was ist DS-Lite/CG-NAT, und warum scheitert dort typischerweise eingehendes Port-Forwarding? | [2.3](#23-provider-ip-vergabe-dual-stack-vs-ds-lite) |
| 3 | Warum ist NAT keine Firewall, obwohl es in der Praxis oft so wahrgenommen wird? | [3.2](#32-nat-ist-keine-firewall) |
| 4 | Warum sollte ein Firmennetz keine verbreiteten Heimrouter-Standardnetze (z. B. `192.168.178.0/24`) verwenden? | [4.3](#43-subnetz-kollision-beim-vpn) |
| 5 | Was unterscheidet IaaS, PaaS und SaaS in der Aufteilung der Verantwortung zwischen Kunde und Anbieter? | [5.2](#52-shared-responsibility) |

---

## 1. Routing am Client

> **Grundprinzip:** Nicht nur Router routen – jedes Endgerät besitzt eine eigene, kleine Routing-Tabelle und trifft vor jedem gesendeten Paket eine einfache Entscheidung: direkt zustellen oder ans Gateway übergeben.

### 1.1 Lokale Routing-Entscheidung: Direkt vs. Gateway

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Direkte Zustellung | Ergibt die lokale Routing-Tabelle, dass die Zieladresse über ein direkt angeschlossenes Netz (dieselbe IP-Subnetzmaske) erreichbar ist, versucht der Client anschließend, die MAC-Adresse des Ziels zu ermitteln – bei IPv4 per ARP, bei IPv6 per Neighbor Discovery Protocol (NDP) – und schickt das Paket direkt über den Switch. Das funktioniert nur, wenn sich beide Geräte tatsächlich im selben Layer-2-Segment/VLAN befinden; ein Router wird dafür nicht benötigt | 🔴 |
| Default Route / Standard-Gateway | Existiert keine spezifischere Route für das Ziel, verwendet der Client seine Default Route (`0.0.0.0/0` bzw. IPv6 `::/0`) und übergibt das Paket an sein Standard-Gateway – der lokale Router entscheidet anhand seiner eigenen, größeren Routing-Tabelle über den nächsten Schritt (Next Hop) | 🔴 |

> **IHK-Typfrage:** *Ein Windows-PC hat die IP `192.168.10.50/24`. Erkläre anhand seiner lokalen Routing-Tabelle, warum er ein Paket an `192.168.10.80` direkt über den Switch schickt, ein Paket an `8.8.8.8` aber an die MAC-Adresse des Routers übergeben muss.*
> **Musterantwort:** Der PC vergleicht bei jedem zu sendenden Paket die Ziel-IP mit seiner eigenen Subnetzmaske. `192.168.10.80` liegt bei `/24` im selben Subnetz wie der PC selbst – das Ziel gilt damit als "direkt erreichbar", der PC ermittelt per ARP dessen MAC-Adresse und sendet das Paket direkt über den Switch, ohne den Router einzubeziehen. `8.8.8.8` liegt dagegen in einem völlig anderen Netz. Da der PC dieses Netz nicht direkt erreichen kann, verwendet er seine Default Route und übergibt das Paket stattdessen an die MAC-Adresse seines Standard-Gateways, das dann für die Weiterleitung ins Internet zuständig ist.

🔴 **Stolperstein – Gateway im falschen Subnetz:** Bei einer normalen Clientkonfiguration muss das Standard-Gateway über eine direkt angeschlossene Route erreichbar sein und deshalb üblicherweise im selben lokalen Subnetz liegen. Wird einem PC die IP `192.168.1.50/24`, aber als Gateway `192.168.2.1` eingetragen, funktioniert die Konfiguration im Regelfall trotzdem nicht: Das Gateway liegt aus Sicht der lokalen Routing-Tabelle bereits in einem fremden Netz und ist damit ohne zusätzliche Route nicht direkt per ARP erreichbar.

🟡 **Praxis-Tipp – Ping ohne Website ist meist kein Routing-Fehler:** Funktioniert `ping 8.8.8.8`, sind für dieses IPv4-Ziel grundsätzlich Routing, Rückweg und ICMP-Kommunikation funktionsfähig – das beweist aber nicht automatisch, dass auch alle anderen Ziele, Protokolle oder eine IPv6-Verbindung funktionieren. Lädt `google.de` im Browser trotzdem nicht, ist die Namensauflösung (DNS) eine naheliegende erste Fehlerursache – für eine vollständige Diagnose sollten aber auch Proxy-Einstellungen, IPv6-spezifische Probleme und lokale Sicherheitssoftware in Betracht gezogen werden.

### 1.2 Traceroute und Hops

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Hop | Eine Layer-3-Weiterleitungsstation (meist ein Router), die ein Paket auf dem Weg zum Ziel passiert – nicht jeder Hop muss in der `traceroute`-Ausgabe sichtbar sein, wenn er auf die dafür genutzten Pakete nicht antwortet | 🔴 |
| `tracert`/`traceroute` | Zeigt die sichtbaren, antwortenden Hops auf dem Weg zu einem Ziel nacheinander an; der erste Eintrag ist häufig das eigene Standard-Gateway | 🔴 |

> **IHK-Typfrage:** *Warum ist der erste sichtbare Hop einer `traceroute`-Ausgabe häufig die IP-Adresse des eigenen Standard-Gateways?*
> **Musterantwort:** Jedes Paket, das den lokalen Rechner in Richtung eines fremden Netzes verlässt, wird zunächst an das Standard-Gateway übergeben – das ist normalerweise der erste "Sprung" (Hop) auf dem Weg zum Ziel, unabhängig davon, wie viele weitere Router danach folgen. Erst von dort aus wird das Paket entsprechend der Routing-Tabellen der beteiligten Router weiter in Richtung Ziel geleitet. Der erste Hop kann in der Ausgabe aber auch fehlen oder anders aussehen, wenn das Gateway keine Antwort auf die von `traceroute` genutzten Pakete sendet (z. B. wegen einer Firewall-Regel) – `traceroute` zeigt grundsätzlich nur die antwortenden Stationen, nicht zwingend jeden tatsächlich durchlaufenen Hop.

### 1.3 Statische Routen

🟡 **Praxis-Tipp – Wenn ein Standard-Gateway nicht mehr reicht:** Besitzt ein Unternehmen zwei Router – einen für den Internetzugang, einen zweiten mit Standleitung in eine Filiale (`10.0.5.0/24`) –, reicht ein einfaches Standard-Gateway auf den PCs allein nicht mehr aus, um beide Ziele korrekt zu erreichen. Eine auf dem Internet-Router manuell eingetragene statische Route ("für Netz `10.0.5.0/24`, nutze als Next Hop den Filial-Router") sorgt dafür, dass Pakete in Richtung Filiale trotzdem den richtigen Weg nehmen, ohne dass jeder einzelne Client umkonfiguriert werden muss. Das gilt aber nur für den Hinweg: Der Filial-Router benötigt spiegelbildlich ebenfalls eine Route zurück zum Netz der Zentrale (bzw. eine passende Default-Route), sonst gehen die Antwortpakete auf einem falschen oder gar keinem Weg verloren.

---

## 2. WAN-Zugang und Provider-Strategien

> **Grundprinzip:** Irgendwo endet das eigene Kabel in der Wand – dort übernimmt der Internet Service Provider (ISP) die "letzte Meile" zwischen Gebäude und Internet, mit unterschiedlichen physikalischen Technologien und IP-Vergabestrategien.

### 2.1 Zugangstechnologien: xDSL, DOCSIS und Glasfaser

| Technologie | Medium | Eigenschaften | IHK-Relevanz |
|---|---|---|---|
| xDSL (z. B. VDSL) | Kupfer-Telefonleitung (Vectoring) | Dedizierte Teilnehmeranschlussleitung auf der letzten Kupferstrecke zum Vermittlungspunkt; die erreichbare Datenrate hängt stark von DSL-Variante, Leitungslänge und -qualität ab | 🔴 |
| DOCSIS (Kabel-TV) | Koaxialkabel aus dem TV-Netz | Shared Medium – mehrere Anschlüsse teilen sich insbesondere das Kabelsegment und dessen verfügbare Kapazität; hohe Spitzenbandbreiten möglich, die tatsächlich nutzbare Datenrate kann bei hoher gleichzeitiger Auslastung aber spürbar sinken | 🔴 |
| Glasfaser (Fiber) | Lichtwellenleiter | Unempfindlich gegenüber elektromagnetischen Störungen, geringe Dämpfung, Gigabit-Bereich und darüber möglich | 🔴 |

🟡 **Praxis-Tipp – Glasfaser-Ausbaustufen (FTTx):** "Glasfaser" ist nicht gleich "Glasfaser" – entscheidend ist, wie weit die Faser tatsächlich reicht. FTTC (Fiber to the Curb) endet am grauen Kasten an der Straße, ab dort geht es mit klassischem Kupfer-DSL weiter – oft trotzdem als "Glasfaser-Anschluss" beworben. FTTB (Fiber to the Building) reicht bis in den Keller des Gebäudes. Nur FTTH (Fiber to the Home) führt die Faser tatsächlich bis in die Wohnung bzw. das Büro.

🔴 **Stolperstein – Die Kabel-Gigabit-Täuschung:** Ein DOCSIS-Anschluss mit beworbenen 1 Gbit/s klingt beeindruckend, ist aber ein geteiltes Medium – im Versorgungsbereich teilen sich üblicherweise mehrere Haushalte dieselbe Infrastruktur. Zu Spitzenzeiten (z. B. abends) kann die tatsächlich nutzbare Bandbreite deshalb spürbar unter dem beworbenen Wert liegen. Auch FTTH-Anschlüsse sind davon nicht zwangsläufig völlig frei – bei der verbreiteten PON-Technik (Passive Optical Network) teilen sich ebenfalls mehrere Anschlüsse ein gemeinsames optisches Segment –, in der Praxis sind FTTH-Netze von den typischen Engpässen eines Koaxialsegments aber meist deutlich weniger betroffen.

### 2.2 Modem vs. Router

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Modem / ONT | Stellt die Verbindung zur Zugangstechnik des Providers her und wandelt bzw. terminiert dessen Signal (elektrisch bei DSL/DOCSIS, optisch bei Glasfaser über ein "Optical Network Terminal") in ein Standard-Ethernet-Signal – arbeitet primär auf der Übertragungsebene, je nach Gerät können aber zusätzlich Funktionen auf Layer 2 hinzukommen | 🟡 |
| Router | Übernimmt Routing zwischen LAN und WAN auf Layer 3; NAT- und Firewall-Regeln beziehen dabei häufig zusätzlich Layer-4-Informationen wie TCP-/UDP-Ports und Verbindungszustände mit ein | 🟡 |

### 2.3 Provider-IP-Vergabe: Dual-Stack vs. DS-Lite

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Dual-Stack | Der Anschluss erhält native IPv4-Konnektivität und zusätzlich ein öffentlich routbares IPv6-Präfix für das Kundennetz (oft zusätzlich eine eigene IPv6-Adresse auf der WAN-Seite des Routers) | 🔴 |
| DS-Lite (Dual-Stack Lite) | Der Anschluss erhält ein öffentlich routbares IPv6-Präfix, aber keine eigene öffentliche IPv4-Adresse; IPv4-Verkehr wird per Tunnel zu einem AFTR (Address Family Transition Router) beim Provider transportiert und dort per CG-NAT (Carrier-Grade NAT) übersetzt | 🔴 |
| CG-NAT | NAT auf Provider-Ebene, bei dem sich viele Kunden gemeinsam eine begrenzte Anzahl öffentlicher IPv4-Adressen teilen | 🔴 |

> **IHK-Typfrage:** *Ein Mitarbeiter bekommt zu Hause einen neuen Kabelanschluss mit DS-Lite. Er kann anschließend nicht mehr per IPv4-VPN auf den Firmenserver zugreifen bzw. keinen eingehenden IPv4-Dienst mehr über Port-Forwarding erreichbar machen. Warum?*
> **Musterantwort:** Bei DS-Lite besitzt der Anschluss keine eigene öffentliche IPv4-Adresse mehr – die öffentliche IPv4-Adresse wird per CG-NAT von vielen Kunden gemeinsam genutzt. Ein eingehender Verbindungsaufbau von außen (etwa ein VPN-Server-Betrieb oder klassisches Port-Forwarding für IPv4) lässt sich vom Provider nicht mehr eindeutig einem einzelnen Kunden-Router zuordnen, da mehrere Kunden dieselbe öffentliche IPv4-Adresse teilen. Anfragen von außen kommen deshalb typischerweise nie am eigenen Router an, ohne zusätzliche Maßnahmen (z. B. IPv6-fähiges VPN oder einen vom Provider bereitgestellten Tunnel-/Portfreigabe-Mechanismus).

---

## 3. Router-Grenzfunktionen: NAT und Firewall

> **Grundprinzip:** An der Grenze zwischen LAN und WAN übernimmt der Router zwei fachlich unterschiedliche Aufgaben, die häufig verwechselt werden: NAT übersetzt Adressen, die Firewall entscheidet, was durchgelassen wird.

### 3.1 NAT/Masquerading (Source-NAT)

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| NAT (Network Address Translation) | Übersetzt private IP-Adressen, die im öffentlichen Internet nicht geroutet werden, in eine (meist einzige) öffentliche IP-Adresse des Routers | 🔴 |
| Masquerading (Source-NAT) | Beim Verlassen des LANs ersetzt der Router die private Absender-IP des PCs durch seine eigene öffentliche IP; teilen sich mehrere interne Verbindungen dieselbe öffentliche Adresse, setzt er dabei zusätzlich den Quellport um (PAT/NAPT) und merkt sich die Zuordnung in einer internen NAT-Tabelle | 🔴 |

> **IHK-Typfrage:** *Beschreibe, was der Router auf IP-Header-Ebene macht, wenn ein Mitarbeiter mit privater IP `192.168.1.50` ein YouTube-Video abruft und Masquerading aktiviert ist.*
> **Musterantwort:** Der Router ersetzt im ausgehenden Paket die private Absender-IP `192.168.1.50` durch seine eigene öffentliche IP-Adresse. Da sich normalerweise viele interne Geräte dieselbe öffentliche Adresse teilen, setzt er zusätzlich den Quellport um (Port Address Translation/PAT) und speichert die Zuordnung aus interner Adresse plus internem Port zu öffentlicher Adresse plus öffentlichem Port in seiner NAT-Tabelle. Antwortet der YouTube-Server, kommt das Paket an der öffentlichen IP und dem umgesetzten Port des Routers an; dieser schlägt anhand der gespeicherten Zuordnung nach, an welchen internen Client (`192.168.1.50`, ursprünglicher Port) er das Paket zurückreichen muss, und übersetzt Zieladresse und Zielport entsprechend zurück.

### 3.2 NAT ist keine Firewall

🔴 **Stolperstein – "NAT schützt uns, weil das Internet unsere PCs nicht sieht":** Diese verbreitete Annahme ("Security by Obscurity") ist fachlich unpräzise. NAT wurde primär entwickelt, um knappe öffentliche IPv4-Adressen einzusparen, nicht als Sicherheitsfunktion. Dass unaufgeforderter eingehender Verkehr aus dem WAN nicht ohne Weiteres ins LAN gelangt, hat zwei Ursachen, die oft vermischt werden: Zum einen fehlt dem Router bei reinem Masquerading ohne bestehenden Tabelleneintrag schlicht die Information, an welchen internen Client ein unaufgefordertes Paket gehören soll – ein Nebeneffekt der NAT-Funktionsweise, kein bewusster Schutzmechanismus. Zum anderen verwirft die zustandsbehaftete ("stateful") Firewall der meisten Router eingehende Pakete ohne passende bestehende Verbindung zusätzlich aktiv. Der praktische Schutz ist damit eine Kombination aus beidem – NAT allein ist trotzdem keine vollwertige Firewall und ersetzt keine bewusst konfigurierten Filterregeln. Sobald eine Portfreigabe (Destination-NAT) eingerichtet ist, wird der betreffende Dienst gezielt von außen erreichbar, sofern die Firewall den Verkehr zusätzlich zulässt.

### 3.3 Destination-NAT / Port-Forwarding

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Destination-NAT (Port-Forwarding) | Leitet eingehende Anfragen aus dem WAN gezielt an einen bestimmten internen Server weiter – das Gegenstück zu Masquerading, das ausgehenden Verkehr ermöglicht | 🔴 |

> **IHK-Typfrage:** *In welchem Szenario kann ein Unternehmen Destination-NAT (Port-Forwarding) benötigen?*
> **Musterantwort:** Typischerweise dann, wenn ein interner Dienst mit privater IPv4-Adresse von außen über die öffentliche IP-Adresse des Routers erreichbar sein soll – klassisches Beispiel ist ein selbst betriebener Webserver oder Mailserver im Firmennetz. Da die öffentliche IP-Adresse des Routers nach außen sichtbar ist, das eigentliche Zielsystem aber eine private, von außen nicht direkt adressierbare IP hat, setzt der Router eingehende Anfragen auf einem bestimmten Port gezielt auf die interne Adresse und den internen Port des Servers um (Destination-NAT). Ein per Port-Forwarding freigegebener Dienst ist damit direkt aus dem Internet erreichbar und sollte entsprechend gehärtet, aktuell gehalten und überwacht werden – die Freigabe allein macht den Dienst nicht automatisch sicher.

### 3.4 Double-NAT

🟡 **Praxis-Tipp – Double-NAT:** Wird ein eigener Router (mit eigenem NAT) an einen bereits vorhandenen Router (ebenfalls mit NAT) angeschlossen, wird derselbe Verkehr zweimal hintereinander übersetzt. Das funktioniert für normales Surfen meist, kann aber VPN-Tunnel und VoIP-Telefonie stören oder komplett verhindern, eingehende Portfreigaben verkomplizieren und Protokolle mit eingebetteten IP-Adressen durcheinanderbringen – ein bekannter Stolperstein bei Heimnetzwerken mit zusätzlichem eigenen Router hinter dem Provider-Router. Wird der vorgeschaltete Router in den Bridge-/Modem-Modus versetzt oder als reiner Access Point betrieben, lässt sich Double-NAT meist vollständig vermeiden.

---

## 4. Standortvernetzung: Standleitung, VPN und SD-WAN

> **Grundprinzip:** Sollen zwei Standorte dauerhaft miteinander verbunden werden, gibt es dafür mehrere Technologiestufen mit unterschiedlichem Verhältnis von Kosten, Sicherheit und Flexibilität.

### 4.1 Standleitung, VPN und SD-WAN im Vergleich

| Technologie | Prinzip | Vorteil | Nachteil | IHK-Relevanz |
|---|---|---|---|---|
| Leased Line (Standleitung) | Dedizierte Punkt-zu-Punkt-Verbindung mit vertraglich vereinbarten Eigenschaften zwischen zwei Standorten | Vertraglich garantierte Bandbreite, läuft nicht über das öffentliche Internet | Vergleichsweise teuer, unflexibel bei Änderungen | 🔴 |
| MPLS-VPN | Providerseitig betriebenes WAN mit logisch getrennten Kundennetzen; nutzt nicht zwingend eine physisch exklusive Leitung, Qualität/Priorität ergeben sich aus vertraglichen SLA-/QoS-Zusagen | Planbare Qualität durch SLA, oft günstiger als eine reine Standleitung | Weiterhin providerabhängig, Kosten- und Komplexitätsvorteil gegenüber Internet-VPN begrenzt | 🟡 |
| VPN über Internet | Verschlüsselter Tunnel (z. B. IPsec, WireGuard) über den normalen, günstigen Internetanschluss | Deutlich günstiger als Standleitung/MPLS | Abhängig von der Auslastung/Qualität des öffentlichen Internets, keine automatisch garantierte Ende-zu-Ende-Qualität | 🔴 |
| SD-WAN (Software-Defined WAN) | Mehrere Anschlüsse (z. B. MPLS, DOCSIS, 5G) werden von einer Software permanent auf Qualität überwacht; Verkehr wird je nach Anwendung, Qualität, Kosten und definierten Richtlinien über eine passende Leitung geroutet | Kombiniert mehrere Leitungen intelligent, kann bei Störungen automatisch umschalten (Failover) | Höhere Komplexität, ersetzt keine grundsätzlich fehlende Bandbreite | 🔴 |

> **IHK-Typfrage:** *Ein Manager möchte die teure Standleitung kündigen und stattdessen ein VPN über einen günstigen DOCSIS-Anschluss für die unternehmenskritische VoIP-Telefonie nutzen. Welche fachlichen Nachteile solltest du ansprechen?*
> **Musterantwort:** Eine Standleitung bietet in der Regel eine vertraglich zugesicherte Bandbreite, definierte Qualitätsparameter und ein SLA mit festgelegten Entstörzeiten – dadurch sind Latenz, Jitter und Paketverlust besser planbar, was für Echtzeitanwendungen wie VoIP besonders wichtig ist. Ein VPN über einen normalen Internetanschluss (insbesondere über ein Shared Medium wie DOCSIS) nutzt dagegen einen Best-Effort-Internetzugang: Latenz und verfügbare Bandbreite können sich, gerade zu Spitzenzeiten, spürbar verschlechtern. Für unternehmenskritische VoIP-Telefonie kann das zu hörbaren Aussetzern oder Verbindungsabbrüchen führen. Wichtig zur Einordnung: Ein VPN sorgt primär für Vertraulichkeit, Authentizität und Integrität der übertragenen Daten – es macht aus einem Best-Effort-Internetzugang keine Leitung mit garantierter Übertragungsqualität.

### 4.2 Site-to-Site vs. Client-to-Site VPN

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Site-to-Site VPN | Verbindet zwei Standorte dauerhaft über die jeweiligen Router/Firewalls miteinander (z. B. Zentrale ↔ Filiale) | 🔴 |
| Client-to-Site VPN | Einzelne Endgeräte (z. B. Laptops im Homeoffice oder auf Reisen) bauen bei Bedarf per VPN-Software eine Verbindung zum Firmennetz auf | 🔴 |

🟢 **Nice to know – Split-Tunneling vs. Full-Tunnel:** Startet ein Laptop im Homeoffice ein Client-to-Site-VPN, behält er typischerweise weiterhin seine Adresse im Heimnetz und erhält zusätzlich eine Adresse auf dem virtuellen VPN-Adapter. Bei Split-Tunneling gehen nur Anfragen an Firmenziele durch den Tunnel, während z. B. der Zugriff auf den heimischen Drucker weiterhin direkt über das Heim-WLAN läuft. Bei einem Full-Tunnel wird dagegen der gesamte Datenverkehr des Geräts durch den VPN-Tunnel geleitet.

### 4.3 Subnetz-Kollision beim VPN

🔴 **Stolperstein – Subnetz-Kollision beim Home-Office-VPN:** Nutzt die Firmenzentrale dasselbe IP-Subnetz wie ein typischer Heimrouter (z. B. `192.168.178.0/24`, eine verbreitete Werkseinstellung), kollidieren beide Netze beim Aufbau eines VPNs: Existiert dasselbe Präfix sowohl am lokalen Heimnetzadapter als auch am virtuellen VPN-Adapter, entstehen konkurrierende bzw. überlappende Routen in der lokalen Routing-Tabelle – der Client kann dann abhängig von Routenmetrik und VPN-Konfiguration Firmenziele fälschlich über das Heimnetz senden (z. B. weil er `192.168.178.10` für den Drucker im Wohnzimmer statt für einen Server in der Firma hält). Manche VPN-Lösungen können überlappende Netze über zusätzliche NAT-Mechanismen innerhalb des Tunnels oder Umnummerierung teilweise umgehen; die robustere und empfohlene Lösung bleibt aber eine unternehmensweit geplante, möglichst kollisionsarme Adressierung – Firmennetze sollten von vornherein IP-Bereiche verwenden, die nicht zu den verbreiteten Heimrouter-Standardnetzen gehören.

### 4.4 SD-WAN in der Praxis

🟡 **Praxis-Tipp – SD-WAN bündelt nicht automatisch einzelne Downloads:** SD-WAN überwacht mehrere WAN-Verbindungen anhand mehrerer Kriterien (u. a. Latenz, Paketverlust, Jitter, Kosten, Auslastung) und wendet abhängig von Anwendung, Qualität und definierten Richtlinien (Policies) die passende Leitung an – nicht einfach "die eine beste" Leitung pauschal für allen Verkehr. Es kann dabei mehrere Sitzungen bzw. Datenströme auf verschiedene Leitungen verteilen, was die aggregierte Gesamtkapazität erhöht – das bedeutet aber nicht automatisch, dass sich die Bandbreite für einen einzelnen, bereits laufenden Datenstrom (z. B. einen einzelnen Download) addiert: Dieser läuft in den meisten gängigen Implementierungen weiterhin über genau eine Leitung. Bei zwei 100-Mbit/s-Leitungen ergibt sich dadurch meist keine einzelne 200-Mbit/s-Downloadverbindung, sondern eher Kapazität für zwei parallele 100-Mbit/s-Verbindungen.

---

## 5. Cloud-Computing und Server-Auslagerung

> **Grundprinzip:** Server müssen nicht mehr zwingend physisch im eigenen Haus stehen – Cloud-Anbieter vermieten Rechenleistung, Plattformen oder fertige Software über das WAN, mit jeweils unterschiedlicher Verantwortungsaufteilung.

### 5.1 On-Premises, IaaS, PaaS und SaaS

| Modell | Beschreibung | Metapher | IHK-Relevanz |
|---|---|---|---|
| On-Premises | Server steht physisch im eigenen Haus, das Unternehmen ist für alles selbst verantwortlich | Pizza komplett selbst backen (Teig, Ofen, Zutaten) | 🔴 |
| IaaS (Infrastructure as a Service) | Gemieteter "nackter" virtueller Server (CPU, RAM, Storage); Betriebssystem und Anwendung verwaltet der Kunde selbst | Küche/Ofen wird gestellt, Pizza backst du selbst | 🔴 |
| PaaS (Platform as a Service) | Gemietete, fertig eingerichtete Plattform (z. B. Datenbank- oder Webserver-Umgebung); Hardware und Betriebssystem verwaltet der Anbieter, der Kunde entwickelt/konfiguriert und betreibt seine Anwendung darauf | Der Teig ist vorbereitet, den Belag bestimmst und legst du selbst auf | 🔴 |
| SaaS (Software as a Service) | Fertige Anwendung wird direkt genutzt (z. B. Microsoft 365); Anbieter verwaltet Infrastruktur, Plattform und Anwendung | Fertige Pizza wird geliefert/konsumiert | 🔴 |

### 5.2 Shared Responsibility

> **IHK-Typfrage:** *Ordne folgende Beispiele den passenden Modellen zu und begründe: ein gemietetes Microsoft-365-Postfach, ein physischer Linux-Server im eigenen Keller, eine nackte Ubuntu-VM bei einem Cloud-Anbieter.*
> **Musterantwort:** Das gemietete Microsoft-365-Postfach ist SaaS – der Anbieter betreibt Infrastruktur, Plattform und die Anwendung selbst; beim Kunden verbleiben dennoch typische Aufgaben wie Benutzerkonten, Berechtigungen, Multi-Faktor-Authentifizierung und die inhaltliche Konfiguration. Der physische Linux-Server im eigenen Keller ist On-Premises – das Unternehmen ist vollständig selbst für Hardware, Betriebssystem und Anwendung verantwortlich. Die nackte Ubuntu-VM bei einem Cloud-Anbieter ist IaaS – der Anbieter verantwortet die physische Hardware, das Rechenzentrum und die Virtualisierungsschicht, für Betriebssystem-Updates, Konfiguration und Absicherung der Anwendung darauf ist weiterhin der Kunde selbst zuständig.

🔴 **Stolperstein – "Die Cloud ist sicherer als mein Keller":** Das trifft meist auf physische Aspekte zu (Brandschutz, redundante Stromversorgung, Zutrittskontrolle) – dafür ist der Cloud-Anbieter verantwortlich. Die Sicherheit innerhalb der gemieteten Ressource (Betriebssystem-Härtung, Passwörter, Zugriffsrechte, Konfiguration von Speicherfreigaben) bleibt beim Shared-Responsibility-Modell dagegen in der Verantwortung des Kunden – ein unsicher konfiguriertes IaaS-System oder ein versehentlich öffentlich freigegebener Storage-Bucket sind trotz "sicherer Cloud" ein reales, selbst verschuldetes Risiko.

### 5.3 Cloud als Ausfallrisiko

🟡 **Praxis-Tipp – Cloud bedeutet Internetabhängigkeit:** Fällt bei einem Unternehmen, das konsequent auf Cloud-Dienste setzt, die WAN-Anbindung aus, sind in der Regel auch interne Abläufe betroffen, die man zunächst nicht mit "Internet" verbindet – etwa Dateizugriff, interne Kommunikation oder cloudbasierte Kassensysteme. Ohne redundante WAN-Anbindung (z. B. per SD-WAN mit mehreren Anschlüssen) wird die alleinige Internetverbindung damit selbst zu einem Single Point of Failure für praktisch den gesamten Betrieb.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Wann schickt ein Client ein Paket direkt, wann ans Gateway? | Direkt bei Zielen im eigenen Subnetz, ans Gateway bei Zielen in fremden Netzen |
| 2 | Was zeigt der erste sichtbare Hop bei `traceroute` häufig? | Das eigene Standard-Gateway – muss aber nicht zwingend antworten/sichtbar sein |
| 3 | Warum reicht ein einzelnes Standard-Gateway nicht mehr, wenn ein Unternehmen zwei Router mit unterschiedlichen Zielen hat? | Weil das Standard-Gateway nur eine Default Route kennt – für gezielte zusätzliche Netze braucht es statische Routen (inkl. Rückweg auf der Gegenseite) |
| 4 | Was unterscheidet FTTC von FTTH? | FTTC endet am Straßenkasten und nutzt ab dort Kupfer, FTTH führt die Glasfaser bis in die Wohnung/das Büro |
| 5 | Warum scheitert Port-Forwarding bei DS-Lite typischerweise? | Der Anschluss hat keine eigene öffentliche IPv4-Adresse mehr, sie wird per CG-NAT geteilt |
| 6 | Warum ist "NAT allein schützt uns" fachlich ungenau? | Der praktische Schutz ist eine Kombination aus NAT-Funktionsweise und der stateful Firewall – NAT allein ist keine vollwertige Firewall |
| 7 | Was ist Double-NAT, und was kann es stören? | Zwei hintereinandergeschaltete NAT-Router; kann VPN-Tunnel und VoIP-Verbindungen stören |
| 8 | Warum darf ein Firmennetz kein verbreitetes Heim-Standardnetz nutzen? | Beim VPN-Aufbau ins Homeoffice würden sich Firmen- und Heimnetz-Adressbereich überschneiden und Routing-Konflikte verursachen |
| 9 | Was unterscheidet IaaS von PaaS? | Bei IaaS verwaltet der Kunde Betriebssystem und Anwendung selbst, bei PaaS übernimmt der Anbieter zusätzlich das Betriebssystem |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Default Route | Route mit Präfixlänge `/0` (`0.0.0.0/0` bzw. `::/0`), die verwendet wird, wenn keine spezifischere Route für das Ziel vorhanden ist |
| Hop | Eine Layer-3-Weiterleitungsstation (meist ein Router) auf dem Weg eines Pakets zum Ziel – nicht jeder Hop ist zwingend in `traceroute` sichtbar |
| FTTC/FTTB/FTTH | Glasfaser bis Straßenkasten / bis Gebäude / bis in die Wohnung |
| Dual-Stack | Anschluss mit nativer IPv4-Konnektivität und einem öffentlich routbaren IPv6-Präfix |
| DS-Lite / CG-NAT | Anschluss nur mit öffentlichem IPv6-Präfix, IPv4 läuft per AFTR-Tunnel über geteilte CG-NAT-Adressen des Providers |
| Masquerading (Source-NAT) / PAT | Übersetzt private Absender-IP (und bei geteilter Adresse zusätzlich den Quellport) in die öffentliche Router-IP für ausgehenden Verkehr |
| Destination-NAT (Port-Forwarding) | Leitet eingehenden Verkehr gezielt an einen internen Server weiter |
| NAT ≠ Firewall | NAT übersetzt Adressen; der praktische Schutz vor unaufgefordertem WAN-Verkehr ist eine Kombination aus NAT-Funktionsweise und stateful Firewall – NAT allein ersetzt keine Firewall |
| Site-to-Site vs. Client-to-Site VPN | Standort-zu-Standort-Kopplung vs. einzelnes Endgerät verbindet sich bei Bedarf |
| SD-WAN | Software steuert mehrere WAN-Leitungen nach Qualität/Kosten/Policy, ersetzt aber keine fehlende Bandbreite pro Einzelverbindung |
| IaaS/PaaS/SaaS | Nackte VM (Kunde verwaltet OS+App) / verwaltete Plattform (Kunde verwaltet Anwendungscode/-daten) / fertige Anwendung (Anbieter verwaltet Infrastruktur+Plattform+App) |
| Shared Responsibility | Anbieter sichert die von ihm betriebene Infrastruktur/Plattform/Anwendung ab; Kunde bleibt je nach Modell für Daten, Identitäten, Berechtigungen, Endgeräte und sichere Konfiguration verantwortlich |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Routing-Entscheidung begründen | "Warum direkt/über Gateway?" | "PC mit IP X sendet an Ziel Y – Gateway nötig?" | Subnetzmaske gegen Ziel-IP prüfen, dann Antwort begründen |
| WAN-Technologie einordnen | "Welche Technologie/Ausbaustufe liegt vor?" | "Anbieter bewirbt 'Glasfaser', liefert aber FTTC." | Unterscheidung zwischen beworbenem Namen und tatsächlicher physischer Reichweite |
| NAT-Konzept anwenden | "Was macht der Router bei ausgehendem/eingehendem Verkehr?" | "Mitarbeiter ruft Webseite auf – was passiert am Router?" | Source-NAT (ausgehend) von Destination-NAT (eingehend) sauber trennen |
| Standortvernetzung bewerten | "Welche Technologie für Szenario X?" | "VoIP-kritische Standleitung vs. günstiges VPN." | Bandbreiten-/Latenzgarantie als Kernkriterium nennen, nicht nur Kosten |
| Cloud-Modell zuordnen | "Welches Modell liegt vor, wer ist wofür verantwortlich?" | "Gemietete Ubuntu-VM bei einem Cloud-Anbieter." | Modell korrekt benennen UND die Verantwortungsgrenze (Shared Responsibility) erklären |

---

## Merk-Sätze fürs Fachgespräch

> Jeder Client entscheidet selbst: Ziel im eigenen Subnetz geht direkt über den Switch, alles andere geht über die Default Route zum Standard-Gateway.

> "Glasfaser" im Vertrag heißt nicht automatisch Glasfaser bis zur Steckdose – erst FTTH führt die Faser wirklich bis ins Büro.

> DS-Lite bedeutet: keine eigene öffentliche IPv4-Adresse mehr, dafür geteiltes CG-NAT beim Provider – klassischer Stolperstein für eingehende Verbindungen.

> NAT spart Adressen, die Firewall filtert gezielt – der praktische Schutz vor unaufgefordertem WAN-Verkehr entsteht erst im Zusammenspiel beider Mechanismen, nicht durch NAT allein.

> Ein Firmennetz im selben Adressbereich wie ein typischer Heimrouter kann beim VPN zu schwer nachvollziehbaren Routing-Konflikten führen – deshalb gehören Firmennetze in unverbrauchte IP-Bereiche.

> Ein erfolgreicher Ping beweist Erreichbarkeit für das getestete Ziel und Protokoll – nicht automatisch die vollständige Funktionsfähigkeit aller Netzwerkdienste.

> Ein VPN schützt die übertragenen Daten (Vertraulichkeit, Integrität, Authentizität) – es garantiert aber weder Bandbreite noch niedrige Latenz oder geringen Jitter.

---

```yaml
lernfeld: LF3.5
titel: Standortvernetzung (WAN & Routing)
status: final
stand: 2026-09-04
review: fachliche Praezisierungen in zwei Runden eingearbeitet (ARP/NDP, NAT-vs-Firewall-Nuance, Leased-Line/MPLS-Trennung, Pizza-Metapher/Shared-Responsibility, Subnetz-Kollision/Traceroute-Formulierungen, PAT/NAPT bei Masquerading, DS-Lite/Dual-Stack-IPv6-Praefix-Terminologie, Ping-Aussage eingeschraenkt, Gateway-Stolperstein/Destination-NAT-Frage entschaerft, Standleitung als SLA statt Exklusivitaet, SD-WAN-Kapazitaet vs. Einzelstrom)
quellen:
  - LF3.5- Standortvernetzung (WAN & Routing)
  - LF3.5.1- Routing am Client (Linux & Windows)
  - LF3.5.2- WAN-Zugang & Provider-Strategien
  - LF3.5.3- Routing, NAT & Firewall (Die Sandbox)
  - LF3.5.4- Standortvernetzung
  - LF3.5.5- Cloud-Computing und Server-Auslagerung
```