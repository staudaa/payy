angka = int(input()) 
        
for j in range (1, 999) :
    for game in angka :
        if game % 3 == 0 :
            game = "Fizz"
        elif game % 5 == 0 :
            game = "Buzz"
        print(game)