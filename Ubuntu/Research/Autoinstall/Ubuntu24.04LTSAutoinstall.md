# cloud-config

## Automatische Ubuntu-Installation (Autoinstall) – Aktualisierte Version

Diese Datei steuert eine komplett unbeaufsichtigte Installation von Ubuntu.  
Sie wird beim Booten von einem angepassten ISO (z. B. mit Cubic erstellt) automatisch ausgeführt. Alle Einstellungen werden hier festgelegt – es sind keine manuellen Eingriffe nötig. (Bei unseren Laptops ist ggf. eine BIOS-Einstellung nötig, um vom richtigen Medium zu booten.)

**Wichtig:** Diese Version ersetzt die vorherige Anleitung und enthält zahlreiche Verbesserungen:  
geänderter SSH-Port, zusätzliche Gruppen, Deaktivierung von Snap, globales Oh‑My‑Bash, GNOME‑Anpassungen, Virtualisierungstuning und ein eigenes Tool zum Anlegen von Laborbenutzern.

---

```yaml
autoinstall:
  version: 1
  source:
    # Wählt die zu installierende Basis aus.
    # 'ubuntu-desktop-minimal' ist eine schlanke Variante der Ubuntu-Desktop-Umgebung.
    # Im Vergleich zum normalen 'ubuntu-desktop' fehlen viele vorinstallierte Apps
    # (wie Spiele, LibreOffice, Thunderbird). Das spart Platz und Zeit bei der Installation.
    # Später können gezielt nur die benötigten Pakete nachinstalliert werden.
    id: ubuntu-desktop-minimal

  # KEINE INTERAKTIVEN ABFRAGEN
  # Diese Liste bleibt leer, damit die Installation ohne jede Benutzereingabe durchläuft.
  # Normalerweise könnte man hier Sektionen wie "keyboard" oder "network" angeben,
  # die dann trotzdem interaktiv abgefragt würden. Da wir alles vorkonfigurieren,
  # lassen wir sie leer.
  interactive-sections: []

  # BENUTZERKONTO (ADMINISTRATOR)
  identity:
    hostname: D3030                # Name des Rechners im Netzwerk (kann später geändert werden)
    username: adminuser            # Erster Benutzer = Administrator (mit sudo-Rechten)
    # Passwort-Hash für das Klartext-Passwort '1234'.
    # Das Passwort wird NIEMALS im Klartext gespeichert, sondern als Hash.
    # Dieser Hash wurde mit dem modernen yescrypt-Algorithmus erzeugt (erkennbar am Prefix $y$),
    # der sicherer ist als der frühere SHA-512. Yescrypt ist seit Ubuntu 22.04 der Standard.
    # So kann das System später das eingegebene Passwort mit dem Hash vergleichen,
    # ohne das Passwort selbst zu kennen.
    # Zum Erzeugen eines eigenen Hashs kann man den Befehl 'mkpasswd -m yescrypt' verwenden.
    password: "$y$j9T$EM4QOn87FWI/ffG4oDDGW.$6/ync8XVbURF4TX4vAEZOHCW2TQelGw9gjsV5tmC2Z9"

  # BENUTZERGRUPPEN (WERDEN SYSTEMWEIT ANGELEGT)
  # Hier definieren wir zusätzliche Gruppen, die später für verschiedene Dienste benötigt werden.
  # Diese Gruppen existieren bereits im System, wir stellen nur sicher, dass sie bei der
  # Installation vorhanden sind. Der Administrator 'adminuser' wird später über
  # late-commands in die Gruppen docker, libvirt und kvm aufgenommen.
  user-data:
    groups: [docker, libvirt, kvm, students]

  # LOKALISIERUNG
  locale: de_DE.UTF-8              # Sprache und Regionsformat (z.B. Datum, Zahlen)
  keyboard:
    layout: de                     # Tastaturlayout auf Deutsch (QWERTZ)
  timezone: Europe/Berlin          # Zeitzone – wichtig für korrekte Systemzeit

  # SSH-SERVER
  ssh:
    install-server: true           # Installiert den OpenSSH-Server, damit man nach der Installation
                                   # remote per SSH auf den Rechner zugreifen kann.
    allow-pw: true                 # Erlaubt Passwort-Authentifizierung (statt nur SSH-Key).
                                   # In Verbindung mit den späteren Firewall-Regeln wird der Zugang
                                   # auf Port 2222 und den Benutzer adminuser beschränkt.

  # SPEICHERKONFIGURATION (PARTITIONIERUNG)
  # Hier wird die Festplatte (NVMe-SSD) komplett neu eingeteilt.
  # Wir verwenden GPT (GUID Partition Table) als Partitionstabelle – das ist der moderne Standard
  # für UEFI-Systeme. Die Festplatte wird mit LVM (Logical Volume Manager) eingerichtet,
  # was später flexible Anpassungen der Partitionen erlaubt.
  storage:
    config:
      # Schritt 1: Die gesamte Festplatte /dev/nvme0n1 als Basis definieren.
      - type: disk
        id: disk-nvme0n1
        match:
          path: /dev/nvme0n1       # Dies ist der Gerätename der ersten NVMe-SSD.
                                   # Bei SATA-Festplatten wäre es z.B. /dev/sda.
        ptable: gpt                # Partitionstabelle: GPT (statt altem MBR)
        # preserve: false (Standard) – die vorhandene Partitionstabelle wird komplett gelöscht
        # und neu geschrieben. Die Festplatte ist danach also leer.

      # Schritt 2: EFI-Systempartition erstellen (zwingend für UEFI-Boot)
      - type: partition
        id: efi-partition
        device: disk-nvme0n1       # Auf dieser Festplatte
        size: 260M                 # Größe: 260 Megabyte – das ist mehr als das Minimum (100M),
                                   # um sicherzugehen, dass genug Platz für mehrere Bootloader ist.
        flag: boot                 # Markiert die Partition als bootfähig (für UEFI wichtig)
        grub_device: true          # Hier wird der Bootloader GRUB installiert
        # preserve: false          # Neu anlegen

      # Schritt 3: Eine weitere Partition, die den gesamten verbleibenden Platz einnimmt.
      # Diese Partition wird später als "physisches Volume" für LVM verwendet.
      - type: partition
        id: lvm-pv-partition
        device: disk-nvme0n1
        size: -1                   # -1 bedeutet: den gesamten restlichen Platz nutzen
        # preserve: false
        wipe: superblock           # Entfernt alte LVM-Signaturen, falls vorhanden – wichtig für Sauberkeit

      # Schritt 4: LVM-Volume-Gruppe (VG) anlegen.
      # Eine Volume-Gruppe fasst mehrere physische Volumes (hier nur die eine Partition) zu einem Pool zusammen.
      - type: lvm_volgroup
        id: ubuntu-vg
        name: ubuntu-vg            # Name der Volume-Gruppe – wird später unter /dev/ubuntu-vg sichtbar
        devices:
          - lvm-pv-partition       # Die oben erstellte Partition wird als physisches Volume (PV) eingebunden

      # Schritt 5: Logisches Volume (LV) für das Root-Dateisystem anlegen.
      # Ein logisches Volume ist wie eine "flexible Partition" innerhalb der Volume-Gruppe.
      - type: lvm_partition
        id: root-lv
        name: root
        volgroup: ubuntu-vg
        size: -1                   # Das logische Volume bekommt den gesamten Platz der Volume-Gruppe.
                                   # Man könnte hier auch eine bestimmte Größe angeben und später weitere LVs anlegen.

      # Schritt 6: Das logische Volume formatieren.
      - type: format
        id: root-fs
        volume: root-lv
        fstype: ext4               # ext4 ist das Standard-Dateisystem unter Linux (stabil, weit verbreitet)

      # Schritt 7: Die EFI-Partition formatieren (muss FAT32 sein, das verlangt die UEFI-Spezifikation).
      - type: format
        id: efi-fs
        volume: efi-partition
        fstype: fat32

      # Schritt 8: Das Root-Dateisystem einhängen (mounten).
      - type: mount
        id: root-mount
        device: root-fs
        path: /                    # Das ist das Wurzelverzeichnis des späteren Systems

      # Schritt 9: Die EFI-Partition einhängen.
      - type: mount
        id: efi-mount
        device: efi-fs
        path: /boot/efi            # Standard-Mountpunkt für EFI unter Linux

  # NETZWERK WÄHREND DER INSTALLATION
  # Wir lassen das Netzwerk während der Installation deaktiviert.
  # Das verhindert, dass das Installationsprogramm versucht, eine Netzwerkverbindung herzustellen
  # und dabei eventuell fehlschlägt, weil noch keine Konfiguration existiert.
  # In den latecommands wird das später installiert und wlan zugriff ist nach dem ersten Booten verfügbar. 
  # Dazu wurde die Linux-Firmware auf das iso gladen und wird im laufe des Prozesses in eine Bilblithek gelegt für die spätere installtation.
  network:
    version: 2
    ethernets: {}                  # Leeres Objekt = keine Ethernet-Schnittstelle wird aktiviert

  # BEFEHLE AM ENDE DER INSTALLATION (late-commands)
  # Diese Befehle werden ausgeführt, NACHDEM das Basissystem auf die Festplatte kopiert wurde,
  # aber bevor der Rechner neu startet. Sie laufen im Kontext des Installationsmediums (Live-System),
  # können aber mit 'curtin in-target -- <Befehl>' Befehle im ZIELSYSTEM (auf der Festplatte) ausführen.
  # Jeder Befehl ist mit '|| true' abgesichert (oder in Skripten eingebettet), damit die Installation
  # auch bei Fehlern fortgesetzt wird.
  late-commands:
    # ------------------------------------------------------------------------
    # 1. SSH-SERVER AUF PORT 2222 UMKONFIGURIEREN UND AUF ADMINUSER BESCHRÄNKEN
    # ------------------------------------------------------------------------
    # Aus Sicherheitsgründen wird der SSH-Port vom Standard 22 auf 2222 geändert.
    # Das reduziert die Anzahl automatischer Angriffe auf den Standard-Port.
    # Zudem wird der Zugriff nur für den Benutzer 'adminuser' erlaubt.
    - curtin in-target -- sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
    - curtin in-target -- bash -c 'echo "AllowUsers adminuser" >> /etc/ssh/sshd_config'

    # ------------------------------------------------------------------------
    # 2. FIRMWARE-DATEIEN KOPIEREN UND INITRAMFS AKTUALISIEREN
    # ------------------------------------------------------------------------
    # Das Installations-ISO (Live-System) enthält oft viele Firmware-Dateien für WLAN-Chips.
    # Nach der Installation fehlen diese manchmal im Zielsystem, weil sie nicht automatisch übernommen werden.
    # Daher kopieren wir den gesamten Firmware-Ordner manuell ins Ziel.
    # Danach muss das Initramfs (ein frühes Dateisystem, das beim Booten geladen wird) aktualisiert werden,
    # damit die neue Firmware auch früh verfügbar ist.
    - mkdir -p /target/lib/firmware
    - cp -a /lib/firmware/. /target/lib/firmware/
    - curtin in-target -- update-initramfs -u

    # ------------------------------------------------------------------------
    # 3. AUTOMATISCHE UPDATES DEAKTIVIEREN
    # ------------------------------------------------------------------------
    # Ubuntu bringt standardmäßig Dienste mit, die regelmäßig im Hintergrund nach Updates suchen und diese installieren.
    # Für einen Schulungsrechner kann das stören (Bandbreite, unerwartete Neustarts). Daher deaktivieren wir das.
    # Die Konfigurationsdatei /etc/apt/apt.conf.d/20auto-upgrades enthält zwei Zeilen, die von "1" auf "0" gesetzt werden.
    - curtin in-target -- sed -i 's/^APT::Periodic::Update-Package-Lists "1";/APT::Periodic::Update-Package-Lists "0";/' /etc/apt/apt.conf.d/20auto-upgrades || true
    - curtin in-target -- sed -i 's/^APT::Periodic::Unattended-Upgrade "1";/APT::Periodic::Unattended-Upgrade "0";/' /etc/apt/apt.conf.d/20auto-upgrades || true

    # ------------------------------------------------------------------------
    # 4. GRUB-BOOTPARAMETER ANPASSEN (split_lock_detect=off)
    # ------------------------------------------------------------------------
    # Auf manchen Dell-Hardware-Modellen (und anderen) kann es zu Leistungseinbrüchen kommen,
    # weil der Kernel standardmäßig "split lock detection" aktiviert hat.
    # Mit split_lock_detect=off wird dieses Feature deaktiviert und die Performance verbessert.
    # Der Befehl fügt die Option in die GRUB_CMDLINE_LINUX_DEFAULT Zeile ein.
    # Danach muss update-grub ausgeführt werden, um die Änderungen zu übernehmen.
    - curtin in-target -- sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT=".*"/GRUB_CMDLINE_LINUX_DEFAULT="split_lock_detect=off \1"/' /etc/default/grub
    - curtin in-target -- update-grub

    # ------------------------------------------------------------------------
    # 5. OH MY BASH GLOBAL INSTALLIEREN (FÜR ALLE BENUTZER)
    # ------------------------------------------------------------------------
    # Oh My Bash ist ein Framework zur Vereinfachung der Bash-Konfiguration.
    # Wenn es bereits im Live-System vorhanden ist (z.B. durch ein Cubic-Image),
    # wird es nach /etc/skel kopiert, sodass alle neu angelegten Benutzer es automatisch erhalten.
    # Zusätzlich wird es für den bestehenden adminuser direkt eingerichtet.
    - |
      curtin in-target -- bash -c '
      if [ -d /opt/oh-my-bash ]; then
        mkdir -p /etc/skel/.oh-my-bash
        cp -a /opt/oh-my-bash/. /etc/skel/.oh-my-bash/
        [ -f /etc/skel/.oh-my-bash/templates/bashrc.osh-template ] && cp /etc/skel/.oh-my-bash/templates/bashrc.osh-template /etc/skel/.bashrc
        # Für adminuser konfigurieren
        user_home="/home/adminuser"
        mkdir -p "$user_home/.oh-my-bash"
        cp -a /opt/oh-my-bash/. "$user_home/.oh-my-bash/"
        [ -f "$user_home/.oh-my-bash/templates/bashrc.osh-template" ] && cp "$user_home/.oh-my-bash/templates/bashrc.osh-template" "$user_home/.bashrc"
        chown -R adminuser:adminuser "$user_home/.oh-my-bash" "$user_home/.bashrc"
      fi
      '

    # ------------------------------------------------------------------------
    # 6. GNOME-EINSTELLUNGEN: PRIVATSPHÄRE, SITZUNG, BEGRÜSSUNGSBILDSCHIRM
    # ------------------------------------------------------------------------
    # Über dconf werden systemweite Voreinstellungen für GNOME festgelegt:
    # - remember-recent-files=false: Zuletzt verwendete Dateien werden nicht gespeichert.
    # - idle-delay=0: Bildschirm wird nicht automatisch gesperrt.
    # - disable-user-list=false: Benutzerliste am Login-Bildschirm wird angezeigt.
    # Zusätzlich wird für adminuser die Datei .config/gnome-initial-setup-done angelegt,
    # damit der Ersteinrichtungsassistent nicht startet.
    - |
      curtin in-target -- bash -c '
      mkdir -p /etc/dconf/db/local.d/
      printf "[org/gnome/desktop/privacy]\nremember-recent-files=false\n\n[org/gnome/desktop/session]\nidle-delay=uint32 0\n\n[org/gnome/login-screen]\ndisable-user-list=false\n" > /etc/dconf/db/local.d/00-labor-settings
      dconf update
      mkdir -p /home/adminuser/.config
      touch /home/adminuser/.config/gnome-initial-setup-done
      chown -R adminuser:adminuser /home/adminuser/.config
      '

    # ------------------------------------------------------------------------
    # 7. FIREWALL (UFW) EINRICHTEN
    # ------------------------------------------------------------------------
    # Die Firewall 'ufw' (Uncomplicated Firewall) wird aktiviert und grundlegend konfiguriert.
    # Erlaubt werden:
    # - Port 8080/tcp (z.B. für Entwicklungsserver)
    # - Port 2222/tcp (angepasster SSH-Port)
    # Standardmäßig werden alle anderen eingehenden Verbindungen blockiert.
    # Ausgehende Verbindungen sind erlaubt (default).
    - curtin in-target -- ufw allow 8080/tcp
    - curtin in-target -- ufw allow 2222/tcp
    - curtin in-target -- ufw default deny incoming
    - curtin in-target -- ufw --force enable

    # ------------------------------------------------------------------------
    # 8. VIRTUALISIERUNG (LIBVIRT) UND SYSTEMSTABILITÄT
    # ------------------------------------------------------------------------
    # Der adminuser wird den Gruppen libvirt und kvm hinzugefügt, um Virtualisierung nutzen zu können.
    # Die Dienste libvirtd und earlyoom werden aktiviert (falls vorhanden).
    # earlyoom beendet bei Speichermangel frühzeitig Prozesse, um das System reaktionsfähig zu halten.
    # Zudem wird die Swappiness auf 10 gesenkt, damit der Kernel weniger dazu neigt, auszulagern.
    - |
      curtin in-target -- bash -c '
      usermod -aG libvirt,kvm adminuser 2>/dev/null || true
      systemctl enable libvirtd earlyoom 2>/dev/null || true
      echo "vm.swappiness=10" > /etc/sysctl.d/99-swappiness.conf
      '

    # ------------------------------------------------------------------------
    # 9. GNOME-EXTENSIONEN GLOBAL VOREINSTELLEN
    # ------------------------------------------------------------------------
    # Über dconf werden bestimmte GNOME-Shell-Erweiterungen systemweit aktiviert.
    # Die Liste enthält nützliche Erweiterungen wie Tiling-Assistant, Emoji-Copy,
    # Grand Theft Focus, Ubuntu Dock, Desktop Icons (Ding) und mehr.
    # Die UUIDs müssen mit den installierten Erweiterungen übereinstimmen.
    - |
      curtin in-target -- bash -c '
      EXTS="['\''tiling-shell@ubuntu.com'\'', '\''emoji-copy@felipeftn'\'', '\''grand-theft-focus@zalckos.github.com'\'', '\''windowIsReady_Remover@nunofarruca@gmail.com'\'', '\''ubuntu-dock@ubuntu.com'\'', '\''ding@rastersoft.com'\'', '\''tiling-assistant@ubuntu.com'\'', '\''ubuntu-appindicators@ubuntu.com'\'']"
      printf "[org/gnome/shell]\nenabled-extensions=$EXTS\n" >> /etc/dconf/db/local.d/00-labor-settings
      dconf update
      '

    # ------------------------------------------------------------------------
    # 10. BLOATWARE ENTFERNEN UND SNAP VOLLSTÄNDIG DEAKTIVIEREN
    # ------------------------------------------------------------------------
    # Ubuntu liefert viele vorinstallierte Anwendungen mit, die wir nicht benötigen:
    # Firefox, Thunderbird, GNOME-Spiele, Medien-Apps (Shotwell, Totem, Rhythmbox, Cheese)
    # und den Ersteinrichtungsassistenten (gnome-initial-setup).
    # Diese werden mit apt purge entfernt.
    # Zusätzlich wird Snap komplett deaktiviert:
    # - Zuerst werden die Snap-Pakete Firefox und Thunderbird entfernt (falls als Snap installiert).
    # - Dann wird eine APT- Präferenzdatei erstellt, die snapd die Installation verweigert (Pin-Priority -1).
    # - Anschließend wird snapd selbst purgiert und alle zugehörigen Verzeichnisse gelöscht.
    # So bleibt das System schlank und frei von Snap-Zwang.
    - curtin in-target -- apt-get purge -y firefox thunderbird gnome-initial-setup aisleriot gnome-mahjongg gnome-mines gnome-sudoku shotwell totem rhythmbox cheese || true
    - curtin in-target -- snap remove firefox thunderbird 2>/dev/null || true
    - |
      curtin in-target -- bash -c 'cat <<EOF > /etc/apt/preferences.d/nosnap.pref
      Package: snapd
      Pin: release a=*
      Pin-Priority: -1
      EOF'
    - curtin in-target -- apt-get purge -y snapd
    - curtin in-target -- rm -rf /snap /var/snap /var/lib/snapd

    # ------------------------------------------------------------------------
    # 11. DAS TOOL: create-lab-user – BENUTZER FÜR UMSCHÜLER ANLEGEN
    # ------------------------------------------------------------------------
    # Dieses Skript wird nach /usr/local/bin/ installiert und steht nach der Installation
    # dem Administrator zur Verfügung. Es erlaubt, schnell und einheitlich neue Benutzer
    # für die Labore anzulegen. Der Benutzer bekommt:
    # - Mitgliedschaft in den Gruppen docker, libvirt, kvm
    # - Ein Home-Verzeichnis mit .bashrc (Oh My Bash kommt automatisch über /etc/skel)
    # - Git-Aliase (gs, ga, gc) werden in die .bashrc eingetragen
    # - Die Datei .config/gnome-initial-setup-done wird angelegt (kein Assistent)
    # - Das Passwort wird interaktiv während der Ausführung des Skripts vergeben.
    - |
      curtin in-target -- bash -c 'cat <<EOF > /usr/local/bin/create-lab-user
      #!/bin/bash
      if [ -z "$1" ]; then
        echo "Nutzung: sudo create-lab-user <benutzername>"
        exit 1
      fi
      NEW_USER=$1
      # User anlegen mit Gruppen
      useradd -m -s /bin/bash -G docker,libvirt,kvm $NEW_USER
      # Passwort interaktiv vergeben
      echo "Bitte Passwort für $NEW_USER setzen:"
      passwd $NEW_USER
      # GNOME Setup überspringen
      mkdir -p /home/$NEW_USER/.config
      touch /home/$NEW_USER/.config/gnome-initial-setup-done
      # Git Aliase
      echo "alias gs=\"git status\"" >> /home/$NEW_USER/.bashrc
      echo "alias ga=\"git add\"" >> /home/$NEW_USER/.bashrc
      echo "alias gc=\"git commit -m\"" >> /home/$NEW_USER/.bashrc
      chown -R $NEW_USER:$NEW_USER /home/$NEW_USER
      echo "--------------------------------------------------"
      echo "Benutzer $NEW_USER wurde erfolgreich eingerichtet!"
      echo "Gruppen: docker, libvirt, kvm"
      echo "Extras: Oh My Bash (via skel), Git Aliase, GNOME Setup Skip"
      echo "--------------------------------------------------"
      EOF
      chmod +x /usr/local/bin/create-lab-user'

    # ------------------------------------------------------------------------
    # 12. SPRACHE UND TASTATUR ENDGÜLTIG FESTSETZEN
    # ------------------------------------------------------------------------
    # Auch wenn locale und keyboard bereits zu Beginn konfiguriert wurden,
    # erzwingen wir hier noch einmal die deutschen Einstellungen.
    # Das Generieren des Locales, Setzen der System-Locale und Anpassen der
    # Tastaturkonfiguration (für die Konsole) stellt sicher, dass alles korrekt ist.
    - |
      curtin in-target -- bash -c '
      locale-gen de_DE.UTF-8
      update-locale LANG=de_DE.UTF-8 LANGUAGE="de_DE:de" LC_ALL=de_DE.UTF-8
      sed -i "s/XKBLAYOUT=.*/XKBLAYOUT=\"de\"/" /etc/default/keyboard
      setupcon
      '

    # ------------------------------------------------------------------------
    # 13. AUFRÄUMEN
    # ------------------------------------------------------------------------
    # Nach dem Entfernen vieler Pakete bleiben oft nicht mehr benötigte Abhängigkeiten übrig.
    # 'autoremove --purge' entfernt diese und löscht auch die Konfigurationsdateien.
    # 'clean' löscht heruntergeladene Paketdateien aus dem Cache – spart Platz.
    - curtin in-target -- apt-get autoremove --purge -y
    - curtin in-target -- apt-get clean