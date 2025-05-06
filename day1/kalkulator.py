print("=== Kalkulator Sederhana ===\n")

num1 = int(input("Masukkan angka pertama: "))
op = input("Masukkan operator (+, -, *, /): ")
num2 = int(input("Masukkan angka kedua: "))

if op == "+":
    hasil = num1 + num2
    if hasil % 2 == 0:
        bilangan = "Genap"
    else:
        bilangan = "Ganjil"
elif op == "-":
    hasil = num1 - num2
    if hasil % 2 == 0:
        bilangan = "Genap"
    else:
        bilangan = "Ganjil"
elif op == "*":
    hasil = num1 * num2
    if hasil % 2 == 0:
        bilangan = "Genap"
    else:
        bilangan = "Ganjil"
elif op == "/":
    if num2 == 0:
        hasil = "Angka tidak bisa dibagi 0"
    else:
        hasil = num1 / num2
        if hasil % 2 == 0:
            bilangan = "Genap"
        else:
            bilangan = "Ganjil"
else:
    print("Operator invalid masukan (+, -, *, /, %, //, **)!")


print(f"Hasil: {num1} {op} {num2} = {hasil}")
print(f"Hasilnya adalah bilangan {bilangan}.")