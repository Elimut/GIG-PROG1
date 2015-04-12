for i in range(3,100,2):
    for j in range (3,i):
        if i % j == 0:
            break
    if i == j:
        print(i)
    
