import random

numbers_list = []
random_number = random.randrange(2, 10)
multiple_number_list = []

for i in range(10):
    generated_number = random.randrange(1, 40)
    numbers_list.append(generated_number)
    if generated_number % random_number == 0:
        multiple_number_list.append(generated_number)

if len(multiple_number_list) > 0:
    print(f'Here is the list with 10 real numbers {numbers_list} and we have {len(multiple_number_list)} multiple '
          f'numbers of {random_number}: {multiple_number_list}. ')
else:
    print(f'Here is the list with 10 real numbers {numbers_list} and there are no multiples of {random_number} '
          f'in that list.')
