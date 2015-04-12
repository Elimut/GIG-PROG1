# všechno v Pythonu je first-class objekt (cokoliv je možné předat jako argument do funkce;
# můžeme tedy funkci předat i jinou funkci
# konvence = joined_lower - funkce, medoty, atributy
#            ALL_CAPS - konstanty ; StudlyCaps - třídy

""" help('list.append') <--- vypíše nápovědu """

# mutable datové typy - list, sets, dictionaries
# immmutable datové typy - strings, tuples
# sekvenční - str, list, tuple, ranges
# mapovací - dict

"""
string <-- "Ahoj světe"
list <-- [2, 'a', {},]
tuple <-- (2, 'a', {},)
set <-- {2, 'a', {},}
dictionary <-- { 'jmeno': ('Karel', 'Novák'), 'vek' 23,}
"""

##### for #####
for word in ["welcome", "to", "python"]:
    print(word)

#součet     
sum = 0
for i in range(10):
    # sum = 0 // nemůže to být tady ty blbe!
    sum += i
    
##### range #####
range(5) # range do 5 -> [0, 1, 2, 3, 4]
range(4,6) # range od 4 do 6 -> [4, 5] !!!!
range(1,7,2) # range od 1 do 7, skoky po 2 -> [1, 3, 5]

##### while #####
while True:
    print("ahoj")
    break

#vypíše čísla od 1 do 10
i = 1
while i <= 10:
    print(i)
    i += 1

##### if a elif #####
colours = ["red", "blue", "yellow", "pink", "black"]
animals = ["elephant", "horse", "my brother"]

word = "my brother"
if word in colours:
    print(word + " is a colour.")
elif word in animals:
        print(word + " is an animal")
else:
        print("Have no idea what " + word + " is!")
        

##### řetězec #####
s = "My brother is still an animal"
"""
len(s) -> 29
s[0] -> 'M'
s[-1] -> 'l' - vraci posledni prvek, stejne tak -2 bude vracet predposledni
s[-4:] -> 'imal' - posledni 4 prvky
s[1:29:2] -> 'ybohri tl naia'

'M' in s -> True
"""

##### FAKTORIAL (pomoci rekurze) #####
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
print(fac(9))

#haha, jsme lini
import math
print(math.factorial(9))

##### dir #####
dir('s') # tak to je vážně ale cool
