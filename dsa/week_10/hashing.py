
class HashTable:
    def __init__(self, size, method):
        self.size = size
        self.method = method
        self.table = [[] for _ in range(size)] if method == 1 else [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)

        if self.method == 1:  # Separate Chaining
            if key not in self.table[index]:
                self.table[index].append(key)

        elif self.method == 2:  # Linear Probing
            for i in range(self.size):
                pos = (index + i) % self.size
                if self.table[pos] is None:
                    self.table[pos] = key
                    return
            print("Hash table is full!")

        elif self.method == 3:  # Quadratic Probing
            for i in range(self.size):
                pos = (index + i * i) % self.size
                if self.table[pos] is None:
                    self.table[pos] = key
                    return
            print("No empty position found!")

    def search(self, key):
        index = self.hash(key)

        if self.method == 1:
            return key in self.table[index]

        for i in range(self.size):
            if self.method == 2:
                pos = (index + i) % self.size
            else:
                pos = (index + i * i) % self.size

            if self.table[pos] is None:
                return False

            if self.table[pos] == key:
                return True

        return False

    def delete(self, key):
        index = self.hash(key)

        if self.method == 1:
            if key in self.table[index]:
                self.table[index].remove(key)
                print("Deleted successfully!")
            else:
                print("Key not found!")
            return

        for i in range(self.size):
            if self.method == 2:
                pos = (index + i) % self.size
            else:
                pos = (index + i * i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Deleted successfully!")
                return

        print("Key not found!")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


print("HASHING TECHNIQUES")
print("1. Separate Chaining")
print("2. Linear Probing")
print("3. Quadratic Probing")

method = int(input("Choose hashing technique: "))
size = int(input("Enter hash table size: "))

h = HashTable(size, method)

while True:
    print("\n--- MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        h.insert(key)

    elif choice == 2:
        key = int(input("Enter key: "))
        if h.search(key):
            print("Key found!")
        else:
            print("Key not found!")

    elif choice == 3:
        key = int(input("Enter key: "))
        h.delete(key)

    elif choice == 4:
        h.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
