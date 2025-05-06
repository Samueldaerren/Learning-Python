print("=== Konversi Mata Uang ===\n")

jumlah_uang = int(input("Masukkan jumlah uang: "))
mata_uang = input("Masukkan mata uang tujuan [USD/YEN/EURO]: ").upper()

if mata_uang == "USD":
    kurs = 16862
    konversi = f"${jumlah_uang / kurs}"
elif mata_uang == "YEN":
    kurs = 118
    konversi = f"¥{jumlah_uang / kurs}"
elif mata_uang == "EURO":
    kurs = 19158
    konversi = f"€{jumlah_uang / kurs}"
else:
    konversi = "Masukkan mata uang yang valid [USD/YEN/EURO]!"

print(f"Hasil: Rp{jumlah_uang} = {konversi} (kurs: Rp{kurs})")