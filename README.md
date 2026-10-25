# Tugas List dan Array

## Identitas Mahasiswa
- Nama: Aulia Safitri
- NIM: 2225250190
- Kelas: 3B
- Mata Kuliah: Algoritma dan Pemrograman

## Deskripsi
Program ini dibuat untuk mempelajari penggunaan list atau array dalam Python, meliputi pembuatan list, indeks dan slicing, manipulasi data, agregasi nilai, penyaringan nilai kelulusan, dan penggunaan fungsi statistik.

## Struktur Folder
- `latihan/01_buat_list.py`: Membuat list dan menghitung banyak data.
- `latihan/02_indeks_slicing.py`: Mengakses elemen list menggunakan indeks dan slicing.
- `latihan/03_manipulasi_list.py`: Mengubah, menambah, dan menghapus elemen list.
- `latihan/04_agregasi_nilai.py`: Menghitung total, rata-rata, minimum, dan maksimum.
- `latihan/05_filter_kelulusan.py`: Menyaring nilai yang memenuhi batas kelulusan.
- `latihan/06_fungsi_statistik.py`: Menghitung rata-rata menggunakan fungsi.
- `praktik/analisis_nilai_mahasiswa.py`: Menganalisis data nilai mahasiswa.

## Cara Menjalankan
1. Pastikan Python sudah terpasang.
2. Buka folder proyek di VS Code.
3. Buka Terminal.
4. Jalankan file yang ingin diuji, misalnya:
   `py latihan/01_buat_list.py`
5. Untuk program utama, jalankan:
   `py praktik/analisis_nilai_mahasiswa.py`

## Hasil Pengujian Program Utama
- Banyak data: 10
- Total nilai: 695
- Rata-rata: 69.50
- Nilai minimum: 45
- Nilai maksimum: 90
- Jumlah lulus (nilai >= 60): 7
- Jumlah belum lulus: 3

## Refleksi
Melalui latihan ini, saya mempelajari cara membuat dan memanipulasi list, mengakses elemen berdasarkan indeks, menghitung statistik sederhana, menyaring data menggunakan perulangan dan kondisi, serta membuat fungsi untuk mengolah data nilai mahasiswa.

## Kuis Formatif – Kuis 3

1. Mengapa list lebih tepat daripada banyak variabel terpisah untuk menyimpan 30 nilai?
Karena list dapat menyimpan banyak nilai dalam satu variabel sehingga data lebih mudah dikelola dan diolah menggunakan perulangan.

2. Berapa indeks elemen pertama pada list Python?
Indeks elemen pertama adalah "0".

3. Apa arti indeks -1?
Indeks "-1" digunakan untuk mengakses elemen terakhir pada list.

4. Apa hasil "[10, 20, 30, 40][1:3]"?
Hasilnya adalah "[20, 30]", karena slicing mengambil elemen dari indeks 1 sampai sebelum indeks 3.

5. Apa perbedaan "append" dan "insert"?
- "append()" menambahkan elemen pada akhir list.
- "insert()" menambahkan elemen pada posisi indeks tertentu.

6. Apa risiko mengakses indeks yang tidak ada?
Program akan menghasilkan error "IndexError" karena indeks yang diakses tidak tersedia dalam list.

7. Fungsi apa yang digunakan untuk menghitung banyak elemen list?
Fungsi "len()".

8. Bagaimana menghitung rata-rata list numerik dengan "sum" dan "len"?
Dengan membagi jumlah seluruh elemen dengan banyaknya elemen.rata_rata = sum(data) / len(data)

9. Mengapa list kosong perlu diperiksa sebelum pembagian?
Karena list kosong memiliki panjang "0". Jika jumlah nilai dibagi dengan "0", program akan menghasilkan error "ZeroDivisionError".

10. Apa perintah yang digunakan untuk mengirim commit lokal ke GitHub?
Perintah "git push" digunakan untuk mengirim commit dari repositori lokal ke GitHub. Untuk push pertama, perintahnya dapat menggunakan "git push -u origin main".