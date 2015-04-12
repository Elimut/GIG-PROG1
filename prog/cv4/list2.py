names = ["Bob", "Alice", "John"]
print(names[2])
print("----------")

names.append("Jan")
names.pop(1)

names2 = names.copy()
names.insert(0, "Jan")
del names [1:3]
print(names)
print(names2)

