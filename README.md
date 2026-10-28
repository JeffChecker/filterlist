# Streaming Werbefilter

Diese Sammlung enthaelt Filterregeln fuer Amazon Prime Video, Disney+ und YouTube sowie einige dazugehoerige Werbe und Trackingdienste.

## Inhalt

`Streaming_Werbeblocker_Amazon_Disney_YouTube.txt`: Filterliste mit Hinweisen zur Nutzung und Fehlerbehebung.

## Verwendung

In AdGuard Home kann die TXT Datei als benutzerdefinierte DNS Filterliste verwendet werden. Fuer die Einbindung ueber eine URL muss die RAW Adresse der Datei aus diesem Repository verwendet werden. Die Kompatibilitaet haengt vom verwendeten Werbeblocker ab.

## Wichtige Einschraenkungen

Diese Regeln blockieren **nicht zuverlaessig die Werbung innerhalb der Videostreams** von Amazon Prime Video, Disney+ oder YouTube. Werbung kann ueber dieselben Server wie der eigentliche Videoinhalt bereitgestellt oder direkt in den Stream integriert werden. DNS Filter koennen ausserdem Wiedergabefehler ausloesen.

Nicht die Hauptdomains der Streamingdienste sperren. Die Datei enthaelt zudem eine ausdruecklich als potenziell problematisch markierte Disney/Hulu Regel. Bei Abspielproblemen zuerst diese Regel deaktivieren.

## Stand

28. Oktober 2026. Diese Liste ist eine ungetestete Ausgangsbasis und sollte vor produktivem Einsatz auf den Zielgeraeten getestet werden.
