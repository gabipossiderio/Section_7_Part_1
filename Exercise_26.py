import random
import math

numbers_vector = []
quadratic_deviation = 0

for i in range(10):
    numbers_vector.append(random.randint(0, 100))

for i in range(10):
    quadratic_deviation += math.pow((numbers_vector[i] - sum(numbers_vector) / 10), 2)

standard_deviation = math.sqrt((1 / 9) * quadratic_deviation)

print(f'The standard deviation of vector {numbers_vector} is {standard_deviation}')
