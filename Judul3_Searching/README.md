Program Cek Validasi Login

Program ini mengecek apakah password dan username yang dimasukan terdapat dalam database, jika ada maka login berhasil jika tidak maka login gagal.
<img width="1284" height="1520" alt="code-snapshot" src="https://github.com/user-attachments/assets/7f7d5ea3-f979-4e17-ab78-88318e5160fa" />
Cara Kerja :
1. Definisikan fungsi LinearSearchLogin
2. Mulai loop for dari i = 0 sampai len(ListUser) - 1
3. Di dalam loop periksa apakah ListUser[i]["username"] sama dengan InputUsername dan ListUser[i]["password"] sama dengan InputPass, Jika ya maka return True dan indeks i
4. Jika loop selesai dan tidak ada yang cocok maka kembalikan False dan -1
5. Deklarasikan daftar pengguna
6. Meminta Input username
7. Meminta Input password
8. Memanggil fungsi search tadi
9. Lalu outputkan hasilnya
10. Jika found True maka print "Login berhasil. Data ditemukan pada indeks ke-{index}"
11. Jika found False maka print "Username atau password salah. Login gagal."
12. Selesai

Output :
<img width="477" height="198" alt="image" src="https://github.com/user-attachments/assets/31306ae2-16b9-4b9d-bd93-52ec9fe5090a" />
Terlihat output jika salah 1 huruf tidak sesuai dengan data base maka akan menampilkan login gagal, namun jika sesuai dengan data base maka login akan berhasil.
