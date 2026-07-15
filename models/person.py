class Person:
    """Class induk untuk manusia di sistem rumah sakit.

    Konsep OOP yang dipakai:
    - Encapsulation: atribut dibuat protected dengan awalan _.
    - Inheritance: class Dokter dan Pasien akan mewarisi class ini.
    - Polymorphism: method tampilkan_info() akan dioverride oleh class turunan.
    """

    def __init__(self, id_person, nama, alamat, telepon):
        self._id_person = id_person
        self._nama = nama
        self._alamat = alamat
        self._telepon = telepon

    # Getter dan setter dipakai agar akses atribut lebih terkontrol.
    def get_id_person(self):
        return self._id_person

    def set_id_person(self, id_person):
        if not id_person:
            raise ValueError("ID tidak boleh kosong")
        self._id_person = id_person

    def get_nama(self):
        return self._nama

    def set_nama(self, nama):
        if not nama:
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama

    def get_alamat(self):
        return self._alamat

    def set_alamat(self, alamat):
        self._alamat = alamat

    def get_telepon(self):
        return self._telepon

    def set_telepon(self, telepon):
        if not telepon:
            raise ValueError("Telepon tidak boleh kosong")
        self._telepon = telepon

    def tampilkan_info(self):
        """Method ini akan dioverride oleh class Dokter dan Pasien."""
        return f"{self._id_person} | {self._nama} | {self._telepon}"

    def to_dict(self):
        return {
            "id_person": self._id_person,
            "nama": self._nama,
            "alamat": self._alamat,
            "telepon": self._telepon,
        }
