import hashlib

BLOB = b'\xf1\r\t\xdal\x9aG\x13U\x89x\x19B\xcf\x00\x96\xdd\x00,\x8f\x86\xc0+\xdf!\xa8Qg}\xd4\x03u\xe6\x1d\x00'
n = 224737

key = hashlib.sha256(str(n).encode()).digest()
stream = (key * ((len(BLOB) // len(key)) + 1))[:len(BLOB)]
flag = bytes(a ^ b for a, b in zip(BLOB, stream))
print(flag.decode())
