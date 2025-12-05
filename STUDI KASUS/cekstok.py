def cek_stok(stok_saat_ini):
    if stok_saat_ini == 0:
        print("ERROR: Stok Habis!")
    elif stok_saat_ini < 5:
        print("WARNING: Stok menipis! Segera restock.")

def gudang_barang():
    stok = 20  # stok awal

    while stok > 0:
        print(f"\nStok Tersedia: {stok}")
        beli = int(input("Jumlah dibeli: "))

        if beli > stok:
            print("Permintaan melebihi stok!")
        else:
            stok -= beli
            print("Transaksi berhasil.")
            cek_stok(stok)

    print("Toko tutup (barang habis).")


# === Tidak ada auto-run ===
# Jika ingin menjalankan, panggil manual:
# gudang_barang()
