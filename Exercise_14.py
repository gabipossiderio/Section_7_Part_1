import random

numbers_list = []
repeated_number = []

for i in range(10):
    generate_number = random.randrange(0, 40)
    numbers_list.append(generate_number)

for x in numbers_list:
    if numbers_list.count(x) > 1:
        repeated_number.append(x)


if len(repeated_number) >= 1:
    print(f'We generate a list of 10 numbers: {numbers_list} and in this list we can observe '
          f'{len(set(repeated_number))} repeated numbers: {set(repeated_number)}.')

else:
    print(f'We generate a list of 10 numbers: {numbers_list} and there are no repeated numbers in this list.')
