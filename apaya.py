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