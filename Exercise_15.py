import random

numbers_list = []

for i in range(20):
    generated_number = random.randrange(0, 40)
    numbers_list.append(generated_number)

print(f'We create a list with 20 whole numbers: {numbers_list}. \nHere is the list without repeated numbers: '
      f'{set(numbers_list)}.')
