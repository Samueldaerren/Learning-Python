print("=== Cek Usia ===\n")

umur = int(input("Masukkan umur kamu: "))

if umur < 13:
    kategori = "Anak-anak"
    status = "Silahkan mengakses konten edukasi"
elif 13 <= umur <= 17:
    kategori = "Remaja"
    status = "Kamu belum cukup umur untuk mengakses konten dewasa"
else:
    kategori = "Dewasa"
    status = "Umur kamu cukup untuk mengakses konten dewasa"
   

print(f"Kategori: {kategori}")
print(f"Status: {status}")