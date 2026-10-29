---
titel: "Storage Area Network (SAN) – Grundlagen & Prüfungsvorbereitung"
kategorie: "LF7 / Netzwerk & Storage"
typ: "Prüfungs-Wiki"
status: "vorläufig"
autor: "David"
stand: "2026-08-14"
---

# Storage Area Network (SAN) – Grundlagen & Prüfungsvorbereitung

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr  
> **Prüfungsbezug:** Grundlagen können insbesondere bei Netzwerken, Server-/Storage-Architekturen, Virtualisierung, Datensicherung und Hochverfügbarkeit relevant sein. Die konkrete Gewichtung hängt vom Ausbildungsberuf und der jeweiligen Prüfungsordnung ab.  
> **Lernzeit:** Ca. 30–40 Minuten  
> **Status:** Vorläufiger Entwurf (Erweiterbar)  
> **Stand:** 2026-08-14

---

## IHK-Kernfragen (Sprungmarken)

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was ist ein SAN und wie grenzt es sich von NAS ab? | [1. Grundprinzip](#1-grundprinzip-und-einordnung) |
| 2 | Welche Komponenten gehören zu einem SAN? | [2. Architektur](#2-architektur-und-komponenten) |
| 3 | Welche Transportprotokolle werden im SAN verwendet? | [3. Transportprotokolle](#3-transportprotokolle-im-san) |
| 4 | Was ist Zoning und welche Arten gibt es? | [4. Betrieb und Sicherheit](#4-betrieb-und-sicherheit) |
| 5 | Warum setzt man in Unternehmen SANs ein? | [5. Nutzen und Praxiseinsatz](#5-nutzen-und-praxiseinsatz) |
| 6 | Welche Sicherheits- und Redundanzmaßnahmen sind wichtig? | [6. Risiken und Gegenmaßnahmen](#6-risiken-und-gegenmaßnahmen) |

---

## 1. Grundprinzip und Einordnung

> Ein **Storage Area Network (SAN)** ist ein spezialisiertes Netzwerk beziehungsweise eine Netzwerkarchitektur, deren Hauptzweck der Datentransfer zwischen Servern und Speichersystemen ist. In der Praxis wird ein SAN meistens für **blockbasierten Speicherzugriff** eingesetzt. ([SNIA](https://www.snia.org/education/online-dictionary/term/storage-area-network))

### 1.1 Definition und Abgrenzung

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| **SAN** | Spezialisierte Netzwerkarchitektur für Storage-Zugriff; in der Praxis überwiegend blockorientiert | 🔴 |
| **NAS** | Datei-basierter Speicherzugriff über Netzwerkfreigaben (SMB/NFS) | 🔴 |
| **Zugriffsebene** | SAN = Block-Level, NAS = File-Level | 🔴 |
| **Transport** | FC, iSCSI, FCoE, NVMe-oF | 🔴 |
| **Einsatzzweck** | Virtualisierung, Datenbanken, Hochverfügbarkeit | 🔴 |

**Analogie (Autobahn):**  
Ein SAN ist wie eine speziell geplante Autobahn für Speicherverkehr. Bei Fibre Channel ist diese Autobahn normalerweise technisch vom normalen LAN getrennt. Bei iSCSI kann sie dagegen auf Ethernet basieren und muss durch geeignete Netzplanung, beispielsweise getrennte VLANs, dedizierte Netzwerkkarten oder QoS, vom übrigen Verkehr geschützt werden. Dadurch lassen sich Speicherverkehr und allgemeiner Benutzerverkehr besser voneinander trennen. Das reduziert mögliche gegenseitige Beeinflussungen, garantiert aber nicht automatisch eine bestimmte Performance.

> **IHK-Typfrage:** *„Was ist ein SAN und worin unterscheidet es sich von einem NAS?“*  
> **Musterantwort:** Ein SAN ist ein spezialisiertes Netzwerk für blockbasierten Speicherzugriff. Der Server sieht die Speicherressourcen als lokale Festplatten und verwaltet das Dateisystem selbst. Ein NAS stellt dagegen Dateifreigaben über Netzwerkprotokolle wie SMB oder NFS bereit – dort liegt das Dateisystem auf dem NAS-Server.

---

## 2. Architektur und Komponenten

Ein typisches SAN besteht aus **Servern (Hosts)**, **SAN-Switches** (Fabric), **Storage-Systemen** (Arrays) und einer **Management-Schicht**.

### 2.1 Kernkomponenten

| Komponente | Funktion | IHK-Relevanz |
|---|---|---|
| **Host Bus Adapter (HBA)** | Schnittstellenkarte im Server, stellt Verbindung zum SAN her (z. B. FC-HBA oder iSCSI-NIC) | 🔴 |
| **SAN-Switch / Fabric** | Verbindet Hosts und Storage, stellt dedizierte Pfade bereit | 🔴 |
| **Storage-Array** | Enthält Festplatten/SSDs und Controller, stellt LUNs bereit | 🔴 |
| **LUN (Logical Unit Number)** | Logische Speichereinheit, die einem Host zugewiesen wird | 🔴 |
| **Management-Software** | Überwachung, Konfiguration von Zoning, Masking, Firmware | 🟡 |

### 2.2 Einfaches Topologiebeispiel (nicht redundant)

```
Server 1 ── HBA ──┐
                   ├─── SAN-Switch ─── Storage-Array (Controller A/B)
Server 2 ── HBA ──┘                     ├── LUN 1 (für Server 1)
                                         └── LUN 2 (für Server 2)
```

**Redundante Topologie (empfohlen für Produktion):**

```
Server 1 ── HBA A ── SAN-Fabric A ── Storage-Controller A
Server 1 ── HBA B ── SAN-Fabric B ── Storage-Controller B

Server 2 ── HBA A ── SAN-Fabric A ── Storage-Controller A
Server 2 ── HBA B ── SAN-Fabric B ── Storage-Controller B
```

> In einer produktiven Umgebung sollten die beiden Fabrics unabhängig voneinander betrieben werden. Ein Ausfall von Fabric A darf die Kommunikation über Fabric B nicht beeinträchtigen. Eine redundante Architektur benötigt außerdem redundante Storage-Controller, Stromversorgung und geeignete Failover-Mechanismen.

> **IHK-Typfrage:** *„Nennen Sie drei typische Komponenten eines SAN.“*  
> **Musterantwort:** Host Bus Adapter (HBA) im Server, SAN-Switch zur Verbindung, Storage-Array mit LUNs.

---

## 3. Transportprotokolle im SAN

Ein SAN ist eine **Architektur**, kein einzelnes Protokoll. Es kann mit unterschiedlichen Transporttechniken realisiert werden.

### 3.1 Überblick und Vergleich

| Protokoll | Beschreibung | Vorteile | Nachteile | IHK-Relevanz |
|---|---|---|---|---|
| **Fibre Channel (FC)** | Klassische Storage-Netzwerktechnologie beziehungsweise Protokollfamilie für SANs; kann SCSI- und NVMe-Verkehr transportieren | Sehr hohe Performance, geringe Latenz, stabil | Meist spezielle Hardware und entsprechendes Fachwissen erforderlich | 🔴 |
| **iSCSI** | SCSI-Kommandos über TCP/IP (Port 3260) auf Standard-Ethernet; unterstützt IQN-, EUI- und NAA-Namensformate ([RFC 7143](https://www.rfc-editor.org/rfc/rfc7143)) | Kostengünstig, nutzt vorhandene Netzwerkinfrastruktur | Performance und Latenz hängen stark von Ethernet-Infrastruktur, Bandbreite, Netzwerkauslastung und Konfiguration ab | 🔴 |
| **FCoE** | Fibre Channel über Ethernet (Converged Network) | Ein Netz für LAN & SAN, weniger Kabel | Wird in bestimmten konvergierten Rechenzentrumsumgebungen eingesetzt, für Grundlagenprüfungen meist weniger wichtig als FC und iSCSI | 🟢 |
| **NVMe-oF** | Oberbegriff für Zugriff auf NVMe-Speicher über eine Fabric; Beispiele: NVMe/FC, NVMe/TCP, NVMe/RDMA (RoCE) | Sehr niedrige Latenz für Flash-Speicher | Relativ neu, hohe Anforderungen an Infrastruktur | 🟡 |

> **IHK-Typfrage:** *„Vergleichen Sie Fibre Channel und iSCSI im SAN-Einsatz.“*  
> **Musterantwort:** Fibre Channel ist eine klassische Storage-Netzwerktechnologie mit sehr hoher Performance und Stabilität, erfordert aber meist spezielle Hardware und Fachwissen. iSCSI nutzt vorhandenes Ethernet und TCP/IP, ist kostengünstiger, aber Leistung und Latenz hängen stark von der Ethernet-Infrastruktur und Netzauslastung ab.

### 3.2 Adressierung: WWPN, WWNN und IQN

| Merkmal | Fibre Channel | iSCSI |
|---|---|---|
| **Typische Identifikatoren** | WWPN, WWNN | IQN, gegebenenfalls EUI/NAA |
| **WWPN** | Eindeutige Kennung eines FC-Ports | Nicht vorhanden |
| **WWNN** | Kennung eines FC-Nodes beziehungsweise Geräts | Nicht vorhanden |
| **IQN** | Nicht verwendet | Eindeutiger iSCSI-Name für Initiator oder Target |
| **Verwendung** | Zoning, LUN-Masking, Fabric-Zuordnung | Discovery, Login, ACLs und Target-/Initiator-Konfiguration |

- **WWPN** = World Wide Port Name (eindeutige Kennung eines einzelnen FC-Ports)  
- **WWNN** = World Wide Node Name (Kennung eines Fibre-Channel-Nodes; ein Node kann z. B. ein HBA, ein Storage-Controller oder ein anderes FC-Gerät sein und mehrere Ports/WWPNs besitzen)  
- **IQN** = iSCSI Qualified Name, z. B. `iqn.2001-04.com.example:storage.disk2.sys1.xyz`

> **Wichtig:** Das Datum im IQN bezeichnet den Zeitraum, in dem die Organisation die verwendete Domain besaß – nicht das Erstellungsdatum des Geräts.

**iSCSI-Initiator und iSCSI-Target:**

| Begriff | Bedeutung |
|---|---|
| **iSCSI-Initiator** | Client beziehungsweise Host, der iSCSI-Verbindungen aufbaut |
| **iSCSI-Target** | Storage-Endpunkt, der iSCSI-LUNs bereitstellt |

> **IHK-Typfrage:** *„Wozu dient die WWPN bei Fibre Channel?“*  
> **Musterantwort:** Die WWPN ist eine weltweit eindeutige Adresse eines FC-Ports (z. B. am HBA). Sie wird für Zoning und LUN-Masking verwendet, um den Zugriff auf Storage-Ressourcen gezielt zu steuern.

---

## 4. Betrieb und Sicherheit

Im Betrieb stehen **Stabilität, Verfügbarkeit und Zugriffskontrolle** im Vordergrund.

### 4.1 Zoning (FC) – Zugriffskontrolle im Fabric

Zoning legt fest, welche Hosts mit welchen Storage-Ports kommunizieren dürfen. Dabei muss man zwei unterschiedliche Klassifizierungen trennen:

**a) Wie wird die Zone technisch durchgesetzt?**

| Zoning-Art | Technisches Prinzip | Bewertung |
|---|---|---|
| **Soft Zoning** | Der Name Server zeigt einem Gerät nur zulässige Kommunikationspartner | Steuert die Sichtbarkeit, ersetzt aber keine vollständige Zugriffskontrolle; für stärkere Durchsetzung wird Hard Zoning eingesetzt |
| **Hard Zoning** | Der Switch setzt Zugriffsregeln im Datenpfad beziehungsweise per Hardware-ACL durch | Stärker durchgesetzt |

**b) Woran orientiert sich die Mitgliedschaft?**

| Zoning-Typ | Prinzip | Vorteil | Nachteil |
|---|---|---|---|
| **Port-based Zoning** | Zone orientiert sich an Switch-Ports | Einfach und physisch nachvollziehbar | Bei Umverkabelung oder Portwechsel muss die Konfiguration angepasst werden |
| **WWPN-based Zoning** | Zone orientiert sich an WWPNs | Flexibler bei Umverkabelung | Bei HBA- oder Porttausch muss die Zone angepasst werden |

> **Merke:** Port-based und WWPN-based beschreiben die **Zuordnung** der Geräte zu einer Zone. Hard und Soft Zoning beschreiben die **technische Durchsetzung** der Zugriffsregel.

> **IHK-Typfrage:** *„Was ist der Unterschied zwischen Hard und Soft Zoning?“*  
> **Musterantwort:** Soft Zoning steuert, welche Geräte ein Host über den Fabric Name Server erkennen kann. Hard Zoning setzt die Zugriffsregel zusätzlich im Datenpfad des Switches durch. Port- und WWPN-basierte Zonen beschreiben dagegen, anhand welcher Merkmale Geräte einer Zone zugeordnet werden.

### 4.2 LUN-Masking

- LUN-Masking wird typischerweise auf dem Storage-System konfiguriert.  
- Dabei werden Initiatoren (z. B. über **WWPNs** bei Fibre Channel oder **IQNs** bei iSCSI) bestimmten Host-Gruppen und den dafür freigegebenen LUNs zugeordnet.  
- Es sorgt dafür, dass ein Host **nur die für ihn freigegebenen LUNs** sieht.

> **Merksatz:**  
> **Zoning regelt, wer im Fabric miteinander kommunizieren darf. LUN-Masking regelt, welche LUNs ein berechtigter Host auf dem Storage sehen darf.**

### 4.3 Multipathing (MPIO)

- **MPIO (Multipath I/O)** stellt mehrere physische Pfade zwischen Host und Storage bereit.  
- Dadurch kann bei einem Pfadausfall ein anderer Pfad verwendet werden.  
- Ob und wie Last verteilt wird, hängt von Betriebssystem, Multipath-Treiber, Storage-System und Path-Selection-Policy ab – MPIO **garantiert nicht automatisch Lastverteilung**. ([Broadcom](https://docs.broadcom.com/doc/MP-Load-Bal-OT))  
- Typische Software: Windows MPIO, Linux Device Mapper Multipath, VMware Native Multipathing.

> **IHK-Typfrage:** *„Warum ist Multipathing in einem SAN wichtig?“*  
> **Musterantwort:** Multipathing erhöht die Ausfallsicherheit, da bei einem Pfadfehler automatisch ein anderer Pfad genutzt wird. Je nach Konfiguration kann zusätzlich eine Lastverteilung möglich sein.

### 4.4 Weitere Betriebs- und Sicherheitsaspekte

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| **Redundanz** | Doppelte Controller, Switches, Pfade | 🔴 |
| **Performance-Monitoring** | IOPS, Latenz, Durchsatz, Queue Depth | 🟡 |
| **Kapazitätsmanagement** | Thin Provisioning, Wachstumskontrolle | 🟡 |
| **Backup & Recovery** | Snapshots ersetzen kein unabhängiges Backup; unabhängige Backups, Replikation, Offsite-Konzepte | 🔴 |
| **Sicherheit** | VLANs allein ersetzen keine iSCSI-Authentisierung und kein LUN-Masking; CHAP bei iSCSI, ACLs, Zoning, sichere Management-Zugänge | 🔴 |
| **Change-Management** | Firmware-Stände, Kompatibilitätsmatrizen | 🟢 |

---

## 5. Nutzen und Praxiseinsatz

### 5.1 Warum setzt man SANs ein?

| Nutzen | Beschreibung | IHK-Relevanz |
|---|---|---|
| **Hohe Performance** | Optimierte Speicherpfade und je nach Technologie geringe Latenz | 🔴 |
| **Zentralisierung** | Einheitliche Verwaltung und Zuweisung von Speicher | 🔴 |
| **Skalierbarkeit** | Einfaches Hinzufügen von Kapazität | 🔴 |
| **Hochverfügbarkeit** | Redundanz, Multipathing, Failover | 🔴 |
| **Professioneller Betrieb** | Bessere Backup-/DR-Integration, zentrale Kontrolle | 🟡 |

### 5.2 Typische Einsatzszenarien

- **Virtualisierungsumgebungen** (mehrere Hypervisor-Hosts teilen sich Datastores)
- **Datenbanken / ERP-Systeme** mit hohen I/O-Anforderungen
- **Transaktionssysteme**, die konsistente Performance benötigen

> **IHK-Typfrage:** *„Nennen Sie zwei Gründe für den Einsatz eines SAN in einem Unternehmen.“*  
> **Musterantwort:** Zum einen ermöglicht ein SAN die zentrale Verwaltung und Skalierung von Speicherressourcen, zum anderen erhöht es durch Redundanz und Multipathing die Verfügbarkeit kritischer Systeme.

---

## 6. Risiken und Gegenmaßnahmen

| Risiko | Beschreibung | Gegenmaßnahme | IHK-Relevanz |
|---|---|---|---|
| **Komplexität** | Design, Betrieb, Fehlersuche erfordern Spezialwissen | Schulung, saubere Dokumentation, Monitoring | 🟡 |
| **Kosten** | Spezialhardware (FC), Lizenzen, Wartung | Kosten-Nutzen-Analyse, ggf. iSCSI wählen | 🟡 |
| **Fehlkonfiguration** | Falsches Zoning, LUN-Zuordnung, Multipath | Änderungsmanagement, Tests, redundante Pfade | 🔴 |
| **Herstellerbindung** | Bei FC oft stark an Hersteller gebunden | Offene Standards, Multi-Vendor-Strategie | 🟢 |
| **Single Point of Failure** | Zentrales Storage-System ohne Redundanz | Redundante Controller, Switches, Pfade | 🔴 |
| **Sicherheitslücken** | Unzureichende Zugriffskontrolle, offene Management-Zugänge | Zoning, LUN-Masking, CHAP, VLAN, ACLs, sichere Admin-Zugänge | 🔴 |

> **IHK-Typfrage:** *„Welche Maßnahmen erhöhen die Ausfallsicherheit eines SAN?“*  
> **Musterantwort:** Redundante Hardware (Controller, Switches, Pfade), Multipathing, sauberes Zoning und LUN-Masking, regelmäßige Tests der Failover-Mechanismen sowie ein funktionierendes Backup- und Recovery-Konzept.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Was ist der Hauptunterschied zwischen SAN und NAS? | SAN = Block-Level, NAS = File-Level |
| 2 | Nennen Sie zwei SAN-Transportprotokolle. | Fibre Channel, iSCSI |
| 3 | Wofür steht die Abkürzung HBA? | Host Bus Adapter |
| 4 | Was ist eine LUN? | Logische Speichereinheit (Logical Unit Number), blockorientiertes Speichergerät für einen Host |
| 5 | Was versteht man unter Zoning? | Zugriffskontrolle im FC-Fabric (Host zu Storage) |
| 6 | Wozu dient Multipathing? | Redundanz (Failover), Lastverteilung je nach Konfiguration möglich |
| 7 | Wie heißt die eindeutige Adresse eines FC-Ports? | WWPN (World Wide Port Name) |
| 8 | Welches Protokoll nutzt Port 3260? | iSCSI |
| 9 | Was ist der Unterschied zwischen WWPN und WWNN? | WWPN = FC-Port, WWNN = FC-Node/Gerät |
| 10 | Warum ersetzen Snapshots kein Backup? | Snapshots sind keine unabhängige Kopie; bei Storage-Ausfall oder Ransomware oft nicht ausreichend |

---

## 8. Prüfungszusammenfassung (Cheatsheet)

| Begriff | Kurzdefinition |
|---|---|
| **SAN** | Spezialisiertes Netzwerk für blockbasierten Speicher |
| **NAS** | Datei-basierter Speicher über Netzwerkfreigabe |
| **Fibre Channel** | Klassische Storage-Netzwerktechnologie für SANs |
| **iSCSI** | SCSI über TCP/IP, Port 3260 |
| **HBA** | Schnittstellenkarte für SAN-Anbindung |
| **LUN** | Logische Speichereinheit, die einem Host als Block-Device präsentiert wird |
| **Zoning** | Zugriffskontrolle im FC-Fabric (Soft/Hard, Port/WWPN-basiert) |
| **LUN-Masking** | Steuert, welche LUNs ein Host sehen darf |
| **MPIO** | Multipath I/O – mehrere Pfade zum Storage, Failover und ggf. Lastverteilung |
| **WWPN** | Eindeutige Adresse eines FC-Ports |
| **WWNN** | Eindeutige Adresse eines FC-Geräts/Nodes |
| **IQN** | Eindeutiger Name für iSCSI-Initiator/Target |
| **NVMe-oF** | Zugriff auf NVMe-Speicher über eine Fabric (z. B. NVMe/FC, NVMe/TCP) |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
|---|---|---|
| Definition | „Was ist ein SAN?“ | Blockbasierter Speicher, spezialisiertes Netzwerk, Abgrenzung zu NAS |
| Vergleich | „Unterschied FC vs. iSCSI“ | Kosten, Performance, Hardware, Einsatzumgebung |
| Betrieb | „Wie sichern Sie den Zugriff ab?“ | Zoning, LUN-Masking, CHAP (bei iSCSI), VLAN, ACLs |
| Ausfallsicherheit | „Wie vermeiden Sie Ausfälle?“ | Redundanz, Multipathing, Failover sowie ein Backup- und Recovery-Konzept; Snapshots können die Wiederherstellung ergänzen, ersetzen aber kein unabhängiges Backup |
| Konzeption | „Planen Sie ein SAN für 3 Server“ | Komponenten nennen, Zoning, Redundanz, Protokollwahl begründen |

---

## 10. Merksätze für das mündliche Fachgespräch

> SAN = Block, NAS = Datei – das ist die wichtigste Unterscheidung.

> Fibre Channel ist eine klassische, leistungsfähige Storage-Netzwerktechnologie, die meist spezielle Hardware und entsprechendes Fachwissen erfordert. iSCSI nutzt Ethernet und TCP/IP und kann dadurch kostengünstiger umgesetzt werden.

> Zoning regelt, wer im Fabric miteinander kommunizieren darf. LUN-Masking regelt, welche LUNs ein berechtigter Host sehen darf.

> Redundanz ist kein Luxus, sondern Pflicht: doppelte Controller, doppelte Switches, doppelte Pfade.

> Multipathing sorgt dafür, dass bei einem Pfadausfall ein anderer Pfad verwendet werden kann. Je nach Konfiguration kann es zusätzlich die Last verteilen.

> Ein SAN wird nicht wegen „mehr Speicher“ eingesetzt, sondern wegen zentraler Kontrolle, Performance und Verfügbarkeit.

---

## Quellen

1. Storage Networking Industry Association (SNIA):  
   Storage Area Network, SNIA Dictionary  
   https://www.snia.org/education/online-dictionary/term/storage-area-network

2. Storage Networking Industry Association (SNIA):  
   What is a Storage Area Network?  
   https://www.snia.org/education/storage_networking_primer/san/what_san

3. RFC 7143:  
   Internet Small Computer Systems Interface (iSCSI) Protocol  
   https://www.rfc-editor.org/rfc/rfc7143

4. Cisco:  
   Configuring and Managing Zones, Cisco MDS Fabric Configuration Guide  
   https://www.cisco.com/c/en/us/td/docs/switches/datacenter/mds9000/sw/8_x/config/fabric/cisco_mds9000_fabric_config_guide_8x/configuring_and_managing_zones.html

5. Broadcom:  
   Multipath Load Balancing Recommendations  
   https://docs.broadcom.com/doc/MP-Load-Bal-OT

Youtube: https://www.youtube.com/watch?v=3yZDDr0JKVc /SAN NAS Visuell erklärt
         https://www.youtube.com/watch?v=5-UO8RE1Ctk /DAS NAS SAN erklärt
         https://www.youtube.com/watch?v=o-83E6levzM /Backup Typs Bonus

> Abrufdatum der Onlinequellen: 14. August 2026
