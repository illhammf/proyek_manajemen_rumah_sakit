from datetime import datetime

from models.dokter import Dokter
from models.pasien import Pasien
from models.obat import Obat
from models.pemeriksaan import Pemeriksaan
from services.file_manager import FileManager


class RumahSakit:
    """Class utama sistem.

    Class ini memakai composition karena memiliki objek FileManager,
    Dokter, Pasien, Obat, dan Pemeriksaan di dalamnya.
    """

    def __init__(self, nama_rumah_sakit="RS Sehat Sentosa", folder_data="data"):
        self.nama_rumah_sakit = nama_rumah_sakit
        self.file_manager = FileManager(folder_data)
        self.dokter = {}
        self.pasien = {}
        self.obat = {}
        self.pemeriksaan = {}
        self.muat_data()

    # -------------------- UTILITAS ID --------------------
    def _buat_id(self, prefix, koleksi):
        nomor = len(koleksi) + 1
        while f"{prefix}{nomor:03d}" in koleksi:
            nomor += 1
        return f"{prefix}{nomor:03d}"

    # -------------------- DATA DOKTER --------------------
    def tambah_dokter(self, nama, alamat, telepon, spesialis, jadwal_praktik):
        id_dokter = self._buat_id("D", self.dokter)
        self.dokter[id_dokter] = Dokter(id_dokter, nama, alamat, telepon, spesialis, jadwal_praktik)
        self.simpan_data()
        return id_dokter

    def ubah_dokter(self, id_dokter, nama=None, alamat=None, telepon=None, spesialis=None, jadwal_praktik=None):
        dokter = self.dokter.get(id_dokter)
        if not dokter:
            return False
        if nama:
            dokter.set_nama(nama)
        if alamat:
            dokter.set_alamat(alamat)
        if telepon:
            dokter.set_telepon(telepon)
        if spesialis:
            dokter.set_spesialis(spesialis)
        if jadwal_praktik:
            dokter.set_jadwal_praktik(jadwal_praktik)
        self.simpan_data()
        return True

    def hapus_dokter(self, id_dokter):
        if id_dokter in self.dokter:
            del self.dokter[id_dokter]
            self.simpan_data()
            return True
        return False

    def cari_dokter(self, keyword):
        keyword = keyword.lower()
        return [d for d in self.dokter.values() if keyword in d.get_nama().lower() or keyword in d.get_spesialis().lower()]

    def daftar_dokter(self):
        return list(self.dokter.values())

    # -------------------- DATA PASIEN --------------------
    def tambah_pasien(self, nama, alamat, telepon, umur, jenis_kelamin, no_rekam_medis):
        id_pasien = self._buat_id("P", self.pasien)
        self.pasien[id_pasien] = Pasien(id_pasien, nama, alamat, telepon, umur, jenis_kelamin, no_rekam_medis)
        self.simpan_data()
        return id_pasien

    def ubah_pasien(self, id_pasien, nama=None, alamat=None, telepon=None, umur=None, jenis_kelamin=None):
        pasien = self.pasien.get(id_pasien)
        if not pasien:
            return False
        if nama:
            pasien.set_nama(nama)
        if alamat:
            pasien.set_alamat(alamat)
        if telepon:
            pasien.set_telepon(telepon)
        if umur is not None and umur != "":
            pasien.set_umur(umur)
        if jenis_kelamin:
            pasien.set_jenis_kelamin(jenis_kelamin)
        self.simpan_data()
        return True

    def hapus_pasien(self, id_pasien):
        if id_pasien in self.pasien:
            del self.pasien[id_pasien]
            self.simpan_data()
            return True
        return False

    def cari_pasien(self, keyword):
        keyword = keyword.lower()
        return [p for p in self.pasien.values() if keyword in p.get_nama().lower() or keyword in p.get_no_rekam_medis().lower()]

    def daftar_pasien(self):
        return list(self.pasien.values())

    # -------------------- DATA OBAT --------------------
    def tambah_obat(self, nama_obat, harga, stok):
        kode_obat = self._buat_id("O", self.obat)
        self.obat[kode_obat] = Obat(kode_obat, nama_obat, harga, stok)
        self.simpan_data()
        return kode_obat

    def ubah_obat(self, kode_obat, nama_obat=None, harga=None):
        obat = self.obat.get(kode_obat)
        if not obat:
            return False
        if nama_obat:
            obat.set_nama_obat(nama_obat)
        if harga is not None and harga != "":
            obat.set_harga(harga)
        self.simpan_data()
        return True

    def tambah_stok_obat(self, kode_obat, jumlah):
        obat = self.obat.get(kode_obat)
        if not obat:
            return False
        obat.tambah_stok(jumlah)
        self.simpan_data()
        return True

    def hapus_obat(self, kode_obat):
        if kode_obat in self.obat:
            del self.obat[kode_obat]
            self.simpan_data()
            return True
        return False

    def cari_obat(self, keyword):
        keyword = keyword.lower()
        return [o for o in self.obat.values() if keyword in o.get_nama_obat().lower()]

    def daftar_obat(self):
        return list(self.obat.values())

    # -------------------- PEMERIKSAAN --------------------
    def buat_pemeriksaan(self, id_pasien, id_dokter, tanggal, keluhan, biaya_jasa=50000):
        if id_pasien not in self.pasien:
            raise ValueError("ID pasien tidak ditemukan")
        if id_dokter not in self.dokter:
            raise ValueError("ID dokter tidak ditemukan")
        datetime.strptime(tanggal, "%Y-%m-%d")
        id_pemeriksaan = self._buat_id("PM", self.pemeriksaan)
        self.pemeriksaan[id_pemeriksaan] = Pemeriksaan(
            id_pemeriksaan, id_pasien, id_dokter, tanggal, keluhan, biaya_jasa=biaya_jasa
        )
        self.simpan_data()
        return id_pemeriksaan

    def tambah_obat_ke_pemeriksaan(self, id_pemeriksaan, kode_obat, jumlah):
        pemeriksaan = self.pemeriksaan.get(id_pemeriksaan)
        obat = self.obat.get(kode_obat)
        if not pemeriksaan:
            raise ValueError("ID pemeriksaan tidak ditemukan")
        if not obat:
            raise ValueError("Kode obat tidak ditemukan")
        obat.kurangi_stok(jumlah)
        pemeriksaan.tambah_obat(kode_obat, jumlah)
        self.simpan_data()
        return True

    def selesaikan_pemeriksaan(self, id_pemeriksaan, diagnosa):
        pemeriksaan = self.pemeriksaan.get(id_pemeriksaan)
        if not pemeriksaan:
            return False
        pemeriksaan.set_diagnosa(diagnosa)
        pemeriksaan.set_status("Selesai")
        self.simpan_data()
        return True

    def batalkan_pemeriksaan(self, id_pemeriksaan):
        pemeriksaan = self.pemeriksaan.get(id_pemeriksaan)
        if not pemeriksaan:
            return False
        pemeriksaan.set_status("Dibatalkan")
        self.simpan_data()
        return True

    def cari_pemeriksaan(self, keyword):
        keyword = keyword.lower()
        hasil = []
        for periksa in self.pemeriksaan.values():
            pasien = self.pasien.get(periksa.get_id_pasien())
            dokter = self.dokter.get(periksa.get_id_dokter())
            nama_pasien = pasien.get_nama().lower() if pasien else ""
            nama_dokter = dokter.get_nama().lower() if dokter else ""
            if keyword in nama_pasien or keyword in nama_dokter or keyword in periksa.get_status().lower():
                hasil.append(periksa)
        return hasil

    def daftar_pemeriksaan(self):
        return list(self.pemeriksaan.values())

    def detail_pemeriksaan(self, id_pemeriksaan):
        periksa = self.pemeriksaan.get(id_pemeriksaan)
        if not periksa:
            return None
        pasien = self.pasien.get(periksa.get_id_pasien())
        dokter = self.dokter.get(periksa.get_id_dokter())
        total = periksa.hitung_total_biaya(self.obat)
        return {
            "pemeriksaan": periksa,
            "pasien": pasien,
            "dokter": dokter,
            "total_biaya": total,
            "obat": periksa.get_obat_diberikan(),
        }

    # -------------------- LAPORAN --------------------
    def laporan_ringkas(self):
        selesai = [p for p in self.pemeriksaan.values() if p.get_status() == "Selesai"]
        pendapatan = sum(p.hitung_total_biaya(self.obat) for p in selesai)
        return {
            "total_dokter": len(self.dokter),
            "total_pasien": len(self.pasien),
            "total_obat": len(self.obat),
            "total_pemeriksaan": len(self.pemeriksaan),
            "pemeriksaan_selesai": len(selesai),
            "estimasi_pendapatan": pendapatan,
        }

    def laporan_stok_rendah(self, batas=5):
        return [obat for obat in self.obat.values() if obat.get_stok() <= batas]

    def ekspor_laporan_txt(self, nama_file="laporan_rumah_sakit.txt"):
        laporan = self.laporan_ringkas()
        baris = [f"Laporan {self.nama_rumah_sakit}", "=" * 40]
        for k, v in laporan.items():
            baris.append(f"{k}: {v}")
        path = self.file_manager.folder_data / nama_file
        path.write_text("\n".join(baris), encoding="utf-8")
        return path

    # -------------------- PERSISTENSI DATA --------------------
    def simpan_data(self):
        self.file_manager.simpan_json("dokter.json", [d.to_dict() for d in self.dokter.values()])
        self.file_manager.simpan_json("pasien.json", [p.to_dict() for p in self.pasien.values()])
        self.file_manager.simpan_json("obat.json", [o.to_dict() for o in self.obat.values()])
        self.file_manager.simpan_json("pemeriksaan.json", [p.to_dict() for p in self.pemeriksaan.values()])

    def muat_data(self):
        self.dokter = {d["id_person"]: Dokter.from_dict(d) for d in self.file_manager.baca_json("dokter.json", [])}
        self.pasien = {p["id_person"]: Pasien.from_dict(p) for p in self.file_manager.baca_json("pasien.json", [])}
        self.obat = {o["kode_obat"]: Obat.from_dict(o) for o in self.file_manager.baca_json("obat.json", [])}
        self.pemeriksaan = {
            p["id_pemeriksaan"]: Pemeriksaan.from_dict(p)
            for p in self.file_manager.baca_json("pemeriksaan.json", [])
        }

    def isi_data_contoh(self):
        if self.dokter or self.pasien or self.obat or self.pemeriksaan:
            return False
        d1 = self.tambah_dokter("dr. Andi Pratama", "Jakarta", "0811111111", "Umum", "Senin-Rabu")
        d2 = self.tambah_dokter("dr. Sinta Lestari", "Tangerang", "0822222222", "Anak", "Kamis-Sabtu")
        p1 = self.tambah_pasien("Budi Santoso", "Tangerang", "0833333333", 20, "L", "RM001")
        self.tambah_pasien("Ayu Wulandari", "Serpong", "0844444444", 19, "P", "RM002")
        o1 = self.tambah_obat("Paracetamol", 5000, 30)
        self.tambah_obat("Amoxicillin", 12000, 20)
        pm1 = self.buat_pemeriksaan(p1, d1, "2026-07-15", "Demam dan pusing", 50000)
        self.tambah_obat_ke_pemeriksaan(pm1, o1, 2)
        self.selesaikan_pemeriksaan(pm1, "Gejala demam ringan")
        return True
