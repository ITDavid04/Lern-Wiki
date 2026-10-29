# LF4.1 – Grundlagen der Informationssicherheit & Gefahrenlandschaft

> **Zielgruppe:** Umschüler FIAE/FISI, 2. Lehrjahr
> **Prüfungsrelevanz:** Grundlagen für AP1 (schriftlich), Transferfragen in AP2 und Fachgespräch möglich
> **Lernzeit:** Ca. 100–130 Minuten reines Lesen, +70–100 Minuten mit Aufgaben – abhängig von Vorkenntnissen und Bearbeitungstiefe
> **Status:** Final
> **Stand:** 2026
>
> Die 🔴/🟡/🟢-Markierungen in diesem Artikel sind eine didaktische Einschätzung zur Prüfungsvorbereitung, keine offizielle IHK-Gewichtung.
>
> **Wichtiger Aktualitätshinweis:** Der deutsche Rechtsrahmen für IT-Sicherheit hat sich zum 6. Dezember 2025 grundlegend geändert (NIS2-Umsetzungsgesetz, BSIG-Novelle). Dieser Artikel bildet den Stand nach dieser Reform ab – ältere Lernmaterialien, die noch von "IT-Sicherheitsgesetz 2.0" und der klassischen KRITIS-Struktur ausgehen, sind in Teilen veraltet (Details siehe Abschnitt 2).

---

## IHK-Kernfragen dieses Artikels

