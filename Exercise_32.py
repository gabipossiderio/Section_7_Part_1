from random import sample

list_numbers1 = sample(range(0, 15), 5)
list_numbers2 = sample(range(0, 15), 5)
sum_list = []
multiplication_list = []

print(f'\nThe first list with 5 unique numbers informed: \n{list_numbers1}.')
print(f'The second list with 5 unique numbers informed: \n{list_numbers2}.')

for i in range(5):
    sum_list.append((list_numbers1[i]) + (list_numbers2[i]))
    multiplication_list.append((list_numbers1[i]) * (list_numbers2[i]))

print(f'''Here is the list with the SUM of the numbers in the first list with the numbers in the second list:
{sum_list}.
Here is the list with the MULTIPLICATION of the numbers in the first list with the numbers in the second list: 
{multiplication_list}.
Here is the list with the DIFFERENCE (all numbers in list 1 that are not in list 2): 
{set(list_numbers1).difference(set(list_numbers2))}. 
Here is the list with the UNION of the two lists: 
{set(list_numbers1).union(set(list_numbers2))}.
Here is the list with the INTERSECTION (only the numbers that appear in the two lists: 
{set(list_numbers1).intersection(set(list_numbers2))}.''')
