import random

list1 = []

for i in range(6):
    list1.append(random.randrange(0, 100000, 2))

print(f'Here is the list just generated with even numbers: {list1}.')
list1.reverse()
print(f'Here is the list generated in reverse order: {list1}.')
