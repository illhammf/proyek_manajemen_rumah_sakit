class Obat:
    """Class untuk data obat dan stok obat."""

    def __init__(self, kode_obat, nama_obat, harga, stok):
        self.__kode_obat = kode_obat
        self.__nama_obat = nama_obat
        self.__harga = float(harga)
        self.__stok = int(stok)

    def get_kode_obat(self):
        return self.__kode_obat

    def get_nama_obat(self):
        return self.__nama_obat

    def set_nama_obat(self, nama_obat):
        if not nama_obat:
            raise ValueError("Nama obat tidak boleh kosong")
        self.__nama_obat = nama_obat

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga):
        harga = float(harga)
        if harga < 0:
            raise ValueError("Harga tidak boleh negatif")
        self.__harga = harga

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        jumlah = int(jumlah)
        if jumlah <= 0:
            raise ValueError("Jumlah tambah stok harus lebih dari 0")
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        jumlah = int(jumlah)
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0")
        if jumlah > self.__stok:
            raise ValueError("Stok obat tidak mencukupi")
        self.__stok -= jumlah

    def tampilkan_info(self):
        return f"{self.__kode_obat} | {self.__nama_obat} | Rp{self.__harga:,.0f} | Stok: {self.__stok}"

    def to_dict(self):
        return {
            "kode_obat": self.__kode_obat,
            "nama_obat": self.__nama_obat,
            "harga": self.__harga,
            "stok": self.__stok,
        }

    @staticmethod
    def from_dict(data):
        return Obat(data["kode_obat"], data["nama_obat"], data["harga"], data["stok"])
