sealed = [
    180, 64, 182, 79, 0, 145, 185, 92,
    84, 106, 11, 228, 69, 146, 39, 16,
    96, 40, 89, 104, 26, 80, 166, 253,
    62, 236
]

def F(x, key):
    return ((x * 5) & 0xff) ^ key

def undo_round(L, R, key):
    old_R = L
    old_L = R ^ F(old_R, key)
    return old_L, old_R

plain = []
for i in range(0, len(sealed), 2):
    L, R = sealed[i], sealed[i + 1]
    L, R = undo_round(L, R, 0xA7)
    L, R = undo_round(L, R, 0x3C)
    plain.extend([L, R])

print(bytes(plain).decode())
