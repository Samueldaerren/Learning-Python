print("=== Biodata Interaktif ===\n")

# Input pengguna
nama = input("Masukkan nama lengkap: ").lower()
umur = int(input("Masukkan umur: "))
kota = input("Masukkan kota asal: ")
hobi = input("Masukkan hobi favorit: ")
nilai = int(input("Masukkan nilai matematika (0-100): "))
tahun_lahir = 2025 - umur # Hitung tahun umur
# Hitung jumlah huruf vokal
total_vokal = nama.count('a') + nama.count('i') + nama.count('u') + nama.count('e') + nama.count('o')
skala = (nilai / 100) * 4 # Hitung nilai skala 4.0

# Biodata
print(f"\nHalo, {nama}! Kamu berasal dari {kota}.")
print(f"Kamu berumur {umur} tahun, lahir pada {tahun_lahir}.")
print(f"Hobi favorit kamu adalah {hobi}.\n")

print(f"Jumlah huruf vokal dalam nama kamu: {'Tidak ada' if total_vokal == 0 else total_vokal}")
print(f"Apakah namamu mengandung huruf 'a' atau 'z'? {'Ya' if 'a' in nama or 'z' in nama else 'Tidak'}\n")

print(f"Nilai matematika kamu: {nilai}")
print(f"Status: {'Lulus' if nilai >= 75 else 'Gagal'}")
print(f"Nilai skala 4.0: {skala}\n")

print(f"Usia kamu 10 tahun lagi: {umur + 10}")
print(f"Status umur: {'Dewasa' if umur >= 18 else 'Belum Dewasa'}\n")

print("===========================")
