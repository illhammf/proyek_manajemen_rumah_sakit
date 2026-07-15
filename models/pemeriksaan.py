from datetime import datetime


class Pemeriksaan:
    """Class untuk jadwal pemeriksaan dan rekam medis sederhana.

    Pemeriksaan menyimpan relasi ke pasien, dokter, dan daftar obat.
    Relasi ini membuat sistem dapat mempraktikkan composition.
    """

    def __init__(
        self,
        id_pemeriksaan,
        id_pasien,
        id_dokter,
        tanggal,
        keluhan,
        diagnosa="Belum diperiksa",
        status="Terjadwal",
        biaya_jasa=50000,
        obat_diberikan=None,
    ):
        self.__id_pemeriksaan = id_pemeriksaan
        self.__id_pasien = id_pasien
        self.__id_dokter = id_dokter
        self.__tanggal = tanggal
        self.__keluhan = keluhan
        self.__diagnosa = diagnosa
        self.__status = status
        self.__biaya_jasa = float(biaya_jasa)
        self.__obat_diberikan = obat_diberikan or []

    def get_id_pemeriksaan(self):
        return self.__id_pemeriksaan

    def get_id_pasien(self):
        return self.__id_pasien

    def get_id_dokter(self):
        return self.__id_dokter

    def get_tanggal(self):
        return self.__tanggal

    def set_tanggal(self, tanggal):
        # Validasi sederhana agar format tanggal konsisten.
        datetime.strptime(tanggal, "%Y-%m-%d")
        self.__tanggal = tanggal

    def get_keluhan(self):
        return self.__keluhan

    def set_keluhan(self, keluhan):
        if not keluhan:
            raise ValueError("Keluhan tidak boleh kosong")
        self.__keluhan = keluhan

    def get_diagnosa(self):
        return self.__diagnosa

    def set_diagnosa(self, diagnosa):
        if not diagnosa:
            raise ValueError("Diagnosa tidak boleh kosong")
        self.__diagnosa = diagnosa

    def get_status(self):
        return self.__status

    def set_status(self, status):
        daftar_status = ["Terjadwal", "Selesai", "Dibatalkan"]
        if status not in daftar_status:
            raise ValueError(f"Status harus salah satu dari {daftar_status}")
        self.__status = status

    def get_biaya_jasa(self):
        return self.__biaya_jasa

    def set_biaya_jasa(self, biaya_jasa):
        biaya_jasa = float(biaya_jasa)
        if biaya_jasa < 0:
            raise ValueError("Biaya jasa tidak boleh negatif")
        self.__biaya_jasa = biaya_jasa

    def get_obat_diberikan(self):
        return list(self.__obat_diberikan)

    def tambah_obat(self, kode_obat, jumlah):
        jumlah = int(jumlah)
        if jumlah <= 0:
            raise ValueError("Jumlah obat harus lebih dari 0")
        self.__obat_diberikan.append({"kode_obat": kode_obat, "jumlah": jumlah})

    def hitung_total_biaya(self, data_obat):
        total_obat = 0
        for item in self.__obat_diberikan:
            obat = data_obat.get(item["kode_obat"])
            if obat:
                total_obat += obat.get_harga() * item["jumlah"]
        return self.__biaya_jasa + total_obat

    def tampilkan_info(self):
        return (
            f"{self.__id_pemeriksaan} | Pasien: {self.__id_pasien} | Dokter: {self.__id_dokter} | "
            f"Tanggal: {self.__tanggal} | Status: {self.__status}"
        )

    def to_dict(self):
        return {
            "id_pemeriksaan": self.__id_pemeriksaan,
            "id_pasien": self.__id_pasien,
            "id_dokter": self.__id_dokter,
            "tanggal": self.__tanggal,
            "keluhan": self.__keluhan,
            "diagnosa": self.__diagnosa,
            "status": self.__status,
            "biaya_jasa": self.__biaya_jasa,
            "obat_diberikan": self.__obat_diberikan,
        }

    @staticmethod
    def from_dict(data):
        return Pemeriksaan(
            data["id_pemeriksaan"],
            data["id_pasien"],
            data["id_dokter"],
            data["tanggal"],
            data["keluhan"],
            data.get("diagnosa", "Belum diperiksa"),
            data.get("status", "Terjadwal"),
            data.get("biaya_jasa", 50000),
            data.get("obat_diberikan", []),
        )
