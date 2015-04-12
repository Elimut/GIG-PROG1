""" N-tice (tuples). Jsou důležitější než seznamy.
    Jsou to sekvenční typy, ale narozdíl od seznamu jsou neměnitelné!
    Vytváří se ohraničením do kulatých závorek """

xs = ('Ahoj!', 123, (12, 'tři'), ['hokus', 'pokus'], 'blah')
print(xs)

# dále lze za pomocí funkce tuple() převádět jiné typy na n-tice
xs = "Hello world"
print(tuple(xs))

##### sekvěnční operace #####
xs = ('Ahoj!', 123, (12, 'tri'), ['hokus', 'pokus'], 'blah')

len(xs)
xs[3]
xs[-3]
xs[1:3]
xs[1::2]

# dotaz na výskyt prvku
print(123 in xs)

# dvě spojené kopie
print(xs*2)

# po sekvencích se dá procházet smyčkou
for x in xs:
    print(x)

for(i, x) in enumerate(xs):
    print(i, x)

# index(PRVEK)
xs = ('jedna', 'dva', 'tři', 'ctyri', 'pet', 'jedna')
print(xs.index('jedna'))
xs.index('pet')

# počítání výskytu zadaného prvku
print(xs.count('jedna'))

##### předání hodnot #####
def fce(x):
    return x, x**2, x**3
# A) vrácení n-tice bez rozbalení
y = fce(2)
print(y)
print(type(y))

# B) vrácení a rozbalení n-tice
prvni, druha, treti = fce(3)
print(prvni, druha, treti)

# iterace seznamů
x, y, z = [1, 2, 3]
print(x) # <- 1


