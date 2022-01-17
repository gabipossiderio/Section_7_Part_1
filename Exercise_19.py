numbers_list = []

for i in range(51):
    numbers_list.append((i + 5 * i) % (i + 1))

print(numbers_list)
