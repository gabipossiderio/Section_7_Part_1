lista = []
lista2 = []
print("Informe 10 valores.\n")
for i in range(1, 11):
    valores = float(input(f'Valor {i}/10: '))
    lista.append(valores)
    lista2.append(valores ** 2)

print(f'\nOs valores da lista 1 são: {lista}.')
print(f'Os valores da lista 1 elevados ao quadrado são: {lista2}.')
