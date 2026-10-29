
try:
    with open("data/file_tidak_ada.txt", "r", encoding="utf-8") as file:
        isi = file.read()
        print(isi)

except FileNotFoundError:
    print("Error: File tidak ditemukan.")

