# LF4.2 (Teil B) – BSI-Grundschutz-Methodik: Schutzmaßnahmen & Betrieb

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 90–110 Minuten reines Lesen, +60–90 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
> **Teil:** 2 von 2 – Sichere Datenträger, TOM/Web-Sicherheit, Patch-Management, Incident Response (Teil A: Strukturanalyse, Physische Sicherheit, Schutzbedarf)
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Aktualitätshinweis:** Die **OWASP Top 10** wurden 2025 zum ersten Mal seit 2021 grundlegend überarbeitet – Abschnitt 2 bildet die neue Rangfolge ab. Bei **DIN 66399** gibt es Hinweise auf eine internationale Nachfolgenorm (ISO/IEC 21964); der genaue Geltungsstand ist vor einer verbindlichen Aussage anhand der offiziellen Quelle zu prüfen (Details siehe Abschnitt 1.3). Das aktuelle **NIST-Incident-Response-Modell** (SP 800-61 Rev. 3, April 2025) orientiert sich an den CSF-2.0-Funktionen – das hier verwendete Sechs-Phasen-Modell ist eine bewährte didaktische Vereinfachung, kein 1:1-Abbild des aktuellen NIST-Standards (Details siehe Abschnitt 4).

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Warum reicht einfaches Löschen nicht aus, und wie unterscheidet sich sicheres Löschen bei HDD und SSD? | [→ 1. Sichere Datenträger](#1-sichere-mobile-datenspeicher-und-rekonstruktionssicheres-löschen) |
| 2 | Was sind TOMs, wie sieht eine moderne Passwort-Richtlinie aus, und wie funktioniert eine SQL-Injection? | [→ 2. TOM & Web-Sicherheit](#2-technisch-organisatorische-maßnahmen-tom-und-web-sicherheit) |
| 3 | Wie läuft der Patch-Management-Prozess ab, und wie wird eine Schwachstelle per CVSS bewertet? | [→ 3. Patch-Management](#3-patch--und-schwachstellenmanagement) |
| 4 | Was sind die typischen Schritte im Incident Response, und welche gesetzlichen Meldepflichten gelten? | [→ 4. Incident Response](#4-der-notfallplan-incident-response) |

---

## 1. Sichere mobile Datenspeicher und rekonstruktionssicheres Löschen

> **Grundprinzip:** Einen Zettel in den Papierkorb zu werfen, entfernt ihn nicht aus der Welt – wer nachschaut, findet ihn wieder. Erst der Reißwolf macht ihn wirklich unlesbar. Digitales Löschen funktioniert im Kern genauso.

### 1.1 Vorgaben für mobile Datenträger

- **Verschlüsselungspflicht:** Mobile Datenträger (USB-Sticks, externe SSDs, Laptops) müssen standardmäßig stark verschlüsselt sein (z. B. BitLocker, LUKS, VeraCrypt).
- **Transportregelungen:** Physisch robuste, versiegelte Verpackung, Nachweisverfahren beim Versand (z. B. Einschreiben, Kuriertransport mit Identitätsprüfung).

### 1.2 Logisches Löschen vs. physisches Überschreiben

| Verfahren | Was passiert | Rekonstruierbar? | IHK-Relevanz |
| --- | --- | --- | --- |
| **Logisches Löschen** (Dateisystem-Ebene) | Nur der Verweis im Inhaltsverzeichnis (MFT/FAT) wird entfernt, Datenblöcke bleiben unberührt | Ja, mit einfachen Recovery-Tools | 🔴 |
| **Physisches Überschreiben (Wiping)** | Speicherzellen werden mit definierten Mustern überschrieben | Nein (bei korrekter Durchführung) | 🔴 |

**HDD vs. SSD:**

| Medium | Verfahren | Hinweis | IHK-Relevanz |
| --- | --- | --- | --- |
| **HDD (Magnetscheiben)** | Einmaliges vollständiges Überschreiben genügt bei moderner Datendichte | Historische 35-fach-Verfahren (Gutmann-Methode) sind bei heutigen HDDs nicht mehr notwendig | 🔴 |
| **SSD (Flash-Speicher)** | Geeignete, vom Hersteller bzw. der Schnittstelle unterstützte **Secure-Erase-/Sanitize-Verfahren** (z. B. ATA Secure Erase, NVMe Sanitize) verwenden statt einfachem Überschreiben; bei nicht vertrauenswürdig durchführbarer Löschung physische Vernichtung vorsehen | **Wear Leveling** verteilt Schreibvorgänge auf wechselnde physische Zellen, weshalb "dieselbe" logische Adresse nicht zuverlässig dieselbe physische Zelle überschreibt. Ein Secure-Erase-Befehl weist das Gerät an, die relevanten Bereiche nach Gerätespezifikation zu bereinigen – die tatsächliche Zuverlässigkeit hängt von Controller/Firmware-Implementierung ab | 🔴 |

**Krypto-Shredding** (Löschen des internen Verschlüsselungsschlüssels statt der Daten selbst) ist eine schnelle Alternative bei durchgängig verschlüsselt speichernden Laufwerken (SEDs) – funktioniert aber nur zuverlässig, wenn die relevanten Daten tatsächlich vollständig verschlüsselt gespeichert wurden, keine unverschlüsselten Kopien existieren und der Schlüssel selbst zuverlässig vernichtet wird.

### 1.3 Physische Vernichtung

Datenträger mit hohem/sehr hohem Schutzbedarf, die defekt oder ausgesondert sind (oder bei denen Secure-Erase-Verfahren nicht vertrauenswürdig durchführbar sind), werden physisch zerstört – Schreddern mit abgestuften Sicherheitsstufen oder Entmagnetisieren per Degausser. Die Datenträgervernichtung wird traditionell anhand der aus **DIN 66399** bekannten Schutzklassen und Sicherheitsstufen (H-1 bis H-7, mit definierten Partikelgrößen) beschrieben. Die passende Sicherheitsstufe richtet sich dabei nach Schutzbedarf, Informationsart und Datenträgertyp – eine pauschale Stufe lässt sich nicht allein aus "personenbezogene Daten" ableiten.

> **Hinweis zur Normung:** Es gibt Hinweise auf eine internationale Nachfolgenorm (ISO/IEC 21964) zu DIN 66399. Für die konkrete aktuelle Normbezeichnung und den Geltungsstand ist vor einer verbindlichen Aussage die jeweils gültige DIN-/ISO-Fassung zu prüfen – eine Gleichsetzung als vollständig "inhaltsgleich" sollte nur mit einem offiziellen Normnachweis erfolgen.

> **IHK-Typfrage:** *"Warum reicht bei einer auszusondernden SSD einfaches mehrfaches Überschreiben oft nicht aus, während es bei einer HDD funktioniert?"*
> **Musterantwort:** Eine SSD verwendet Wear Leveling: Der interne Controller verteilt Schreibvorgänge gezielt auf unterschiedliche physische Speicherzellen, um deren begrenzte Lebensdauer gleichmäßig auszunutzen. Ein Überschreibbefehl an eine logische Adresse landet deshalb nicht zuverlässig auf derselben physischen Zelle wie der ursprüngliche Schreibvorgang – alte Daten können in als "frei" markierten, aber physisch noch beschriebenen Zellen verbleiben. Eine HDD schreibt dagegen direkt auf feste physische Sektoren, weshalb ein vollständiges Überschreiben zuverlässig alle Daten ersetzt.

---

## 2. Technisch-Organisatorische Maßnahmen (TOM) und Web-Sicherheit

> **Grundprinzip:** Ein gutes Rezept braucht sowohl die richtigen Zutaten (Technik) als auch die richtige Vorgehensweise (Organisation) – fehlt eines von beidem, misslingt das Ergebnis, egal wie gut die andere Hälfte ist.

### 2.1 Technische vs. organisatorische Maßnahmen (Art. 32 DSGVO)

| Kategorie | Beispiele | IHK-Relevanz |
| --- | --- | --- |
| **Technische Maßnahmen** | Firewalls, Verschlüsselung, Backups, Netzwerk-Segmentierung, IPS/IDS | 🔴 |
| **Organisatorische Maßnahmen** | Passwort-Richtlinien, Notfallpläne, Security-Awareness-Schulungen, Zutrittsregelungen | 🔴 |

### 2.2 Moderne Authentifizierungs-Grundprinzipien (NIST SP 800-63B / BSI)

Veraltete Richtlinien (erzwungene 90-Tage-Rotation, komplexe Zeichenvorgaben) führten nachweislich zu vorhersagbaren Mustern (`Winter2026!` → `Fruehling2026!`) oder aufgeschriebenen Passwörtern.

| Prinzip | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Länge vor Komplexität** | Eine ausreichend lange, nicht leicht erratbare Passphrase (unzusammenhängende Wörter, keine naheliegenden persönlichen Informationen wie Geburtsdatum oder Wohnort) bietet meist mehr Sicherheit und Gebrauchstauglichkeit als ein kurzes Passwort mit vielen erzwungenen Sonderregeln | 🔴 |
| **Keine erzwungene Rotation** ohne konkreten Verdacht | Regelmäßiger Zwangswechsel ohne Anlass fördert schwache, vorhersagbare Muster | 🔴 |
| **MFA einsetzen** | Insbesondere externe, administrative und anderweitig schutzbedürftige Zugriffe sollten durch einen zweiten Faktor (z. B. FIDO2-Hardware-Token, Authenticator-App) geschützt werden. Ob MFA verpflichtend ist, ergibt sich aus Schutzbedarf, unternehmensinterner Sicherheitsrichtlinie und ggf. rechtlichen/vertraglichen Anforderungen – NIST/BSI empfehlen MFA nachdrücklich, schreiben es aber nicht als universelle Pflicht für jeden denkbaren Zugriff vor | 🔴 |

### 2.3 OWASP Top 10:2025 – Web Application Security

Die *OWASP Top 10* wurden 2025 zum ersten Mal seit 2021 grundlegend aktualisiert. Wichtigste Änderungen gegenüber 2021: **Security Misconfiguration** stieg von Platz 5 auf Platz 2, **Software Supply Chain Failures** ist neu auf Platz 3, SSRF wurde in Broken Access Control integriert, und **Injection** rutschte von Platz 3 auf Platz 5.

| Rang 2025 | Kategorie | IHK-Relevanz |
| --- | --- | --- |
| A01 | Broken Access Control (weiterhin Platz 1, jetzt inkl. SSRF) | 🔴 |
| A02 | Security Misconfiguration (aufgestiegen von Platz 5) | 🔴 |
| A03 | Software Supply Chain Failures (neu, Erweiterung von "Vulnerable and Outdated Components") | 🟡 |
| A04 | Cryptographic Failures (abgestiegen von Platz 2) | 🟡 |
| A05 | **Injection** (u. a. SQL-Injection) – abgestiegen von Platz 3 | 🔴 |
| A06 | Insecure Design | 🟡 |
| A07 | Authentication Failures | 🟡 |
| A08 | Software or Data Integrity Failures | 🟢 |
| A09 | Security Logging and Alerting Failures | 🟢 |
| A10 | Mishandling of Exceptional Conditions (neu) | 🟢 |

**SQL-Injection im Detail:** Der unsichere Code

```php
$sql = "SELECT * FROM accounts WHERE customer_id = '" . $_GET['id'] . "'";
```

kann durch die Eingabe `' OR '1'='1` so manipuliert werden, dass die Datenbank die Bedingung als immer wahr interpretiert:

```sql
SELECT * FROM accounts WHERE customer_id = '' OR '1'='1'
```

Das Ergebnis: Statt eines einzelnen Kundendatensatzes werden **alle** Datensätze der Tabelle zurückgegeben – der Filter wurde vollständig ausgehebelt.

**Gegenmaßnahme – "Never trust user input":** Prepared Statements (parametrisierte Abfragen) sind die zentrale technische Abwehr, bei der SQL-Befehlsstruktur und Nutzdaten strikt getrennt an die Datenbank übergeben werden – die Nutzdaten werden dadurch nie als ausführbarer SQL-Code interpretiert. Eingabevalidierung ist zusätzlich sinnvoll, ersetzt Prepared Statements aber nicht.

> **IHK-Typfrage:** *"Warum ist Injection in der OWASP Top 10:2025 auf Platz 5 statt wie 2021 auf Platz 3 – bedeutet das, SQL-Injection ist heute unwichtig?"*
> **Musterantwort:** Nein. Die Platzierung spiegelt die *relative* Häufigkeit/Kritikalität in den zugrunde liegenden Praxisdaten wider, nicht absolute Irrelevanz – Injection bleibt laut OWASP eine der am häufigsten getesteten Kategorien mit einer sehr großen Zahl zugeordneter CVEs. Der Rückgang erklärt sich eher dadurch, dass andere Kategorien (Security Misconfiguration, Supply-Chain-Risiken) relativ stärker zugenommen haben, nicht dadurch, dass Injection seltener vorkäme.

---

## 3. Patch- und Schwachstellenmanagement

> **Grundprinzip:** Ein Handwerker baut ein neues Werkzeug nicht ungetestet direkt in der laufenden Produktion ein – er prüft es erst in einer kontrollierten Umgebung, bevor es in den regulären Betrieb geht. Genauso funktioniert professionelles Patch-Management.

### 3.1 Der Schwachstellen-Lebenszyklus

```text
[ Entdeckung ] --> [ Zero-Day (aktiv ausgenutzt, kein Patch) ] --> [ CVE-Veröffentlichung ] --> [ Patch verfügbar ]
```

Eine **CVE-Nummer** (z. B. `CVE-2017-0144`) ist die eindeutige Kennung einer registrierten Schwachstelle, gelistet in globalen Datenbanken wie der NVD (National Vulnerability Database) des NIST.

### 3.2 CVSS – Common Vulnerability Scoring System

CVSS bewertet Schwachstellen auf einer Skala von 0,0 (unbedeutend) bis 10,0 (kritisch). Aktuell sind zwei Versionen parallel im Einsatz: **CVSS v3.1** (seit 2019, weiterhin der historische Anker vieler Datenbanken) und **CVSS v4.0** (seit November 2023, zunehmend Standard für neue Bewertungen) – in der Praxis werden je nach Quelle und Datensatz weiterhin beide Versionen angetroffen, die konkrete Bewertungsquelle und -version sollte deshalb immer geprüft werden.

> CVSS unterstützt die Priorisierung, ersetzt aber keine organisationsbezogene Risiko- und Betroffenheitsbewertung: Für die tatsächliche Patch-Priorität zählen zusätzlich die reale Erreichbarkeit des betroffenen Systems, vorhandene Schutzmaßnahmen, Exploit-Verfügbarkeit und die Kritikalität des betroffenen Geschäftsprozesses – ein hoher CVSS-Wert allein sagt noch nicht, wie dringend im eigenen Unternehmen gehandelt werden muss.

| Metrik | Bedeutung | Hinweis | IHK-Relevanz |
| --- | --- | --- | --- |
| **Attack Vector (AV)** | Von wo ist der Angriff möglich? (Netzwerk, Lokal, Physisch) | In v3.1 und v4.0 vorhanden | 🔴 |
| **Attack Complexity (AC)** | Wie schwer ist der Angriff durchzuführen? | In v3.1 und v4.0 vorhanden | 🔴 |
| **Attack Requirements (AT)** | Welche zusätzlichen Bedingungen müssen erfüllt sein? | **Neu in v4.0**, ergänzt die alte Attack-Complexity-Logik | 🟡 |
| **Privileges Required (PR)** | Welche Rechte benötigt der Angreifer vorab? | In v3.1 und v4.0 vorhanden | 🔴 |
| **User Interaction (UI)** | Muss ein Nutzer aktiv mitwirken? | v4.0 mit feineren Abstufungen als v3.1 | 🔴 |
| **Impact (C/I/A)** | Wie stark werden Vertraulichkeit, Integrität, Verfügbarkeit beeinträchtigt? | v4.0 trennt Auswirkungen auf das verwundbare System und auf nachgelagerte Systeme (kein "Scope" mehr wie in v3.1) | 🔴 |

> Scores aus unterschiedlichen CVSS-Versionen sollten nicht unkritisch direkt miteinander verglichen werden, da sich Metrik-Definitionen und Berechnung zwischen v3.1 und v4.0 unterscheiden. Für die Grundlagenprüfung reicht das Verständnis der Kernmetriken; welche exakte Version zugrunde liegt, wird in der Aufgabenstellung meist mitgeliefert.

### 3.3 Der Patch-Management-Prozess

| Schritt | Inhalt | IHK-Relevanz |
| --- | --- | --- |
| **1. Identifizieren** | Laufende Überwachung veröffentlichter Lücken für die eigene Software-Struktur | 🔴 |
| **2. Bewerten** | Einstufung von Relevanz/Dringlichkeit mittels CVSS | 🔴 |
| **3. Testen** | Patch in isolierter Staging-Umgebung prüfen | 🔴 |
| **4. Freigeben & Ausrollen** | Kontrolliertes Einspielen, möglichst in Wellen und mit Rückfallplan. Der Zeitpunkt richtet sich nach Dringlichkeit, Geschäftsrisiko und Wartungsfenster – oft außerhalb der Hauptgeschäftszeiten, bei aktiv ausgenutzten kritischen Schwachstellen kann aber ein beschleunigtes Notfallverfahren nötig sein | 🔴 |
| **5. Überwachen** | Kontrolle auf erfolgreiche Installation und Folgefehler | 🟡 |

> **IHK-Typfrage:** *"Warum wird ein sicherheitskritischer Patch nicht sofort auf alle Produktivsysteme gleichzeitig ausgerollt?"*
> **Musterantwort:** Ein ungetesteter Patch kann unvorhergesehene Inkompatibilitäten oder Abstürze verursachen. Ein gestaffelter Rollout (zunächst Staging-Umgebung, dann Wellen im Produktivsystem) begrenzt den möglichen Schaden auf einen kleinen Teil der Infrastruktur, falls der Patch doch Probleme verursacht – ein Totalausfall aller Systeme gleichzeitig wird vermieden.

---

## 4. Der Notfallplan (Incident Response)

> **Grundprinzip:** Eine Feuerwehr improvisiert im Ernstfall nicht – sie folgt einem eingeübten Ablauf, der lange vor dem eigentlichen Brand feststeht. Incident Response funktioniert nach demselben Muster: Der Plan muss stehen, bevor der Vorfall eintritt.

### 4.1 Ein vereinfachtes Incident-Response-Ablaufmodell

Für Unterricht und Prüfung lässt sich Incident Response in sechs gut merkbare Schritte gliedern:

| Phase | Ziel | IHK-Relevanz |
| --- | --- | --- |
| **1. Vorbereitung** | Notfallpläne, Alarmketten, Teamschulung – *vor* einem Angriff | 🔴 |
| **2. Identifikation** | Anomalie erkennen und bestätigen, dass es sich um einen echten Vorfall handelt | 🔴 |
| **3. Eindämmung** | Schaden sofort begrenzen (z. B. Netzwerk-Isolierung betroffener Systeme) | 🔴 |
| **4. Beseitigung** | Ursache identifizieren, Schadsoftware/Lücke vollständig entfernen | 🔴 |
| **5. Wiederherstellung** | Kontrollierter Wiederaufbau aus sauberen, geprüften Backups | 🔴 |
| **6. Lessons Learned** | Vorfall analysieren, Sicherheitskonzept anpassen | 🟡 |

> **Aktualitätshinweis:** Dieses Sechs-Phasen-Modell fasst verbreitete, bewährte Vorgehensweisen didaktisch zusammen. Es ist **nicht identisch** mit dem aktuellen NIST-Modell: NIST SP 800-61 Rev. 3 (April 2025) hat die frühere Vier-Phasen-Struktur abgelöst und ordnet Incident Response stattdessen den sechs **CSF-2.0-Funktionen** zu: Govern, Identify, Protect, Detect, Respond, Recover. Eindämmung und Beseitigung sind dort Tätigkeiten innerhalb von "Respond", Lessons Learned wird als kontinuierliche Verbesserung verstanden. NIST lässt ausdrücklich auch andere geeignete Ablaufmodelle wie das hier gezeigte zu – für die Grundlagenprüfung ist das Sechs-Phasen-Modell weiterhin eine gültige und verbreitete Darstellung.

### 4.2 Sofortmaßnahmen bei Ransomware-Verdacht

- **System sofort isolieren:** Netzwerkverbindungen trennen – Netzwerkkabel ziehen, WLAN deaktivieren.
- **Nicht eigenmächtig herunterfahren:** Ein Ausschalten kann flüchtige forensische Spuren im Arbeitsspeicher (RAM) vernichten (z. B. Verschlüsselungsschlüssel, laufende Angreifer-Prozesse). Ein Weiterbetrieb kann jedoch ebenfalls zusätzlichen Schaden verursachen (weitere Verschlüsselung, Datenexfiltration, Ausbreitung auf andere Systeme). **Ob das System eingeschaltet bleibt, kontrolliert heruntergefahren oder sofort abgeschaltet wird, ist eine lageabhängige Entscheidung des Incident-Response- bzw. Forensikteams** – keine pauschale Regel.
- **Meldung an das Incident-Response-Team** über einen separaten Kommunikationskanal (z. B. Telefon statt E-Mail, falls das Mailsystem selbst betroffen sein könnte).

### 4.3 Meldepflicht nach Art. 33 DSGVO

Eine Verletzung des Schutzes personenbezogener Daten (z. B. Abfluss von Kundendaten) ist **unverzüglich und möglichst binnen 72 Stunden** nach Bekanntwerden an die zuständige Datenschutzaufsichtsbehörde zu melden – es sei denn, sie führt voraussichtlich nicht zu einem Risiko für die Rechte und Freiheiten natürlicher Personen. Die 72 Stunden sind dabei kein Zeitraum, der grundsätzlich ausgeschöpft werden darf: Die Meldung muss unverzüglich erfolgen, spätestens jedoch nach 72 Stunden.

> **IHK-Typfrage:** *"Warum sollte ein infizierter Rechner im Ransomware-Verdachtsfall nicht eigenmächtig heruntergefahren werden, ohne dass es dabei eine absolute Regel gibt?"*
> **Musterantwort:** Beim Herunterfahren wird der flüchtige Arbeitsspeicher (RAM) gelöscht – dort können wichtige forensische Spuren liegen (z. B. der Verschlüsselungsschlüssel der Ransomware, laufende Angreifer-Prozesse, Netzwerkverbindungen). Diese Informationen gehen dann unwiederbringlich verloren. Gleichzeitig kann ein weiterlaufendes System aber auch aktiv Schaden anrichten – etwa weiter verschlüsseln, Daten exfiltrieren oder sich im Netzwerk ausbreiten. Da beide Optionen Risiken bergen, entscheidet das Incident-Response- bzw. Forensikteam situationsabhängig, nicht nach einer starren Vorgabe. Unstrittig und immer sinnvoll ist dagegen die sofortige Netzwerk-Isolierung.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Mehrfaches Überschreiben funktioniert bei SSDs genauso zuverlässig wie bei HDDs | Wear Leveling verhindert, dass Überschreibbefehle zuverlässig dieselben physischen Zellen treffen – SSDs sollten geeignete, herstellerseitig unterstützte Secure-Erase-/Sanitize-Verfahren verwenden, bei nicht vertrauenswürdiger Durchführung physisch vernichten |
| 2 | Erzwungene, regelmäßige Passwort-Rotation ist immer eine gute Sicherheitsmaßnahme | Moderne NIST/BSI-Richtlinien empfehlen Länge statt Rotation ohne Anlass – erzwungener Wechsel fördert vorhersagbare, schwächere Muster |
| 3 | MFA ist laut NIST/BSI für jeden Zugriff ausnahmslos zwingend vorgeschrieben | MFA wird nachdrücklich empfohlen, insbesondere für externe/administrative Zugriffe – die konkrete Verpflichtung ergibt sich aus Schutzbedarf und Unternehmensrichtlinie, nicht aus einer universellen Pflicht für jeden denkbaren Fall |
| 4 | SQL-Injection ist nach OWASP Top 10:2025 kein wichtiges Thema mehr, weil auf Platz 5 statt 3 | Die Platzierung ist relativ zu anderen Kategorien, nicht absolut – Injection bleibt eine der am häufigsten ausgenutzten und geprüften Schwachstellenklassen |
| 5 | Patches sollten möglichst sofort auf allen Systemen gleichzeitig eingespielt werden | Ein gestaffelter Rollout (Test → Wellen) begrenzt das Risiko unvorhergesehener Inkompatibilitäten |
| 6 | Bei Ransomware-Verdacht sollte der PC immer sofort ausgeschaltet werden | Zuerst konsequent isolieren (Netzwerk trennen); ob das System dann eingeschaltet bleibt oder abgeschaltet wird, entscheidet das Incident-Response-Team lageabhängig – RAM-Spuren können sonst verloren gehen |
| 7 | Die "6 Phasen des Incident Response" sind identisch mit dem aktuellen NIST-Standard | Das Sechs-Phasen-Modell ist eine bewährte didaktische Vereinfachung; das aktuelle NIST SP 800-61 Rev. 3 (2025) ordnet Incident Response den CSF-2.0-Funktionen (Govern, Identify, Protect, Detect, Respond, Recover) zu |
| 8 | Eine meldepflichtige Datenpanne darf grundsätzlich erst nach vollen 72 Stunden gemeldet werden | Die Meldung muss unverzüglich erfolgen – 72 Stunden sind die Obergrenze, kein auszuschöpfender Zeitraum |

---

## 6. Deep-Dive-Ausblick (freiwillig)

- **CVSS-Kalkulator in der Praxis** (→ Abschnitt 3.2): Wie ein konkreter CVSS-Score mit dem offiziellen FIRST-Kalkulator (v3.1 oder v4.0) hergeleitet und jede Metrik-Entscheidung begründet wird.
- **Aktueller Normstand der Datenträgervernichtung** (→ Abschnitt 1.3): Welche DIN-/ISO-Fassung aktuell gilt, und wie die Schutzklassen/Sicherheitsstufen (H-1 bis H-7) konkret den drei BSI-Schutzbedarfskategorien zugeordnet werden.
- **NIST CSF 2.0 im Detail** (→ Abschnitt 4.1): Wie die sechs Funktionen Govern/Identify/Protect/Detect/Respond/Recover zusammenspielen und sich vom hier gezeigten Sechs-Phasen-Modell unterscheiden.
- **Business Continuity Planning** (→ Abschnitt 4): Wie kritische Geschäftsprozesse bei einem mehrtägigen IT-Totalausfall über analoge Notverfahren aufrechterhalten werden können.
- **OWASP-Steckbriefe A06–A10** (→ Abschnitt 2.3): Vertiefung der in der Haupttabelle nur kurz genannten, niedriger priorisierten OWASP-Kategorien.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Warum reicht Formatieren nicht zum sicheren Löschen? | Es entfernt nur den Dateisystem-Verweis, die Daten bleiben auf den Speicherzellen erhalten |
| 2 | Was ist der Unterschied zwischen Secure-Erase-Verfahren und einfachem Überschreiben bei SSDs? | Secure-Erase-Verfahren weisen das Gerät an, auch nicht direkt sichtbare Bereiche (inkl. Wear-Leveling-Reserveblöcke) nach Gerätespezifikation zu bereinigen – einfaches Überschreiben erreicht das nicht zuverlässig |
| 3 | Welche Norm regelt traditionell die Sicherheitsstufen bei der Datenträgervernichtung, und was ist beim aktuellen Normstatus zu beachten? | DIN 66399 (Stufen H-1 bis H-7); es gibt Hinweise auf eine internationale Nachfolgenorm (ISO/IEC 21964) – der genaue Geltungsstand ist vor einer verbindlichen Aussage zu prüfen |
| 4 | Was ist laut NIST SP 800-63B wichtiger als Passwort-Rotation? | Ausreichende Passwortlänge (Passphrase) |
| 5 | Auf welchem Platz steht "Injection" in der OWASP Top 10:2025? | Platz 5 (A05) – 2021 noch Platz 3 |
| 6 | Was schützt vor SQL-Injection wirksam? | Prepared Statements (parametrisierte Abfragen), die SQL-Struktur und Nutzdaten strikt trennen |
| 7 | Was bedeutet ein hoher CVSS-Wert? | Eine besonders kritische Schwachstelle (Skala 0,0 bis 10,0) |
| 8 | Welche CVSS-v4.0-Metrik gibt es in v3.1 noch nicht? | Attack Requirements (AT) |
| 9 | Nenne die 6 Phasen des hier verwendeten Incident-Response-Modells. | Vorbereitung, Identifikation, Eindämmung, Beseitigung, Wiederherstellung, Lessons Learned |
| 10 | Welche sechs Funktionen nutzt das aktuelle NIST CSF 2.0 stattdessen? | Govern, Identify, Protect, Detect, Respond, Recover |
| 11 | Innerhalb welcher Frist muss eine meldepflichtige Datenpanne an die Aufsichtsbehörde gemeldet werden? | Unverzüglich und, soweit möglich, spätestens binnen 72 Stunden nach Bekanntwerden – keine Meldung nötig, wenn voraussichtlich kein Risiko für die Rechte und Freiheiten natürlicher Personen besteht (Art. 33 DSGVO) |

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **Wear Leveling** | SSD-Mechanismus, der Schreibvorgänge auf wechselnde Zellen verteilt – erschwert einfaches Überschreiben |
| **Krypto-Shredding** | Löschen des Verschlüsselungsschlüssels statt der Daten – schnell, aber nur bei durchgängiger Verschlüsselung zuverlässig |
| **Datenträgervernichtung** | Schutzklassen/Sicherheitsstufen traditionell nach DIN 66399 (H-1 bis H-7); Hinweise auf internationale Nachfolgenorm ISO/IEC 21964, Geltungsstand vor Zitat prüfen. Stufenwahl abhängig von Schutzbedarf, Informationsart und Datenträgertyp |
| **Prepared Statement** | Parametrisierte SQL-Abfrage, trennt Befehlsstruktur strikt von Nutzdaten – Schutz vor Injection |
| **CVE** | Eindeutige Kennung einer registrierten Sicherheitslücke |
| **CVSS** | Bewertungssystem für Schwachstellen (0,0–10,0), aktuell v3.1 und v4.0 parallel im Einsatz |
| **Attack Requirements (AT)** | Neue CVSS-v4.0-Metrik für zusätzliche Angriffsbedingungen |
| **CSF 2.0** | Aktuelles NIST-Funktionsmodell: Govern, Identify, Protect, Detect, Respond, Recover |
| **72-Stunden-Frist** | Gesetzlicher spätester Meldezeitpunkt für Datenpannen, sofern erforderlich und praktisch einhaltbar – Meldung muss unverzüglich erfolgen, keine Ausschöpfungsfrist (Art. 33 DSGVO) |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Löschverfahren-Auswahl | "Welches Löschverfahren empfehlen Sie für Datenträger X?" | Bezug auf Medientyp (HDD/SSD) UND Schutzbedarfskategorie, nicht pauschal "überschreiben" |
| Sicherheitslücken-Analyse | "Erklären Sie den SQL-Injection-Angriff auf diesen Code" | Konkreten manipulierten Eingabewert nennen und die resultierende SQL-Logik erklären |
| Prozessfrage | "Beschreiben Sie den Ablauf bei einem Ransomware-Vorfall" | Konkrete Phasenreihenfolge und Sofortmaßnahmen nennen, dabei "isolieren" von "lageabhängig entscheiden" trennen – nicht pauschal "sofort ausschalten" |
| Rechtsfrage | "Wann muss eine Datenpanne gemeldet werden?" | "Unverzüglich, spätestens binnen 72 Stunden" – nicht "erst nach 72 Stunden" |

---

## 10. Merksätze für das Fachgespräch

> Löschen ist nicht gleich Löschen: Der Papierkorb entfernt den Verweis, nicht den Inhalt – erst Überschreiben oder Zerstören macht Daten wirklich weg.

> Länge schlägt Komplexität, und ein Passwort ohne Grund zu wechseln bringt niemandem Sicherheit – moderne Richtlinien setzen auf Passphrasen statt auf Zwangsrotation.

> Eine Rangliste wie die OWASP Top 10 zeigt Relevanz im Vergleich, nicht absolute Wichtigkeit – Platz 5 heißt nicht "unwichtig".

> Bei Ransomware-Verdacht ist nur eines unstrittig: sofort isolieren. Ob ausschalten oder nicht, entscheidet die Lage, nicht eine starre Regel.

> 72 Stunden sind die Obergrenze, keine Wartezeit – eine Meldung erfolgt unverzüglich, nicht erst am letzten möglichen Tag.

---

```yaml
dokument: LF4.2B-wiki-artikel
lernfeld: LF4.2
teil: "2 von 2 (B: Sichere Datenträger, TOM/Web-Sicherheit, Patch-Management, Incident Response)"
titel: "BSI-Grundschutz-Methodik: Schutzmaßnahmen & Betrieb"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-08
quellen_intern:
  - "LF4.2.4: Sichere mobile Datenspeicher & rekonstruktionssicheres Löschen.md"
  - "LF4.2.5: Technisch-Organisatorische Maßnahmen (TOM) & OWASP Top 10.md"
  - "LF4.2.6: Patch- & Schwachstellenmanagement.md"
  - "LF4.2.7: Der Notfallplan (Incident Response).md"
quellen_fachlich:
  - titel: "OWASP Top 10:2025"
    herausgeber: "OWASP Foundation"
    status: "2025 veröffentlicht, erste Aktualisierung seit 2021. WICHTIG: Rohmaterial bezog sich noch auf die 2021er-Rangfolge (Injection = A03); im Artikel auf 2025er-Rangfolge korrigiert (Injection = A05), Tabelle auf alle 10 Kategorien vervollständigt"
  - titel: "CVSS v3.1 / v4.0"
    herausgeber: "FIRST.org"
    status: "v4.0 seit November 2023 veröffentlicht (u. a. neue Metrik Attack Requirements, kein Scope mehr), v3.1 (2019) bleibt parallel im Einsatz"
  - titel: "NIST SP 800-63B (Digital Identity Guidelines)"
    herausgeber: "NIST"
    status: "aktuelle Passwort-Richtlinie: Länge vor Komplexität, keine anlasslose Zwangsrotation; MFA als starke Empfehlung, nicht als universelle Pflicht dargestellt"
  - titel: "NIST SP 800-61 Rev. 3 (Incident Response Recommendations)"
    herausgeber: "NIST"
    status: "seit April 2025 aktuell, ordnet Incident Response den CSF-2.0-Funktionen zu (Govern/Identify/Protect/Detect/Respond/Recover) statt der älteren Vier-Phasen-Struktur; hier verwendetes Sechs-Phasen-Modell explizit als didaktische Vereinfachung gekennzeichnet, nicht als deckungsgleiches NIST-Modell"
  - titel: "DIN 66399 (Vernichtung von Datenträgern) / mögliche Nachfolgenorm ISO/IEC 21964"
    herausgeber: "DIN / ISO/IEC"
    status: "Stufenlogik H-1 bis H-7 nach DIN 66399 verwendet; Hinweise auf internationale Nachfolgenorm ISO/IEC 21964 liegen vor, aber KEIN im Artikel verifizierter Primärnachweis für vollständige Ablösung/Inhaltsgleichheit – vor verbindlicher Aussage offizielle DIN-/ISO-Quelle prüfen"
  - titel: "Art. 33 DSGVO (Meldepflicht Datenpannen)"
    herausgeber: "Europäische Union"
    status: "unverändert in Kraft; Meldung 'unverzüglich, spätestens binnen 72 Stunden' – keine Ausschöpfungsfrist"
review_historie:
  - runde: 1
    datum: 2026-09-08
    ergebnis: "Ursprünglich Teil eines gemeinsamen LF4.2-Artikels (7 Unterkapitel). Externe Review (3 Reviews) ergab: Artikel zu lang – auf Nutzerwunsch in Teil A und Teil B (dieser Artikel) aufgeteilt. Dabei mehrere echte Fachkorrekturen aus der gründlichsten Review (mit Zitaten aus NIST SP 800-61 Rev. 3, DSGVO-Volltext, OWASP-Vollliste) übernommen: 'Niemals herunterfahren' bei Ransomware-Verdacht war zu absolut – jetzt als lageabhängige Entscheidung des IR-Teams dargestellt; 'Incident Response nach BSI/NIST' überzeichnete die Aktualität – jetzt explizit als didaktische Vereinfachung gekennzeichnet, mit Verweis auf das tatsächliche aktuelle NIST-CSF-2.0-Modell; 'MFA zwingend' relativiert (starke Empfehlung statt universelle Pflicht); OWASP-Tabelle von 4 auf alle 10 Kategorien vervollständigt; SQL-Injection-Beispiel korrigiert (vorheriges Beispiel prüfte kein Passwort, obwohl das behauptet wurde – jetzt konsistentes Beispiel mit Datensatz-Filter-Umgehung); DSGVO-Formulierung auf 'unverzüglich, spätestens binnen 72 Stunden' präzisiert; CVSS-v4.0-Unterschiede (Attack Requirements, kein Scope mehr) ergänzt. HINWEIS: Ein in dieser Runde zunächst übernommener, unbelegter Hinweis auf eine DIN-66399→ISO/IEC-21964-Ablösung wurde in Runde 3 zurückgenommen, da kein Primärnachweis vorlag (siehe Runde 3). Markdown-Fehler, die eine Review meldete, beim Abgleich mit der tatsächlichen Datei nicht bestätigt – nicht übernommen."
  - runde: 2
    datum: 2026-09-08
    ergebnis: "Externe Prüfung (4 Reviews) eingearbeitet, gewichtet nach Quellenqualität. Wichtigster Fund: Die in Runde 1 übernommene DIN-66399/ISO-21964-Aussage war selbst nicht mit einer Primärquelle belegt – auf 'Hinweise auf eine Nachfolgenorm, vor verbindlicher Aussage prüfen' zurückgenommen, ebenso die pauschale 'H-4 für Festplatten mit personenbezogenen Daten'-Empfehlung entfernt (Stufenwahl hängt von Schutzbedarf/Informationsart/Datenträgertyp ab, nicht pauschal vom Datentyp). Weitere Präzisierungen: Secure-Erase-Aussage von 'adressiert alle Zellen' auf 'weist Gerät an, nach Spezifikation zu bereinigen – Zuverlässigkeit hängt von Implementierung ab' abgeschwächt; unbelegte NVD-Parallelveröffentlichungs-Aussage entfernt, dafür CVSS-Priorisierungsgrenze ergänzt (CVSS ersetzt keine Betroffenheitsbewertung); Patch-Rollout-Zeitpunkt um Notfall-Ausnahme bei aktiv ausgenutzten Lücken ergänzt; DSGVO-Selbsttestantwort und Cheatsheet um die Risikoausnahme aus Art. 33 DSGVO ergänzt (fehlte trotz korrekter Hauptformulierung im Fließtext); Passphrase-Empfehlung um Zufälligkeits-/Vorhersagbarkeitsvorbehalt ergänzt (eine erdachte Passphrase wie 'Sommer Urlaub Hamburg' kann schwach sein)"
  - runde: 3
    datum: 2026-09-08
    ergebnis: "Externe Prüfung (3 Reviews) zeigte: Die in Runde 2 vorsichtig formulierte DIN-66399/ISO-21964-Aussage war nur im Haupttext (Abschnitt 1.3) konsequent umgesetzt, an fünf weiteren Stellen (Aktualitätshinweis, Deep-Dive, Selbsttest, Cheatsheet, YAML quellen_fachlich/review_historie) stand noch die alte, zu bestimmte Formulierung ('abgelöst', 'inhaltsgleich', 'Stufenlogik übernommen'). Alle sechs Stellen jetzt konsistent auf die vorsichtige Fassung gebracht. Teil-Kennzeichnung im Frontmatter (Teil A/B) klarer formuliert – beschreibt jetzt den eigenen statt nur den anderen Teil, um Missverständnisse zu vermeiden. Übrige Punkte (OWASP-Tabellenkopf, NIST-Ablaufmodell-Formulierung, kleinere Stilkorrekturen) als nicht-blockierende Kosmetik eingestuft und nicht in dieser Runde bearbeitet."
  - runde: 4
    datum: 2026-09-08
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): gesamte Datei durchgelesen, kleines Blockquote-Spacing-Problem in Abschnitt 1.3 behoben (fehlende Leerzeile vor 'Hinweis zur Normung'), Konsistenz aller Kernaussagen (DIN 66399/ISO 21964, Ransomware-Lageabhängigkeit, NIST-CSF-2.0-Abgrenzung, DSGVO-Risikoausnahme) über Haupttext/Selbsttest/Cheatsheet/YAML bestätigt. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Reviews + 1 eigene Abschlussprüfung, 2026-09-08) – Freigabe durch Autor:in bestätigt"
```