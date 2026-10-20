import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "data" / "assets.json"


def load_assets():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            assets = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            "File data tidak valid. Periksa data/assets.json."
        ) from error

    required_fields = {"id", "name", "location", "condition"}

    if not isinstance(assets, list):
        raise ValueError("Format data aset harus berupa daftar.")

    for asset in assets:
        if not isinstance(asset, dict):
            raise ValueError("Format salah satu aset tidak valid.")

        if not required_fields.issubset(asset):
            raise ValueError("Data salah satu aset tidak lengkap.")

        if not all(isinstance(asset[key], str) for key in required_fields):
            raise ValueError("Nilai data aset harus berupa teks.")

    return assets


def save_assets(assets):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(assets, file, indent=2, ensure_ascii=False)

    temporary_file.replace(DATA_FILE)