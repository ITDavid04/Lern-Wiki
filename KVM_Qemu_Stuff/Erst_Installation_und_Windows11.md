🚀Windows 11 in der KVM-Box- Der Profi-Guide

#### **Zielgruppe:** Fachinformatiker (SI & AE) | **Fokus:** Performance & Best Practices

#### Windows 11 stellt hohe Anforderungen an die Hardware-Emulation. Mit dieser Anleitung konfigurierst du eine VM,

#### die performant läuft und alle Microsoft-Checks besteht.

#### Am Ende hast du eine vollständig laufende Windows-11-VM auf deinem Ubuntu-Host.


#### 💡 Wichtig: Lese Die Anleitung erst einmal Komplett und einzelne Punkte damit es nicht zu Überraschungen kommt bei der Umsetzung.


## 🛠️ 1. Vorbereitung – Werkzeugkasten füllen

Bevor wir die VM bauen, muss die Host-Umgebung (Linux) vorbereitet werden. Alle folgenden Befehle werden im **Terminal** ausgeführt (öffnen mit `Strg + Alt + T`).

### 📦 1.1 Pakete installieren

Aktualisiere zuerst die Paketquellen und installiere die notwendigen Pakete:

```
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager virt-viewer cpu-checker swtpm
```

**Was wird installiert?**

- **qemu-kvm**: Die eigentliche Virtualisierungssoftware.
- **libvirt-daemon-system**: Dienst zur Verwaltung von VMs.
- **virt-manager**: Grafische Oberfläche zur VM-Verwaltung.
- **swtpm**: Emuliert ein TPM 2.0 – **zwingend erforderlich für Windows 11**.
- **cpu-checker**: Prüft, ob deine CPU Virtualisierung unterstützt.

**Teste nach der Installation, ob alles bereit ist:**

```
kvm-ok
```

Es sollte eine Meldung wie `INFO: /dev/kvm exists – KVM acceleration can be used` erscheinen. Falls nicht, musst du im BIOS/UEFI die Virtualisierung (VT-x/AMD-V) aktivieren.

Prüfe außerdem, ob der libvirt-Dienst läuft:

```
systemctl status libvirtd
```

Wenn er nicht aktiv ist, starte ihn mit `sudo systemctl start libvirtd` und aktiviere den Autostart: `sudo systemctl enable libvirtd`.

### 1.2 Berechtigungen setzen, **Die „VIP-Karte“ lösen:**

Damit du die VM ohne Root-Rechte verwalten kannst, füge deinen Benutzer zu den Gruppen `libvirt` und `kvm` hinzu:

```
sudo adduser $(whoami) libvirt
sudo adduser $(whoami) kvm
```

💡 **\> WICHTIG:** Melde dich einmal ab und wieder an (oder starte den Rechner neu), damit die Gruppenrechte aktiv werden.  
Alternativ kannst du im Terminal `newgrp libvirt` und `newgrp kvm` ausführen, das wirkt aber nur für das aktuelle Terminalfenster.

## 📥 2. ISOs besorgen

Du benötigst zwei Dateien. Lege sie am besten in deinem **Downloads-Ordner** ab und verschiebe sie dann an den systemweiten Speicherort für VM-Images.

