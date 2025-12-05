import diskon
import bmi
import bunga
import gaji
import cekstok

def tampilkan_menu():
    print("\n" + "="*45)
    print("Silahkan pilih menu aplikasi:")
    print("1. Kasir Toko")
    print("2. Cek Kesehatan Keluarga (BMI)")
    print("3. Simulasi Investasi")
    print("4. Sistem Penggajian")
    print("5. Gudang Barang")
    print("="*45)

def main_aplikasi():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih nomor (exit untuk keluar): ").lower()

        if pilihan == "exit":
            print("Program selesai. Terima kasih!")
            break

        elif pilihan == "1":
            diskon.kasir_toko()

        elif pilihan == "2":
            jumlah = int(input("Jumlah anggota keluarga: "))
            bmi.cek_kesehatan_keluarga(jumlah)

        elif pilihan == "3":
            bunga.simulasi_investasi()

        elif pilihan == "4":
            gaji.sistem_penggajian()

        elif pilihan == "5":
            cekstok.gudang_barang()

        else:
            print("Pilihan tidak valid! Pilih angka 1–5.")

if __name__ == "__main__":
    main_aplikasi()