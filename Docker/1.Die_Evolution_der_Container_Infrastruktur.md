

# Die Evolution der Container-Infrastruktur im Jahr 2026: Architektonische Divergenzen, Sicherheits-Compliance und die Relevanz für die IT-Berufsausbildung

> **📘 Inhaltsverzeichnis**

> 1. [Marktlage & ökonomische Verschiebungen](#1-marktlage--ökonomische-verschiebungen-im-jahr-2026)

> 2. [Technische Architekturanalyse](#2-technische-architekturanalyse-und-differenzierung)

> 3. [Deep Dive: CLI bis Kernel](#3-deep-dive-der-workflow-von-der-cli-bis-zum-kernel-level)

> 4. [Grundlagen: Linux-Prozessmodell](#4-grundlagen-warm-up-das-linux-prozessmodell-und-die-virtualisierungs-divergenz)

> 5. [Betriebssystem-Primitive](#5-die-betriebssystem-primitive-der-containerisierung)

> 6. [Sicherheit & Compliance](#6-sicherheitsaspekte-und-compliance-richtlinien-im-enterprise-umfeld)

> 7. [Effizientes Image-Design](#7-effizientes-image-design-und-multi-stage-build-konzepte)

> 8. [Zukunftsaspekte: WASM & Edge](#8-zukunftsaspekte-die-strategische-bedeutung-von-webassembly-wasm-und-edge-computing)

> 9. [Relevanz für die IT-Ausbildung](#9-die-relevanz-in-der-it-berufsausbildung-und-für-umschüler)

> 10. [Zertifizierungen: DCA vs. CKA](#10-zertifizierungen-als-karriere-katalysator-dca-vs-cka)

---

## 1. Marktlage & ökonomische Verschiebungen im Jahr 2026

Der globale Markt für Container-Technologien wächst 2026 stabil auf ein Volumen von rund **1,22 Milliarden US-Dollar**. Prognosen sagen einen Anstieg auf **6,43 Milliarden US-Dollar bis 2035** voraus (CAGR ≈ 19,8 %). Getrieben wird dies durch die flächendeckende Cloud-nativer Architekturen: **Über 85 % aller Unternehmen** setzen auf Container, mehr als **70 % betreiben diese produktiv**.

Statt einer Monokultur hat sich eine **strategische Koexistenz verschiedener Laufzeitumgebungen** etabliert. Der Trend geht zu hybriden Strategien (34 % der Organisationen), bei denen Tools je nach Anforderung kombiniert werden:

- **Docker** für die lokale Entwicklung

- **Podman** für CI/CD-Pipelines

- **containerd** als Runtime in Kubernetes

| Container-Technologie | Marktanteil (Entwickler) | Primärer Einsatzbereich | Lizenzierungskosten |
| :--- | :---: | :--- | :--- |
| **Docker / Docker Desktop** | **67 %** | Lokale Entwicklung, GUI, Prototyping | Kostenpflichtig für Unternehmen >250 MA / >10 Mio. $ Umsatz (9–24 $ / Nutzer / Monat) |
| **Podman** | **19 %** | CI/CD-Pipelines, hochsichere Umgebungen (Finanzen, Behörden) | Open Source (Apache 2.0) |
| **containerd** (direkt) | **11 %** | Standard-Runtime (CRI) für produktive Kubernetes-Cluster (95 % Abdeckung) | Open Source (CNCF) |

> **💸 Kostendruck als Treiber:** Seit den Lizenzänderungen für Docker Desktop (2021) und der Bündelung von Cloud-Diensten (2024/25) ist Docker für große Teams teuer. Ein Team von 200 Entwicklern zahlt jährlich ca. **50.400 US-Dollar** (Business-Tarif). Dies beschleunigte den Aufstieg kostenfreier Alternativen wie **Podman Desktop**, das bis Feb. 2026 über **3 Millionen Downloads** verzeichnete.

---

## 2. Technische Architekturanalyse und Differenzierung

Die Architektur bestimmt die Eignung der Runtime für verschiedene Szenarien.

| Architekturmerkmal | Docker (Daemon-basiert) | Podman (Daemonless) | containerd (Minimal Runtime) |
| :--- | :--- | :--- | :--- |
| **Modell** | Client-Server (`dockerd`) | Fork-Exec (direkte Kindprozesse) | Modular/Plugin-basiert (Daemon-gestützt) |
| **Root-Rechte** | Daemon läuft oft mit root (Rootless-Modus bei nur 8 %) | Von Grund auf "Rootless" konzipiert | Variabel/Minimal |
| **Fehlertoleranz** | Single Point of Failure (Daemon) | Kein zentraler Dienst, Prozessausfall ist isoliert | Hochverfügbar via Shim-Prozess |
| **Kubernetes-Integration** | Dockershim entfernt (seit v1.24) | Eingeschränkt (Pod-Generierung möglich) | **Nativ via CRI** (Standard in 95 % aller Cluster) |

<details>
<summary><b>📊 Technische Kennzahlen im direkten Vergleich</b></summary>

| Kennzahl | Docker (dockerd) | Podman (Daemonless) | containerd |
| :--- | :---: | :---: | :---: |
| **RAM Leerlauf** | 140–180 MB | **0 MB** | ~30 MB |
| **RAM Gesamt-Fußabdruck** | ~2 GB (inkl. VM, UI) | ~500 MB (inkl. VM) | **~50 MB** |
| **Durchschn. Startzeit** | ~1,2 Sekunden | **~0,8 Sek.** (33 % schneller) | Minimal |
| **Kernel-Capabilities** | 14 Capabilities | **11 Capabilities** | Variabel/Minimal |

</details>

<br>

> **✅ Fazit der Divergenz:**

> - **Docker:** Unerreichte Developer Experience (Compose v2, Extensions).

> - **Podman:** Schließt die Sicherheitslücke in CI/CD, da rootless Betrieb teure Admin-Rechte auf Build-Runnern spart.

> - **containerd:** Das Arbeitstier für produktiven Kubernetes-Betrieb mit minimalem Overhead.

---

## 3. Deep Dive: Der Workflow von der CLI bis zum Kernel-Level

Am Beispiel `docker run -d -p 8080:80 nginx` wird der Weg eines Containers durch die Abstraktionsschichten nachvollzogen – einfach und übersichtlich als Schritt-für-Schritt-Ablauf.

**Schritt 1:** Docker CLI → REST API über Unix-Socket → dockerd  
**Schritt 2:** dockerd → Image lokal? (Ja: weiter / Nein: Registry Pull) → gRPC-Aufruf → containerd  
**Schritt 3:** containerd → Snapshotter & OCI-Konfig → containerd-shim  
**Schritt 4:** containerd-shim → startet runc  
**Schritt 5:** runc → clone(), cgroups → Linux Kernel → Container läuft als isolierter Prozess

<details>
<summary><b>🔍 Schritt-für-Schritt-Erläuterung</b></summary>

1.  **CLI & Daemon:** Der Befehl wird als JSON-Payload über das Unix-Socket `/var/run/docker.sock` an den Hintergrunddienst `dockerd` gesendet.

2.  **Image-Prüfung:** Der Daemon prüft, ob das Image lokal vorhanden ist. Fehlt es, authentifiziert er sich bei der Registry, lädt die Layer herunter und persistiert sie.

3.  **Delegation an containerd:** Sobald das Image bereit ist, delegiert `dockerd` die Container-Erstellung per **gRPC** an die High-Level-Runtime `containerd`.

4.  **Vorbereitung:** `containerd` erzeugt mithilfe eines Snapshotter das Dateisystem und schreibt die OCI-konforme `config.json`.

5.  **Shim als Isolationsschicht:** Für jeden Container startet `containerd` einen eigenen `containerd-shim`-Prozess. Dieser bleibt als Elternprozess des Containers aktiv und hält die Ein-/Ausgabekanäle offen – selbst dann, wenn der Docker-Daemon oder containerd neu gestartet werden.

6.  **runc erstellt den Container:** Der Shim ruft die Low-Level-Runtime `runc` auf. `runc` führt den Systemaufruf `clone()` mit den erforderlichen Namespace-Flags (z. B. `CLONE_NEWPID`, `CLONE_NEWNET`) aus und setzt die Ressourcenlimits über das cgroups-Dateisystem (`/sys/fs/cgroup/`).

7.  **Übergabe und Beendigung:** Nach erfolgreichem Start übergibt `runc` die Prozesskontrolle an den wartenden Shim und beendet sich selbst. Der Container läuft nun als isolierter Linux-Prozess.

</details>

---

## 4. Grundlagen-Warm-up: Das Linux-Prozessmodell und die Virtualisierungs-Divergenz

**User-Space vs. Kernel-Space:**

- **Kernel-Space:** Der Kern des OS mit Vollzugriff auf Hardware (CPU, RAM). Verwaltet Ressourcen.

- **User-Space:** Geschützter Bereich für Anwendungen (Datenbanken, Webserver). Zugriff auf Hardware nur durch 

**Systemaufrufe (Syscalls)** an den Kernel.

**Prozess:** Eine laufende Instanz eines Programms mit eigener PID, virtuellem Speicher und Umgebungsvariablen.

**Virtuelle Maschine vs. Container:**

| Ebene | Virtuelle Maschine (VM) | Container |
| :--- | :--- | :--- |
| **Isolations-Ebene** | **Hardware-Ebene** (Hypervisor emuliert Hardware) | **Prozess-Ebene** (Nutzung der Kernel-Primitive des Hosts) |
| **Betriebssystem** | Jede VM besitzt eigenes, vollständiges **Guest-OS** + Kernel | **Kein eigenes OS.** Alle Container teilen sich den Host-Kernel. |
| **Overhead** | Hoch (mehrere GB RAM pro VM, Boot in Minuten) | Minimal (Start in Millisekunden, kaum RAM-Extraverbrauch) |
| **Isolationsstärke** | Sehr stark (komplette physische Trennung) | Stark (logische Trennung durch Kernel-Features), geringere Angriffsfläche durch Host-Teilung |

---

## 5. Die Betriebssystem-Primitive der Containerisierung

Container sind keine VMs, sondern reguläre Linux-Prozesse, die durch Kernel-Mechanismen in ihrer Sicht und Ressourcennutzung beschränkt werden.

| Primitive | Funktion |
| :--- | :--- |
| **Namespaces** | **Was der Prozess sieht.** Sie erzeugen für den Container die Illusion eines exklusiven Systems. |
| *PID-Namespace* | Eigene Prozess-ID-Hierarchie (Container-Prozess sieht sich als PID 1). |
| *NET-Namespace* | Isolierte Netzwerk-Interfaces, IPs, Routing-Tabellen. Verbindung über `veth`-Paare. |
| *MNT-Namespace* | Isolierte Dateisystem-Mounts. `pivot_root` lenkt das Stammverzeichnis um und verbirgt das Host-FS. |
| *USER-Namespace* | Rechte-Umwandlung: Container-Root (UID 0) wird auf einen unprivilegierten Host-User gemappt. |
| **Control Groups (cgroups v2)** | **Wie viel der Prozess bekommt.** Zentrales Ressourcen-Management (CPU, RAM, I/O). Verhindert, dass ein Container das Host-System lahmlegt. |
| **OverlayFS (Copy-on-Write)** | **Effizientes Speicher-Backend.** Ein Image besteht aus schreibgeschützten Layern (`LowerDir`). Änderungen werden in einen flüchtigen `UpperDir` kopiert (Copy-up). Mehrere Container teilen sich einen Basis-Layer. |

---

## 6. Sicherheitsaspekte und Compliance-Richtlinien im Enterprise-Umfeld

> **⚠️ Kritische Sicherheitsanforderung:** Compliance-Frameworks wie SOC 2 und HIPAA fordern das Prinzip der **minimalen Rechtevergabe (Least Privilege)**. Der privilegierte Docker-Daemon stellt hier eine Gefahr dar.

### 🔒 OWASP & HIPAA Best Practices für 2026

1.  **Daemon-Absicherung:** Das Unix-Socket `/var/run/docker.sock` **niemals** unverschlüsselt im Netzwerk freigeben oder in unsichere Container mounten. Der Besitz des Sockets ist äquivalent zum Host-Root-Zugriff.

2.  **Netzwerkisolation:** Inter-Container-Kommunikation standardmäßig deaktivieren (`--icc=false`). Nur explizite, benutzerdefinierte Netzwerke nutzen.

3.  **Privilegien-Minimierung:** Keinesfalls das `--privileged` Flag nutzen. Stattdessen alle Capabilities entziehen (`--cap-drop=ALL`) und selektiv hinzufügen (`--cap-add=NET_BIND_SERVICE`). Container mit `--read-only` Root-Dateisystem betreiben.

4.  **Schwachstellen-Scans:** Jedes Image in der CI/CD-Pipeline automatisiert scannen (z. B. mit **Trivy** oder Docker Scout).

5.  **Sicheres Secrets-Management:** API-Keys & Passwörter **niemals** als Umgebungsvariablen. Dedizierte, in-memory Secrets-Manager (z. B. HashiCorp Vault, Docker Secrets) verwenden.

6.  **Datenverschlüsselung (Data at Rest):** Persistente Speichermedien verschlüsseln, Schlüsselmanagement via Hardware-Security-Modul (HSM) oder Cloud-KMS.

---

## 7. Effizientes Image-Design und Multi-Stage-Build-Konzepte

Multi-Stage-Builds beheben das Problem aufgeblähter Images, indem Build-Tools und -Abhängigkeiten nicht in das produktive Image gelangen.

### 📉 Optimierungspotential durch Multi-Stage-Builds

| Technologie | Single-Stage | Multi-Stage | Reduktion |
| :--- | :---: | :---: | :---: |
| **Rust Web Server** | 1,5 GB | **8 MB** | **99 %** |
| **Go API Server** | 850 MB | **15 MB** | **98 %** |
| **React Frontend** | 1,2 GB | **25 MB** | **98 %** |
| **Node.js Express** | 950 MB | **180 MB** | **81 %** |
| **Java Spring Boot** | 700 MB | **280 MB** | **60 %** |

<br>

<details>
<summary><b>💡 Beispiel-Dockerfile: Sicheres, optimiertes Node.js-Image</b></summary>

```dockerfile
# Stufe 1: Der Builder-Prozess
FROM node:20-alpine AS builder
WORKDIR /app

# Strategisches Kopieren für Docker-Build-Cache
COPY package*.json ./
RUN npm ci

# Quellcode kopieren und kompilieren (TypeScript -> JavaScript)
COPY . .
RUN npm run build

# Stufe 2: Minimale Laufzeitumgebung (Production)
FROM node:20-alpine AS runtime
WORKDIR /app

# Nur produktionsrelevante Abhängigkeiten
COPY package*.json ./
RUN npm ci --omit=dev && npm cache clean --force

# Kompilierte Artefakte aus dem Builder kopieren
COPY --from=builder /app/dist ./dist

# Sicherheits-Härtung: Unprivilegierten User anlegen und nutzen
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001 -G nodejs
USER nodejs

EXPOSE 3000
CMD ["node", "dist/index.js"]
```
</details>

---

## 8. Zukunftsaspekte: Die strategische Bedeutung von WebAssembly (WASM) und Edge Computing

Im Jahr 2026 entstehen **über 75 % aller Unternehmensdaten außerhalb zentraler Rechenzentren**. WebAssembly (WASM) mit dem standardisierten WebAssembly System Interface (WASI) wird zur extrem schlanken Alternative für Edge-Workloads.

| Eigenschaft | Klassischer Linux-Container | WebAssembly (WASM) |
| :--- | :---: | :---: |
| **Typische Größe** | 100–200 MB | **2–5 MB** (50–75x kleiner) |
| **Kaltstartzeit** | ~100 ms | **< 1 ms** (z. B. Fermyon Spin) |
| **RAM-Fußabdruck (Leerlauf)** | Mehrere MB | **< 1 MB** (~40 % Reduktion) |
| **Sicherheitsmodell** | Linux-Namespaces & Capabilities | Sandboxed VM auf Bytecode-Ebene |

> **🚀 Marktbewegungen:** Akamai hat 2025 den WASM-Pionier Fermyon übernommen. Docker integriert WASM nativ per `containerd-wasm-shims` in Docker Desktop. WASM wird traditionelle Container nicht ersetzen, sondern dominiert **zustandslose, hochfrequente Serverless-Funktionen** am Edge, während komplexe, I/O-intensive Backends im Container bleiben.

---

## 9. Die Relevanz in der IT-Berufsausbildung und für Umschüler

Der sichere Umgang mit Containern ist für **Fachinformatiker (FISI & FIAE)** eine Schlüsselqualifikation.

### 📚 Einordnung in den IHK-Rahmenlehrplan

| Lernfeld | Relevanz für Container-Technologie |
| :--- | :--- |
| **LF 3** (Clients in Netzwerke einbinden) | Netzwerktechnische Grundlagen für Port-Mappings, Bridge-Netzwerke. |
| **LF 10b** (Serverdienste automatisieren) | Praktische Bereitstellung von Diensten, CI/CD-Pipelines, Docker Compose. |
| **LF 11b** (Betrieb & Sicherheit) | Absicherung von Container-Hosts, Firewall-Regeln, Netzwerkisolation. |
| **LF 12b** (Kundenspezifische Systemintegration) | Konzeption komplexer Multi-Container-Lösungen im Kundenauftrag. |

### 🏆 Das IHK-Abschlussprojekt

> **⚠️ Stolperfalle:** Ein Projekt, das nur das Schreiben eines Dockerfiles oder den `docker run`-Befehl zeigt, ist als eigenständiges Projekt **nicht geeignet** (zu geringe Komplexität, reines "Copy & Paste").

Ein erfolgreicher Projektantrag muss komplexe Entscheidungen umfassen:

1.  **Wirtschaftliche Nutzwertanalyse:** Kaufmännischer Vergleich der Varianten (z. B. "Kosteneinsparung durch Ablösung von Docker Desktop durch Podman im Unternehmen").

2.  **Architekturentscheidung:** Begründete Evaluation: Monolith (VM) vs. Multi-Container (Compose) vs. Kubernetes-Cluster.

3.  **Sicherheits- & Netzwerkkonzept:** Einbindung in bestehende Firewall, VLANs, Reverse-Proxy-Setup (Nginx) zur SSL-Terminierung und Zugriffskontrolle.

---

## 10. Zertifizierungen als Karriere-Katalysator: DCA vs. CKA

Zertifikate helfen Quereinsteigern, ihr Fachwissen formal zu belegen.

### Docker Certified Associate (DCA)

- **Anbieter:** Mirantis
- **Format:** 55 Multiple-Choice-Fragen, 90 Min.
- **Vorbereitung:** ~160 Lernstunden / 8 Wochen
- **Kosten:** ~250 $ (Prüfungsgebühr)

| Prüfungsdomäne | Gewichtung |
| :--- | :---: |
| Orchestration (Docker Swarm) | 25 % |
| Image Creation, Management & Registry | 20 % |
| Installation & Configuration | 15 % |
| Networking | 15 % |
| Security | 15 % |
| Storage & Volumes | 10 % |

### Certified Kubernetes Administrator (CKA)

- **Stellenwert:** Höhere Marktakzeptanz und besseres Gehalt als DCA, da Kubernetes der Orchestrierungs-Standard ist.
- **Empfehlung:** Für Quereinsteiger ist der DCA ein ideales **Zwischenziel**, um die grundlegenden Container-Konzepte zu festigen, die 1:1 auf Kubernetes übertragbar sind.

> **💰 Gehaltsperspektive 2026:**

> - DevOps Engineer **mit** Container-Zertifizierung (CKA): **105.000 – 145.000 US-Dollar**

> - DevOps Engineer **ohne** spezifische Zertifizierung: **95.000 – 130.000 US-Dollar**

### lINKS 

https://www.businessresearchinsights.com/market-reports/container-technology-market-106710

https://eitt.academy/knowledge-base/docker-vs-podman-vs-containerd-comparison-2026/

https://daily.dev/blog/docker-vs-podman-container-runtime-which-to-use/

https://medium.com/@surbhi19/is-docker-still-worth-it-in-2026-or-should-you-switch-to-podman-29d89b42dc80

https://spacelift.io/blog/docker-alternatives

https://oneuptime.com/blog/post/2026-02-08-how-to-understand-docker-containerd-architecture/view

https://docs.docker.com/engine/daemon/alternative-runtimes/

https://www.atlantbh.com/how-docker-containers-work-under-the-hood-namespaces-and-cgroups/

https://oneuptime.com/blog/post/2026-02-02-docker-multi-stage-builds/view

https://www.youtube.com/watch?v=RqTEHSBrYFw