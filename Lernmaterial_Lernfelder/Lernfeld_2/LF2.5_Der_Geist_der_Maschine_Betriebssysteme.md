# LF2.5 – Der Geist der Maschine (Betriebssysteme)

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Kerninhalt: 130–160 Min., mit Vertiefung (Nice-to-know, Historie-Details): 170–200 Min.
> **Status:** Final
> **Stand:** 2026-08-27 – Marktanteile und aktuelle Sicherheitsfunktionen sollten vor Verwendung im Unterricht kurz gegengeprüft werden.

**Legende:** 🔴 Prüfungsstoff (hohe Relevanz) · 🟡 Kontextwissen (mittlere Relevanz) · 🟢 Nice to know

---

## IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was unterscheidet Ring 0 von Ring 3, und warum ist ein Kontextwechsel dazwischen "teuer"? | [1](#1-die-architektur-der-macht-ringe--firmware) |
| 2 | Welche Kernaufgaben übernimmt ein Betriebssystem, und welches Dateisystem passt zu welchem Einsatzzweck? | [2](#2-der-system-verwalter-os-grundlagen--dateisysteme) |
| 3 | Was unterscheidet Batch-Processing von Time-Sharing? | [3](#3-die-ahnenreihe-der-betriebssysteme) |
| 4 | Warum wurden die DOS- und NT-Linie von Windows erst mit XP vereint? | [4](#4-windows) |
| 5 | Warum brauchte Linus Torvalds das GNU-Projekt, obwohl er einen eigenen Kernel geschrieben hatte? | [5](#5-linux) |
| 6 | Was unterscheidet Sideloading (Android) vom App-Store-Zwang (iOS) sicherheitstechnisch? | [8](#8-mobile-welten-android--ios) |

---

## 1. Die Architektur der Macht (Ringe & Firmware)

> **Grundprinzip:** Ein Betriebssystem hat zwei Kernaufgaben – Abstraktion (komplexe Hardware hinter einfachen Konzepten verstecken) und Ressourcen-Management (CPU-Zeit, RAM und Geräte fair verteilen). Das Ring-Modell sichert ab, dass fehlerhafte oder böswillige Software nicht das gesamte System gefährden kann.

### 1.1 Das Ring-Modell

> 🟡 Das folgende Modell beschreibt die klassische Privilegienstufen-Architektur von **x86-Systemen**. Andere Architekturen (z. B. ARM mit sog. Exception Levels wie EL0/EL1) verwenden abweichende, aber konzeptionell ähnliche Schutzmechanismen. Ring -3/-2/-1 sind zudem keine offiziellen x86-Ring-Bezeichnungen im engeren Sinne, sondern eine in der Lehre und IT-Sicherheit gebräuchliche, anschauliche Erweiterung des klassischen Ring-0-bis-3-Modells um hardwarenahe Kontrollebenen: Die Intel Management Engine ist technisch eine separate, im Chipsatz integrierte Firmware-/Management-Komponente (kein CPU-Ring im eigentlichen Sinne), SMM ist ein spezieller CPU-Betriebsmodus, und Virtualisierung nutzt eigene CPU-Erweiterungen wie Intel VT-x oder AMD-V.

| Ring | Ebene | Beispiel | Risiko bei Kompromittierung |
|---|---|---|---|
| Ring -3 | Hardware (Intel Management Engine/ME) | Läuft auf dem Chipsatz, auch im Standby, mit eigenem Mini-Betriebssystem | Bei einer Kompromittierung theoretisch weitreichender, für das Hauptsystem kaum sichtbarer Zugriff – ein in der Fachwelt kontrovers diskutiertes Sicherheitsrisiko |
| Ring -2 | Hardware (SMM – System Management Mode) | Regelt u. a. Strom-/Lüftersteuerung, für das OS unsichtbar | Rootkits könnten sich hier theoretisch verstecken |
| Ring -1 | Virtualisierung (Hypervisor, z. B. ESXi, Hyper-V) | Verwaltet virtuelle Maschinen, kontrolliert Ring 0 | Kompromittierter Hypervisor kontrolliert alle darunter laufenden Gast-Betriebssysteme |
| Ring 0 | Kernel | Betriebssystem-Kern, Treiber – voller Hardwarezugriff | Systemabsturz (BSOD/Kernel Panic) |
| Ring 1/2 | (praktisch ungenutzt) | Theoretisch für Treiber vorgesehen, in der Praxis bei den meisten modernen OS kaum verwendet | – |
| Ring 3 | User Space | Anwendungen – kein direkter Hardwarezugriff, muss Ring 0 per System Call bitten | App-Absturz, OS läuft in der Regel weiter |

> **IHK-Typfrage:** *Beschreibe den Ablauf eines System Calls und begründe, warum der Übergang zwischen User Space (Ring 3) und Kernel Space (Ring 0) aus Sicht der Systemleistung als "teuer" gilt.*
> **Musterantwort:** Möchte ein Programm in Ring 3 eine privilegierte Operation ausführen (z. B. eine Datei schreiben), kann es nicht direkt auf die Hardware zugreifen, sondern muss einen System Call auslösen. Die CPU wechselt dabei vom User Mode in den Kernel Mode, sichert bestimmte Ausführungsinformationen, führt die angeforderte Operation im Kernel aus und wechselt anschließend wieder zurück nach Ring 3. Dieser Übergang gilt als "teuer", weil ein kontrollierter Wechsel in den privilegierten Kernel-Modus, zusätzliche Prüfungen und das Sichern von Ausführungsinformationen zusätzliche CPU-Zyklen kosten – bei sehr häufigen System Calls (z. B. in schlecht optimierter I/O-lastiger Software) kann sich das spürbar auf die Performance auswirken. Wichtig zur Einordnung: Der Übergang in den Kernel-Modus ist nicht automatisch mit einem vollständigen Prozess-/Thread-Kontextwechsel gleichzusetzen – ein solcher entsteht erst, wenn der Kernel anschließend tatsächlich einen anderen Thread einplant (z. B. weil der aktuelle blockiert oder auf I/O wartet); oft kann der Kernel nach der Bearbeitung einfach zum selben Thread zurückkehren.

🔴 **Stolperstein:** "Ein Webbrowser könnte theoretisch direkt auf die Webcam zugreifen, wenn er wollte." Anwendungen laufen in Ring 3 ohne direkten Hardwarezugriff – jeder Zugriff auf Geräte wie die Webcam läuft über Betriebssystem-APIs und Gerätetreiber, wobei das Betriebssystem Berechtigungen prüfen und den Zugriff anzeigen oder protokollieren kann. Ein Berechtigungs-Popup bei jedem einzelnen Zugriff ist dabei aber nicht garantiert – ob eine explizite Nachfrage erscheint, hängt u. a. von Betriebssystem, bereits erteilten Berechtigungen und Unternehmensrichtlinien ab. Diese grundsätzliche Trennung zwischen Anwendung und Hardware ist aber kein Zufall, sondern der Kern des Sicherheitsmodells.

🟡 **Kontextwissen – Firmware:** Das klassische **BIOS** arbeitet in einer historischen 16-Bit-Umgebung und wurde weitgehend durch **UEFI** abgelöst – eine modernere Firmware-Schnittstelle, die kein bestimmtes CPU-Bitformat vorschreibt; moderne PC-Systeme nutzen aber typischerweise 64-Bit-fähige UEFI-Umgebungen. UEFI bietet u. a. **Secure Boot**, das prüft, ob Bootloader und bestimmte Firmware-Komponenten von einer vertrauenswürdigen Stelle signiert wurden, und dadurch das Einschleusen vieler unsignierter Bootkits erschwert. Ein vollständiger Schutz vor sämtlichen Rootkits ist es aber nicht – ist beispielsweise ein vertrauenswürdiger Signaturschlüssel selbst kompromittiert, kann Secure Boot die betreffende Schadsoftware unter Umständen nicht erkennen.

🟢 **Nice to know:** Der sogenannte **"Blue Pill"**-Angriff (vorgestellt von Joanna Rutkowska, 2006) beschreibt konzeptionell, wie ein bereits laufendes Betriebssystem nachträglich unbemerkt in eine virtuelle Maschine "verschoben" werden könnte (Ring -1), ohne dass das OS selbst dies bemerkt – ein anschauliches Beispiel dafür, warum der Hypervisor eine noch weitreichendere Kontrollposition hat als der Kernel selbst.

---

## 2. Der System-Verwalter (OS-Grundlagen & Dateisysteme)

> **Grundprinzip:** Ohne Betriebssystem ist Hardware nutzlos – Anwendungen kennen nur logische Konzepte ("C:\Dokumente\Brief.txt"), nicht die physische Realität dahinter ("Sektor 512 auf Platte 0").

### 2.1 Die Kern-Komponenten (Ring 0)

| Komponente | Aufgabe |
|---|---|
| Scheduler (Prozess-Verwaltung) | Entscheidet, welches Programm wann auf die CPU darf; wechselt sehr häufig zwischen Programmen (**Preemptives Multitasking**), sodass der Eindruck von Gleichzeitigkeit entsteht |
| Memory Manager (Speicher-Verwaltung) | Verwaltet virtuellen Speicher (**Paging**) und verteilt RAM; kann selten benötigte Speicherseiten bei Bedarf auf ein **Swap**-Gerät oder in eine Auslagerungsdatei verschieben und später wieder in den RAM laden. Verhindert außerdem, dass ein Programm in den Speicherbereich eines anderen schreibt (Speicherschutz) |
| I/O-Manager (Geräte-Verwaltung) | Kommuniziert über Treiber mit Tastatur, Maus, Festplatte etc. |

> **IHK-Typfrage:** *Warum friert bei einem in einer Endlosschleife hängenden Programm heute nicht mehr der ganze PC ein?*
> **Musterantwort:** Dank preemptivem Multitasking entscheidet der Scheduler zentral, wie viel CPU-Zeit jedes Programm bekommt, und kann einem Programm diese Zeit zwangsweise wieder entziehen, statt zu warten, bis das Programm sie freiwillig abgibt. Ein hängendes Programm kann dadurch normalerweise nicht dauerhaft die gesamte CPU monopolisieren – der Scheduler weist den anderen laufenden Prozessen weiterhin regelmäßig Rechenzeit zu, sodass das restliche System bedienbar bleibt. Vollständig ausgeschlossen ist eine starke Beeinträchtigung damit aber nicht: Übermäßiger Speicher- oder I/O-Verbrauch des hängenden Programms sowie Fehler in Treibern oder im Kernel selbst können das Gesamtsystem trotzdem spürbar verlangsamen oder zum Absturz bringen.

### 2.2 Dateisysteme im Vergleich

| Dateisystem | OS-Heimat | Max. Dateigröße | Features | Einsatzzweck |
|---|---|---|---|---|
| FAT32 | Alle (breite Kompatibilität) | 4 GiB | Keine Zugriffsrechte, kein Journaling | USB-Sticks für maximale Kompatibilität |
| exFAT | Alle | Sehr groß (keine 4-GiB-Grenze) | Für große Dateien und Wechseldatenträger allgemein konzipiert (nicht nur Flash-Speicher) | Große USB-Sticks, SD-Karten für Kameras |
| NTFS | Windows | Sehr groß | ACLs (Zugriffsrechte), Journaling, Kompression | Windows-Systempartitionen |
| ext4 | Linux | Sehr groß | Journaling, als stabiler Standard etabliert | Linux-Systeme |
| APFS | macOS | Sehr groß | Für SSDs optimiert, Snapshots, Verschlüsselung "out of the box" | Macs (seit 2017) |
| ZFS | Ursprünglich Sun/Solaris, heute v. a. BSD/Linux-Server | Sehr groß | Selbstheilung, integriertes RAID | NAS, Enterprise-Storage |

> **IHK-Typfrage:** *Ein Kunde will einen USB-Stick, der regelmäßig große Videodateien (>4 GiB) zwischen Windows-PCs und Macs transportieren soll. Welches Dateisystem empfiehlst du, und warum nicht FAT32?*
> **Musterantwort:** FAT32 scheidet aus, da es Dateien auf maximal 4 GiB begrenzt – eine typische HD-Videodatei überschreitet diese Grenze oft. **exFAT** ist die passende Wahl: Es wurde für große Dateien und Wechseldatenträger allgemein konzipiert, kennt keine 4-GiB-Dateigrößenbegrenzung und wird sowohl von aktuellen Windows- als auch von macOS-Systemen nativ ohne Zusatzsoftware gelesen und beschrieben – im Gegensatz zu NTFS (unter macOS in vielen Versionen nativ nur lesbar, Schreibzugriff meist erst mit Drittsoftware) oder APFS (unter Windows nicht nativ unterstützt).

🔴 **Stolperstein:** "Windows kann von Haus aus keine ext4-Partitionen lesen, weil das technisch nicht möglich ist." Falsch – der Grund ist nicht rein technischer, sondern strategischer Natur: Windows bietet standardmäßig keinen allgemeinen nativen ext4-Treiber für den direkten Zugriff im Explorer. Über Drittsoftware oder Linux-Integrationslösungen wie WSL (Windows Subsystem for Linux) ist ein Zugriff auf ext4-Daten dennoch möglich – das ist aber nicht dasselbe wie ein direkt im Dateisystem eingebundener nativer Treiber.

🟡 **Kontextwissen – Journaling:** Ein "Logbuch" für Dateioperationen – bevor eine Änderung tatsächlich geschrieben wird, wird die geplante Operation im Journal vermerkt. Bei einem Stromausfall mitten im Schreibvorgang kann das Dateisystem beim nächsten Start anhand des Journals feststellen, welche Transaktionen vollständig protokolliert wurden, und diese erneut anwenden bzw. unvollständige Transaktionen verwerfen – das schützt primär die interne Konsistenz der Dateisystemstrukturen. Ob dabei auch die zuletzt gewünschte Dateiänderung selbst vollständig erhalten bleibt, hängt vom konkreten Dateisystem und seinem Journaling-Modus ab (viele Journaling-Dateisysteme protokollieren primär Metadaten, nicht zwingend jeden Dateiinhalt).

---

## 3. Die Ahnenreihe der Betriebssysteme

> **Grundprinzip:** Jede Generation von Betriebssystemen war eine Antwort auf die Möglichkeiten (und Grenzen) der jeweils aktuellen Hardware-Generation.

### 3.1 Die vier Generationen

> 🟡 Die folgende Einteilung ist ein verbreitetes didaktisches Modell zur groben Orientierung – die tatsächlichen Übergänge waren fließend, Zeiträume überschneiden sich, und verschiedene Konzepte (z. B. Batch-Verarbeitung) existierten teils parallel über mehrere Generationen hinweg fort.

| Generation | Zeitraum (ca.) | Hardware-Basis | OS-Merkmal | Beispiele |
|---|---|---|---|---|
| Gen 1 | 1945–ca. 1956 | Elektronenröhren, Steckbretter | Praktisch kein echtes OS, später einfache Batch-Systeme | GM-NAA I/O (1956) – gilt oft als eines der ersten Betriebssysteme überhaupt (für IBM 704) |
| Gen 2 | 1955–1965 | Transistoren | Mainframes, Batch-Verarbeitung & Spooling | IBSYS, FMS (Fortran Monitor System) |
| Gen 3 | 1965–1980 | Integrierte Schaltkreise (ICs) | Multiprogramming, Time-Sharing (Nutzer teilen sich Rechenzeit) | OS/360, UNIX (1969) |
| Gen 4 | 1980–heute | Mikroprozessoren | PC, GUI, Netzwerk, Distributed OS | MS-DOS, Windows, macOS, Linux |

> **IHK-Typfrage:** *Vergleiche Batch-Processing (Generation 2) und Time-Sharing (Generation 3) und erkläre, warum Time-Sharing eine Revolution für die Benutzerinteraktion darstellte.*
> **Musterantwort:** Beim Batch-Processing wurden Aufträge (Jobs) vorab als Stapel eingereicht, nacheinander vollständig abgearbeitet und die Ergebnisse erst danach ausgegeben – eine direkte, interaktive Rückmeldung während der Verarbeitung gab es nicht, Nutzer mussten oft Stunden oder länger auf ihr Ergebnis warten. Time-Sharing teilt die Rechenzeit eines einzigen Großrechners in kleine Zeitscheiben auf, die reihum an mehrere gleichzeitig angemeldete Nutzer vergeben werden – für jeden einzelnen Nutzer entsteht dadurch der Eindruck einer sofortigen, interaktiven Antwort des Systems, obwohl im Hintergrund viele Nutzer denselben Rechner teilen. Das war die Grundlage für interaktives statt rein stapelverarbeitendes Arbeiten am Computer.

### 3.2 Meilensteine

| Jahr | System | Bedeutung |
|---|---|---|
| 1969 | UNIX | Bei Bell Labs entwickelt, portabel (in C geschrieben), Grundprinzip "Everything is a file" – Basis vieler späterer Systeme (u. a. Linux, macOS) |
| 1977 | BSD | Akademisches Unix-Derivat der UC Berkeley – BSD-Komponenten und -Konzepte flossen später u. a. in Darwin/macOS ein |
| 1981 | MS-DOS | Microsoft lizenzierte das gekaufte QDOS als PC-DOS an IBM; Single-Tasking |
| 1984 | Mac OS (Classic) | Bringt die grafische Benutzeroberfläche (GUI) in den Massenmarkt |
| 1985 | AmigaOS | Frühes echtes preemptives Multitasking im Heimcomputer-Bereich |
| 1987 | OS/2 | Gemeinsame Entwicklung von IBM und Microsoft als DOS/Windows-Nachfolger; Microsoft stieg zugunsten von NT aus, OS/2 setzte sich am Markt nicht durch |
| 1991 | Linux | Linus Torvalds veröffentlicht den Linux-Kernel |
| 1993 | Windows NT | Microsofts eigenständige 32-Bit-Kernel-Linie – Basis für spätere XP-, 7- und 11-Generationen |
| 2001 | Mac OS X | Apple wechselt den Unterbau radikal auf ein Unix-System (BSD/Darwin) |

🔴 **Stolperstein:** "MULTICS war ein Flop und deshalb irrelevant." MULTICS gilt kommerziell zwar weitgehend als gescheitert, war aber technisch enorm einflussreich – viele seiner Konzepte (u. a. hierarchisches Dateisystem, Sicherheitsmodell) flossen direkt in die Entwicklung von UNIX ein, weshalb es oft als technischer "Vater" von Unix bezeichnet wird.

🟢 **Nice to know – Year 2038 Problem:** Viele Unix-basierte Systeme speichern Zeitstempel klassischerweise als Sekunden seit dem 1.1.1970 in einer 32-Bit-Ganzzahl mit Vorzeichen. Diese Darstellung läuft am 19. Januar 2038 über und würde ohne Gegenmaßnahmen zu einem Sprung auf ein Datum im Jahr 1901 führen – moderne Systeme migrieren deshalb zunehmend auf 64-Bit-Zeitstempel.

---

## 4. Windows

> **Grundprinzip:** Bis 2001 gab es zwei technisch komplett getrennte Windows-Welten – Consumer-Kompatibilität (DOS-Linie) und Profi-Stabilität (NT-Linie) –, die erst mit Windows XP zusammengeführt wurden.

### 4.1 Zwei Familien, eine Hochzeit

| Linie | Vertreter | Eigenschaft |
|---|---|---|
| DOS-Familie (Consumer) | Windows 95, 98, ME | Basierte auf MS-DOS, deutlich schwächerer Speicherschutz als bei NT, dafür maximale Kompatibilität zu älteren Spielen/Anwendungen |
| NT-Familie (Profi) | Windows NT, 2000 | Eigenständiger, von Dave Cutler (zuvor an VMS beteiligt) entwickelter Kernel – stabiler, sicherer, echtes Multitasking, aber hardwarehungriger |

**Windows XP (2001)** vereinte beide Linien: Der stabile NT-Kernel wurde erstmals auch für Privatanwender/Gamer nutzbar. Seitdem basieren alle Windows-Versionen (Vista bis Windows 11) durchgehend auf dem NT-Kernel.

> **IHK-Typfrage:** *Warum lief altsoftware der 90er-Jahre besser unter Windows 95/98 als unter Windows NT/2000 – und warum war das trotzdem ein Sicherheitsproblem?*
> **Musterantwort:** Die DOS-Linie (95/98/ME) hatte einen deutlich schwächeren Speicherschutz als die NT-Linie und erlaubte Programmen oft recht direkten Zugriff auf Hardware-nahe Funktionen – viele ältere Spiele und Anwendungen waren genau auf dieses Verhalten programmiert und liefen deshalb auf der DOS-Linie reibungsloser. Die NT-Linie erzwang dagegen von Anfang an eine strengere Trennung zwischen Anwendungen und Systemressourcen (echter Speicherschutz, kontrollierter Hardwarezugriff), was zu höherer Stabilität und Sicherheit führte, aber ältere, nicht konforme Software oft zum Absturz brachte. Der schwächere Schutz der DOS-Linie war entsprechend auch ein Sicherheitsrisiko – fehlerhafte oder bösartige Software konnte das gesamte System leichter destabilisieren oder kompromittieren.

### 4.2 Warum Windows dominiert

🟡 **Kontextwissen:** Windows hält traditionell einen sehr hohen Marktanteil auf dem Desktop (grobe Richtwerte um 70–80 %, je nach Quelle und Zeitpunkt schwankend). Zwei strategische Faktoren neben der Technik selbst:
- **OEM-Bündelung:** Microsoft schloss in den 1990ern Verträge mit PC-Herstellern (u. a. IBM, Dell, HP) – PCs wurden meist mit vorinstalliertem Windows verkauft, wodurch Windows für Endkunden vorinstalliert und ohne separate Kauf- oder Installationsentscheidung sofort einsatzbereit verfügbar war (die Lizenzkosten waren dabei regelmäßig im Gerätepreis enthalten).
- **Abwärtskompatibilität:** Sehr alte Software läuft teils noch heute unter Windows 11 – das bindet Unternehmen an das System (Vendor Lock-in), da ein Wechsel oft bedeuten würde, geschäftskritische Altsoftware zu verlieren.

### 4.3 Technische Besonderheiten

| Aspekt | Beschreibung |
|---|---|
| Kernel | Wird häufig als Hybridkernel eingeordnet – enthält sowohl monolithisch wirkende als auch stärker modulare/mikrokernartige Komponenten; historisch liefen u. a. Teile der Grafikausgabe aus Performance-Gründen direkt im Kernel-Modus |
| Registry | Eine zentrale, hierarchische Datenbank für praktisch alle Systemeinstellungen (statt vieler Einzel-Textdateien wie bei Unix-Systemen) – ermöglicht zentralen Zugriff, kann aber schwer zu warten und zu diagnostizieren sein. Das sog. "DLL-Hell"-Problem entstand dagegen primär durch Konflikte zwischen gemeinsam genutzten, unterschiedlich versionierten DLL-Dateien – die Registry (u. a. über COM-Registrierungen) konnte solche Konflikte zusätzlich verschärfen, war aber nicht deren eigentliche Ursache |
| Dateisystem | NTFS mit ACLs (Access Control Lists) für granulare Benutzerrechte; Laufwerke werden als Buchstaben (`C:\`, `D:\`) statt als ein gemeinsamer Verzeichnisbaum abgebildet |

🟡 **Kontextwissen – Registry-Struktur:** Im Registrierungseditor werden dem Benutzer fünf zentrale Root Keys angezeigt: `HKEY_CLASSES_ROOT`, `HKEY_CURRENT_USER`, `HKEY_LOCAL_MACHINE`, `HKEY_USERS` und `HKEY_CURRENT_CONFIG`. Diese sind nicht alle eigenständige "Hives" (physisch gespeicherte Registry-Dateien) – `HKEY_CLASSES_ROOT` ist z. B. lediglich eine zusammengeführte Ansicht aus Teilen von `HKEY_LOCAL_MACHINE` und `HKEY_CURRENT_USER`.

🔴 **Stolperstein:** "32-Bit-Software läuft grundsätzlich auf 64-Bit-Windows genauso wie 16-Bit-Software." Falsch – viele 32-Bit-Windows-Anwendungen können dank der Kompatibilitätsschicht **WoW64** (Windows on Windows 64) auf x64-Windows ausgeführt werden (Treiber, hardwarenahe Komponenten und alte Abhängigkeiten können dennoch inkompatibel sein), echte 16-Bit-Anwendungen laufen auf 64-Bit-x86-Windows dagegen nicht mehr.

🟡 **Praxis-Tipp – UAC:** Die Benutzerkontensteuerung (User Account Control) fragt bei Aktionen, die Administratorrechte erfordern (z. B. Installation ins Systemverzeichnis), gezielt nach Bestätigung – auch wenn der angemeldete Benutzer selbst Administratorrechte besitzt. Das schützt davor, dass Schadsoftware unbemerkt im Hintergrund systemweite Änderungen vornimmt.

---

## 5. Linux

> **Grundprinzip:** "Linux" bezeichnet im engeren Sinn nur den Kernel – ein vollständiges, nutzbares Betriebssystem entsteht erst durch die Kombination mit den GNU-Werkzeugen, weshalb manche korrekterweise von "GNU/Linux" sprechen.

### 5.1 Entstehung: Zwei fehlende Puzzleteile finden sich

1991 war kommerzielles Unix für Studierende wie Linus Torvalds unerschwinglich. Er entwickelte daraufhin als Hobbyprojekt den Kernel eines Unix-artigen Systems ("Linux") und stellte ihn 1992 unter die GPL. Für ein praktisch nutzbares freies Betriebssystem waren zusätzlich Compiler, Shell, C-Bibliothek, Systemprogramme und weitere Komponenten nötig – viele davon waren im Rahmen des **GNU-Projekts** bereits weitgehend vorhanden. Umgekehrt fehlte dem GNU-System damals noch ein allgemein einsatzfähiger eigener Kernel: Der geplante GNU-Kernel ("Hurd", eine Sammlung von Servern auf dem GNU-Mach-Mikrokernel) erreichte nicht rechtzeitig die Produktionsreife und wird bis heute weiterentwickelt, ohne im Alltag breit produktiv eingesetzt zu werden. Linux-Kernel und die weitgehend vorhandenen GNU-Werkzeuge schlossen so gegenseitig entscheidende Lücken und bildeten zusammen mit weiterer freier Software die Grundlage vieler Distributionen – deshalb wird das Gesamtsystem häufig als GNU/Linux bezeichnet (auch wenn nicht jedes Linux-basierte System zwingend GNU-Werkzeuge nutzt, z. B. Android).

> **IHK-Typfrage:** *Erläutere, warum Linus Torvalds das GNU-Projekt für sein Betriebssystem benötigte und warum umgekehrt das GNU-Projekt den Linux-Kernel brauchte.*
> **Musterantwort:** Linus Torvalds hatte 1991 zwar einen funktionierenden Kernel geschrieben, aber keine Anwendungswerkzeuge (Compiler, Shell, Systemprogramme usw.), um damit tatsächlich arbeiten zu können – diese waren im Rahmen des GNU-Projekts bereits weitgehend unter freier Lizenz vorhanden. Umgekehrt hatte das GNU-Projekt zwar die meisten nötigen Werkzeuge fertiggestellt, aber keinen produktionsreifen eigenen Kernel (der geplante GNU-Hurd-Kernel erreichte nicht rechtzeitig die allgemeine Einsatzreife) – ohne einen funktionierenden Kernel konnte das GNU-System nicht eigenständig laufen. Die Kombination aus Linux-Kernel und den weitgehend vorhandenen GNU-Werkzeugen (zusammen mit weiterer freier Software) ergab ein praktisch nutzbares, freies Betriebssystem.

### 5.2 Struktur

Der Linux-Kernel ist **monolithisch, aber modular ladbar** (Kernel-Module können zur Laufzeit nach- oder entladen werden, ohne den gesamten Kernel neu übersetzen zu müssen). Die Ordnerstruktur folgt dem **FHS** (Filesystem Hierarchy Standard):

| Verzeichnis | Inhalt |
|---|---|
| `/etc` | Konfigurationsdateien |
| `/home` | Benutzerdaten |
| `/var` | Variable Daten (u. a. Logs) |
| `/bin` | Ausführbare Programme (Binaries) |

🟡 **Kontextwissen – Open Source:** Der Quellcode ist offen einsehbar – jeder darf ihn lesen, verändern und weitergeben. Der Linux-Kernel selbst steht unter der GPLv2; die GNU-Werkzeuge stehen überwiegend, aber nicht ausnahmslos, ebenfalls unter freien Lizenzen wie der GPL. Diese Offenheit ermöglichte ein sehr schnelles, weltweit verteiltes Entwicklertempo.

🟢 **Nice to know – Bug #1:** 2004 eröffnete Mark Shuttleworth (Ubuntu-Gründer) in seinem Bug-Tracker scherzhaft den "Bug #1": *"Microsoft has a majority market share."* Auf dem klassischen Desktop blieb Linux mit einem Marktanteil im niedrigen einstelligen Prozentbereich eine Nische; 2013 wurde der Bug mit dem Kommentar geschlossen: *"Android has fixed this"* – denn Android (mit Linux-Kernel) erreichte im mobilen Bereich einen sehr hohen Marktanteil.

🔴 **Stolperstein:** "Root und sudo sind dasselbe." Root ist der Name des Benutzerkontos mit uneingeschränkten Rechten auf einem Unix-artigen System. `sudo` ("superuser do" als Merkhilfe) ist dagegen ein Werkzeug, mit dem ein entsprechend berechtigter Benutzer einzelne Befehle unter der Identität eines anderen Benutzers ausführen kann – standardmäßig als Root, die genaue Konfiguration kann aber auch andere Zielbenutzer oder -gruppen erlauben. Der Vorteil: Es ist keine dauerhafte Anmeldung als Root nötig, und privilegierte Aufrufe bleiben nachvollziehbar protokolliert – ein wichtiger Sicherheitsunterschied zum permanenten Arbeiten als Root.

---

## 6. macOS

> **Grundprinzip:** Der Wechsel von "Mac OS Classic" zu "Mac OS X" (2001) war technisch einschneidend: Der Umstieg auf einen echten Unix-Unterbau brachte präemptives Multitasking, robusten Speicherschutz, moderne Netzwerkfunktionen und eine stabilere Systemarchitektur – Eigenschaften, die dem bisherigen Mac OS fehlten.

### 6.1 Der große Wechsel

Nach der Rückkehr von Steve Jobs (über die von Apple aufgekaufte Firma NeXT) wurde **NeXTSTEP** (bereits Unix-basiert) zur Grundlage von **Mac OS X** (2001). Das Fundament heißt **Darwin** – die Unix-artige Open-Source-Basis von macOS, die u. a. den XNU-Kernel (mit Mach- und BSD-Komponenten) sowie BSD-Systemprogramme und Bibliotheken umfasst. Sie brachte dem Mac eine deutlich robustere Prozessisolation, präemptives Multitasking für Anwendungen, moderne Netzwerkfunktionen und eine stabilere Systemarchitektur.

> **IHK-Typfrage:** *Erläutere, welche technischen Probleme von Mac OS 9 durch den Wechsel zu Mac OS X gelöst wurden.*
> **Musterantwort:** Mac OS 9 (Classic) plante normale Anwendungen überwiegend **kooperativ** ein – ein Programm musste die CPU freiwillig wieder freigeben, damit andere Programme drankamen; zudem teilten sich Anwendungen weitgehend denselben Adressraum, wodurch ein fehlerhaftes Programm leichter andere Programme oder das gesamte System beeinträchtigen konnte. (Zwar boten die sogenannten Multiprocessing Services bereits begrenzte präemptive Hintergrund-Tasks für speziell dafür entwickelte Programme, die normalen Anwendungsprozesse blieben davon aber unberührt.) Diese Instabilität war im Vergleich zu den bereits stabileren Konkurrenzsystemen (u. a. Windows NT-Linie) ein zunehmendes Wettbewerbsproblem. Der Wechsel auf das Darwin-Fundament mit Mac OS X brachte echtes präemptives Multitasking für Anwendungen, robusten Speicherschutz und eine moderne Unix-Basis – Eigenschaften, die insbesondere im professionellen und Entwickler-Umfeld zunehmend als Standard erwartet wurden.

### 6.2 Technische Basis

| Aspekt | Beschreibung |
|---|---|
| Kernel | XNU – ein Hybrid aus Mach-Mikrokernel-Anteilen und BSD-Komponenten |
| Dateisystem | APFS (Apple File System) – für Flash-/SSD-Speicher optimiert, unterstützt Snapshots und Verschlüsselung direkt "out of the box" |
| GUI | Aqua – hardwarebeschleunigte, grafisch aufwendige Oberfläche |

🟡 **Kontextwissen – Verbreitung:** macOS hält weltweit einen deutlich geringeren Desktop-Marktanteil als Windows (grobe Richtwerte im Bereich 15–20 %, in den USA tendenziell höher, je nach Quelle und Zeitpunkt schwankend) – ist aber in bestimmten Zielgruppen (Kreativbranche, Softwareentwicklung) stark vertreten, u. a. weil ein Unix-Terminal und kreative Software auf derselben Plattform zusammenkommen.

🟡 **Kontextwissen – Systemschutz:** "Security by Obscurity" (Sicherheit allein durch geringe Verbreitung) gilt für macOS nicht mehr uneingeschränkt – Macs sind längst ein reales Angriffsziel. Apple begegnet dem u. a. mit **Gatekeeper** (prüft die Herkunft/Signatur von Software vor der Ausführung) und **SIP** (System Integrity Protection, schützt kritische Systembereiche selbst vor Root-Zugriff).

---

## 7. Unix & BSD

> **Grundprinzip:** UNIX (1969) prägte mit "Everything is a file" und dem KISS-Prinzip (kleine, kombinierbare Werkzeuge statt monolithischer Alleskönner) die Denkweise praktisch aller späteren Unix-artigen Systeme – einschließlich Linux und macOS.

### 7.1 Die Geburt (Bell Labs, 1969)

UNIX entstand ab 1969 bei Bell Labs durch Ken Thompson, Dennis Ritchie und weitere Entwickler. Die frühen Versionen enthielten noch viel Assemblercode; ab etwa 1973 wurde UNIX weitgehend in der von Dennis Ritchie mitentwickelten Programmiersprache **C** neu geschrieben – dadurch wurde das System deutlich portabler und ließ sich auf verschiedenste Hardware übertragen, statt wie zuvor an hardwarenahen Assembler gebunden zu sein. Dieser Schritt gilt als einer der Gründe für den langfristigen Erfolg von UNIX.

### 7.2 Der "Unix-Krieg"

| Lager | Charakter | Erbe |
|---|---|---|
| System V (AT&T) | Kommerziell, proprietär | Basis für Solaris, AIX, HP-UX – noch heute u. a. in Banken/Großrechnerumgebungen im Einsatz |
| BSD (Berkeley Software Distribution) | Akademisch entstanden, freizügigere Lizenz | Beide Linien beeinflussten spätere Systeme erheblich; BSD wurde insbesondere durch seine Lizenz und seine Netzwerkkomponenten sehr einflussreich – von einem eindeutigen "Sieger" des Rechtsstreits mit AT&T im Sinne einer vollständigen Ablösung von System V kann man aber nicht sprechen |

### 7.3 BSD heute

| Variante | Fokus | Bekanntes Einsatzgebiet |
|---|---|---|
| FreeBSD | Performance, Netzwerk und Storage | BSD-Komponenten und -Konzepte flossen in Darwin/macOS ein (Darwin ist aber ein eigenständiger XNU-Kernel-Verbund, keine direkte FreeBSD-Kopie); laut öffentlich verfügbaren Angaben u. a. bei PlayStation-Systemsoftware und in Teilen der Netflix-Open-Connect-Infrastruktur sowie bei der Firewall-Distribution pfSense im Einsatz |
| OpenBSD | Sicherheit und Codequalität | Bekannt für den Werbespruch "Only two remote holes in a heck of a long time"; Basis für den weitverbreiteten OpenSSH sowie das Paketfilter-Framework "pf" (das u. a. auch in FreeBSD-basierten Systemen wie pfSense übernommen wurde) |
| NetBSD | Portabilität | Bekannt für seinen Anspruch, auf praktisch jeder Hardware lauffähig zu sein |

> **IHK-Typfrage:** *Begründe, warum Unternehmen wie Netflix für ihre Video-Serverinfrastruktur teils FreeBSD anstelle von Linux einsetzen.*
> **Musterantwort:** Netflix verwendet bzw. verwendete FreeBSD insbesondere in Teilen seiner Open-Connect-Infrastruktur. Für bestimmte Hochlast-Netzwerkszenarien gilt der FreeBSD-Netzwerk-Stack als besonders performant und gut anpassbar, was für das Ausliefern sehr großer Datenmengen an viele gleichzeitige Nutzer (wie bei Video-Streaming) vorteilhaft sein kann. Zusammen mit der freizügigen BSD-Lizenz, die eine kommerzielle Anpassung ohne Offenlegungspflicht des eigenen Codes erlaubt, ergibt sich für spezialisierte Infrastrukturanbieter ein attraktives Gesamtpaket. Daraus folgt aber nicht, dass FreeBSD generell für jedes Streaming- oder Serverszenario der Linux-Alternative überlegen wäre – die Wahl hängt stark vom konkreten Anwendungsfall ab.

🟡 **Kontextwissen – Wheel-Gruppe:** In vielen BSD-Systemen dürfen nur Mitglieder der Gruppe "wheel" den Befehl `su` nutzen, um zum Root-Benutzer zu wechseln – ein zusätzlicher, expliziter Berechtigungsmechanismus oberhalb des reinen Passwortschutzes.

---

## 8. Mobile Welten (Android & iOS)

> **Grundprinzip:** Android ist als Plattform offener und stärker anpassbar, wird aber von Geräteherstellern unterschiedlich umgesetzt; iOS ist stärker kontrolliert und geschlossener, bietet dafür ein einheitlicheres Sicherheits- und Update-Modell innerhalb der unterstützten Geräte – "mehr Freiheit" und "mehr Kontrolle" sind zwei unterschiedliche Philosophien, keine einfache Besser/Schlechter-Bewertung.

### 8.1 Architektur-Vergleich

| Merkmal | Android | iOS |
|---|---|---|
| Hersteller/Modell | Google, quelloffene Basis (AOSP) | Apple, proprietär |
| Kernel | Linux | Darwin (XNU) – dieselbe Kernel-Familie wie macOS |
| App-Installation | APKs (Java/Kotlin), Sideloading außerhalb des Play Stores grundsätzlich vorgesehen | Historisch grundsätzlich nur über den App Store, der Apps vorab prüft; seit dem 6. März 2024 gelten in der EU die zentralen DMA-Verpflichtungen, wonach Apple unter bestimmten Voraussetzungen alternative App-Marktplätze und Web-Distribution ermöglichen muss – die konkreten Bedingungen können sich durch weitere Gesetzgebung und Unternehmensänderungen entwickeln, Sideloading auf iOS ist damit auch in der EU nicht mit einer völlig freien Installation wie unter Desktop-Linux gleichzusetzen |
| Sicherheitsupdates | Abhängig vom jeweiligen Gerätehersteller, dadurch oft uneinheitlich/verzögert | Zentral von Apple bereitgestellt, meist für unterstützte Geräte gleichzeitig verfügbar |
| Geräte-Vielfalt | Läuft auf sehr unterschiedlicher Hardware vieler Hersteller | Nur auf Apple-eigener Hardware (iPhone/iPad) |

> **IHK-Typfrage:** *Erläutere den Begriff "Sideloading" und bewerte das damit verbundene Sicherheitsrisiko.*
> **Musterantwort:** Sideloading bezeichnet die Installation einer App außerhalb des offiziellen App-Stores – bei Android z. B. durch das direkte Installieren einer APK-Datei aus einer beliebigen Quelle. Der Vorteil ist mehr Freiheit für Nutzer und Entwickler (z. B. Beta-Versionen, alternative App-Stores, selbst entwickelte Apps ohne Store-Freigabe). Das Sicherheitsrisiko besteht darin, dass eine sideloaded App nicht dieselben Prüfprozesse wie im offiziellen Store durchlaufen hat – Schadsoftware kann sich so leichter als scheinbar harmlose App tarnen. Nutzer sollten Sideloading deshalb nur aus vertrauenswürdigen Quellen und mit Bewusstsein für das erhöhte Risiko durchführen. Bei iOS war Sideloading historisch praktisch ausgeschlossen; seit 2024 erlaubt Apple in der EU aufgrund des Digital Markets Act (DMA) alternative App-Marktplätze und Web-Distribution direkt von Entwickler-Websites – Apple prüft die Apps dabei weiterhin über einen Notarisierungsprozess, allerdings mit weniger strenger Kontrolle als im klassischen App-Store-Modell.

### 8.2 Sandboxing

Apps werden grundsätzlich voneinander isoliert (**Sandbox**) und erhalten nur über definierte System-APIs, Berechtigungen (Permissions) oder gemeinsame Container kontrollierten Zugriff auf bestimmte Ressourcen oder Daten anderer Apps – ein zentrales Sicherheitsprinzip auf beiden Plattformen.

🟡 **Kontextwissen – Laufzeitumgebung:** Android-Apps liefen historisch in der **Dalvik**-Laufzeitumgebung, heute im moderneren **ART** (Android Runtime), das je nach Android-Version und Anwendung mehrere Techniken kombiniert – u. a. Ahead-of-Time- und Just-in-Time-Kompilierung sowie Laufzeitprofiling – für bessere Performance und Akkueffizienz.

🟢 **Nice to know:** Das gezielte Umgehen der Herstellerbeschränkungen wird bei Android als **Rooting**, bei iOS als **Jailbreak** bezeichnet – beides verschafft dem Nutzer erweiterte Systemrechte, kann aber wesentliche Schutzmechanismen wie Sandboxing, Signaturprüfung und Einschränkungen privilegierter Zugriffe abschwächen oder umgehen. Zudem kann es Herstellersupport, freiwillige Garantiebedingungen, Sicherheitsupdates und die zukünftige Update-Fähigkeit beeinträchtigen – gesetzliche Gewährleistungsrechte (die von der freiwilligen Herstellergarantie zu unterscheiden sind) entfallen dadurch aber nicht automatisch.

---

## Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Welcher Ring hat die höchsten, welcher die niedrigsten Rechte? | Ring -3 die höchsten (hardwarenächsten), Ring 3 die niedrigsten |
| 2 | Welches Dateisystem eignet sich für einen USB-Stick mit >4-GiB-Dateien für Windows und Mac? | exFAT |
| 3 | Was unterscheidet Batch-Processing von Time-Sharing? | Batch: Aufträge komplett nacheinander ohne Interaktion; Time-Sharing: Rechenzeit wird in Zeitscheiben auf mehrere gleichzeitige Nutzer verteilt |
| 4 | Welches Windows-Release vereinte erstmals DOS- und NT-Linie? | Windows XP (2001) |
| 5 | Was ist GNU/Linux eigentlich, streng genommen? | Linux = nur der Kernel; erst mit den GNU-Werkzeugen ergibt sich ein vollständiges Betriebssystem |
| 6 | Worauf basiert der macOS-Kernel XNU? | Ein Hybrid aus Mach-Mikrokernel-Anteilen und BSD |
| 7 | Was ist der Unterschied zwischen Root und sudo? | Root ist ein Benutzerkonto mit vollen Rechten; sudo erlaubt temporäre, nachvollziehbare Rechteausweitung für einzelne Befehle |
| 8 | Was ist der zentrale Unterschied im App-Vertrieb zwischen Android und iOS? | Android erlaubt Sideloading grundsätzlich; iOS war historisch auf den App Store beschränkt, erlaubt in der EU seit 2024 (DMA) aber alternative Marktplätze und Web-Distribution unter Bedingungen |

---

## IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Ring 0 / Ring 3 | Kernel-Mode (voller Hardwarezugriff) vs. User-Mode (kein direkter Hardwarezugriff, System Calls nötig) |
| System Call | Kontrollierter Übergang von Ring 3 zu Ring 0 für privilegierte Operationen – mit Performance-Kosten durch den Kontextwechsel |
| Secure Boot (UEFI) | Erschwert den Start unsignierter Bootloader/Bootkits durch Signaturprüfung – kein vollständiger Rootkit-Schutz |
| Preemptives Multitasking | Der Scheduler kann einem Programm die CPU-Zeit auch gegen dessen "Willen" entziehen |
| Journaling | Logbuch für Dateioperationen zum Schutz vor Inkonsistenzen bei Stromausfall |
| Time-Sharing | Mehrere Nutzer teilen sich interaktiv die Rechenzeit eines Systems in kleinen Zeitscheiben |
| NT-Kernel | Seit Windows XP einheitliche Kernel-Basis aller Windows-Versionen |
| WoW64 | Kompatibilitätsschicht für 32-Bit-Software auf 64-Bit-Windows |
| GNU/Linux | Linux-Kernel + GNU-Werkzeuge = vollständiges freies Betriebssystem |
| FHS | Filesystem Hierarchy Standard – standardisierte Linux-Verzeichnisstruktur |
| Darwin/XNU | BSD-basiertes Unix-Fundament von macOS (und Kernel-Basis von iOS) |
| Sandboxing | Isolierte Ausführungsumgebung pro App, Zugriff auf fremde Daten nur mit expliziter Erlaubnis |
| Sideloading | App-Installation außerhalb des offiziellen Stores – bei Android grundsätzlich vorgesehen; bei iOS historisch stark eingeschränkt, in der EU seit 2024 aufgrund des Digital Markets Act (DMA) über alternative Marktplätze/Web-Distribution unter Bedingungen möglich |

---

## Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Beispiel aus AP1 | Was die IHK hören will |
|---|---|---|---|
| Architekturzuordnung | "Ordne X der passenden Ring-Ebene zu" | "Ordne Word, Windows-Kernel, Intel ME, Hyper-V und Grafiktreiber den korrekten Ringen zu." | Korrekte Zuordnung + kurze Begründung je Ebene |
| Ursache-Wirkung (historisch) | "Warum wurde X eingeführt/geändert?" | "Warum wurden DOS- und NT-Linie erst mit XP vereint?" | Konkrete technische/historische Begründung, nicht nur Jahreszahl |
| Dateisystem-/Technologiewahl | "Welches System passt zu Einsatzzweck Y?" | "Welches Dateisystem für einen plattformübergreifenden USB-Stick mit großen Dateien?" | Konkrete Empfehlung + Ausschluss der ungeeigneten Alternativen mit Begründung |
| Sicherheitsbewertung | "Bewerte das Risiko von X" | "Bewerte das Sicherheitsrisiko von Sideloading unter Android." | Vorteil UND Risiko benennen, keine einseitige Bewertung |

---

## Merk-Sätze fürs Fachgespräch

> Ring 0 und Ring 3 trennen nicht aus Bürokratie, sondern aus Sicherheitsprinzip – jeder System Call ist der kontrollierte Türsteher zwischen Anwendung und Hardware.

> "Linux" ist streng genommen nur der Kernel – erst zusammen mit den weitgehend vorhandenen GNU-Werkzeugen (und weiterer freier Software) entstanden praktisch nutzbare GNU/Linux-Distributionen.

> DOS-Linie und NT-Linie waren technisch zwei komplett verschiedene Welten – Windows XP war die Hochzeit, nicht die Erfindung von Windows.

> macOS, iOS und (über den Linux-Kernel) auch Android führen ihre Wurzeln letztlich auf Unix-Konzepte der späten 1960er zurück – "Everything is a file" und kleine, kombinierbare Werkzeuge sind bis heute prägend.

> Android und iOS lösen dasselbe Sicherheitsproblem (Sandboxing) mit unterschiedlicher Philosophie – mehr Offenheit gegen mehr Kontrolle, kein System ist per se "sicherer" in jeder Hinsicht.

---

```yaml
lernfeld: LF2.5
titel: Der Geist der Maschine (Betriebssysteme)
status: final
stand: 2026-08-27
quellen:
  - "LF2.5 – Der Geist der Maschine (Betriebssysteme)"
  - "LF2.5.1 – Die Architektur der Macht (Ringe & Firmware)"
  - "LF2.5.2 – Der System-Verwalter (OS-Grundlagen & Dateisysteme)"
  - "LF2.5.3 – Die Ahnenreihe der Betriebssysteme"
  - "LF2.5.4 – Windows"
  - "LF2.5.5 – Linux"
  - "LF2.5.6 – macOS"
  - "LF2.5.7 – Unix & BSD"
  - "LF2.5.8 – Mobile Welten (Android & iOS)"
```