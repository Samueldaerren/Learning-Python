print("=== Cek Kelayakan Beli Barang ===\n") # Title

harga_barang = int(input("Harga barang: ")) # Input user harga barang
uang = int(input("Uang kamu: ")) # Input user uang yang ada

# Logika pembelian
if uang >= harga_barang:
    hasil = uang - harga_barang
    status = f"Uang cukup. Kamu bisa beli barang ini!\nkembalian anda {hasil}"
elif uang < harga_barang:
    hasil = harga_barang - uang
    status = f"Uang tidak cukup. Uang anda kurang {hasil}"
else:
    print("Masukkan angka!")

print(f"Status: {status}") # Print status