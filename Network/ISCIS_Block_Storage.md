# iSCSI – Block-Storage über TCP/IP

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 25–35 Minuten
> **Status:** Final
> **Stand:** 2026

---

## IHK-Kernfragen (Sprungmarken)

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was ist iSCSI und wie ordnet es sich in eine Speicherarchitektur ein? | [1. Grundprinzip](#1-grundprinzip-und-einordnung) |
| 2 | Was unterscheidet SAN (iSCSI) von NAS (SMB/NFS)? | [2. SAN vs. NAS](#2-san-vs-nas) |
| 3 | Was sind Initiator, Target und LUN? | [3. Architektur](#3-architektur-und-komponenten) |
| 4 | Warum wird iSCSI in Virtualisierungsumgebungen eingesetzt? | [4. Praxiseinsatz](#4-praxiseinsatz) |
| 5 | Welche Sicherheitsmaßnahmen sind bei iSCSI sinnvoll? | [5. Sicherheit und Risiken](#5-sicherheit-und-risiken) |

---

## 1. Grundprinzip und Einordnung

> iSCSI verpackt klassische SCSI-Blockbefehle in TCP/IP-Pakete – für den Server sieht ein entfernter Speicher dadurch aus wie eine lokal eingebaute Festplatte.

### 1.1 Was ist iSCSI?

| Aspekt | Beschreibung | IHK-Relevanz |
|---|---|---|
| Name | Internet Small Computer System Interface | 🔴 |
| Funktion | Transportprotokoll für SCSI-Kommandos über TCP/IP-Netzwerke | 🔴 |
| Zugriffsebene | Block-Level-Storage (nicht Datei-Ebene) | 🔴 |
| Einsatzzweck | Aufbau eines Storage Area Network (SAN) über normales Ethernet statt Fibre Channel | 🔴 |
| Standardport | TCP 3260 (von IANA vergeben) | 🔴 |

**Analogie (Gärtnerei-Kontext):** Stell dir vor, dein Gewächshaus (Server) braucht Wasser aus einem zentralen Brunnen (Storage-Array), der drei Straßen weiter steht. iSCSI ist die Rohrleitung durch das bestehende Wassernetz (TCP/IP) – am Hahn im Gewächshaus kommt trotzdem ganz normal Wasser raus, so als stünde der Brunnen direkt daneben. Man merkt dem Endgerät die Entfernung nicht an.

> **IHK-Typfrage:** *„Erläutern Sie kurz den Begriff iSCSI und ordnen Sie ihn in eine Speicherarchitektur ein."*
> **Musterantwort:** iSCSI überträgt SCSI-Blockbefehle über TCP/IP-Netzwerke (Standardport 3260). Es dient dem Aufbau eines Storage Area Network (SAN) über Ethernet-Infrastruktur, wobei entfernte Speicher (LUNs) dem Betriebssystem als lokale Datenträger erscheinen.

---

## 2. SAN vs. NAS

| Aspekt | SAN (z. B. iSCSI) | NAS (z. B. SMB/NFS) | IHK-Relevanz |
|---|---|---|---|
| Zugriffsebene | Block-Level (rohe Blöcke) | File-Level (Dateien/Ordner) | 🔴 |
| Erscheinungsbild am Client | Wie lokale Festplatte (z. B. `/dev/sdb`) | Netzwerkfreigabe (Share) | 🔴 |
| Dateisystem | Wird vom Client verwaltet | Wird vom Storage-System verwaltet | 🟡 |
| Typischer Einsatz | VM-Datastores, Datenbanken | Dateiablage, gemeinsame Dokumente | 🔴 |

```
Client                       SAN (iSCSI)                File-Server (NAS)
  │                              │                              │
  │  SCSI-Kommandos über TCP     │      SMB/NFS-Anfragen         │
  │ ───────────────────────────►│                                │
  │  sieht: /dev/sdb (Block)     │      sieht: \\server\share    │
  │  legt selbst Dateisystem an  │      Dateisystem liegt auf     │
  │                              │      dem Server                │
```

> **IHK-Typfrage:** *„Unterscheiden Sie SAN und NAS unter Verwendung von iSCSI und SMB/NFS."*
> **Musterantwort:** Ein SAN (z. B. über iSCSI) stellt Block-Level-Speicher bereit, der Client sieht ihn als lokale Festplatte und verwaltet selbst das Dateisystem. Ein NAS (z. B. über SMB/NFS) stellt File-Level-Speicher als Netzwerkfreigabe bereit, das Dateisystem liegt auf dem Server.

---

## 3. Architektur und Komponenten

> Initiator fragt an, Target liefert – dazwischen liegt eine TCP-Session, in der SCSI-Kommandos als iSCSI-PDUs verpackt werden.

### 3.1 Die Kernbegriffe

| Begriff | Beschreibung | IHK-Relevanz |
|---|---|---|
| **Initiator** | Client-Komponente auf dem Server, die SCSI-Kommandos erzeugt (Software: Windows-iSCSI-Initiator, Linux `open-iscsi`; oder Hardware-HBA) | 🔴 |
| **Target** | Speichersystem, das LUNs bereitstellt und Kommandos verarbeitet | 🔴 |
| **LUN** (Logical Unit Number) | Vom Target bereitgestellte logische SCSI-Speichereinheit. In der Praxis entspricht sie meist einem Volume/Datenträger – aber „LUN" bezeichnet ursprünglich die Kennung, nicht automatisch „das Volume" | 🔴 |
| **Session** | Logische iSCSI-Verbindung zwischen Initiator und Target. Eine Session kann mehrere TCP-Verbindungen enthalten | 🟡 |
| **MPIO** (Multipath I/O) | Nutzung mehrerer redundanter Netzwerkpfade (getrennte NICs, Switches, Storage-Ports) zwischen Host und Target für Lastverteilung und Failover. Schützt nur, wenn die Pfade *wirklich* getrennt aufgebaut sind | 🟡 |
| **PDU** (Protocol Data Unit) | Container, in dem SCSI-Kommandos/Daten/Status über TCP transportiert werden | 🟢 |
| **IQN** (iSCSI Qualified Name) | Eindeutiger Name für Initiator/Target nach dem Schema `iqn.JJJJ-MM.reverse-domain:eindeutiger-name`, z. B. `iqn.2010-05.com.example:storage.array1` | 🟢 |

> **Wichtige Unterscheidung:** Eine Session kann aus mehreren TCP-Verbindungen bestehen – das ist noch kein Multipathing. MPIO ist ein eigenes Konzept: mehrere unabhängige, redundante Pfade zwischen Host und Storage.

### 3.2 Ablauf einer Verbindung

1. Initiator wird auf dem Server konfiguriert (Ziel-IP des Targets eintragen).
2. Discovery: Initiator fragt Target nach verfügbaren LUNs (z. B. via SendTargets).
3. Login/Session-Aufbau, ggf. mit CHAP-Authentifizierung.
4. LUN wird im Betriebssystem als Blockgerät sichtbar (z. B. neues Volume in der Datenträgerverwaltung).
5. Betriebssystem legt Dateisystem an oder nutzt das Volume direkt (z. B. als VM-Datastore).

> **IHK-Typfrage:** *„Was versteht man bei iSCSI unter einem Initiator und einem Target?"*
> **Musterantwort:** Der Initiator ist die Client-Komponente auf dem Server, die SCSI-Anfragen stellt. Das Target ist das Speichersystem, das diese Anfragen entgegennimmt und über LUNs bedient.

---

## 4. Praxiseinsatz

| Szenario | Nutzen | IHK-Relevanz |
|---|---|---|
| Virtualisierung (ESXi, Hyper-V, Proxmox) | Mehrere Hosts können gemeinsamen iSCSI-Storage als Datastore nutzen – **vorausgesetzt**, Hypervisor/Dateisystem unterstützt gleichzeitigen Zugriff (z. B. VMFS bei VMware) | 🔴 |
| Storage-Konsolidierung | Zentrale Verwaltung und flexible Erweiterung statt vieler lokaler Server-Disks; Backup/Snapshots vereinfachen sich nur bei sauberer Planung und Applikationskonsistenz | 🔴 |
| KMU-Umgebungen | Nutzung vorhandener Ethernet-Infrastruktur statt teurer Fibre-Channel-Hardware | 🟡 |
| Datenbanken auf zentralem Storage | Unterstützt zentrale Verwaltung, Backup und bestimmte HA-Konzepte – **ersetzt aber keine Datenbankreplikation** | 🟡 |

> ⚠️ **Praxisfalle:** Ein normales NTFS-, ext4- oder XFS-Dateisystem darf **nicht** einfach gleichzeitig von mehreren Hosts schreibend eingebunden werden. Gemeinsamer Zugriff braucht ein Cluster-/Shared-Filesystem (z. B. VMFS) oder ein entsprechendes Storage-Konzept.

> **IHK-Typfrage:** *„Warum wird in vielen Virtualisierungsumgebungen iSCSI eingesetzt?"*
> **Musterantwort:** iSCSI stellt mehreren Hypervisor-Hosts zentralen Block-Storage bereit. Sofern der Hypervisor bzw. das Dateisystem gleichzeitige Zugriffe unterstützt (z. B. VMFS), können die Hosts gemeinsame Datastores nutzen. Darauf aufbauend werden – abhängig von der Umgebung – Funktionen wie Live-Migration, HA und zentrale VM-Verwaltung möglich. Für Ausfallsicherheit sind zusätzlich MPIO und redundante Storage-/Netzwerkkomponenten nötig.

### 4.1 Performance-Optimierung

| Maßnahme | Wirkung | IHK-Relevanz |
|---|---|---|
| Jumbo Frames (MTU 9000) | Reduziert Header-Overhead bei großen Block-Transfers, senkt CPU-Last auf Server und Target | 🟡 |
| Dediziertes Storage-VLAN | Vermeidet Konkurrenz mit normalem LAN-Verkehr | 🟡 |
| MPIO | Lastverteilung über mehrere Pfade zusätzlich zur Redundanz | 🟡 |

---

## 5. Sicherheit und Risiken

| Maßnahme | Zweck | IHK-Relevanz |
|---|---|---|
| CHAP | **Authentifizierung** von Initiator und Target – verschlüsselt die Daten **nicht** | 🔴 |
| Separates Storage-VLAN/-Netz | Trennt Storage-Verkehr vom Benutzer-/Servernetz, reduziert Angriffsfläche – ersetzt aber keine Zugriffskontrolle | 🔴 |
| Firewall-/ACL-Regeln | Nur berechtigte Hosts dürfen auf TCP 3260 und definierte Targets zugreifen | 🔴 |
| LUN-Masking/Zugriffskontrolle | Nur berechtigte Initiatoren sehen bestimmte LUNs (bei iSCSI: keine „Zoning"-Begrifflichkeit wie bei Fibre Channel) | 🟡 |
| IPsec (bei Bedarf) | Verschlüsselung des Datenverkehrs, falls Vertraulichkeit gefordert ist | 🟢 |
| MPIO / Redundante Storage-Komponenten | Schutz vor Ausfall von Controller, Netzteil, Port oder Laufwerk | 🔴 |

> **CHAP-Arten:** *One-Way CHAP* (nur das Target prüft den Initiator) vs. *Mutual/bidirektionales CHAP* (beide Seiten authentifizieren sich gegenseitig). Für höhere Sicherheitsanforderungen wird Mutual CHAP gefordert.

> **Netzwerkabhängigkeit:** Bei Netzwerkausfall ist der zentrale Storage nicht erreichbar. Ohne Redundanz ist das zentrale Storage-System selbst ein **Single Point of Failure** – der Konsolidierungsvorteil kippt dann ins Risiko.

> **IHK-Typfrage:** *„Welche Sicherheitsmaßnahmen sind bei der Nutzung von iSCSI in einem Unternehmensnetzwerk sinnvoll?"*
> **Musterantwort:** CHAP zur Authentifizierung von Initiator und Target (idealerweise Mutual CHAP), ein separates Storage-VLAN kombiniert mit Firewall-/ACL-Regeln, LUN-Masking zur Zugriffsbeschränkung, bei Bedarf IPsec zur Verschlüsselung sowie redundante Auslegung (MPIO, redundante Storage-Komponenten) gegen Ausfälle. CHAP allein verschlüsselt keine Daten – dafür ist zusätzlich IPsec nötig.

---

## 6. Selbsttest

| # | Frage | Kurzantwort |
|---|---|---|
| 1 | Welche Transportschicht nutzt iSCSI? | TCP/IP, Standardport 3260 |
| 2 | Was ist der Unterschied zwischen Initiator und Target? | Initiator = Client (fordert an), Target = Speichersystem (liefert LUNs) |
| 3 | Block-Level oder File-Level? | iSCSI ist Block-Level-Storage (im Gegensatz zu NAS/SMB/NFS) |
| 4 | Wofür wird CHAP genutzt – und wofür nicht? | Authentifizierung zwischen Initiator und Target; **keine** Verschlüsselung |
| 5 | Was braucht ein gemeinsamer VM-Datastore über iSCSI zusätzlich? | Ein Cluster-/Shared-Filesystem (z. B. VMFS), das gleichzeitigen Zugriff mehrerer Hosts unterstützt |
| 6 | Was ist der Unterschied zwischen Session und MPIO? | Session = TCP-Verbindung(en) zu einem Pfad; MPIO = mehrere redundante Pfade für Failover/Lastverteilung |

---

## 7. IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| iSCSI | SCSI-Kommandos über TCP/IP, Block-Storage |
| Initiator | Client-Komponente auf dem Server |
| Target | Speichersystem, stellt LUNs bereit |
| LUN | Logische Speichereinheit auf dem Target |
| SAN | Storage Area Network, Block-Level-Zugriff |
| NAS | Network Attached Storage, File-Level-Zugriff |
| Port 3260 | Standard-TCP-Port für iSCSI |
| CHAP | Authentifizierung (nicht Verschlüsselung!) zwischen Initiator/Target |
| MPIO | Mehrere redundante Pfade zwischen Host und Target |
| Jumbo Frames | MTU 9000, reduziert Overhead bei Block-Transfers |
| IQN | `iqn.JJJJ-MM.reverse-domain:name` – eindeutiger iSCSI-Name |
| PDU | Container für SCSI-Kommandos im iSCSI-Transport |
| RFC 7143 | Aktuelle konsolidierte iSCSI-Spezifikation (löst RFC 3720 ab) |

---

## 8. Prüfungstaktik

| Aufgabentyp | Formulierung | Was die IHK hören will |
|---|---|---|
| Definition | „Erläutern Sie iSCSI" | Block-Storage über TCP/IP, Port 3260, SAN-Kontext |
| Vergleich | „Unterschied SAN/NAS" | Block- vs. File-Level, konkrete Beispiele (iSCSI vs. SMB/NFS) |
| Konzeption | „Skizzieren Sie eine Lösung für X Hosts mit gemeinsamem Storage" | Initiator/Target/LUN nennen, Shared-Filesystem-Voraussetzung erwähnen, VLAN + MPIO/Redundanz |
| Sicherheit | „Welche Maßnahmen..." | CHAP (+Hinweis: keine Verschlüsselung), VLAN-Trennung, Firewall/LUN-Masking, Redundanz – nicht nur eine Maßnahme nennen |
| Performance | „Wie optimiert man ein iSCSI-Netz?" | Jumbo Frames, dediziertes VLAN, MPIO |

---

## 9. Merksätze für die mündliche Prüfung

> iSCSI macht aus einem entfernten Speicher scheinbar eine lokale Festplatte – transportiert wird SCSI über TCP/IP.

> SAN = Blöcke, NAS = Dateien. Das ist der Kernunterschied, den die IHK hören will.

> Initiator fragt, Target liefert, die LUN ist das, was am Ende als Datenträger erscheint.

> iSCSI gehört nicht ungeschützt ins normale Benutzer-LAN – separates Storage-Netz, CHAP und restriktive Zugriffsregeln sind die Basis, nicht die Kür.

> Ein zentrales Storage-System ist nur so gut wie seine Redundanz – sonst wird der Vorteil (Konsolidierung) zum Risiko (SPoF).

---

```yaml
titel: "iSCSI – Block-Storage über TCP/IP"
kategorie: "LF7 / Netzwerk & Storage"
typ: "Typ A – Kompakter Prüfungs-Wiki"
ihk_relevanz: "AP1 schriftlich, Fachgespräch"
quellen:
  - "RFC 3720 (2004) – ursprüngliche iSCSI-Spezifikation, obsolet"
  - "RFC 7143 (2014) – konsolidierte iSCSI-Spezifikation, löst RFC 3720/3980/4850/5048 ab"
  - "RFC 7144 (2014) – iSCSI SCSI Features Update (SAM-3/4/5-Erweiterungen)"
  - "RFC 3721 – iSCSI Naming and Discovery"
autor: "David"
stand: "2026"
status: "final"
```
