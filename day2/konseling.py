from enum import Enum
from collections import defaultdict
from collections import Counter

class StatusEmosional(Enum):
    TENANG = 1
    CEMAS = 2
    MARAH = 3

print("=== Input Data Konseling Siswa ===")
nama1 = input("Masukkan nama siswa: ").title()
umur1 = int(input("Masukkan umur: "))
status1 = input("Masukkan status emosional (Tenang/Cemas/Marah): ").upper()
if status1 in StatusEmosional.__members__:
    status_validasi1 = StatusEmosional[status1].name
else:
    print("Status tidak valid!")
    exit()
problem1 = input("Masukkan masalah utama (pisahkan dengan koma): ").replace(' ','').split(',')
problem_set1 = set(problem1)

nama2 = input("\nMasukkan nama siswa: ").title()
umur2 = int(input("Masukkan umur: "))
status2 = input("Masukkan status emosional (Tenang/Cemas/Marah): ").upper()
if status2 in StatusEmosional.__members__:
    status_validasi2 = StatusEmosional[status2].name
else:
    print("Status tidak valid!")
    exit()
problem2 = input("Masukkan masalah utama (pisahkan dengan koma): ").replace(' ','').split(',')
problem_set2 = set(problem2)

nama3 = input("\nMasukkan nama siswa: ").title()
umur3 = int(input("Masukkan umur: "))
status3 = input("Masukkan status emosional (Tenang/Cemas/Marah): ").upper()
if status3 in StatusEmosional.__members__:
    status_validasi3 = StatusEmosional[status3].name
else:
    print("Status tidak valid!")
    exit()
problem3 = input("Masukkan masalah utama (pisahkan dengan koma): ").replace(' ','').split(',')
problem_set3 = set(problem3)

tuple1 = (nama1, umur1, status_validasi1, problem_set1)
tuple2 = (nama2, umur2, status_validasi2, problem_set2)
tuple3 = (nama3, umur3, status_validasi3, problem_set3)

list_data = [tuple1[2], tuple2[2], tuple3[2]]

dict_data = {
    nama1 : tuple1,
    nama2 : tuple2,
    nama3 : tuple3
}

masalah_dict = defaultdict(set)
list_masalah = problem1 + problem2 + problem3
masalah_counter = Counter(list_masalah)

for siswa in dict_data.values():
    nama = siswa[0]
    masalah_set = siswa[3]
    for masalah in masalah_set:
        masalah_dict[masalah].add(nama)

print("\n=== Data Konseling Siswa ===\n")

print(f"Nama: {dict_data[nama1][0]}")
print(f"  Umur: {dict_data[nama1][1]}")
print(f"  Status Emosional: {dict_data[nama1][2]}")
print(f"  Masalah Utama: {dict_data[nama1][3]}")

print(f"\nNama: {dict_data[nama2][0]}")
print(f"  Umur: {dict_data[nama2][1]}")
print(f"  Status Emosional: {dict_data[nama2][2]}")
print(f"  Masalah Utama: {dict_data[nama2][3]}")

print(f"\nNama: {dict_data[nama3][0]}")
print(f"  Umur: {dict_data[nama3][1]}")
print(f"  Status Emosional: {dict_data[nama3][2]}")
print(f"  Masalah Utama: {dict_data[nama3][3]}")

print("\n=== Statistik Konseling ===\n")

print(f"Jumlah siswa dengan status CEMAS: {list_data.count('CEMAS')}\n")

print(f"Masalah paling sering muncul: {masalah_counter}")

print("Siswa yang punya masalah yang sama:")
for masalah, siswa_set in masalah_dict.items():
    if len(siswa_set) > 1:
        print(f"- {masalah}: {', '.join(siswa_set)}")
