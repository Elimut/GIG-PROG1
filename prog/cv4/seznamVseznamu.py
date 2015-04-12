row1 = [1, 2, 3, 4]
row2 = [12, 15]
row3 = [156, 184, 199, 252]

rows = (row1, row2, row3)

for row in rows:
    for number in row:
        print(number, end=" ")
    print()
