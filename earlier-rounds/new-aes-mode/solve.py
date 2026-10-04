from pwn import *
import hashlib

HOST = "play.gctf.ctf.onl"
PORT = 33709

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def digest(ciphertext):
    length = len(ciphertext).to_bytes(16, "big")
    return hashlib.sha3_256(ciphertext + length).digest()[:16]

io = remote(HOST, PORT)

io.recvuntil(b"Challenge nonce: ")
nonce = bytes.fromhex(io.recvline().strip().decode())

io.recvuntil(b"Challenge ciphertext: ")
ct = bytes.fromhex(io.recvline().strip().decode())

io.recvuntil(b"Challenge tag: ")
tag = bytes.fromhex(io.recvline().strip().decode())

print("[+] nonce =", nonce.hex())
print("[+] ct    =", ct.hex())
print("[+] tag   =", tag.hex())

mask = xor(tag, digest(ct))

ct2 = bytearray(ct)
ct2[0] ^= 1
ct2 = bytes(ct2)

tag2 = xor(digest(ct2), mask)

io.sendlineafter(b"> ", b"2")
io.sendlineafter(b"Nonce (hex): ", nonce.hex().encode())
io.sendlineafter(b"Ciphertext (hex): ", ct2.hex().encode())
io.sendlineafter(b"Tag (hex): ", tag2.hex().encode())

io.recvuntil(b"Plaintext: ")
p2 = bytes.fromhex(io.recvline().strip().decode())

print("[+] modified plaintext =", p2.hex())

plaintext = bytearray(p2)
plaintext[0] ^= 1
plaintext = bytes(plaintext)

print("[+] challenge plaintext =", plaintext.hex())

io.sendlineafter(b"> ", b"3")
io.sendlineafter(
    b"Challenge plaintext (hex): ",
    plaintext.hex().encode()
)

print(io.recvall().decode())
