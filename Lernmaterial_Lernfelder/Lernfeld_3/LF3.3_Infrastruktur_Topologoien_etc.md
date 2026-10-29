# LF3.3 – Infrastruktur (Topologien, Übertragungsmedien & Strukturierte Verkabelung)

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 90–110 Min., mit Vertiefung (Vollvermaschungs-Berechnung, Schirmungsklassen, Rack-Planung): 130–150 Min.
> **Status:** Final
> **Stand:** 2026-09-02

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Warum ist die Stern-Topologie trotz ihres Single Point of Failure der weltweite LAN-Standard? | [1.1](#11-klassische-topologien-im-überblick) |
| 2 | Wie lässt sich der Unterschied zwischen physischer und logischer Topologie am Beispiel Token Ring erklären? | [1.2](#12-physische-vs-logische-topologie) |
| 3 | Was verursacht Übersprechen (Crosstalk), und wie schützt sich ein Twisted-Pair-Kabel dagegen? | [2.2](#22-physikalische-störfaktoren) |
| 4 | Warum liegt die Grenze für Kupfer-Verkabelung bei 100 Metern, und was zählt alles dazu? | [2.3](#23-duplex--die-100-meter-regel) |
| 5 | Was unterscheidet einen Unmanaged- von einem Managed-Switch fachlich – nicht nur im Preis? | [3.2](#32-aktive-und-passive-komponenten) |

---

## 1. Netzwerktopologien

> **Grundprinzip:** Die Topologie beschreibt die geometrische Anordnung von Geräten und Kabeln. Dabei wird zwischen physischer Topologie (wie liegen die Kabel tatsächlich?) und logischer Topologie (wie fließen die Daten?) unterschieden – beide müssen nicht übereinstimmen.

### 1.1 Klassische Topologien im Überblick

| Topologie | Kurzbeschreibung | Ausfallsicherheit | IHK-Relevanz |
|---|---|---|---|
| Bus | Alle Geräte hängen an einem gemeinsamen Hauptkabel, ohne zentralen Verteiler (historisch, z. B. 10Base2 mit Koaxialkabel) | Sehr gering – ein Kabelbruch legt das gesamte Segment lahm | 🟡 |
| Ring | Jedes Gerät ist mit genau zwei Nachbarn verbunden, Signale laufen im Kreis | Gering – ein Ausfall unterbricht den Ring (außer bei redundanten Doppel-Ring-Systemen) | 🟡 |
| Stern | Alle Geräte sind einzeln mit einem zentralen Verteiler (Switch) verbunden | Hoch für einzelne Endgeräte, aber der zentrale Verteiler ist ein Single Point of Failure | 🔴 |
| Mesh (vermascht) | Jedes Gerät ist mit jedem anderen (Vollvermaschung) oder mit mehreren anderen (Teilvermaschung) direkt verbunden | Sehr hoch – es existieren Ausweichrouten, dafür hoher Verkabelungsaufwand | 🔴 |
| Baum | Mehrere Stern-Topologien werden hierarchisch verbunden (z. B. Etagen-Switches an einem Gebäude-Switch) | Hoch, typische Struktur für strukturierte Verkabelung in Gebäuden | 🔴 |

> **IHK-Typfrage:** *Warum ist die Stern-Topologie heute der weltweite LAN-Standard, obwohl ein zentraler Switch-Ausfall das gesamte Netz lahmlegen kann?*
> **Musterantwort:** Der entscheidende Vorteil gegenüber Bus und Ring ist die Fehlerisolation: Fällt bei einer Stern-Topologie ein einzelnes Kabel oder Endgerät aus, sind ausschließlich dieses eine Gerät betroffen, der Rest des Netzes läuft unbeeinträchtigt weiter. Bei Bus oder Ring legt dagegen bereits ein einzelner Kabelbruch potenziell das gesamte Segment lahm. Der verbleibende Single Point of Failure (der zentrale Switch) lässt sich zudem gezielt absichern – z. B. durch redundante Switches oder eine unterbrechungsfreie Stromversorgung (USV) – während sich ein verteilter Bus praktisch nicht auf diese Weise absichern lässt.

🔴 **Stolperstein – Fehlender Terminator (Bus):** Fehlt bei einer Bus-Topologie der Abschlusswiderstand (Terminator), wird das Signal am offenen Kabelende reflektiert und stört die gesamte Kommunikation auf dem Segment – heute in modernen Netzen praktisch nicht mehr relevant, taucht aber in Prüfungsfragen zu Legacy-Systemen auf.

🔴 **Stolperstein – Die Switch-Schleife (Loop):** Bestehen zwischen zwei oder mehr Switches mehrere gleichzeitige Layer-2-Wege – etwa weil versehentlich zwei Ports desselben oder zweier verbundener Switches miteinander verkabelt werden – entsteht eine Schleife: Broadcast-Frames zirkulieren endlos (Broadcast Storm) und können das Netzwerk innerhalb von Sekunden überlasten. Managed Switches können redundante Pfade über das Spanning Tree Protocol (STP/RSTP) erkennen und einen davon gezielt blockieren – das setzt aber voraus, dass STP auf dem Gerät überhaupt verfügbar UND aktiviert ist. Einfache Unmanaged Switches bieten diesen Schutz in der Regel gar nicht.

🟡 **Praxis-Tipp – Mesh ist nicht gleich Mesh:** Im WLAN-Consumer-Bereich wird "Mesh" oft als Marketingbegriff für Repeater-Systeme verwendet. Ein Netzwerk-Mesh im eigentlichen Sinn benötigt redundante, unabhängige Verbindungen zwischen den Knotenpunkten – ein einzelner Repeater in Reihe erfüllt dieses Kriterium nicht.

### 1.2 Physische vs. logische Topologie

> **IHK-Typfrage:** *Ein altes Token-Ring-Netzwerk war physisch als Stern verkabelt (alle Kabel liefen zu einem zentralen Verteilerkasten), logisch flossen die Daten aber im Kreis. Wie erklärst du diesen Unterschied?*
> **Musterantwort:** Die physische Topologie beschreibt, wie die Kabel tatsächlich im Raum verlegt sind – beim Token Ring liefen alle Kabel sternförmig zu einem zentralen Verteiler (MAU), rein optisch also eine Stern-Verkabelung. Die logische Topologie beschreibt dagegen, wie die Daten tatsächlich fließen: Innerhalb des Verteilers wurden die Signale intern so weitergeschaltet, dass sie weiterhin von Gerät zu Gerät im Kreis liefen, wie bei einem klassischen Ring. Ein Gerät gab das Datenpaket (Token) also logisch an seinen Nachbarn weiter, obwohl physisch alle Kabel im selben Schrank zusammenliefen.

🟡 **Praxis-Tipp – Hub vs. Switch:** Ein altes Hub-basiertes Netz zeigt dasselbe Prinzip umgekehrt: physisch liegt eine Stern-Verkabelung vor, logisch verhält sich das Netz aber wie ein Bus, da ein Hub jedes eingehende Signal ungefiltert an alle anderen Ports weiterleitet (Shared Medium) – alle angeschlossenen Geräte teilen sich dieselbe Kollisionsdomäne. Ein Switch dagegen lernt, welche MAC-Adresse an welchem Port hängt, und leitet Frames gezielt nur an den passenden Port weiter.

🟢 **Nice to know – Vollvermaschung rechnen:** Für eine vollvermaschte Verbindung von *n* Geräten werden `n · (n-1) / 2` Kabel benötigt. Bei 10 Computern wären das bereits 45 Kabel – der Aufwand wächst quadratisch mit der Geräteanzahl. Deshalb wird Vollvermaschung im lokalen LAN praktisch nie eingesetzt, sondern eher im WAN/Internet-Backbone oder als Teilvermaschung zwischen wenigen zentralen Switches.

---

## 2. Übertragungsmedien und Leitungselektrik

> **Grundprinzip:** Jedes Übertragungsmedium hat physikalische Grenzen bei Reichweite, Bandbreite und Störanfälligkeit – die Wahl des richtigen Mediums hängt von Umgebung (Störquellen), Distanz und benötigter Bandbreite ab.

### 2.1 Kupfer, Koax und Glasfaser im Vergleich

| Medium | Signal | Typischer Einsatz | Reichweite pro Segment | IHK-Relevanz |
|---|---|---|---|---|
| Twisted-Pair (Kupfer) | Elektrisch, über verdrillte Adernpaare | LAN (Büro, Heimnetzwerk) | Nach Verkabelungsnorm auf 100 m begrenzt (siehe 2.3) | 🔴 |
| Koaxialkabel (Kupfer) | Elektrisch, über massiven Kupferkern mit Schirmgeflecht | Heute im LAN kaum noch üblich, aber weiterhin relevant bei TV- und Kabelinternetnetzen wie DOCSIS | Je nach Anwendung deutlich länger als Twisted-Pair, bei DOCSIS durch aktive Verstärker im Netz zusätzlich verlängerbar | 🟡 |
| Glasfaser (LWL) | Lichtimpulse (LED/Laser) | Backbone, MAN/WAN, Rechenzentrum, zunehmend auch Gebäudeverbindungen | Multimode (OM3/OM4) typischerweise einige Hundert Meter, Singlemode (OS1/OS2) von mehreren Kilometern bis zu mehreren zehn Kilometern – abhängig von der eingesetzten Sender-/Empfänger-Technik | 🔴 |

> **IHK-Typfrage:** *Ihr müsst ein Netzwerkkabel durch einen Aufzugsschacht direkt neben Starkstromkabeln und großen Motoren verlegen. Welches Übertragungsmedium wählt ihr, und warum scheitert hier ein ungeschirmtes U/UTP-Kabel?*
> **Musterantwort:** In unmittelbarer Nähe starker elektromagnetischer Störquellen (Motoren, Starkstrom) ist ein ungeschirmtes Kupferkabel (U/UTP) ungeeignet, da die Adernpaare elektrische Signale führen und dadurch besonders anfällig für Interferenz (EMI) von außen sind. Sinnvoller ist entweder ein geschirmtes Kupferkabel mit Gesamt- und Aderpaarschirm (z. B. S/FTP) oder – bei besonders starken Störquellen bzw. größerer Distanz – Glasfaser, da Lichtsignale grundsätzlich unempfindlich gegenüber elektromagnetischen Störungen sind.

🟢 **Nice to know – Schirmungskürzel entschlüsselt:** Die Bezeichnung folgt dem Schema `[Gesamtschirm]/[Aderpaarschirm]TP`. `U/UTP` bedeutet: kein Gesamtschirm (U = unshielded), keine Schirmung der einzelnen Aderpaare. `S/FTP` bedeutet: Gesamtschirm als Geflecht (S = braided screen), zusätzlich jedes Aderpaar einzeln foliengeschirmt (F = foil). Mehr Schirmungsebenen verbessern den Schutz gegen EMI aber nur dann zuverlässig, wenn der Schirm über durchgängig geeignete geschirmte Komponenten (Dosen, Patchpanels, Stecker) und einen fachgerechten Potentialausgleich lückenlos verbunden ist – eine unsachgemäß geerdete oder unterbrochene Schirmung kann den Nutzen sogar zunichtemachen oder neue Störungen einbringen.

### 2.2 Physikalische Störfaktoren

| Störfaktor | Beschreibung | Gegenmaßnahme | IHK-Relevanz |
|---|---|---|---|
| Dämpfung (Attenuation) | Das Signal wird mit zunehmender Kabellänge schwächer | Maximale Segmentlänge einhalten, ggf. Repeater/Switches einsetzen | 🔴 |
| Interferenz (EMI) | Elektromagnetische Störungen von außen (Motoren, Starkstrom, Leuchtstoffröhren) verfälschen das elektrische Signal | Schirmung (Folie/Geflecht) oder Wechsel auf Glasfaser | 🔴 |
| Übersprechen (Crosstalk/NEXT) | Die Magnetfelder benachbarter Adernpaare im selben Kabel stören sich gegenseitig | Verdrillung (Twisting) der Adernpaare | 🔴 |

🔴 **Stolperstein – Knick im Kabel:** Ein scharf geknicktes Glasfaserkabel bricht intern und fällt in der Regel vollständig aus. Bei einem geknickten Kupferkabel verändert sich dagegen die Geometrie der Verdrillung – der Schutz gegen Übersprechen geht an dieser Stelle verloren, ohne dass die Verbindung zwangsläufig komplett ausfällt; typischerweise sinkt die erreichbare Bandbreite oder es treten sporadische Übertragungsfehler auf.

🟡 **Praxis-Tipp – Auflegen ohne "Detwisting":** Die Adernpaare sind mit unterschiedlichen, genormten Schlaglängen verdrillt. Beim Auflegen auf Dose oder Patchpanel darf die Verdrillung nur so weit wie unbedingt nötig (nach Norm meist wenige Millimeter) aufgelöst werden – wird deutlich mehr Verdrillung entfernt, verschlechtern sich die Übersprechwerte an genau dieser Stelle spürbar.

### 2.3 Duplex & die 100-Meter-Regel

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Half-Duplex | Es kann zu einem Zeitpunkt nur gesendet oder empfangen werden (wie Walkie-Talkie); senden zwei gleichzeitig, entsteht eine Kollision | 🔴 |
| Full-Duplex | Senden und Empfangen sind gleichzeitig möglich (wie Telefonieren), Standard bei modernen Switch-Verbindungen; die konkrete technische Umsetzung (z. B. getrennte Adernpaare oder gemeinsame Nutzung) hängt von der jeweiligen Ethernet-Variante ab | 🔴 |
| 100-Meter-Grenze | Nach gängigen Verkabelungsnormen (u. a. EIA/TIA-568 in den USA, EN 50173 / ISO/IEC 11801 international) gilt für ein komplettes Kupfer-Segment ("Channel") eine Grenze von 100 m; die konkrete nutzbare Länge hängt zusätzlich von Kabelkategorie, Temperatur und Übertragungsparametern ab | 🔴 |

> **IHK-Typfrage:** *Warum liegt die Kupfer-Grenze bei 100 Metern, und was zählt konkret dazu?*
> **Musterantwort:** Die 100-Meter-Grenze gilt für das gesamte Segment (den "Channel") zwischen zwei aktiven Geräten, nicht nur für ein einzelnes Kabelstück. Sie setzt sich zusammen aus dem starren Verlegekabel in der Wand (dem "Permanent Link", nach Norm maximal 90 m) plus den flexiblen Patchkabeln an beiden Enden – am Schreibtisch und im Verteilerschrank – die zusammen maximal 10 m ausmachen dürfen. Wird diese Gesamtlänge überschritten, macht sich das durch zunehmende Dämpfung und potenzielle Übertragungsfehler bemerkbar; die exakt nutzbare Länge hängt außerdem von Kabelkategorie und Umgebungsbedingungen ab.

🔴 **Stolperstein – Duplex-Mismatch:** Wird an einem Switchport Geschwindigkeit und Duplex-Modus manuell fest eingestellt, während die Gegenseite auf automatische Aushandlung (Autonegotiation) steht, kommt es häufig zu einem fehlerhaften Half-Duplex-Rückfall auf einer Seite – erkennbar an massiven Paketverlusten und starker Verzögerung trotz augenscheinlich passender Geschwindigkeitsanzeige. Ursache und Symptom sind so charakteristisch, dass "beide Seiten auf Autonegotiation belassen" als erste Prüfempfehlung gilt. Ist eine manuelle Festlegung nötig (z. B. aus betrieblichen Gründen), sollte sie konsequent auf beiden Seiten der Verbindung identisch gesetzt werden.

---

## 3. Strukturierte Verkabelung und Komponenten

> **Grundprinzip:** Strukturierte Verkabelung unterteilt ein Gebäude bzw. Firmengelände in klar abgegrenzte Bereiche, damit Verkabelung, Verteiler und Übertragungsmedien systematisch und normgerecht geplant werden können, statt Kabel unstrukturiert querbeet zu verlegen.

### 3.1 Primär-, Sekundär- und Tertiärbereich

| Bereich | Verbindet | Typisches Medium | IHK-Relevanz |
|---|---|---|---|
| Primärbereich | Gebäude untereinander auf einem Firmengelände (Campus-Backbone) | Glasfaser (größere Distanzen, störungsunempfindlich) | 🔴 |
| Sekundärbereich | Hauptverteiler (MDF) mit den Etagenverteilern (IDF) innerhalb eines Gebäudes | Typischerweise Glasfaser; bei kurzen Strecken innerhalb der 100-Meter-Grenze und geeigneter Umgebung ist auch hochwertiges geschirmtes Kupfer möglich | 🔴 |
| Tertiärbereich | Etagenverteiler (IDF) mit der Anschlussdose am Arbeitsplatz (horizontale Verkabelung) | Twisted-Pair-Kupfer, wegen der 100-Meter-Grenze meist ausreichend | 🔴 |

> **IHK-Typfrage:** *Ordnet für euer Szenario-Unternehmen jeder Zone der strukturierten Verkabelung das passende Übertragungsmedium zu und begründet.*
> **Musterantwort:** Im Primärbereich (Verbindung mehrerer Gebäude) sind die Distanzen für Kupfer meist zu groß und die Umgebung häufig störanfällig, deshalb wird hier typischerweise Glasfaser eingesetzt. Im Sekundärbereich (Hauptverteiler zu Etagenverteilern) ist Glasfaser die typische Lösung; nur bei kurzen Strecken innerhalb der 100-Meter-Grenze und einer geeigneten, wenig störbelasteten Umgebung kommt auch geschirmtes Kupfer infrage. Im Tertiärbereich (letzte Etappe zum Arbeitsplatz) reicht die Kupfer-Distanz von deutlich unter 100 m in der Regel aus, weshalb hier meist kostengünstigeres Twisted-Pair-Kabel verwendet wird.

### 3.2 Aktive und passive Komponenten

| Komponente | Layer | Beschreibung | IHK-Relevanz |
|---|---|---|---|
| Patchpanel / Dose | Layer 1 (passiv) | Fixiert und terminiert das starre Verlegekabel aus der Wand – rein passiv: regeneriert oder analysiert keine Signale/Frames und besitzt keine eigene MAC-Adresstabelle | 🔴 |
| Unmanaged Switch | Layer 2 | Einfacher "Plug & Play"-Verteiler ohne Konfigurationsmöglichkeit, typisch für den Heimgebrauch | 🔴 |
| Managed Switch | Layer 2, optional zusätzlich Layer-3-Funktionen (Routing) | Konfigurierbarer Enterprise-Verteiler mit eigener Verwaltungsoberfläche: einzelne Ports abschalten, VLANs einrichten, Port-Security aktivieren, PoE-Stromverbrauch steuern und überwachen. "Managed" bedeutet dabei nicht automatisch Layer 3 – ein Managed Switch kann ein reiner Layer-2-Switch mit Zusatzfunktionen sein oder zusätzlich routen können | 🔴 |
| Router/Gateway | Layer 3(+) | Verbindet unterschiedliche Netze miteinander (z. B. internes LAN mit dem Internet); in kleineren Umgebungen häufig mit Firewall- und NAT-Funktion kombiniert | 🔴 |

> **IHK-Typfrage:** *Was unterscheidet einen Unmanaged- von einem Managed-Switch fachlich – nicht nur im Preis?*
> **Musterantwort:** Ein Unmanaged Switch arbeitet grundsätzlich automatisch auf Layer 2: Er lernt, welche MAC-Adresse an welchem Port hängt, und leitet Frames möglichst gezielt an den passenden Port weiter – unbekannte Unicast-Ziele sowie Broadcast- und Multicast-Frames werden dabei geflutet, also an alle Ports außer dem Eingangsport gesendet. Konfigurationsmöglichkeiten oder Diagnosefunktionen bietet er aber nicht – er wird angeschlossen und läuft, ohne dass ein Administrator eingreifen kann. Ein Managed Switch besitzt dagegen eine eigene Verwaltungsoberfläche (Web-GUI, CLI oder beides), über die sich einzelne Ports gezielt deaktivieren, Netzwerke per VLAN voneinander trennen, der Zugriff per Port-Security auf bestimmte MAC-Adressen beschränken und der Stromverbrauch angeschlossener PoE-Geräte auslesen und steuern lässt. Für kleine Heimnetze reicht ein Unmanaged Switch meist aus, in Unternehmensnetzwerken sind die Verwaltungs- und Sicherheitsfunktionen eines Managed Switch dagegen in der Regel notwendig.

> **IHK-Typfrage:** *Warum kann ein einfacher Switch kein Routing zwischen zwei IP-Netzen übernehmen, ein Router aber schon?*
> **Musterantwort:** Ein klassischer Switch arbeitet auf Layer 2 und trifft seine Weiterleitungsentscheidung ausschließlich anhand von MAC-Adressen innerhalb eines einzigen Netzsegments – er kennt IP-Adressen und Subnetze gar nicht. Ein Router arbeitet auf Layer 3 und trifft seine Entscheidung anhand von IP-Adressen und einer Routing-Tabelle, wodurch er Pakete gezielt zwischen unterschiedlichen Netzen weiterleiten kann. Ein Managed Switch mit zusätzlichen Layer-3-Funktionen bildet hier eine Zwischenstufe: Er kann VLANs intern zwar routen, ersetzt aber nicht zwangsläufig einen vollwertigen Router an der Netzgrenze.

🟡 **Praxis-Tipp – VLANs als logische Trennung ohne neue Kabel:** Ein Managed Switch kann seine physischen Ports per VLAN (Virtual LAN) logisch in mehrere getrennte Netze aufteilen, ohne dass dafür zusätzliche Verkabelung nötig ist – z. B. ein VLAN für Mitarbeiter-PCs und ein separates VLAN für Gäste-WLAN am selben Switch. Die genaue Funktionsweise (Tagging, Trunking) ist Thema des WLAN/VLAN-Kapitels (LF3.4); für LF3.3 reicht das Verständnis, dass VLANs eine rein logische, softwareseitige Trennung sind und nichts an der physischen Stern-Verkabelung ändern.

| PoE-Standard | Leistung am Switchport (PSE) | Leistung am Endgerät (PD) | Typischer Einsatz | IHK-Relevanz |
|---|---|---|---|---|
| IEEE 802.3af (PoE) | ca. 15,4 W | ca. 12,95 W | IP-Telefone, einfache Access Points | 🟡 |
| IEEE 802.3at (PoE+) | ca. 30 W | ca. 25,5 W | Leistungsfähigere Access Points, PTZ-Kameras | 🟡 |
| IEEE 802.3bt Type 3 | ca. 60 W | ca. 51 W | Geräte mit höherem Strombedarf | 🟢 |
| IEEE 802.3bt Type 4 (PoE++) | ca. 90–100 W | ca. 71–90 W | Geräte mit hohem Strombedarf, z. B. manche Thin Clients oder Displays | 🟢 |

🟡 **Praxis-Tipp – PSE vs. PD nicht verwechseln:** Die am Switchport bereitgestellte Leistung (PSE = Power Sourcing Equipment) ist immer höher als die am Endgerät tatsächlich ankommende Leistung (PD = Powered Device), da auf dem Kabel selbst Verluste auftreten. Wird in einer Aufgabe oder Datenblatt-Angabe nicht klar zwischen beiden unterschieden, lohnt sich beim PoE-Budget immer die Rückfrage, welcher der beiden Werte gemeint ist.

🟡 **Praxis-Tipp – PoE-Budget im Blick behalten:** Jeder PoE-fähige Switch hat ein begrenztes Gesamt-Leistungsbudget für alle Ports zusammen, nicht nur ein Limit pro Port. Werden mehr PoE-Geräte angeschlossen, als das Gesamtbudget hergibt, schaltet der Switch einzelne Ports ab oder verweigert ihnen die Stromversorgung – bei der Planung (z. B. für mehrere Access Points oder IP-Kameras) muss deshalb immer die Summe aller angeschlossenen Geräte gegen das Switch-Gesamtbudget geprüft werden, nicht nur der Bedarf des einzelnen Geräts.

🔴 **Stolperstein – Kabel-Spaghetti im Rack:** Werden Patchkabel ohne Kabelmanagement kreuz und quer vom Patchpanel zum Switch geführt, wird der Schaltschrank nach kurzer Zeit unübersichtlich – ein einzelner Switch-Tausch kann dann versehentlich weitere, äußerlich unbeteiligte Verbindungen unterbrechen. Sauberes Kabelmanagement ist deshalb keine Kosmetik, sondern reduziert das Risiko ungeplanter Ausfälle bei Wartungsarbeiten.

🟡 **Praxis-Tipp – Port-Security kann nach hinten losgehen:** Wird Port-Security zu strikt konfiguriert (z. B. exakt eine feste MAC-Adresse pro Port ohne Ausnahme), sperrt sie sich bei jedem Geräte- oder Laptop-Tausch selbst aus – etwa wenn ein Kollege ein neues Gerät bekommt oder kurzzeitig ein Diagnosegerät angeschlossen werden soll. Die Konfiguration sollte deshalb administrative Prozesse für geplante Änderungen mitdenken.

🟢 **Nice to know – Green IT im Rack:** Der Standard Energy Efficient Ethernet (IEEE 802.3az) senkt den Stromverbrauch, indem ein Port bei geringer oder fehlender Auslastung in einen energiesparenden "Low Power Idle"-Zustand wechselt, statt dauerhaft mit voller Sendeleistung zu laufen – ein Baustein von "Green IT"-Konzepten neben effizienter Hardware-Auswahl und bedarfsgerechter Kühlung im Serverraum.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Was unterscheidet die physische von der logischen Topologie? | Die physische Topologie beschreibt die tatsächliche Kabelführung, die logische Topologie den tatsächlichen Datenfluss – beide können voneinander abweichen (z. B. Token Ring) |
| 2 | Warum ist die Stern-Topologie trotz SPOF Standard? | Weil ein Kabel-/Geräteausfall nur das jeweils betroffene Gerät trifft, nicht das ganze Netz, und der zentrale Switch gezielt abgesichert werden kann |
| 3 | Wie viele Kabel braucht eine Vollvermaschung von 10 Geräten? | 45 (`10 · 9 / 2`) |
| 4 | Was verursacht Übersprechen (Crosstalk), und was hilft dagegen? | Sich gegenseitig störende Magnetfelder benachbarter Adernpaare; Gegenmaßnahme ist die Verdrillung |
| 5 | Woraus setzt sich die 100-Meter-Grenze bei Kupfer zusammen? | Max. 90 m starres Verlegekabel plus max. 10 m Patchkabel an beiden Enden zusammen |
| 6 | Wann kommt eher Glasfaser statt Kupfer zum Einsatz? | Bei großen Distanzen und/oder starken elektromagnetischen Störquellen |
| 7 | Was kann ein Managed Switch, was ein Unmanaged Switch nicht kann? | U. a. VLANs einrichten, Ports abschalten, Port-Security aktivieren, PoE steuern/überwachen |
| 8 | Welchem Bereich der strukturierten Verkabelung entspricht die Verbindung vom Etagenverteiler zur Dose am Arbeitsplatz? | Tertiärbereich (horizontale Verkabelung) |
| 9 | Was verursacht typischerweise einen Duplex-Mismatch? | Eine Seite mit fest eingestelltem Duplex-Modus, die andere auf Autonegotiation |
| 10 | Warum kann ein einfacher Switch nicht zwischen zwei IP-Netzen routen? | Er arbeitet auf Layer 2 und kennt nur MAC-Adressen, keine IP-Adressen/Routing-Tabelle |
| 11 | Was begrenzt bei PoE die Anzahl anschließbarer Geräte an einem Switch? | Das Gesamt-Leistungsbudget des Switches, nicht nur das Limit pro Port |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Bus / Ring / Stern / Mesh / Baum | Klassische Netzwerktopologien mit stark unterschiedlicher Ausfallsicherheit |
| SPOF | Single Point of Failure – die eine Komponente, deren Ausfall das ganze System lahmlegt |
| Physisch vs. logisch (Topologie) | Physisch = tatsächliche Kabelführung, logisch = tatsächlicher Datenfluss |
| Dämpfung | Signalschwächung mit zunehmender Kabellänge |
| Interferenz (EMI) | Elektromagnetische Störung von außen, Gegenmaßnahme: Schirmung |
| Übersprechen (Crosstalk) | Störung benachbarter Adernpaare, Gegenmaßnahme: Verdrillung |
| 100-Meter-Grenze (Channel) | Typisch: bis zu 90 m Permanent Link plus insgesamt bis zu 10 m Anschluss-/Patchkabel |
| Primär / Sekundär / Tertiär | Campus-Backbone / Gebäude-Backbone (MDF↔IDF) / horizontale Verkabelung zum Arbeitsplatz |
| Unmanaged vs. Managed Switch | Ohne vs. mit Konfigurationsoberfläche (VLAN, Port-Security, PoE-Steuerung) |
| Duplex-Mismatch | Fehlkonfiguration durch feste Einstellung auf einer Seite, Autonegotiation auf der anderen |
| VLAN | Logische Netztrennung auf einem Managed Switch ohne zusätzliche Verkabelung (Details in LF3.4) |
| PoE (802.3af/at/bt) | Stromversorgung über das Netzwerkkabel; Leistungsklassen ca. 15,4 W / 30 W / 60–90 W, begrenzt durch das Gesamtbudget des Switches |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Topologie begründen | "Welche Topologie eignet sich für Szenario X, und warum nicht Y?" | "Warum keine Bus-Topologie für die neue Firmenzentrale?" | Konkreter Bezug auf Ausfallsicherheit/SPOF, nicht nur "ist moderner" |
| Medium auswählen | "Welches Übertragungsmedium für Umgebung X?" | "Kabelverlegung neben Starkstrom in der Lagerhalle." | Bezug auf konkreten Störfaktor (EMI) und passende Gegenmaßnahme (Schirmung/Glasfaser) |
| Grenzwert erklären | "Warum genau 100 m bei Kupfer?" | "Warum scheitert eine direkte 150-m-Kupferverbindung?" | Zusammensetzung der 100 m (90+10) nennen, nicht nur die Zahl |
| Komponente einordnen | "Wo im Netzplan gehört Komponente X hin, und was kann sie?" | "Unmanaged vs. Managed Switch am Empfang." | Konkrete Funktionsunterschiede (VLAN, Port-Security, PoE) statt nur "einer ist teurer" |

---

## Merk-Sätze fürs Fachgespräch

> Eine Stern-Topologie tauscht viele kleine Ausfallrisiken gegen ein einziges, gezielt absicherbares Risiko – den zentralen Switch.

> Physische und logische Topologie sind zwei unterschiedliche Fragen: "Wie liegen die Kabel?" ist nicht dasselbe wie "Wie fließen die Daten?".

> Dämpfung schwächt das Signal über die Distanz, Interferenz stört von außen, Übersprechen stört von innen – drei verschiedene Probleme mit drei verschiedenen Gegenmaßnahmen.

> Die 100-Meter-Grenze ist kein Kabelmaß, sondern ein Segmentmaß: Verlegekabel plus alle Patchkabel an beiden Enden zusammen.

> Ein Managed Switch unterscheidet sich von einem Unmanaged Switch nicht durch mehr Kabel, sondern durch eine Verwaltungsoberfläche für VLANs, Port-Security und PoE.

---

```yaml
lernfeld: LF3.3
titel: Infrastruktur (Topologien, Übertragungsmedien & Strukturierte Verkabelung)
status: final
stand: 2026-09-02
review: fachliche Praezisierungen in zwei Runden eingearbeitet (100-m-Regel/Normen als typischer Channel, Sekundaerbereich, Full-Duplex, Switch-Loop/STP, Uebersprechen/Detwisting, Schirmung/durchgaengige Erdung, Managed-Switch-Layer3, Patchpanel, PoE PSE/PD-Unterscheidung, 802.3az Low-Power-Idle, Glasfaser-Reichweiten vereinfacht, Unmanaged-Switch-Flooding, DOCSIS gekuerzt); ergaenzt um PoE-Standards, VLAN-Kurzeinordnung, Layer-Typfrage
quellen:
  - LF3.3 Strukturierte Verkabelung & Netzwerktopologien
  - LF3.3.1- Netzwerktopologien
  - LF3.3.2- Übertragungsmedien und Leitungselektrik
  - LF3.3.3- Strukturierte Verkabelung und Komponenten
```