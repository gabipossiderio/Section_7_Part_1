import random

numbers_list = []
numbers_list2 = []

for i in range(10):
    numbers_list.append(random.randrange(0, 20))
    numbers_list2.append(random.randrange(0, 20))

numbers_set1 = set(numbers_list)
numbers_set2 = set(numbers_list2)

both = numbers_set1.union(numbers_set2)

print(f'Here is the first list with 10 numbers: {numbers_list}. \nHere is the second list with 10 numbers: '
      f'{numbers_list2}. \nHere is the set with the union of the two lists: {both}.')
