Program antrian kasir cafe

Program antrian kasir ini menggunakan queue linked list yang didalamnya terdapat fitur enqueue, dequeue, peek, display antrian pengunjung, hitung total pengunjung, mencari nama pengunjung, dan menghapus semua antrian.
Source Code :
<img width="1748" height="5814" alt="SCTA" src="https://github.com/user-attachments/assets/c9666118-507f-41c8-b3d2-c0223b4316f9" />
Langkah Langkah Kode :
1. Program membuat class Node untuk menyimpan data pengunjung dan pointer next untuk menghubungkan node selanjutnya.
2. Buat class QueueLinkedList untuk mengatur antrian menggunakan dua pointer yaitu front untuk depan dan rear untuk belakang antrian.
3. Pada fungsi enqueue program membuat node baru lalu menambahkannya ke belakang antrian.
4. Saat fungsi dequeue ditrigger data paling depan dihapus karena queue menggunakan konsep FIFO.
5. Fungsi peek dipakai untuk melihat siapa pengunjung paling depan tanpa menghapus datanya.
6. Fungsi display menampilkan seluruh isi antrian dari depan ke belakang.
7. Fungsi hitungTotalPengunjung bekerja dengan menghitung jumlah node dalam linked list sehingga menghasilkan output total pengunjung.
8. Fungsi cariPengunjung melakukan pencarian nama pengunjung pada antrian dengan cara melakukan perulangan traversal ke seluruh node (posisi +=1) sampai terjadi kecocokan.
9. Fungsi clearQueue menghapus semua isi antrian dengan cara mengosongkan pointer front dan rear.
10. Terakhir Pada fungsi main program menampilkan menu dengan perulangan sampai memilih opsi keluar.

Output Kode :
<img width="1603" height="903" alt="image" src="https://github.com/user-attachments/assets/0372df5a-7cdd-46f7-a813-5e7ca31a08d2" />
Gambar diatas adalah contoh output dari fungsi display, hitung total, cariPengunjung, dan hapus semua antrian.

Link youtube : https://youtu.be/--pHdYWS6L4
