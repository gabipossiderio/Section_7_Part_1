numbers_list = []

print('Enter 10 different numbers. PLEASE do not repeat the numbers.\n')
for i in range(1, 11):
    entered_numbers = int(input(f'Number {i}/10: '))
    if entered_numbers in numbers_list:
        print(f'\nThe number entered in gap number {i} has already been entered. Please, try again!')
        break
    numbers_list.append(entered_numbers)

if len(numbers_list) == 10:
    print(f'\nThe numbers entered were: {numbers_list}.')
