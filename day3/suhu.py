class KonversiSuhu:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def Farenheit(self):
        return (self.nilai * 9/5) + 32
    
    def Kelvin(self):
        return self.nilai + 273.15

class KonversiJarak:
    def __init__(self, nilai): 
        self.nilai = nilai
    
    def Meter(self):
        return self.nilai * 1000
    
    def Mil(self):
        return self.nilai * 0.621371
    
class KonversiKilogram:
    def __init__(self, nilai):
        self.nilai = nilai

    def Gram(self):
        return self.nilai * 1000
    
    def Pon(self):
        return self.nilai * 2.20462
    
def main():
    while True:
        print("\nKonversi Satuan")
        print("1.Konversi Suhu (Celcius)")
        print("2.Konversi Jarak (KM)")
        print("3.Konversi Berat (KG)")
        print("4.Keluar")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 4:
            print("Terimakasih!")
            break

        try:
            nilai = float(input("Masukkan angka: "))
        except ValueError:
            print("Masukkan angka!")

        if pilihan == 1:
            suhu = KonversiSuhu(nilai)
            print(f"{nilai} C = {suhu.Farenheit():.2f} F")
            print(f"{nilai} C = {suhu.Kelvin():.2f} K")
        elif pilihan == 2:
            jarak = KonversiJarak(nilai)
            print(f"{nilai} KM = {jarak.Meter():.2f} Meter")
            print(f"{nilai} KM = {jarak.Mil():.2f} Mil")
        elif pilihan == 3:
            berat = KonversiKilogram(nilai)
            print(f"{nilai} KG = {berat.Gram():.2f} G")
            print(f"{nilai} KG = {berat.Pon():.2f} P")
        else:
            print("Pilihan Tidak Valid!")

main()