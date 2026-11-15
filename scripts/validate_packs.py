"""Validate final ZIPs with Umeko Desktop's actual pack reader and importer."""
import argparse
import hashlib
import importlib.util
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
    parser.add_argument('--pet-id', action='append', help='Only validate these pet IDs')
    args = parser.parse_args()
    # Load the actual host module without initializing an unrelated application.
    module_path = args.desktop_source.resolve() / 'app/pet_packs.py'
    spec = importlib.util.spec_from_file_location('umeko_host_pet_packs', module_path)
    host = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(host)
    STATES, import_pack, read_pack = host.STATES, host.import_pack, host.read_pack
    from PySide6.QtCore import QCoreApplication
    from PySide6.QtGui import QImageReader
    app = QCoreApplication([])
    catalog = json.loads((ROOT / "catalog.json").read_text())
    report = []
    with tempfile.TemporaryDirectory(prefix="umeko-pet-packs-") as temporary:
        destination = Path(temporary) / "imported"
        for entry in catalog["pets"]:
            if args.pet_id and entry['id'] not in args.pet_id:
                continue
            archive = ROOT / entry["download"]
            assert hashlib.sha256(archive.read_bytes()).hexdigest() == entry["sha256"]
            with zipfile.ZipFile(archive) as source:
                expected = json.loads(source.read('pet.json'))
                names = set(expected['states'].values())
                if expected.get('rareIdle'):
                    names.add(expected['rareIdle']['image'])
                assert set(source.namelist()) == {'pet.json', 'LICENSE.txt', *names}
            pack = import_pack(archive, destination)
            assert pack["id"] == entry["id"] and set(pack["states"]) == set(STATES)
            # import_pack already fully decodes and checks the host constraints.
            checked = read_pack(destination / pack["id"])
            assert checked.get('persona') == expected.get('persona')
            assert len(checked.get('persona', '')) <= 1000
            states = {}
            animations = dict(checked['states'])
            if checked.get('rareIdle'):
                animations['idle-rare'] = checked['rareIdle']['image']
            for state, filename in animations.items():
                reader = QImageReader(str(destination / pack["id"] / filename))
                assert reader.imageCount() >= 2 and reader.loopCount() == -1
                duration = 0
                frame_hashes = set()
                for _ in range(reader.imageCount()):
                    frame = reader.read()
                    assert not frame.isNull() and frame.hasAlphaChannel()
                    corners = [(0, 0)]
                    if entry['category'] == 'characters':
                        corners += [(frame.width()-1, 0), (0, frame.height()-1), (frame.width()-1, frame.height()-1)]
                    for x, y in corners:
                        assert frame.pixelColor(x, y).alpha() == 0, (entry['id'], filename, x, y)
                    frame_hashes.add(hashlib.sha256(bytes(frame.constBits())).digest())
                    duration += reader.nextImageDelay()
                assert len(frame_hashes) > 1, f'No actual frame changes: {filename}'
                declared = expected.get('images', {}).get(filename, {})
                if 'durationMs' in declared:
                    assert duration == declared['durationMs'], (filename, duration)
                if 'frames' in declared:
                    assert reader.imageCount() == declared['frames']
                with zipfile.ZipFile(archive) as source:
                    assert (destination / pack['id'] / filename).read_bytes() == source.read(filename)
                states[state] = {**checked["images"][filename], "durationMs": duration}
                # Release the file before TemporaryDirectory cleanup on Windows.
                del reader
            report.append({"id": pack["id"], "status": "imported", "states": states})
            print("PASS actual Umeko import:", pack["name"], pack["id"])
    assert report, 'No matching packages were validated'
    output = ROOT / "build/validation.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
