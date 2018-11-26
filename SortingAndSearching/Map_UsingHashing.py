'''Hashing Using Linear Probing and Quadratic Probing'''
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size
                                                                                        # - (Uncomment the lines (1) to (8) For Quadratic Hashiing)
    def __getitem__(self, key): #get() or Fetch
        # temp = 1                                                                     - (1)
        found = False
        startKey = self.hashing(key, len(self.slots))
        if self.slots[startKey] == key:
            found = True
        nexthash = startKey
        while self.slots[nexthash] != None and not found:
            nexthash = self.reHashing(nexthash, len(self.slots))                       #- (Comment this line For Quadratic Hashiing)
            # nexthash = self.quadraticReHashing(nexthash, len(self.slots),temp**2)     - (2)
            # temp += 1                                                                 - (3)
            if nexthash == startKey:
                break
            if self.slots[nexthash] == key:
                found = True
        if found == True:
            return self.data[nexthash]
        else:
            return None

    def __setitem__(self, key, data): #put() or Insert
        # temp = 1                                                                     - (4)
        hashkey = self.hashing(key, len(self.slots))
        if self.slots[hashkey] == None:
            self.slots[hashkey] = key
            self.data[hashkey] = data
        elif self.slots[hashkey] == key:
            self.data[hashkey] = data
        else:
            newHashKey = self.reHashing(hashkey, len(self.slots))                       #- (Comment this line For Quadratic Hashiing)
            # newHashKey = self.quadraticReHashing(hashkey, len(self.slots),temp**2)    - (5)
            # temp+=1                                                                   - (6)
            while self.slots[newHashKey] != None and self.slots[newHashKey] != key:
                newHashKey = self.reHashing(newHashKey, len(self.slots))                        #- (Comment this line For Quadratic Hashiing)
                # newHashKey = self.quadraticReHashing(newHashKey, len(self.slots),temp**2)   - (7)
                # temp+=1                                                                     - (8)

            if self.slots[newHashKey] == None:
                self.slots[newHashKey] = key
                self.data[newHashKey] = data
            else:
                self.data[newHashKey] = data

    def hashing(self,key,length):
        return key%length

    def reHashing(self,key,length):
        return (key+1)%length

    def quadraticReHashing(self,key,length,rehashFactor):
        return (key+rehashFactor)%length

    def __len__(self):
        return sum([1 for x in self.slots if x != None])

    def __contains__(self, item):
        return item in self.slots

    def __delitem__(self, key):
        index = self.slots.index(key)
        self.slots[index] = None
        self.data[index] = None

if __name__ == "__main__":
    H = HashTable()

    print("__________ Hashing Using Linear Probing __________")

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
#Best Time Complexity - O (1) [with no collosions]
#Worst Time Complexity - O (K) [where k is the size of HashTable]