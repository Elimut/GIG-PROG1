#udelat
#0 1 2
#3 4 5
#6 7 8...

n = int(input("Zadej pocet radku: "))
m = int(input("Zadej pocet znaku na radek: "))

for i in range (0,n):
    for x in range(0,m):
        hodnota = i*m+x
        print(hodnota, end=" ")   
    print()
