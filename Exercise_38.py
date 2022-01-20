import random

ascending_order_list = []

print('Please, enter 10 numbers.')

for i in range(10):
    ascending_order_list.append(int(input(f'Number {i + 1}/10: ')))
    ascending_order_list.sort()

print(ascending_order_list)
