#!/usr/bin/env python3
"""Baut die FRITZ!Box DNS-Liste aus zwei milden, gepflegten Quellen.

Fuer die FRITZ!Box werden ausschliesslich Domainnamen ausgegeben.
Bei Downloadfehlern oder unerwarteten Groessen bleibt die letzte Liste erhalten.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import re

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "Streaming_Werbeblocker_Amazon_Disney_YouTube.txt"
SOURCES = (
    ("HaGeZi Multi Light", "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/light-onlydomains.txt", 30000),
    ("OISD Small", "https://raw.githubusercontent.com/sjhgvr/oisd/main/domainswild2_small.txt", 20000),
)
HOST = re.compile(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?")
MAX_DOWNLOAD = 8_000_000
MAX_ENTRIES = 180_000
MIN_ENTRIES = 70_000

def parse_domains(text):
    blocked, permitted = set(), set()
    for raw in text.splitlines():
        domain = raw.strip().lower()
        if not domain or domain.startswith(("#", "!")) or domain == "[adblock plus]":
            continue
        if domain.startswith("@@||") and domain.endswith("^"):
            item = domain[4:-1]
            if HOST.fullmatch(item):
                permitted.add(item)
            continue
        if domain.startswith("||") and domain.endswith("^"):
            domain = domain[2:-1]
        elif domain.startswith(("0.0.0.0 ", "127.0.0.1 ")):
            parts = domain.split()
            if len(parts) != 2:
                continue
            domain = parts[1]
        if HOST.fullmatch(domain) and len(domain) <= 253:
            blocked.add(domain)
    return blocked, permitted


def download(url):
    request = Request(url, headers={"User-Agent": "JeffChecker-Fritzbox-DNS-Filter/1.0"})
    with urlopen(request, timeout=35) as response:
        data = response.read(MAX_DOWNLOAD + 1)
    if len(data) > MAX_DOWNLOAD:
        raise RuntimeError("Quellliste ist unerwartet gross: " + url)
    return data.decode("utf-8-sig")


def read_local(filename):
    return parse_domains((ROOT / filename).read_text(encoding="utf-8"))


def main():
    all_domains = set()
    upstream_allow = set()
    for name, url, minimum in SOURCES:
        domains, allowed = parse_domains(download(url))
        print(f"{name}: {len(domains)} Domains")
        if not (minimum <= len(domains) <= MAX_ENTRIES):
            raise RuntimeError("Unerwartete Quelllistengroesse: " + name)
        all_domains.update(domains)
        upstream_allow.update(allowed)

    additions, _ = read_local("custom-domains.txt")
    protected, _ = read_local("ausnahmen.txt")
    all_domains.update(additions)
    all_domains.difference_update(protected | upstream_allow)
    if not (MIN_ENTRIES <= len(all_domains) <= MAX_ENTRIES):
        raise RuntimeError("Unerwartete Groesse nach Merge; bisherige Datei bleibt erhalten")

    header = [
        "# FRITZ!Box DNS-Filter: Werbung, Tracking und uebliche Schadsoftware",
        "# Dateiname und RAW-URL bleiben dauerhaft unveraendert.",
        "# Format: reine Domains, eine Domain pro Zeile (FRITZ!OS 8.40/8.50)",
        "# Quellen: HaGeZi Multi Light und OISD Small (beide GPL-3.0)",
        "# https://github.com/hagezi/dns-blocklists",
        "# https://github.com/sjhgvr/oisd",
        "# Nur Werbung/Tracking und allgemeine Risiken, kein Jugendschutz-/Social-/Shopping-Blocker.",
        "# DNS kann Prime Video-, Disney+- und YouTube-Videowerbung nicht sicher entfernen.",
        "# Lizenz: GPL-3.0. Ausnahmen und eigene Eintraege siehe Repository.",
        f"# Domains: {len(all_domains)}",
        "#",
    ]
    output = "\n".join(header) + "\n" + "\n".join(sorted(all_domains)) + "\n"
    if OUTPUT.exists() and OUTPUT.read_text(encoding="utf-8") == output:
        print("Keine Aenderungen")
        return
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Liste aktualisiert: {len(all_domains)} Domains")


if __name__ == "__main__":
    main()
