print("=== Format Kalimat ===\n")

kalimat = ' '.join(input("Input: ").strip().split()).lower()

if "gk" in kalimat:
    kalimat = kalimat.replace('gk', 'tidak')

hasil = kalimat[0].upper() + kalimat[1:]
print(f"Output: {hasil}")