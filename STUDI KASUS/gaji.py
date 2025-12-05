def hitung_gaji(jam_kerja, tarif_per_jam):
    if jam_kerja > 40:
        jam_normal = 40
        jam_lembur = jam_kerja - 40
        gaji = (jam_normal * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)
    else:
        gaji = jam_kerja * tarif_per_jam
    return gaji

def sistem_penggajian():
    list_karyawan = ["andi", "budi", "citra"]
    tarif = int(input("Masukkan jumlah tarif per jam : "))

    for nama in list_karyawan:
        jam = int(input(f"Masukkan jam kerja {nama} : "))
        total_gaji = hitung_gaji(jam, tarif)
        print(f"Gaji {nama}: Rp {total_gaji:,.0f}")

# === Tidak auto-run ===
# Jika ingin menjalankan, panggil:
# sistem_penggajian()