def hitung_diskon(total):
    if total > 500000:
        return 0.2
    elif total > 200000:
        return 0.1
    else:
        return 0

def kasir_toko():
    total_belanja = 0
    print("\n=== Program Kasir ===")
    
    while True:
        harga = int(input("Masukkan harga barang (0 untuk selesai): "))
        if harga == 0:
            break
        total_belanja += harga

    diskon_persen = hitung_diskon(total_belanja)
    potongan = total_belanja * diskon_persen
    pajak = total_belanja * 0.12
    total_akhir = total_belanja + pajak - potongan

    print(f"Total awal : Rp {total_belanja}")
    print(f"Diskon ({diskon_persen*100}%) : Rp {potongan}")
    print(f"Pajak 12% : Rp {pajak}")
    print(f"Total bayar : Rp {total_akhir}")

if __name__ == "__main__":
    kasir_toko()
