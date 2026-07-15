import tempfile
import unittest

from services.rumah_sakit import RumahSakit


class TestRumahSakit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.rs = RumahSakit(folder_data=self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_tambah_data_dasar(self):
        id_dokter = self.rs.tambah_dokter("dr. Budi", "Jakarta", "081", "Umum", "Senin")
        id_pasien = self.rs.tambah_pasien("Ani", "Tangerang", "082", 21, "P", "RM100")
        kode_obat = self.rs.tambah_obat("Paracetamol", 5000, 10)
        self.assertEqual(id_dokter, "D001")
        self.assertEqual(id_pasien, "P001")
        self.assertEqual(kode_obat, "O001")

    def test_pemeriksaan_dan_total_biaya(self):
        id_dokter = self.rs.tambah_dokter("dr. Budi", "Jakarta", "081", "Umum", "Senin")
        id_pasien = self.rs.tambah_pasien("Ani", "Tangerang", "082", 21, "P", "RM100")
        kode_obat = self.rs.tambah_obat("Paracetamol", 5000, 10)
        id_pm = self.rs.buat_pemeriksaan(id_pasien, id_dokter, "2026-07-15", "Demam", 50000)
        self.rs.tambah_obat_ke_pemeriksaan(id_pm, kode_obat, 2)
        detail = self.rs.detail_pemeriksaan(id_pm)
        self.assertEqual(detail["total_biaya"], 60000)
        self.assertEqual(self.rs.obat[kode_obat].get_stok(), 8)

    def test_selesaikan_pemeriksaan(self):
        id_dokter = self.rs.tambah_dokter("dr. Budi", "Jakarta", "081", "Umum", "Senin")
        id_pasien = self.rs.tambah_pasien("Ani", "Tangerang", "082", 21, "P", "RM100")
        id_pm = self.rs.buat_pemeriksaan(id_pasien, id_dokter, "2026-07-15", "Demam")
        self.assertTrue(self.rs.selesaikan_pemeriksaan(id_pm, "Demam ringan"))
        self.assertEqual(self.rs.pemeriksaan[id_pm].get_status(), "Selesai")

    def test_pencarian_pasien(self):
        self.rs.tambah_pasien("Ani Putri", "Tangerang", "082", 21, "P", "RM100")
        hasil = self.rs.cari_pasien("ani")
        self.assertEqual(len(hasil), 1)

    def test_persistensi_json(self):
        self.rs.tambah_dokter("dr. Budi", "Jakarta", "081", "Umum", "Senin")
        rs_baru = RumahSakit(folder_data=self.tmp.name)
        self.assertEqual(len(rs_baru.daftar_dokter()), 1)


if __name__ == "__main__":
    unittest.main()
