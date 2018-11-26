'''Hashing Using Chaining technique for Collision'''
class HashingUsingChaining:

    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None] * self.size

    def hashing(self,key,length):
        return key%length

    def __setitem__(self,key,data):
        hashkey = self.hashing(key, len(self.slots))
        if self.slots[hashkey] == None:
            self.slots[hashkey] = [key]
            self.data[hashkey] = [data]
        else:
            self.slots[hashkey].append(key)
            self.data[hashkey].append(data)

    def __getitem__(self, key):
        hashkey = self.hashing(key, len(self.slots))
        try:
            return self.data[hashkey][self.slots[hashkey].index(key)]
        except:
            return 'None'

    def __len__(self):
        return sum([len(x) for x in self.slots if x != None])

    def __contains__(self, item):
        for x in self.slots:
            if x != None and item in x:
                return True

    def __delitem__(self, key):
        hashkey = self.hashing(key, len(self.slots))
        self.data[hashkey].remove(self.data[hashkey][self.slots[hashkey].index(key)])

if __name__ == "__main__":
    H = HashingUsingChaining()
    print("__________ Hashing Using Chaining __________")
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    print(len(H))
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    del(H[55])
    H[20] = "chicken"
    print(H.slots)
    print(len(H))
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H[99])
    print(31 in H)
    print(33 in H)