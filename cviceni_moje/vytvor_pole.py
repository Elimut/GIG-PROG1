seznam = []
x = 1

for i in range(0,3):
    radek = []
    for j in range(0,4):
        radek.append(x)
        x += 1
    seznam.append(radek)


for k in range(0,len(seznam)):
    print(seznam[k])
