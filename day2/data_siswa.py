from enum import Enum

class StatusKeanggotaan(Enum):
    CALON = 1
    AKTIF = 2
    PASIF = 3

print("=== Input Data Siswa Amabalan ===")
nama1 = input("Masukkan nama siswa: ")
umur1 = int(input("Masukkan umur siswa: "))
status1 = input("Masukkan status keanggotaan (Calon/Aktif/Pasif): ").upper()
if status1 in StatusKeanggotaan.__members__:
    status_validasi1 = StatusKeanggotaan[status1].name
else:
    print("Status tidak valid!")
    exit()  
minat_eskul1 = input("Masukkan minat ekstrakurikuler (pisahkan dengan koma): ").replace(' ','').split(',')
minat_set1 = set(minat_eskul1)

nama2 = input("\nMasukkan nama siswa: ")
umur2 = int(input("Masukkan umur siswa: "))
status2 = input("Masukkan status keanggotaan (Calon/Aktif/Pasif): ").upper()
if status2 in StatusKeanggotaan.__members__:
    status_validasi2 = StatusKeanggotaan[status2].name
else:
    print("Status tidak valid!")
    exit()  
minat_eskul2 = input("Masukkan minat ekstrakurikuler (pisahkan dengan koma): ").replace(' ','').split(',')
minat_set2 = set(minat_eskul2)

nama3 = input("\nMasukkan nama siswa: ")
umur3 = int(input("Masukkan umur siswa: "))
status3 = input("Masukkan status keanggotaan (Calon/Aktif/Pasif): ").upper()
if status3 in StatusKeanggotaan.__members__:
    status_validasi3 = StatusKeanggotaan[status3].name
else:
    print("Status tidak valid!")
    exit()  
minat_eskul3 = input("Masukkan minat ekstrakurikuler (pisahkan dengan koma): ").replace(' ','').split(',')
minat_set3 = set(minat_eskul3)
tuple1 = (nama1, umur1, status_validasi1, minat_set1)
tuple2 = (nama2, umur2, status_validasi2, minat_set2)
tuple3 = (nama3, umur3, status_validasi3, minat_set3)

list1 = [tuple1, tuple2, tuple3]
list2 = [tuple1[2], tuple2[2], tuple3[2]]

dict_siswa = {
    nama1 : tuple1,
    nama2 : tuple2,
    nama3 : tuple3
}

print("\n=== Data Siswa Terdaftar ===")
print(f"Nama: {dict_siswa[nama1][0]}")
print(f"  Usia: {dict_siswa[nama1][1]}")
print(f"  Status: {dict_siswa[nama1][2]}")
print(f"  Minat Ekstrakurikuler: {dict_siswa[nama1][3]}")

print(f"\nNama: {dict_siswa[nama2][0]}")
print(f"  Usia: {dict_siswa[nama2][1]}")
print(f"  Status: {dict_siswa[nama2][2]}")
print(f"  Minat Ekstrakurikuler: {dict_siswa[nama2][3]}")

print(f"\nNama: {dict_siswa[nama3][0]}")
print(f"  Usia: {dict_siswa[nama3][1]}")
print(f"  Status: {dict_siswa[nama3][2]}")
print(f"  Minat Ekstrakurikuler: {dict_siswa[nama3][3]}\n")

print(f"Total siwa aktif: {list2.count('AKTIF')}")

print(f"\nJenis Ekstrakurikuler terdaftar: {dict_siswa[nama1][3] | dict_siswa[nama2][3] | dict_siswa[nama3][3] }")