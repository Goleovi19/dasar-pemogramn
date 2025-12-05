def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100
    return berat / (tinggi_m ** 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "kekurangan berat badan"
    elif 18.5 <= bmi < 24.9:
        return "normal(ideal)"
    elif 25 <= bmi < 29.9:
        return "kelebihan berat badan"
    else:
        return "obesitas"

def cek_kesehatan_keluarga(jumlah_anggota):
    for i in range(jumlah_anggota):
        print(f"\nAnggota ke-{i+1}")
        b = float(input("Berat (kg):"))
        t = float(input("Tinggi (cm):"))
        bmi = hitung_bmi(b, t)
        print(f"BMI: {bmi :.2f} -> {kategori_bmi(bmi)}")

# === Tidak ada auto-run di sini ===
# Kalau mau menjalankan, panggil manual di bawah: 
# cek_kesehatan_keluarga(2)
