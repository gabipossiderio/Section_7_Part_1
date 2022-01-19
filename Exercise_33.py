from random import sample

numbers_list = sample(range(0, 40), 15)
print(f'Here is the list: {numbers_list}.')
numbers_list.pop(0)
print(f'Here is the list with its position number 0 taken out {numbers_list}.')
