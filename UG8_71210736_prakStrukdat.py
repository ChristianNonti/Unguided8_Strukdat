class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3

    def __init__(self):
        self._items = [None] * Kasir.DEFAULT_CAPACITY
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Antrian kosong')
        else:
            item = self._items[0]
            for i in range(self._size - 1):
                self._items[i] = self._items[i + 1]
            self._items[self._size - 1] = None
            self._size -= 1
            return item.getNamaPelanggan()
        
    def enqueue(self, namaPelanggan):
        if self._size == len(self._items):
            self.resize(2 * len(self._items))
        node = NodePelanggan(namaPelanggan)
        self._items[self._size] = node
        self._size += 1
        
    def resize(self, cap):
        old_items = self._items
        self._items = [None] * cap
        for i in range(self._size):
            self._items[i] = old_items[i]
        for i in range(self._size, cap):
            self._items[i] = "kosong"
        
    def printAll(self):
        print('=== Kasir ===')
        if self.is_empty():
            print('Kosong')
        else:
            for i in range(self._size):
                print(f"{i+1}. {self._items[i].getNamaPelanggan()}")
        print()
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniff")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

print("### Melakukan Resize ###")
tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

print("### Pelanggan Haniif Selesai Membayar ###")
tempatKasir.dequeue()
tempatKasir.printAll()

print("### Pelanggan Beatrix Selesai Membayar ###")
tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

print("### Pelanggan Sindu Selesai Membayar ###")
tempatKasir.dequeue()
tempatKasir.printAll()
