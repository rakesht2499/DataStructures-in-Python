from DataStructures.LinearDS import Stack

def Converter(num,base):
    value,op,val_s = "0123456789ABCDEF","",Stack()
    while num > 0:
        val_s.push(num%base)
        num = num//base
    while not val_s.isEmpty():
        op += value[val_s.pop()]
    return op
if __name__ == "__main__":
    print("Binary of 256: ",Converter(256,2))
    print("Oct of 256: ",Converter(256,8))
    print("Hex of 256: ",Converter(256,16))