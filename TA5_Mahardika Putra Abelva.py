#Mahardika Putra Abelva
#2515061076
class Node:
    def __init__(self, nama):
        self.key = nama
        self.left = None
        self.right = None


class BSTKontak:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nama):
        if root is None:
            return Node(nama)

        if nama < root.key:
            root.left = self.insert_node(root.left, nama)

        elif nama > root.key:
            root.right = self.insert_node(root.right, nama)

        return root

    def insert(self, nama):
        self.root = self.insert_node(self.root, nama)

    def search_node(self, root, nama):
        if root is None:
            return False

        if root.key == nama:
            return True

        if nama < root.key:
            return self.search_node(root.left, nama)

        return self.search_node(root.right, nama)

    def search(self, nama):
        return self.search_node(self.root, nama)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return

        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

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

        return current.key

    def find_last_contact(self, root):
        if root is None:
            return None

        current = root

        while current.right is not None:
            current = current.right

        return current.key


def main():
    kontak = BSTKontak()

    pilih = 0

    while pilih != 8:
        print("\nSistem Save Kontak Fineshyt Whatsapp")
        print("1. Tambah Kontak Fineshyt")
        print("2. Cari Kontak Fineshyt")
        print("3. Urutkan Inorder")
        print("4. Urutkan Preorder")
        print("5. Urutkan Postorder")
        print("6. Jumlah Kontak Fineshyt")
        print("7. Fineshyt Awal & Akhir")
        print("8. Keluar")

        pilih = int(input("Pilih menu: "))

        if pilih == 1:
            nama = input("Masukkan nama kontak: ")
            kontak.insert(nama)
            print("Kontak berhasil ditambahkan")

        elif pilih == 2:
            nama = input("Masukkan nama yang dicari: ")

            if kontak.search(nama):
                print("Kontak ditemukan")
            else:
                print("Kontak tidak ditemukan")

        elif pilih == 3:
            print("Data kontak inorder:")
            kontak.inorder(kontak.root)

        elif pilih == 4:
            print("Data kontak preorder:")
            kontak.preorder(kontak.root)

        elif pilih == 5:
            print("Data kontak postorder:")
            kontak.postorder(kontak.root)

        elif pilih == 6:
            print("Jumlah kontak:",
                  kontak.count_contacts(kontak.root))

        elif pilih == 7:
            print("Kontak pertama alfabet:",
                  kontak.find_first_contact(kontak.root))

            print("Kontak terakhir alfabet:",
                  kontak.find_last_contact(kontak.root))

        elif pilih == 8:
            print("Program selesai")

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
