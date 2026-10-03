t = "60697976212062707651517748415c4468534e1f30322020230d36373f3b1c"
b = bytes.fromhex(t)

flag = "".join(
    chr(x ^ ((i * 3 + 7) & 0xff))
    for i, x in enumerate(b)
)

print(flag)
