# Pertemuan 12 — File I/O dan Error Handling

## Identitas Mahasiswa

- **Nama:** Muhammad Fatih Ammar
- **NIM:** 2225250135
- **Kelas:** 3E
- **Mata Kuliah:** Algoritma dan Pemrograman

## Deskripsi

Program ini membaca data nilai dari file teks, memvalidasi data, menghitung statistik nilai, dan menyimpan hasil rekap ke file teks. Program menggunakan File I/O, fungsi, serta penanganan error dengan `try-except`.

## Struktur Proyek

```text
pertemuan-12-file-io-2225250135/
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
├── tugas/
│   └── rekap_nilai_file.py
├── .gitignore
└── README.md
```

## Format Data Input

Data disimpan di `data/nilai.txt` dengan format `NIM,nilai`, satu data per baris.

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Data dengan nilai yang tidak valid akan dilewati.

## Cara Menjalankan

Pastikan terminal berada di folder utama proyek, kemudian jalankan:

```powershell
python tugas/rekap_nilai_file.py
```

## Penanganan Error

- `FileNotFoundError`: menangani file input yang tidak ditemukan.
- `ValueError`: menangani nilai yang tidak dapat dikonversi menjadi angka.
- Baris kosong dilewati agar tidak diproses sebagai data nilai.

## Hasil Rekap

Program menghitung:
- Jumlah data nilai valid.
- Rata-rata nilai.
- Nilai minimum.
- Nilai maksimum.
- Jumlah mahasiswa yang lulus dengan nilai minimal 60.

Hasil disimpan di `data/hasil_rekap.txt`.

## Pengujian

| Skenario | Hasil yang Diharapkan |
|---|---|
| Data normal | Statistik nilai dihitung |
| Nilai bukan angka | Baris tidak valid dilewati |
| Baris kosong | Baris dilewati |
| File input tidak ditemukan | Pesan error ditampilkan |
| Nilai minimal 60 | Nilai 60 atau lebih dihitung lulus |

## Refleksi

Melalui praktikum ini, saya mempelajari cara membaca dan menulis file menggunakan Python, memilih mode file yang sesuai, memvalidasi data, serta menangani error secara spesifik. Saya juga memahami bahwa pengujian diperlukan untuk memastikan program berjalan sesuai kebutuhan.
