class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        return self.angka1 + self.angka2
    
    def kurang(self):
        return self.angka1 - self.angka2
    
    def kali(self):
        return self.angka1 * self.angka2
    
    def bagi(self):
        if self.angka2 == 0:
            return "Angka tidak bisa dibagi 0"
        else:
            return self.angka1 / self.angka2
        
def main():
    while True:
        print("\nKalkulator Sederhana")
        print("1.Tambah")
        print("2.Kurang")
        print("3.Kali")
        print("4.Bagi")
        print("5.Exit")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 5:
            print("Terimakasih!")
            break

        try:
            angka1 = int(input("Masukkan angka1: "))
            angka2 = int(input("Masukkan angka2: "))
        except ValueError:
            print("Masukkan angka bukan huruf!")
            continue

        kalkulator = Kalkulator(angka1, angka2)

        if pilihan == 1:
            print(f"Hasil: {kalkulator.tambah()}")
        elif pilihan == 2:
            print(f"Hasil: {kalkulator.kurang()}")
        elif pilihan == 3:
            print(f"Hasil: {kalkulator.kali()}")
        elif pilihan == 4:
            print(f"Hasil: {kalkulator.bagi()}")
        else:
            print(f"Pilihan tidak valid!")

main()
