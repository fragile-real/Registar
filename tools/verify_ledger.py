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

def main():
    if not LEDGER.exists():
        print("nedostaje REGISTAR_LEDGER.csv")
        raise SystemExit(1)

    ok = True
    with LEDGER.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            rel = row.get("fajl") or row.get("file")
            path = ROOT / rel
            if not path.exists():
                print(f"nedostaje: {rel}")
                ok = False
                continue

            text = path.read_text(encoding="utf-8")
            full_hash = hashlib.sha256(normalized_bytes(text)).hexdigest()
            if full_hash != row["hash_full"]:
                print(f"promenjeno: {rel}")
                print(f"  knjiga upisa: {row['hash_full']}")
                print(f"  stvarno:       {full_hash}")
                ok = False
            else:
                print(f"u redu: {rel}")

    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
