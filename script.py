import os.path
import time

start = time.time()
rep = "test/"
key = "".encode()
sizeKey = len(key)
count = 0

def chunkString(string,length):
    return (list(string[0+i:length+i] for i in range(0, len(string), length)))

def byte_xor(b):
    return bytes([_a ^ _b for _a, _b in zip(b, key)])

def total_time(start,end):
    return(end-start)

for root, dirs, files in os.walk(rep, topdown=False):
   for name in files:
        print("Processing...")
        count+=1
        link = os.path.join(root, name)
        sizeFile = os.path.getsize(link)
        with open(link,"rb") as f:
            content = f.read()
            content = chunkString(content,sizeKey)
            cryptedContent = list(map(byte_xor,content))
        with open(link,"wb") as f:
            for e in cryptedContent:
                f.write(e)
            # map(f.write,cryptedContent)

print("END")
print(total_time(start,time.time()))
print(str(count)+" files crypted.")
