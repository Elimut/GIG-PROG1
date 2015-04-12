def prumer(listOfValues):
    suma = 0
    for x in listOfValues:
        suma += x
    prumer = suma / len(listOfValues)
    return(prumer)

a = [2,4,5,8,10]
print(prumer(a))
