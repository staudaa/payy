kata = input()

kata1 = kata[::2]
kata2 = kata[1::2]

hasil1 = ""
hasil2 = ""
for i in kata1:
    hasil1 += chr(ord(i)-5)
for i in kata2:
    hasil2 += chr(ord(i)-5)

print(hasil1, "\n")
print(hasil2)
