import math

def funkce (x, y, z):
    vysledek = (2*x)-math.sin(y)+math.tan(z)+((4/x)**y)
    return(vysledek)

print(funkce(4,8,2))
