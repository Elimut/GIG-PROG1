def listDefinition(number):
    listOfValues = []
    for i in range(number):
        listOfValues.append(float(input("Zadej číslo: ")))
    return(listOfValues)


number = int(input("Zadej počet prvků v seznamu: "))
listOfValues = listDefinition(number)
print(listOfValues)
