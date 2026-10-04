import re

data = open("hastad.txt", "r").read()

e = int(re.search(r"^e\s*=\s*(\d+)", data, re.M).group(1))
ns = [int(x) for x in re.findall(r"^n\d+\s*=\s*(\d+)", data, re.M)]
cs = [int(x) for x in re.findall(r"^c\d+\s*=\s*(\d+)", data, re.M)]

print("[+] e =", e)
print("[+] Moduli found:", len(ns))
print("[+] Ciphertexts found:", len(cs))

assert len(ns) >= e
assert len(cs) >= e

N = 1
for n in ns:
    N *= n

combined = 0
for n, c in zip(ns, cs):
    Ni = N // n
    inv = pow(Ni, -1, n)
    combined += c * Ni * inv

m_to_e = combined % N

def integer_nth_root(value, power):
    low = 0
    high = 1
    while high ** power <= value:
        high *= 2
    while low + 1 < high:
        mid = (low + high) // 2
        if mid ** power <= value:
            low = mid
        else:
            high = mid
    return low

m = integer_nth_root(m_to_e, e)
assert m ** e == m_to_e

plaintext = m.to_bytes((m.bit_length() + 7) // 8, "big")
print("[+] Plaintext:", plaintext.decode())
