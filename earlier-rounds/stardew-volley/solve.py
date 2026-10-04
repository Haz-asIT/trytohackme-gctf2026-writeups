from pathlib import Path
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

blob = Path("assets/volley.dat").read_bytes()
assert blob[:4] == b"SVL1"

magic = blob[:4]
nonce = blob[4:16]
tag = blob[16:32]
ciphertext = blob[32:]

order = [2, 7, 11, 14, 5, 9]
mask = bytes.fromhex(
    "00 12 25 3a 48 41 30 1d "
    "0c 04 10 21 34 3d 2b 15"
)

rally_profile = bytes(
    mask[value] ^ (0x31 + i * 7)
    for i, value in enumerate(order)
)

label = b"SVP/1.4"
normalized = bytes(
    b ^ 0x14 ^ i
    for i, b in enumerate(label)
)

unique_id = "Razlan.StardewVolley"
context = (unique_id + "\nVolleyball").encode()

material = context + b"\x00" + rally_profile + b"\x00" + normalized
key = hashlib.sha256(material).digest()

print("[+] rally_profile :", rally_profile.hex())
print("[+] normalized    :", normalized)
print("[+] AES key       :", key.hex())

plaintext = AESGCM(key).decrypt(nonce, ciphertext + tag, magic)
print("[+] plaintext:")
print(plaintext.decode())
