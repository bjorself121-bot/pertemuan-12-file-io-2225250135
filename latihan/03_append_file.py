
# Mode a digunakan untuk menambahkan isi file
with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Saya sedang belajar mode file Python.\n")

print("Data berhasil ditambahkan.")
