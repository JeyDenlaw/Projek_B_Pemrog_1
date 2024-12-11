class MahasiswaView:
    def tampilkan_list(self, mahasiswa_list):
        print("=================")
        print("Daftar Mahasiswa:")
        print("=================")
        for mhs in mahasiswa_list:
            print(f"Nama: {mhs.nama}, NIM: {mhs.nim}")

    def tampilkan_detail(self, mahasiswa):
        if mahasiswa:
            print(f"Detail Mahasiswa:\nNama: {mahasiswa.nama}\nNIM: {mahasiswa.nim}")
        else:
            print("Mahasiswa tidak ditemukan.")