""" řetězce.
    i toto je vlastně řetězec.
    """

##### kolizní uvozovky #####
print("Ahoj, 'Pavle', jak se máš?")
print('Ahoj, "Petře", a jak ty?')
print("Ahoj, \"Kamile\", tebe se ptát nebudem\n")
print("Já jsem Kamil, \n\ta jsem fajn\n")

##### sekvenční operace #####
xs = "Přivítejte podplukovníka Matku Terezu !!!"
print("xs: " + xs)
print("délka xs: " + (str(len(xs))))
print(xs[6]) #nějak to hapruje s češtinou. Python 3 pokládá vše za UTF-8, ale Python 2 pokládá všechno za ASCII. Supr.
print(xs[-3]) #třetí od konce
print(xs[7:44:10])
print(xs[10:])

# dotaz na výskyt prvku
'!!' in xs #true
'oo!' in xs #false

# s řetezci se dají dělat celkem dobré harakiri
print(xs * 2)
print((xs[7:44:5]*2)+(xs[-10:]))
for x in xs:
    " print(x) "
# pokud je důležitá i pozice výskytu, tak:
for (i, x) in enumerate(xs):
   " print(i, x) "

##### zarovnání textu #####
xs = "BLAH"
xs.center(40)
xs.center(40, '*')
xs.ljust(40, '-')
xs.rjust(40, '+')

 
##### analýza #####
'123'.isalnum() #alfanumericke znaky (+*/ tam nepatri!)
'abc'.isalpha() #abeceda
'123'.isdigit() #cisla
'  '.isspace() #mezera. vyuziti asi nulove
'abc'.islower() #mala pismena
'ABC'.isupper() #velka pismena
'Ahoj Zas A Znova'.istitle() #titulek

# další metody analýzy (ale už ne tak globální)
xs = "Pan Seznam se rád seznamuje s neznámými"
xs.count('se') # -> 2
xs.startswith('P') # true
xs.endswith('i') # false
print(xs.startswith('Pan'))

## vyhledávání podřetězců ##
xs = "There were 42 monkeys in the airplane."
print(xs.find('e')) #najde první výskyt! -> 2
print(xs.rfind('e')) #najde poslední výskyt! -> 36
print(xs.find('e', 5, 18)) #najde v xs [5:18]

""" index a rindex fungují stejně jako find a rfind. pouze je místo -1 u index vráceno
    ValueError při neúspěšném hledání """

## úprava písmen ##
xs = "Apples, Citrones and peaches!"
print(xs.swapcase())
print(xs.upper())
print(xs.lower())
print(xs.title())
print(xs.capitalize())

## odstranování znaků ##
xs = "12Jabka, citrony a hrušky 34"
print("\n" + xs)
print(xs.strip('1234'))
print(xs.lstrip('1234'))
print(xs.rstrip('1234'))
# bez parametru ten strip smaže mezery zleva zprava
 
## záměna znaků ##
xs = "USA, China, Slovakia, Slovenia"
print(xs)
print(xs.replace(',', ' - '))
print(xs.replace(',', ' - ', 2))

## split() ##
# vrací seznam
xs = "All men must die."
print(xs.split())
print(xs.split(' ',2))
print(xs.split('m'))

print(xs.rsplit(' ',2))

## partition() <-rozdělí řetezec podle prvního výskytu sep. ##
print(xs.partition('e'))
print(xs.rpartition('e'))
print(xs.partition('must'))
# nezahazuje separátor a navíc vrací tupl!!!

## join() ##
print("\n" + xs)
ys = xs.split()
print(ys)
print(' '.join(ys)) #woohoou, zas to spojí dohromady






