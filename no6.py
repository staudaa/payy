kiri = "q, w, e, r, t, a, s, d, f, g, z, x, c, v, b".split(", ")
kanan = "y, u, i, o, p, h, j, k, l, n, m".split(", ")

masukan = input()
tangan = [] # 0 = kiri, 1 = kanan
for i in masukan:
    for j in kiri:
        if i == j:
            tangan.append(0)
            break
    for j in kanan:
        if i == j:
            tangan.append(1)
            break
posisi = ""
aaa = True
# print(tangan)
for i in tangan:
    if i == 0:
        if posisi == "kiri":
            aaa = False
            break
        else:
            posisi = "kiri"
    else:
        if posisi == "kanan":
            aaa = False
            break
        else:
            posisi = "kanan"
print(aaa)