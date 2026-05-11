# Mahardika Putra Abelva
# 2515061076

def LinearSearchLogin(ListUser, InputUsername, InputPass):
    for i in range(len(ListUser)):
        if (ListUser[i]["username"] == InputUsername and
            ListUser[i]["password"] == InputPass):
            return True, i
    return False, -1


DaftarUser = [
    {"username": "Dika", "password": "123456"},
    {"username": "Dini", "password": "654321"},
    {"username": "Indri", "password": "abcdef"},
    {"username": "Jesika", "password": "fedcba"},
    {"username": "Rashell", "password": "111111"},
    {"username": "Admin", "password": "admin123"}
]

username = input("Masukkan username: ")
password = input("Masukkan password: ")

found, index = LinearSearchLogin(DaftarUser, username, password)

if found:
    print(f"Login berhasil. Data ditemukan pada indeks ke-{index}")
else:
    print("Username atau password salah. Login gagal.")
