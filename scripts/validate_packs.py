"""Validate final ZIPs with Umeko Desktop's actual pack reader and importer."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import zipfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--desktop-source", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.desktop_source.resolve()))
    from app.pet_packs import STATES, import_pack, read_pack
    from PySide6.QtCore import QCoreApplication
    from PySide6.QtGui import QImageReader
    app = QCoreApplication([])
    catalog = json.loads((ROOT / "catalog.json").read_text())
    report = []
    with tempfile.TemporaryDirectory(prefix="umeko-animal-packs-") as temporary:
        destination = Path(temporary) / "imported"
        for entry in catalog["pets"]:
            archive = ROOT / entry["download"]
            assert hashlib.sha256(archive.read_bytes()).hexdigest() == entry["sha256"]
            with zipfile.ZipFile(archive) as source:
                assert set(source.namelist()) == {"pet.json", "LICENSE.txt", *(state + ".webp" for state in STATES)}
            pack = import_pack(archive, destination)
            assert pack["id"] == entry["id"] and set(pack["states"]) == set(STATES)
            checked = read_pack(destination / pack["id"], check=True)
            states = {}
            for state, filename in checked["states"].items():
                reader = QImageReader(str(destination / pack["id"] / filename))
                assert reader.imageCount() >= 2 and reader.loopCount() == -1
                duration = 0
                for _ in range(reader.imageCount()):
                    frame = reader.read()
                    assert not frame.isNull() and frame.hasAlphaChannel()
                    assert frame.pixelColor(0, 0).alpha() == 0
                    duration += reader.nextImageDelay()
                states[state] = {**checked["images"][filename], "durationMs": duration}
                # Release the file before TemporaryDirectory cleanup on Windows.
                del reader
            report.append({"id": pack["id"], "status": "imported", "states": states})
            print("PASS actual Umeko import:", pack["name"], pack["id"])
    output = ROOT / "build/validation.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
