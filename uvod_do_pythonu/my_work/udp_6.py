""" seznam jako zásobník a jako fronta """

##### zásobník #####
# LIFO = poslední přidaný prvek je i první vrácený
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop() #odebere 7
stack.pop() #odebere 6
stack.pop() #odebere 5
print(stack)

##### fronta #####
# FIFO = první přidaný prvek je i první vrácený
queue = ["Bender", "Leela", "Fry", "Zoidberg"]
queue.append("Scruffy")
queue.append("Amy")
print(queue.pop(0)) #odebere Bendera
print(queue)

