import random

numbers_list = []
chosen_code = 1000

for i in range(5):
    generated_number = random.randrange(-100000, 100000)
    numbers_list.append(generated_number)

while chosen_code != 0:
    chosen_code = int(input('\nENTER A CODE\n'
                            '\n0 - End the program\n'
                            '1 - Vector in direct order\n'
                            '2 - Vector in reverse order:\n'))
    match chosen_code:
        case 0:
            print('\nFinalized program! Thanks.')
        case 1:
            print(f'\nHere is the list with 5 real numbers {numbers_list}.')
        case 2:
            numbers_list.reverse()
            print(f'\nHere is the list with 5 real numbers in the reverse form {numbers_list}.')
        case _:
            print('\nInvalid code. Please, try again.')


