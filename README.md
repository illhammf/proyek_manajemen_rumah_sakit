# Sistem Manajemen Rumah Sakit Berbasis Object-Oriented Programming

Proyek ini dibuat untuk tugas Bahasa Pemrograman menggunakan Python dan konsep Object-Oriented Programming.

## Tema
Sistem Manajemen Rumah Sakit Berbasis Object-Oriented Programming.

## Fitur Utama
1. Kelola data dokter.
2. Kelola data pasien.
3. Kelola data obat dan stok.
4. Kelola jadwal pemeriksaan.
5. Kelola rekam medis sederhana berupa keluhan dan diagnosa.
6. Tambah obat ke pemeriksaan.
7. Hitung total biaya pemeriksaan.
8. Laporan ringkas rumah sakit.
9. Laporan stok obat rendah.
10. Penyimpanan data otomatis menggunakan JSON.

## Cara Menjalankan di VS Code
1. Ekstrak ZIP.
2. Buka folder proyek di VS Code.
3. Pastikan Python sudah terpasang.
4. Buka terminal pada folder proyek.
5. Jalankan perintah berikut:

```bash
python main.py
```

Pada Windows, jika `python` tidak terbaca, gunakan:

```bash
py main.py
```

## Cara Menjalankan Pengujian
```bash
python run_tests.py
```

## Struktur Folder
```text
Sistem_Manajemen_Rumah_Sakit_OOP/
├── main.py
├── utils.py
├── run_tests.py
├── requirements.txt
├── models/
│   ├── person.py
│   ├── dokter.py
│   ├── pasien.py
│   ├── obat.py
│   └── pemeriksaan.py
├── services/
│   ├── file_manager.py
│   └── rumah_sakit.py
├── data/
├── tests/
└── docs/
```

## Akun Login
Program ini tidak memakai login agar demo lebih cepat. Fokus proyek berada pada penerapan OOP.
