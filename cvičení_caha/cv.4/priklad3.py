def prumer(listOfValues):
    suma = 0
    for x in listOfValues:
        suma += x
    prumer = suma / len(listOfValues)
    return(prumer)

a = [10,24,316,41,5133]
print(prumer(a))
