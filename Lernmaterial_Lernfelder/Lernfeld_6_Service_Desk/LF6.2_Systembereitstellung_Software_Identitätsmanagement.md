# LF6.2 – Systembereitstellung, Software & Identitätsmanagement

*Wie Systeme automatisiert entstehen, sicher aktuell bleiben und wer worauf zugreifen darf*

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** AP1 (schriftlich) + Fachgespräch
> **Lernzeit:** Ca. 45–60 Minuten
> **Status:** Final
> **Stand:** 2026

---

## 📌 IHK-Kernfragen

| # | Frage | Abschnitt |
|---|---|---|
| 1 | Was macht Autoinstall/YAML und wofür wird TPM dabei genutzt? | [1.1 Zero-Touch-Bereitstellung](#11-zero-touch-bereitstellung-mit-autoinstall) |
| 2 | Was ist der Unterschied zwischen Unattended Upgrades und Kernel-Livepatching? | [1.2 Wartung im laufenden Betrieb](#12-wartung-im-laufenden-betrieb) |
| 3 | Wie funktioniert ein Staged Rollout / das Ring-Modell? | [2.1 Staged Rollout](#21-staged-rollout-und-update-ringe) |
| 4 | Was ist RBAC und warum nicht Einzelpersonen berechtigen? | [3. Identität & Zugriff](#3-identitäts--und-zugriffsverwaltung) |
| 5 | Lokale Benutzerverwaltung vs. OpenLDAP vs. Entra ID – wann was? | [3.2 Vergleich der Ansätze](#32-lokal-vs-verzeichnisdienst-vs-cloud) |

---

## 1. Automatisierte Systembereitstellung und Wartung

> Zero-Touch-Provisioning bedeutet: Gerät anschließen, Kaffee holen, fertig konfiguriertes System vorfinden.

### 1.1 Zero-Touch-Bereitstellung mit Autoinstall

Das YAML-basierte Autoinstall-Verfahren (Ubuntu/Subiquity) ersetzt ältere Methoden wie Debian-Preseeding.

| Sektion | Funktion | IHK-Relevanz |
|---|---|---|
| `identity` | Hostname, Benutzer, Passwörter | 🔴 |
| `storage` | Partitionstabelle (GPT), LVM, RAID | 🔴 |
| `network` | DHCP/statische IP, VLAN via Netplan | 🟡 |
| `early-commands` | Skripte **vor** der Installation | 🟡 |
| `late-commands` | Skripte **im Zielsystem** (chroot) am Ende | 🔴 |

Bereitstellung meist über HTTP-Server oder **PXE-Boot** (Preboot Execution Environment).

**Sicherheitsintegration – FDE + TPM:** Der Autoinstall-Prozess automatisiert Full Disk Encryption per LUKS. Der Entschlüsselungsschlüssel wird während der Installation generiert und im **TPM (Trusted Platform Module)** versiegelt. Das ermöglicht unbeaufsichtigten Boot **und** Schutz bei Diebstahl der Festplatte oder Manipulation der Boot-Kette.

> **IHK-Typfrage:** *"Warum reicht ein einfaches LUKS-Passwort nicht für einen unbeaufsichtigten Zero-Touch-Bootvorgang?"*
> **Musterantwort:** Ohne TPM müsste bei jedem Boot manuell ein Passwort eingegeben werden. Das TPM speichert den Schlüssel hardwaregebunden und gibt ihn nur frei, wenn die Boot-Kette (Firmware, Bootloader, Kernel) unverändert ist – so ist der Boot automatisch **und** gegen Manipulation abgesichert.

### 1.2 Wartung im laufenden Betrieb

| Konzept | Erklärung | IHK-Relevanz |
|---|---|---|
| Unattended Upgrades | Automatische Installation von Sicherheitspatches im Hintergrund | 🔴 |
| Kernel-Livepatching | Kritische Kernel-Lücken schließen **ohne Reboot** | 🔴 |
| LTS (Long Term Support) | 5–12+ Jahre Support, Fokus Stabilität | 🟡 |

**Unattended Upgrades – Best Practices:**
- Nur dedizierte Sicherheits-Repositories zulassen
- Blacklist für kritische Pakete (Kernel/Treiber oft ausgeschlossen, da instabilisierend)
- **Jitter** (zufällige Verzögerung) verhindert Lastspitzen in großen Flotten
- Automatische Neustarts nur außerhalb der Geschäftszeiten, wenn kein Nutzer angemeldet ist

**Kernel-Livepatching – Funktionsweise:**
1. Sicherheitslücke (CVE) wird identifiziert
2. Minimales Patch-Modul mit der korrigierten Funktion wird kompiliert
3. Modul wird in den Arbeitsspeicher geladen, `ftrace` leitet den fehlerhaften Funktionsaufruf auf die neue Funktion um
4. Läuft in Millisekunden, transparent für laufende Prozesse

Wichtig: Livepatches sind **kumulativ** – das neueste Modul enthält alle vorherigen Fixes. So lassen sich Neustarts bis zum nächsten Wartungsfenster verschieben, ohne ungeschützt zu sein.

> **IHK-Typfrage:** *"Ein kritischer Kernel-Patch muss sofort eingespielt werden, ein Reboot des Produktionsservers ist aber erst in 3 Wochen möglich. Welche Technik nutzt du?"*
> **Musterantwort:** Kernel-Livepatching (z. B. Canonical Livepatch, kpatch) – schließt die Lücke sofort im laufenden Betrieb über ftrace-Umleitung, ohne dass ein Neustart nötig ist.

### 1.3 Qualitätssicherung vor dem Rollout

Vor dem Ausrollen auf produktive Systeme: Tests in **virtuellen Maschinen** (Staging-Umgebung), oft mit Frameworks wie openQA oder autopkgtest, orchestriert über CI/CD (Jenkins, GitLab).

**Ablauf:** Snapshot der VM → Patch anwenden → automatisierte Funktionsprüfung kritischer Dienste → Health-Check → Freigabe für nächste Rollout-Phase.

---

## 2. Software-Verteilung und SaaS-Management

> Software wird nicht an alle gleichzeitig verteilt – sie wandert in Ringen von wenigen zu vielen.

### 2.1 Staged Rollout und Update-Ringe

| Ring | Zielgruppe | Umfang | Zweck | IHK-Relevanz |
|---|---|---|---|---|
| Test/Pilot Ring | IT-Team, Freiwillige | < 1–10 % | Technische Integrität prüfen | 🔴 |
| Fast Ring | Nicht-kritische Abteilungen | 20–30 % | Skalierbarkeit validieren | 🟡 |
| Broad Ring | Gesamte Organisation | Rest | Finaler Rollout | 🔴 |

**Ubuntus Phased Updates** (Praxisbeispiel): Ein Update wird zunächst nur einem kleinen Prozentsatz angeboten. Ohne Fehlerberichte steigt die Verfügbarkeit alle 6 Stunden um 10 %, bis nach ~2 Tagen 100 % erreicht sind. Bei gemeldeten Problemen wird das Phasing sofort auf 0 % gesetzt – weltweiter Stopp, bevor die Mehrheit betroffen ist.

> Ein Staged Rollout schützt die **Verfügbarkeit** – eines der höchsten Schutzziele der Informationssicherheit.

### 2.2 SaaS-Provisionierung und zentrale Verwaltung

| Konzept | Erklärung | IHK-Relevanz |
|---|---|---|
| SaaS-Provisionierung | Nutzer Zugang zu Web-App geben (z. B. M365, Slack) | 🟡 |
| SSO (Single Sign-On) | Ein Login für Windows + alle SaaS-Apps (z. B. via Entra ID) | 🔴 |
| RBAC | Rechte werden Rollen/Gruppen zugewiesen, nicht Einzelpersonen | 🔴 |
| Least Privilege | Jede Gruppe erhält nur die Rechte, die sie tatsächlich braucht | 🔴 |

**Enterprise-Plattformen (Beispiel Matrix42):** Vereinen ITSM, Unified Endpoint Management (UEM) und Software Asset Management (SAM) in einer Plattform. Praxisbeispiele:
- **Zero-Touch-Onboarding:** Neues Gerät registriert sich selbst, Rolle bestimmt automatisch installierte Software + Lizenzzuordnung
- **Lizenz-Re-Harvesting:** Ungenutzte Lizenz (z. B. 90 Tage keine Nutzung) wird automatisch zurückgeholt und dem Lizenzpool zugeführt
- **Automatische Isolation:** Bei Malware-Meldung wird das Gerät per UEM vom Netz isoliert und ein Incident-Ticket erstellt

> **IHK-Typfrage:** *"Warum wird Software-Zugriff über Gruppen statt über einzelne Nutzerkonten vergeben?"*
> **Musterantwort:** RBAC mit Least Privilege – Rechte an Rollen (z. B. "HR_Personal") zu binden statt an Personen macht Berechtigungen nachvollziehbar, skalierbar und einfach zu entziehen (Mitarbeiter verlässt Rolle → verliert automatisch Zugriff, kein manuelles Aufräumen nötig).

---

## 3. Identitäts- und Zugriffsverwaltung

> Ob lokal, per Verzeichnisdienst oder in der Cloud – die Frage bleibt dieselbe: Wer darf was, und wie zentral verwaltest du das?

### 3.1 Lokale Rechteverwaltung unter Linux

Klassisches Beispiel aus der Praxis – zwei Gruppen, ein gemeinsamer Ordner:

```bash
sudo groupadd vertrieb
sudo groupadd technik
sudo useradd -m -G technik tim
sudo mkdir /lagerhaus
sudo chgrp technik /lagerhaus
sudo chmod 770 /lagerhaus
```

**`770` entschlüsselt:**

| Stelle | Wert | Bedeutung |
|---|---|---|
| Besitzer | `7` (rwx) | Voller Zugriff |
| Gruppe (`technik`) | `7` (rwx) | Voller Zugriff |
| Andere | `0` (---) | Kein Zugriff |

Ergebnis: `drwxrwx--- 2 root technik /lagerhaus` – ein Nutzer aus `vertrieb` hat hier **keinen** Zugriff.

### 3.2 Lokal vs. Verzeichnisdienst vs. Cloud

| Merkmal | Lokale Verwaltung | OpenLDAP | Entra ID (Cloud) | IHK-Relevanz |
|---|---|---|---|---|
| Einsatzort | Einzelne PCs, kleine Teams | Große lokale Firmennetze | Moderne Unternehmen, Cloud-Apps | 🔴 |
| Vorteil | Einfach, funktioniert offline | Volle Datenkontrolle, Open Source | Zugriff von überall, kein eigener Server, MFA | 🔴 |
| Nachteil | Kein zentrales Passwort-Management | Komplexe Einrichtung, eigene Hardware | Laufende Kosten, Internetabhängigkeit | 🟡 |
| Skalierbarkeit | Sehr schlecht | Sehr gut (lokal) | Exzellent (global) | 🟡 |

**Der entscheidende Denksprung:** Lokal = Nutzer existiert nur auf einem Gerät. Zentral (LDAP/AD/Entra ID) = Nutzer existiert im Netzwerk und kann sich an jedem angeschlossenen Gerät anmelden – die Grundlage für SSO.

> **IHK-Typfrage:** *"Ein Unternehmen mit 300 Mitarbeitern verwaltet Zugänge noch lokal auf jedem PC. Was schlägst du vor und warum?"*
> **Musterantwort:** Umstieg auf einen zentralen Verzeichnisdienst (OpenLDAP oder Entra ID, je nach On-Premises/Cloud-Strategie). Vorteil: zentrale Passwortänderung, ein Login für alle Geräte/Apps (SSO), Rechte per RBAC statt manuell pro PC – bei 300 Nutzern ist lokale Verwaltung nicht mehr skalierbar.

---

## ✅ Selbsttest

| Frage | Kurzantwort |
|---|---|
| 1. Wofür wird das TPM beim Autoinstall-Prozess genutzt? | Sichere Versiegelung des LUKS-Entschlüsselungsschlüssels für unbeaufsichtigten, aber geschützten Boot |
| 2. Was ist der Vorteil von Kernel-Livepatching gegenüber normalen Updates? | Schließt Sicherheitslücken ohne Reboot – kein Ausfall laufender Prozesse |
| 3. Was passiert bei Ubuntus Phased Updates, wenn Fehler gemeldet werden? | Phasing wird sofort auf 0 % gesetzt, Rollout weltweit gestoppt |
| 4. Was bedeutet Least Privilege im Kontext von RBAC? | Jede Rolle/Gruppe erhält nur die Rechte, die für ihre Aufgabe nötig sind – nicht mehr |
| 5. Warum ist lokale Benutzerverwaltung bei vielen Geräten problematisch? | Keine zentrale Passwortänderung, kein SSO, Aufwand steigt linear mit Geräteanzahl |

---

## 📋 IHK-Cheatsheet

| Begriff | Kurzdefinition |
|---|---|
| Autoinstall (YAML) | Deklarative Konfigurationsdatei für Zero-Touch-OS-Installation |
| PXE-Boot | Netzwerkbasierter Boot-Vorgang zur automatisierten Installation |
| TPM | Hardware-Chip zur sicheren Schlüsselverwaltung (z. B. LUKS-Schlüssel) |
| Unattended Upgrades | Automatische Hintergrund-Installation von Sicherheitspatches |
| Kernel-Livepatching | Kernel-Fix ohne Reboot via ftrace-Umleitung |
| Staged Rollout | Stufenweise Softwareverteilung (Pilot → Fast → Broad Ring) |
| RBAC | Role-Based Access Control – Rechte an Rollen statt Personen |
| Least Privilege | Nur die minimal nötigen Rechte vergeben |
| OpenLDAP | Quelloffener Verzeichnisdienst für zentrale Benutzerverwaltung |
| SSO | Single Sign-On – ein Login für mehrere Systeme/Apps |

---

## 🎯 Prüfungstaktik

| Aufgabentyp | Formulierung im Fachgespräch | Was die IHK hören will |
|---|---|---|
| Automatisierung | "Wie stellst du 50 Rechner ohne manuellen Aufwand bereit?" | Autoinstall/YAML + PXE-Boot nennen, TPM für Verschlüsselung erwähnen |
| Wartungsstrategie | "Wie hältst du Systeme sicher ohne Ausfallzeiten?" | Unterschied Unattended Upgrades (Patches) vs. Livepatching (Kernel, kein Reboot) |
| Rollout-Risiko | "Wie vermeidest du einen Totalausfall bei neuer Software?" | Staged Rollout / Ring-Modell mit klaren Prozentsätzen |
| Zugriffskonzept | "Wie vergibst du Berechtigungen in einem wachsenden Unternehmen?" | RBAC + Least Privilege, Verweis auf zentralen Verzeichnisdienst |

---

## 💬 Merk-Sätze für die mündliche Prüfung

> "Zero-Touch heißt nicht ungeschützt – TPM sorgt dafür, dass Automatisierung und Sicherheit zusammen funktionieren."

> "Livepatching behebt den Fehler im Speicher, nicht auf der Festplatte – deshalb braucht es keinen Reboot."

> "Ein Rollout ohne Ringe ist ein Blindflug – man merkt den Fehler erst, wenn alle betroffen sind."

> "RBAC bindet Rechte an Rollen, nicht an Namen – wechselt die Rolle, wechseln automatisch die Rechte."

---

```yaml
lernfeld: LF6.2
titel: Systembereitstellung, Software & Identitätsmanagement
teil: 2 von 5
quellen:
  - LF6.2.1 Automatisierte Systembereitstellung und Wartung
  - LF6.2.2 Software-Verteilung und SaaS-Management
  - LF6.2.3 Identitäts- und Zugriffsberechtigung
status: final
stand: 2026
```
