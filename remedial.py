#Nama   : Siti Raudatul Jannah
#NIM    : 242410103048


#Soal NO 1
angka = int(input("angka akhir: ")) 
        
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
    print("bB")