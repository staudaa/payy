angka = input()
angka_split = angka.split(",")
target = input()
hasil = int(target)


kosong = []
for i in angka_split :
    for j in angka_split :
        if int(i) + int(j) == hasil :
            kosong.append([i, j])
            angka_split.remove(j)
print(kosong)

