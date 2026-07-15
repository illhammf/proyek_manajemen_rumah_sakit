def garis():
    print("-" * 70)


def input_tidak_kosong(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")


def input_angka(pesan, default=None):
    while True:
        nilai = input(pesan).strip()
        if nilai == "" and default is not None:
            return default
        try:
            return int(nilai)
        except ValueError:
            print("Input harus berupa angka.")


def tampilkan_daftar(objek_list):
    if not objek_list:
        print("Data belum tersedia.")
        return
    for item in objek_list:
        print(item.tampilkan_info())
