# Filterliste fuer FRITZ!Box

Ausgewogene DNS Sperrliste gegen normale Werbung, Tracking, Telemetrie und uebliche schadhafte Werbeziele. Die Datei ist fuer die neue DNS Filterfunktion in FRITZ!OS 8.40 / 8.50 und kompatible DNS Filter konzipiert.

## Unveraenderte Filteradresse

```text
https://raw.githubusercontent.com/JeffChecker/filterlist/main/Streaming_Werbeblocker_Amazon_Disney_YouTube.txt
```

Der Dateiname und die RAW URL bleiben bestehen. Eine FRITZ!Box, die die Liste bereits abonniert hat, braucht **keine neue Adresse**.

## Was wird gesperrt?

* Klassische Werbe- und Trackerdomains, auch auf vielen Mobilgeraeten und Streamingboxen
* Analytik, Telemetrie und einige bekannte schadhafte Domains
* Gezielt bekannte Amazon, Disney und Google Werbedomains

Bewusst **nicht** kategorisch gesperrt: soziale Netzwerke, normale Shoppingseiten, Affiliate Links, Erwachsenenseiten, VPN und Messenger. Die Hauptdomains gaengiger Streaming- und Kommunikationsdienste bleiben geschuetzt.

**Wichtige Grenze:** DNS Filter koennen keine Werbung entfernen, die ueber dieselbe Domain wie der Film / das Video ausgeliefert wird. Das betrifft besonders Prime Video, Disney+ und YouTube.

## Einrichten

FRITZ!Box: **Heimnetz > Netzwerk > Netzwerkeinstellungen > Erweiterte Netzwerkeinstellungen > DNS-Filter**. DNS Filter aktivieren, *Filterliste hinzufuegen* und die obige RAW Adresse eintragen. Die FRITZ!Box ruft die Datei in ihren Aktualisierungsintervallen ab. Es ist weder AdGuard DNS noch ein Pi-hole erforderlich.

## Wartung

Die Liste wird aus zwei zurueckhaltenden, regelmaessig gepflegten Quellen mit entferntem Duplikatbestand erstellt:

* [HaGeZi Multi Light](https://github.com/hagezi/dns-blocklists) (GPL-3.0)
* [OISD Small](https://oisd.nl/) ([GitHub](https://github.com/sjhgvr/oisd), GPL-3.0)

Beide enthalten bereits Regeln aus zahlreichen weiteren Projekten. Die aggressiven Pro++, Ultimate, Jugendschutz- und kategorischen Sperrlisten werden bewusst nicht zusammengemischt.

* `custom-domains.txt`: zusaetzliche bekannte Werbe- und Trackingdomains
* `ausnahmen.txt`: Domains, die nicht blockiert werden duerfen
* `scripts/aktualisieren.py`: fuehrt beide Listen zusammen, validiert Domains und entfernt Duplikate
* `.github/workflows/update-filterlist.yml`: fuehrt die Aktualisierung taeglich in GitHub Actions aus

Bei fehlgeschlagenem Download oder stark abweichender Groesse ueberschreibt der Generator die bisherige Liste nicht. Wenn GitHub Actions deaktiviert oder gesperrt sind, erfolgt die Aktualisierung nicht automatisch.

## Falls eine App nicht funktioniert

Zunaechst in der FRITZ!Box unter DNS Filter eine Ausnahme fuer die **konkret betroffene Domain** eintragen. Nicht pauschal komplette Anbieter oder CDN Domains freigeben. Falls der Fehler durch die Sperrliste verursacht wird, einen Eintrag unter `ausnahmen.txt` pflegen, damit er beim naechsten GitHub Lauf dauerhaft aus der Liste entfernt wird.

## Lizenz / Herkunft

Abgeleitete Liste unter [GPL-3.0](LICENSE) entsprechend den Lizenzen von HaGeZi und OISD. Quelle und Hinweise der Originalprojekte beachten. Keine Garantie, dass alle Dienste funktionieren oder jede Werbung erkannt wird.
