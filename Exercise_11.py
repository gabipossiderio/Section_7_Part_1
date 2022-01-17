import random

real_numbers = []
negative_numbers = 0
positive_numbers_sum = 0

for i in range(10):
    generate_number = random.randrange(-100000, 100000)
    real_numbers.append(generate_number)
    if generate_number < 0:
        negative_numbers += 1
    else:
        positive_numbers_sum += generate_number


print(f'Here is the list just generated with real numbers:  {real_numbers}.')
print(f'The list has {negative_numbers} negative numbers and the sum of all positive numbers in the list is '
      f'{positive_numbers_sum}.')
