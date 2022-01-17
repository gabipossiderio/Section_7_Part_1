numbers_list1 = []
numbers_list2 = []
numbers_list3 = []

print('Enter 10 numbers for the first list.\n')
for i in range(1, 11):
    numbers_list1.append(int(input(f'Number {i}/10: ')))

print('Enter 10 numbers for the second list.\n')
for i in range(1, 11):
    numbers_list2.append(int(input(f'Number {i}/10: ')))

for i in range(10):
    numbers_list3.append(numbers_list1[i] - numbers_list2[i])

print(f'\nHere is the third list with all the numbers of the first list subtracted by the numbers in the second list: '
      f'{numbers_list3}.')
