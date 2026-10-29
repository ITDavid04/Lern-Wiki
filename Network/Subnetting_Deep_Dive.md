# Subnetting

## 1. Einleitung

Subnetting ist die Aufteilung eines IP-Netzwerks in mehrere kleinere logische Teilnetze. Man braucht es immer dann, wenn ein großer Adressraum sinnvoll strukturiert werden soll – etwa um Abteilungen, Standorte oder Sicherheitszonen technisch zu trennen, statt allen Geräten dieselbe flache Broadcast Domain zuzumuten.

---

## 2. Einfache Erklärung (Analogie)

Stell dir ein großes, zusammenhängendes Grundstück vor – vergleichbar mit einer Gärtnerei-Fläche von einem Hektar. Ohne Parzellierung gehört die gesamte Fläche einer einzigen Nutzung: Jeder Weg, jede Bewässerungsleitung betrifft das ganze Grundstück.

Subnetting ist wie das Aufteilen dieser Fläche in klar vermessene Parzellen:

- Das **Gesamtgrundstück** entspricht dem übergeordneten IP-Netz (z. B. `192.168.1.0/24`).
- Die **Parzellengrenze** entspricht der Subnetzmaske – sie legt fest, wie viel Fläche (wie viele Hostadressen) jede Parzelle bekommt.
- Jede **Parzelle** ist ein eigenes Subnetz mit eigener Zufahrt (Gateway) und eigener Grundstücksadresse (Netzadresse).
- Zwei benachbarte Parzellen kommunizieren nicht direkt über den Zaun, sondern über den Hof-Eingang (Router) – genau wie zwei Subnetze nur über einen Router miteinander sprechen.

Genauso wie ein Gärtner nicht jedem Kunden das ganze Grundstück gibt, sondern klar bemessene Parzellen zuteilt, teilt ein Netzwerkadministrator den Adressraum in exakt bemessene Subnetze auf.

---

## 3. Voraussetzungen / Wann anwenden?

Subnetting-Rechnungen setzen voraus:

- Grundverständnis der **IPv4-Adressstruktur** (32 Bit, vier Oktette).
- Sicherheit im **Umrechnen zwischen Dezimal und Binär** (mindestens für ein Oktett).
- Verständnis von **Netzanteil vs. Hostanteil** einer Adresse.
- Kenntnis der **CIDR-Schreibweise** (`/24`, `/26` usw.).

**Anwenden, wenn:**

- ein vorhandenes Netz in mehrere gleich große Teilnetze aufgeteilt werden soll,
- für ein Subnetz eine bestimmte Mindest-Hostanzahl gefordert ist,
- zu einer gegebenen IP-Adresse und Maske Netz- und Broadcastadresse gesucht werden,
- ein größerer IPv6-Block in mehrere `/64`-Subnetze unterteilt werden soll.

---

## 4. Schritt-für-Schritt-Rezept

**Rezept A – Subnetzmaske aus Hostanforderung ableiten:**

1. Geforderte Hostanzahl notieren.
2. Kleinstes $n$ finden, für das gilt: $2^n - 2 \geq H$ (mit $H$ = geforderte Hostanzahl). $n$ = Anzahl Hostbits.
3. Netzbits berechnen: $32 - n$ (IPv4) → ergibt das Präfix (z. B. `/26`).
4. Präfix in Dotted-Decimal-Maske umrechnen.

**Rezept B – Ein Netz in $k$ gleich große Subnetze aufteilen:**

1. Anzahl benötigter Subnetz-Bits $s$ bestimmen: kleinstes $s$ mit $2^s \geq k$.
2. Neues Präfix = altes Präfix $+ s$.
3. Blockgröße berechnen: $2^{(32 - p)}$ (mit $p$ = neues Präfix).
4. Subnetze der Reihe nach auflisten, jeweils um die Blockgröße im relevanten Oktett weiterzählen.
5. Pro Subnetz: erste Adresse = Netzadresse, letzte Adresse = Broadcastadresse, dazwischen = nutzbare Hosts.

**Rezept C – Netz- und Broadcastadresse zu gegebener IP + Maske finden:**

1. IP-Adresse und Maske in Binär umwandeln (mindestens das betroffene Oktett).
2. Bitweises UND aus IP und Maske → Netzadresse.
3. Hostanteil komplett auf 1 setzen → Broadcastadresse.
4. Hostbereich = Netzadresse + 1 bis Broadcastadresse − 1.

---

## 5. Praktische Aufgaben

> Erst selbst rechnen, dann mit Abschnitt 8 vergleichen.

**Aufgabe 1:** Wie viele nutzbare Hostadressen passen in ein `/28`-Netz?

**Aufgabe 2:** Teile `192.168.10.0/24` in 8 gleich große Subnetze auf. Bestimme Netzadresse, Broadcastadresse und Hostbereich des **dritten** Subnetzes.

**Aufgabe 3:** Ein Serverraum-Subnetz soll mindestens 100 Hosts aufnehmen können. Welches Präfix (CIDR) wird mindestens benötigt, und wie lautet die zugehörige Dotted-Decimal-Maske?

**Aufgabe 4:** Gegeben ist die IP-Adresse `172.16.50.130` mit der Maske `255.255.255.192` (`/26`). Bestimme Netzadresse, Broadcastadresse und gültigen Hostbereich.

