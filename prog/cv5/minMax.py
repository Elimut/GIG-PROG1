def minMax(a, b):
    sortedValues = []
    if a<b:
        sortedValues.append(a)
        sortedValues.append(b)
    else:
        sortedValues.append(b)
        sortedValues.append(a)
    return(sortedValues)

values = minMax(5, 10)
print(values)
values = minMax(8, 2)
print(values)

