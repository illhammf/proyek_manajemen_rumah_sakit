from models.person import Person


class Dokter(Person):
    """Class turunan dari Person untuk menyimpan data dokter."""

    def __init__(self, id_person, nama, alamat, telepon, spesialis, jadwal_praktik):
        super().__init__(id_person, nama, alamat, telepon)
        self.__spesialis = spesialis      # private attribute
        self.__jadwal_praktik = jadwal_praktik

    def get_spesialis(self):
        return self.__spesialis

    def set_spesialis(self, spesialis):
        if not spesialis:
            raise ValueError("Spesialis tidak boleh kosong")
        self.__spesialis = spesialis

    def get_jadwal_praktik(self):
        return self.__jadwal_praktik

    def set_jadwal_praktik(self, jadwal_praktik):
        self.__jadwal_praktik = jadwal_praktik

    def tampilkan_info(self):
        # Polymorphism: method ini mengganti method milik Person.
        return (
            f"Dokter: {self._id_person} | {self._nama} | "
            f"Spesialis: {self.__spesialis} | Jadwal: {self.__jadwal_praktik}"
        )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "spesialis": self.__spesialis,
            "jadwal_praktik": self.__jadwal_praktik,
        })
        return data

    @staticmethod
    def from_dict(data):
        return Dokter(
            data["id_person"],
            data["nama"],
            data["alamat"],
            data["telepon"],
            data["spesialis"],
            data["jadwal_praktik"],
        )
