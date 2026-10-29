# Ubuntu 26.04 LTS "Resolute Raccoon": Status, Features, Bugs

> **Veröffentlichung:** 23. April 2026  
> **Codename:** Resolute Raccoon  
> **Support:** 5 Jahre Standard (bis 2031), via Ubuntu Pro bis zu 15 Jahre  
> **Upgrade von 24.04 LTS:** Freigeschaltet mit Ubuntu 26.04.1 LTS am 6. August 2026

---

## Einleitung

Ubuntu 26.04 LTS markiert einen Wendepunkt in der Ubuntu-Architektur. Es konsolidiert moderne Linux-Technologien:
- **Wayland only** (X11 entfernt, nur noch Xwayland für Legacy-Apps)
- **Rust-basierte Systembasis** (speichersichere Coreutils, sudo-rs)
- **TPM-gestützte Vollverschlüsselung (FDE)** nun General Availability

---

## Systemarchitektur & Neuerungen

### Kernel & Toolchain
| Komponente | Version |
|------------|---------|
| Linux-Kernel | 7.0 |
| GCC | 15.2 |
| Python | 3.14.3 |
| systemd | 259 (nur cgroup v2) |
| Mesa | 26.0.x |
| Snapd | aktuell |

### Hardwareanforderungen (empfohlen)
| Komponente | Minimal | Empfohlen |
|------------|---------|------------|
| CPU | 2 GHz Dual-Core | 3 GHz Quad-Core+ |
| RAM | 2 GB (4 GB für Desktop) | **6 GB+** |
| Speicher | 25 GB frei | 100 GB+ SSD |
| Grafik | OpenGL/Vulkan | Wayland-beschleunigt |
| Firmware | UEFI + Secure Boot | UEFI 2.7+ mit TPM 2.0 |

> **Hinweis:** 6 GB RAM werden für flüssige Nutzung mit GNOME 50 und Snaps empfohlen. Installation auf 2/4 GB möglich, aber leistungseingeschränkt.

### Die "Oxidierungs"-Strategie (Rust-Integration)
- **sudo-rs** – vollständige Neuimplementierung von `sudo` in Rust
- **rust-coreutils** – `ls`, `grep`, `cat` etc. (Ausnahmen: `cp`, `mv` bleiben GNU)
- **Resources** – neue Systemmonitor-App (Rust + GTK4/libadwaita)

---

## Desktop-Umgebung: GNOME 50

- **Wayland only** – keine Xorg-Sitzung mehr
- **Variable Refresh Rate (VRR)** standardmäßig aktiviert
- **Fraktionales Scaling** verbessert (weniger Unschärfe)
- **Mauszeiger** läuft mit max. Bildwiederholfrequenz
- **Suchprovider** für Web und nicht installierte Snaps
- **Yaru-Theme** verschlankt (5.000 Zeilen weniger)

### Neue Standard-Apps (GTK4 / libadwaita)
| Alte App (24.04) | Neue App (26.04) | Besonderheit |
|------------------|------------------|--------------|
| Totem | **Showtime** | Bessere Hardwarebeschleunigung |
| GNOME System Monitor | **Resources** | Rust-basiert, CPU/GPU/NPU-Tracking |
| Evince | **Papers** | Sandboxed Loading, bessere Annotationen |
| Eye of GNOME | **Loupe** | Schnelleres Rendering (Glycin/Rust) |
| GNOME Terminal | **Ptyxis** | Für Container optimiert |
| Firefox 124 | **Firefox 150** | Höhere JS-Performance |

---

## Sicherheitsarchitektur

### TPM-gestützte Vollverschlüsselung (FDE) – GA
- **Verschlüsselung** über TPM 2.0, kein Passwort beim Boot nötig
- **Unified Kernel Image (UKI)** – signierte Binärdatei verhindert Initramfs-Manipulation
- **Recovery Key** wird während Installation generiert (extern sichern!)
- **PIN** optional zusätzlich im Security Center einstellbar
- **Dual-Boot** neben BitLocker-geschütztem Windows möglich

