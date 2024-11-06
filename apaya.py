data = input()
data_split = data.split(" ")

count = 0
for i in data_split :
    if i.isalpha():
        if (i == "e" ) :
            count += 1
            continue
        elif (i == "d" ) :
            count += 1
            continue
    else :
        print("Inputan Harus Berupa Alphabet!")
    # print(count)
