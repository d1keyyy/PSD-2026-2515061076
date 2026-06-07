Sistem Daftar CCTV

Sistem ini menyimpan ID CCTV dan Lokasi CCTV menggunakan fungsi hashmap Separate Chaining ke dalam memori.

Source Code :
<img width="1982" height="4370" alt="SourceCode" src="https://github.com/user-attachments/assets/b04e50e1-9927-4673-9848-24e2f740eba8" />
Penjelasan kode : 
  Kelas Node
    class Node: Membuat struktur node untuk menyimpan data CCTV.
    def __init__(self, key, value): Constructor yang dijalankan saat node dibuat.
    self.key = key Menyimpan ID CCTV.
    self.value = value Menyimpan lokasi CCTV.
    self.next = None Menyimpan referensi ke node berikutnya dalam Linked List.
  Kelas HashMapSeparateChaining
    class HashMapSeparateChaining: Membuat Hash Map dengan metode Separate Chaining.
    def __init__(self, size=10): Membuat Hash Table dengan ukuran default 10.
    self.SIZE = size Menyimpan ukuran Hash Table.
    self.table = [None] * self.SIZE Membuat tabel yang seluruh slotnya masih kosong.
  Fungsi Hash
    def hash_function(self, key): Menentukan posisi penyimpanan data dalam Hash Table.
    return (key % self.SIZE + self.SIZE) % self.SIZE Menghasilkan indeks berdasarkan operasi modulo agar selalu berada dalam rentang indeks yang valid.
  Fungsi Insert
    def insert(self, key, value): Menambahkan data CCTV ke Hash Table.
    index = self.hash_function(key) Menghitung indeks penyimpanan berdasarkan ID CCTV.
    current = self.table[index] Mengambil data pertama pada indeks tersebut.
    while current is not None: Memeriksa seluruh node pada indeks yang sama.
    if current.key == key: Mengecek apakah ID CCTV sudah ada.
    current.value = value Memperbarui lokasi CCTV jika ID ditemukan.
    return Menghentikan proses karena data sudah diperbarui.
    current = current.next Berpindah ke node berikutnya.
    new_node = Node(key, value) Membuat node baru.
    new_node.next = self.table[index] Menghubungkan node baru dengan node yang sudah ada.
    self.table[index] = new_node Menjadikan node baru sebagai node pertama pada indeks tersebut.
  Fungsi Search
    def search(self, key): Mencari data CCTV berdasarkan ID.
    index = self.hash_function(key) Menentukan indeks pencarian.
    current = self.table[index] Mengambil node pertama pada indeks tersebut.
    while current is not None: Menelusuri seluruh node yang ada.
    if current.key == key: Mengecek apakah ID yang dicari ditemukan.
    return current Mengembalikan data CCTV yang ditemukan.
    current = current.next Berpindah ke node berikutnya.
    return None Menandakan data CCTV tidak ditemukan.
  Fungsi Remove
    def remove_key(self, key): Menghapus data CCTV berdasarkan ID.
    index = self.hash_function(key) Menentukan indeks data yang akan dihapus.
    current = self.table[index] Mengambil node pertama pada indeks tersebut.
    prev = None Menyimpan node sebelumnya.
    while current is not None: Menelusuri seluruh node pada indeks tersebut.
    if current.key == key: Mengecek apakah ID ditemukan.
    if prev is None: Memeriksa apakah node yang dihapus berada di posisi pertama.
    self.table[index] = current.next Menghapus node pertama dengan menggantinya menggunakan node berikutnya.
    prev.next = current.next Menghapus node di tengah atau akhir Linked List.
    return True Menandakan penghapusan berhasil.
    prev = current Menyimpan node saat ini sebagai node sebelumnya.
    current = current.next Berpindah ke node berikutnya.
    return False Menandakan data tidak ditemukan.
  Fungsi Display
    def display(self): Menampilkan seluruh isi Hash Table.
    print("\nIsi Hash Table (Separate Chaining):") Menampilkan judul tampilan data.
    for i in range(self.SIZE): Mengulang seluruh indeks dalam Hash Table.
    print(f"{i}: ", end="") Menampilkan nomor indeks.
    current = self.table[i] Mengambil node pertama pada indeks tersebut.
    while current is not None: Menampilkan seluruh node yang ada pada indeks tersebut.
    print(f"({current.key},{current.value})", end="") Menampilkan ID dan lokasi CCTV.
    current = current.next Berpindah ke node berikutnya.
    print("NULL") Menandakan tidak ada node lagi pada indeks tersebut.
  Fungsi Main
    def main(): Merupakan fungsi utama program.
    cctv_system = HashMapSeparateChaining() Membuat objek Hash Map untuk menyimpan data CCTV.
    cctv_system.insert() Menambahkan beberapa data CCTV awal ke dalam sistem.
    pilihan = 0 Menyimpan pilihan menu pengguna.
    while pilihan != "5": Menjalankan program terus-menerus sampai pengguna memilih keluar.
    input() Digunakan untuk menerima masukan dari pengguna.

Output :
<img width="1208" height="465" alt="image" src="https://github.com/user-attachments/assets/d31cc22b-0654-4091-ab60-c9602306510c" />

Link Youtube : 
