lista = [0]

print("Informe 8 valores. Criaremos uma lista para você.\n")
for i in range(1, 9):
    lista.append(float(input(f'Valor {i}/8: ')))

print('\nEscolha duas posições da lista criada para que os valores sejam somados.')
posicao1 = int(input('\nPosição 1 (entre 1 e 8): '))
posicao2 = int(input('Posição 2 (entre 1 e 8): '))

print(f'\nA soma dos dois valores nas posições escolhidas é: {(lista[posicao1] + lista[posicao2])}.')
