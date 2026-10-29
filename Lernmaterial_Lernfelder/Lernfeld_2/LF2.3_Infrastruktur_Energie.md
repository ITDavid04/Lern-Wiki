# LF2.3 – Infrastruktur & Energie

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 90–110 Min., mit Vertiefung (Rechenbeispiele, Nice-to-know): 130–150 Min.
> **Status:** Final
> **Stand:** 2026-09-16

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie berechnet man die theoretische Bandbreite eines RAM-Moduls, und warum funktioniert RDIMM nicht in jedem PC? | [1](#1-das-rückgrat--die-onboard-welt) |
| 2 | Was unterscheidet Wirk-, Blind- und Scheinleistung, und wozu dient Aktive PFC? | [2](#2-die-energiezentrale-psu) |
| 3 | Warum sind SMR-Festplatten im RAID-Verbund riskant? | [3](#3-massenspeicher-i--die-magnetische-ära--protokolle) |
| 4 | Was ist TBW, und warum bricht die Geschwindigkeit einer QLC-SSD bei großen Kopiervorgängen ein? | [4](#4-massenspeicher-ii--die-flash-revolution) |
| 5 | Wie erkennt man rechnerisch, ob eine PCIe-Verbindung oder der Chipsatz-Uplink (DMI) zum Flaschenhals wird? | [5](#5-bottleneck-detective) |

---

## 1. Das Rückgrat & die Onboard-Welt

> **Grundprinzip:** Das Mainboard ist das Nervensystem des PCs – es verbindet alle Komponenten, aber "passt physisch" bedeutet nicht automatisch "funktioniert elektrisch/logisch".

### 1.1 Erweiterungs-Slots im Überblick

| Slot-Typ | Übertragung | Speed (max., historisch) | Nutzung |
|---|---|---|---|
| ISA | Parallel | ~8 MB/s | Uralt-Steuerkarten (Retro) |
| PCI | Parallel | ~133 MB/s | Netzwerk, Sound (veraltet) |
| AGP | Parallel | ~2 GB/s | Exklusiv für GPUs (Vorgänger von PCIe) |
| PCIe | Seriell | Skalierbar (abhängig von Generation und Lane-Anzahl) | Der heutige universelle Standard |

🔴 **Stolperstein:** "Ein x16-Slot liefert immer x16-Bandbreite." Nicht zwingend – der **physische** Slot (z. B. x16, mechanisch) und die **elektrische Anbindung** (z. B. nur x4 Lanes tatsächlich verdrahtet) können auseinanderfallen. Das steht meist im Mainboard-Handbuch und ist besonders bei zusätzlichen M.2-Slots relevant (siehe Lane-Sharing in Abschnitt 5).

### 1.2 RAM-Evolution & Bandbreitenformel

> **Merksatz:** Ein RAM-Modul hat eine Busbreite von 64 Bit (8 Byte). Die Bandbreite ergibt sich aus effektivem Takt (MT/s) mal Busbreite in Byte.

**Formel:** Bandbreite (MB/s) = MT/s × 8 Byte

🟡 **Praxis-Tipp:** Diese einfache Formel (Datenrate × Busbreite) gilt gut für RAM. Bei seriellen Schnittstellen wie PCIe oder USB kommen zusätzlich Kodierungs-/Protokoll-Overhead und die Lane-Anzahl ins Spiel – dort reicht "Takt × Busbreite" allein nicht aus (siehe Abschnitt 5).

Wichtig zur Begriffsklärung: Bei "DDR4-3200" ist die **3200** bereits die effektive Datenrate in **MT/s** (MegaTransfers pro Sekunde) – also der tatsächliche I/O-Takt (hier 1600 MHz) bereits verdoppelt (DDR = Double Data Rate, zwei Datenübertragungen pro Taktzyklus).

> **IHK-Typfrage:** *Berechne die theoretische Bandbreite eines DDR4-Moduls mit 3200 MT/s unter Berücksichtigung der 64-Bit-Busbreite.*
> **Musterantwort:** Bandbreite = 3200 MT/s × 8 Byte = 25.600 MB/s = **25,6 GB/s** pro Modul (Single-Channel-Betrieb). Bei Dual-Channel-Betrieb mit zwei identischen Modulen verdoppelt sich dieser Wert theoretisch auf ca. 51,2 GB/s.

### 1.3 RAM-Begriffe

| Begriff | Bedeutung |
|---|---|
| Unbuffered (UDIMM) | Standard für PCs/Laptops – der Speichercontroller greift direkt auf die Chips zu |
| Buffered/Registered (RDIMM) | Zusätzlicher "Register"-Chip stabilisiert die Signale – Pflicht für Server mit viel RAM, dafür etwas höhere Latenz |
| ECC (Error Correction Code) | Ein zusätzlicher Speicherchip (72 statt 64 Bit Busbreite) erkennt und korrigiert einzelne Bit-Kipper – wichtig für Server/Workstations |

> **IHK-Typfrage:** *Warum funktioniert RDIMM-Speicher meist nicht in einem gewöhnlichen Gaming-PC, obwohl er physisch in den RAM-Slot passt?*
> **Musterantwort:** RDIMM benötigt einen Speichercontroller und ein BIOS/UEFI, das explizit für registrierten/gepufferten Speicher ausgelegt ist, da die zusätzliche Register-Stufe anders angesteuert wird als bei UDIMM. Consumer-Mainboards und -CPUs sind in aller Regel nur für UDIMM (und ggf. ECC-UDIMM) freigegeben – ein RDIMM-Modul passt zwar mechanisch in den Slot, wird vom System aber nicht erkannt oder führt zum Bootfehler.

🔴 **Stolperstein:** "ECC-RAM ist einfach RAM mit Fehlerkorrektur-Software." Falsch – ECC ist eine Hardware-Erweiterung mit zusätzlichem Speicherchip (72 statt 64 Bit Busbreite je Kanal), die Bitfehler auf Hardwareebene erkennt und korrigiert; sie erfordert einen dafür ausgelegten Speichercontroller (CPU) und ein passendes Mainboard.

🟡 **Kontextwissen – DDR-Generationen:** Von SD-RAM über DDR1–DDR5 sinkt die Betriebsspannung tendenziell (3,3 V → 1,1 V bei DDR5), während sich die effektive Datenrate mit jeder Generation etwa verdoppelt bis vervielfacht. Bei mobilen Geräten kommen zusätzlich LPDDR-Varianten (Low Power DDR) zum Einsatz, die oft direkt auf die Platine gelötet sind.

### 1.4 Onboard-Chips

Neben CPU und RAM sitzen auf dem Mainboard weitere Chips für Alltagsfunktionen: der **Audio-Codec** wandelt digitale Signale in analoge Töne (und umgekehrt) um, der **Netzwerk-PHY** (Physical Layer Chip) übernimmt die eigentliche elektrische Signalübertragung fürs Netzwerk. Diese Onboard-Lösungen sind meist ausreichend für Standardanwendungen, werden aber bei hohen Ansprüchen (Studio-Audio, 10-Gbit-Netzwerk) oft durch dedizierte Steckkarten ersetzt.

---

## 2. Die Energiezentrale (PSU)

> **Grundprinzip:** Das Netzteil (PSU) wandelt Wechselstrom (AC) aus der Steckdose in die vom PC benötigten Gleichspannungen (DC) um – dabei geht immer ein Teil der Energie als Wärme verloren.

### 2.1 Wirk-, Blind- und Scheinleistung (die "Bierglas"-Analogie)

| Leistungsart | Symbol/Einheit | Bierglas-Bild | Bedeutung |
|---|---|---|---|
| Wirkleistung | P, Watt (W) | Das Bier | Tatsächlich genutzte Energie |
| Blindleistung | Q, var | Der Schaum | Pendelenergie durch Spulen/Kondensatoren, verrichtet keine Nutzarbeit |
| Scheinleistung | S, Voltampere (VA) | Das ganze Glas | Aus dem Netz tatsächlich bezogene Gesamtleistung (P und Q zusammen) – wichtig für die Dimensionierung einer USV |

> **IHK-Typfrage:** *Welche Leistungsart wird durch eine "Aktive PFC" (Power Factor Correction) optimiert bzw. minimiert?*
> **Musterantwort:** Aktive PFC sorgt dafür, dass die Stromaufnahme des Netzteils möglichst sinusförmig verläuft und phasengleich mit der Netzspannung ist. Dadurch verbessert sich der Leistungsfaktor (cos φ = P/S) und Oberschwingungen/Netzrückwirkungen werden reduziert – im Ergebnis sinkt die **Blindleistung**, sodass die Scheinleistung näher an die Wirkleistung heranrückt und das Netzteil das Stromnetz effizienter belastet.

### 2.2 Rechenbeispiel: Stromstärke

> **IHK-Typfrage:** *Berechne die Stromstärke in Ampere für eine Komponente, die 300 W an der 12-V-Schiene zieht.*
> **Musterantwort:** Nach der Formel I = P / U ergibt sich: I = 300 W / 12 V = **25 A**.

### 2.3 80 PLUS – Effizienzzertifizierung

> ⚠️ 80-PLUS-Anforderungen unterscheiden sich je nach Eingangsspannung (115 V US vs. 230 V EU) und Netzteilkategorie – die folgende Tabelle zeigt die **230-V-EU-Werte** (relevant für den Betrieb in Deutschland/Europa); bei 115 V (USA) liegen die Prozentwerte für dieselbe Stufe etwas niedriger. 80 PLUS bewertet primär Energieeffizienz (teils auch den Leistungsfaktor), nicht automatisch Spannungsqualität, Lautstärke oder allgemeine Bauqualität.

| Zertifikat | Effizienz bei 20 % Last | bei 50 % Last | bei 100 % Last | Empfehlung |
|---|---|---|---|---|
| 80 PLUS (White) | 82 % | 85 % | 82 % | Nur für einfachste Office-PCs |
| Bronze | 85 % | 88 % | 85 % | Budget-Gaming/Standard |
| Silver | 87 % | 90 % | 87 % | Selten einzeln vermarktet, liegt zwischen Bronze und Gold |
| Gold | 90 % | 92 % | 89 % | Standard für gute PCs |
| Platinum | 92 % | 94 % | 90 % | Server/Workstation (Dauerlast) |
| Titanium | 93 % | 95 % | 91 % | High-End, auch bei niedriger Last effizient |

🟢 **Nice to know:** Titanium ist die einzige Stufe, die zusätzlich einen **vierten Messpunkt bei nur 10 % Last** verlangt (dort mind. 90 %) – ein Hinweis darauf, dass Titanium-Netzteile speziell auch im Teillastbereich (z. B. Server im Nachtbetrieb) effizient bleiben sollen, nicht nur bei mittlerer/hoher Auslastung.

> **IHK-Typfrage:** *Berechne die Stromkosten (0,35 €/kWh) über 5 Jahre (8 h/Tag, 220 Tage/Jahr) für einen PC mit 300 W Leistungsbedarf an den Komponenten (DC-seitig), und vergleiche ein Bronze- mit einem Titanium-Netzteil bei angenommener 50 %-Last-Effizienz.*
> **Musterantwort:** Die 300 W beziehen sich auf die von den PC-Komponenten tatsächlich benötigte Gleichstromleistung – die aus der Steckdose bezogene Leistung ergibt sich aus: Leistungsbedarf ÷ Wirkungsgrad.
> - Bronze (88 % bei 50 % Last): 300 W ÷ 0,88 ≈ 340,9 W
> - Titanium (95 % bei 50 % Last): 300 W ÷ 0,95 ≈ 315,8 W
> - Differenz ≈ 25,1 W
>
> Betriebsstunden über 5 Jahre: 8 h × 220 Tage × 5 Jahre = 8.800 Stunden.
> Mehrverbrauch Bronze ggü. Titanium: 25,1 W × 8.800 h ÷ 1000 ≈ 221 kWh.
> Mehrkosten: 221 kWh × 0,35 €/kWh ≈ **77,40 € über 5 Jahre** (der angenommene Strompreis ist ein gerundeter Beispielwert – aktuelle Haushaltsstrompreise in Deutschland schwanken je nach Tarif und Zeitpunkt etwa zwischen 25 und 40 Cent/kWh).
>
> Diese Kostendifferenz muss dem höheren Anschaffungspreis eines Titanium-Netzteils gegenübergestellt werden, um die Wirtschaftlichkeit zu beurteilen (Amortisationsrechnung).

🔴 **Stolperstein:** "Ein 1000-W-Netzteil ist immer die sichere/beste Wahl." Netzteile erreichen ihren besten Wirkungsgrad typischerweise im mittleren Lastbereich (häufig ungefähr 40–60 %), nicht nahe 100 % Auslastung. Bei sehr geringer Auslastung (z. B. ein 150-W-Office-PC an einem 1000-W-Netzteil) sinkt der Wirkungsgrad oft spürbar, wie die 80-PLUS-Tabelle bei 20 %-Last zeigt – ein stark überdimensioniertes Netzteil begünstigt daher den ineffizienten Niedriglastbereich und ist meist unwirtschaftlich, nicht "auf der sicheren Seite".

🟡 **Kontextwissen:** Für die Dimensionierung einer **USV** (unterbrechungsfreie Stromversorgung) ist die **Scheinleistung (VA)** maßgeblich, nicht die Wirkleistung – ein häufiger Fehler bei der Ausschreibung ist, beide Werte gleichzusetzen.

---

## 3. Massenspeicher I – Die magnetisc# LF2.3 – Infrastruktur & Energie

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 90–110 Min., mit Vertiefung (Rechenbeispiele, Nice-to-know): 130–150 Min.
> **Status:** Review (Bandbreitenformel, PFC, 80-PLUS-Spannungsbezug, Effizienzkurve, SAS-Versionen, SMR/RAID-Absolutheit, DMI-Pauschalisierung korrigiert)
> **Stand:** 2026-08-27 – Zahlenangaben zu Kapazitäten, Preisen und Schnittstellen-Bandbreiten sollten vor Verwendung im Unterricht kurz gegengeprüft werden.

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Wie berechnet man die theoretische Bandbreite eines RAM-Moduls, und warum funktioniert RDIMM nicht in jedem PC? | [1](#1-das-rückgrat--die-onboard-welt) |
| 2 | Was unterscheidet Wirk-, Blind- und Scheinleistung, und wozu dient Aktive PFC? | [2](#2-die-energiezentrale-psu) |
| 3 | Warum sind SMR-Festplatten im RAID-Verbund riskant? | [3](#3-massenspeicher-i--die-magnetische-ära--protokolle) |
| 4 | Was ist TBW, und warum bricht die Geschwindigkeit einer QLC-SSD bei großen Kopiervorgängen ein? | [4](#4-massenspeicher-ii--die-flash-revolution) |
| 5 | Wie erkennt man rechnerisch, ob eine PCIe-Verbindung oder der Chipsatz-Uplink (DMI) zum Flaschenhals wird? | [5](#5-bottleneck-detective) |

---

## 1. Das Rückgrat & die Onboard-Welt

> **Grundprinzip:** Das Mainboard ist das Nervensystem des PCs – es verbindet alle Komponenten, aber "passt physisch" bedeutet nicht automatisch "funktioniert elektrisch/logisch".

### 1.1 Erweiterungs-Slots im Überblick

| Slot-Typ | Übertragung | Speed (max., historisch) | Nutzung |
|---|---|---|---|
| ISA | Parallel | ~8 MB/s | Uralt-Steuerkarten (Retro) |
| PCI | Parallel | ~133 MB/s | Netzwerk, Sound (veraltet) |
| AGP | Parallel | ~2 GB/s | Exklusiv für GPUs (Vorgänger von PCIe) |
| PCIe | Seriell | Skalierbar (abhängig von Generation und Lane-Anzahl) | Der heutige universelle Standard |

🔴 **Stolperstein:** "Ein x16-Slot liefert immer x16-Bandbreite." Nicht zwingend – der **physische** Slot (z. B. x16, mechanisch) und die **elektrische Anbindung** (z. B. nur x4 Lanes tatsächlich verdrahtet) können auseinanderfallen. Das steht meist im Mainboard-Handbuch und ist besonders bei zusätzlichen M.2-Slots relevant (siehe Lane-Sharing in Abschnitt 5).

### 1.2 RAM-Evolution & Bandbreitenformel

> **Merksatz:** Ein RAM-Modul hat eine Busbreite von 64 Bit (8 Byte). Die Bandbreite ergibt sich aus effektivem Takt (MT/s) mal Busbreite in Byte.

**Formel:** Bandbreite (MB/s) = MT/s × 8 Byte

🟡 **Praxis-Tipp:** Diese einfache Formel (Datenrate × Busbreite) gilt gut für RAM. Bei seriellen Schnittstellen wie PCIe oder USB kommen zusätzlich Kodierungs-/Protokoll-Overhead und die Lane-Anzahl ins Spiel – dort reicht "Takt × Busbreite" allein nicht aus (siehe Abschnitt 5).

Wichtig zur Begriffsklärung: Bei "DDR4-3200" ist die **3200** bereits die effektive Datenrate in **MT/s** (MegaTransfers pro Sekunde) – also der tatsächliche I/O-Takt (hier 1600 MHz) bereits verdoppelt (DDR = Double Data Rate, zwei Datenübertragungen pro Taktzyklus).

> **IHK-Typfrage:** *Berechne die theoretische Bandbreite eines DDR4-Moduls mit 3200 MT/s unter Berücksichtigung der 64-Bit-Busbreite.*
> **Musterantwort:** Bandbreite = 3200 MT/s × 8 Byte = 25.600 MB/s = **25,6 GB/s** pro Modul (Single-Channel-Betrieb). Bei Dual-Channel-Betrieb mit zwei identischen Modulen verdoppelt sich dieser Wert theoretisch auf ca. 51,2 GB/s.

### 1.3 RAM-Begriffe

| Begriff | Bedeutung |
|---|---|
| Unbuffered (UDIMM) | Standard für PCs/Laptops – der Speichercontroller greift direkt auf die Chips zu |
| Buffered/Registered (RDIMM) | Zusätzlicher "Register"-Chip stabilisiert die Signale – Pflicht für Server mit viel RAM, dafür etwas höhere Latenz |
| ECC (Error Correction Code) | Ein zusätzlicher Speicherchip (72 statt 64 Bit Busbreite) erkennt und korrigiert einzelne Bit-Kipper – wichtig für Server/Workstations |

> **IHK-Typfrage:** *Warum funktioniert RDIMM-Speicher meist nicht in einem gewöhnlichen Gaming-PC, obwohl er physisch in den RAM-Slot passt?*
> **Musterantwort:** RDIMM benötigt einen Speichercontroller und ein BIOS/UEFI, das explizit für registrierten/gepufferten Speicher ausgelegt ist, da die zusätzliche Register-Stufe anders angesteuert wird als bei UDIMM. Consumer-Mainboards und -CPUs sind in aller Regel nur für UDIMM (und ggf. ECC-UDIMM) freigegeben – ein RDIMM-Modul passt zwar mechanisch in den Slot, wird vom System aber nicht erkannt oder führt zum Bootfehler.

🔴 **Stolperstein:** "ECC-RAM ist einfach RAM mit Fehlerkorrektur-Software." Falsch – ECC ist eine Hardware-Erweiterung mit zusätzlichem Speicherchip (72 statt 64 Bit Busbreite je Kanal), die Bitfehler auf Hardwareebene erkennt und korrigiert; sie erfordert einen dafür ausgelegten Speichercontroller (CPU) und ein passendes Mainboard.

🟡 **Kontextwissen – DDR-Generationen:** Von SD-RAM über DDR1–DDR5 sinkt die Betriebsspannung tendenziell (3,3 V → 1,1 V bei DDR5), während sich die effektive Datenrate mit jeder Generation etwa verdoppelt bis vervielfacht. Bei mobilen Geräten kommen zusätzlich LPDDR-Varianten (Low Power DDR) zum Einsatz, die oft direkt auf die Platine gelötet sind.

### 1.4 Onboard-Chips

Neben CPU und RAM sitzen auf dem Mainboard weitere Chips für Alltagsfunktionen: der **Audio-Codec** wandelt digitale Signale in analoge Töne (und umgekehrt) um, der **Netzwerk-PHY** (Physical Layer Chip) übernimmt die eigentliche elektrische Signalübertragung fürs Netzwerk. Diese Onboard-Lösungen sind meist ausreichend für Standardanwendungen, werden aber bei hohen Ansprüchen (Studio-Audio, 10-Gbit-Netzwerk) oft durch dedizierte Steckkarten ersetzt.

---

## 2. Die Energiezentrale (PSU)

> **Grundprinzip:** Das Netzteil (PSU) wandelt Wechselstrom (AC) aus der Steckdose in die vom PC benötigten Gleichspannungen (DC) um – dabei geht immer ein Teil der Energie als Wärme verloren.

### 2.1 Wirk-, Blind- und Scheinleistung (die "Bierglas"-Analogie)

| Leistungsart | Symbol/Einheit | Bierglas-Bild | Bedeutung |
|---|---|---|---|
| Wirkleistung | P, Watt (W) | Das Bier | Tatsächlich genutzte Energie |
| Blindleistung | Q, var | Der Schaum | Pendelenergie durch Spulen/Kondensatoren, verrichtet keine Nutzarbeit |
| Scheinleistung | S, Voltampere (VA) | Das ganze Glas | Aus dem Netz tatsächlich bezogene Gesamtleistung (P und Q zusammen) – wichtig für die Dimensionierung einer USV |

> **IHK-Typfrage:** *Welche Leistungsart wird durch eine "Aktive PFC" (Power Factor Correction) optimiert bzw. minimiert?*
> **Musterantwort:** Aktive PFC sorgt dafür, dass die Stromaufnahme des Netzteils möglichst sinusförmig verläuft und phasengleich mit der Netzspannung ist. Dadurch verbessert sich der Leistungsfaktor (cos φ = P/S) und Oberschwingungen/Netzrückwirkungen werden reduziert – im Ergebnis sinkt die **Blindleistung**, sodass die Scheinleistung näher an die Wirkleistung heranrückt und das Netzteil das Stromnetz effizienter belastet.

### 2.2 Rechenbeispiel: Stromstärke

> **IHK-Typfrage:** *Berechne die Stromstärke in Ampere für eine Komponente, die 300 W an der 12-V-Schiene zieht.*
> **Musterantwort:** Nach der Formel I = P / U ergibt sich: I = 300 W / 12 V = **25 A**.

### 2.3 80 PLUS – Effizienzzertifizierung

> ⚠️ 80-PLUS-Anforderungen unterscheiden sich je nach Eingangsspannung (115 V US vs. 230 V EU) und Netzteilkategorie – die folgenden Werte sind typische Beispielwerte und ersetzen nicht den Blick in die konkrete Zertifikatsstufe. 80 PLUS bewertet primär Energieeffizienz (teils auch den Leistungsfaktor), nicht automatisch Spannungsqualität, Lautstärke oder allgemeine Bauqualität.

| Zertifikat | Effizienz bei 20 % Last | bei 50 % Last | bei 100 % Last | Empfehlung |
|---|---|---|---|---|
| 80 PLUS (White) | 82 % | 85 % | 82 % | Nur für einfachste Office-PCs |
| Bronze | 85 % | 88 % | 85 % | Budget-Gaming/Standard |
| Gold | 90 % | 92 % | 89 % | Standard für gute PCs |
| Platinum | 92 % | 94 % | 90 % | Server/Workstation (Dauerlast) |
| Titanium | 94 % | 96 % | 94 % | High-End, auch bei niedriger Last effizient |

> **IHK-Typfrage:** *Berechne die Stromkosten (0,35 €/kWh) über 5 Jahre (8 h/Tag, 220 Tage/Jahr) für einen PC mit 300 W Leistungsbedarf an den Komponenten (DC-seitig), und vergleiche ein Bronze- mit einem Titanium-Netzteil bei angenommener 50 %-Last-Effizienz.*
> **Musterantwort:** Die 300 W beziehen sich auf die von den PC-Komponenten tatsächlich benötigte Gleichstromleistung – die aus der Steckdose bezogene Leistung ergibt sich aus: Leistungsbedarf ÷ Wirkungsgrad.
> - Bronze (88 % bei 50 % Last): 300 W ÷ 0,88 ≈ 340,9 W
> - Titanium (96 % bei 50 % Last): 300 W ÷ 0,96 ≈ 312,5 W
> - Differenz ≈ 28,4 W
>
> Betriebsstunden über 5 Jahre: 8 h × 220 Tage × 5 Jahre = 8.800 Stunden.
> Mehrverbrauch Bronze ggü. Titanium: 28,4 W × 8.800 h ÷ 1000 ≈ 250 kWh.
> Mehrkosten: 250 kWh × 0,35 €/kWh ≈ **87,50 € über 5 Jahre**.
>
> Diese Kostendifferenz muss dem höheren Anschaffungspreis eines Titanium-Netzteils gegenübergestellt werden, um die Wirtschaftlichkeit zu beurteilen (Amortisationsrechnung).

🔴 **Stolperstein:** "Ein 1000-W-Netzteil ist immer die sichere/beste Wahl." Netzteile erreichen ihren besten Wirkungsgrad typischerweise im mittleren Lastbereich (häufig ungefähr 40–60 %), nicht nahe 100 % Auslastung. Bei sehr geringer Auslastung (z. B. ein 150-W-Office-PC an einem 1000-W-Netzteil) sinkt der Wirkungsgrad oft spürbar, wie die 80-PLUS-Tabelle bei 20 %-Last zeigt – ein stark überdimensioniertes Netzteil begünstigt daher den ineffizienten Niedriglastbereich und ist meist unwirtschaftlich, nicht "auf der sicheren Seite".

🟡 **Kontextwissen:** Für die Dimensionierung einer **USV** (unterbrechungsfreie Stromversorgung) ist die **Scheinleistung (VA)** maßgeblich, nicht die Wirkleistung – ein häufiger Fehler bei der Ausschreibung ist, beide Werte gleichzusetzen.

---

## 3. Massenspeicher I – Die magnetische Ära & Protokolle

> **Grundprinzip:** Magnetische Speichertechnologien unterscheiden sich stark in Zugriffsmuster und Haltbarkeit – "günstig pro TB" und "geeignet für den Einsatzzweck" sind zwei verschiedene Fragen.

### 3.1 Magnetische Technologien im Vergleich

| Technologie | Verfahren | Vorteile | Nachteile | Typischer Einsatz |
|---|---|---|---|---|
| CMR (HDD) | Conventional Magnetic Recording | Stabil, auch beim Schreiben zuverlässig schnell | Mechanischer Verschleiß, geringere Maximal-Kapazität als SMR | NAS, RAID, Server |
| SMR (HDD) | Shingled Magnetic Recording (überlappende Spuren) | Höhere maximale Kapazität, günstiger pro TB | Beim Überschreiben/Rewrite extrem langsam, da überlappende Spuren neu geschrieben werden müssen | Cold Storage, einfache Desktop-Nutzung |
| LTO (Tape) | Linear Tape Open | "Air Gap" möglich (physisch getrennt lagerbar), sehr lange Haltbarkeit (Jahrzehnte), günstig pro TB | Rein sequenzieller Zugriff, Laufwerk selbst teuer | Langzeitarchivierung, Disaster Recovery |

> **IHK-Typfrage:** *Warum ist der Einsatz von SMR-Festplatten in einem RAID-5-Verbund riskant?*
> **Musterantwort:** SMR-Festplatten schreiben Daten in überlappenden Spuren, wodurch das Ändern bereits geschriebener Daten (Rewrite) deutlich langsamer ist als bei CMR. Muss im Fehlerfall ein RAID-5-Array neu aufgebaut werden (Rebuild), erfordert das anhaltende, intensive Schreibvorgänge über die gesamte Platte – bei vielen (insbesondere host-managed oder für den Desktop-Einsatz ausgelegten) SMR-Platten kann dieser Vorgang so lange dauern, dass er Timeout-Grenzen des RAID-Controllers überschreitet oder das Risiko eines zweiten Plattenausfalls während der ungewöhnlich langen Rebuild-Zeit deutlich steigt, was im ungünstigen Fall zum Totalverlust des Arrays führen kann. Für RAID-/NAS-Einsatz sollten deshalb ausdrücklich vom Hersteller dafür freigegebene CMR- bzw. NAS-Laufwerke verwendet werden.

🟡 **Kontextwissen – "Air Gap":** Ein physisch vom Netzwerk getrenntes Speichermedium (wie ein Tape im Schrank) kann nicht durch Ransomware verschlüsselt werden, die sich über das Netzwerk verbreitet – das ist der Hauptgrund, warum LTO-Tapes trotz "veralteter" Technik weiterhin bei Backup-Strategien eingesetzt werden.

### 3.2 Die Protokoll-Evolution

| Schnittstelle | Zeitraum | Technik | Speed (max., historisch) | Besonderheit |
|---|---|---|---|---|
| IDE (PATA) | ca. 1986–2013 | Parallel | ~133 MB/s | Benötigt Master/Slave-Jumper-Konfiguration |
| SCSI | ca. 1981–2003 | Parallel | ~320 MB/s | Profi-Standard der 1990er, benötigte Terminierung |
| SATA | seit 2003 | Seriell | ~600 MB/s | Point-to-Point, Hot-Swap-fähig, Half-Duplex |
| SAS | seit 2004 | Seriell | SAS-2: 6 Gbit/s, SAS-3: 12 Gbit/s, SAS-4: 24 Gbit/s pro Lane | Full-Duplex, Server-Standard, zusätzliche Enterprise-Funktionen |

> **IHK-Typfrage:** *Warum bietet Full-Duplex (SAS) im Serverumfeld Vorteile gegenüber Half-Duplex (SATA)?*
> **Musterantwort:** Bei Half-Duplex (SATA) können Daten zu einem Zeitpunkt nur in eine Richtung übertragen werden (entweder lesen oder schreiben) – bei Full-Duplex (SAS) ist gleichzeitiges Lesen und Schreiben möglich. In Serverumgebungen mit vielen parallelen, gemischten Lese-/Schreibzugriffen (z. B. Datenbank- oder Virtualisierungsserver) erhöht das den effektiven Durchsatz spürbar. Der Duplex-Unterschied ist aber nicht der einzige Vorteil von SAS: Zusätzlich bietet SAS Enterprise-Funktionen wie Dual-Porting (Anbindung eines Laufwerks über zwei unabhängige Pfade) und SAS-Expander (Anschluss vieler Laufwerke über wenige Controller-Ports), die für große Server-Storage-Umgebungen ebenso wichtig sind.

🔴 **Stolperstein:** "SAS und SATA sind elektrisch dasselbe, nur anders benannt." Ein SATA-Stecker passt zwar in einen SAS-Controller (SAS-Controller sind meist abwärtskompatibel zu SATA-Laufwerken), umgekehrt passt ein SAS-Stecker aber physisch nicht in einen normalen SATA-Port – SAS nutzt ein anderes, komplexeres Protokoll und andere Signalpegel als reines SATA.

🟢 **Nice to know – IOPS:** Bei zufälligen (nicht-sequenziellen) 4K-Zugriffen bricht die Performance einer klassischen HDD drastisch ein, weil Schreib-/Lesekopf und Platter für jeden Zugriff neu physisch positioniert werden müssen (Seek-Zeit + Rotationslatenz) – SSDs haben dieses Problem nicht, da sie keine beweglichen Teile besitzen.

---

## 4. Massenspeicher II – Die Flash-Revolution

> **Grundprinzip:** "Mehr Bits pro Speicherzelle" bedeutet mehr Kapazität pro Fläche, aber auch weniger Haltbarkeit und geringere native Geschwindigkeit – ein bewusster Kompromiss, kein technischer Rückschritt.

### 4.1 Zell-Typen im Vergleich

> ⚠️ Die folgenden Werte sind grobe didaktische Größenordnungen zur Einordnung, keine allgemeingültigen oder garantierten technischen Werte – die tatsächliche Haltbarkeit hängt zusätzlich von NAND-Generation, Controller, Overprovisioning und Schreibmuster ab. Maßgeblich für die Praxis ist immer die vom Hersteller angegebene TBW- bzw. DWPD-Angabe des konkreten Produkts.

| Typ | Bits pro Zelle | P/E-Zyklen (grobe Orientierung) | Native Geschwindigkeit | Haltbarkeit (TBW, grobe Tendenz) |
|---|---|---|---|---|
| SLC | 1 | ~100.000 | Sehr hoch | Sehr hoch (Server-Einsatz) |
| MLC | 2 | ~10.000 | Hoch | Hoch (Server-Einsatz) |
| TLC | 3 | ~3.000 | Mittel | Mittel (Consumer-Standard) |
| QLC | 4 | ~1.000 | Niedriger (nativ) | Niedriger |

> **IHK-Typfrage:** *Würdest du für einen schreibintensiven Datenbank-Server QLC- oder TLC-Speicherzellen empfehlen?*
> **Musterantwort:** TLC ist hier tendenziell die bessere Wahl. Datenbank-Server erzeugen viele, teils zufällige Schreibvorgänge über die gesamte Lebensdauer – dabei ist die Haltbarkeit (ausgedrückt in TBW, Total Bytes Written) ein wichtiges Auswahlkriterium, die mit den P/E-Zyklen der Zellen zusammenhängt. QLC weist im Allgemeinen eine geringere Schreibreserven- und Dauerlast-Eignung als TLC auf; für schreibintensive Datenbanklasten sind daher meist Enterprise-TLC-SSDs mit passender TBW-/DWPD-Auslegung geeigneter. Für rein lesefokussierte oder wenig schreibintensive Anwendungen kann QLC dagegen wegen der höheren Kapazität pro Kosten sinnvoll sein – die konkrete Herstellerangabe zu TBW/DWPD des jeweiligen Produkts bleibt aber immer die maßgebliche Entscheidungsgrundlage, nicht der Zelltyp allein.

### 4.2 SLC-Cache und "Prospekt-Geschwindigkeit"

Viele QLC/TLC-SSDs nutzen einen Teil ihrer Zellen dynamisch als schnellen **SLC-Cache** (Pseudo-SLC-Modus), um kurzzeitig hohe Schreibgeschwindigkeiten zu erreichen. Ist dieser Cache bei sehr großen, anhaltenden Kopiervorgängen erschöpft, fällt die Geschwindigkeit auf die deutlich niedrigere native Geschwindigkeit der eigentlichen Zellen zurück.

> **IHK-Typfrage:** *Erkläre einem Kunden den Unterschied zwischen "Prospekt-Geschwindigkeit" und "realer Geschwindigkeit" beim Kopieren einer sehr großen Datei auf eine QLC-SSD.*
> **Musterantwort:** Die im Prospekt beworbene Spitzengeschwindigkeit gilt meist nur, solange der SLC-Cache der SSD noch Kapazität frei hat – dort werden Daten kurzzeitig sehr schnell zwischengespeichert. Bei einer sehr großen Datei, die die Kapazität dieses Zwischenspeichers übersteigt, muss die SSD auf die native Schreibgeschwindigkeit der eigentlichen QLC-Zellen zurückfallen, die deutlich niedriger liegt – der Kunde sieht dann mitten im Kopiervorgang einen spürbaren Geschwindigkeitseinbruch, obwohl das Produkt nicht defekt ist.

🟡 **Kontextwissen – Wear Leveling:** Der SSD-Controller verteilt Schreibvorgänge bewusst gleichmäßig über alle verfügbaren Speicherzellen, statt immer dieselben Zellen zu beschreiben – da jede Zelle nur eine begrenzte Anzahl an P/E-Zyklen erträgt, verlängert das die Gesamtlebensdauer der SSD spürbar.

### 4.3 Schnittstellen und Bandbreiten

| Schnittstelle | Protokoll | Typische max. Bandbreite (netto, Größenordnung) | Typischer Einsatz |
|---|---|---|---|
| SATA III | AHCI | ~560 MB/s | Office-PC, HDD-Ersatz |
| PCIe 3.0 x4 | NVMe | ~3.500 MB/s | Standard-Laptops |
| PCIe 4.0 x4 | NVMe | ~7.500 MB/s | High-End-PC |
| PCIe 5.0 x4 | NVMe | ~14.000 MB/s | Enthusiast, Workstation |
| UFS | SCSI-basiert | ~4.600 MB/s | High-End-Smartphones |
| eMMC | MMC | ~400 MB/s | Budget-Tablets (Half-Duplex) |

🟡 **Praxis-Tipp:** Die Zuordnung von PCIe-Generation zu einer bestimmten NVMe-Protokollversion (z. B. "PCIe 4.0 → NVMe 1.4") ist eine typische, aber keine zwingende Kombination – PCIe-Generation (die elektrische/physische Anbindung) und NVMe-Version (das Protokoll darüber) sind grundsätzlich unabhängig voneinander und werden von Hersteller zu Hersteller unterschiedlich kombiniert.

🔴 **Stolperstein:** "Random Read ist für die Nutzererfahrung weniger wichtig als die sequenzielle Transferrate." Für alltägliche Aufgaben wie Windows-/Programmstart ist meist die **Random-Read-Geschwindigkeit** entscheidender als die (in Prospekten meist beworbene) sequenzielle Transferrate, da beim Programmstart viele kleine, verstreut liegende Dateien gelesen werden – große, zusammenhängende Dateien (die von sequenzieller Geschwindigkeit profitieren) sind im Alltag seltener.

---

## 5. Bottleneck Detective

> **Grundprinzip:** Ein System ist immer nur so schnell wie sein langsamstes relevantes Glied – Bandbreiten lassen sich mit derselben Grundformel wie beim RAM (Takt × Busbreite) für praktisch jede Schnittstelle nachrechnen.

**Grundformel:** Datenrate = Takt × Busbreite

> **IHK-Typfrage:** *Eine Grafikkarte steckt in einem PCIe-3.0-x16-Slot, ist elektrisch aber nur mit x8 angebunden. Bestimme die maximale Bandbreite und erkläre die Konsequenz.*
> **Musterantwort:** Die maximale Bandbreite richtet sich nach der tatsächlichen elektrischen Anbindung (x8), nicht nach der mechanischen Slotgröße (x16) – bei PCIe 3.0 stehen pro Lane und Richtung ca. 985 MB/s (netto, nach Protokoll-/Kodierungs-Overhead) zur Verfügung, mit 8 Lanes also ca. 7,9 GB/s **pro Richtung** (PCIe ist bidirektional). Eine sehr leistungsstarke Grafikkarte, die theoretisch von x16 profitieren würde, kann durch die x8-Anbindung in Grenzfällen ausgebremst werden – in den meisten Spielen ist der Unterschied zwischen x8 und x16 aber gering; messbarer wird er eher bei Workloads mit besonders häufigem Datenaustausch zwischen Hauptspeicher und Grafikkarte (z. B. bestimmten Compute-/Streaming-Szenarien) als allein durch eine hohe Auflösung.

🔴 **Stolperstein:** "Eine schnelle CPU macht jedes System automatisch schneller." Beim Videoschnitt mit Zugriff auf eine langsame USB-2.0-Festplatte (max. ca. 60 MB/s) wartet selbst die schnellste CPU auf die eintreffenden Daten – der Flaschenhals liegt hier eindeutig bei der Speicherschnittstelle, nicht bei der Rechenleistung. Das Gesamtsystem ist immer nur so schnell wie sein langsamstes, für die jeweilige Aufgabe relevantes Glied.

🟡 **Kontextwissen – DMI-Flaschenhals:** Der Chipsatz (PCH) ist über eine Verbindung namens **DMI** (Direct Media Interface) an die CPU angebunden. Diese Verbindung hat eine begrenzte Gesamtbandbreite, die je nach DMI-Version und Plattform unterschiedlich ausfällt (grob in der Größenordnung mehrerer PCIe-Lanes) – neuere Plattformgenerationen bieten hier tendenziell mehr Bandbreite als ältere. Sind mehrere schnelle NVMe-SSDs, SATA-Ports und weitere Peripherie gleichzeitig über den Chipsatz angebunden, teilen sie sich diese eine DMI-Verbindung zur CPU – bei voller gleichzeitiger Auslastung mehrerer schneller Geräte kann das zum gemeinsamen Engpass werden, unabhängig von der Einzel-Bandbreite jedes Geräts. Das genaue DMI-Limit einer konkreten Plattform steht im jeweiligen Mainboard-/Chipsatz-Datenblatt.

🟢 **Nice to know – Lane-Sharing:** Manche Mainboards deaktivieren bestimmte SATA-Ports automatisch, sobald ein zusätzlicher M.2-Steckplatz belegt wird – Grund ist, dass sich beide Anschlüsse dieselben, begrenzt verfügbaren PCIe-Lanes bzw. Chipsatz-Ressourcen teilen. Das steht im Mainboard-Handbuch und ist ein klassischer Stolperstein bei der Systemplanung.

### USB-Generationen (Auszug)

| Bezeichnung (aktuell) | Frühere Bezeichnung | Geschwindigkeit |
|---|---|---|
| USB 3.2 Gen 1 | USB 3.0 / USB 3.1 Gen 1 | 5 Gbit/s |
| USB 3.2 Gen 2 | USB 3.1 Gen 2 | 10 Gbit/s |
| USB 3.2 Gen 2x2 | – | 20 Gbit/s |

🟡 **Praxis-Tipp:** Die USB-Namensgebung wurde vom USB-IF mehrfach rückwirkend umbenannt (z. B. hieß dieselbe 5-Gbit/s-Technik erst USB 3.0, dann USB 3.1 Gen 1, dann USB 3.2 Gen 1) – bei Datenblättern und Prüfungsfragen lohnt sich deshalb der Blick auf die tatsächliche Gbit/s-Angabe statt allein auf die Versionsbezeichnung. Wichtig für die Praxis: **USB-C bezeichnet nur die Steckerform**, nicht automatisch eine bestimmte Geschwindigkeit oder Norm (USB-C-Kabel/-Anschlüsse können z. B. USB 2.0, USB 3.2 oder Thunderbolt transportieren) – das ist ein häufiger Verwechslungspunkt bei Kunden und in Prüfungen.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Berechne die Bandbreite eines DDR4-2400-Moduls (Single-Channel). | 2400 MT/s × 8 Byte = 19.200 MB/s ≈ 19,2 GB/s |
| 2 | Warum ist Scheinleistung für die USV-Dimensionierung entscheidend? | Sie beschreibt die tatsächlich aus dem Netz bezogene Gesamtleistung (Wirk- + Blindleistung) |
| 3 | Warum sind SMR-Platten für RAID-5 riskant? | Extrem langsames Rewrite kann Rebuild-Vorgänge über Timeout-Grenzen verlängern |
| 4 | Was passiert, wenn der SLC-Cache einer QLC-SSD bei großen Dateien voll ist? | Die Geschwindigkeit fällt auf die niedrigere native Schreibgeschwindigkeit der QLC-Zellen zurück |
| 5 | Was bedeutet "elektrisch nur x4 angebunden" bei einem physischen x16-Slot? | Nur 4 der 16 Lanes sind tatsächlich verdrahtet – die Bandbreite entspricht der x4-Anbindung |
| 6 | Passt ein SAS-Stecker in einen normalen SATA-Port? | Nein – nur umgekehrt (SATA-Laufwerk in SAS-Controller) funktioniert meist |
| 7 | Was ist der DMI-Flaschenhals? | Die begrenzte Bandbreite der Chipsatz-CPU-Verbindung, die sich mehrere Chipsatz-Geräte teilen |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Bandbreite = Takt × Busbreite | Grundformel für RAM, Busse und viele weitere Schnittstellen |
| RDIMM/UDIMM | Registered (Server, Puffer-Chip) vs. Unbuffered (Consumer, Standard) |
| ECC-RAM | Zusätzlicher Speicherchip zur Bitfehler-Erkennung/-Korrektur (72 statt 64 Bit Busbreite) |
| Wirk-/Blind-/Scheinleistung | Nutzenergie / Pendelenergie / Gesamtleistung aus dem Netz (P, Q, S) |
| Aktive PFC | Minimiert Blindleistung, verbessert den Leistungsfaktor (cos φ) |
| 80 PLUS | Effizienzzertifizierung von Netzteilen (White bis Titanium) |
| CMR vs. SMR | Konventionell zuverlässig vs. hohe Kapazität, aber langsames Rewrite – für RAID/NAS explizit freigegebene CMR-/NAS-Laufwerke verwenden |
| LTO/Tape | Sequenzieller, aber langlebiger und "air-gap-fähiger" Archivspeicher |
| SATA vs. SAS | Half-Duplex, Consumer vs. Full-Duplex, Server-Standard |
| SLC/MLC/TLC/QLC | Zunehmend mehr Bits pro Zelle → mehr Kapazität, aber weniger Haltbarkeit/Geschwindigkeit |
| TBW | Total Bytes Written – Kennzahl für die Schreib-Haltbarkeit einer SSD |
| SLC-Cache | Dynamischer schneller Zwischenspeicher, dessen Erschöpfung die Geschwindigkeit einbrechen lässt |
| DMI | Verbindung zwischen Chipsatz und CPU, gemeinsam genutzter Flaschenhals für Chipsatz-Peripherie |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Bandbreiten-Rechnung | "Berechne die Bandbreite von X" | "Berechne die theoretische Bandbreite eines DDR5-5600-Moduls." | Vollständiger Rechenweg (MT/s × Byte), Ergebnis mit Einheit |
| Kosten-/Wirtschaftlichkeitsrechnung | "Berechne die Kosten von X über Zeitraum Y" | "Vergleiche die Stromkosten eines Bronze- und eines Gold-Netzteils über 3 Jahre." | Wirkungsgrad einbeziehen, vollständige Rechnung, nachvollziehbares Zwischenergebnis |
| Kompatibilitätsprüfung | "Funktioniert Komponente X in System Y?" | "Ein Kunde will RDIMM-Speicher in seinen Gaming-PC einbauen. Geht das?" | Konkrete technische Begründung, nicht nur Ja/Nein |
| Flaschenhals-Identifikation | "Wo liegt der Engpass im System?" | "Eine schnelle NVMe-SSD läuft in einem PCIe-3.0-Slot – was passiert?" | Engpass benennen + Bandbreiten-Vergleich als Beleg |

---

## Merk-Sätze fürs Fachgespräch

> Bandbreite = Takt × Busbreite ist eine Universalformel – ob RAM, PCIe oder Storage, das Prinzip bleibt gleich, nur die Einheiten ändern sich.

> Physisch passend heißt nicht elektrisch/logisch kompatibel – das gilt für RDIMM in Consumer-PCs genauso wie für x16-Slots mit x4-Anbindung.

> Ein überdimensioniertes Netzteil ist kein Sicherheitsgewinn, sondern oft ein Effizienzverlust – die meisten Netzteile arbeiten im mittleren Lastbereich (ca. 40–60 %) am wirtschaftlichsten, nicht nahe 100 % oder nahe 0 %.

> SMR spart Geld pro Terabyte, kostet aber im RAID-Ernstfall möglicherweise die gesamten Daten – die Technologie passt zum Einsatzzweck, nicht zu jedem Einsatzzweck.

> Prospekt-Geschwindigkeit gilt oft nur "solange der Cache reicht" – SLC-Cache bei SSDs und Effizienzangaben bei Netzteilen folgen demselben Muster: Randbedingungen zählen mehr als der Bestwert.

---

```yaml
lernfeld: LF2.3
titel: Infrastruktur & Energie
status: review
stand: 2026-08-27
quellen:
  - "LF2.3 – Infrastruktur & Energie"
  - "LF2.3.1 – Das Rückgrat & die Onboard-Welt"
  - "LF2.3.2 – Die Energiezentrale (PSU)"
  - "LF2.3.3 – Massenspeicher I: Die magnetische Ära & Protokolle"
  - "LF2.3.4 – Massenspeicher II: Die Flash-Revolution"
  - "LF2.3.5 – Bottleneck Detective"
```he Ära & Protokolle

> **Grundprinzip:** Magnetische Speichertechnologien unterscheiden sich stark in Zugriffsmuster und Haltbarkeit – "günstig pro TB" und "geeignet für den Einsatzzweck" sind zwei verschiedene Fragen.

### 3.1 Magnetische Technologien im Vergleich

| Technologie | Verfahren | Vorteile | Nachteile | Typischer Einsatz |
|---|---|---|---|---|
| CMR (HDD) | Conventional Magnetic Recording | Stabil, auch beim Schreiben zuverlässig schnell | Mechanischer Verschleiß, geringere Maximal-Kapazität als SMR | NAS, RAID, Server |
| SMR (HDD) | Shingled Magnetic Recording (überlappende Spuren) | Höhere maximale Kapazität, günstiger pro TB | Beim Überschreiben/Rewrite extrem langsam, da überlappende Spuren neu geschrieben werden müssen | Cold Storage, einfache Desktop-Nutzung |
| LTO (Tape) | Linear Tape Open | "Air Gap" möglich (physisch getrennt lagerbar), sehr lange Haltbarkeit (Jahrzehnte), günstig pro TB | Rein sequenzieller Zugriff, Laufwerk selbst teuer | Langzeitarchivierung, Disaster Recovery |

> **IHK-Typfrage:** *Warum ist der Einsatz von SMR-Festplatten in einem RAID-5-Verbund riskant?*
> **Musterantwort:** SMR-Festplatten schreiben Daten in überlappenden Spuren, wodurch das Ändern bereits geschriebener Daten (Rewrite) deutlich langsamer ist als bei CMR. Muss im Fehlerfall ein RAID-5-Array neu aufgebaut werden (Rebuild), erfordert das anhaltende, intensive Schreibvorgänge über die gesamte Platte – bei vielen (insbesondere host-managed oder für den Desktop-Einsatz ausgelegten) SMR-Platten kann dieser Vorgang so lange dauern, dass er Timeout-Grenzen des RAID-Controllers überschreitet oder das Risiko eines zweiten Plattenausfalls während der ungewöhnlich langen Rebuild-Zeit deutlich steigt, was im ungünstigen Fall zum Totalverlust des Arrays führen kann. Für RAID-/NAS-Einsatz sollten deshalb ausdrücklich vom Hersteller dafür freigegebene CMR- bzw. NAS-Laufwerke verwendet werden.

🟡 **Kontextwissen – "Air Gap":** Ein physisch vom Netzwerk getrenntes Speichermedium (wie ein Tape im Schrank) kann nicht durch Ransomware verschlüsselt werden, die sich über das Netzwerk verbreitet – das ist der Hauptgrund, warum LTO-Tapes trotz "veralteter" Technik weiterhin bei Backup-Strategien eingesetzt werden.

### 3.2 Die Protokoll-Evolution

| Schnittstelle | Zeitraum | Technik | Speed (max., historisch) | Besonderheit |
|---|---|---|---|---|
| IDE (PATA) | ca. 1986–2013 | Parallel | ~133 MB/s | Benötigt Master/Slave-Jumper-Konfiguration |
| SCSI | ca. 1981–2003 | Parallel | ~320 MB/s | Profi-Standard der 1990er, benötigte Terminierung |
| SATA | seit 2003 | Seriell | ~600 MB/s | Point-to-Point, Hot-Swap-fähig, Half-Duplex |
| SAS | seit 2004 | Seriell | SAS-2: 6 Gbit/s, SAS-3: 12 Gbit/s, SAS-4: 22,5 Gbit/s pro Lane (als Generation vermarktet unter dem Namen "24G SAS") | Full-Duplex, Server-Standard, zusätzliche Enterprise-Funktionen |

> **IHK-Typfrage:** *Warum bietet Full-Duplex (SAS) im Serverumfeld Vorteile gegenüber Half-Duplex (SATA)?*
> **Musterantwort:** Bei Half-Duplex (SATA) können Daten zu einem Zeitpunkt nur in eine Richtung übertragen werden (entweder lesen oder schreiben) – bei Full-Duplex (SAS) ist gleichzeitiges Lesen und Schreiben möglich. In Serverumgebungen mit vielen parallelen, gemischten Lese-/Schreibzugriffen (z. B. Datenbank- oder Virtualisierungsserver) erhöht das den effektiven Durchsatz spürbar. Der Duplex-Unterschied ist aber nicht der einzige Vorteil von SAS: Zusätzlich bietet SAS Enterprise-Funktionen wie Dual-Porting (Anbindung eines Laufwerks über zwei unabhängige Pfade) und SAS-Expander (Anschluss vieler Laufwerke über wenige Controller-Ports), die für große Server-Storage-Umgebungen ebenso wichtig sind.

🔴 **Stolperstein:** "SAS und SATA sind elektrisch dasselbe, nur anders benannt." Ein SATA-Stecker passt zwar in einen SAS-Controller (SAS-Controller sind meist abwärtskompatibel zu SATA-Laufwerken), umgekehrt passt ein SAS-Stecker aber physisch nicht in einen normalen SATA-Port – SAS nutzt ein anderes, komplexeres Protokoll und andere Signalpegel als reines SATA.

🟢 **Nice to know – IOPS:** Bei zufälligen (nicht-sequenziellen) 4K-Zugriffen bricht die Performance einer klassischen HDD drastisch ein, weil Schreib-/Lesekopf und Platter für jeden Zugriff neu physisch positioniert werden müssen (Seek-Zeit + Rotationslatenz) – SSDs haben dieses Problem nicht, da sie keine beweglichen Teile besitzen.

---

## 4. Massenspeicher II – Die Flash-Revolution

> **Grundprinzip:** "Mehr Bits pro Speicherzelle" bedeutet mehr Kapazität pro Fläche, aber auch weniger Haltbarkeit und geringere native Geschwindigkeit – ein bewusster Kompromiss, kein technischer Rückschritt.

### 4.1 Zell-Typen im Vergleich

> ⚠️ Die folgenden Werte sind grobe didaktische Größenordnungen zur Einordnung, keine allgemeingültigen oder garantierten technischen Werte – die tatsächliche Haltbarkeit hängt zusätzlich von NAND-Generation, Controller, Overprovisioning und Schreibmuster ab. Maßgeblich für die Praxis ist immer die vom Hersteller angegebene TBW- bzw. DWPD-Angabe des konkreten Produkts.

| Typ | Bits pro Zelle | P/E-Zyklen (grobe Orientierung) | Native Geschwindigkeit | Haltbarkeit (TBW, grobe Tendenz) |
|---|---|---|---|---|
| SLC | 1 | ~100.000 | Sehr hoch | Sehr hoch (Server-Einsatz) |
| MLC | 2 | ~10.000 | Hoch | Hoch (Server-Einsatz) |
| TLC | 3 | ~3.000 | Mittel | Mittel (Consumer-Standard) |
| QLC | 4 | ~1.000 | Niedriger (nativ) | Niedriger |

> **IHK-Typfrage:** *Würdest du für einen schreibintensiven Datenbank-Server QLC- oder TLC-Speicherzellen empfehlen?*
> **Musterantwort:** TLC ist hier tendenziell die bessere Wahl. Datenbank-Server erzeugen viele, teils zufällige Schreibvorgänge über die gesamte Lebensdauer – dabei ist die Haltbarkeit (ausgedrückt in TBW, Total Bytes Written) ein wichtiges Auswahlkriterium, die mit den P/E-Zyklen der Zellen zusammenhängt. QLC weist im Allgemeinen eine geringere Schreibreserven- und Dauerlast-Eignung als TLC auf; für schreibintensive Datenbanklasten sind daher meist Enterprise-TLC-SSDs mit passender TBW-/DWPD-Auslegung geeigneter. Für rein lesefokussierte oder wenig schreibintensive Anwendungen kann QLC dagegen wegen der höheren Kapazität pro Kosten sinnvoll sein – die konkrete Herstellerangabe zu TBW/DWPD des jeweiligen Produkts bleibt aber immer die maßgebliche Entscheidungsgrundlage, nicht der Zelltyp allein.

### 4.2 SLC-Cache und "Prospekt-Geschwindigkeit"

Viele QLC/TLC-SSDs nutzen einen Teil ihrer Zellen dynamisch als schnellen **SLC-Cache** (Pseudo-SLC-Modus), um kurzzeitig hohe Schreibgeschwindigkeiten zu erreichen. Ist dieser Cache bei sehr großen, anhaltenden Kopiervorgängen erschöpft, fällt die Geschwindigkeit auf die deutlich niedrigere native Geschwindigkeit der eigentlichen Zellen zurück.

> **IHK-Typfrage:** *Erkläre einem Kunden den Unterschied zwischen "Prospekt-Geschwindigkeit" und "realer Geschwindigkeit" beim Kopieren einer sehr großen Datei auf eine QLC-SSD.*
> **Musterantwort:** Die im Prospekt beworbene Spitzengeschwindigkeit gilt meist nur, solange der SLC-Cache der SSD noch Kapazität frei hat – dort werden Daten kurzzeitig sehr schnell zwischengespeichert. Bei einer sehr großen Datei, die die Kapazität dieses Zwischenspeichers übersteigt, muss die SSD auf die native Schreibgeschwindigkeit der eigentlichen QLC-Zellen zurückfallen, die deutlich niedriger liegt – der Kunde sieht dann mitten im Kopiervorgang einen spürbaren Geschwindigkeitseinbruch, obwohl das Produkt nicht defekt ist.

🟡 **Kontextwissen – Wear Leveling:** Der SSD-Controller verteilt Schreibvorgänge bewusst gleichmäßig über alle verfügbaren Speicherzellen, statt immer dieselben Zellen zu beschreiben – da jede Zelle nur eine begrenzte Anzahl an P/E-Zyklen erträgt, verlängert das die Gesamtlebensdauer der SSD spürbar.

### 4.3 Schnittstellen und Bandbreiten

| Schnittstelle | Protokoll | Typische max. Bandbreite (netto, Größenordnung) | Typischer Einsatz |
|---|---|---|---|
| SATA III | AHCI | ~560 MB/s | Office-PC, HDD-Ersatz |
| PCIe 3.0 x4 | NVMe | ~3.500 MB/s | Standard-Laptops |
| PCIe 4.0 x4 | NVMe | ~7.500 MB/s | High-End-PC |
| PCIe 5.0 x4 | NVMe | ~14.000 MB/s | Enthusiast, Workstation |
| UFS | SCSI-basiert | ~4.600 MB/s | High-End-Smartphones |
| eMMC | MMC | ~400 MB/s | Budget-Tablets (Half-Duplex) |

🟡 **Praxis-Tipp:** Die Zuordnung von PCIe-Generation zu einer bestimmten NVMe-Protokollversion (z. B. "PCIe 4.0 → NVMe 1.4") ist eine typische, aber keine zwingende Kombination – PCIe-Generation (die elektrische/physische Anbindung) und NVMe-Version (das Protokoll darüber) sind grundsätzlich unabhängig voneinander und werden von Hersteller zu Hersteller unterschiedlich kombiniert.

🔴 **Stolperstein:** "Random Read ist für die Nutzererfahrung weniger wichtig als die sequenzielle Transferrate." Für alltägliche Aufgaben wie Windows-/Programmstart ist meist die **Random-Read-Geschwindigkeit** entscheidender als die (in Prospekten meist beworbene) sequenzielle Transferrate, da beim Programmstart viele kleine, verstreut liegende Dateien gelesen werden – große, zusammenhängende Dateien (die von sequenzieller Geschwindigkeit profitieren) sind im Alltag seltener.

---

## 5. Bottleneck Detective

> **Grundprinzip:** Ein System ist immer nur so schnell wie sein langsamstes relevantes Glied – Bandbreiten lassen sich mit derselben Grundformel wie beim RAM (Takt × Busbreite) für praktisch jede Schnittstelle nachrechnen.

**Grundformel:** Datenrate = Takt × Busbreite

> **IHK-Typfrage:** *Eine Grafikkarte steckt in einem PCIe-3.0-x16-Slot, ist elektrisch aber nur mit x8 angebunden. Bestimme die maximale Bandbreite und erkläre die Konsequenz.*
> **Musterantwort:** Die maximale Bandbreite richtet sich nach der tatsächlichen elektrischen Anbindung (x8), nicht nach der mechanischen Slotgröße (x16) – bei PCIe 3.0 stehen pro Lane und Richtung ca. 985 MB/s (netto, nach Protokoll-/Kodierungs-Overhead) zur Verfügung, mit 8 Lanes also ca. 7,9 GB/s **pro Richtung** (PCIe ist bidirektional). Eine sehr leistungsstarke Grafikkarte, die theoretisch von x16 profitieren würde, kann durch die x8-Anbindung in Grenzfällen ausgebremst werden – in den meisten Spielen ist der Unterschied zwischen x8 und x16 aber gering; messbarer wird er eher bei Workloads mit besonders häufigem Datenaustausch zwischen Hauptspeicher und Grafikkarte (z. B. bestimmten Compute-/Streaming-Szenarien) als allein durch eine hohe Auflösung.

🔴 **Stolperstein:** "Eine schnelle CPU macht jedes System automatisch schneller." Beim Videoschnitt mit Zugriff auf eine langsame USB-2.0-Festplatte (max. ca. 60 MB/s) wartet selbst die schnellste CPU auf die eintreffenden Daten – der Flaschenhals liegt hier eindeutig bei der Speicherschnittstelle, nicht bei der Rechenleistung. Das Gesamtsystem ist immer nur so schnell wie sein langsamstes, für die jeweilige Aufgabe relevantes Glied.

🟡 **Kontextwissen – DMI-Flaschenhals:** Der Chipsatz (PCH) ist über eine Verbindung namens **DMI** (Direct Media Interface) an die CPU angebunden. Diese Verbindung hat eine begrenzte Gesamtbandbreite, die je nach DMI-Version und Plattform unterschiedlich ausfällt (grob in der Größenordnung mehrerer PCIe-Lanes) – neuere Plattformgenerationen bieten hier tendenziell mehr Bandbreite als ältere. Sind mehrere schnelle NVMe-SSDs, SATA-Ports und weitere Peripherie gleichzeitig über den Chipsatz angebunden, teilen sie sich diese eine DMI-Verbindung zur CPU – bei voller gleichzeitiger Auslastung mehrerer schneller Geräte kann das zum gemeinsamen Engpass werden, unabhängig von der Einzel-Bandbreite jedes Geräts. Das genaue DMI-Limit einer konkreten Plattform steht im jeweiligen Mainboard-/Chipsatz-Datenblatt.

🟢 **Nice to know – Lane-Sharing:** Manche Mainboards deaktivieren bestimmte SATA-Ports automatisch, sobald ein zusätzlicher M.2-Steckplatz belegt wird – Grund ist, dass sich beide Anschlüsse dieselben, begrenzt verfügbaren PCIe-Lanes bzw. Chipsatz-Ressourcen teilen. Das steht im Mainboard-Handbuch und ist ein klassischer Stolperstein bei der Systemplanung.

### USB-Generationen (Auszug)

| Bezeichnung (aktuell) | Frühere Bezeichnung | Geschwindigkeit |
|---|---|---|
| USB 3.2 Gen 1 | USB 3.0 / USB 3.1 Gen 1 | 5 Gbit/s |
| USB 3.2 Gen 2 | USB 3.1 Gen 2 | 10 Gbit/s |
| USB 3.2 Gen 2x2 | – | 20 Gbit/s |

🟡 **Praxis-Tipp:** Die USB-Namensgebung wurde vom USB-IF mehrfach rückwirkend umbenannt (z. B. hieß dieselbe 5-Gbit/s-Technik erst USB 3.0, dann USB 3.1 Gen 1, dann USB 3.2 Gen 1) – bei Datenblättern und Prüfungsfragen lohnt sich deshalb der Blick auf die tatsächliche Gbit/s-Angabe statt allein auf die Versionsbezeichnung. Wichtig für die Praxis: **USB-C bezeichnet nur die Steckerform**, nicht automatisch eine bestimmte Geschwindigkeit oder Norm (USB-C-Kabel/-Anschlüsse können z. B. USB 2.0, USB 3.2 oder Thunderbolt transportieren) – das ist ein häufiger Verwechslungspunkt bei Kunden und in Prüfungen.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Berechne die Bandbreite eines DDR4-2400-Moduls (Single-Channel). | 2400 MT/s × 8 Byte = 19.200 MB/s ≈ 19,2 GB/s |
| 2 | Warum ist Scheinleistung für die USV-Dimensionierung entscheidend? | Sie beschreibt die tatsächlich aus dem Netz bezogene Gesamtleistung (Wirk- + Blindleistung) |
| 3 | Warum sind SMR-Platten für RAID-5 riskant? | Extrem langsames Rewrite kann Rebuild-Vorgänge über Timeout-Grenzen verlängern |
| 4 | Was passiert, wenn der SLC-Cache einer QLC-SSD bei großen Dateien voll ist? | Die Geschwindigkeit fällt auf die niedrigere native Schreibgeschwindigkeit der QLC-Zellen zurück |
| 5 | Was bedeutet "elektrisch nur x4 angebunden" bei einem physischen x16-Slot? | Nur 4 der 16 Lanes sind tatsächlich verdrahtet – die Bandbreite entspricht der x4-Anbindung |
| 6 | Passt ein SAS-Stecker in einen normalen SATA-Port? | Nein – nur umgekehrt (SATA-Laufwerk in SAS-Controller) funktioniert meist |
| 7 | Was ist der DMI-Flaschenhals? | Die begrenzte Bandbreite der Chipsatz-CPU-Verbindung, die sich mehrere Chipsatz-Geräte teilen |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Bandbreite = Takt × Busbreite | Grundformel für RAM, Busse und viele weitere Schnittstellen |
| RDIMM/UDIMM | Registered (Server, Puffer-Chip) vs. Unbuffered (Consumer, Standard) |
| ECC-RAM | Zusätzlicher Speicherchip zur Bitfehler-Erkennung/-Korrektur (72 statt 64 Bit Busbreite) |
| Wirk-/Blind-/Scheinleistung | Nutzenergie / Pendelenergie / Gesamtleistung aus dem Netz (P, Q, S) |
| Aktive PFC | Minimiert Blindleistung, verbessert den Leistungsfaktor (cos φ) |
| 80 PLUS | Effizienzzertifizierung von Netzteilen (White bis Titanium) |
| CMR vs. SMR | Konventionell zuverlässig vs. hohe Kapazität, aber langsames Rewrite – für RAID/NAS explizit freigegebene CMR-/NAS-Laufwerke verwenden |
| LTO/Tape | Sequenzieller, aber langlebiger und "air-gap-fähiger" Archivspeicher |
| SATA vs. SAS | Half-Duplex, Consumer vs. Full-Duplex, Server-Standard |
| SLC/MLC/TLC/QLC | Zunehmend mehr Bits pro Zelle → mehr Kapazität, aber weniger Haltbarkeit/Geschwindigkeit |
| TBW | Total Bytes Written – Kennzahl für die Schreib-Haltbarkeit einer SSD |
| SLC-Cache | Dynamischer schneller Zwischenspeicher, dessen Erschöpfung die Geschwindigkeit einbrechen lässt |
| DMI | Verbindung zwischen Chipsatz und CPU, gemeinsam genutzter Flaschenhals für Chipsatz-Peripherie |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Bandbreiten-Rechnung | "Berechne die Bandbreite von X" | "Berechne die theoretische Bandbreite eines DDR5-5600-Moduls." | Vollständiger Rechenweg (MT/s × Byte), Ergebnis mit Einheit |
| Kosten-/Wirtschaftlichkeitsrechnung | "Berechne die Kosten von X über Zeitraum Y" | "Vergleiche die Stromkosten eines Bronze- und eines Gold-Netzteils über 3 Jahre." | Wirkungsgrad einbeziehen, vollständige Rechnung, nachvollziehbares Zwischenergebnis |
| Kompatibilitätsprüfung | "Funktioniert Komponente X in System Y?" | "Ein Kunde will RDIMM-Speicher in seinen Gaming-PC einbauen. Geht das?" | Konkrete technische Begründung, nicht nur Ja/Nein |
| Flaschenhals-Identifikation | "Wo liegt der Engpass im System?" | "Eine schnelle NVMe-SSD läuft in einem PCIe-3.0-Slot – was passiert?" | Engpass benennen + Bandbreiten-Vergleich als Beleg |

---

## Merk-Sätze fürs Fachgespräch

> Bandbreite = Takt × Busbreite ist eine Universalformel – ob RAM, PCIe oder Storage, das Prinzip bleibt gleich, nur die Einheiten ändern sich.

> Physisch passend heißt nicht elektrisch/logisch kompatibel – das gilt für RDIMM in Consumer-PCs genauso wie für x16-Slots mit x4-Anbindung.

> Ein überdimensioniertes Netzteil ist kein Sicherheitsgewinn, sondern oft ein Effizienzverlust – die meisten Netzteile arbeiten im mittleren Lastbereich (ca. 40–60 %) am wirtschaftlichsten, nicht nahe 100 % oder nahe 0 %.

> SMR spart Geld pro Terabyte, kostet aber im RAID-Ernstfall möglicherweise die gesamten Daten – die Technologie passt zum Einsatzzweck, nicht zu jedem Einsatzzweck.

> Prospekt-Geschwindigkeit gilt oft nur "solange der Cache reicht" – SLC-Cache bei SSDs und Effizienzangaben bei Netzteilen folgen demselben Muster: Randbedingungen zählen mehr als der Bestwert.

---

```yaml
lernfeld: LF2.3
titel: Infrastruktur & Energie
status: final
stand: 2026-09-16
quellen:
  - "LF2.3 – Infrastruktur & Energie"
  - "LF2.3.1 – Das Rückgrat & die Onboard-Welt"
  - "LF2.3.2 – Die Energiezentrale (PSU)"
  - "LF2.3.3 – Massenspeicher I: Die magnetische Ära & Protokolle"
  - "LF2.3.4 – Massenspeicher II: Die Flash-Revolution"
  - "LF2.3.5 – Bottleneck Detective"
review_historie:
  - runde: 1
    datum: 2026-08-27
    ergebnis: "Vorherige Korrekturrunde (vor dieser Session, Details nicht mehr im Volltext vorliegend): Bandbreitenformel, PFC, 80-PLUS-Spannungsbezug, Effizienzkurve, SAS-Versionen, SMR/RAID-Absolutheit und DMI-Pauschalisierung korrigiert. Status damals auf 'Review' belassen mit explizitem Hinweis, dass Zahlenangaben zu Kapazitäten, Preisen und Schnittstellen-Bandbreiten vor Unterrichtseinsatz noch gegengeprüft werden sollten."
  - runde: 2
    datum: 2026-09-16
    ergebnis: "Gezielte Web-Verifikation der im Status-Hinweis explizit als unsicher markierten Zahlenangaben. WICHTIGSTER FUND: 80-PLUS-Effizienztabelle enthielt keine Silver-Stufe (übersprang direkt von Bronze zu Gold) und die übrigen Prozentwerte waren uneinheitlich zwischen 115V-US- und 230V-EU-Norm gemischt, Titanium-Wert (94/96/94) entsprach keiner offiziellen Spezifikation. Tabelle komplett auf verifizierte, konsistente 230V-EU-Werte umgestellt (relevant für deutsche/europäische Zielgruppe, im Hinweistext oberhalb jetzt auch so benannt statt nur 'typische Beispielwerte'), Silver ergänzt, Titanium korrigiert (93/95/91 bei 20/50/100%) inkl. Ergänzung des vierten Messpunkts bei 10% Last als Nice-to-know. Das direkt folgende Stromkosten-Rechenbeispiel nutzte den alten, falschen Titanium-Wert (96% statt 95% bei 50%-Last) - komplett neu durchgerechnet (Differenz jetzt 25,1 W statt 28,4 W, Mehrkosten ca. 77,40 € statt 87,50 € über 5 Jahre), da sonst ein inkonsistenter Widerspruch zur korrigierten Tabelle entstanden wäre. Zweiter Fund (web-verifiziert gegen INCITS 534-2019 und mehrere unabhängige Quellen): SAS-4 wurde mit 24 Gbit/s pro Lane angegeben - die tatsächliche technische Leitungsrate ist 22,5 Gbit/s; '24G SAS' ist nur der Marketingname der Generation (Verdopplung von SAS-3s 12 Gbit/s gerundet). Korrigiert und der Marketingname als Erklärung ergänzt, damit die Diskrepanz zur Bezeichnung nachvollziehbar bleibt. Strompreis-Beispielwert (0,35 €/kWh) gegen aktuelle Marktdaten geprüft: liegt plausibel zwischen Bestandskunden-Durchschnitt (~31 Ct/kWh) und Grundversorgung (~37-40 Ct/kWh) im September 2026 - als bewusst gerundeter Beispielwert im Antworttext gekennzeichnet statt unkommentiert als exakter aktueller Wert stehen zu lassen. Alle anderen im Status-Hinweis genannten Zahlenbereiche (Bandbreitenformeln, PCIe-Lane-Werte, Storage-Schnittstellen-Geschwindigkeiten, Zell-Typ-Tabelle) beim Durchlesen plausibel und mit der bereits in Runde 1 eingeführten Hedging-Sprache ('grobe Orientierung', 'typische Größenordnung') konsistent - keine weiteren Fachfehler gefunden. Status von Review auf Final gesetzt."
```