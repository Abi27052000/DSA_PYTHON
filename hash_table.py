class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # To get ASCII value

        return h % self.Max

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        print(self.arr[h])


t = HashTable()
t.add("march 6", 130)
print(t.arr)
t.get("march 6")
