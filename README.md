# Simple Asset Inventory

Aplikasi inventaris aset berbasis terminal untuk mencatat aset, menampilkan daftar aset, dan memperbarui kondisi aset. Data disimpan dalam file JSON agar tetap tersedia setelah aplikasi ditutup.

## Identitas

- Nama: Syahrul Mubaroq
- NIM: 0110223236
- Program Studi: Teknik Informatika
- Tugas: DevSecOps Pertemuan 5

## Fitur

- Menambahkan aset dengan ID unik.
- Menampilkan daftar aset beserta lokasi dan kondisinya.
- Memperbarui kondisi aset berdasarkan ID.
- Memvalidasi input nama, lokasi, dan kondisi aset.
- Menyimpan data secara lokal dalam file JSON.

Kondisi aset yang tersedia:
- baik
- rusak ringan
- rusak berat

## Bahasa dan Teknologi

- Python 3.
- Library bawaan: json, pathlib, dan uuid.
- Tanpa framework dan tanpa dependencies eksternal untuk menjalankan aplikasi.

## Struktur Source Code

| File | Fungsi |
|---|---|
| main.py | Menampilkan menu dan menerima input pengguna |
| models.py | Membentuk data aset dengan ID unik |
| validators.py | Memvalidasi input pengguna |
| storage.py | Membaca dan menyimpan data JSON |
| services.py | Menangani penambahan, penampilan, dan pembaruan aset |

File data/assets.json dibuat otomatis setelah aset pertama disimpan.

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Buka terminal di folder proyek.
3. Jalankan aplikasi.

Windows:

```bash
py main.py
```

Linux atau WSL:

```bash
python3 main.py
```

Gunakan menu terminal:
- 1: Tambah aset.
- 2: Lihat daftar aset.
- 3: Perbarui kondisi aset.
- 0: Keluar.

Untuk memperbarui kondisi, salin ID lengkap aset dari menu daftar aset.

## Pengujian Manual

Pengujian berikut telah dilakukan dan berhasil:

| Pengujian | Hasil |
|---|---|
| Menambahkan aset | Aset tersimpan dengan ID unik |
| Menampilkan daftar aset | Data aset tampil sesuai input |
| Memperbarui kondisi | Kondisi baru tampil pada daftar aset |
| Mengisi nama kosong | Input ditolak dengan pesan validasi |
| Menjalankan ulang aplikasi | Data dan perubahan kondisi tetap tersimpan |

## Overview Pipeline DevSecOps

Pipeline direncanakan menggunakan GitHub Actions dengan konfigurasi
.github/workflows/devsecops.yml.

Workflow akan dipicu oleh:
- Push ke branch main.
- Pull request menuju branch main.

Tahapan pipeline:
1. Job build: menyiapkan Python, memeriksa kompilasi source code, dan menjalankan unit test yang akan ditambahkan.
2. Job sast-scan: menjalankan analisis keamanan kode menggunakan Bandit setelah job build berhasil.
3. Quality Gate: menentukan kelulusan berdasarkan hasil pengujian dan ambang temuan keamanan yang akan dikonfigurasi.

Kedua job akan menggunakan runner ubuntu-latest.
Job sast-scan akan bergantung pada job build melalui needs: build.

Status: workflow, unit test otomatis, SAST, dan Quality Gate belum diimplementasikan. Dokumentasi ini akan diperbarui setelah konfigurasi dan pengujian pipeline selesai.
# devsecops-p5-0110223252-feri_ardiansyah
