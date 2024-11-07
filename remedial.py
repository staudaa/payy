#Nama   : Siti Raudatul Jannah
#NIM    : 242410103048


#Soal NO 1
angka = int(input()) 
        
if 1 <= angka <= 999 :
    for j in range (1, angka+1) :
        if j % 3 == 0:
            if j % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else:
            print(j)
        
else :
    print("angka diluar kondisi")

#Soal NO 2
awal = int(input())
akhir = int(input())

print()
if(0 < awal < akhir < 100):
    count = 0
    for i in range(awal+1, akhir+1):
        prima = True
        for j in range(2, i):
            if i % j == 0:
                prima = False
                break
        if(prima):
            count = count+1
    print(count)
else:
    print("Angka diluar kondisi")
    

#Soal NO 3
kata = input()

huruf = {}
for i in kata:
    if(i == " "):
        continue
    elif huruf == {}:
        huruf.update({i:1})
    else:
        if(huruf.get(i)):
            huruf.update({i:(huruf.get(i)+1)})
        else:
            huruf.update({i:1})

for alp in huruf:
    print("Huruf:", alp, ": Jumlah: ", huruf.get(alp))
    
    
#Soal NO 4
data = input()
data_split = data.split(" ")

count = 0
for i in data_split :
    if i.isalpha():
        if 'e' in i or 'd' in i:
            count += 1
    else :
        print("Inputan Harus Berupa Alphabet!")
print(count)


#Soal NO 5
angka = input()
angka_split = angka.split(", ")
target = input()
hasil = int(target)


kosong = []
for i in angka_split :
    for j in angka_split :
        if int(i) + int(j) == hasil :
            kosong.append([i, j])
            angka_split.remove(j)
print(kosong)


#Soal NO 6
kiri = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
kanan = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]
kata = input()
tangan = [] # 0 = kiri, 1 = kanan

for i in kata:
    for j in kiri:
        if i == j:
            tangan.append(0)
            break
    for j in kanan:
        if i == j:
            tangan.append(1)
            break
posisi = ""
hasil = True
for i in tangan:
    if i == 0:
        if posisi == "kiri":
            hasil = False
            break
        else:
            posisi = "kiri"
    else:
        if posisi == "kanan":
            hasil = False
            break
        else:
            posisi = "kanan"
print(hasil)


#Soal NO 7
message = input()
messagee = input()

