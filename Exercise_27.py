import random

list_numbers = []
index_prime_numbers = []
prime_number_checker = 0

for i in range(10):
    generated_number = random.randint(0, 20)
    list_numbers.append(generated_number)

    for j in range(3, generated_number, 2):
        if generated_number % j == 0 or generated_number % 2 == 0:
            prime_number_checker += 1
            break

    if prime_number_checker == 0 and generated_number != 1 and generated_number != 0 or generated_number == 2:
        index_prime_numbers.append(i)

    prime_number_checker = 0

print(f'The generated vector is:: {list_numbers}\n'
      f'The positions of the vector that have prime numbers are: {index_prime_numbers}')
