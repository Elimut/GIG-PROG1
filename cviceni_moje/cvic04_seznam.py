


def seznamR (L, S):
    seznam = []
    for retezec in L:
        if S in retezec:
            seznam.append(retezec)
    return(seznam)
seznam = ["ahoj", "bla", "blah", "blabla", "ahoj", "ahoj"]
retezec = "ahoj"
print(seznamR(seznam, retezec))
            
def seznam (S):
    suma = 0
    for i in S:
        suma += i
        prumer = suma/len(S)
    return(prumer)
seznam2 = [1,2,3]
print(seznam(seznam2))
