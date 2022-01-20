import random

ascending_order = []
descending_order = []

for i in range(6):
    ascending_order.append(random.randrange(0, 100))
    ascending_order.sort()

for i in range(5):
    descending_order.append(random.randrange(0, 100))
    descending_order.sort(reverse=True)


print(ascending_order + descending_order)

