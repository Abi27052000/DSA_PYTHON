class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    # def __getitem__(self, key):
    def __getitem__(self, key):

        h = self.get_hash(key)

        if self.arr[h] == None:
            return
        for idx in list(range(h, self.MAX)) + list(range(0, h)):
            if self.arr[idx] == None:
                continue

            if self.arr[idx][0] == key:
                return self.arr[idx][1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if self.arr[h] == None:
            self.arr[h] = (key, val)
            return

        elif self.arr[h][0] == key:
            self.arr[h] = (key, val)
            return

        else:
            for idx in list(range(h, self.MAX)) + list(range(0, h)):
                if self.arr[idx] == None:
                    self.arr[idx] = (key, val)
                    return

                elif self.arr[idx][0] == key:
                    self.arr[idx] = (key, val)
                    return

    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h] == None:
            return

        for idx in list(range(h, self.MAX)) + list(range(0, h)):

            if self.arr[idx] == None:
                return

            if self.arr[idx][0] == key:
                self.arr[idx] = None


t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
t["march 33"] = 999
t["april 1"] = 87
t["april 2"] = 123
t["april 3"] = 234234
t["april 4"] = 91
t["May 22"] = 4
t["May 7"] = 47
print(t.arr)

del t["april 2"]

print(t.arr)