**Aufgabe 5 (IPv6):** Ein Unternehmen erhält den Block `2001:db8:abcd::/48`. Wie viele `/64`-Subnetze lassen sich daraus bilden?

---

## 6. Sidefacts mit IHK-Relevanz

**ROT** – Formel für nutzbare Hosts: $2^h - 2$ (mit $h$ = Anzahl Hostbits). Die „−2" steht für Netz- und Broadcastadresse, die nie als Hostadresse vergeben werden.

**ROT** – Ein VLAN entspricht in der Praxis meist genau einem Subnetz; die Broadcastdomäne bleibt dadurch auf das jeweilige Subnetz begrenzt.

**ROT** – Router bzw. Layer-3-Switches vermitteln zwischen Subnetzen; Subnetting selbst ist ein Layer-3-Konzept.

**GELB** – Bei IPv6 gibt es keine separate Broadcastadresse mehr; die Funktion wird durch Multicast-Adressen ersetzt. Die „−2"-Formel gilt dort nicht.

**GELB** – Für IPv6 wird standardmäßig ein `/64`-Präfix pro Subnetz verwendet, unabhängig von der tatsächlichen Hostzahl – Adresseffizienz ist hier kein Thema.

**GRÜN** – VLSM (Variable Length Subnet Masking) erlaubt unterschiedlich große Subnetze innerhalb desselben Netzes, statt überall gleich große Blöcke zu verwenden.

**GRÜN** – Die historische Einteilung in Class A/B/C-Netze ist durch CIDR weitgehend abgelöst worden, taucht aber gelegentlich als Kontextwissen auf.

---

## 7. Typische Fehler / Prüfungsfallen

**ROT** – Die „−2" bei der Hostberechnung vergessen und Netz- oder Broadcastadresse fälschlich als nutzbare Hostadresse mitzählen.

**ROT** – Hostbits und Netzbits verwechseln, z. B. bei `/26` fälschlich mit 26 Hostbits statt 6 Hostbits rechnen.

**GELB** – Die Blockgröße falsch berechnen und dadurch Subnetzgrenzen verschieben (führt zu überlappenden oder falsch nummerierten Subnetzen).

**GELB** – Bei IPv6-Aufgaben reflexhaft nach einer Broadcastadresse suchen, obwohl IPv6 diese nicht kennt.

**GRÜN** – Bei Aufgaben zur Subnetzanzahl das $2^s \geq k$ mit $2^s = k$ verwechseln und dadurch bei ungeraden Subnetzanzahlen falsch runden.

---

## 8. Lösungen

**Lösung 1:**  
`/28` → Hostbits $= 32 - 28 = 4$.  
Nutzbare Hosts: $2^4 - 2 = 16 - 2 = 14$.

**Lösung 2:**  
Ausgangsnetz `/24` → 8 Hostbits. Für 8 Subnetze: $2^s \geq 8$ → $s = 3$.  
Neues Präfix: $24 + 3 = 27$. Blockgröße: $2^{32-27} = 2^5 = 32$.

Die Subnetze im vierten Oktett zählen jeweils in 32er-Schritten:

| Subnetz | Netzadresse | Broadcastadresse | Hostbereich |
|---|---|---|---|
| 1 | 192.168.10.0 | 192.168.10.31 | .1 – .30 |
| 2 | 192.168.10.32 | 192.168.10.63 | .33 – .62 |
| **3** | **192.168.10.64** | **192.168.10.95** | **.65 – .94** |

→ Drittes Subnetz: Netzadresse `192.168.10.64`, Broadcastadresse `192.168.10.95`, Hostbereich `192.168.10.65` – `192.168.10.94`.

**Lösung 3:**  
Gesucht: kleinstes $n$ mit $2^n - 2 \geq 100$.  
$2^6 - 2 = 62$ → zu wenig. $2^7 - 2 = 126$ → ausreichend. Also $n = 7$ Hostbits.  
Präfix: $32 - 7 = 25$ → `/25`.  
Dotted-Decimal-Maske für `/25`: `255.255.255.128`.

**Lösung 4:**  
`/26` → Hostbits = 6, Blockgröße im letzten Oktett = $2^6 = 64$.  
`.130` liegt im Block `128–191` (zweiter `/26`-Block ab 128).  
Netzadresse: `172.16.50.128`.  
Broadcastadresse: `172.16.50.191`.  
Hostbereich: `172.16.50.129` – `172.16.50.190`.

**Lösung 5:**  
`/48` → `/64`: Differenz = $64 - 48 = 16$ Bit stehen für Subnetze zur Verfügung.  
Anzahl möglicher `/64`-Subnetze: $2^{16} = 65.536$.

---

```yaml
titel: Subnetting
lernfeld: Netzwerktechnik-Grundlagen / IP-Adressierung
typ: B
ihk_relevanz: hoch
letzte_pruefung: 2026
verwandte_artikel:
  - Broadcast Domain
  - VLAN
  - OSI-Modell
  - IPv6-Adressierung
```
Bonus
Quelle Youtube: https://www.youtube.com/watch?v=s_Ntt6eTn94 /Subnet Mask Explained
                https://www.youtube.com/watch?v=3jLTvJDbc2Q /Subnetting in 4 Min
                https://www.youtube.com/watch?v=bWVrqReifJ8 /Osi Modell
