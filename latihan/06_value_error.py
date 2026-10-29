
nilai_teks = "abc"

try:
    nilai = float(nilai_teks)
    print("Nilai:", nilai)

except ValueError:
    print("Error: Nilai harus berupa angka.")
