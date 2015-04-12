""" Slovníky jsou jediným zástupcem mapovacích typů
    slovnik = {
    KLÍČ1: HODNOTA1,
    KLÍČ2: HODNOTA2,
    ...
    }
Hodnotou může být cokoliv, klíč musí být ale neměnný datový typ.
Jsou to v podstatě hashovací tabulky optimalizované na vyhledávání hodnot podle klíčů
"""

dc = {'a':1,
      'b':[1,2,3],
      'c':"blah",
      }
print(type(dc))
print(dc) # bacha na pořadí prvků - je jiné!

##### vlastnosti #####

# dotaz na počet dvojic klíč:hodnosta
print(len(dc))

# dotaz na výskyt klíče
'a' in dc
123 in dc

# průchod klíči slovníku
for key in dc:
    print(key)

# dotaz na hodnotu odpovídající klíči 'b'
print(dc['b'])


""" přístup k prvkům :
    - známe-li klíč, můžeme pomocí něj získat odpovídající hodnotu
    - pomocí smyčky přes vybraný pohled na slovník probrat prvky slovníku jeden po druhém
    - views na slovník(dc):
        - ds.keys() <- pohled přes klíče
        - ds.values() <- pohled přes hodnoty
        - ds.items() - pohled přes n-tice (klíč, hodnota)

    - každého pohledu se můžeme zeptat na počet jeho členů pomocí fce len()
    - přes každý pohled můžeme iterovat (pomocí for in)
    - každý pohled můžeme testovat na přítomnost prvků pomocí operátoru in
"""

print(dc.keys())

for key in dc.keys():
    print(key)

# pohled přes hodnoty
print(dc.items())

print(('a', 1) in dc.items())

for (key, val) in dc.items():
    print(key, val)

""" zbytek toho je strašně strašně moc a dodělám to pak """

