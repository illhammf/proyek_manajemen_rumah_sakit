from models.person import Person


class Pasien(Person):
    """Class turunan dari Person untuk menyimpan data pasien."""

    def __init__(self, id_person, nama, alamat, telepon, umur, jenis_kelamin, no_rekam_medis):
        super().__init__(id_person, nama, alamat, telepon)
        self.__umur = int(umur)
        self.__jenis_kelamin = jenis_kelamin
        self.__no_rekam_medis = no_rekam_medis

    def get_umur(self):
        return self.__umur

    def set_umur(self, umur):
        umur = int(umur)
        if umur < 0:
            raise ValueError("Umur tidak boleh negatif")
        self.__umur = umur

    def get_jenis_kelamin(self):
        return self.__jenis_kelamin

    def set_jenis_kelamin(self, jenis_kelamin):
        if jenis_kelamin.upper() not in ["L", "P"]:
            raise ValueError("Jenis kelamin harus L atau P")
        self.__jenis_kelamin = jenis_kelamin.upper()

    def get_no_rekam_medis(self):
        return self.__no_rekam_medis

    def set_no_rekam_medis(self, no_rekam_medis):
        if not no_rekam_medis:
            raise ValueError("Nomor rekam medis tidak boleh kosong")
        self.__no_rekam_medis = no_rekam_medis

    def tampilkan_info(self):
        # Polymorphism: format informasi pasien berbeda dengan dokter.
        return (
            f"Pasien: {self._id_person} | {self._nama} | "
            f"RM: {self.__no_rekam_medis} | Umur: {self.__umur} | JK: {self.__jenis_kelamin}"
        )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "umur": self.__umur,
            "jenis_kelamin": self.__jenis_kelamin,
            "no_rekam_medis": self.__no_rekam_medis,
        })
        return data

    @staticmethod
    def from_dict(data):
        return Pasien(
            data["id_person"],
            data["nama"],
            data["alamat"],
            data["telepon"],
            data["umur"],
            data["jenis_kelamin"],
            data["no_rekam_medis"],
        )
