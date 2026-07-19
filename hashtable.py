class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Check if key already exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Add new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = self.hash_function(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True

        return False

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")


if __name__ == "__main__":

    ht = HashTable()

    ht.insert("Alice", 90)
    ht.insert("Bob", 85)
    ht.insert("Charlie", 95)

    print("Search Alice:", ht.search("Alice"))
    print("Search Bob:", ht.search("Bob"))

    ht.delete("Bob")

    print("Search Bob after deletion:", ht.search("Bob"))

    ht.display()
