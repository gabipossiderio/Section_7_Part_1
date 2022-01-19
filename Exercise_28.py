import random

v = []
v1 = []
v2 = []

for i in range(10):
    generated_numbers = random.randrange(0,100000)
    v.append(generated_numbers)
    if v[i] % 2 != 0:
        v2.append(v[i])
    else:
        v1.append(v[i])

print(f'Here is the list with 10 numbers: {v}. \nHere is the list with only the odd numbers from the previous list: {v1}'
      f'\nHere is the list with just the even numbers from the previous list: {v2}. \nThe list of odd numbers had '
      f'{len(v1)} elements used and the list of even numbers had {len(v2)} elements used.')
