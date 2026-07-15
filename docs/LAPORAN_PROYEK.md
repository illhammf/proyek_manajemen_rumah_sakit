# Laporan Proyek

## Judul
Sistem Manajemen Rumah Sakit Berbasis Object-Oriented Programming.

## 1. Latar Belakang
Rumah sakit membutuhkan sistem informasi sederhana untuk mengelola data layanan dasar. Data yang sering dikelola meliputi pasien, dokter, jadwal pemeriksaan, obat, dan rekam medis. Jika data tersebut dicatat secara manual, proses pencarian, pembaruan, dan pelaporan membutuhkan waktu lebih lama. Risiko kesalahan pencatatan juga meningkat.

Proyek ini mengembangkan aplikasi berbasis Python dengan pendekatan Object-Oriented Programming. Pendekatan OOP dipilih karena data rumah sakit memiliki entitas yang jelas. Entitas tersebut dapat dimodelkan menjadi class seperti `Person`, `Dokter`, `Pasien`, `Obat`, `Pemeriksaan`, dan `RumahSakit`.

## 2. Analisis Kebutuhan
### 2.1 Kebutuhan Fungsional
1. Sistem dapat menambah data dokter.
2. Sistem dapat menampilkan data dokter.
3. Sistem dapat mencari dokter berdasarkan nama atau spesialis.
4. Sistem dapat mengubah data dokter.
5. Sistem dapat menghapus data dokter.
6. Sistem dapat menambah data pasien.
7. Sistem dapat menampilkan data pasien.
8. Sistem dapat mencari pasien berdasarkan nama atau nomor rekam medis.
9. Sistem dapat mengubah data pasien.
10. Sistem dapat menghapus data pasien.
11. Sistem dapat menambah data obat.
12. Sistem dapat menampilkan data obat.
13. Sistem dapat mengubah data obat.
14. Sistem dapat menambah stok obat.
15. Sistem dapat menghapus data obat.
16. Sistem dapat membuat jadwal pemeriksaan.
17. Sistem dapat menambahkan obat pada pemeriksaan.
18. Sistem dapat menyelesaikan pemeriksaan dengan diagnosa.
19. Sistem dapat membatalkan pemeriksaan.
20. Sistem dapat membuat laporan ringkas.

### 2.2 Kebutuhan Nonfungsional
1. Sistem dapat dijalankan melalui terminal VS Code.
2. Data tersimpan otomatis menggunakan file JSON.
3. Kode program diberi komentar agar mudah dipahami.
4. Struktur folder dibuat modular.
5. Sistem dapat diuji menggunakan unit test.

## 3. Desain Class
### 3.1 Person
Class induk untuk data manusia. Atribut utama meliputi ID, nama, alamat, dan telepon.

### 3.2 Dokter
Class turunan dari `Person`. Class ini menambahkan atribut spesialis dan jadwal praktik.

### 3.3 Pasien
Class turunan dari `Person`. Class ini menambahkan atribut umur, jenis kelamin, dan nomor rekam medis.

### 3.4 Obat
Class untuk menyimpan kode obat, nama obat, harga, dan stok.

### 3.5 Pemeriksaan
Class untuk menyimpan jadwal pemeriksaan, keluhan, diagnosa, status, biaya jasa, dan obat yang diberikan.

### 3.6 RumahSakit
Class utama yang mengelola seluruh objek dokter, pasien, obat, dan pemeriksaan.

### 3.7 FileManager
Class pendukung untuk membaca dan menyimpan data JSON.

## 4. Implementasi Konsep OOP
### 4.1 Class
Program memiliki tujuh class utama, yaitu `Person`, `Dokter`, `Pasien`, `Obat`, `Pemeriksaan`, `RumahSakit`, dan `FileManager`.

### 4.2 Object
Objek dibuat dari setiap class. Contohnya objek dokter dibuat melalui `Dokter(...)`, pasien melalui `Pasien(...)`, dan obat melalui `Obat(...)`.

### 4.3 Inheritance
Class `Dokter` dan `Pasien` mewarisi class `Person`.

### 4.4 Encapsulation
Atribut pada class menggunakan protected attribute seperti `_nama` dan private attribute seperti `__spesialis`, `__umur`, dan `__stok`. Akses data dilakukan melalui getter dan setter.

### 4.5 Polymorphism
Method `tampilkan_info()` dioverride pada class `Dokter`, `Pasien`, `Obat`, dan `Pemeriksaan`. Setiap class menampilkan informasi dengan format yang berbeda.

### 4.6 Composition
Class `RumahSakit` memiliki objek `FileManager`, `Dokter`, `Pasien`, `Obat`, dan `Pemeriksaan`. Class `Pemeriksaan` juga berelasi dengan data obat untuk menghitung biaya.

### 4.7 Constructor
Setiap class memiliki constructor `__init__()`.

## 5. Pengujian
Pengujian dilakukan menggunakan `unittest`. Skenario pengujian meliputi penambahan data dasar, pemeriksaan dan total biaya, penyelesaian pemeriksaan, pencarian pasien, dan persistensi JSON.

## 6. Kesimpulan
Aplikasi berhasil memenuhi kebutuhan dasar sistem manajemen rumah sakit. Program juga memenuhi konsep OOP yang diminta, yaitu class, object, inheritance, encapsulation, polymorphism, composition, constructor, dan method yang relevan. Aplikasi dapat dikembangkan lebih lanjut dengan fitur login, database SQLite, dan tampilan GUI.