|     |     |     |
| --- | --- | --- |
| Datei | Zweck | Bezugsquelle |
| **Windows 11 ISO** | Das Betriebssystem | [Microsoft Offizielle Seite](https://www.microsoft.com/de-de/software-download/windows11) |
| **VirtIO-Win ISO** | Hochgeschwindigkeitstreiber für Festplatte, Netzwerk, etc. | [Fedora GitHub (virtio-win.iso)](https://github.com/virtio-win/virtio-win-pkg-scripts/blob/master/README.md) (direkter Download-Link: https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso) |

**Bilder:**


![Bild1_ISO_Auswahl](PNG/Bild1_ISO_Auswahl.png)

![Bild2_Iso_Auswahl](PNG/Bild2_Iso_Auswahl.png)

Nach Bestätigen startet der Download ca 7,8 GB

![Bild3_Iso_Auswahl](PNG/Bild3_Iso_Auswahl.png)

### \*\*💡\*\*Tip:

Lege dir eine Kopie an wenn du das Image später nochmal nutzen möchtest bevor du weitermachst.

### ISO-Dateien an den richtigen Ort bringen

Der Standardordner für VM-Images ist `/var/lib/libvirt/images/`. Da dieser Ordner Root-Rechte benötigt, verschieben wir die ISOs mit `sudo`:

```
sudo mv ~/Downloads/Windows11.iso /var/lib/libvirt/images/
sudo mv ~/Downloads/virtio-win.iso /var/lib/libvirt/images/
```

### **💡 Hinweis:**

Falls deine heruntergeladenen Dateien anders heißen, passe die Namen entsprechend an.  
Du kannst die ISOs auch später direkt im Assistenten auswählen – der Speicherort ist dann egal, aber die Ablage im images-Ordner ist aufgeräumt und vermeidet Berechtigungsprobleme.

## ⚙️ 3. VM erstellen – Die "Hardware" konfigurieren

Jetzt öffnen wir den **Virtual Machine Manager** (kurz: Virt-Manager). Du findest ihn im Anwendungsmenü oder startest ihn über das Terminal mit `virt-manager`.

### 3.1 Neue VM anlegen

1. Klicke in der Menüleiste auf das Symbol mit der **blinkenden Glühbirne** oder wähle **Datei → Neue virtuelle Maschine**.
2. **Installationsmedium**: Wähle **„Lokales Installationsmedium (ISO-Image oder CDROM)“** und klicke auf **Weiter**.
3. **ISO auswählen**: Klicke auf **„Durchsuchen“** → **„Durchsuchen lokal“**. Navigiere zu `/var/lib/libvirt/images/` und wähle die **Windows11.iso** aus. Klicke auf **Volume auswählen**.
4. **Betriebssystem-Typ/Version**: Normalerweise erkennt Virt-Manager automatisch „Microsoft Windows 11“. Falls nicht, wähle **„Microsoft Windows“** und als Version **„Microsoft Windows 10“** (Windows 11 wird oft noch nicht explizit angeboten, ist aber kompatibel). Klicke auf **Weiter**.

💡 Wird in der Regel erkannt von VM-Manager das es ein Windows 11 ISO ist.

**Bild**


![Bild4_KVM_erstellen](PNG/Bild4_KVM_erstellen.png)

**3.2 RAM und CPU**:

- RAM: **8192 MB** (mindestens 8 GB, sonst verweigert Windows 11 die Installation)
- CPUs: **4** (Anzahl der Kerne, die du der VM zuweisen möchtest)
- Aktiviere **„Host-CPU-Konfiguration kopieren“**? Das machen wir später im Detail – erstmal nur die Zahlen einstellen.
- Klicke auf **Weiter**.


**Bild**


![Bild4_KVM_erstellen](PNG/Bild5_KVM_erstellen.png)

**3.3 Festplatte**:

- Wähle **„Festplatte erzeugen“**.
- Größe: **64 GB** (mindestens; Windows 11 bricht bei kleineren Platten die Installation ab).
- Haken bei **„Speicherplatz jetzt zuweisen“** kann optional gesetzt werden (dann wird die volle Größe sofort belegt, was die Performance etwas verbessert).
- Klicke auf **Weiter**.

**Bild**


![Bild6_KVM_erstellen](PNG/Bild6_KVM_erstellen.png)

**3.4 Name und Konfiguration**:

- Vergib einen Namen, z.B. **Win11-Profi**.
- **WICHTIG:** Setze den Haken bei **„Konfiguration vor der Installation anpassen“**.
- Klicke auf **Fertigstellen**.

**Bild**


![Bild7_KVM_erstellen](PNG/Bild7_KVM_erstellen.png)

3.2 Detail-Konfiguration (vor dem ersten Start)

Nach dem Klick auf Fertigstellen öffnet sich automatisch das Fenster mit den VM-Details. Hier nimmst du jetzt die entscheidenden Einstellungen vor:

**Bild**


![Bild8_KVM_erstellen](PNG/Bild8_KVM_erstellen.png)

#### Übersicht (ganz oben links)

- **Firmware**: Ändere den Eintrag auf **„UEFI x86_64: … OVMF_CODE.secboot.fd“** (oder nur „UEFI mit Secure Boot“). Das ist notwendig für TPM 2.0 und Secure Boot.

## 💡Wichtig, nach jeder Änderung Übernehmen bestätigen über den Button!!!

**Bild**


![Bild9_KVM_erstellen](PNG/Bild9_KVM_erstellen.png)

#### CPUs

- Klicke auf **„CPUs“** im linken Menü.
- Aktiviere unter **„CPU-Konfiguration“** die Option **„Host-Modell kopieren“**. Das sorgt für beste Performance, weil die VM die CPU-Funktionen des Hosts direkt nutzt.

Ist Stabdardmäßig Aktiviert!!!

**Bild**


![Bild10_KVM_erstellen](PNG/Bild10_KVM_erstellen.png)

#### SATA-Disk 1

- Klicke auf **„SATA-Disk 1“**.
- Ändere den **„Disk-Bus“** von **SATA** auf **VirtIO**.
  - _Hintergrund:_ VirtIO ist ein paravirtualisierter Treiber, der wesentlich schneller ist als die Emulation einer SATA-Festplatte. Windows benötigt dafür aber den Treiber von der VirtIO-ISO – den laden wir später während der Installation.

**Bild**


![Bild11_KVM_erstellen](PNG/Bild11_KVM_erstellen.png)

#### TPM (Trusted Platform Module)

- Windows 11 **erfordert** ein TPM 2.0. Falls noch kein TPM in der Liste auftaucht, füge es hinzu:
  - Klicke unten auf **„Hardware hinzufügen“**.
  - Wähle in der Liste **„TPM“** aus.
  - **Typ**: Wähle **„TPM 2.0“**.
  - **Modell**: **„TIS“** (oder „CRB“ – beides funktioniert; TIS ist gebräuchlicher).
  - Klicke auf **Fertigstellen**.

**Bild**


![Bild12_KVM_erstellen](PNG/Bild12_KVM_erstellen.png)

#### VirtIO-Treiber-ISO einlegen

- Damit Windows später die Treiber für Festplatte, Netzwerk etc. findet, legen wir jetzt die zweite ISO als CD-ROM ein:
  - Wieder **„Hardware hinzufügen“** → **„Storage“**.
  - **Gerätetyp**: **„CD-ROM-Gerät“**.
  - Wähle **„Vorhandenes Image verwenden“** und klicke auf **„Durchsuchen“**.
  - Navigiere zu `/var/lib/libvirt/images/virtio-win.iso` und wähle sie aus.
  - Klicke auf **Fertigstellen**.

**Bild**


![Bild13_KVM_erstellen](PNG/Bild13_KVM_erstellen.png)


Auf Verwalten Klicken


![Bild14_KVM_erstellen](PNG/Bild14_KVM_erstellen.png)


![Bild15_KVM_erstellen](PNG/Bild15_KVM_erstellen.png)

💡Optional

💡Windows 11 (besonders die Home-Edition) erkennt manchmal nicht alle zugewiesenen Kerne, wenn sie als separate "Sockets" emuliert werden.

- **Tipp:** Gehe in den Bereich **CPUs**, klappe **Topologie** auf und setze den Haken bei "CPU-Topologie manuell festlegen".
- Stell es so ein: **Sockets: 1**, **Kerne: 4** (oder deine Anzahl), **Threads: 1** (oder 2 für Hyperthreading).
- **Warum?** Das stellt sicher, dass Windows die volle Leistung nutzt und nicht denkt, du hättest ein seltener unterstütztes Multi-Socket-System.

💡 **Tipp:** Stelle bei der VirtIO-Disk den **Cache-Modus** auf `none` (wenn die Host-Disk sicher ist) oder `writeback` und den **I/O-Modus** auf `native`. Das reduziert den Overhead spürbar, besonders auf NVMe-Speichern.

### Video-Treiber & Anzeige

Windows 11 fühlt sich mit dem Standard-VGA-Treiber sehr zäh an.

- **Empfehlung:** In den VM-Details unter **Video** sollte idealerweise **Virtio** ausgewählt sein. Wenn der Host eine GPU mit 3D-Beschleunigung hat, aktiviere „3D-Beschleunigung“. Zusammen mit dem `virtio-win-guest-tools`\-Paket (Punkt 5) wird die UI dadurch butterweich.

**Bild**


![Bild16_KVM_erstellen](PNG/Bild16_KVM_erstellen.png)



💡 Hinweis: Du kannst auch später während der Installation die ISO nachträglich einlegen. Aber so ist sie schon da und du musst nicht unterbrechen.

Jetzt ist die Hardware perfekt vorbereitet. Klicke oben links auf „Installation beginnen“.

**Bild**


![Bild17_KVM_erstellen](PNG/Bild17_KVM_erstellen.png)



💿 4. Windows 11 Installation & Fallstricke

Die VM startet nun und bootet von der Windows-ISO. Drücke sofort eine beliebige Taste, wenn die Meldung „Press any key to boot from CD/DVD“ erscheint.

**Bild**


![Bild18_Windows_setup](PNG/Bild18_Windows_setup.png)


4.1 „Wo ist meine Festplatte?“ – VirtIO-Treiber laden

Nach der Sprachauswahl und dem Klick auf „Jetzt installieren“ wirst du nach dem Produktschlüssel gefragt. Wenn du keinen hast, klicke auf „Ich habe keinen Produktschlüssel“ und wähle die gewünschte Edition (meist Windows 11 Pro).
Akzeptiere die Lizenzbedingungen und wähle „Benutzerdefiniert: Nur Windows installieren (erweitert)“.

Jetzt kommt der entscheidende Moment: Es wird keine Festplatte angezeigt! Das ist normal, weil wir den Bus auf VirtIO gestellt haben und der Treiber fehlt.

**Bild**


![Bild19_Windows_setup](PNG/Bild19_Windows_setup.png)


1. Klicke auf **„Treiber laden“**
2. Es öffnet sich ein Fenster. Klicke auf **„Durchsuchen“**.
3. Wähle das CD-Laufwerk mit der **VirtIO-ISO** (meistens **D:**).

**Bild**


![Bild20_Windows_setup](PNG/Bild20_Windows_setup.png)


Dropdownmenü Öffnen


![Bild21_Windows_setup](PNG/Bild21_Windows_setup.png)


Navigiere zu `amd64` → `w11` (für Windows 11) oder `2k22` (für Windows Server).  
Bei manchen Versionen heißt der Ordner nur `w10` – auch den kannst du verwenden.

1. Bestätige mit **„OK“**.
2. Es erscheint ein Treiber namens **„Red Hat VirtIO SCSI controller“** (oder ähnlich). Markiere ihn und klicke auf **„Weiter“**.
3. Nach einem kurzen Moment sollte deine 64-GB-Festplatte erscheinen.

**Bild**


![Bild22_Windows_setup](PNG/Bild22_Windows_setup.png)


💡 Hintergrund: Der Treiber wird jetzt installiert und Windows kann auf die VirtIO-Festplatte zugreifen. Wähle die Festplatte aus und klicke auf „Weiter“. Die Installation beginnt.


![Bild23_Windows_setup](PNG/Bild23_Windows_setup.png)


Installation Starten


![Bild24_Windows_setup](PNG/Bild24_Windows_setup.png)


🎊 Warten bis fertig, Ohne Scheiß wenn du alles richtig gemacht hast bist du auf diesem Schirm. 🎊


![Bild25_Windows_setup](PNG/Bild25_Windows_setup.png)


![Bild26_Windows_setup](PNG/Bild26_Windows_setup.png)

🪔Folge der Installation. Bring Geduld mit es ist WINDOWS! 🪔

**Bild**


![Bild27_Windows_setup](PNG/Bild27_Windows_setup.png)


💡Nutze im Verlauf die Einstellung Privat Einrichten und nicht den Button Schüler etc. Damit du dich nicht mit einem Windows Konto anmelden musst.💡 (Falls deine Windows-Lizenz über Schule oder Bildungsträger läuft und später entfällt, legst du so am Ende der Installation ein eigenes lokales Konto an.)

**Bild**


![Bild28_Windows_setup](PNG/Bild28_Windows_setup.png)


🪔Dann heist es wieder Geduld haben…Sorry Updates und so🪔. 30 MIN Einplanen

Erstelle ein Windows Konto neu. Und führe den rest der Installtion durch. am ende solltest du auf dem Startbildschrim Landen.


![Bild29_Windows_setup](PNG/Bild29_Windows_setuo.png)


## 🧩 5. Post-Installation – Performance-Boost

Jetzt sind wir auf dem Desktop. Aber Netzwerk, Grafik und Mausintegration funktionieren noch nicht optimal – auch hier fehlen die VirtIO-Treiber.

1. Öffne den **Windows Explorer** und wechsle zu **Dieser PC**. Dort siehst du das CD-Laufwerk mit der **VirtIO-ISO** (meistens **D:**).

**Bild**


![Bild30_Windows_boost](PNG/Bild30_Windows_boost.png)


![Bild31_Windows_boost](PNG/Bild31_Windows_boost.png)


Öffne das Laufwerk. Suche nach der Datei virtio-win-gt-x64.msi (manchmal heißt sie auch virtio-win-guest-tools.msi). Starte sie mit einem Doppelklick.


![Bild32_Windows_boost](PNG/Bild32_Windows_boost.png)


![Bild33_Windows_boost](PNG/Bild33_Windows_boost.png)


**Folge dem Installationsassistenten. Wähle die Standardinstallation (alle Komponenten).**

**Dadurch werden installiert:**

Netzwerktreiber (für Internet in der VM)
Balloon-Treiber (für dynamische Speicherverwaltung)
QEMU Guest Agent (ermöglicht sauberes Herunterfahren und flüssige Fensterskalierung)
Grafische Treiber (für bessere Auflösung)

**Bild**


![Bild34_Windows_boost](PNG/Bild34_Windows_boost.png)


1. Starte die VM nach Abschluss der Installation **neu** (über das Windows-Startmenü).

Nach dem Neustart sollte das Netzwerk funktionieren und die VM sich nahtlos in das Fenster einpassen lassen.

**Zusatz**

## 🛠️ 6. Profi-Tipps für SIs und AEs

### 💡 Für Systemintegratoren (SI): Netzwerk-Konfiguration

Standardmäßig nutzt KVM **NAT** (Network Address Translation). Das bedeutet: Die VM kommt ins Internet, ist aber von außen nicht erreichbar – wie ein Gerät hinter einem Router.

Wenn du Dienste in der VM anbieten möchtest (z.B. IIS, SQL-Server, Testumgebungen), solltest du die Netzwerkquelle auf **Bridge** umstellen. Dadurch erhält die VM eine eigene IP-Adresse im selben Netzwerk wie dein Host und ist direkt erreichbar.

**So erstellst du eine Bridge (vereinfacht):**

- Installiere das Paket `bridge-utils` (falls nicht schon geschehen):  
  `sudo apt install bridge-utils`
- Konfiguriere eine Bridge in `/etc/netplan/` (bei Ubuntu). Eine detaillierte Anleitung findest du in der [Ubuntu Wiki](https://wiki.ubuntu.com/KvmWithBridge).
- Danach kannst du in den VM-Einstellungen unter **NIC** die Netzwerkquelle auf das Bridge-Gerät umstellen.

### 💡 Für Anwendungsentwickler (AE): Snapshots

Bevor du große Entwicklungsumgebungen wie Visual Studio, Docker oder mehrere Datenbanken installierst, erstelle einen **Snapshot** (Momentaufnahme) der VM.

- **Vorgehen:** Öffne den Virt-Manager, wähle die VM aus und klicke auf das **Kamera-Symbol** in der Symbolleiste (oder über das Menü **VM → Snapshot**). Gib dem Snapshot einen Namen wie „Clean nach Installation“.
- **Vorteil:** Wenn später etwas schiefgeht (Registry-Fehler, verseuchte Umgebung), kannst du in Sekunden zu diesem sauberen Zustand zurückkehren – ohne Neuinstallation.

### Gemeinsamer Ordner (Shared Folder) zwischen Host und Gast

Um Dateien einfach auszutauschen, kannst du einen gemeinsamen Ordner einrichten. Dazu benötigst du den **spice-webdavd** Dienst.

1. Installiere auf dem Host: `sudo apt install spice-webdavd`
2. Starte den Dienst: `systemctl --user start spice-webdavd`
3. In der VM (Windows) installiere den **Spice Guest Tools** (enthalten in der VirtIO-ISO oder separat herunterladbar). Nach der Installation erscheint im Dateiexplorer ein neues Laufwerk, das auf einen Ordner deiner Wahl auf dem Linux-Host zeigt.
4. **Hinweis:** Virtio-FS ist performanter als WebDAV, benötigt aber unter Windows einen speziellen Treiber (WinFSP), der ebenfalls im VirtIO-ISO-Umfeld zu finden ist. Für den schnellen Austausch reicht deine WebDAV-Lösung aber völlig aus.

### 💡 _Korrektur:_ Der Dienst auf dem Ubuntu-Host heißt meist `phodav` oder wird direkt über `virt-manager` (Channel hinzufügen) gesteuert. `spice-webdavd` ist der Name des Dienstes **innerhalb** der Windows-VM.

---

## 🏁 Abschluss-Checkliste

Bevor du die VM produktiv nutzt, überprüfe noch einmal die wichtigsten Punkte:

- **UEFI & TPM 2.0 aktiviert?** (In den VM-Einstellungen unter „Übersicht“ und „TPM“ prüfen)
- **Festplatte mit mind. 64 GB und Bus auf VirtIO?**
- **VirtIO-Treiber (MSI-Paket) installiert?** (Netzwerk und Grafik sollten funktionieren)
- **OOBE-Bypass erfolgreich genutzt?** (Lokales Konto vorhanden)
- **Snapshot erstellt?** (Für späteren schnellen Reset)
- **CPU-Pinning / Host-Modell kopiert?** (Für maximale Leistung)

---

### 🚀 **Mission erfüllt!** Deine Windows 11 Umgebung ist nun bereit für den professionellen Einsatz – ob als Testlabor, Entwicklungsumgebung oder Server-Emulation.

📡 7. Netzwerk-Bridge (SI-Spezial)

Für direkten LAN-Zugriff der VM (statt NAT).

Netplan Beispiel (/etc/netplan/01-bridge.yaml):

network:
  version: 2
  ethernets:
    enp3s0: # Prüfen mit 'ip link'
      dhcp4: no
  bridges:
    br0:
      interfaces: [enp3s0]
      dhcp4: yes
      parameters:
        stp: true
        forward-delay: 0


📸 Maintenance

💡[!TIP] Snapshot erstellen: Erstelle sofort nach der Treiber-Installation einen Snapshot im Virt-Manager ("Clean_Install"), um jederzeit zu einem sauberen System zurückzukehren.

