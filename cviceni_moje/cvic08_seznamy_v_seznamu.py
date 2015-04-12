A = [["a",1],["b",2],["c",3]]
B = [[2,"text2"],[3,"text3"],[1,"text1"],[4,"text4"]]

C = []

for x in range(0,len(A)):
    radek = []
    radek.append(A[x][0])
    radek.append(A[x][1])

    for y in range(0,len(B)):
        if B[y][0] == A[x][1]:
            radek.append(B[y][1])
    C.append(radek)

print(C) 
