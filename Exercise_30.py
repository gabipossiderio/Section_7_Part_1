import random

numbers_list = []
numbers_list2 = []

for i in range(10):
    numbers_list.append(random.randrange(0, 20))
    numbers_list2.append(random.randrange(0, 20))

print(f'\nNumbers of the first vector: {numbers_list}')
print(f'Numbers of the second vector: {numbers_list2}')

numbers_set1 = set(numbers_list)
numbers_set2 = set(numbers_list2)

both = numbers_set1.intersection(numbers_set2)

print(f'The intersection of the two vectors: {both}.')
