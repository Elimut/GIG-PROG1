def fce1(n):
    for x in range(3,10):
        if n%x==0:
            print("Cislo", n,"je bezezbytku delitelne", str(x))
   
n = float(input("Zadej cislo: "))
fce1(n)
