print("=== CEK PASSWORD ===\n")

password = input("Masukkan password: ")

panjang = len(password) >= 8
print("✔ Panjang cukup" if panjang else "❌ Minimal 8 karakter")

huruf_besar = password.lower() != password
print("✔ Mengandung huruf besar" if huruf_besar else "❌ Harus mengandung huruf besar")

angka_ada = any(char.isdigit() for char in password)
print("✔ Mengandung angka" if angka_ada else "❌ Harus mengandung angka")

tanpa_spasi = " " not in password
print("✔ Tidak mengandung spasi" if tanpa_spasi else "❌ Tidak boleh mengandung spasi")

if panjang and huruf_besar and angka_ada and tanpa_spasi:
    print("\nStatus: Password valid!")
else:
    print("\nStatus: Password tidak valid!")
