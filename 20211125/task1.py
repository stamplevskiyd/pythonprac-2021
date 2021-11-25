import struct, random

f = "fi"*10
file = open("struct", "wb")
data = tuple(random.random() if i % 2 == 0 else random.randint(0, 100) for i in range(20))
r = struct.pack(f, *data)
file.write(r)
file.close()
file = open("struct", "rb")
r = file.read()
s = struct.unpack(f, r)
print(s)
