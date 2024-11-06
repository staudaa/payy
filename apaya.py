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

