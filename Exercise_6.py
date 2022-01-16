lista = [0]

print("Informe 10 valores. Criaremos uma lista para você.\n")
for i in range(1, 11):
    lista.append(int(input(f'Valor {i}/10: ')))

print(f'\nO maior número digitado foi {max(lista)} e o menor foi {min(lista)}.')
