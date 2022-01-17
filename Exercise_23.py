import random

vector_1 = []
vector_2 = []
dot_product = 0

for i in range(5):
    vector_1.append(random.randint(0, 100))
    vector_2.append(random.randint(0, 100))
    dot_product += vector_1[i] * vector_2[i]

print(f'The first vector is: {vector_1}\n'
      f'The second vector is: {vector_2}\n'
      f'The dot product of the two vectors is: {dot_product}')
