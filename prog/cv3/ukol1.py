delitel = 14
r = range(100,701)
for x in r:
    zb = x%delitel   #zbytek po deleni
    if zb == 0:
        print(x) 
