# Mahardika Putra Abelva
#2515061076

def CekLogin(ListUser, InputUsername, InputPass):
    for user in ListUser:
        if user["username"] == InputUsername and user["password"] == InputPass:
            return True
    return False

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

if CekLogin(DaftarUser, username, password):
    print("Login berhasil.")
else:
    print("Username atau password salah. Login gagal.")