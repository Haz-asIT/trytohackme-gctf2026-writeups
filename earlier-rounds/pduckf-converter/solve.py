from pathlib import Path
import hashlib, zlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

exe = Path("PDuckF.exe").read_bytes()

p = exe.index(b"PDFL\x01\x01\x00\x00")
blob = exe[p:p+80]
nonce = blob[8:20]
ct_len = int.from_bytes(blob[20:24], "little")
ct = blob[24:24+ct_len]
tag = blob[24+ct_len:24+ct_len+16]

s = exe.index(b"%PDF-1.4")
e = exe.index(b"%%EOF", s) + len(b"%%EOF")
while e < len(exe) and exe[e] in b"\r\n":
    e += 1
pdf = exe[s:e]

def field(t, k, data):
    return bytes([t, k]) + len(data).to_bytes(2, "little") + data

mat = bytes.fromhex("4017f3ffc48aa906f44fbe6c674af9d37487d45cd52779a995b6ceee409b0a23")
ref = bytes.fromhex("768f33a9ad137d5a3ea452a4b561a5b62243e00f6855511d1784534931c625d7")

fields = [
    field(0x05, 0x03, hashlib.sha256(pdf).digest()),
    field(0x04, 0x02, len(pdf).to_bytes(8, "little")),
    field(0x03, 0x02, b"\x01"),
    field(0x14, 0x01, b"PDuckF Offline PDF Engine 1.0"),
    field(0x11, 0x01, b"Private Document Handling Notice"),
    field(0x17, 0x02, (1).to_bytes(4, "little")),
    field(0x12, 0x01, b"PDuckF Documentation Team"),
    field(0x10, 0x01, b"1.4"),
    field(0x02, 0x01, b".pdf"),
    field(0x01, 0x01, b"Private_Notice.pdf"),
    field(0x13, 0x01, b"PDuckF Private Document Utility"),
    field(0x15, 0x01, b"D:20260919090000+08'00'"),
    field(0x16, 0x01, b"D:20260919090000+08'00'"),
    field(0x20, 0x01, b"https://privacy-guide.invalid/offline"),
    field(0x20, 0x01, b"https://document-safety.invalid/local"),
]

payload = b"".join(fields)
pdr2 = (
    b"PDR2" + b"\x02\x01"
    + len(fields).to_bytes(2, "little")
    + len(payload).to_bytes(4, "little")
    + zlib.crc32(payload).to_bytes(4, "little")
    + payload
)

d1 = hashlib.sha256(pdr2).digest()
key = hashlib.sha256(b"PDuckF.flag.v1" + mat + d1).digest()
assert hashlib.sha256(key + b"PDuckF.reference.v1").digest() == ref

print(AESGCM(key).decrypt(nonce, ct + tag, blob[:24]).decode())
