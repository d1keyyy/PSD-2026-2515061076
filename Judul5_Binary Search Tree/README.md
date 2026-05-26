Sistem kontak sederhana untuk menyimpan nomor Fineshyt

Sistem kontak menggunakan struktur data Binary Search Tree yang memiliki fungsi menambah kontak, mencari kontak, mengurutkan Inorder, mengurutkan Preorder, mengurutkan Postorder, menghitung jumlah kontak, dan menampilkan kontak fineshyt awal dan akhir

Source Code :
<img width="1334" height="7030" alt="TA5_Mahardika Putra Abelva" src="https://github.com/user-attachments/assets/008240c1-03e0-4476-a190-d9bf37d15957" />

Penjelasan Source Code:
1. class Node:
Digunakan untuk membuat node kontak pada BST.
2. self.key = nama
Menyimpan nama kontak sebagai key utama BST.
3. self.nomor = nomor
Menyimpan nomor telepon kontak.
4. self.left = None dan self.right = None
Pointer menuju child kiri dan kanan.
5. class BSTKontak:
Class utama untuk mengumpulkan Binary Search Tree.
6. self.root = None
Root awal BST kosong.
7. def insert_node()
Function rekursif untuk menambahkan kontak ke BST.
8. if nama < root.key
Data dimasukkan ke subtree kiri jika nama lebih kecil.
9. elif nama > root.key
Data dimasukkan ke subtree kanan jika nama lebih besar.
10. def search_node()
Function untuk mencari kontak berdasarkan nama.
11. if root.key == nama
Mengecek apakah kontak ditemukan.
12. def inorder()
Traversal inorder untuk menampilkan kontak secara urut alfabet.
13. def preorder()
Traversal preorder menampilkan root terlebih dahulu.
14. def postorder()
Traversal postorder menampilkan root terakhir.
15. def count_contacts()
Menghitung jumlah seluruh kontak dalam BST.
16. def find_first_contact()
Mencari kontak pertama alfabet dengan bergerak ke kiri terus.
17. def find_last_contact()
Mencari kontak terakhir alfabet dengan bergerak ke kanan terus.
18. def main()
Function utama program berbasis menu.

Output :
<img width="1592" height="7068" alt="code-snapshot" src="https://github.com/user-attachments/assets/108148ad-38d0-4216-890f-d6d0c5e91ee6" />

Youtube : 
