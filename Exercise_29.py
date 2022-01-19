import random

numbers_list = []
even_numbers = []
odd_numbers = []

for i in range(6):
    generated_numbers = random.randrange(0, 20)
    numbers_list.append(generated_numbers)
    if numbers_list[i] % 2 != 0:
        odd_numbers.append(numbers_list[i])
    else:
        even_numbers.append(numbers_list[i])

print(f'Here is the list with 6 numbers: {numbers_list}. \nAmong these numbers we can find {len(even_numbers)} even '
      f'numbers: {even_numbers} and {len(odd_numbers)} odd numbers: {odd_numbers}.')
