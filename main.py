from services import (
    list_assets,
    register_asset,
    update_asset_condition,
)


def display_assets():
    assets = list_assets()

    if not assets:
        print("\nBelum ada aset yang terdaftar.")
        return

    print("\nDAFTAR ASET")

    for number, asset in enumerate(assets, start=1):
        print(f"\n{number}. {asset['name']}")
        print(f"   ID      : {asset['id']}")
        print(f"   Lokasi  : {asset['location']}")
        print(f"   Kondisi : {asset['condition']}")


def main():
    while True:
        print("\n=== SIMPLE ASSET INVENTORY ===")
        print("1. Tambah aset")
        print("2. Lihat daftar aset")
        print("3. Perbarui kondisi aset")
        print("0. Keluar")

        choice = input("Pilih menu: ").strip()

        try:
            if choice == "1":
                name = input("Nama aset: ")
                location = input("Lokasi: ")
                condition = input(
                    "Kondisi (baik/rusak ringan/rusak berat): "
                )

                asset = register_asset(name, location, condition)
                print(f"Aset berhasil ditambahkan. ID: {asset['id']}")

            elif choice == "2":
                display_assets()

            elif choice == "3":
                asset_id = input("Masukkan ID lengkap aset: ")
                condition = input(
                    "Kondisi baru (baik/rusak ringan/rusak berat): "
                )

                asset = update_asset_condition(asset_id, condition)
                print(
                    f"Kondisi {asset['name']} diperbarui "
                    f"menjadi {asset['condition']}."
                )

            elif choice == "0":
                print("Aplikasi ditutup.")
                break

            else:
                print("Pilihan menu tidak tersedia.")

        except (ValueError, OSError) as error:
            print(f"Gagal: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nAplikasi ditutup.")