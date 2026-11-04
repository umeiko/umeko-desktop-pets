"""Slice generated animation atlases, encode WebP, and build reproducible Umeko ZIPs.

This is an asset export pipeline; it does not draw, deform or synthesize poses.
Requires Python 3.10+ and Pillow with animated WebP support.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import zipfile

from PIL import Image, features

ROOT = Path(__file__).resolve().parents[1]
STATES = ("idle", "thinking", "working", "waiting", "done", "error")
VERSION = "1.0.0"
SIZE = 384
# Actual illustrated poses are replayed with longer holds for quiet states.
TIMELINES = {
    "idle": ([0, 1, 2, 1, 0, 3], [600, 220, 160, 220, 600, 200]),
    "thinking": ([0, 1, 2, 1, 0, 3], [360, 220, 480, 220, 360, 220]),
    "working": ([0, 1, 2, 3], [180, 180, 180, 180]),
    "waiting": ([0, 1, 2, 1, 0, 3], [850, 300, 180, 300, 850, 300]),
    "done": ([0, 1, 2, 3, 2, 1], [220, 180, 360, 360, 180, 200]),
    "error": ([0, 1, 2, 1, 0, 3], [450, 280, 300, 280, 450, 320]),
}
PETS = {
    "labrador": {
        "id": "labrador-retriever", "name": "拉布拉多", "englishName": "Labrador Retriever",
        "description": "奶油黄色短毛、垂耳、棕眼睛，温柔又有精神的拉布拉多。",
        "dialogue": {
            "tap": ["汪！我在。", "摸摸耳朵？", "一起把任务做好。"],
            "hover": ["陪你盯着呢。", "尾巴已经准备好了。"],
            "drag": ["换个位置，继续陪你。", "轻一点，汪。"],
            "done": ["汪！任务完成啦。", "干得漂亮，摇尾巴！"],
            "error": ["汪？这一步需要再看看。", "没关系，我陪你检查。"],
        },
    },
    "ragdoll": {
        "id": "ragdoll-cat", "name": "布偶猫", "englishName": "Ragdoll Cat",
        "description": "海豹双色、蓝眼睛、白色倒 V 面纹和蓬松长尾，安静陪伴的布偶猫。",
        "dialogue": {
            "tap": ["喵，叫我吗？", "可以摸摸，不许捣乱。", "我在陪你。"],
            "hover": ["工作归你，陪伴归我。", "我有认真看着。"],
            "drag": ["喵，换个舒服的地方。"],
            "done": ["喵，做好了。", "这次值得伸个懒腰。"],
            "error": ["喵？这里有点不对。", "慢慢检查，我等你。"],
        },
    },
}


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def export_frame(atlas: Image.Image, column: int, row: int):
    cell = atlas.crop((column * 256, row * 256, (column + 1) * 256, (row + 1) * 256))
    # Ignore antialiased fur tips when measuring the common ground baseline.
    bounds = cell.getchannel("A").point(lambda alpha: 255 if alpha > 32 else 0).getbbox()
    if bounds is None:
        raise ValueError(f"Empty sprite at {row}, {column}")
    if bounds[0] == 0 or bounds[1] == 0 or bounds[2] == 256 or bounds[3] == 256:
        raise ValueError(f"Sprite touches a cell boundary at {row}, {column}: {bounds}")
    scale = SIZE / 256
    sprite = cell.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    frame = Image.new("RGBA", (SIZE, SIZE))
    # One fixed scale, with paws aligned across all states. No independent
    # per-frame stretching or body deformation is used.
    frame.alpha_composite(sprite, (0, round((230 - bounds[3]) * scale)))
    return frame


def build_one(slug, pet):
    source = ROOT / "art/animals" / slug / "atlas.png"
    atlas = Image.open(source).convert("RGBA")
    if atlas.size != (1024, 1536):
        raise ValueError(f"Expected 4x6 atlas at 1024x1536: {source}")
    folder = ROOT / "pets/animals" / slug
    folder.mkdir(parents=True, exist_ok=True)
    metadata = {}
    for row, state in enumerate(STATES):
        poses = [export_frame(atlas, column, row) for column in range(4)]
        sequence, durations = TIMELINES[state]
        frames = [poses[index] for index in sequence]
        path = folder / (state + ".webp")
        frames[0].save(path, "WEBP", save_all=True, append_images=frames[1:],
                       duration=durations, loop=0, lossless=True, method=6, exact=True)
        encoded = Image.open(path)
        if encoded.n_frames < 2:
            raise ValueError(f"State must be animated: {path}")
        top = min(frame.getchannel("A").getbbox()[1] for frame in frames)
        metadata[path.name] = {"animated": True, "width": SIZE, "height": SIZE,
                               "frames": encoded.n_frames, "contentTop": top / SIZE}
        if state == "idle":
            frames[0].save(ROOT / "preview" / (slug + ".png"))
    manifest = {
        "format": "umeko-pet", "version": 1, "id": pet["id"], "name": pet["name"],
        "packVersion": VERSION, "author": "Umeko contributors", "license": "MIT",
        "description": pet["description"],
        "states": {state: state + ".webp" for state in STATES},
        "images": metadata, "dialogue": pet["dialogue"],
    }
    write_json(folder / "pet.json", manifest)
    output = ROOT / "dist/animals" / f"umeko-pet-{slug}-{VERSION}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        files = {path.name: path.read_bytes() for path in sorted(folder.iterdir())
                 if path.name in {"pet.json", *(state + ".webp" for state in STATES)}}
        files["LICENSE.txt"] = (ROOT / "LICENSE").read_bytes()
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, (2026, 11, 4, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data, compresslevel=9)
    record = {"id": pet["id"], "name": pet["name"], "englishName": pet["englishName"],
              "category": "animals", "version": VERSION, "description": pet["description"],
              "manifest": str((folder / "pet.json").relative_to(ROOT)),
              "preview": f"preview/{slug}.png", "animation": f"pets/animals/{slug}/idle.webp",
              "download": str(output.relative_to(ROOT)), "bytes": output.stat().st_size,
              "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}
    print(f"BUILT {record['download']} ({record['bytes']:,} bytes)")
    return record


if __name__ == "__main__":
    if not features.check("webp_anim"):
        raise SystemExit("Pillow needs animated WebP support")
    (ROOT / "preview").mkdir(exist_ok=True)
    entries = [build_one(slug, pet) for slug, pet in PETS.items()]
    write_json(ROOT / "catalog.json", {
        "format": "umeko-desktop-pets-catalog", "version": 1,
        "categories": [{"id": "animals", "name": "动物"}, {"id": "characters", "name": "人物"}],
        "pets": entries,
    })
    (ROOT / "dist/SHA256SUMS").write_text("".join(
        f"{entry['sha256']}  {entry['download'].removeprefix('dist/')}\n" for entry in entries), encoding="utf-8")
