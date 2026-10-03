c = [207, 206, 36, 221, 236, 247, 57, 60, 7, 60, 12, 56, 2, 6, 15, 25, 18, 18, 119, 117, 113, 104, 65, 68, 93]

flag = bytes(
    ((b ^ 0xA5) - 5*i - 3) & 0xff
    for i, b in enumerate(c)
)

print(flag.decode())