> **Einschränkungen:**  
> - Konflikt mit BIOS-Funktion "Absolute" (Computrace) → TPM-Bereitstellung schlägt fehl (LP: #2125409)  
> - Bestimmte NVMe-RAID-Konfigurationen inkompatibel  
> - ThinkPad-Modelle können PCR-Fehler zeigen → dann klassisches LUKS verwenden

### Weitere Härtung
- **Post-Quantum-Kryptographie** – hybrid `mlkem768x25519-sha256` standardmäßig für TLS
- **DSA** komplett entfernt
- **TLS 1.0/1.1** standardmäßig deaktiviert (Apache/Nginx)
- **chrony** mit Network Time Security (NTS) statt NTP
- **SSSD** läuft als unprivilegierter Benutzer (`sssd` statt `root`)

---

## Automatisierte Bereitstellung (Autoinstall)

Subiquity-Installer mit YAML-Autoinstall. Integration mit Landscape (OIDC-Authentifizierung).

### Beispiel `autoinstall.yaml` (LVM-on-LUKS)
```yaml
autoinstall:
  version: 1
  identity:
    hostname: resolute-node
    username: admin
    password: "$6$rounds=4096$..."   # gehasht
  storage:
    layout:
      name: lvm
      match:
        size: largest
      encrypted: true
      password: "initial-provisioning-secret"
  late-commands:
    - curtin in-target -- apt-get update
    - curtin in-target -- apt-get install -y landscape-client

Diese Struktur ermöglicht ein LVM-on-LUKS Setup. Nach der Installation können Tools wie
snap-tpmctl genutzt werden, um von der passwortbasierten zur TPM-basierten Entsperrung
zu wechseln.    

    # USB-Stick für automatisierte Installation (Ubuntu 26.04 LTS)

## Vorbereitung des USB-Sticks

1. **Partition mit Label `CIDATA` erstellen**  
   (z. B. mit `gparted` oder `fdisk`, Dateisystem z. B. `vfat` oder `ext4`)

2. **Dateien in das Stammverzeichnis der Partition kopieren**  
   - `user-data` (enthält Autoinstall-YAML)  
   - `meta-data` (kann leer sein)

3. **Bootfähiges Medium erstellen**  
   - **Ubuntu**: Startup Disk Creator  
   - **Windows**: Rufus (ISO-Modus)  
   - **macOS**: balenaEtcher

> ℹ️ Der USB-Stick wird nach dem Booten automatisch von der Ubuntu-Installation als `autoinstall`-Quelle erkannt, wenn die Partition das Label `CIDATA` trägt.

---

## Bekannte Probleme & Workarounds

| Problem | Symptom | Workaround / Status |
|---------|---------|---------------------|
| Benutzererstellung (GUI) | Fehler 255 in GNOME-Einstellungen; Konto wird deaktiviert angelegt | Terminal: `sudo adduser <name>` funktioniert |

| Wayland-Menü-Verzögerungen | Snap-Apps (z. B. Steam) reagieren verzögert | Bug in `mutter` (LP: #2147501); Update in Vorbereitung |

| `who` / `users` | Keine Ausgabe (rust-coreutils) | Ersatz: `w` verwenden |

| GNOME-Erweiterungen | Inkompatibel mit GNOME 50 | In `metadata.json` `"50"` zu `shell-version` hinzufügen (keine Garantie) |

| TPM-FDE Pre-Check | False Positive "PCR unusable" auf ThinkPads | Manuelle Verschlüsselung nach Installation mit `systemd-cryptenroll` |

| Ventoy 1.1.11 | Installationsabbruch beim Booten | Upgrade auf 1.1.12 oder Downgrade auf 1.1.10 |

| Bootstrap-Blockade | Installer hängt bei `unattended-upgrades` | Terminal öffnen, Prozess `ubuntu-desktop-bootstrap` manuell beenden |

| Apache2/PHP | PHP 8.5 Standard; Nextcloud <32 findet Pfade nicht | Über `update-alternatives` oder Ondřej Surý PPA auf 8.3/8.4 downgraden |

| Software & Updates GUI | Klassische PPA-Verwaltung fehlt | `sudo apt install software-properties-gtk` nachinstallieren |

---

## Upgrade-Pfad & Stabilitätsbewertung

- **Offizieller Upgrade-Pfad von 24.04 LTS**  
  Erst mit **26.04.1 LTS** (voraussichtlich 6. August 2026) möglich.

- **cgroup v1 wurde entfernt**  
  Container-Runtimes müssen vor dem Upgrade auf **cgroup v2** umgestellt werden (z. B. `systemd-cgroup-driver`).

---

## Vergleich 24.04 LTS ↔ 26.04 LTS

| Feature | 24.04 LTS | 26.04 LTS |
|---------|-----------|-----------|
| Anzeige-Protokoll | X11 / Wayland hybrid | Wayland only |
| Verschlüsselung | LUKS (Passwort) | TPM-FDE (GA) |
| Systemwerkzeuge | GNU C-basiert | Rust-basiert (coreutils) |
| Softwareverwaltung | Software & Updates GUI | Integriertes App Center |
| Identitätsdienst | SSSD (als root) | SSSD (unprivilegiert) |

---

## Hilfreiche Links (Dokumentation & Diskussion)

- Ubuntu 26.04 LTS Release Notes  
- Hardware-backed disk encryption (TPM-FDE)  
- Autoinstall Reference Manual  
- What's new in security for Ubuntu 26.04 LTS  
- Phoronix: Benchmarks vs. 24.04  
- OMG! Ubuntu! – GNOME 50 & Wayland-only  
- The Register – Drops Xorg, keeps X11 apps alive  
- Reddit – Diskussion zu TPM-FDE und Bugs

> **Hinweis:** Die Originalquellen enthalten keine konkreten URLs – obige Punkte sind als Suchbegriffe / Titel zu verstehen.