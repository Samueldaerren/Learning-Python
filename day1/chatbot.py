print("=== Chatbot Mini ===\n")

user = input("User: ").lower()

if "hai" in user:
    print("Bot : Halo juga! Ada yang bisa aku bantu?")
elif "siapa kamu?" in user:
    print("Bot : Aku chatbot Python buatan Daerren!")
elif "apa kabar?" in user:
    print("Bot : Saya Baik terimakasih.")
else:
    print("""Bot : Terimakasih sudah menggunakan Chatbot. 
      Untuk informasi selengkapnya silahkan tanyakan""")