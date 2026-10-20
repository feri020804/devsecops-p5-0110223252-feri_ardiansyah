from models import create_asset
from storage import load_assets, save_assets
from validators import validate_condition, validate_text


def register_asset(name, location, condition):
    name = validate_text(name, "Nama aset")
    location = validate_text(location, "Lokasi")
    condition = validate_condition(condition)

    assets = load_assets()
    asset = create_asset(name, location, condition)

    assets.append(asset)
    save_assets(assets)

    return asset


def list_assets():
    return load_assets()


def update_asset_condition(asset_id, condition):
    asset_id = validate_text(asset_id, "ID aset")
    condition = validate_condition(condition)
    assets = load_assets()

    for asset in assets:
        if asset["id"] == asset_id:
            asset["condition"] = condition
            save_assets(assets)
            return asset

    raise ValueError("Aset dengan ID tersebut tidak ditemukan.")