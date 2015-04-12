from random import *
from string import *

"z intervalu 0-1000 000 vygeneruje 10 000 náhodných čísel"
for i in range (0, 10000):
    string = str(randint(0, 1000000)) + "\n"
    #print(string)

#print(random()*1000)

"10 000 dvojic náhodných čísel z intervalu 0,1000"
delimiter = " - "
for i in range(10000):
    value1 = random()*1000
    value2 = random()*1000
    string = str(value1) + delimiter + str(value2) + "\n"
    #print(string)

"vygenerujte 1000 řetězců oddělených středníkem o délce 9 znaků, které obsahují náhodnou kombinaci velkých písmen a číslic. znaky se mohou opakovat"
char_set = ascii_uppercase + digits
for i in range (1000):
    stringRandom = ''.join(sample(char_set * 9,9))
    string = stringRandom + ";"
    #print(string)
