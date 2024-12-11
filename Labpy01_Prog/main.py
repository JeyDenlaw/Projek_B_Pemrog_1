from data.mahasiswa import DataMahasiswa, Mahasiswa
from view.form_input import Nasgor
from view.mahasiswa import MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()
    form_input = Nasgor()
    mahasiswa_view = MahasiswaView()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Ubah Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Tampilkan Semua Mahasiswa")
        print("5. Cari Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama, nim = form_input.input_data()
            mhs = Mahasiswa(nama, nim)
            data_mahasiswa.tambah_mahasiswa(mhs)
            while True:
                lagi = input("Apakah Anda ingin menambahkan data lagi? (y/n): ")
                if lagi.lower() == 'y':
                    nama, nim = form_input.input_data()
                    mhs = Mahasiswa(nama, nim)
                    data_mahasiswa.tambah_mahasiswa(mhs)
                elif lagi.lower() == 'n':
                    break
                else:
                    print("Input tidak valid.")

        elif pilihan == '2':
            nim = input("Masukkan NIM Mahasiswa yang ingin diubah: ")
            nama_baru = input("Masukkan Nama Baru: ")
            if data_mahasiswa.ubah_mahasiswa(nim, nama_baru):
                print("Data mahasiswa berhasil diubah.")
            else:
                print("Mahasiswa tidak ditemukan.")

        elif pilihan == '3':
            nim = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
            if data_mahasiswa.hapus_mahasiswa(nim):
                print("Mahasiswa berhasil dihapus.")
            else:
                print("Mahasiswa tidak ditemukan.")

        elif pilihan == '4':
            mahasiswa_view.tampilkan_list(data_mahasiswa.tampilkan_semua())

        elif pilihan == '5':
            nim = input("Masukkan NIM Mahasiswa yang dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            mahasiswa_view.tampilkan_detail(mahasiswa)

        elif pilihan == '6':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()