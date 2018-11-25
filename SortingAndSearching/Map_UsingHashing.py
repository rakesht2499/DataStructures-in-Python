class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self,key,data):
        hashkey = self.hashing(key,len(self.slots))
        if self.slots[hashkey] == None:
            self.slots[hashkey] = key
            self.data[hashkey] = data
        elif self.slots[hashkey] == key:
            self.data[hashkey] = key
        else:
            newHashKey = self.reHashing(hashkey,len(self.slots))
            while self.slots[newHashKey] != None and self.slots[newHashKey] != key:
                newHashKey = self.reHashing(newHashKey,len(self.slots))

            if self.slots[newHashKey] == None:
                self.slots[newHashKey] = key
                self.data[newHashKey] = data
            else:
                self.data[newHashKey] = data

    def get(self,key):
        found = False
        startKey = self.hashing(key,len(self.slots))
        if self.slots[startKey] == key:
            found = True
        nexthash = startKey
        while self.slots[nexthash] != None and not found:
            nexthash = self.reHashing(nexthash, len(self.slots))
            if nexthash == startKey:
                break
            if self.slots[nexthash] == key:
                found = True
        if found == True:
            return self.data[nexthash]
        else:
            return None

    def hashing(self,key,length):
        return key%length

    def reHashing(self,key,length):
        return (key+1)%length

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)

if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H[99])
#Best Time Complexity - O (1) [with no collosions]
#Worst Time Complexity - O (K) [where k is the size of HashTable]