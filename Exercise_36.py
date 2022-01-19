import random

numbers_list = [random.randrange(0, 10000) for i in range(10)]

print(f'Here is the list: {numbers_list}.')

numbers_list.sort()

print(f'Here is the list in ascending order: {numbers_list}.')
