import math

def szudzik_unpack(z):
    q = math.isqrt(z)
    r = z - q*q
    if r < q:
        x = r
        y = q
    else:
        x = q
        y = r - q
    return x, y

def unpack_recursive(z):
    # Original data is bytes, so leaf values are 0..255.
    if z <= 255:
        return [z]
    x, y = szudzik_unpack(z)
    return unpack_recursive(x) + unpack_recursive(y)

with open("output.txt", "r") as f:
    lines = f.read().splitlines()

z = int(lines[1])
data = unpack_recursive(z)

print("Byte values:", data)
print("Recovered:", bytes(data))
print("Flag:", bytes(data).decode())
