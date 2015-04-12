""" SEZNAMY
    - pomocí list(xs) se dají jiné typy převádět na seznam
    - taky jsou jako sekvence, takze všechny ty metody, co šly použít u řetezců, jdou použít i tady
    - taky se v nich dá procházet smyčkou i zjištovat pozici výskytu prvku
    """    
# seznamy jsou měnitelné sekvence!
    # (jejich obsah můžeme po vytvoření libovolně upravovat)
xs = [1, 2, 3, ('ctyri', 'pet'), ['sest', 'sedm'], 'osm']
print(xs)
xs[4]='devet' #to není víceúrovnové??
print(xs)

## klasické použití in
print('osm' in xs)
print('devet' in xs)

##index = vrací pozici prvního výskytu prvku s uvedenou hodnotou
print(xs.index(3))
# jinak ValueError
xs.count('osm') #počítá výskyty zadaného prvku


##### přidávání prvku do seznamu #####
xs = [1, 2.0, 'dva']
xs.append('blah') #přidá prvek na konec seznamu
print(xs)

# insert vkládá prvek před určitou pozici v seznamu
xs.insert(3, 'bl') # 3 = pozice prvku ZA!
print(xs)

# extend vkládá na konec seznamu více prvků jiného seznamu
xs.extend(['brain', 'fuck'])
print(xs)

# bacha na rozdíl mezi extendem a appendem. Append seznam nerozbaluje a vznikná tak seznam s připojeným podseznamem na konci původního seznamu
# extend() seznam "rozbalí"7


##### odebírání prvků ze seznamu #####
xs = ['jedna', 'dve', 'tri', 'ctyri', 'pet', 'sest']

# del odebírá prvky na základě jejich pozice
del xs[3:] #odebere od 'ctyri' a dal

# pop([index]) dělá vesměs to samé
xs.pop() #odstraní poslední prvek
xs.pop(0) #odstraní první prvek ... a tak dál...

# remove(PRVEK) odstranuje prvek na základě jeho obsahu. Odstraní první prvek výskytu
xs = ['jedna', 'dve', 'tri', 'ctyri', 'pet', 'sest']
xs.remove('tri') #odstrani trojku


##### řazení #####
xs = [1, 2, 3, 4, 5, 6]

# reverse() otočí seznam
xs.reverse() #operuje nad aktuálním seznamem, nic nevrací

# sort([key[, reverse]])
xs = ['jedna', 'dve', 'tri', 'ctyri', 'pet', 'sest']
xs.sort()
print(xs)
# toto třídění se děje přímo v místě, takže ztratíme původní uspořádání
# další průser -> třídění probíhá porovnáváním unicodových code-points, takže české znaky jsou až za ASCII

# sorted()
xs = ['jedna', 'dve', 'tri', 'ctyri', 'pet', 'sest']
ys = sorted(xs)
# ponechává původní seznam beze změny

# obě funkce se navíc dají použít i s parametrem reverse
sorted(xs, reverse=True)

# další magický parametr je parametr "key" - slouží k určení porovnávacího klíče nad prvky seznamu
jmena = ["Rimmer", "Lister", "Kryton", "Cat", "Joffrey", "Daenerys"]
sorted(jmena, key=len) #setridi to podle delky, ale zachová jejich původní pořadí
#pokud chceme stejně dlouhé prvky navíc i setřídit podle abecedy, tak v tento moment přichází lambda
sorted(jmena, key=lambda x: (len(x),x))



















