#Mahardika Putra Abelva
#251506076

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"Pengunjung '{data}' masuk ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong!")
            return

        hapus = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Pengunjung '{hapus}' telah dilayani.")

    def peek(self):
        if self.is_empty():
            print("Antrian kosong!")
        else:
            print(f"Antrian terdepan: {self.front.data}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong!")
            return

        current = self.front
        no = 1

        print("\nDaftar Antrian Pengunjung:")
        while current:
            print(f"{no}. {current.data}")
            current = current.next
            no += 1

    def hitungTotalPengunjung(self):
        total = 0
        current = self.front

        while current:
            total += 1
            current = current.next

        print(f"Total pengunjung dalam antrian: {total}")

    def cariPengunjung(self, nama):
        current = self.front
        posisi = 1

        while current:
            if current.data.lower() == nama.lower():
                print(f"Pengunjung '{nama}' ditemukan pada antrian ke-{posisi}")
                return

            current = current.next
            posisi += 1

        print(f"Pengunjung '{nama}' tidak ditemukan.")

    def clearQueue(self):
        self.front = None
        self.rear = None
        print("Semua antrian berhasil dihapus.")

    def is_empty(self):
        return self.front is None


def main():
    queue = QueueLinkedList()
    pilih = 0

    while pilih != 8:
        print("\n=== Manajemen Antrian Pengunjung Perpustakaan ===")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Tampilkan")
        print("5. Hitung Total Pengunjung")
        print("6. Cari Pengunjung")
        print("7. Hapus Semua Antrian")
        print("8. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            val = input("Nama Pengunjung: ")
            queue.enqueue(val)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            queue.hitungTotalPengunjung()

        elif pilih == 6:
            nama = input("Masukkan nama pengunjung yang dicari: ")
            queue.cariPengunjung(nama)

        elif pilih == 7:
            queue.clearQueue()

        elif pilih == 8:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
