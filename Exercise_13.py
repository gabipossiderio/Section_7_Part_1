import random

numbers_list = []

for i in range(5):
    generate_numbers = (random.randrange(0, 100000))
    numbers_list.append(generate_numbers)

print(f'Here is the list generated with five numbers:  {numbers_list}. \nThe highest number on this list is in the'
      f'position {(numbers_list.index(max(numbers_list)) + 1)} and the smallest number in this list is in the position '
      f'{(numbers_list.index(min(numbers_list)) + 1)}.')
