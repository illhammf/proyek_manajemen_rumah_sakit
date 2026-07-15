from services.rumah_sakit import RumahSakit
from utils import garis, input_tidak_kosong, input_angka, tampilkan_daftar


# Program utama berbasis menu agar mudah didemonstrasikan di VS Code.
rs = RumahSakit()


def menu_dokter():
    while True:
        garis()
        print("MENU DOKTER")
        print("1. Tambah dokter")
        print("2. Lihat dokter")
        print("3. Cari dokter")
        print("4. Ubah dokter")
        print("5. Hapus dokter")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input_tidak_kosong("Nama dokter: ")
            alamat = input_tidak_kosong("Alamat: ")
            telepon = input_tidak_kosong("Telepon: ")
            spesialis = input_tidak_kosong("Spesialis: ")
            jadwal = input_tidak_kosong("Jadwal praktik: ")
            id_baru = rs.tambah_dokter(nama, alamat, telepon, spesialis, jadwal)
            print(f"Dokter berhasil ditambahkan dengan ID {id_baru}.")
        elif pilihan == "2":
            tampilkan_daftar(rs.daftar_dokter())
        elif pilihan == "3":
            keyword = input_tidak_kosong("Kata kunci nama/spesialis: ")
            tampilkan_daftar(rs.cari_dokter(keyword))
        elif pilihan == "4":
            id_dokter = input_tidak_kosong("ID dokter: ")
            nama = input("Nama baru, kosongkan jika tidak diubah: ").strip() or None
            alamat = input("Alamat baru, kosongkan jika tidak diubah: ").strip() or None
            telepon = input("Telepon baru, kosongkan jika tidak diubah: ").strip() or None
            spesialis = input("Spesialis baru, kosongkan jika tidak diubah: ").strip() or None
            jadwal = input("Jadwal baru, kosongkan jika tidak diubah: ").strip() or None
            print("Berhasil diubah." if rs.ubah_dokter(id_dokter, nama, alamat, telepon, spesialis, jadwal) else "ID tidak ditemukan.")
        elif pilihan == "5":
            id_dokter = input_tidak_kosong("ID dokter: ")
            print("Berhasil dihapus." if rs.hapus_dokter(id_dokter) else "ID tidak ditemukan.")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


def menu_pasien():
    while True:
        garis()
        print("MENU PASIEN")
        print("1. Tambah pasien")
        print("2. Lihat pasien")
        print("3. Cari pasien")
        print("4. Ubah pasien")
        print("5. Hapus pasien")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input_tidak_kosong("Nama pasien: ")
            alamat = input_tidak_kosong("Alamat: ")
            telepon = input_tidak_kosong("Telepon: ")
            umur = input_angka("Umur: ")
            jenis_kelamin = input_tidak_kosong("Jenis kelamin L/P: ").upper()
            no_rm = input_tidak_kosong("Nomor rekam medis: ")
            try:
                id_baru = rs.tambah_pasien(nama, alamat, telepon, umur, jenis_kelamin, no_rm)
                print(f"Pasien berhasil ditambahkan dengan ID {id_baru}.")
            except ValueError as error:
                print(f"Gagal: {error}")
        elif pilihan == "2":
            tampilkan_daftar(rs.daftar_pasien())
        elif pilihan == "3":
            keyword = input_tidak_kosong("Kata kunci nama/rekam medis: ")
            tampilkan_daftar(rs.cari_pasien(keyword))
        elif pilihan == "4":
            id_pasien = input_tidak_kosong("ID pasien: ")
            nama = input("Nama baru, kosongkan jika tidak diubah: ").strip() or None
            alamat = input("Alamat baru, kosongkan jika tidak diubah: ").strip() or None
            telepon = input("Telepon baru, kosongkan jika tidak diubah: ").strip() or None
            umur = input("Umur baru, kosongkan jika tidak diubah: ").strip()
            jk = input("Jenis kelamin baru L/P, kosongkan jika tidak diubah: ").strip().upper() or None
            print("Berhasil diubah." if rs.ubah_pasien(id_pasien, nama, alamat, telepon, umur, jk) else "ID tidak ditemukan.")
        elif pilihan == "5":
            id_pasien = input_tidak_kosong("ID pasien: ")
            print("Berhasil dihapus." if rs.hapus_pasien(id_pasien) else "ID tidak ditemukan.")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


def menu_obat():
    while True:
        garis()
        print("MENU OBAT")
        print("1. Tambah obat")
        print("2. Lihat obat")
        print("3. Cari obat")
        print("4. Ubah obat")
        print("5. Tambah stok")
        print("6. Hapus obat")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input_tidak_kosong("Nama obat: ")
            harga = input_angka("Harga: ")
            stok = input_angka("Stok awal: ")
            id_baru = rs.tambah_obat(nama, harga, stok)
            print(f"Obat berhasil ditambahkan dengan kode {id_baru}.")
        elif pilihan == "2":
            tampilkan_daftar(rs.daftar_obat())
        elif pilihan == "3":
            keyword = input_tidak_kosong("Kata kunci obat: ")
            tampilkan_daftar(rs.cari_obat(keyword))
        elif pilihan == "4":
            kode = input_tidak_kosong("Kode obat: ")
            nama = input("Nama baru, kosongkan jika tidak diubah: ").strip() or None
            harga = input("Harga baru, kosongkan jika tidak diubah: ").strip()
            print("Berhasil diubah." if rs.ubah_obat(kode, nama, harga) else "Kode tidak ditemukan.")
        elif pilihan == "5":
            kode = input_tidak_kosong("Kode obat: ")
            jumlah = input_angka("Jumlah tambah stok: ")
            try:
                print("Stok berhasil ditambah." if rs.tambah_stok_obat(kode, jumlah) else "Kode tidak ditemukan.")
            except ValueError as error:
                print(f"Gagal: {error}")
        elif pilihan == "6":
            kode = input_tidak_kosong("Kode obat: ")
            print("Berhasil dihapus." if rs.hapus_obat(kode) else "Kode tidak ditemukan.")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


