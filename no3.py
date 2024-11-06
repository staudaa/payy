kata = input()

# listKata = kata.split()
# print(listKata)
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