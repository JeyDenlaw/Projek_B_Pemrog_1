class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def ubah_mahasiswa(self, nim, nama_baru):
        for mhs in self.mahasiswa_list:
            if mhs.nim == nim:
                mhs.nama = nama_baru
                return True
        return False

    def hapus_mahasiswa(self, nim):
        for mhs in self.mahasiswa_list:
            if mhs.nim == nim:
                self.mahasiswa_list.remove(mhs)
                return True
        return False

    def cari_mahasiswa(self, nim):
        for mhs in self.mahasiswa_list:
            if mhs.nim == nim:
                return mhs
        return None

    def tampilkan_semua(self):
        return self.mahasiswa_list