def menu_pemeriksaan():
    while True:
        garis()
        print("MENU PEMERIKSAAN")
        print("1. Buat jadwal pemeriksaan")
        print("2. Lihat pemeriksaan")
        print("3. Detail pemeriksaan")
        print("4. Tambah obat ke pemeriksaan")
        print("5. Selesaikan pemeriksaan")
        print("6. Batalkan pemeriksaan")
        print("7. Cari pemeriksaan")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                id_pasien = input_tidak_kosong("ID pasien: ")
                id_dokter = input_tidak_kosong("ID dokter: ")
                tanggal = input_tidak_kosong("Tanggal YYYY-MM-DD: ")
                keluhan = input_tidak_kosong("Keluhan: ")
                biaya = input_angka("Biaya jasa dokter: ", default=50000)
                id_baru = rs.buat_pemeriksaan(id_pasien, id_dokter, tanggal, keluhan, biaya)
                print(f"Pemeriksaan dibuat dengan ID {id_baru}.")
            elif pilihan == "2":
                tampilkan_daftar(rs.daftar_pemeriksaan())
            elif pilihan == "3":
                id_pm = input_tidak_kosong("ID pemeriksaan: ")
                detail = rs.detail_pemeriksaan(id_pm)
                if not detail:
                    print("ID pemeriksaan tidak ditemukan.")
                else:
                    print(detail["pemeriksaan"].tampilkan_info())
                    print(detail["pasien"].tampilkan_info() if detail["pasien"] else "Pasien tidak ditemukan")
                    print(detail["dokter"].tampilkan_info() if detail["dokter"] else "Dokter tidak ditemukan")
                    print(f"Total biaya: Rp{detail['total_biaya']:,.0f}")
                    print(f"Obat: {detail['obat']}")
            elif pilihan == "4":
                id_pm = input_tidak_kosong("ID pemeriksaan: ")
                kode_obat = input_tidak_kosong("Kode obat: ")
                jumlah = input_angka("Jumlah: ")
                rs.tambah_obat_ke_pemeriksaan(id_pm, kode_obat, jumlah)
                print("Obat berhasil ditambahkan ke pemeriksaan.")
            elif pilihan == "5":
                id_pm = input_tidak_kosong("ID pemeriksaan: ")
                diagnosa = input_tidak_kosong("Diagnosa: ")
                print("Pemeriksaan selesai." if rs.selesaikan_pemeriksaan(id_pm, diagnosa) else "ID tidak ditemukan.")
            elif pilihan == "6":
                id_pm = input_tidak_kosong("ID pemeriksaan: ")
                print("Pemeriksaan dibatalkan." if rs.batalkan_pemeriksaan(id_pm) else "ID tidak ditemukan.")
            elif pilihan == "7":
                keyword = input_tidak_kosong("Kata kunci pasien/dokter/status: ")
                tampilkan_daftar(rs.cari_pemeriksaan(keyword))
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError as error:
            print(f"Gagal: {error}")


def menu_laporan():
    while True:
        garis()
        print("MENU LAPORAN")
        print("1. Laporan ringkas")
        print("2. Laporan stok obat rendah")
        print("3. Ekspor laporan TXT")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            laporan = rs.laporan_ringkas()
            for k, v in laporan.items():
                print(f"{k}: {v}")
        elif pilihan == "2":
            batas = input_angka("Batas stok rendah: ", default=5)
            tampilkan_daftar(rs.laporan_stok_rendah(batas))
        elif pilihan == "3":
            path = rs.ekspor_laporan_txt()
            print(f"Laporan berhasil diekspor ke {path}")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


def main():
    while True:
        garis()
        print("SISTEM MANAJEMEN RUMAH SAKIT BERBASIS OOP")
        print(rs.nama_rumah_sakit)
        print("1. Kelola dokter")
        print("2. Kelola pasien")
        print("3. Kelola obat")
        print("4. Kelola pemeriksaan")
        print("5. Laporan")
        print("6. Isi data contoh")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_dokter()
        elif pilihan == "2":
            menu_pasien()
        elif pilihan == "3":
            menu_obat()
        elif pilihan == "4":
            menu_pemeriksaan()
        elif pilihan == "5":
            menu_laporan()
        elif pilihan == "6":
            print("Data contoh berhasil dibuat." if rs.isi_data_contoh() else "Data sudah ada, data contoh tidak ditambahkan.")
        elif pilihan == "0":
            print("Program selesai. Data sudah tersimpan otomatis.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()
