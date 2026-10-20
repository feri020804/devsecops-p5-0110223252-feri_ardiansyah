import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from services import (
    list_assets,
    register_asset,
    update_asset_condition,
)


class TestAssetInventory(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_directory.cleanup)

        test_data_file = (
            Path(self.temp_directory.name) / "assets.json"
        )
        self.storage_patch = patch(
            "storage.DATA_FILE", test_data_file
        )
        self.storage_patch.start()
        self.addCleanup(self.storage_patch.stop)

    def test_initial_inventory_is_empty(self):
        self.assertEqual(list_assets(), [])

    def test_register_asset_is_saved(self):
        asset = register_asset("AC", "Depok", "baik")

        self.assertTrue(asset["id"])
        self.assertEqual(list_assets(), [asset])

    def test_update_condition_is_saved(self):
        asset = register_asset("AC", "Depok", "baik")

        update_asset_condition(asset["id"], "rusak ringan")

        self.assertEqual(
            list_assets()[0]["condition"], "rusak ringan"
        )

    def test_empty_name_is_rejected(self):
        with self.assertRaises(ValueError):
            register_asset("", "Depok", "baik")

        self.assertEqual(list_assets(), [])

    def test_invalid_condition_is_rejected(self):
        with self.assertRaises(ValueError):
            register_asset("AC", "Depok", "tidak valid")

        self.assertEqual(list_assets(), [])

    def test_unknown_id_is_rejected(self):
        asset = register_asset("AC", "Depok", "baik")

        with self.assertRaises(ValueError):
            update_asset_condition("id-tidak-ada", "rusak berat")

        self.assertEqual(list_assets(), [asset])


if __name__ == "__main__":
    unittest.main()