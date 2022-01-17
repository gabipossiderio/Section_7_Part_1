import random

numbers_list1 = []
numbers_list2 = []
numbers_list3 = []

for i in range(10):
    numbers_list1.append(random.randrange(-100000, 100000))
    numbers_list2.append(random.randrange(-100000, 100000))
    numbers_list3.append(numbers_list1[i])
    numbers_list3.append(numbers_list2[i])

print(numbers_list1)
print(numbers_list2)
print(numbers_list3)
