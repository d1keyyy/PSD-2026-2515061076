#Mahardika Putra Abelva
#2515061076
class Node:
    def __init__(self, nama, nomor):
        self.key = nama
        self.nomor = nomor
        self.left = None
        self.right = None


class BSTKontak:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nama, nomor):
        if root is None:
            return Node(nama, nomor)

        if nama < root.key:
            root.left = self.insert_node(root.left, nama, nomor)

        elif nama > root.key:
            root.right = self.insert_node(root.right, nama, nomor)

        return root

    def insert(self, nama, nomor):
        self.root = self.insert_node(self.root, nama, nomor)

    def search_node(self, root, nama):
        if root is None:
            return None

        if root.key == nama:
            return root

        if nama < root.key:
            return self.search_node(root.left, nama)

        return self.search_node(root.right, nama)

    def search(self, nama):
        return self.search_node(self.root, nama)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(f"Nama : {root.key} | Nomor : {root.nomor}")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return

        print(f"Nama : {root.key} | Nomor : {root.nomor}")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(f"Nama : {root.key} | Nomor : {root.nomor}")

    def count_contacts(self, root):
        if root is None:
            return 0

        return 1 + self.count_contacts(root.left) + self.count_contacts(root.right)

    def find_first_contact(self, root):
        if root is None:
            return None

        current = root

        while current.left is not None:
            current = current.left

        return current

    def find_last_contact(self, root):
        if root is None:
            return None

        current = root

        while current.right is not None:
            current = current.right

        return current


def main():
    kontak = BSTKontak()

    pilih = 0

    while pilih != 8:
        print("\nSistem Save Kontak Fineshyt")
        print("1. Tambah Kontak Fineshyt")
        print("2. Cari Kontak Fineshyt")
        print("3. Urutkan Inorder")
        print("4. Urutkan Preorder")
        print("5. Urutkan Postorder")
        print("6. Jumlah Kontak Fineshyt")
        print("7. Kontak Fineshyt Awal & Akhir")
        print("8. Keluar")

        pilih = int(input("Pilih menu: "))

        if pilih == 1:
            nama = input("Masukkan nama Fineshyt : ")
            nomor = input("Masukkan nomor telepon Fineshyt : ")

            kontak.insert(nama, nomor)

            print("Fineshyt berhasil ditambahkan")

        elif pilih == 2:
            nama = input("Masukkan Fineshyt yang dicari : ")

            hasil = kontak.search(nama)

            if hasil is not None:
                print("Kontak Fineshyt ditemukan")
                print("Nama  :", hasil.key)
                print("Nomor :", hasil.nomor)

            else:
                print("Kontak Fineshyt tidak ditemukan")

        elif pilih == 3:
            print("\nData kontak Fineshyt inorder:")
            kontak.inorder(kontak.root)

        elif pilih == 4:
            print("\nData kontak Fineshyt preorder:")
            kontak.preorder(kontak.root)

        elif pilih == 5:
            print("\nData kontak Fineshyt postorder:")
            kontak.postorder(kontak.root)

        elif pilih == 6:
            print("Jumlah kontak Fineshyt:",
                  kontak.count_contacts(kontak.root))

        elif pilih == 7:
            awal = kontak.find_first_contact(kontak.root)
            akhir = kontak.find_last_contact(kontak.root)

            if awal is not None:
                print("\nKontak Fineshyt pertama alfabet:")
                print(f"{awal.key} - {awal.nomor}")

            if akhir is not None:
                print("\nKontak Fineshyt terakhir alfabet:")
                print(f"{akhir.key} - {akhir.nomor}")

        elif pilih == 8:
            print("Program selesai, hope u find the love of your life soon big dawg")

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
