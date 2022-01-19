list_numbers = []
count = 0

while len(list_numbers) != 100:
    count_list = list(str(count))
    if count % 7 != 0 or count_list[len(count_list) - 1] == '7':
        list_numbers.append(count)

    count += 1

print(f'Here is the list with the first 100 natural numbers that are not multiples of 7 or that end in 7:'
      f'\n{list_numbers}.')
