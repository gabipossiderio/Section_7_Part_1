import random

numbers_list = []
odd_numbers = []

for i in range(10):
    generated_numbers = random.randrange(0, 50)
    numbers_list.append(generated_numbers)
    if generated_numbers % 2 != 0:
        odd_numbers.append(generated_numbers)

print(f'Here is the list with 10 numbers {numbers_list}.')
print(f'Here is the list with only odd numbers {odd_numbers}.')