| # | Frage | Abschnitt |
| --- | --- | --- |
| 1 | Was sind die drei CIA-Schutzziele, und wie kann die Verletzung eines Ziels kaskadierend andere Ziele gefährden? | [→ 1. CIA-Triade](#1-die-cia-triade-die-drei-schutzziele) |
| 2 | Was unterscheidet gesetzliche Pflichten von freiwilligen Normen, und wer ist heute von NIS2/BSIG-neu betroffen? | [→ 2. Rechtlicher Rahmen](#2-rechtlicher-und-normativer-rahmen-compliance) |
| 3 | Wie unterscheiden sich Gefährdung, Schwachstelle und Risiko, und wie klassifiziert STRIDE Bedrohungen? | [→ 3. Gefährdungen & Risiko](#3-gefährdungen-schwachstellen-risiko-und-stride) |
| 4 | Wie hängen Datenleak, Identitätsdiebstahl und Doxing ursächlich zusammen? | [→ 4. Moderne Angriffsmuster](#4-moderne-angriffsmuster-und-digitale-identität) |
| 5 | Was sind SEO-Poisoning und Botnetze, und wie schützt man digitale Identitäten wirksam? | [→ 4. Moderne Angriffsmuster](#4-moderne-angriffsmuster-und-digitale-identität) |

---

## 1. Die CIA-Triade: Die drei Schutzziele

> **Grundprinzip:** Ein Tresor mit einem versiegelten Brief schützt nur, wenn drei Dinge gleichzeitig stimmen – niemand Unbefugtes kommt heran (Vertraulichkeit), der Inhalt bleibt unverändert (Integrität), und der Berechtigte kann ihn öffnen, wann er will (Verfügbarkeit). Fehlt eine dieser drei Eigenschaften, ist der Tresor wertlos.

### 1.1 Die drei Säulen

| Schutzziel | Bedeutung | Typische IT-Maßnahme | IHK-Relevanz |
| --- | --- | --- | --- |
| **Vertraulichkeit (Confidentiality)** | Daten sind nur für autorisierte Personen zugänglich | Verschlüsselung (symmetrisch/asymmetrisch), Zugriffsrechte (ACLs) | 🔴 |
| **Integrität (Integrity)** | Daten sind korrekt, vollständig und unmanipuliert; Änderungen sind nachvollziehbar | Kryptografische Prüfsummen (Hashing), digitale Signaturen | 🔴 |
| **Verfügbarkeit (Availability)** | Systeme und Daten sind für Berechtigte zum geforderten Zeitpunkt nutzbar | Redundante Netzanbindungen, USV, RAID-Systeme | 🔴 |

> Manche Rahmenwerke ergänzen die klassische CIA-Triade um weitere Schutzziele wie **Authentizität** (Echtheit des Urhebers) oder **Verbindlichkeit/Nichtabstreitbarkeit** (Non-Repudiation) – im STRIDE-Modell (Abschnitt 3) tauchen diese als eigene Bedrohungskategorien wieder auf. Für die Grundlagenprüfung bleibt CIA der zentrale Ausgangspunkt.

### 1.2 Kaskadierende Effekte

Der Verlust eines einzigen Schutzziels kann weitere Schutzziele mit sich reißen – ein Domino-Effekt, kein isoliertes Einzelproblem:

```text
[ Stromausfall ] --(kein USV)--> [ Verlust Verfügbarkeit ]
        |
        v (unvollständiger Schreibvorgang)
[ Verlust Integrität ] --(korrupte Datenbank)--> [ Systemabsturz ]
```

Ein anderes Beispiel: Ein unbemerkt eingeschleuster Admin-Account (Verletzung der **Integrität** des Active Directory) kann im nächsten Schritt Zugriff auf vertrauliche Personalakten ermöglichen (Verletzung der **Vertraulichkeit**).

> **IHK-Typfrage:** *"Erklären Sie an einem Beispiel, wie die Verletzung eines Schutzziels ein anderes gefährden kann."*
> **Musterantwort:** Ein erfolgreicher Ransomware-Angriff verschlüsselt zunächst Dateien – das verletzt primär die **Verfügbarkeit** (Daten sind nicht mehr nutzbar). Werden vor der Verschlüsselung zusätzlich Daten exfiltriert ("Double Extortion"), ist zugleich die **Vertraulichkeit** verletzt. Wird bei der Wiederherstellung aus einem veralteten oder manipulierten Backup zurückgespielt, kann zusätzlich die **Integrität** der wiederhergestellten Daten fraglich sein. Ein einzelner Vorfall kann also mehrere Schutzziele gleichzeitig oder nacheinander treffen.

---

## 2. Rechtlicher und normativer Rahmen (Compliance)

> **Grundprinzip:** Ein Gesetz ist wie eine Bauvorschrift – wer sie missachtet, riskiert Bußgeld und Baustopp. Eine Norm ist wie eine freiwillige Gütesiegel-Zertifizierung – niemand zwingt dazu, aber sie schafft Vertrauen und kann in Ausschreibungen den Unterschied machen.

### 2.1 Gesetze vs. Normen

| Kategorie | Verbindlichkeit | Beispiele |
| --- | --- | --- |
| **Gesetze** | Verpflichtend, Verstöße sind bußgeld- bzw. haftungsbewehrt | DSGVO, BSIG (novelliert) |
| **Normen/Standards** | Freiwillig, schaffen aber oft faktischen Druck (Kunden, Ausschreibungen, Versicherungen) | ISO/IEC 27001, BSI IT-Grundschutz |

### 2.2 DSGVO (Datenschutz-Grundverordnung)

Regelt EU-weit den Schutz personenbezogener Daten. Zentrale Artikel:

| Artikel | Inhalt | IHK-Relevanz |
| --- | --- | --- |
| **Art. 5** | Grundsätze der Verarbeitung (Rechtmäßigkeit, Zweckbindung, Datenminimierung, Richtigkeit, Speicherbegrenzung, Integrität/Vertraulichkeit) | 🔴 |
| **Art. 17** | Recht auf Löschung ("Recht auf Vergessenwerden") | 🔴 |
| **Art. 32** | Sicherheit der Verarbeitung durch technisch-organisatorische Maßnahmen (TOMs), orientiert am "Stand der Technik" | 🔴 |

Verstöße können mit Bußgeldern bis zu **20 Mio. € oder 4 % des weltweiten Jahresumsatzes** geahndet werden – es gilt jeweils der höhere Betrag.

### 2.3 BSIG-neu / NIS2-Umsetzungsgesetz (Stand: aktuell gültige Rechtslage)

> **Was sich geändert hat:** Bis Ende 2025 regelte das BSI-Gesetz in der Fassung des "IT-Sicherheitsgesetzes 2.0" (2021) im Kern die klassischen **KRITIS**-Betreiber (Energie, Wasser, Gesundheit etc.), rund 4.500 Unternehmen. Mit dem **NIS2-Umsetzungsgesetz (NIS2UmsuCG)**, das die EU-Richtlinie 2022/2555 umsetzt, wurde das BSIG zum **6. Dezember 2025** grundlegend novelliert und ist seither ohne Übergangsfrist in Kraft – die Pflichten gelten sofort, unabhängig von der separaten Registrierungsfrist (siehe unten). "BSIG-neu" ist dabei eine vereinfachte Lernbezeichnung dieses Artikels, kein eigener Gesetzestitel.

Das novellierte BSIG unterscheidet nach § 28 im Kern **zwei Hauptkategorien** – **nicht** drei gleichrangige, wie man beim schnellen Lesen annehmen könnte:

| Kategorie | Einordnung | Bußgeldrahmen |
| --- | --- | --- |
| **Besonders wichtige Einrichtungen** | Insbesondere große Einrichtungen aus Anlage 1 des BSIG sowie bestimmte ausdrücklich genannte Anbieter (z. B. Telekommunikation, DNS, Vertrauensdienste) | Bis zu 10 Mio. € oder 2 % des weltweiten Jahresumsatzes |
| **Wichtige Einrichtungen** | Insbesondere mittlere Einrichtungen aus Anlage 1 oder 2, soweit sie nicht bereits als besonders wichtig gelten | Bis zu 7 Mio. € oder 1,4 % des weltweiten Jahresumsatzes |

> **Wichtig für die Prüfung:** "Betreiber kritischer Anlagen" ist **keine dritte, gleichrangige Kategorie**, sondern nach § 28 Abs. 1 Nr. 1 BSIG eine **Untergruppe der besonders wichtigen Einrichtungen** – nämlich die mit den strengsten Zusatzpflichten (u. a. Systeme zur Angriffserkennung, gesonderte Nachweispflicht nach § 39). Die vereinfachte Merkregel: *Wer eine kritische Anlage betreibt, ist automatisch auch "besonders wichtig" – aber nicht jede besonders wichtige Einrichtung betreibt eine kritische Anlage.*

Die genaue Einordnung hängt von mehreren Kriterien ab: konkrete Einrichtungsart nach Anlage 1/2 des BSIG, Zahl der Mitarbeitenden, Jahresumsatz **und** Jahresbilanzsumme (beide Werte relevant, nicht nur einer davon), sowie sektorspezifische Sonderregeln.

Insgesamt gelten heute rund **29.500 Unternehmen** als betroffen – deutlich mehr als unter der alten KRITIS-Regelung. Zentrale Pflichten:

- **Registrierungspflicht:** grundsätzlich innerhalb von drei Monaten, nachdem eine Organisation erstmals oder erneut als besonders wichtige oder wichtige Einrichtung gilt (§ 33 BSIG) – für bereits am 6.12.2025 erfasste Einrichtungen endete diese Frist rechnerisch am 6. März 2026; bei später eintretender Betroffenheit läuft die Dreimonatsfrist individuell weiter
- **Mindestsicherheitsmaßnahmen** nach § 30 BSIG (setzt Art. 21 NIS2 in deutsches Recht um)
- **Meldepflicht** bei erheblichen Sicherheitsvorfällen (§ 32, gestufte Meldung, Erstmeldung binnen 24 Stunden)
- **Umsetzungs-, Überwachungs- und Schulungspflichten der Geschäftsleitung** nach § 38 BSIG; bei schuldhafter Pflichtverletzung kommt eine persönliche **Innenhaftung gegenüber der eigenen Einrichtung** nach den anwendbaren gesellschaftsrechtlichen Regeln in Betracht – keine allgemeine Haftung gegenüber Dritten oder Behörden
- **Zusätzliche Anforderungen und Nachweispflicht für Betreiber kritischer Anlagen** (§§ 31, 39): Nachweis über Sicherheitsaudits, Prüfungen oder Zertifizierungen, dass die Anforderungen aus § 30 und die verschärften Zusatzanforderungen aus § 31 (u. a. Systeme zur Angriffserkennung) erfüllt sind – grundsätzlich alle drei Jahre zu wiederholen

> **IHK-Typfrage:** *"Warum belegt eine ISO-27001-Zertifizierung nicht automatisch die vollständige Erfüllung der Nachweispflicht eines Betreibers kritischer Anlagen nach § 39 BSIG?"*
> **Musterantwort:** Eine Zertifizierung kann grundsätzlich eine der in § 39 genannten Nachweisformen (Audit, Prüfung, Zertifizierung) sein. Für den Nachweis nach § 39 BSIG muss aber konkret belegt werden, dass die für die kritische Anlage maßgeblichen Systeme, Komponenten und Prozesse sowohl die allgemeinen Anforderungen aus § 30 **als auch** die verschärften Zusatzanforderungen aus § 31 erfüllen – dazu zählt insbesondere der vorgeschriebene Einsatz von Systemen zur Angriffserkennung. Entscheidend sind also der konkrete Geltungsbereich, die geprüften Systeme und die vollständige Abdeckung der §§ 30/31-Anforderungen; ein allgemeines ISO-27001-Zertifikat ohne diese spezifische Abdeckung genügt nicht automatisch. (Unabhängig davon bestehen außerdem eigenständige Melde- und Geschäftsleitungspflichten nach §§ 32 und 38 BSIG – diese sind vom § 39-Nachweis zu unterscheiden.)

### 2.4 ISO/IEC 27001 vs. BSI IT-Grundschutz

| Kriterium | ISO/IEC 27001:2022 | BSI IT-Grundschutz |
| --- | --- | --- |
| Charakter | Internationaler, prozessorientierter Standard für ein ISMS – definiert *was* zu tun ist | Deutsche, sehr konkrete Methodik – liefert im IT-Grundschutz-Kompendium Bausteine mit *wie*-Vorgaben |
| Struktur | Anhang A referenziert 93 Referenzmaßnahmen in 4 Themenbereichen (organisatorisch, personell, physisch, technologisch) – ausführlich erläutert in der Schwesternorm ISO/IEC 27002:2022 | Bausteine je Zielobjekttyp, kompatibel zu ISO 27001 |
| Internationalität | Weltweit anerkannt | Primär deutscher Kontext, zunehmend auch international referenziert |

> **Vereinfachter Merksatz (mit Einschränkung):** ISO 27001 ist stärker management- und prozessorientiert ("was" grundsätzlich zu leisten ist), IT-Grundschutz liefert zusätzlich sehr konkrete Bausteine und Umsetzungsvorschläge für typische Zielobjekte ("wie" es in der Praxis oft umgesetzt wird). Das ist eine didaktische Vereinfachung: ISO 27001 enthält durchaus konkrete Anforderungen, und der IT-Grundschutz schreibt nicht in jedem Fall einen einzigen zwingenden technischen Weg vor – die Bausteine des IT-Grundschutzes können zudem selbst als Grundlage einer ISO-27001-Zertifizierung dienen.

> **KRITIS-Sektoren-Hinweis:** Die früher bekannten KRITIS-**Sektoren** (Energie, Gesundheit, Wasser, IT/TK, Finanzen, Transport/Verkehr, Ernährung, Siedlungsabfallentsorgung, Staat/Verwaltung, Medien/Kultur) bleiben als fachliche Orientierung und insbesondere für Betreiber kritischer Anlagen relevant. Für die allgemeine NIS2-/BSIG-Einordnung sind sie aber nicht mehr die zentrale Systematik: Maßgeblich sind die – umfangreicheren und teils anders zugeschnittenen – Einrichtungsarten und Sektoren nach den **Anlagen 1 und 2 des BSIG** sowie die Größen- und Sonderregeln des § 28.

---

## 3. Gefährdungen, Schwachstellen, Risiko und STRIDE

> **Grundprinzip:** Ein Schädlingsbefall im Gewächshaus bricht nicht einfach so aus – es braucht einen anfälligen Bestand (Schwachstelle: geschwächte Pflanzen) und einen Erreger, der diese Anfälligkeit ausnutzt (Gefährdung: der Schädling). Das Risiko ist die Kombination aus Wahrscheinlichkeit eines Befalls und dem Schaden, den er anrichten würde.

### 3.1 Begriffsabgrenzung und Risikoformel

| Begriff | Bedeutung |
| --- | --- |
| **Schwachstelle** | Eine Verwundbarkeit im System (z. B. ungepatchtes Betriebssystem, offenes Kellerfenster) |
| **Gefährdung** | Ein potenzielles schädigendes Ereignis (z. B. Ransomware, Einbrecher) |
| **Risiko** | Ergibt sich aus der Kombination von Eintrittswahrscheinlichkeit und Schadensausmaß |

$$\text{Risiko} = \text{Eintrittswahrscheinlichkeit} \times \text{Schadensausmaß}$$

> Diese Formel ist ein nützliches Denkmodell, liefert aber keine exakte, objektiv "richtige" Zahl – Eintrittswahrscheinlichkeit und Schadensausmaß sind in der Praxis Schätzwerte (Schadensausmaß umfasst dabei nicht nur monetäre Verluste, sondern z. B. auch Reputationsschäden oder Betriebsunterbrechungen). Rein mathematische Berechnungen stoßen an ihre Grenzen und werden im IT-Sicherheitsbetrieb durch qualitative Experteneinschätzung ergänzt, insbesondere bei Kumulationseffekten (mehrere kleine Risiken verstärken sich gegenseitig zu einer existenzbedrohenden Gefahr).

### 3.2 Bedrohungsklassifizierung nach STRIDE

Das STRIDE-Modell (von Microsoft entwickelt) klassifiziert Bedrohungen nach dem verletzten Schutzziel:

| Buchstabe | Bedrohung (EN) | Bedrohung (DE) | Verletztes Schutzziel | IHK-Relevanz |
| --- | --- | --- | --- | --- |
| **S** | Spoofing | Identität vortäuschen | Authentizität | 🔴 |
| **T** | Tampering | Daten manipulieren | Integrität | 🔴 |
| **R** | Repudiation | Abstreitbarkeit | Verbindlichkeit/Nachvollziehbarkeit | 🟡 |
| **I** | Information Disclosure | Informationsenthüllung | Vertraulichkeit | 🔴 |
| **D** | Denial of Service | Dienstblockade | Verfügbarkeit | 🔴 |
| **E** | Elevation of Privilege | Rechteausweitung | Autorisierung | 🔴 |

### 3.3 Malware-Klassen und Social Engineering

| Malware-Typ | Merkmal |
| --- | --- |
| **Virus** | Braucht ein Wirtsprogramm, verbreitet sich bei dessen Ausführung |
| **Wurm** | Verbreitet sich eigenständig über Netzwerke, ohne Wirtsprogramm |
| **Trojaner** | Tarnt sich als nützliches Programm, führt im Hintergrund Schadfunktionen aus |
| **Ransomware** | Verschlüsselt Daten und fordert Lösegeld für die Entschlüsselung (oft kombiniert mit Datenexfiltration, "Double Extortion") |

**Social Engineering** nutzt psychologische Manipulation statt technischer Lücken – typische Trigger sind künstlich erzeugter Zeitdruck, vorgetäuschte Autorität und Neugier. **Phishing** ist die häufigste Ausprägung: gefälschte Absenderadressen, Dringlichkeit und ein manipulierter Link oder Anhang führen zur Preisgabe von Zugangsdaten.

> **IHK-Typfrage:** *"Ordnen Sie folgenden Angriff einer STRIDE-Kategorie zu und begründen Sie: Ein Angreifer fälscht die Absenderadresse einer E-Mail, um sich als Vorgesetzter auszugeben (CEO-Fraud)."*
> **Musterantwort:** **Spoofing** – der Angreifer täuscht eine falsche Identität vor (der vermeintliche Absender ist nicht der tatsächliche Absender). Das verletzte Schutzziel ist die Authentizität: Das Opfer kann sich nicht mehr sicher sein, dass die Nachricht wirklich vom angegebenen Absender stammt.

---

## 4. Moderne Angriffsmuster und digitale Identität

> **Grundprinzip:** Ein einzelnes Datenleak ist wie ein loser Karton in einer Lieferkette, der vom Lkw fällt – für sich genommen ärgerlich, aber oft der erste Schritt einer Kette: Der Inhalt wird aufgesammelt, sortiert und weiterverkauft, bis er in ganz anderen Zusammenhängen wieder auftaucht.

### 4.1 Eine mögliche Angriffskette: Von Datenleak zu Doxing

| Begriff | Bedeutung | IHK-Relevanz |
| --- | --- | --- |
| **Datenleak (Data Leak)** | Unbeabsichtigter oder unrechtmäßiger Abfluss sensibler Informationen nach außen – häufig durch Cloud-Fehlkonfigurationen | 🔴 |
| **Identitätsdiebstahl (Identity Theft)** | Missbräuchliche Nutzung persönlicher Identitätsmerkmale (Name, E-Mail, Zugangsdaten), um Verträge abzuschließen oder Systeme zu kompromittieren | 🔴 |
| **Doxing** | Gezieltes Ausspähen, Zusammentragen und Veröffentlichen privater Daten einer Person, meist zur Erpressung oder Einschüchterung | 🟡 |

```text
[ Datenleak bei Online-Shop ] --(Zugangsdaten geleakt)--> [ Credential Stuffing
                                                              gegen andere Dienste ]
                                                                    |
                                                                    v
                                            [ Identitätsdiebstahl (Konto übernommen) ]
                                                                    |
                                                                    v
                                        [ Doxing: private Daten zusammengetragen
                                          und veröffentlicht ]
```

**Credential Stuffing** ist die Technik dahinter: Angreifer probieren geleakte Zugangsdaten automatisiert bei vielen anderen Diensten aus – funktioniert vor allem, weil viele Menschen Passwörter mehrfach verwenden.

> Die drei Ereignisse können aufeinander aufbauen, müssen es aber nicht zwingend in dieser Reihenfolge: Ein Datenleak kann auch direkt zu Doxing führen, und Identitätsdiebstahl kann ganz ohne vorheriges Datenleak entstehen, etwa durch gezieltes Phishing.

### 4.2 SEO-Poisoning und Botnetze

- **SEO-Poisoning:** Angreifer manipulieren durch gezielte Suchmaschinenoptimierung die Sichtbarkeit präparierter Seiten in den Suchergebnissen. Die Zielseiten können ganz unterschiedlich schädlich sein – klassische Schadsoftware-Downloads (z. B. bei "Download VLC Player"), aber auch Phishing-Seiten, gefälschte Support-Seiten oder betrügerische Fake-Shops.
- **Botnetz:** Ein Verbund infizierter Computer ("Bots"), gesteuert über eine Command-and-Control-Infrastruktur (klassisch ein zentraler Server, zunehmend auch mehrere Server oder dezentrale Peer-to-Peer-Strukturen, um die Abschaltung zu erschweren) – für koordinierte Massenangriffe (DDoS) oder Spam-Verteilung. Historische Beispiele: *Mirai* (IoT-Geräte), *Emotet* (Windows-Systeme, oft als "Downloader" für weitere Schadsoftware wie Ransomware genutzt).

### 4.3 Schutz digitaler Identitäten

| Maßnahme | Wirkung | IHK-Relevanz |
| --- | --- | --- |
| **Passwortmanager** | Ermöglicht einzigartige, komplexe Passwörter pro Dienst – verhindert, dass ein Leak bei Dienst A auch Dienst B gefährdet | 🔴 |
| **Multi-Faktor-Authentifizierung (MFA)** | Zusätzlicher Faktor (Besitz/Biometrie) macht gestohlene Zugangsdaten allein unbrauchbar | 🔴 |
| **Single Sign-On (SSO)** | Zentrale Anmeldung über einen Identitätsanbieter statt vieler Einzelkonten – reduziert Passwort-Wiederverwendung, konzentriert aber das Risiko auf ein Hauptkonto | 🟡 |

> **Trade-off bei SSO:** Ein kompromittiertes SSO-Hauptkonto (z. B. Microsoft- oder Google-Konto) gefährdet potenziell alle daran angebundenen Dienste gleichzeitig – SSO tauscht viele kleine Angriffsflächen gegen eine einzige, dafür besonders kritische Angriffsfläche. Das macht ein starkes MFA für das Hauptkonto besonders wichtig.

> **IHK-Typfrage:** *"Warum reicht ein einzelnes, sehr starkes Passwort für alle Online-Konten nicht als Schutzmaßnahme aus?"*
> **Musterantwort:** Wird eines der Konten durch ein Datenleak beim jeweiligen Anbieter kompromittiert (unabhängig von der Passwortstärke, z. B. durch einen Server-Hack), können Angreifer per Credential Stuffing dasselbe Passwort bei anderen Diensten ausprobieren. Ein wiederverwendetes Passwort macht aus einem einzelnen Leak eine Kompromittierung vieler Konten gleichzeitig – ein Passwortmanager mit einzigartigen Passwörtern pro Dienst begrenzt den Schaden auf den ursprünglich betroffenen Dienst.

---

## 5. Typische Prüfungsfallen

| # | Falle | Richtigstellung |
| --- | --- | --- |
| 1 | Die CIA-Triade besteht aus genau drei, abschließenden Schutzzielen | CIA ist der zentrale Ausgangspunkt; manche Rahmenwerke ergänzen Authentizität und Verbindlichkeit als weitere Schutzziele (siehe STRIDE) |
| 2 | "KRITIS", "besonders wichtig" und "wichtig" sind drei gleichrangige, getrennte Kategorien | Das BSIG unterscheidet nur **zwei** Hauptkategorien (besonders wichtig / wichtig) – "Betreiber kritischer Anlagen" ist keine dritte, sondern eine **Untergruppe** der besonders wichtigen Einrichtungen mit verschärften Zusatzpflichten |
| 3 | ISO 27001 und BSI IT-Grundschutz sind austauschbar | ISO 27001 sagt *was* zu tun ist (prozessorientiert), BSI IT-Grundschutz sagt zusätzlich sehr konkret *wie* – beide sind zueinander kompatibel, aber unterschiedlich detailliert |
| 4 | Ein hohes Risiko-Matrix-Ergebnis ist eine objektive, exakte Zahl | Eintrittswahrscheinlichkeit und Schadensausmaß sind Schätzwerte – die Formel ist ein Denkmodell, kein Laborergebnis, und wird durch Expertenurteil ergänzt |
| 5 | Ransomware verletzt nur die Verfügbarkeit | Moderne Ransomware kombiniert oft Verschlüsselung (Verfügbarkeit) mit vorheriger Datenexfiltration (Vertraulichkeit) – "Double Extortion" |
| 6 | Ein starkes, aber wiederverwendetes Passwort schützt ausreichend | Ein Datenleak beim Anbieter kompromittiert das Passwort unabhängig von seiner Stärke – Wiederverwendung ermöglicht Credential Stuffing gegen andere Dienste |
| 7 | SSO ist grundsätzlich unsicherer als viele einzelne Passwörter | SSO reduziert Passwort-Wiederverwendung, konzentriert das Risiko aber auf ein Hauptkonto – die Bewertung hängt vom Schutzniveau (v. a. MFA) dieses Hauptkontos ab |

---

## 6. Deep-Dive-Ausblick (freiwillig)

- **DSGVO-Auskunftsprozess** (→ Abschnitt 2.2): Der konkrete Ablauf einer Auskunftsanfrage nach Art. 15 DSGVO – Identitätsprüfung, Fristenlauf (1 Monat, verlängerbar), Form der Bereitstellung.
- **Weitere STRIDE-Schwestermodelle** (→ Abschnitt 3.2): Wie Bedrohungsmodellierungs-Ansätze wie PASTA oder DREAD STRIDE ergänzen oder für andere Schwerpunkte (z. B. Risikopriorisierung) genutzt werden.
- **k-Anonymität bei "Have I Been Pwned"** (→ Abschnitt 4.1): Wie die Plattform Passwort-Hashes so aufbereitet, dass Suchende ihre eigenen Zugangsdaten prüfen können, ohne dass die Plattform selbst die vollständigen Klartext-Anfragen sieht.
- **72-Stunden-Meldefrist bei Datenschutzvorfällen** (→ Abschnitt 2.2/4.1): Das Zusammenspiel von DSGVO-Meldepflicht (Art. 33, 72 Stunden an die Aufsichtsbehörde) und der neuen NIS2-Meldepflicht (24 Stunden Erstmeldung ans BSI) bei überschneidenden Vorfällen.

---

## 7. Selbsttest

| # | Frage | Kurzantwort |
| --- | --- | --- |
| 1 | Nenne die drei klassischen CIA-Schutzziele. | Vertraulichkeit, Integrität, Verfügbarkeit |
| 2 | Was regelt Art. 32 DSGVO? | Sicherheit der Verarbeitung durch technisch-organisatorische Maßnahmen, orientiert am Stand der Technik |
| 3 | Seit wann gilt das novellierte BSIG (NIS2-Umsetzung) in Deutschland? | Seit 6. Dezember 2025, ohne Übergangsfrist |
| 4 | Wie ist die Adressatenstruktur des novellierten BSIG aufgebaut? | Zwei Hauptkategorien: besonders wichtige Einrichtungen und wichtige Einrichtungen. Betreiber kritischer Anlagen sind keine dritte Kategorie, sondern eine Untergruppe der besonders wichtigen Einrichtungen mit verschärften Zusatzpflichten (§§ 31, 39) |
| 5 | Was unterscheidet eine Schwachstelle von einer Gefährdung? | Schwachstelle = Verwundbarkeit im System; Gefährdung = potenzielles schädigendes Ereignis, das die Schwachstelle ausnutzen könnte |
| 6 | Wofür steht das "T" in STRIDE, und welches Schutzziel ist betroffen? | Tampering (Daten manipulieren) – verletzt die Integrität |
| 7 | Was ist der Unterschied zwischen einem Virus und einem Wurm? | Virus braucht ein Wirtsprogramm zur Verbreitung, ein Wurm verbreitet sich eigenständig über Netzwerke |
| 8 | Was ist Credential Stuffing? | Automatisiertes Ausprobieren geleakter Zugangsdaten bei vielen anderen Diensten |
| 9 | Was ist SEO-Poisoning? | Manipulation von Suchmaschinenergebnissen, damit präparierte Schadsoftware-Seiten bei legitimen Suchanfragen vorne erscheinen |
| 10 | Nenne einen Trade-off von Single Sign-On. | Reduziert Passwort-Wiederverwendung, konzentriert das Risiko aber auf ein einzelnes Hauptkonto |
| 11 | Ein Unternehmen betreibt einen Rechenzentrumsdienst mit 80 Mitarbeitenden. Muss es sich voraussichtlich beim BSI registrieren, und in welche Kategorie würde es grob fallen? | Voraussichtlich ja – die allgemeine Beschäftigtenschwelle (≥ 50 Mitarbeitende) ist überschritten, und Rechenzentrumsdienste zählen zu den NIS2-Sektoren. Ob "wichtige" oder "besonders wichtige Einrichtung", hängt von der konkreten Einrichtungsart (Anlage 1/2 BSIG) und ggf. weiteren Größenkriterien ab – wichtig: Für die allgemeine Schwelle zählen bei Umsatz **und** Bilanzsumme beide Werte, nicht nur der Umsatz allein |

---

## 8. IHK-Cheatsheet

| Begriff | Kurzdefinition |
| --- | --- |
| **CIA-Triade** | Vertraulichkeit, Integrität, Verfügbarkeit – die drei zentralen Schutzziele |
| **DSGVO Art. 32** | Pflicht zu technisch-organisatorischen Maßnahmen nach Stand der Technik |
| **BSIG-neu / NIS2UmsuCG** | Seit 6.12.2025 geltende Novelle des BSI-Gesetzes; zwei Hauptkategorien (besonders wichtige/wichtige Einrichtungen) statt reiner KRITIS-Regulierung – Betreiber kritischer Anlagen sind Untergruppe der besonders wichtigen Einrichtungen |
| **STRIDE** | Bedrohungsmodell: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege |
| **Risiko** | Kombination aus Eintrittswahrscheinlichkeit und Schadensausmaß; quantitativ oft als Produkt dargestellt, qualitativ auch über eine Risikomatrix bewertbar |
| **Credential Stuffing** | Automatisiertes Ausprobieren geleakter Zugangsdaten bei anderen Diensten |
| **Doxing** | Gezieltes Veröffentlichen privater Daten zur Einschüchterung/Erpressung |
| **Botnetz** | Verbund ferngesteuerter, infizierter Rechner für koordinierte Angriffe |
| **SEO-Poisoning** | Manipulierte Suchergebnisse führen zu schadhaften Webseiten |
| **ISO 27001 vs. BSI-Grundschutz** | "Was" (prozessorientiert, international) vs. "Wie" (konkret, deutsch, kompatibel) |

---

## 9. Prüfungstaktik

| Aufgabentyp | Typische Formulierung | Was die IHK hören will |
| --- | --- | --- |
| Kaskaden-Analyse | "Erklären Sie, wie Vorfall X mehrere Schutzziele gefährdet" | Konkrete Kausalkette zwischen mindestens zwei Schutzzielen, nicht nur ein Schutzziel benennen |
| Rechtsrahmen-Einordnung | "Ist Unternehmen X von NIS2/BSIG-neu betroffen?" | Bezug auf Sektor + Schwellenwerte (Mitarbeitende/Umsatz), nicht nur "ja, weil IT-Firma" |
| STRIDE-Zuordnung | "Ordnen Sie Angriff X einer STRIDE-Kategorie zu" | Kategorie **und** verletztes Schutzziel nennen, mit Begründung am konkreten Beispiel |
| Risikobewertung | "Bewerten Sie das Risiko von X" | Beide Faktoren (Wahrscheinlichkeit UND Schadensausmaß) einzeln einschätzen, nicht nur pauschal "hoch" |
| Schutzmaßnahmen-Empfehlung | "Wie schützt man sich gegen Credential Stuffing/Identitätsdiebstahl?" | Konkrete Maßnahme (Passwortmanager, MFA) plus Begründung, welches Angriffsmuster sie konkret verhindert |

---

## 10. Merksätze für das Fachgespräch

> CIA ist kein Ranking, sondern ein Dreiklang – die Verletzung eines Ziels reißt oft die anderen mit, wie beim Dominoeffekt.

> Ein Gesetz zwingt, eine Norm überzeugt – DSGVO und BSIG-neu sind Pflicht, ISO 27001 und BSI-Grundschutz sind Kür mit Wirkung.

> Seit Dezember 2025 heißt es nicht mehr nur "KRITIS oder nicht" – zwei Hauptkategorien (besonders wichtig / wichtig), mit Betreibern kritischer Anlagen als besonders streng regulierter Untergruppe, haben den Kreis der Betroffenen von rund 4.500 auf rund 29.500 Unternehmen erweitert.

> Risiko braucht immer zwei Faktoren, nie nur einen – Eintrittswahrscheinlichkeit ohne Schadensausmaß (und umgekehrt) ist nur die halbe Wahrheit. Ob man beide dann multipliziert oder qualitativ in einer Matrix einordnet, ist zweitrangig.

> Ein Datenleak ist selten das Ende der Geschichte – es ist oft der erste Dominostein einer Kette bis zu Identitätsdiebstahl und Doxing.

---

```yaml
dokument: LF4.1-wiki-artikel
lernfeld: LF4.1
titel: "Grundlagen der Informationssicherheit & Gefahrenlandschaft"
typ: "Typ A – Kompakter Prüfungs-Wiki"
status: final
stand: 2026-09-08
quellen_intern:
  - "LF4.1.1: Die drei Säulen der Informationssicherheit.md"
  - "LF4.1.2: Gesetzlicher und normativer Rahmen (Compliance).md"
  - "LF4.1.3: IT-Gefährdungen, Risiken & Risiko-Matrix.md"
  - "LF4.1.4: Moderne Angriffsmuster & Digitale Identität.md"
quellen_fachlich:
  - titel: "NIS2-Umsetzungsgesetz (NIS2UmsuCG) / BSIG-Novelle"
    herausgeber: "Deutscher Bundestag / BSI"
    status: "in Kraft seit 6.12.2025 ohne Übergangsfrist; Registrierung grundsätzlich innerhalb 3 Monaten nach Betroffenheit (§ 33 BSIG) – für am 6.12.2025 bereits erfasste Einrichtungen rechnerisch 6.3.2026, danach individuelle Frist. Zwei Hauptkategorien (besonders wichtig/wichtig), Betreiber kritischer Anlagen als Untergruppe nach § 28 Abs. 1 Nr. 1. WICHTIG: Rohmaterial ging noch von 'IT-Sicherheitsgesetz 2.0' und reiner KRITIS-Struktur aus – im Artikel auf aktuellen Rechtsstand korrigiert; Quelle: gesetze-im-internet.de/bsig_2025"
  - titel: "ISO/IEC 27001:2022"
    herausgeber: "ISO/IEC"
    status: "aktuelle Fassung; Anhang A referenziert 93 Referenzmaßnahmen in 4 Themenbereichen (ausführlich erläutert in ISO/IEC 27002:2022), löst ISO 27001:2013 vollständig ab (Übergangsfrist endete Oktober 2025)"
  - titel: "DSGVO (Verordnung (EU) 2016/679)"
    herausgeber: "Europäische Union"
    status: "unverändert in Kraft, Bußgeldrahmen unverändert"
  - titel: "Microsoft STRIDE Threat Modeling"
    herausgeber: "Microsoft"
    status: "etabliertes, unverändertes Bedrohungsmodellierungs-Framework"
review_historie:
  - runde: 1
    datum: 2026-09-08
    ergebnis: "Erstdraft mit integrierter Web-Verifikation erstellt – dabei wichtige, im Rohmaterial durchgehend veraltete Rechtslage korrigiert: BSIG wurde zum 6.12.2025 durch NIS2-Umsetzungsgesetz grundlegend novelliert (drei Adressaten-Kategorien statt reiner KRITIS-Struktur, ca. 29.500 statt ca. 4.500 betroffene Unternehmen, neue Bußgeldrahmen, Meldepflichten, persönliche Geschäftsführerhaftung). ISO 27001:2022 als aktuelle Fassung bestätigt. Eigene Review nach Style-Guide-Checkliste direkt eingearbeitet: Typische Prüfungsfallen und Deep-Dive-Ausblick von Anfang an vorhanden, Analogien aus vier Domänen (Handwerk/Tresor, Bauvorschrift/Gütesiegel, Gärtnerei, Logistik/Lieferkette)"
  - runde: 2
    datum: 2026-09-08
    ergebnis: "Externe Prüfung (3 Reviews) eingearbeitet, gewichtet nach Quellenqualität. Wichtigster Fund (Review mit direkten Zitaten aus gesetze-im-internet.de/bsig_2025): Strukturfehler behoben – 'Betreiber kritischer Anlagen' war fälschlich als dritte, gleichrangige Kategorie dargestellt, ist aber nach § 28 Abs. 1 Nr. 1 BSIG eine Untergruppe der besonders wichtigen Einrichtungen (nur noch zwei Hauptkategorien). Weitere Rechts-Präzisierungen: § 39-Nachweispflicht korrekt auf §§ 30/31 (Sicherheitsmaßnahmen, Angriffserkennung) statt auf Meldeverfahren/Geschäftsleitungspflichten bezogen, § 38 als Innenhaftung gegenüber der eigenen Einrichtung statt pauschaler 'persönlicher Haftung' präzisiert, Registrierungsfrist als relative Drei-Monats-Frist (§ 33) statt fixem Stichtag für alle dargestellt, Selbsttest 11 korrigiert (Umsatz UND Bilanzsumme statt nur Umsatz). Weitere Präzisierungen: ISO-27001-Controls korrekt als Annex-A-Referenzmaßnahmen (elaboriert in 27002) statt pauschaler Norminhalt, ISO/Grundschutz-Vergleich als didaktische Vereinfachung gekennzeichnet, Risiko-Merksatz entschärft (Formel als Denkmodell, nicht zwingend Multiplikation), Angriffskette als 'eine mögliche' statt zwingende Reihenfolge, SEO-Poisoning auf Phishing/Fake-Shops erweitert, Botnetz-C2 als zentral oder dezentral möglich dargestellt"
  - runde: 3
    datum: 2026-09-08
    ergebnis: "Finale Review (2 Reviews) geprüft: kritischste, von beiden Reviews unabhängig bestätigte Inkonsistenz behoben – Selbsttest Frage 4 hatte noch die alte, falsche Drei-Kategorien-Struktur, obwohl Abschnitt 2.3/2.4, Prüfungsfalle 2 und Cheatsheet bereits in Runde 2 korrigiert waren. Weitere echte Funde: doppelter, fast wortgleicher Blockquote in Abschnitt 2.3 entfernt (diesmal kein Übertragungsartefakt, sondern eigener Fehler beim Editieren), § 39-Nachweispflicht um konkrete Nachweisformen (Audit/Prüfung/Zertifizierung) und Drei-Jahres-Turnus ergänzt, ISO-27001-Musterantwort von 'genügt nicht automatisch' zu 'kann eine mögliche Nachweisform sein, wenn Geltungsbereich §§30/31 abdeckt' korrigiert, KRITIS-Sektoren-Hinweis vorsichtiger formuliert (nicht mehr als zentrale NIS2-Systematik dargestellt, Verweis auf Anlagen 1/2 BSIG ergänzt), Cheatsheet-Risiko-Eintrag um qualitative Alternative ergänzt (Schadenshöhe→Schadensausmaß), 'BSIG-neu' explizit als Lernbezeichnung statt Gesetzestitel gekennzeichnet, Deep-Dive-Verweise von 'Kapitel' auf 'Abschnitt' vereinheitlicht"
  - runde: 4
    datum: 2026-09-08
    ergebnis: "Eigene Abschlussprüfung (kein externer Review): doppeltes Codeblock-Ende am Dateiende entfernt (YAML-Syntaxfehler), Terminologie 'Schadenshöhe'/'Schadensausmaß' vollständig auf 'Schadensausmaß' vereinheitlicht (war zuvor nur in Cheatsheet/Merksatz/Prüfungstaktik korrigiert, nicht aber in Kapitel 3.1 und Prüfungsfalle 4), YAML-Quellenangabe zu ISO 27001 an die präzisere Annex-A-Formulierung aus Kapitel 2.4 angeglichen. Keine weiteren Fachfehler gefunden."
freigabe: "Final gesetzt nach 4 Runden (3 externe Reviews + 1 eigene Abschlussprüfung, 2026-09-08) – Freigabe durch Autor:in bestätigt"
```