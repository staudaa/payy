prima = int(input())    
    
jumlah = 0
for num in range(5, 15):
    for i in range(3, num):
        if num % i == 0:
            break
    else : 
        n = (num % i)
        while n > 0:
            n //= 10
            jumlah += 1

        print(jumlah)