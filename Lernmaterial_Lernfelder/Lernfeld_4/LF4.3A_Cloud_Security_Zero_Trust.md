# LF4.3 (Teil A) – Cloud Security & Zero Trust

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 90–120 Minuten reines Lesen, +60–90 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
> **Teil:** 1 von 2 – Cloud Security & Zero Trust (Teil B: Security Awareness, Supply-Chain, KI-Bedrohungen, OWASP LLM Top 10)
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Wie verteilt sich Sicherheitsverantwortung zwischen Cloud-Anbieter und Kunde bei IaaS, PaaS und SaaS? | [→ 1. Cloud Security](#1-cloud-security-und-shared-responsibility) |
| 2 | Was unterscheidet Container von virtuellen Maschinen, und wofür braucht man Orchestrierung? | [→ 2. Container & Orchestrierung](#2-containerisierung-und-orchestrierung) |
| 3 | Warum reicht das klassische Perimeter-Modell allein nicht mehr aus, und was sind die drei verbreiteten Kernprinzipien von Zero Trust? | [→ 3. Zero Trust](#3-zero-trust-architektur) |
| 4 | Wie ist die Zero-Trust-Referenzarchitektur nach NIST SP 800-207 aufgebaut, und welche fünf Umsetzungssäulen unterscheidet das CISA Zero Trust Maturity Model? | [→ 3. Zero Trust](#3-zero-trust-architektur) |

---

## 1. Cloud Security und Shared Responsibility

> **Grundprinzip:** Eine gemietete Werkshalle mit Vollausstattung ist nicht automatisch sicher, nur weil der Vermieter für Dach und Wände sorgt – wer seine Maschinen unverschlossen stehen lässt, muss sie und seine Zugänge trotzdem selbst angemessen absichern. Cloud-Sicherheit funktioniert nach demselben Prinzip: Der Anbieter sichert die Hülle, der Mieter sichert seinen Inhalt.

### 1.1 Das Shared-Responsibility-Modell

Sicherheit in der Cloud ist **immer** eine geteilte Aufgabe zwischen Anbieter und Kunde – wie genau die Aufgaben verteilt sind, hängt vom Dienstmodell ab:

| Dienstmodell | Anbieter verantwortet typischerweise | Kunde verantwortet typischerweise | IHK-Relevanz |
| --- | --- | --- | --- |
| **IaaS** | Rechenzentrum, Hardware, physisches Netzwerk, Hypervisor | Gastbetriebssystem, virtuelle Netzwerkkonfiguration (Routing, Firewallregeln), Anwendungen, Identitäten, Zugriffsregeln, Daten und Nutzung der Verschlüsselungsfunktionen | 🔴 |
| **PaaS** | Zusätzlich Gastbetriebssystem, Middleware, Laufzeitumgebung | Eigene Anwendung, Anwendungskonfiguration, Identitäten, Zugriffsrechte, verarbeitete Daten | 🔴 |
| **SaaS** | Betrieb und Absicherung der bereitgestellten Anwendung und Infrastruktur | Benutzerkonten, Rollen, Freigaben, sichere Nutzung, Klassifizierung und rechtmäßige Verarbeitung der eingegebenen Daten | 🔴 |

> Das Wort "typischerweise" ist wichtig: Die konkrete Aufgabenverteilung hängt zusätzlich vom jeweiligen Produkt, Vertrag und Funktionsumfang ab. Auch Verschlüsselung ist kein reines "Kunde macht alles"-Thema: Der Anbieter stellt und betreibt die technischen Verschlüsselungsfunktionen, der Kunde verantwortet insbesondere deren Auswahl, Konfiguration und Schlüsselverwaltung (siehe Deep-Dive CMK/PMK/BYOK).

> **Die goldene Regel:** Unabhängig vom Dienstmodell behält der Kunde Verantwortung für den angemessenen Umgang mit seinen Daten, für seine Identitäten und für die von ihm konfigurierbaren Zugriffsrechte – welche technischen Sicherheitskontrollen der Anbieter darüber hinaus übernimmt, hängt vom konkreten Cloud-Dienst ab. Fehlkonfigurationen, kompromittierte Zugangsdaten und zu weitreichende Berechtigungen auf Kundenseite gehören zu den häufigsten und typischsten Ursachen von Cloud-Sicherheitsvorfällen – klassisches Beispiel: ein öffentlich lesbarer Cloud-Speicher ("offener S3-Bucket"), bei dem sensible Daten ohne Zugriffsbeschränkung im Internet einsehbar sind.

### 1.2 IAM und Security Groups

- **Identity & Access Management (IAM):** Zentrale Verwaltung von Nutzerkonten, Rollen und Berechtigungen – Zugriff sollte grundsätzlich nach dem **Least-Privilege-Prinzip** und mit **MFA** abgesichert sein.
- **Security Groups (virtuelle Firewalls):** Zustandsbehaftete Firewalls, die den Netzwerkverkehr zu/von Cloud-Ressourcen über explizite Freigaberegeln (Protokoll, Port, Quell-IP-Bereich) steuern. Die genaue Standardkonfiguration ist plattformabhängig – bei AWS haben neu angelegte Security Groups zunächst z. B. keine eingehenden Regeln, während ausgehender Verkehr standardmäßig erlaubt ist. Für eine konsequente Least-Privilege-Konfiguration müssen deshalb **sowohl eingehende als auch ausgehende** Regeln geprüft und auf das erforderliche Maß begrenzt werden.

> **IHK-Typfrage:** *"Warum ist es problematisch, wenn ein Unternehmen ausschließlich auf die Sicherheitsversprechen des Cloud-Anbieters vertraut und keine eigenen IAM-/Security-Group-Konfigurationen prüft?"*
> **Musterantwort:** Das Shared-Responsibility-Modell überträgt dem Kunden – unabhängig vom Dienstmodell – die Verantwortung für Daten, Zugangsdaten und die von ihm konfigurierbaren Zugriffsrechte. Der Anbieter stellt zwar Sicherheitsfunktionen, Warnungen und teilweise automatische Schutzmechanismen bereit, kann aber nicht garantieren, dass jede kundenseitige IAM- oder Netzwerkkonfiguration fachlich korrekt und dem Schutzbedarf angemessen ist. Ein alleiniges Vertrauen auf den Anbieter ignoriert damit genau den Teil der Verantwortung, den der Kunde tatsächlich trägt – Fehlkonfigurationen auf Kundenseite gehören zu den häufigsten und typischsten Ursachen realer Cloud-Sicherheitsvorfälle, nicht Einbrüche beim Anbieter selbst.

---

## 2. Containerisierung und Orchestrierung

> **Grundprinzip:** Ein Frachtcontainer transportiert seinen Inhalt unabhängig davon, ob er auf einem Schiff, einem Zug oder einem Lkw steht – die Umgebung außen herum ändert sich, der Inhalt bleibt isoliert und funktionsfähig. Software-Container funktionieren nach demselben Prinzip.

### 2.1 Container vs. virtuelle Maschinen

| Merkmal | Virtuelle Maschine | Container |
| --- | --- | --- |
| Isolationsebene | Eigenes Betriebssystem pro VM (Hypervisor-Ebene) | Teilt sich den Kernel des Host-Betriebssystems |
| Ressourcenbedarf | Höher (vollständiges Gast-OS) | Niedriger (nur Anwendung + Abhängigkeiten) |
| Startzeit | In der Regel langsamer, da ein Gastbetriebssystem gestartet wird | In der Regel schneller, da kein vollständiges Gastbetriebssystem startet |
| Typisches Werkzeug | VMware, Hyper-V | Docker |

> **Sicherheitsimplikation des geteilten Kernels:** Weil Container sich den Host-Kernel teilen, ist die Isolation grundsätzlich anders (tendenziell schwächer) als bei vollständig getrennten VMs. Ein **Container-Escape** (Ausbruch aus der Container-Isolation, z. B. durch eine Kernel-Schwachstelle) kann potenziell den Host und damit alle darauf laufenden Container gefährden. Das bedeutet nicht, dass Container grundsätzlich unsicher sind – es erklärt aber, warum zusätzliche Härtungsmaßnahmen (siehe unten) nötig sind.

### 2.2 Orchestrierung

Sobald viele Container in einer verteilten, skalierenden Cloud-Landschaft laufen, wird die manuelle Verwaltung unpraktikabel. **Orchestrierungsplattformen** wie **Kubernetes** übernehmen automatisiert:

- **Deployment:** Container an die richtigen Stellen im Cluster verteilen
- **Skalierung:** Bei Lastspitzen automatisch weitere Container-Instanzen starten
- **Selbstheilung:** Abgestürzte Container automatisch neu starten

Für Lern- und Testzwecke lässt sich mit **Minikube** lokal ein Kubernetes-Cluster betreiben – Minikube ist kein eigenständiges, konkurrierendes Orchestrierungssystem, sondern ein Werkzeug für eine lokale Kubernetes-Umgebung.

**Sicherheitsrelevant** ist auch die Orchestrierungsebene selbst: Wer die Steuerungsebene (z. B. die Kubernetes-API) kontrolliert, kann Deployments verändern, Secrets auslesen und potenziell große Teile des Clusters beeinflussen. Zusätzliche typische Risikofelder:

- **Image-Sicherheit:** Nur vertrauenswürdige, regelmäßig geprüfte Images verwenden; bekannte Schwachstellen per Image-Scanning erkennen.
- **Secret Management:** Passwörter, Tokens und API-Schlüssel nicht fest in Images oder Deployment-Dateien speichern.
- **Runtime-Härtung:** Container möglichst ohne Root-Rechte und mit eingeschränkten Betriebssystemfähigkeiten betreiben.

---

## 3. Zero-Trust-Architektur

> **Grundprinzip:** Eine Burg mit Burggraben schützt nur so lange, wie niemand die Zugbrücke überwindet – ist ein Angreifer erst einmal drin, kann er sich ohne zusätzliche interne Kontrollen innerhalb der Mauern weiterbewegen. Zero Trust ergänzt die eine große Zugbrücke um einen Kontrollpunkt vor jeder einzelnen Tür im Gebäude.

### 3.1 Vom Perimeterschutz zu Zero Trust

Das klassische **"Castle-and-Moat"-Modell** (Burg-und-Burggraben) vertraut implizit allem, was sich innerhalb der Netzwerkgrenze befindet – wer per VPN eingewählt oder im Büro-LAN ist, gilt automatisch als vertrauenswürdig. Als alleinige Sicherheitsstrategie reicht das nicht mehr aus:

1. Ein Angreifer, der einmal ins interne Netz gelangt (z. B. per Phishing), kann sich je nach interner Segmentierung und Zugriffskontrolle lateral ausbreiten.
2. Cloud-Dienste, Homeoffice und BYOD bedeuten, dass es nicht mehr nur eine klar abgegrenzte, zentrale Netzwerkzone gibt – Zugriffe erfolgen über viele Geräte, Standorte und Dienste, sodass der Netzwerkstandort allein kein ausreichendes Vertrauenssignal mehr darstellt.

```text
Klassisch:   [ Externes Netz ] --( Firewall/VPN )--> [ Internes Netz (implizit vertraut, freie Bewegung) ]

Zero Trust:  [ Zugriff von überall ] --> [ Explizite Prüfung: Identität, Gerät, Kontext ] --> [ Nur die eine angefragte Ressource ]
```

Zero Trust ersetzt dabei vor allem das **implizite Vertrauen aufgrund des Netzwerkstandorts** – klassische Perimeter-Elemente wie Firewalls, VPN-Gateways und Netzwerksegmentierung bleiben auch in einer Zero-Trust-Architektur relevant, werden aber um explizite, kontextbezogene Prüfung ergänzt statt allein als Vertrauensgrenze zu dienen.

### 3.2 Die drei Kernprinzipien

In der Praxis werden Zero-Trust-Konzepte häufig durch drei Leitprinzipien zusammengefasst, die insbesondere durch Microsoft in dieser Dreiteilung verbreitet wurden (NIST SP 800-207 selbst benennt sie nicht in exakt dieser Form):

| Prinzip | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Verify Explicitly** (Explizit überprüfen) | Jeder Zugriff wird anhand aller verfügbaren Signale geprüft – Identität, Gerätestatus, Standort, Datenklassifizierung, Anomalien | 🔴 |
| **Least Privilege Access** (Minimale Rechte) | Zugriff zeitlich begrenzt (Just-in-Time) und auf das zwingend Nötige beschränkt (Just-Enough-Access) | 🔴 |
| **Assume Breach** (Von Kompromittierung ausgehen) | Es wird angenommen, dass Angreifer bereits im System sind – Mikrosegmentierung, Ende-zu-Ende-Verschlüsselung, kontinuierliches Monitoring begrenzen den möglichen Schaden | 🔴 |

### 3.3 Referenzarchitektur nach NIST SP 800-207

Das NIST-Referenzmodell strukturiert eine Zero-Trust-Architektur in logische Kontrollkomponenten:

| Komponente | Rolle | IHK-Relevanz |
| --- | --- | --- |
| **Policy Engine (PE)** | Bewertet Zugriffsanfragen anhand von Richtlinien und Kontextinformationen und trifft die Entscheidung: erlauben, verweigern oder widerrufen | 🟡 |
| **Policy Administrator (PA)** | Führt die Entscheidung der Policy Engine aus und weist den PEP an, einen Kommunikationspfad einzurichten oder zu beenden | 🟡 |
| **Policy Decision Point (PDP)** | Logische Einheit aus Policy Engine und Policy Administrator – "Gehirn" der Architektur | 🟡 |
| **Policy Enforcement Point (PEP)** | Kontrolliert die Verbindung zwischen Subjekt und Ressource und setzt die Entscheidung des PDP technisch durch | 🔴 |

### 3.4 Die fünf Säulen nach dem CISA Zero Trust Maturity Model

Über die drei Kernprinzipien hinaus gliedert das **CISA Zero Trust Maturity Model** (aktuell Version 2.0, April 2023) – nicht NIST SP 800-207 selbst – die praktische Umsetzung in fünf Säulen:

| Säule | Typische Maßnahmen | IHK-Relevanz |
| --- | --- | --- |
| **Identitäten** | Zentrales IAM, durchgängige/adaptive MFA, attributbasierte Autorisierung (ABAC) | 🔴 |
| **(End-)Geräte** | Lückenloses Assetmanagement, Echtzeit-Compliance-Prüfung (OS-Patch-Stand, Antivirus-Status), Endpoint Protection/EDR | 🔴 |
| **Netzwerke** | Mikrosegmentierung, durchgehende Verschlüsselung, automatische Anomalie-Erkennung gegen laterale Bewegung | 🔴 |
| **Anwendungen und Workloads** | Container-Kapselung/Sandboxing, starke Dienst-zu-Dienst-Authentifizierung, DevSecOps-Integration (SAST/DAST) | 🟡 |
| **Daten** | Zentrale Klassifizierung nach Schutzbedarf, Ende-zu-Ende-Verschlüsselung, Data Loss Prevention (DLP) | 🔴 |

> Ergänzend zu den fünf Säulen definiert das CISA-Modell drei Querschnittsfähigkeiten, die über alle Säulen hinweg wirken: **Sichtbarkeit und Analyse**, **Automatisierung und Orchestrierung** sowie **Governance**.

> **IHK-Typfrage:** *"Ein Mitarbeiter meldet sich mit korrekten Zugangsdaten von einem unbekannten, nicht als firmeneigen registrierten Gerät aus dem Ausland an, um auf einen sensiblen Kundendaten-Server zuzugreifen. Wie würde eine Zero-Trust-Architektur reagieren, und warum reicht die korrekte Passworteingabe allein nicht aus?"*
> **Musterantwort:** Nach dem Prinzip "Verify Explicitly" bewertet die Policy Engine nicht nur die Anmeldedaten, sondern zusätzliche Kontextsignale wie Gerätestatus (nicht registriert), Standort (ungewöhnlich) und Ressourcen-Sensibilität. Ein korrektes Passwort belegt lediglich, dass der Anfragende über das Passwort verfügt – nicht zuverlässig, dass es sich tatsächlich um den berechtigten Nutzer handelt, da Passwörter gestohlen oder weitergegeben worden sein können. Je nach Risikoeinstufung könnte die Policy den Zugriff verweigern, bis ein verwaltetes und richtlinienkonformes Gerät verwendet wird, eine zusätzliche (idealerweise phishingresistente) MFA verlangen oder den Zugriff auf eingeschränkte Funktionen begrenzen. Das Least-Privilege-Prinzip sorgt zusätzlich dafür, dass selbst bei erfolgreicher Anmeldung nur der zwingend nötige Ausschnitt der Daten zugänglich wäre.

### 3.5 Regulatorische Treiber

Zero Trust ist nicht nur eine technische Empfehlung, sondern wird zunehmend regulatorisch gefordert bzw. nahegelegt:

- **NIS2 und deutsches BSIG:** Das am 6. Dezember 2025 in Kraft getretene BSIG (siehe LF4.1) verlangt in § 30 Abs. 2 unter den Risikomanagementmaßnahmen unter anderem Konzepte für Zugriffskontrollen sowie den Einsatz von Lösungen zur **Multi-Faktor-Authentifizierung oder kontinuierlichen Authentifizierung** – das überschneidet sich inhaltlich mit Zero-Trust-Prinzipien. Das Gesetz schreibt aber weder eine vollständige Zero-Trust-Architektur noch die Verwendung des Begriffs "Zero Trust" wörtlich vor.
- **Reifegradmodelle als Umsetzungshilfe:** Zero Trust ist kein einzelnes Produkt, sondern ein langfristiger Transformationsprozess. Modulare Reifegradmodelle wie das **CISA Zero Trust Maturity Model** unterstützen eine schrittweise, nachvollziehbare Umsetzung statt eines "Alles-oder-nichts"-Ansatzes.

---

## 4. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Der Cloud-Anbieter ist für die gesamte Sicherheit verantwortlich, unabhängig vom Dienstmodell | Der Kunde behält bei jedem Modell (IaaS/PaaS/SaaS) Verantwortung für den angemessenen Umgang mit seinen Daten, für seine Identitäten und für die von ihm konfigurierbaren Zugriffsrechte – der Umfang der übrigen technischen Aufgaben variiert je nach Dienst |
| 2 | Cloud-Sicherheitsvorfälle entstehen meist durch Angriffe auf den Anbieter | Fehlkonfigurationen auf Kundenseite (z. B. offene S3-Buckets) gehören zu den häufigsten Ursachen – nicht primär Einbrüche beim Anbieter |
| 3 | Container sind einfach "kleine virtuelle Maschinen" | Container teilen sich den Kernel des Host-Systems, VMs haben ein eigenes Gast-Betriebssystem – unterschiedliche Isolationsebene |
| 4 | Zero Trust bedeutet, niemandem mehr Zugriff zu gewähren | Zero Trust bedeutet, jeden Zugriff explizit und kontinuierlich zu prüfen statt implizit zu vertrauen – berechtigte Zugriffe werden weiterhin gewährt |
| 5 | Ein korrektes Passwort genügt in einer Zero-Trust-Architektur als Vertrauensnachweis | Zero Trust bewertet zusätzlich Kontextsignale (Gerät, Standort, Verhalten) – Passwortkenntnis allein ersetzt das nicht |
| 6 | Zero Trust ist ein einzelnes Produkt, das man einfach kauft und installiert | Zero Trust ist ein langfristiger organisatorischer und technischer Transformationsprozess, idealerweise über Reifegradmodelle schrittweise umgesetzt |

---

## 5. Deep-Dive-Ausblick (freiwillig)

- **Cloud-Verschlüsselungskonzepte** (→ Abschnitt 1): Unterschiede zwischen Customer-Managed Keys (CMK), Provider-Managed Keys (PMK) und Bring Your Own Key (BYOK).
- **Secret Management** (→ Abschnitt 1): Wie Cloud-Secret-Manager verhindern, dass API-Schlüssel und Zugangsdaten versehentlich im Quellcode landen.
- **Mikrosegmentierung vs. klassische VLANs** (→ Abschnitt 3.4): Warum Mikrosegmentierung auf Anwendungsebene granularer arbeitet als traditionelle Netzwerksegmentierung.
- **Just-in-Time-Berechtigungen** (→ Abschnitt 3.2): Wie zeitlich befristete, automatisiert freigegebene Admin-Rechte das Risiko dauerhaft bestehender privilegierter Konten reduzieren.
- **CISA Zero Trust Maturity Model im Detail** (→ Abschnitt 3.4): Die Reifegradstufen von "Traditional" bis "Optimal" über die fünf Säulen hinweg.

---

## 6. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Wer ist bei SaaS für die Absicherung der eigenen Zugangsdaten verantwortlich? | Immer der Kunde – unabhängig vom Dienstmodell |
| 2 | Was ist ein "offener S3-Bucket", und welches Schutzziel verletzt er primär? | Ein öffentlich lesbarer Cloud-Speicher ohne Zugriffsbeschränkung – verletzt primär die Vertraulichkeit |
| 3 | Warum müssen bei Security Groups sowohl eingehende als auch ausgehende Regeln geprüft werden? | Weil eingehender Verkehr häufig zunächst gesperrt ist, ausgehender Verkehr aber je nach Plattform/Standardkonfiguration bereits erlaubt sein kann |
| 4 | Was ist der zentrale Unterschied zwischen Container und virtueller Maschine? | Container teilen sich den Host-Kernel, VMs haben ein eigenes Gast-Betriebssystem |
| 5 | Nenne die drei Kernprinzipien von Zero Trust. | Verify Explicitly, Least Privilege Access, Assume Breach |
| 6 | Was ist die Aufgabe des Policy Enforcement Point (PEP)? | Ermöglicht, überwacht und beendet die Verbindung zwischen Subjekt und Ressource entsprechend der Entscheidung des PDP |
| 7 | Nenne die fünf Säulen des CISA Zero Trust Maturity Models. | Identitäten, Geräte, Netzwerke, Anwendungen und Workloads, Daten |
| 8 | Warum reicht das Castle-and-Moat-Modell bei Homeoffice und Cloud-Diensten allein nicht mehr aus? | Zugriffe erfolgen über viele Standorte, Geräte und Cloud-Dienste – eine interne Netzwerkposition allein ist deshalb kein ausreichendes Vertrauenssignal mehr |
| 9 | Was ist der Zweck eines Zero-Trust-Reifegradmodells (z. B. CISA)? | Schrittweise, nachvollziehbare Umsetzung von Zero Trust statt eines abrupten Komplettwechsels |

---

## 7. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Shared Responsibility** | Geteilte Sicherheitsverantwortung; genaue Aufteilung hängt vom Dienst ab – Kunde bleibt insbesondere für Identitäten, Datenverwendung und konfigurierbare Zugriffe verantwortlich |
| **IAM** | Identity & Access Management – zentrale Verwaltung von Nutzerkonten und Berechtigungen |
| **Security Group** | Zustandsbehaftete virtuelle Firewall mit expliziten Freigaberegeln; Standardkonfiguration (v. a. ausgehender Verkehr) ist plattformabhängig |
| **Container** | Isolierte Ausführungsumgebung, teilt sich den Host-Kernel (im Unterschied zur VM) |
| **Orchestrierung** | Automatisiertes Deployment/Skalierung/Selbstheilung von Containern (z. B. Kubernetes) |
| **Minikube** | Werkzeug für eine lokale Kubernetes-Umgebung zu Lern-/Testzwecken – kein eigenes, konkurrierendes Orchestrierungssystem |
| **Castle-and-Moat** | Klassisches Perimeter-Sicherheitsmodell mit implizitem Innen-Vertrauen |
| **Zero Trust** | "Never trust, always verify" – jeder Zugriff wird explizit geprüft, unabhängig vom Ursprung |
| **PE / PA / PDP / PEP** | Policy Engine (trifft Entscheidung) + Policy Administrator (führt sie aus) = Policy Decision Point (PDP); Policy Enforcement Point (PEP) setzt sie an der Ressource durch – nach NIST SP 800-207. **Achtung:** "PAP" ist **kein** NIST-Begriff (stammt aus XACML) |
| **Mikrosegmentierung** | Feingranulare Netzwerksegmentierung auf Anwendungs-/Workload-Ebene |
| **JIT / JEA** | Just-in-Time / Just-Enough-Access – zeitlich und funktional minimierte Zugriffsrechte |
| **Authentisierung vs. Autorisierung** | Authentisierung = Nachweis einer behaupteten Identität; Autorisierung = Entscheidung, worauf zugegriffen werden darf – zwei getrennte Schritte |
| **Container-Escape** | Ausbruch aus der Container-Isolation (z. B. über eine Kernel-Schwachstelle) – gefährdet potenziell den Host und alle anderen Container |

---

## 8. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Shared-Responsibility-Zuordnung | "Wer ist für X bei PaaS verantwortlich?" | Konkrete Zuordnung Anbieter/Kunde je nach Dienstmodell, nicht pauschal "beide" |
| Architekturvergleich | "Vergleichen Sie Castle-and-Moat mit Zero Trust" | Konkreten Schwachpunkt des alten Modells benennen (laterale Ausbreitung), nicht nur "Zero Trust ist moderner" |
| Zero-Trust-Anwendung | "Entwerfen Sie eine Zero-Trust-Zugriffsregel für Szenario X" | Konkrete Kontextfaktoren (Gerät, Standort, Zeit, Rolle) nennen, alle drei Kernprinzipien einbeziehen |
| Container-Sicherheit | "Welche Sicherheitsrisiken entstehen beim Betrieb einer Container-Plattform?" | Gemeinsam genutzter Host-Kernel, unsichere Images, zu weitreichende Container-Rechte, ungeschützte Secrets nennen |
| Orchestrierung | "Warum muss die Kubernetes-Steuerungsebene besonders geschützt werden?" | Wer die Steuerungsebene kontrolliert, kann Deployments verändern, Secrets auslesen und große Teile des Clusters beeinflussen |

---

## 9. Merksätze für das Fachgespräch

> Geteilte Verantwortung heißt nicht halbe Verantwortung – auch bei SaaS bleiben Identitäten, Freigaben und der angemessene Umgang mit den eigenen Daten Aufgaben des Kunden.

> Ein Container ist kein kleiner Bruder der VM, sondern ein anderes Isolationsprinzip – geteilter Kernel statt eigenem Betriebssystem.

> "Never trust, always verify" heißt nicht Misstrauen gegenüber jedem Menschen, sondern die Abschaffung des blinden Vertrauens gegenüber dem Netzwerkstandort.

> Zero Trust hat einen Kontrollpunkt vor jeder Tür, nicht nur einen großen Zaun ums Grundstück – laterale Ausbreitung wird dadurch erschwert und begrenzt, weil der interne Netzwerkstandort allein nicht mehr als Vertrauensnachweis genügt.

> Zero Trust ist eine Reise, kein Produkt – Reifegradmodelle machen aus dem großen Sprung viele kleine, nachvollziehbare Schritte.

---

```yaml
dokument: LF4.3A-wiki-artikel
lernfeld: LF4.3
teil: "1 von 2 – Cloud Security & Zero Trust (Teil B: Security Awareness, Supply-Chain, KI-Bedrohungen, OWASP LLM Top 10)"
titel: "Cloud Security & Zero Trust"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-09
quellen_intern:
  - "LF4.3.1: Cloud Security & Shared-Responsibility.md"
  - "LF4.3.2: Zero-Trust-Architektur - Vertraue niemandem.md"
  - "Ergänzendes Material: NotebookLM-Zusammenfassung aus 'IT-Handbuch für Fachinformatiker – Der Ausbildungsbegleiter' (Sascha Kersken, Rheinwerk Verlag): 5 Säulen der Zero-Trust-Architektur (CISA-Modell), Containerisierung/Orchestrierung, regulatorische Treiber (NIS2, Reifegradmodelle) – NIST-Komponentenbezeichnung PE/PA/PDP/PEP wurde gegen die offizielle NIST-SP-800-207-Terminologie korrigiert (Quellmaterial nannte fälschlich 'PAP')"
quellen_fachlich:
  - titel: "NIST SP 800-207 (Zero Trust Architecture)"
    herausgeber: "NIST"
    status: "seit 2020 veröffentlicht, weiterhin die maßgebliche Referenzarchitektur für Zero Trust"
  - titel: "CISA Zero Trust Maturity Model, Version 2.0"
    herausgeber: "Cybersecurity and Infrastructure Security Agency (CISA)"
    status: "veröffentlicht April 2023; am 2026-09-09 als aktuelle offizielle Version geprüft und im Fließtext (Abschnitt 3.4) entsprechend zitiert"
  - titel: "BSI-Gesetz (BSIG), insbesondere § 30 Abs. 2"
    herausgeber: "Bundesministerium der Justiz / Bundesamt für Justiz"
    status: "geltendes BSIG (Ausfertigung 2.12.2025, in Kraft seit 6.12.2025); § 30 Abs. 2 Nr. 9/10 nennt Konzepte für Zugriffskontrolle sowie MFA/kontinuierliche Authentifizierung – am 2026-09-09 geprüft, siehe auch LF4.1"
review_historie:
  - runde: 1
    datum: 2026-09-09
    ergebnis: "Erstdraft erstellt, kombiniert Rohmaterial (LF4.3.1, LF4.3.2) mit vom Nutzer bereitgestellter NotebookLM-Zusammenfassung aus dem Kersken-Handbuch (NIST-SP-800-207-Komponenten, 5 Säulen, Container/Orchestrierung, regulatorische Treiber). Artikel aufgrund absehbarer Länge (6 Unterthemen in LF4.3 insgesamt) direkt in Teil A/B aufgeteilt, wie bei LF4.2 etabliert. Eigene Review nach Style-Guide-Checkliste direkt eingearbeitet: Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an vorhanden, Analogien aus mehreren Domänen (Werkshalle/Vermietung, Frachtcontainer, Burg/Kontrollpunkt)."
  - runde: 2
    datum: 2026-09-09
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet. Wichtigster Fund, von zwei Reviews unabhängig mit NIST-SP-800-207-PDF-Zitat bestätigt: 'Policy Administration Point (PAP)' ist keine echte NIST-Komponente (stammt aus XACML) – korrigiert auf die tatsächliche NIST-Terminologie Policy Engine (PE) + Policy Administrator (PA) = PDP, plus PEP. Zweiter wichtiger Fund: Die 'fünf Säulen' stammen aus dem CISA Zero Trust Maturity Model, nicht aus NIST SP 800-207 selbst – Kernfrage 4, Abschnittsüberschrift 3.4 und Einleitung entsprechend getrennt zugeordnet, CISA-Querschnittsfähigkeiten (Sichtbarkeit/Analyse, Automatisierung/Orchestrierung, Governance) ergänzt, Säule 'Anwendungen' auf offizielle Bezeichnung 'Anwendungen und Workloads' korrigiert. Die drei Kernprinzipien (Verify Explicitly/Least Privilege/Assume Breach) als verbreitete Microsoft-Systematik statt offizielle NIST-Benennung gekennzeichnet. Weitere Korrekturen: Sicherheitsimplikation des geteilten Container-Kernels (Container-Escape) ergänzt – von zwei Reviews unabhängig gefordert und mit der bestehenden Prüfungstaktik-Zeile abgeglichen; Minikube korrekt als lokales Kubernetes-Testwerkzeug statt 'kleinere Orchestrierungs-Variante' beschrieben; Image-Sicherheit/Secret-Management/Runtime-Härtung als Orchestrierungsrisiken ergänzt; 'Default Deny' bei Security Groups auf plattformabhängige Realität präzisiert (AWS: ausgehender Verkehr standardmäßig erlaubt); 'häufigste Ursache'/'Anbieter kann nicht korrigieren' entschärft; laterale Bewegung als 'erschwert/begrenzt' statt 'verhindert' dargestellt; NIS2/BSIG-Aussage auf die konkrete gesetzliche Formulierung (MFA oder kontinuierliche Authentifizierung) präzisiert, unbelegte 'BSI-Orientierungshilfen'-Erwähnung entfernt. Redaktionell: trailing pipe in VM/Container-Tabelle behoben, 'haftet' (juristisch aufgeladen) und 'Außen (Böse)' neutraler formuliert. Umfangreiche Scope-Erweiterungsvorschläge einer Review (AWS/Azure/GCP-Tabellen, zusätzliche Labs, Diskussionsfragen) bewusst nicht übernommen."
  - runde: 3
    datum: 2026-09-09
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet. Von zwei Reviews unabhängig bestätigt: YAML-CISA-Quellenangabe widersprach dem im Fließtext bereits verifizierten Stand ('Version 2.0, April 2023') – synchronisiert; Selbsttest 7 fragte generisch nach 'fünf Säulen einer Zero-Trust-Architektur' statt konsistent nach dem CISA-Modell, wie in 3.4 sauber eingeführt – korrigiert, inkl. korrekter Bezeichnung 'Anwendungen und Workloads'. Weitere Präzisierungen (eine Review, mit AWS-Doku-Zitat): Shared-Responsibility-Tabelle differenziert ('typischerweise' statt fixer Zuordnung, IaaS-Netz-Zeile auf virtuelle Netzwerkkonfiguration statt physisches Netz präzisiert, Verschlüsselung als geteilte statt reine Kundenaufgabe dargestellt); 'Goldene Regel' von 'immer' auf 'behält Verantwortung für...' entschärft, mit Konsistenzfolgen in Prüfungsfalle 1/Cheatsheet/Merksatz; verbliebene kategorische 'häufigste Ursache'-Formulierung in der goldenen Regel selbst nachgezogen; Kernfrage 3 von 'Zero Trust ersetzt Perimeter-Modell' auf 'warum reicht Perimeter-Modell allein nicht mehr aus' präzisiert (Firewalls/VPN-Gateways bleiben relevant, ersetzt wird das implizite Standort-Vertrauen); Burg-Analogie und 3.1-Fließtext entsprechend von 'ungehindert'/'keine feste Netzwerkgrenze' auf differenziertere Formulierungen umgestellt, Selbsttest 8 nachgezogen; BSIG-Quellenangabe um konkrete Fundstelle (§ 30 Abs. 2) ergänzt; Deep-Dive-Verweis auf CISA-Modell von Abschnitt 3.5 auf 3.4 korrigiert; Minikube-Formulierung vereinfacht und ins Cheatsheet aufgenommen; PEP-Selbsttest-Antwort präzisiert. Weitere Scope-Vorschläge (Trivy/Snyk-Tool-Namen, Azure/GCP-Beispiele, zusätzliche Prüfungsfalle, DORA-Erwähnung) als optionale, nicht-blockierende Erweiterungen eingestuft und nicht übernommen."
naechste_review: "Keine harten Fachfehler mehr gefunden – bereit für final nach Bestätigung. Status Final erteilt durch Autor."
```