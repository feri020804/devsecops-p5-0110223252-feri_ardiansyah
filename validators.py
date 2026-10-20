VALID_CONDITIONS = ("baik", "rusak ringan", "rusak berat")


def validate_text(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} tidak boleh kosong.")

    cleaned = value.strip()

    if len(cleaned) > 100:
        raise ValueError(f"{field_name} maksimal 100 karakter.")

    return cleaned


def validate_condition(value):
    if not isinstance(value, str):
        raise ValueError("Kondisi harus berupa teks.")

    condition = value.strip().lower()

    if condition not in VALID_CONDITIONS:
        raise ValueError(
            "Kondisi harus: baik, rusak ringan, atau rusak berat."
        )

    return condition