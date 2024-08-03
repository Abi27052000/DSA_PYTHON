class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    # def __getitem__(self, key):
    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, val)
                return

        self.arr[h].append((key, val))

    def __delitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                break


t = HashTable()
t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459

print(t.arr)
del t["march 17"]
print(t.arr)
