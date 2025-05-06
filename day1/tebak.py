print("=== Tebak Gambar ===\n")

kata = "python"

kata_tampil = "_" * len(kata)

kesempatan = 3

print("=== TEBAK KARAKTER ===")
print("Kata:", kata_tampil)

if "_" not in kata_tampil:
    print("\nSelamat! Kamu berhasil menebak kata:", kata_tampil)
else:
    if kesempatan > 0:
        tebakan = input(f"Tebakan kamu: ").lower()

        if len(tebakan) != 1:
            print("Harap masukkan hanya satu karakter.")
        
        elif tebakan in kata:
            print("Benar!")
            kata_tampil = ''.join([tebakan if kata[i] == tebakan else kata_tampil[i] for i in range(len(kata))])
            print("Kata:", kata_tampil)
        else:
            print(f"Salah! Kesempatan tinggal: {kesempatan - 1}")
            kesempatan -= 1

    if kesempatan == 0:
        print(f"\nGame Over! Kata yang benar adalah: {kata}")
