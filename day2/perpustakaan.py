from enum import Enum

class StatusBuku(Enum):
    TERSEDIA = 1
    DIPINJAM = 2
    RUSAK = 3

print("=== Input Data Buku ===")
judul1 = input("Judul: ").title()
penulis1 = input("Penulis: ").title()
status1 = input("Status Buku (Tersedia/Dipinjam/Rusak): ").upper()
if status1 in StatusBuku.__members__:
    status_validasi1 = StatusBuku[status1].name
else:
    print("Status Tidak Valid!")
    exit()
kategori1 = input("Kategori Buku (pisahkan dengan koma): ").replace(' ','').split(',')
kategori_set1 = set(kategori1)

judul2 = input("\nJudul: ").title()
penulis2 = input("Penulis: ").title()
status2 = input("Status Buku (Tersedia/Dipinjam/Rusak): ").upper()
if status2 in StatusBuku.__members__:
    status_validasi2 = StatusBuku[status2].name
else:
    print("Status Tidak Valid!")
    exit()
kategori2 = input("Kategori Buku (pisahkan dengan koma): ").replace(' ','').split(',')
kategori_set2 = set(kategori2)

judul3 = input("\nJudul: ").title()
penulis3 = input("Penulis: ").title()
status3 = input("Status Buku (Tersedia/Dipinjam/Rusak): ").upper()
if status3 in StatusBuku.__members__:
    status_validasi3 = StatusBuku[status3].name
else:
    print("Status Tidak Valid!")
    exit()
kategori3 = input("Kategori Buku (pisahkan dengan koma): ").replace(' ','').split(',')
kategori_set3 = set(kategori3)

tuple1 = (judul1, penulis1, status_validasi1, kategori_set1)
tuple2 = (judul2, penulis2, status_validasi2, kategori_set2)
tuple3 = (judul3, penulis3, status_validasi3, kategori_set3)

list_buku = [tuple1[2], tuple2[2], tuple3[2]]

dict_buku = {
    judul1 : tuple1,
    judul2 : tuple2,
    judul3 : tuple3
}

print("\n=== Data Buku Perpustakaan ===")
print(f"Judul: {dict_buku[judul1][0]}")
print(f"  Penulis: {dict_buku[judul1][1]}")
print(f"  Status: {dict_buku[judul1][2]}")
print(f"  Kategori: {dict_buku[judul1][3]}")

print(f"\nJudul: {dict_buku[judul2][0]}")
print(f"  Penulis: {dict_buku[judul2][1]}")
print(f"  Status: {dict_buku[judul2][2]}")
print(f"  Kategori: {dict_buku[judul2][3]}")

print(f"\nJudul: {dict_buku[judul3][0]}")
print(f"  Penulis: {dict_buku[judul3][1]}")
print(f"  Status: {dict_buku[judul3][2]}")
print(f"  Kategori: {dict_buku[judul3][3]}")

print(f"\nJumlah Buku Tersedia: {list_buku.count('TERSEDIA')}")
print(f"Kategori Buku yang Terdaftar: {dict_buku[judul1][3] | dict_buku[judul2][3] | dict_buku[judul3][3]}")