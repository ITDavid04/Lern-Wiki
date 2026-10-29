# LF2.4 – Anbindung an die Außenwelt (Peripherie & I/O)

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 110–140 Min., mit Vertiefung (Rechenbeispiele, Nice-to-know): 150–180 Min.
> **Status:** Final
> **Stand:** 2026-08-27 – Versions- und Marktangaben (USB4, Thunderbolt, WiFi-Generationen) sollten vor Verwendung im Unterricht kurz gegengeprüft werden.

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was unterscheidet die physische Schnittstelle (Stecker/Kabel) vom logischen Protokoll? | [1](#1-kabel-protokolle--standards) |
| 2 | Wie berechnet man die für eine bestimmte Auflösung/Bildwiederholrate nötige Bandbreite, und was bedeutet DSC? | [2](#2-visuelle-ausgabe-monitore--video) |
| 3 | Wie funktioniert die Signalkette ADC/DAC, und was unterscheidet verlustfreie von verlustbehafteten Audioformaten? | [3](#3-auditive-ein---ausgabe) |
| 4 | Was bedeutet das Zwei-Sinne-Prinzip, und welche Rolle spielt das GS-Zeichen? | [4](#4-human-interface-devices-eingabe--ergonomie) |
| 5 | Warum ist "interpolierte Auflösung" bei Scannern reines Marketing, und was leistet der Blaue Engel bei Druckern? | [5](#5-hardcopy-drucken--scannen) |
| 6 | Warum ist 5 GHz-WLAN oft schneller als 2,4 GHz, obwohl die Reichweite geringer ist? | [6](#6-drahtlose-evolution-wireless) |

---

## 1. Kabel, Protokolle & Standards

> **Grundprinzip:** Das Kabel/der Stecker ist die Straße (Physis), das Protokoll die Verkehrsregel (Logik) – ein und derselbe Stecker kann ganz unterschiedliche "Verkehrsregeln" transportieren.

### 1.1 Physis vs. Protokoll

> **IHK-Typfrage:** *Ein USB-C-Stecker passt in mehrere Geräte, verhält sich aber unterschiedlich. Erkläre anhand eines Beispiels den Unterschied zwischen physischer Schnittstelle und Protokoll.*
> **Musterantwort:** Der USB-C-Stecker ist nur die physische Form (die "Straße") – über denselben Stecker können verschiedene Protokolle (die "Verkehrsregeln") laufen: reine USB-Daten, DisplayPort-Videosignale (DP Alt Mode), Strom (Power Delivery) oder Thunderbolt (PCIe-Tunneling). Zwei Geräte mit identisch aussehendem USB-C-Stecker können deshalb völlig unterschiedliche Fähigkeiten haben – ob eine Funktion (z. B. Laden, Video-Ausgabe, hohe Datenrate) unterstützt wird, hängt vom implementierten Protokoll ab, nicht vom Stecker allein. Standardisierungsgremien wie USB-IF (USB), VESA (DisplayPort) und PCI-SIG (PCIe) legen die jeweiligen Protokolle fest.

🔴 **Stolperstein:** "Mein Laptop lädt nicht am USB-C-Port des Monitors, obwohl der Stecker passt." Der Port muss zusätzlich **Power Delivery (PD)** unterstützen – ein passender Stecker allein reicht nicht, das zugrundeliegende Protokoll muss die gewünschte Funktion auch tatsächlich implementieren. Ebenso trügerisch: Viele einfache USB-C-**Ladekabel** unterstützen nur USB 2.0 (theoretisch max. 480 Mbit/s) – wer damit eine schnelle externe SSD anschließt, erreicht in der Praxis oft nur etwa 30–40 MB/s statt der eigentlich möglichen Geschwindigkeit. Grundsätzlich gilt: USB-C ist nicht automatisch USB 3.x, nicht automatisch Power Delivery und nicht automatisch DisplayPort Alt Mode – Kabel und Geräte können sich bei Datenrate, Ladeleistung und Video-Unterstützung erheblich unterscheiden, auch wenn der Stecker identisch aussieht.

### 1.2 Historie der kabelgebundenen Schnittstellen

| Schnittstelle | Zeitraum (ca.) | Max. Speed (brutto) | Besonderheit |
|---|---|---|---|
| USB 1.1 | ~1998 | 12 Mbit/s | Nur für einfache Eingabegeräte geeignet |
| FireWire 400 (IEEE 1394) | ~2000 | 400 Mbit/s | Stabiler Datenstrom als USB, aber teuer (Legacy) |
| USB 2.0 | 2000 | 480 Mbit/s | Datenübertragung erfolgt nicht gleichzeitig in beide Richtungen (kein echtes Vollduplex wie bei USB 3.x) |
| USB 3.0 (USB 3.2 Gen 1) | 2008 | 5 Gbit/s | Blaue Buchse (Kennfarbe), kann 2,4-GHz-WLAN stören |
| Thunderbolt 1 | 2011 | 10 Gbit/s | Teures Aktivkabel, Daisy-Chain-fähig (Apple-Fokus, Legacy) |
| USB 3.1 (USB 3.2 Gen 2) | 2013 | 10 Gbit/s | Effizientere Kodierung (128b/132b statt 8b/10b) |
| Thunderbolt 2 | 2013 | 20 Gbit/s | Nutzte noch Mini-DisplayPort-Stecker (nicht USB-C) |
| Thunderbolt 3 | 2015 | 40 Gbit/s | Nutzt USB-C-Stecker; Intel öffnete die Spezifikation 2019 zur lizenzgebührenfreien Implementierung |
| USB4 (Version 1.0) | 2019 | 20/40 Gbit/s | Baut u. a. auf von Intel eingebrachten Thunderbolt-3-Technologien auf, PCIe-Tunneling optional |
| Thunderbolt 4 | 2020 | 40 Gbit/s | Verbindliche Mindestanforderungen (u. a. mind. zwei 4K-Displays oder ein 8K-Display, garantierte PCIe-Mindestbandbreite) – stärker standardisiertes/zertifiziertes Profil als reines USB4 |
| USB4 Version 2.0 | 2022 (Spezifikation) | bis 80 Gbit/s symmetrisch | Neuere PAM-3-Signalisierung; höhere asymmetrische Modi optional, nicht jedes Gerät/Kabel unterstützt alle Geschwindigkeitsprofile |
| Thunderbolt 5 | 2024 | 80 Gbit/s bidirektional | Bei videointensiven Anwendungen per "Bandwidth Boost" bis zu 120 Gbit/s in Richtung Display (dafür reduzierte Gegenrichtung) – keine dauerhaften 120 Gbit/s in beide Richtungen |

> **IHK-Typfrage:** *Warum entsprechen 5 Gbit/s Brutto-Datenrate bei USB 3.0 nicht 500 MB/s Netto-Datendurchsatz für den Nutzer?*
> **Musterantwort:** USB 3.0 kodiert Daten mit **8b/10b-Kodierung**: Jedes 8-Bit-Datenbyte wird als 10-Bit-Symbol übertragen (Overhead von 20 %, u. a. zur Takt-Rückgewinnung beim Empfänger). Rechnerisch ergibt das aus 5 Gbit/s zunächst 4 Gbit/s Nutzdaten = 500 MB/s als reinen Kodierungs-Nettowert. Zusätzlicher Protokoll-Overhead (Paket-Rahmen, Flusskontrolle, Bestätigungen) reduziert den in der Praxis tatsächlich erreichbaren Durchsatz aber weiter auf realistisch ca. 400 MB/s oder etwas mehr – deutlich weniger als die oft missverstandenen "625 MB/s" (5 Gbit/s ÷ 8 ohne jeden Overhead).

🟡 **Praxis-Tipp:** Neuere USB-Generationen mit effizienterer 128b/132b-Kodierung (USB 3.1/3.2 Gen 2 und höher) haben nur noch ca. 3 % statt 20 % Kodierungs-Overhead – ein wichtiger Grund, warum sich die Netto-Geschwindigkeit von Gen 1 zu Gen 2 mehr als verdoppelt, obwohl sich die Brutto-Datenrate "nur" verdoppelt.

### 1.3 Netzwerk-Physis

| Medium | Typ | Eigenschaft |
|---|---|---|
| Twisted Pair (Kupfer) | Cat5e/Cat6a/Cat7/Cat8 | Steigende Frequenz/Schirmung mit höherer Kategorie; Stecker: RJ45 |
| LWL (Glasfaser) | Lichtwellenleiter | Unempfindlich gegen elektromagnetische Störungen (EMV); wichtig für lange Strecken (>100 m) oder Etagenverbindungen |

> **IHK-Typfrage:** *Warum kann LWL trotz höherer Kosten für eine Industriehalle die bessere Wahl gegenüber Kupferkabeln sein?*
> **Musterantwort:** In einer Industriehalle erzeugen große Motoren, Frequenzumrichter und Schaltvorgänge starke elektromagnetische Störfelder (EMV), die auf ungeschirmte oder auch geschirmte Kupferleitungen einstreuen und Datenübertragungsfehler verursachen können. Glasfaser überträgt Licht statt elektrischer Signale und ist deshalb praktisch immun gegen diese Störungen. Zusätzlich überbrückt LWL deutlich größere Distanzen (weit über 100 m) ohne Signalverstärkung – ein Vorteil, den Kupfer-Twisted-Pair-Kabel systembedingt nicht bieten.

---

## 2. Visuelle Ausgabe (Monitore & Video)

> **Grundprinzip:** Auflösung, Bildwiederholfrequenz und Farbtiefe bestimmen zusammen die nötige Übertragungsbandbreite – reicht die Schnittstelle nicht, sinkt automatisch eine dieser drei Größen.

### 2.1 Auflösungen im Überblick

| Bezeichnung | Pixel | Megapixel (ca.) | Status |
|---|---|---|---|
| HD Ready (720p) | 1280 × 720 | 0,9 MP | Veraltet |
| Full HD (1080p) | 1920 × 1080 | 2,1 MP | Standard im Büro |
| WQHD (1440p) | 2560 × 1440 | 3,7 MP | "Sweetspot" für 27 Zoll |
| UHD/4K | 3840 × 2160 | 8,3 MP | 4× so viele Pixel wie Full HD |

> **IHK-Typfrage:** *Berechne die exakte Pixelanzahl von WQHD und 4K/UHD. Um welchen Faktor hat 4K mehr Pixel als Full HD?*
> **Musterantwort:** WQHD: 2560 × 1440 = 3.686.400 Pixel (≈ 3,7 MP). UHD/4K: 3840 × 2160 = 8.294.400 Pixel (≈ 8,3 MP). Full HD hat 1920 × 1080 = 2.073.600 Pixel. Faktor 4K gegenüber Full HD: 8.294.400 ÷ 2.073.600 = genau **4** – UHD hat also exakt die vierfache Pixelanzahl von Full HD (doppelte Breite × doppelte Höhe = vierfache Fläche).

🔴 **Stolperstein:** "'4K' und 'UHD' sind dasselbe." Nahezu, aber nicht exakt: "4K" im Kino-/DCI-Standard ist mit 4096 Pixel Breite etwas breiter als "UHD" im TV-/Monitor-Bereich mit 3840 Pixel Breite – umgangssprachlich werden beide Begriffe aber meist synonym verwendet.

### 2.2 Schnittstellen-Bandbreiten (ab 2010, Auswahl)

| Standard | Jahr | Bandbreite (brutto) | Typische Auflösung @ 60 Hz | Besonderheit |
|---|---|---|---|---|
| HDMI 1.4 | 2009 | 10,2 Gbit/s | Full HD, 4K nur @ 30 Hz | Lange Zeit Standard in Beamern |
| DisplayPort 1.2 | 2010 | 17,2 Gbit/s | 4K @ 60 Hz | Multi-Stream (Daisy-Chain) möglich |
| HDMI 2.0 | 2013 | 18,0 Gbit/s | 4K @ 60 Hz | Statisches HDR |
| DisplayPort 1.4 | 2016 | 25,9 Gbit/s | 8K @ 60 Hz (mit DSC) | Standard bei Gaming-Monitoren, auch über USB-C (DP Alt Mode) |
| HDMI 2.1 | 2017 | 48,0 Gbit/s | 4K @ 120 Hz, 8K @ 60 Hz | Dynamisches HDR, VRR (Variable Refresh Rate) |
| DisplayPort 2.0/2.1 | 2019 | 80,0 Gbit/s | 16K @ 60 Hz | Oft über USB-C (USB4-Tunneling), benötigt UHBR-Zertifizierung |

> **IHK-Typfrage:** *Vergleiche HDMI 2.0 und DisplayPort 1.4 hinsichtlich Bandbreite und maximaler Auflösung bei 60 Hz.*
> **Musterantwort:** HDMI 2.0 bietet 18,0 Gbit/s Bandbreite und erreicht 4K bei 60 Hz. DisplayPort 1.4 bietet mit 25,9 Gbit/s deutlich mehr Bandbreite und kann durch zusätzlichen Einsatz von DSC (Display Stream Compression) sogar 8K bei 60 Hz darstellen. DisplayPort 1.4 ist damit sowohl bei roher Bandbreite als auch bei erreichbarer Maximalauflösung überlegen – ein wichtiger Aspekt für Gaming-Monitore mit hohen Auflösungen und Bildwiederholraten.

🟡 **Kontextwissen – DSC:** Display Stream Compression ist eine **"visually lossless"** Kompression – der Qualitätsverlust ist für das menschliche Auge unter typischen Betrachtungsbedingungen praktisch nicht wahrnehmbar. Im informationstheoretischen Sinne ist DSC aber **nicht verlustfrei** (anders als z. B. eine PNG-Komprimierung) – ein wichtiger Unterschied, der in der Prüfung abgefragt werden kann. DSC erlaubt es, Auflösungen zu übertragen, für die die rohe Bandbreite der Schnittstelle rechnerisch nicht ausreichen würde: Ein 8K-Signal (7680 × 4320) bei 60 Hz benötigt unkomprimiert deutlich mehr Bandbreite, als DisplayPort 1.4 (25,9 Gbit/s) bietet – erst durch DSC-Kompression wird die Übertragung über diese Schnittstelle möglich.

### 2.3 Display-Technologien im Vergleich

| Technologie | Funktionsweise | Typischer Einsatz | Vorteile | Nachteile |
|---|---|---|---|---|
| TN (LCD) | Kristalle drehen sich | E-Sports, Low-Budget | Sehr schnelle Reaktionszeit, günstig | Schlechter Blickwinkel, blasse Farben |
| IPS (LCD) | Kristalle drehen parallel | Grafikdesign, Büro, Allround | Exzellente Farben, stabiler Blickwinkel | "IPS Glow" (Leuchten im Dunkeln), etwas langsamer/teurer als TN |
| VA/PVA (LCD) | Kristalle stehen vertikal | TV, Curved-Monitore, Filme | Sehr hoher Kontrast, sattes Schwarz | "Ghosting" (Schlieren bei Bewegung) |
| W-OLED | Weißes OLED + Farbfilter | High-End-TV | Perfektes Schwarz, gute Haltbarkeit | Geringere Farbhelligkeit durch Filter, Burn-In-Risiko |
| QD-OLED | Blaues OLED + Quantenpunkte | High-End-Gaming-Monitore | Extrem reine Farben, sehr hell | Teuer, Textdarstellung an Kanten teils mit Farbsäumen |

🟡 **Kontextwissen:** "Burn-In" (dauerhaftes Einbrennen statischer Bildinhalte) ist ein bekanntes Risiko bei OLED-Technologien, das durch Alterungsmanagement (Pixel-Shifting, Helligkeitsbegrenzung) in modernen Geräten deutlich reduziert, aber nicht vollständig ausgeschlossen wird.

### 2.4 Farbtiefe und Bildwiederholfrequenz

| Farbtiefe | Abstufungen pro Kanal | Gesamtfarben | Verwendung |
|---|---|---|---|
| 8 Bit | 256 | ≈16,7 Millionen (256³) | Standard |
| 8 Bit + FRC | 256 (simuliert erweitert) | "Pseudo-10-Bit" | Günstigere Annäherung an 10-Bit-Darstellung durch schnellen Farbwechsel |
| 10 Bit (nativ) | 1024 | ≈1,07 Milliarden (1024³) | HDR, professionelles Color-Grading, vermeidet "Banding" |

🟡 **Praxis-Tipp:** "8 Bit + FRC" simuliert zusätzliche Zwischenfarben durch extrem schnellen Wechsel zwischen zwei benachbarten Farbwerten (Dithering) – für die meisten Alltagsanwendungen kaum vom nativen 10-Bit zu unterscheiden, für hochpräzises Color-Grading (z. B. medizinische Bildgebung) aber nicht gleichwertig.

🔴 **Stolperstein:** "Mein neuer 144-Hz-Monitor läuft nur mit 60 Hz." Häufige Ursache ist ein zu altes/nicht ausreichend spezifiziertes Kabel (z. B. altes HDMI-Kabel ohne die nötige Bandbreite) oder eine falsche Windows-Anzeigeeinstellung – nicht zwingend ein Defekt des Monitors.

---

## 3. Auditive Ein- & Ausgabe

> **Grundprinzip:** Schall ist analog (Wellen), Computer sind digital (0/1) – ADC und DAC sind die beiden Übersetzer zwischen diesen Welten.

### 3.1 Die Signalkette

| Baustein | Funktion |
|---|---|
| ADC (Analog-Digital-Converter) | Wandelt Schall in Zahlen (Aufnahme) |
| DAC (Digital-Analog-Converter) | Wandelt Zahlen in Spannung zurück (Wiedergabe) – steckt in jedem Lautsprecher/Kopfhörer-Signalweg (im PC, im USB-Stecker, im Bluetooth-Hörer) |

> **IHK-Typfrage:** *Berechne grob den Speicherbedarf für 1 Minute unkomprimiertes CD-Audio (Stereo, 44,1 kHz, 16 Bit).*
> **Musterantwort:** Rechnung: 44.100 Hz × 16 Bit × 2 Kanäle × 60 Sekunden ÷ 8 (Bit→Byte) = 84.672.000 ÷ 8 = 10.584.000 Byte ≈ **10,1 MB** (dezimal, ÷ 1.000.000) bzw. ≈ **10,09 MiB** (binär, ÷ 1.048.576) pro Minute Stereo-CD-Audio.

🟡 **Kontextwissen – Nyquist-Shannon-Abtasttheorem:** Um ein Signal mit einer bestimmten Maximalfrequenz verlustfrei rekonstruieren zu können, muss mit mehr als dem Doppelten dieser Frequenz abgetastet werden. Da der Mensch bis ca. 20 kHz hört, muss mit mehr als 40 kHz abgetastet werden – die CD-Abtastrate von 44,1 kHz liegt bewusst mit Sicherheitsabstand darüber.

### 3.2 Audioformate

| Kategorie | Format | Bitrate (typisch) | Verwendung |
|---|---|---|---|
| Unkomprimiert | WAV/AIFF (i. d. R. PCM-Container, meist ohne Kompression) | 1.411 kbit/s (CD-Qualität) | Studio, Archivierung |
| Lossless (verlustfrei) | FLAC | ~700–1.000 kbit/s | Musiksammlung, High-Res-Streaming |
| Lossless (verlustfrei) | ALAC | ~700–1.000 kbit/s | Apple-Ökosystem |
| Lossy (verlustbehaftet) | MP3 | 128–320 kbit/s | Kompatibilitäts-Standard |
| Lossy (verlustbehaftet) | AAC | ~128–256 kbit/s | YouTube, Apple-Geräte, teilweise Bluetooth-Audio (optional, nicht verpflichtend) |
| Lossy (verlustbehaftet) | Opus/Ogg | 32–160 kbit/s | VoIP, Discord, Spotify (sehr effizient) |

> **IHK-Typfrage:** *Warum verwenden verlustbehaftete Formate wie MP3 trotz geringerer Bitrate eine für die meisten Menschen kaum wahrnehmbare Qualitätseinbuße?*
> **Musterantwort:** Verlustbehaftete Formate nutzen **Psychoakustik**: Sie entfernen gezielt Frequenzanteile und Details, die das menschliche Gehör ohnehin kaum oder gar nicht wahrnimmt (z. B. sehr leise Töne, die von gleichzeitig lauteren Tönen ähnlicher Frequenz "maskiert" werden). Dadurch lässt sich die Datenmenge stark reduzieren, ohne dass die meisten Hörer einen deutlichen Qualitätsverlust bemerken – bei sehr niedrigen Bitraten oder empfindlichem Gehör wird der Unterschied aber wieder hörbar.

### 3.3 Bluetooth-Audio-Codecs

| Codec | Eigenschaft |
|---|---|
| SBC | Basis-Codec, von praktisch jedem Bluetooth-Gerät unterstützt, aber geringste Qualität |
| AAC | Häufig im Apple-Ökosystem eingesetzt, aber rechenintensiv; ob verfügbar, hängt von beiden verbundenen Geräten ab |
| aptX/aptX HD | Von Qualcomm entwickelt, gute Qualität, geringere Latenz, aber lizenzpflichtig |
| LDAC | Von Sony entwickelter Codec, nahezu Hi-Res (bis 990 kbit/s), seltener unterstützt |
| LC3 (LE Audio) | Neuerer Codec für Bluetooth LE Audio (seit Bluetooth 5.2), bietet bei gleicher Bitrate bessere Qualität und geringeren Energieverbrauch als SBC – zunehmend relevant für Hörgeräte und True Wireless Earbuds |

🔴 **Stolperstein:** "Ein teurer Bluetooth-Kopfhörer klingt an jedem Gerät gleich gut." Falsch – die tatsächlich genutzte Codec-Qualität hängt vom **schwächeren** der beiden verbundenen Geräte ab. Unterstützt das Quellgerät (z. B. ein älteres Smartphone) nur SBC, fällt die Verbindung auf diesen Basis-Codec zurück, selbst wenn der Kopfhörer eigentlich aptX oder LDAC beherrscht.

---

## 4. Human Interface Devices (Eingabe & Ergonomie)

> **Grundprinzip:** Ergonomie und Barrierefreiheit sind keine Kür, sondern normierte Anforderungen (GS-Zeichen, ISO-9241-Reihe) – "funktioniert" und "ist normkonform/gesundheitsgerecht" sind zwei unterschiedliche Fragen.

### 4.1 Normen & Sicherheit

| Norm/Siegel | Bedeutung |
|---|---|
| GS-Zeichen (Geprüfte Sicherheit) | Freiwilliges deutsches Prüfzeichen, das bestätigt, dass ein Produkt von einer zugelassenen Prüfstelle auf bestimmte sicherheitstechnische Anforderungen geprüft wurde – nicht speziell auf Eingabegeräte beschränkt und kein allgemeines Ergonomie-Siegel |
| DIN EN ISO 9241-Reihe | Normenreihe zur Ergonomie der Mensch-System-Interaktion (nicht ausschließlich physische Eingabegeräte, sondern auch Software-Ergonomie, Barrierefreiheit u. a.); die 400er-Unterreihe behandelt speziell physikalische Eingabegeräte |
| Zwei-Sinne-Prinzip | Barrierefreiheits-Grundsatz: Information muss über mindestens zwei unterschiedliche Sinneskanäle wahrnehmbar sein (z. B. Sehen + Hören oder Sehen + Tasten) |

> **IHK-Typfrage:** *Erläutere das Zwei-Sinne-Prinzip anhand einer Fehlermeldung am Computer – wie muss diese für einen blinden Nutzer wahrnehmbar gemacht werden?*
> **Musterantwort:** Eine Fehlermeldung, die nur farblich oder rein visuell vermittelt wird (z. B. ein rotes Popup-Fenster), verletzt das Zwei-Sinne-Prinzip, da sie nur über den Sehsinn wahrnehmbar ist. Der Inhalt sollte zusätzlich z. B. über einen Screenreader akustisch ausgegeben und für Nutzer einer Braillezeile strukturiert zugänglich gemacht werden – wichtig dabei: Der Screenreader kann den Inhalt nur vorlesen, wenn dieser technisch korrekt ausgezeichnet ist (z. B. über passende Alt-Texte/ARIA-Labels), eine akustische Ausgabe allein macht eine Meldung also nicht automatisch vollständig barrierefrei. Entscheidend ist, dass die Information nicht ausschließlich über einen einzigen Wahrnehmungskanal vermittelt wird.

### 4.2 Eingabegeräte im Überblick

| Kategorie | Typen |
|---|---|
| Tastaturen | Rubberdome (Standard), Mechanisch (präzise, langlebig, aber lauter), Scissor (flach) |
| Mäuse | Optisch (LED), Laser (funktioniert auf mehr Oberflächen als viele optische Sensoren, aber nicht zuverlässig auf jedem Glas/jeder spiegelnden Fläche), Trackball, Touchpad |
| Assistive Technology (motorisch) | Fingerführraster, Saug-Blas-Schalter, Kopfmaus, adaptive Kits |
| Assistive Technology (visuell) | Braille-Zeile, Großfeldtastatur, taktile Aufkleber |

🔴 **Stolperstein:** "Eine Vertikalmaus hilft bei jedem RSI-Syndrom (Repetitive Strain Injury)." Nicht zwingend – je nach Ursache der Beschwerden kann z. B. ein Trackball (Belastung über den Daumen statt über den ganzen Arm) die geeignetere Lösung sein. Ebenso ist eine "Gamer-Tastatur" (laute mechanische Switches) im Großraumbüro meist ungeeignet – nicht wegen fehlender Präzision, sondern wegen Lärmbelästigung der Kollegen.

🟡 **Praxis-Tipp – Software-Helfer:** Die **Einrastfunktion** (Sticky Keys) erlaubt es, Tastenkombinationen (z. B. Strg+Alt+Entf) nacheinander statt gleichzeitig zu drücken – wichtig für Nutzer mit motorischen Einschränkungen. Die **Anschlagverzögerung** ignoriert kurze, unbeabsichtigte Tastendrücke (z. B. durch Tremor).

---

## 5. Hardcopy (Drucken & Scannen)

> **Grundprinzip:** Die Wahl der Drucktechnologie ist eine Abwägung zwischen Seitenkosten, Geschwindigkeit, Dokumentenechtheit und Umweltbelastung – keine Technologie ist in jedem Szenario überlegen.

### 5.1 Drucker-Technologien

| Technologie | Funktionsweise | Typischer Einsatz | Vorteile | Nachteile |
|---|---|---|---|---|
| Laserdrucker | Bildtrommel + Toner + Hitze | Büro, Text, Archiv | Dokumentenecht, schnell, niedrige Seitenkosten | Feinstaub/Ozon-Emissionen, hoher Stromverbrauch |
| Tintenstrahl | Spritzt Flüssigtinte (Piezo/Bubble) | Home-Office, Foto | Fotorealistisch, günstig in der Anschaffung, kompakt | Tinte kann bei seltener Nutzung in den Düsen eintrocknen; Dokumentenechtheit/Wasserfestigkeit hängt stark von der Tintenart ab (pigmentbasiert: wasserfest/dokumentenecht; farbstoffbasiert: neigt eher zu Verblassen/Verlaufen) |
| Nadeldrucker | Nadeln schlagen auf Farbband | Durchschläge (Logistik, Rezepte) | Kopien/Durchschläge möglich, sehr robust | Sehr laut, langsam, schlechte Grafikqualität |
| Thermodruck | Hitze verfärbt Spezialpapier | Kassenbons, Etiketten | Kein Toner/Tinte nötig, sehr schnell | Papier verblasst, nicht archivfest |

> **IHK-Typfrage:** *Warum ist der Nadeldrucker in Arztpraxen und Speditionen trotz Lärm und geringer Grafikqualität weiterhin unverzichtbar?*
> **Musterantwort:** Der entscheidende Vorteil des Nadeldrucks ist die Fähigkeit, **Durchschläge** (mehrere Kopien in einem Druckvorgang über Kohle- oder Selbstdurchschreibepapier) zu erzeugen – eine Funktion, die Laser- und Tintenstrahldrucker technisch nicht bieten können. In Arztpraxen (mehrteilige Rezeptformulare) und in der Logistik (Lieferscheine mit mehreren Durchschlägen für unterschiedliche Empfänger) ist genau diese Eigenschaft unverzichtbar, weshalb der Nadeldrucker trotz sonstiger Nachteile dort weiterhin Standard ist.

### 5.2 Scanner-Technologien

| Technologie | Funktionsweise | Eigenschaft |
|---|---|---|
| CCD (Charge-Coupled Device) | System aus Linsen/Spiegeln | Hohe Tiefenschärfe (auch Buchrücken scanbar), hohe Farbtreue, aber mehr Platz-/Strombedarf |
| CIS (Contact Image Sensor) | Sensorzeile liegt direkt am Glas | Sehr flach/kompakt, USB-Strom reicht aus, aber kaum Tiefenschärfe (Papier muss plan aufliegen) |

🔴 **Stolperstein:** "Interpolierte Auflösung" bei Scannern wird oft als vermeintliches Qualitätsmerkmal beworben – nur die **optische** DPI-Angabe beschreibt die tatsächlich vom Sensor erfasste Auflösung. Beispiel: Ein Scanner wirbt mit "12.000 dpi interpoliert", die optische Auflösung beträgt aber nur 4.800 dpi – die zusätzlichen 12.000 dpi sind eine Software-Hochrechnung (vergleichbar einem Digital-Zoom) und fügen keine echten zusätzlichen Bildinformationen hinzu. Für bestimmte Zwecke (z. B. OCR-Texterkennung oder Barcode-Verarbeitung) kann Interpolation dennoch praktisch nützlich sein – sie ersetzt aber nicht die optische Auflösung als Qualitätsmaß.

### 5.3 Der Blaue Engel (DE-UZ 219)

Das Umweltsiegel prüft bei Druckern u. a.: **Emissionsgrenzwerte** (Ultrafeinstaub, Ozon, Lärm), **Energieverbrauch** (u. a. anhand des TEC-Werts – Typical Electricity Consumption, der typische Verbrauch über einen definierten Nutzungszyklus inkl. Betrieb und Bereitschaft, nicht nur der reine Standby-Wert), **Langlebigkeit/Reparierbarkeit** (u. a. Ersatzteilverfügbarkeit) und die Fähigkeit, **100 % Recyclingpapier** zu verarbeiten. Die konkreten Anforderungen (z. B. genaue Jahresangaben zur Ersatzteilverfügbarkeit) sind in der jeweils gültigen Vergabekriterien-Ausgabe (aktuell u. a. DE-UZ 219) festgelegt und können sich mit neuen Ausgaben ändern.

> **IHK-Typfrage:** *Warum stinkt ein Laserdrucker während des Betriebs, und was hilft dagegen?*
> **Musterantwort:** Der typische Geruch entsteht durch **Ozon** (durch die Koronaentladung bei der elektrostatischen Aufladung der Bildtrommel) und **Styrol**-Ausdünstungen aus dem erhitzten Toner. Abhilfe schaffen ein **Aktivkohlefilter** im Gerät (baut Ozon chemisch ab) sowie ausreichendes **Lüften** des Raumes – bei Geräten mit dem Blauen Engel sind die entsprechenden Emissionsgrenzwerte bereits durch die Zertifizierung begrenzt.

---

## 6. Drahtlose Evolution (Wireless)

> **Grundprinzip:** Höhere Frequenz bedeutet mehr mögliche Datenrate, aber schlechtere Durchdringung von Materie (Wänden) – ein physikalischer Kompromiss, keine reine Qualitätsfrage.

### 6.1 WLAN-Frequenzbänder

| Frequenz | Reichweite | Durchdringung | Geschwindigkeit | Störanfälligkeit |
|---|---|---|---|---|
| 2,4 GHz | Sehr hoch | Gut (Wände) | Mittel | Hoch (Mikrowelle, Bluetooth, viele Nachbar-WLANs, nur 3 nicht überlappende Kanäle) |
| 5 GHz | Mittel | Mäßig | Hoch | Mittel (Radar/DFS-Pflicht in bestimmten Kanälen) |
| 6 GHz | Gering | Schlecht | Extrem hoch | Sehr gering (noch wenig genutzt) |

> **IHK-Typfrage:** *Warum ist 5-GHz-WLAN oft schneller als 2,4-GHz-WLAN, auch wenn der Router gleich weit entfernt steht?*
> **Musterantwort:** Im 2,4-GHz-Band stehen in Europa als Faustregel typischerweise nur die drei überlappungsfreien 20-MHz-Kanäle 1, 6 und 11 zur Verfügung. Im 5-GHz-Band existieren deutlich mehr Kanäle und häufig größere Kanalbreiten (die genaue Anzahl hängt von Land, Kanalbreite und DFS-Nutzung ab), wodurch unter geeigneten Bedingungen höhere Datenraten möglich sind. Zudem ist 2,4 GHz durch die enorme Verbreitung anderer Geräte (u. a. Mikrowellen, Bluetooth, benachbarte WLANs) stärker durch Interferenzen belastet. Die höhere Frequenz von 5 GHz bedeutet zwar eine geringere Reichweite und schlechtere Wanddurchdringung, ermöglicht aber bei ausreichender Signalstärke einen saubereren, schnelleren Kanal.

### 6.2 Regulierung (Bundesnetzagentur)

| Frequenzbereich | Max. Sendeleistung (EIRP, grobe Richtwerte) | Einschränkung |
|---|---|---|
| 2,4 GHz (2400–2483,5 MHz) | 100 mW | Allgemeinzuteilung |
| 5,15–5,35 GHz (Indoor) | 200 mW | Nur Indoor, teils DFS/TPC |
| 5,47–5,725 GHz | bis 1000 mW | DFS/TPC-Pflicht |
| 6 GHz, LPI (5945–6425 MHz) | 200 mW (23 dBm), nur Indoor | Neueres Band, noch wenig genutzt |
| 6 GHz, VLP | 25 mW (14 dBm), Indoor/Outdoor möglich | Eigene Gerätekategorie mit geringerer Leistung |

🟡 **Kontextwissen:** Die genauen EIRP-Grenzwerte sind je nach konkretem Frequenzbereich innerhalb des 5-GHz-Bands unterschiedlich geregelt (die Tabelle zeigt grobe Richtwerte, keine vollständige Rechtsgrundlage) und teils an **DFS** (Dynamic Frequency Selection) sowie **TPC** (Transmit Power Control) gekoppelt – Schutzmechanismen, die WLAN-Geräte zwingen, bestimmte Kanäle bei Erkennung von Radarsignalen (z. B. in Flughafennähe) automatisch zu verlassen bzw. die Sendeleistung dynamisch anzupassen.

🔴 **Stolperstein:** "Ich darf die Sendeleistung meines Routers einfach erhöhen, wenn die Software das zulässt." Die Sendeleistung ist gesetzlich durch die Bundesnetzagentur begrenzt (EIRP-Grenzwerte) – eine Überschreitung ist unzulässig, unabhängig davon, ob die Firmware des Geräts technisch eine höhere Einstellung erlauben würde.

### 6.3 WLAN-Evolution (IEEE 802.11)

| Jahr | Standard | Marketing-Name | Frequenz | Max. Speed (brutto, theoretisch) | Besonderheit |
|---|---|---|---|---|---|
| 1999 | 802.11b | – | 2,4 GHz | 11 Mbit/s | Durchbruch für die Massenverbreitung |
| 2003 | 802.11g | – | 2,4 GHz | 54 Mbit/s | Standard der 2000er-Jahre |
| 2009 | 802.11n | WiFi 4 | 2,4/5 GHz | 600 Mbit/s | MIMO (mehrere Antennen) |
| 2014 | 802.11ac | WiFi 5 | 5 GHz | ~3,5 Gbit/s | Beamforming |
| 2019 | 802.11ax | WiFi 6 | 2,4/5 GHz | ~9,6 Gbit/s | Effizienzsteigerung durch OFDMA |
| 2024 | 802.11be | WiFi 7 | 2,4/5/6 GHz | ~46 Gbit/s | Multi-Link Operation (MLO) |

> ⚠️ Die angegebenen Maximalwerte sind theoretische Bruttowerte unter Idealbedingungen (mehrere Antennen/Streams, breitester Kanal) – die tatsächlich an einem einzelnen Endgerät ankommende Geschwindigkeit liegt in der Praxis meist deutlich darunter.

🔴 **Stolperstein:** "WiFi 7 macht mein Internet automatisch schneller." Ein neuerer WLAN-Standard verbessert nur die Verbindung zwischen Endgerät und Router/Access Point – ist der Internetanschluss selbst auf z. B. 50 Mbit/s begrenzt, bringt WiFi 7 dafür keinen Vorteil (wohl aber für interne Übertragungen im lokalen Netzwerk, z. B. zu einem NAS).

### 6.4 Bluetooth: Evolution & Technik

Bluetooth wurde 1994 von Ericsson entwickelt und nutzt **FHSS** (Frequency Hopping Spread Spectrum) im 2,4-GHz-Band – das Signal springt ca. 1.600-mal pro Sekunde zwischen verschiedenen Frequenzen, um Kollisionen mit anderen Nutzern des Bandes (u. a. WLAN) zu vermeiden bzw. zu minimieren.

| Version | Jahr (ca.) | Speed | Reichweite (ca.) | Neuerung |
|---|---|---|---|---|
| 1.0–1.2 | ~1999 | 732 kbit/s | ~10 m | Frühe, noch unsichere Implementierung |
| 2.0 + EDR | 2004 | 2,1 Mbit/s | ~10 m | EDR (Enhanced Data Rate), Standard für Audio |
| 4.0–4.2 | 2010 | 1 Mbit/s (LE) | ~50 m | Bluetooth Low Energy (BLE) – Durchbruch für IoT/Wearables |
| 5.0–5.4 | 2016 | 2 Mbit/s (LE) | ~200 m (theoretisch, Idealbedingungen; in Innenräumen praktisch eher 50–100 m) | Mesh-Netzwerke, Audio Sharing, Direction Finding, LE Audio mit LC3-Codec (ab 5.2) |

> **IHK-Typfrage:** *Warum läuft eine Smartwatch wochenlang mit einer Akkuladung, während ein Bluetooth-Headset täglich geladen werden muss?*
> **Musterantwort:** Eine Smartwatch nutzt meist **Bluetooth Low Energy (BLE)**, das für sehr geringen Energieverbrauch bei kleinen, unregelmäßigen Datenmengen (Benachrichtigungen, Sensordaten) optimiert ist – der Funkchip verbringt die meiste Zeit in einem Ruhezustand. Ein Bluetooth-Headset benötigt dagegen einen kontinuierlichen, verzögerungsarmen Audio-Datenstrom (Bluetooth Classic mit Audio-Codec wie SBC/AAC/aptX), was einen deutlich höheren und permanenten Energiebedarf verursacht – daher die deutlich kürzere Akkulaufzeit trotz ähnlicher Batteriegröße.

> **IHK-Typfrage (Rechenbeispiel):** *Ein WLAN-Signal hat vor einer Stahlbetonwand eine Signalstärke von -50 dBm. Die Wand dämpft das Signal um 15–20 dB. Reicht die Signalstärke danach noch für eine stabile Verbindung (als Modellannahme: Minimum -70 dBm)?*
> **Musterantwort:** Nach der Dämpfung ergibt sich ein Wertebereich von -50 dBm - 15 dB = **-65 dBm** bis -50 dBm - 20 dB = **-70 dBm**. Der Wert liegt damit im besten Fall bei -65 dBm (deutlich über dem angenommenen Minimum) und im ungünstigsten Fall genau auf der Grenze von -70 dBm. Die Verbindung ist also grenzwertig bis ausreichend stabil – zusätzliche Faktoren (weitere Wände, Störquellen, Entfernung) könnten sie in der Praxis unter die nutzbare Schwelle drücken. dBm-Werte sind hierbei logarithmisch: -70 dBm ist ein deutlich schwächeres Signal als -50 dBm, auch wenn der Zahlenunterschied klein wirkt. Der Wert -70 dBm ist für dieses Rechenbeispiel eine vereinfachte Modellannahme – in der Praxis gibt es keine universelle, für jede Anwendung gültige Mindest-Signalstärke; die tatsächlich benötigte Schwelle hängt zusätzlich von Modulation, Störabstand (SNR) und Anwendung ab.

🟡 **Kontextwissen:** Bluetooth und 2,4-GHz-WLAN nutzen dasselbe Frequenzband und können sich trotz FHSS gegenseitig stören, insbesondere bei hoher Gerätedichte oder wenn beide Technologien gleichzeitig auf stark überlappenden Frequenzbereichen aktiv sind (z. B. viele Bluetooth-Geräte plus mehrere überlappende WLAN-Netze in einem Großraumbüro).

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Was ist der Unterschied zwischen Stecker und Protokoll bei USB-C? | Stecker = physische Form; Protokoll (USB-Daten, DP, PD, Thunderbolt) bestimmt die tatsächliche Funktion |
| 2 | Warum entsprechen 5 Gbit/s USB 3.0 nicht 500 MB/s beim Nutzer in der Praxis? | 8b/10b-Kodierung (20 % Overhead) ergibt rechnerisch 500 MB/s Rohwert; weiterer Protokoll-Overhead senkt den realen Wert auf ca. 400 MB/s |
| 3 | Wie viele Pixel hat ein 4K/UHD-Bild, und um welchen Faktor mehr als Full HD? | 8.294.400 Pixel, Faktor 4 |
| 4 | Was ist der Unterschied zwischen CCD- und CIS-Scannern? | CCD: mehr Tiefenschärfe (Buchrücken), mehr Platz/Strom; CIS: flach/kompakt, aber ohne Tiefenschärfe |
| 5 | Was besagt das Zwei-Sinne-Prinzip? | Information muss über mindestens zwei unabhängige Sinneskanäle wahrnehmbar sein |
| 6 | Warum ist "interpolierte Auflösung" bei Scannern kritisch zu sehen? | Sie ist softwareseitig hochgerechnet, nur die optische DPI zählt echte Bildinformation |
| 7 | Warum läuft eine Smartwatch länger als ein Bluetooth-Headset mit gleicher Akkugröße? | Smartwatch nutzt BLE (sehr sparsam), Headset braucht kontinuierlichen Audio-Datenstrom |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Physis vs. Protokoll | Stecker/Kabel (Straße) vs. übertragene Logik (Verkehrsregel) – ein Stecker kann mehrere Protokolle transportieren |
| 8b/10b vs. 128b/132b | Kodierungsverfahren mit 20 % bzw. ca. 3 % Overhead – erklärt den Unterschied zwischen Brutto- und Nettodatenrate |
| USB4 / Thunderbolt | USB4 v1.0 (2019, 20/40 Gbit/s) und v2.0 (2022, bis 80 Gbit/s) bauen auf Thunderbolt-3-Technologie auf; Thunderbolt 4 (2020, 40 Gbit/s) und Thunderbolt 5 (2024, 80/120 Gbit/s) sind parallele Intel-Standards mit strengeren Mindestanforderungen |
| DSC | Display Stream Compression – erlaubt höhere Auflösungen als die rohe Bandbreite erlauben würde |
| ADC/DAC | Analog→Digital (Aufnahme) / Digital→Analog (Wiedergabe) |
| Lossy vs. Lossless | Verlustbehaftet (MP3, AAC, Opus) vs. verlustfrei (FLAC, ALAC, WAV) |
| Zwei-Sinne-Prinzip | Information muss über ≥ 2 unabhängige Sinneskanäle zugänglich sein |
| GS-Zeichen | Freiwilliges deutsches Sicherheitsprüfzeichen; kein allgemeines Qualitäts- oder Ergonomiesiegel |
| CCD vs. CIS | Tiefenschärfe + mehr Platz/Strom vs. flach/kompakt ohne Tiefenschärfe |
| Blauer Engel (DE-UZ 219) | Umweltsiegel für Drucker: Emissionen, Energieverbrauch, Langlebigkeit, Recyclingpapier |
| EIRP | Äquivalente isotrope Strahlungsleistung – berücksichtigt Sendeleistung und Antennengewinn, gesetzlich begrenzt durch die Bundesnetzagentur |
| DFS | Radar-Schutzmechanismus, der WLAN-Geräte zum Kanalwechsel zwingt |
| FHSS | Frequency Hopping Spread Spectrum – Bluetooth-Frequenzsprungverfahren |
| BLE | Bluetooth Low Energy – sehr sparsam, für IoT/Wearables |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Rechenaufgabe | "Berechne X" | "Berechne den Speicherbedarf für 3 Minuten CD-Audio." | Vollständiger Rechenweg, Ergebnis mit Einheit (MB/MiB unterscheiden) |
| Ursache-Wirkung | "Warum entspricht X nicht Y?" | "Warum entsprechen 10 Gbit/s USB nicht 1.250 MB/s?" | Kodierungs-Overhead + Protokoll-Overhead getrennt benennen |
| Technologievergleich | "Vergleiche X und Y für Einsatzzweck Z" | "Vergleiche CCD und CIS für das Scannen eines gebundenen Buches." | Konkrete Empfehlung + fachliche Begründung (Tiefenschärfe) |
| Normkonformität prüfen | "Erfüllt X die Anforderung Y?" | "Erfüllt ein reiner Touchscreen-Kiosk das Zwei-Sinne-Prinzip für blinde Nutzer?" | Norm/Prinzip korrekt anwenden, konkrete Lösung vorschlagen |

---

## Merk-Sätze fürs Fachgespräch

> Stecker und Protokoll sind zwei getrennte Fragen – ein passender USB-C-Stecker sagt nichts darüber, ob Laden, Video oder hohe Datenraten tatsächlich unterstützt werden.

> Brutto-Datenraten sind Marketing, Netto-Datenraten sind Realität – Kodierungs- und Protokoll-Overhead fressen bei jeder seriellen Schnittstelle einen Teil der beworbenen Geschwindigkeit.

> Höhere Frequenz bedeutet mehr Bandbreite, aber schlechtere Wanddurchdringung – 2,4 GHz, 5 GHz und 6 GHz sind ein physikalischer Kompromiss, keine gestaffelte Qualitätsleiter.

> Das Zwei-Sinne-Prinzip ist erfüllt, wenn Information über zwei unabhängige Sinneskanäle zugänglich ist – nicht schon, wenn sie besonders gut sichtbar dargestellt wird.

> Interpolierte Auflösung ist Software-Zoom, keine echte zusätzliche Bildinformation – nur die optische Auflösung zählt fachlich.

---

```yaml
lernfeld: LF2.4
titel: Anbindung an die Außenwelt (Peripherie & I/O)
status: final
stand: 2026-08-27
quellen:
  - "LF2.4 – Anbindung an die Außenwelt (Peripherie & I/O)"
  - "LF2.4.1 – Kabel, Protokolle & Standards"
  - "LF2.4.2 – Visuelle Ausgabe (Monitore & Video)"
  - "LF2.4.3 – Auditive Ein- & Ausgabe"
  - "LF2.4.4 – Human Interface Devices (Eingabe & Ergonomie)"
  - "LF2.4.5 – Hardcopy (Drucken & Scannen)"
  - "LF2.4.6 – Drahtlose Evolution (Wireless)"
```