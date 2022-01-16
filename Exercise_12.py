import random

numbers_list = []

for i in range(5):
    generate_numbers = (random.randrange(0, 100000))
    numbers_list.append(generate_numbers)

print(f'Here is the list generated with five numbers:  {numbers_list}. \nThe highest number on this list is '
      f'{(max(numbers_list))} and the smallest number in this list is {(min(numbers_list))}. The average of the '
      f'generated numbers is {(sum(numbers_list))/5}.')
