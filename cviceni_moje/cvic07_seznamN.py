from random import *
from string import *

def generateData(N):

    dataset = []
    chars1 = ascii_letters
    chars2 = digits
    chars3 = chars2[1:len(chars2)]
    
    for x in range(N):
        row = []
        row.append(''.join(random.sample(chars1*9, 9)))
        row.append(random.randint(500,600))
        row.append(random.random()*5+50)
        row.append(''.join(random.sample(chars3, 1))
                   + "".join(random.sample(chars2*2, 2)))
        dataset.append(row)
        
    return(dataset)

x = generateData(5)
print(x)
