#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "REGISTAR_LEDGER.csv"

def normalized_bytes(text: str) -> bytes:
    text = re.sub(r"SHA256:\s*[0-9a-fA-F]{12,64}|SHA256:\s*\[UNSEALED\]", "SHA256: [HASH-EXCLUDED]", text)
    return text.encode("utf-8")

def get_meta(text: str, label: str) -> str:
    pattern = rf"<dt>{re.escape(label)}</dt>\s*<dd[^>]*>(.*?)</dd>"
    m = re.search(pattern, text, flags=re.S)
    if not m:
        return ""
    return re.sub(r"<.*?>", "", m.group(1)).strip()

def main():
    if len(sys.argv) != 2:
        print("upotreba: python3 tools/close_entry.py 004")
        raise SystemExit(1)

    br = sys.argv[1].zfill(3)
    path = ROOT / "entries" / f"{br}.html"
    if not path.exists():
        print(f"nedostaje unos: {path}")
        raise SystemExit(1)

    text = path.read_text(encoding="utf-8")
    full_hash = hashlib.sha256(normalized_bytes(text)).hexdigest()
    short_hash = full_hash[:12]

    text = re.sub(r"SHA256:\s*[0-9a-fA-F]{12,64}|SHA256:\s*\[UNSEALED\]", f"SHA256: {short_hash}", text)
    path.write_text(text, encoding="utf-8")

    row = {
        "br": br,
        "fajl": f"entries/{br}.html",
        "format": get_meta(text, "FORMAT"),
        "oblik": get_meta(text, "OBLIK"),
        "tip": get_meta(text, "TIP"),
        "serija": get_meta(text, "SERIJA"),
        "datum_registracije": get_meta(text, "DATUM REGISTRACIJE"),
        "datum_dogadjaja": get_meta(text, "DATUM DOGAĐAJA"),
        "status_zapisa": get_meta(text, "STATUS ZAPISA"),
        "status_dogadjaja": get_meta(text, "STATUS DOGAĐAJA"),
        "hash_full": full_hash,
        "hash_short": short_hash,
        "napomena": ""
    }

    fieldnames = list(row.keys())
    rows = []
    if LEDGER.exists():
        with LEDGER.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            rows = [r for r in reader if (r.get("br") or r.get("no")) != br]

    rows.append(row)
    rows.sort(key=lambda r: r.get("br") or r.get("no") or "")

    with LEDGER.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"zatvoren unos {br}: SHA256 {full_hash}")

if __name__ == "__main__":
    main()
