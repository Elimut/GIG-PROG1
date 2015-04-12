""" generátor seznamu (i nejen seznamu) umožnuje na minimu prostoru vytvořit z původnáho
seznamu nový seznam, který se skládá třeba z úplně nových prvků, ale je vytvořený na základě
prvků z původního seznamu a dodatečných pravidel """

# [Funce(I) for I in SEKVENCE [if PODMÍNKA]
xs = list(range(10))
print(xs)

## vytvoření kopie seznamu
[x for x in xs]

## každý prvek seznamu bude zvětšený o tři
xy = [x+3 for x in xs]
print(xy)

## seznam druhých mocnin původního seznamu
xz = [x*x for x in xs]
print(xz)

## výběr sudých prvků
print([x for x in xs if x%2 ==0])


# seznam tuplů, kde je každý prvek přítomen jako číslo a zároveň i jako řetězec
# woow!
print([(x, str(x)) for x in xs])

##### vícenásobná generátorová notace #####
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

# první prvek vynásobíme všemi prvky druhého seznamu
xy = [x*y for x in vec1 for y in vec2]
print(xy)

# skalární součin
xz = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(xz)
