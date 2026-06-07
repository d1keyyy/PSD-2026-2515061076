class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nIsi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    cctv_system = HashMapSeparateChaining()

    cctv_system.insert(1001, "Bundaran Gajah")
    cctv_system.insert(1011, "Terminal Rajabasa")
    cctv_system.insert(1021, "Simpang Tanjung Karang")
    cctv_system.insert(1002, "Mall Boemi Kedaton")
    cctv_system.insert(1031, "Hajimena")


    pilihan = 0
    
    while pilihan != "5":
        print ("\n===System CCTV Bandarlampung===")
        print("1. Tampilkan CCTV\n2. Tambah CCTV\n3. Cari CCTV\n4. Hapus CCTV\n5. Keluar\nPilih (1-5): ")
        try:
            pilihan = input()
        except ValueError:
            print("Input tidak valid, masukkan angka 1-5.")
            continue
        if pilihan == "1":
            cctv_system.display()
        elif pilihan == "2":
            cctv_system.insert(int(input("Masukkan ID CCTV baru: ")), input("Masukkan lokasi CCTV baru: "))
        elif pilihan == "3":
            id_cctv = int(input("Masukkan ID CCTV yang dicari: "))
            hasil = cctv_system.search(id_cctv)
            if hasil is not None:
                print(f"CCTV ditemukan: ID {hasil.key}, Lokasi: {hasil.value}")
            else:
                print("CCTV tidak ditemukan.")
        elif pilihan == "4":
            id_cctv = int(input("Masukkan ID CCTV yang ingin dihapus: "))
            cctv_system.remove_key(id_cctv)
        elif pilihan == "5":
            print("Keluar dari program.")
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")



if __name__ == "__main__":
    main()
