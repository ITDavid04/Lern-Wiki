# 🛠️ Workaround: Verschwundenes WLAN/LAN bei Lenovo ThinkPads unter Ubuntu

## Problem

Nach einem Kernel-Update oder nach dem Aufwachen aus dem Standby kann es bei manchen Lenovo ThinkPads vorkommen, dass WLAN- oder LAN-Hardware nicht mehr erkannt wird.

Häufig betroffen sind beispielsweise:

- Intel-WLAN-Adapter wie der **AX211**
- Intel-Ethernet-Adapter wie der **I219-LM**

Mögliche Ursachen sind Probleme mit:

- PCIe-Power-Management
- ACPI
- Geräte-Firmware
- Kernel- oder Treiber-Regressionen
- Zuständen nach Suspend/Resume

Das folgende Skript führt einen PCIe-Rescan durch und versucht anschließend, die ausgewählten Intel-Netzwerktreiber neu zu laden.

> **Hinweis:** Dies ist ein Workaround und keine Garantie für die Wiederherstellung der Hardware. Bestehende Netzwerkverbindungen werden unterbrochen. Führe das Skript daher möglichst direkt am Gerät und nicht über eine SSH-Verbindung aus.

> **Achtung:** Sollte das Skript beim Entladen eines Treibers vollständig einfrieren, liegt möglicherweise ein Kernel- oder Hardware-Deadlock vor. In diesem seltenen Fall kann ein erzwungenes Ausschalten über den Power-Button erforderlich sein. Nicht gespeicherte Daten können dabei verloren gehen.

---

## 1. Skript anlegen

Erstelle eine Datei für das lokale Administrationsskript:

```bash
sudo nano /usr/local/bin/fix-network
```

Füge den folgenden Code vollständig ein und speichere ihn in Nano mit **Strg+O**, **Enter** und **Strg+X**:

```bash
#!/usr/bin/env bash
# /usr/local/bin/fix-network
# Führt einen PCIe-Rescan durch und lädt ausgewählte Intel-Netzwerktreiber neu.

set -u

if [[ ${EUID} -ne 0 ]]; then
    echo "Fehler: Bitte mit sudo ausführen." >&2
    exit 1
fi

restart_networkmanager() {
    echo "Starte NetworkManager ..."

    if systemctl restart NetworkManager; then
        echo "  ✓ NetworkManager gestartet"
        return 0
    else
        echo "  ⚠ NetworkManager konnte nicht gestartet werden." >&2
        return 1
    fi
}

# NetworkManager auch bei einem vorzeitigen Abbruch wieder starten.
trap restart_networkmanager EXIT

echo "=== [1/4] Ausgangszustand ==="
echo

lspci -nnk | grep -A3 -Ei 'network|ethernet' || true

echo
echo "=== [2/4] Netzwerkverwaltung anhalten ==="

systemctl stop NetworkManager 2>/dev/null || true

echo "Entlade Intel-Netzwerktreiber ..."

if modprobe -r --wait=6000 iwlmvm 2>/dev/null; then
    echo "  ✓ iwlmvm entladen"
else
    echo "  - iwlmvm nicht geladen oder konnte nicht entladen werden"
fi

if modprobe -r --wait=6000 iwlwifi 2>/dev/null; then
    echo "  ✓ iwlwifi entladen"
else
    echo "  - iwlwifi nicht geladen oder konnte nicht entladen werden"
fi

if modprobe -r --wait=6000 e1000e 2>/dev/null; then
    echo "  ✓ e1000e entladen"
else
    echo "  - e1000e nicht geladen oder konnte nicht entladen werden"
fi

echo
echo "=== [3/4] PCIe-Rescan und Treiber laden ==="

if [[ -w /sys/bus/pci/rescan ]]; then
    echo "Führe PCIe-Rescan durch ..."
    echo 1 > /sys/bus/pci/rescan
    sleep 2
else
    echo "⚠ PCIe-Rescan ist auf diesem System nicht verfügbar." >&2
fi

if modprobe iwlwifi 2>/dev/null; then
    echo "  ✓ iwlwifi geladen"
else
    echo "  - iwlwifi konnte nicht geladen werden"
fi

if modprobe e1000e 2>/dev/null; then
    echo "  ✓ e1000e geladen"
else
    echo "  - e1000e konnte nicht geladen werden"
fi

rfkill unblock wlan 2>/dev/null || true

# NetworkManager vor dem Status-Check explizit starten.
if ! restart_networkmanager; then
    echo "Abbruch: NetworkManager ist nicht verfügbar." >&2
    exit 1
fi

# Das EXIT-Trap ist jetzt nicht mehr erforderlich.
trap - EXIT

echo
echo "Warte auf die Netzwerkverwaltung ..."

for _ in {1..10}; do
    if nmcli -t -f STATE general >/dev/null 2>&1; then
        break
    fi
    sleep 1
done

echo
echo "=== [4/4] Status-Check ==="

wlan_found=0
lan_found=0

for interface in /sys/class/net/*; do
    [[ -e "$interface" ]] || continue

    name=${interface##*/}

    if [[ -d "$interface/wireless" ]]; then
        echo "✓ WLAN-Schnittstelle gefunden: $name"
        wlan_found=1
        continue
    fi

    driver_link=$(readlink -f "$interface/device/driver" 2>/dev/null || true)
    driver_name=${driver_link##*/}

    if [[ "$driver_name" == "e1000e" ]]; then
        echo "✓ Intel-LAN-Schnittstelle gefunden: $name"
        lan_found=1
    fi
done

echo

if (( wlan_found && lan_found )); then
    echo "WLAN und Intel-LAN wurden erkannt."
    exit 0
elif (( wlan_found )); then
    echo "⚠ WLAN wurde erkannt, Intel-LAN jedoch nicht."
    exit 2
elif (( lan_found )); then
    echo "⚠ Intel-LAN wurde erkannt, WLAN jedoch nicht."
    exit 2
fi

echo "⚠ Es wurde weder eine WLAN- noch eine Intel-LAN-Schnittstelle erkannt."
echo
echo "Letzte relevante Kernelmeldungen:"

journalctl -k -b --no-pager |
    grep -Ei \
        'iwlwifi|iwlmvm|e1000e|firmware|PCI|PCIe|AER|ACPI|D3cold|timeout|error' |
    tail -n 30 || true

echo
echo "Empfohlene nächste Schritte:"
echo "  1. Laptop vollständig herunterfahren."
echo "  2. Netzteil und gegebenenfalls Dockingstation trennen."
echo "  3. Etwa 30 Sekunden warten und das Gerät wieder einschalten."
echo "  4. Falls das Problem nach einem Kernel-Update begann,"
echo "     testweise einen älteren Kernel über GRUB starten."
echo "  5. BIOS/UEFI- und Ubuntu-Updates prüfen."

exit 1
```

