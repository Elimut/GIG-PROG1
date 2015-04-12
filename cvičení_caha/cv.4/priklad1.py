def compareLists(firstList, secondList):
    sameLength = False

    if len(firstList) == len(secondList):
        sameLength = True

    return(sameLength)


    
a = [1, 3, 5, 7]
b = [1, 8, 9, 12]

sameLength = compareLists(a,b)
print(sameLength)

