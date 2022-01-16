import random

lista = []
lista2 = []
pares = 0

for i in range(10):
    valores = random.randrange(1, 100000)
    lista.append(valores)
    if valores % 2 == 0:
        lista2.append(valores)
        pares += 1

print(f'\nGeramos uma lista de 10 números. São eles {lista}. \nDentro dessa lista, foram encontrados {pares} números '
      f'pares. São eles: {lista2}.')
