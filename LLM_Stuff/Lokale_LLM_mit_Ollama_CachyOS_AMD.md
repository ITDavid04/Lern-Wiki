# 🧠 Deep Dive: Lokale LLMs mit Ollama auf CachyOS (AMD Hardware)

> **Lernziel:** Verstehen, wie man Large Language Models lokal betreibt — unabhängig von Cloud-Diensten — und welche Hardware-Voraussetzungen dabei entscheidend sind.
>
> **Zielgruppe:** IT-Umschüler (FIAE/FISI), Einsteiger in KI-Infrastruktur
>
> **IHK-Relevanz:** LF7 (Vernetzte IT-Systeme), LF12 (IT-Sicherheit & Datenschutz — lokale Datenverarbeitung), Grundlagen KI-gestützte Systeme

---

## 📚 Inhaltsverzeichnis

1. [Was ist Ollama?](#was-ist-ollama)
2. [Warum lokale LLMs?](#warum-lokale-llms)
3. [Hardware-Grundlagen für LLM-Inferenz](#hardware-grundlagen)
4. [AMD GPU + ROCm — die Herausforderung](#amd-rocm)
5. [Vulkan als Alternative](#vulkan-alternative)
6. [Modellauswahl nach VRAM](#modellauswahl)
7. [Installation auf CachyOS](#installation)
8. [Open WebUI als Frontend](#open-webui)
9. [Praxisbeispiel: Typisches Setup](#praxisbeispiel)
10. [Glossar](#glossar)

---

## 🤖 Was ist Ollama? {#was-ist-ollama}

**Ollama** ist ein Open-Source-Tool, das das lokale Ausführen von Large Language Models (LLMs) stark vereinfacht. Es funktioniert ähnlich wie Docker — man „pullt" ein Modell und führt es lokal aus, ohne Cloud-Verbindung.

```bash
# Prinzip: ähnlich wie Docker
ollama pull llama3.2     # Modell herunterladen
ollama run llama3.2      # Modell starten
```

Ollama startet einen lokalen HTTP-Server (`localhost:11434`), über den Anwendungen per API auf das Modell zugreifen können — kompatibel mit der OpenAI-API.

> 💡 **Merksatz:** Ollama = „Docker für KI-Modelle"

---

## 🔒 Warum lokale LLMs? {#warum-lokale-llms}

| Aspekt | Cloud-LLM (z.B. ChatGPT) | Lokales LLM |
|---|---|---|
| **Datenschutz** | Daten verlassen das Gerät | Daten bleiben lokal ✅ |
| **Kosten** | Abomodell / API-Kosten | Einmalige Hardware ✅ |
| **Verfügbarkeit** | Internetzugang nötig | Offline nutzbar ✅ |
| **Kontrolle** | Modell vom Anbieter | Eigenes Modell wählbar ✅ |
| **Geschwindigkeit** | Abhängig vom Netz | Direkt auf Hardware |
| **Modellgröße** | Unbegrenzt (Serverseite) | Durch RAM/VRAM begrenzt ⚠️ |

> 🎓 **IHK-relevant:** DSGVO-Konformität — sensible Daten (Kundendaten, interne Dokumente) dürfen nicht unkontrolliert an externe KI-Dienste übertragen werden. Lokale LLMs lösen dieses Problem strukturell.

---

## ⚙️ Hardware-Grundlagen für LLM-Inferenz {#hardware-grundlagen}

### Die drei entscheidenden Ressourcen

```
┌─────────────────────────────────────────────────────┐
│  LLM-Inferenz braucht vor allem:                    │
│                                                     │
│  1. VRAM (GPU-Speicher)  → schnellste Inferenz      │
│  2. RAM (Arbeitsspeicher) → CPU-Fallback, langsamer │
│  3. CPU-Kerne             → Parallelisierung        │
└─────────────────────────────────────────────────────┘
```

### Warum ist VRAM so wichtig?

Ein LLM-Modell muss vollständig in den Speicher geladen werden. Die Modellgröße hängt von zwei Faktoren ab:

- **Parameteranzahl** (z.B. 7B = 7 Milliarden Parameter)
- **Quantisierung** (wie viele Bits pro Parameter)

**Faustformel für den Speicherbedarf:**

```
Speicher (GB) ≈ Parameter (B) × Bits_pro_Parameter / 8
```

| Modell | Quantisierung | Speicherbedarf |
|---|---|---|
| 7B | Q4 (4-Bit) | ~4 GB |
| 7B | Q8 (8-Bit) | ~8 GB |
| 13B | Q4 | ~8 GB |
| 70B | Q4 | ~40 GB |

> ⚠️ **Wichtig:** Passt das Modell nicht vollständig in den VRAM, werden Teile in den RAM ausgelagert (*Offloading*). Das ist möglich, aber deutlich langsamer.

---

## 🔴 AMD GPU + ROCm — die Herausforderung {#amd-rocm}

### Was ist ROCm?

**ROCm** (Radeon Open Compute) ist AMDs Open-Source-Pendant zu NVIDIAs CUDA — die Software-Schicht, die GPU-beschleunigtes Rechnen ermöglicht.

```
NVIDIA: Hardware → CUDA → LLM-Framework
AMD:    Hardware → ROCm → LLM-Framework
```

### Offiziell unterstützte AMD-Architekturen (2026)

| Architektur | Beispiel-GPUs | ROCm-Support |
|---|---|---|
| RDNA4 | RX 9000er | ✅ Offiziell |
| RDNA3 | RX 7000er | ✅ Offiziell |
| RDNA2 | RX 6000er | ⚠️ Community |
| **RDNA1** | **RX 5700 XT** | ⚠️ Workaround nötig |

### Der Workaround für RDNA1 (gfx1010)

Die RX 5700 XT verwendet die GPU-Architektur `gfx1010`. ROCm kennt diese nicht nativ, kann aber überlistet werden:

```bash
# Umgebungsvariable setzen — ROCm denkt, es wäre eine neuere GPU
export HSA_OVERRIDE_GFX_VERSION=10.3.0
```

Diese Variable wird persistent in der Ollama systemd-Unit gesetzt:

```ini
# /etc/systemd/system/ollama.service.d/rocm-override.conf
[Service]
Environment=HSA_OVERRIDE_GFX_VERSION=10.3.0
```

> ⚠️ **Praxishinweis:** Dieser Workaround funktioniert, ist aber nicht offiziell supported. Abstürze bei bestimmten Modellen sind möglich.

---

## 🌋 Vulkan als Alternative {#vulkan-alternative}

**Vulkan** ist eine plattformübergreifende Grafik- und Compute-API, die breiter unterstützt wird als ROCm. Für LLM-Inferenz ist Vulkan oft die zuverlässigere Wahl bei älteren AMD-GPUs.

### ROCm vs. Vulkan im Vergleich

| Kriterium | ROCm | Vulkan |
|---|---|---|
| **Kompatibilität** | Nur neuere AMD-GPUs | Fast alle GPUs |
| **Performance** | Höher (nativ) | Etwas geringer |
| **Stabilität (5700 XT)** | Workaround nötig | Stabil ✅ |
| **Einrichtungsaufwand** | Hoch | Gering |

### Installation auf CachyOS (Arch-basiert)

```bash
# Option A: Vulkan-Backend (empfohlen für ältere AMD-GPUs)
yay -S ollama-vulkan

# Option B: ROCm-Backend (mit manuellem Workaround)
yay -S ollama-rocm
```

> 💡 **Empfehlung für RX 5700 XT:** Mit `ollama-vulkan` starten — stabil, keine Workarounds, gute Performance.

---

## 📦 Modellauswahl nach VRAM {#modellauswahl}

### Für 8 GB VRAM (RX 5700 XT)

| Modell | Quantisierung | VRAM | Einsatzgebiet |
|---|---|---|---|
| Llama 3.2 8B | Q4_K_M | ~5 GB | Allgemein, Chat ✅ |
| Mistral 7B | Q4_K_M | ~4 GB | Allgemein, Code ✅ |
| Qwen 2.5 7B | Q4_K_M | ~5 GB | Code, Mehrsprachig ✅ |
| DeepSeek Coder 6.7B | Q4 | ~4 GB | Code-Fokus ✅ |
| Llama 3.1 8B | Q8 | ~8 GB | Höhere Qualität ⚠️ |
| Llama 3 70B | Q4 | ~40 GB | ❌ Zu groß für VRAM |

### Mit 32 GB RAM (CPU-Fallback)

Modelle, die nicht in den VRAM passen, können im RAM laufen — langsamer, aber möglich:

| Szenario | Geschwindigkeit |
|---|---|
| Modell vollständig im VRAM | ~20–40 Token/s |
| Modell vollständig im RAM (CPU) | ~3–8 Token/s |
| Teilweise VRAM, Rest RAM | ~10–20 Token/s |

---

## 🛠️ Installation auf CachyOS {#installation}

### Schritt 1: Ollama installieren

```bash
# Vulkan-Variante (empfohlen für RX 5700 XT)
yay -S ollama-vulkan

# Dienst aktivieren und starten
sudo systemctl enable --now ollama
```

### Schritt 2: Erstes Modell laden

```bash
# Kleines, schnelles Modell zum Testen
ollama pull llama3.2

# Interaktiver Chat direkt im Terminal
ollama run llama3.2
```

### Schritt 3: GPU-Nutzung prüfen

```bash
# AMD GPU-Monitoring
rocm-smi

# Oder allgemeiner:
watch -n 1 rocm-smi

# Ollama-Logs prüfen (sollte GPU-Layer-Meldung zeigen)
journalctl -u ollama -f
```

### Schritt 4 (Optional): ROCm-Workaround für RX 5700 XT

```bash
# Drop-in für systemd erstellen
sudo mkdir -p /etc/systemd/system/ollama.service.d

sudo tee /etc/systemd/system/ollama.service.d/rocm-override.conf << 'EOF'
[Service]
Environment=HSA_OVERRIDE_GFX_VERSION=10.3.0
EOF

sudo systemctl daemon-reload
sudo systemctl restart ollama
```

---

## 🖥️ Open WebUI als Frontend {#open-webui}

**Open WebUI** ist ein selbst gehostetes Web-Interface für Ollama — ähnlich wie ChatGPT, aber lokal.

### Installation via Docker

```bash
# Docker installieren (falls nicht vorhanden)
yay -S docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# Open WebUI starten
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

Danach erreichbar unter: **http://localhost:3000**

### Alternative: yay (Arch-Paket)

```bash
yay -S open-webui
sudo systemctl enable --now open-webui
```

---

## 🏗️ Praxisbeispiel: Typisches Setup {#praxisbeispiel}

```
┌─────────────────────────────────────────┐
│           Benutzer (Browser)            │
│         http://localhost:3000           │
└────────────────┬────────────────────────┘
                 │ HTTP
┌────────────────▼────────────────────────┐
│            Open WebUI                   │
│     (Chat-Interface, lokal gehostet)    │
└────────────────┬────────────────────────┘
                 │ REST API
┌────────────────▼────────────────────────┐
│         Ollama (localhost:11434)        │
│    Modell-Management & Inferenz-Engine  │
└────────────────┬────────────────────────┘
                 │ Vulkan / ROCm
┌────────────────▼────────────────────────┐
│         AMD RX 5700 XT (8 GB)          │
│    GPU-beschleunigte Inferenz           │
│    + 32 GB RAM als Fallback             │
└─────────────────────────────────────────┘
```

### Empfohlene Modelle für den Einstieg

```bash
ollama pull llama3.2        # Allgemein, Chat
ollama pull mistral         # Code, Analyse
ollama pull qwen2.5-coder   # Code-Fokus
```

---

## 📖 Glossar {#glossar}

| Begriff | Erklärung |
|---|---|
| **LLM** | Large Language Model — großes Sprachmodell |
| **Inferenz** | Das Ausführen / Berechnen eines KI-Modells (nicht Training) |
| **VRAM** | Video RAM — Speicher direkt auf der GPU |
| **Quantisierung** | Reduzierung der Bit-Tiefe von Modellgewichten (weniger Speicher, etwas weniger Qualität) |
| **Q4_K_M** | 4-Bit-Quantisierung mit mittlerer Qualitätsstufe — guter Kompromiss |
| **ROCm** | AMDs Open-Source Compute-Plattform (Pendant zu NVIDIAs CUDA) |
| **Vulkan** | Plattformübergreifende GPU-API, breite Hardware-Kompatibilität |
| **gfx1010** | Interne GPU-Architekturbezeichnung der RX 5700 XT (RDNA1) |
| **Offloading** | Teile des Modells in den RAM auslagern, wenn VRAM nicht reicht |
| **Token** | Grundeinheit der Textverarbeitung in LLMs (~¾ eines Worts) |
| **Token/s** | Geschwindigkeitsmaß: Tokens pro Sekunde bei der Textgenerierung |
| **Open WebUI** | Selbst gehostetes Web-Frontend für Ollama |

---

> 📝 **Weiterführende Quellen:**
> - [Ollama Dokumentation](https://github.com/ollama/ollama)
> - [Open WebUI GitHub](https://github.com/open-webui/open-webui)
> - [ROCm AMD GPU-Kompatibilitätsliste](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)
> - [Ollama Modell-Library](https://ollama.com/library)

---

*Erstellt für das IT-Umschulungs-Wiki | Stand: Juni 2026*