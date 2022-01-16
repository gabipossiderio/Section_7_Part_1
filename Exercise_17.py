import random

numbers_list = []

for i in range(10):
    numbers_list.append(random.randrange(-100000, 100000))

print(f'Here is the list with 10 real numbers {numbers_list}.')

for numbers in range(10):
    if numbers_list[numbers] < 0:
        numbers_list[numbers] = 0

print(f'Here is the list with all negative numbers replaced by 0: {numbers_list}.')
