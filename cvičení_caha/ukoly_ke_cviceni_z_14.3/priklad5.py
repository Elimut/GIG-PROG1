a = int(input("Zadej jednu hranici intervalu:"))
b = int(input("Zadej druhou hranici intervalu:"))

found = False

for x in range(a,b):
    if x%17==0 and x%14==0:
        found = True
        print(x)

if found:
    print("Hodnota existuje.")
else:
    for x in range(a-50,b+50):
        if x%17==0 and x%14==0:
            found = True
    if found:
        print("Hodnota existuje v rozšířeném intervalu.")
    else:
        print("Hodnota neexistuje ani v rozšířeném intervalu.")
