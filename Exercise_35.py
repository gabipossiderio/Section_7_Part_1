import random

numbers_list1 = []
numbers_list2 = []
amount_list = []
larger_list = []
remainder = 0
amount = 0

number1 = str(random.randint(0, 10000))
number2 = str(random.randint(0, 10000))

for i in number1[::-1]:
    numbers_list1.append(int(i))

for i in number2[::-1]:
    numbers_list2.append(int(i))

# Checks the size of both lists and declares which is larger and which is smaller
if len(numbers_list1) >= len(numbers_list2):
    larger_list = numbers_list1
    smaller_list = numbers_list2
else:
    larger_list = numbers_list2
    smaller_list = numbers_list1

for i in range(len(larger_list)):
    # Access smaller list item only if it exists
    if i < len(smaller_list):
        amount = larger_list[i] + smaller_list[i] + remainder
        if amount >= 10:
            amount = amount - 10
            remainder = 1
        else:
            remainder = 0
    else:
        amount = (larger_list[i])
    amount_list.append(amount)

if remainder == 1:
    amount_list.append(remainder)

print(f'The numbers are {number1} and {number2}.')
print(f'The first list is {numbers_list1} and the second list is {numbers_list2}.')
print(f'The sum of the two lists is {amount_list}.')
