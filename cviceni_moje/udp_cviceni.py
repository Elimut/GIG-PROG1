 # Napište program, který vypíše část řetězce před prvním výskytempísmene „m“.

text="Jak jsi na tom, co dnes podniknem?"
	if "m" in text:
		print( text[:text.index("m")] )
	else:
		print (text)

# Napište fukci, která bere jako první argument seznam celých číselxsajako druhý jedno celé čísloy. Výstupem funkce je seznamysobsahující tačísla zxs, která jsou větší ney
#.Ukázka:
#  f([1,2,3,1,2,1,2,4,6,2], 3) => [4,6`
def bigger_than(xs, y):
	ret = []
	for x in xs:
		if x > y:
			ret.append(x)
	return ret

#fce, ktera vraci seznam ys, ve kterem jsou odstraneny vsechny duplikaty prvku z xs
def remove(xs):
	ret = []
	for x in xs:
		if not x in ret:
			ret.append(x)
	return ret

#fce, prvni argument seznam celych cisel xs a jako druhy jedno cele cislo. vraci seznam vsech pozic cisla v xs
def index (xs, y):
	ret = []
	i = 0
	for x in xs:
		if x == y:
			ret.append(i)
		i+= 1
	return ret

# zase xs a vraci ten prvek, ktery je jako prvni roven svemu nasledovnikovi, jinak none
def doubles(xs):
	i = 0
	for x in xs
		if i+1 < len(xs) and x == xs[i+1]:
			return x
		i = i + 1
	return None

# ted vraci seznam takovych prvku, ktere jsou rovny svym nasledovnikum
def doubles(xs):
	ret = []
	i = 0
	for x in xs:
		if i+1 < les(xs) and x == xs[i+1]:
			ret.append(x)
		i+= 1
	return(ret)


