
def baca_dan_validasi_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                try:
                    nim, nilai_teks = baris.split(",")
                    nilai = float(nilai_teks.strip())
                    nim = nim.strip()

                    if not nim:
                        print("Data dilewati: NIM kosong.")
                        continue

                    data_nilai.append((nim, nilai))

                except ValueError:
                    print(f"Data tidak valid, dilewati: {baris}")

    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")
        return None

    return data_nilai


def tulis_rekap(nama_file, data_nilai):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("===========================\n")

        if not data_nilai:
            file.write("Tidak ada data nilai yang valid.\n")
        else:
            daftar_nilai = [nilai for nim, nilai in data_nilai]

            jumlah_data = len(daftar_nilai)
            rata_rata = sum(daftar_nilai) / jumlah_data
            nilai_minimum = min(daftar_nilai)
            nilai_maksimum = max(daftar_nilai)
            jumlah_lulus = sum(1 for nilai in daftar_nilai if nilai >= 60)

            file.write(f"Jumlah data valid : {jumlah_data}\n")
            file.write(f"Rata-rata nilai   : {rata_rata:.2f}\n")
            file.write(f"Nilai minimum     : {nilai_minimum:g}\n")
            file.write(f"Nilai maksimum    : {nilai_maksimum:g}\n")
            file.write(f"Jumlah lulus      : {jumlah_lulus}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}.")


def main():
    data_nilai = baca_dan_validasi_nilai("data/nilai.txt")

    if data_nilai is None:
        return

    tulis_rekap("data/hasil_rekap.txt", data_nilai)


if __name__ == "__main__":
    main()
