angka = int(input("angka akhir: ")) 
        
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