# Peta Implementasi OOP

| Konsep OOP | Implementasi dalam Program |
|---|---|
| Class | `Person`, `Dokter`, `Pasien`, `Obat`, `Pemeriksaan`, `RumahSakit`, `FileManager` |
| Object | Objek dokter, pasien, obat, dan pemeriksaan dibuat saat data ditambahkan |
| Inheritance | `Dokter(Person)` dan `Pasien(Person)` |
| Encapsulation | Atribut `_nama`, `__spesialis`, `__umur`, `__stok`, dan atribut private lain |
| Getter Setter | `get_nama()`, `set_nama()`, `get_stok()`, `set_harga()`, dan lainnya |
| Polymorphism | Method `tampilkan_info()` dioverride di beberapa class |
| Composition | `RumahSakit` memiliki objek `FileManager`, `Dokter`, `Pasien`, `Obat`, dan `Pemeriksaan` |
| Constructor | Semua class menggunakan `__init__()` |
| Method | Lebih dari 20 method tersedia di seluruh class |
