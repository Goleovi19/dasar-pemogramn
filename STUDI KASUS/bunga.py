def hitung_bunga(saldo_awal, bunga_persen, tahun):
    saldo = saldo_awal
    print(f"Saldo awal : Rp {saldo:,.2f}")

    for i in range(1, tahun + 1):
        bunga = saldo * (bunga_persen / 100)
        saldo += bunga
        print(f"Tahun ke-{i}: Bunga Rp {bunga:,.2f} | Saldo : Rp{saldo:,.2f}")
    return saldo
    

def simulasi_investasi():
    modal = float(input("Modal awal : "))
    rate = float(input("Bunga per tahun (%): "))
    durasi = int(input("Lama investasi (tahun) : "))

    if modal < 0 or rate < 0:
        print("Input tidak boleh negatif.")
    else:
        hitung_bunga(modal, rate, durasi)

# === Tidak ada auto-run di sini ===
# Kalau mau menjalankan, ketik secara manual:
# simulasi_investasi()
