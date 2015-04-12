# Napište funkci, která jako vstup přijímá dvě proměnné.
# Předpokládejte, že vstupy jsou seznamy. Porovnejte jejich délku (funkce len(listName)), pokud obsahují stejný počet prvků funkce vrací hodnotu true, jinak vrací hodnotu false.
def compareLists(firstList, secondList):
    sameLength = False

    if len(firstList) == len(secondList):
        sameLength = True

    return(sameLength)


    
a = [1, 3, 5, 7]
b = [1, 8, 9, 12]

sameLength = compareLists(a,b)
print(sameLength)


############################
# Napište funkci, která jako argument přímá počet prvků v seznamu - n.
# Funkce od uživatele bude požadovat n vstupů, ze kterých vytvoří seznam, který bude funkce vracet.

def listDefinition(number):
    listOfValues = []
    for i in range(number):
        listOfValues.append(float(input("Zadej číslo: ")))
    return(listOfValues)


number = int(input("Zadej počet prvků v seznamu: "))
listOfValues = listDefinition(number)
print(listOfValues)


############################
# Napište funkci, která jako argument přijímá seznam hodnot. Předpokládejte, že seznam obsahuje pouze čísla. Funkce vrací jako výsledek průměr z čísel v seznamu.

def prumer(listOfValues):
    suma = 0
    for x in listOfValues:
        suma += x
    prumer = suma / len(listOfValues)
    return(prumer)

a = [10,24,316,41,5133]
print(prumer(a))

############################
# Napište funkci, která ze vstupního řetězce vrátí znaky v rozmezí 5 - 9 znaku.
# Pokud je řetězec kratší než 9 znaků, vypište hlášku, že operaci nelze provést.
def znaky(retezec):
    if len(retezec) < 9:
        print("Operaci nelze provést")
    else:
        podretezec = retezec[4:9] 
        return(podretezec)

string = "01234567"
print(znaky(string))

############################
# Napište funkci, která jako argument přijímá řetězec.
# Upravte vstupní řetězec tak, aby obsahoval pouze malá písmena.
# Následně nahraďte všechny české znaky (s háčky, čárkami a kroužky) v řetězci za jejich ekvivalenty bez těchto znaků.
# Takto upravený řetězec bude návratovou hodnotou funkce. 
def odstranZnaky(retezec):
    retezec = retezec.lower()
    ceskeZnaky = ["ě", "š", "č", "ř", "ž", "ý", "á", "í", "é", "ú", "ů", "ť", "ď", "ó", "ň"]
    asciiZnaky = ["e", "s", "c", "r", "z", "y", "a", "i", "e", "u", "u", "t", "d", "o", "n"]

    for i in range(len(ceskeZnaky)):
        retezec = retezec.replace(ceskeZnaky[i],asciiZnaky[i])

    return(retezec)    


testovaciRetezec = "Příšerně žluťoučký kůň úpěl ďábelské ódy."
print(testovaciRetezec)
vyslek = odstranZnaky(testovaciRetezec)
print(vyslek)





















