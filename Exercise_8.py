import random

lista = []

for i in range(6):
    lista.append(random.randrange(1, 100000))

print(f'Aqui está a lista gerada: {lista}.')
lista.reverse()
print(f'Aqui está a lista gerada em ordem inversa: {lista}.')