---

## 2. Skript ausführbar machen

Setze die Ausführungsrechte:

```bash
sudo chmod 755 /usr/local/bin/fix-network
```

Optional kannst du die Bash-Syntax prüfen:

```bash
bash -n /usr/local/bin/fix-network
```

---

## 🚀 Anwendung

Wenn WLAN oder LAN verschwunden ist, führe das Skript direkt am ThinkPad aus:

```bash
sudo fix-network
```

Das Skript:

1. zeigt den aktuellen Hardwarezustand,
2. stoppt NetworkManager,
3. entlädt ausgewählte Intel-Netzwerktreiber,
4. führt einen PCIe-Rescan durch,
5. lädt die Treiber erneut,
6. hebt eine WLAN-Sperre auf,
7. startet NetworkManager,
8. wartet auf die Netzwerkverwaltung,
9. prüft WLAN und Intel-LAN getrennt.

---

## 🩺 Erweiterte Diagnose

### PCI-Geräte und zugeordnete Treiber prüfen

```bash
lspci -nnk | grep -A3 -Ei 'network|ethernet'
```

### Netzwerkschnittstellen anzeigen

```bash
ip -br link
```

### WLAN-Sperren prüfen

```bash
rfkill list
```

### Geladene Intel-Netzwerkmodule prüfen

```bash
lsmod | grep -E 'iwlwifi|iwlmvm|e1000e'
```

### Relevante Kernelmeldungen anzeigen

```bash
journalctl -k -b --no-pager |
    grep -Ei \
        'iwlwifi|iwlmvm|e1000e|firmware|PCI|PCIe|AER|ACPI|D3cold|timeout|error'
```

### Aktuell verwendeten Kernel anzeigen

```bash
uname -r
```

---

## Firmware und Initramfs

Meldet das Kernel-Log eine fehlende Firmwaredatei, kann das Paket `linux-firmware` neu installiert werden:

```bash
sudo apt update
sudo apt install --reinstall linux-firmware
```

Anschließend kann das Initramfs für den aktuell gestarteten Kernel aktualisiert werden:

```bash
sudo update-initramfs -u -k "$(uname -r)"
```

Danach sollte das System neu gestartet werden:

```bash
sudo reboot
```

> **Wichtig:** `update-initramfs` repariert kein PCIe-Gerät, das nach dem Standby verschwunden ist. Der Befehl hilft hauptsächlich bei fehlenden Firmwaredateien oder beschädigten Initramfs-Dateien.

---

## Rückgabecodes

Das Skript verwendet folgende Rückgabecodes:

| Code | Bedeutung |
|---:|---|
| `0` | WLAN und Intel-LAN wurden erkannt |
| `1` | Keine passende Schnittstelle erkannt oder NetworkManager konnte nicht gestartet werden |
| `2` | Nur WLAN oder nur Intel-LAN wurde erkannt |

> Die Erkennung des kabelgebundenen Netzwerks berücksichtigt in diesem Skript ausschließlich Schnittstellen, die den Treiber `e1000e` verwenden. USB-LAN-Adapter oder bestimmte Dockingstationen können daher unberücksichtigt bleiben.
````