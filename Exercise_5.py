lista = [0]
pares = 0

print("Informe 10 valores. Verificaremos quantos valores pares você informou.\n")
for i in range(1, 11):
    valores = (float(input(f'Valor {i}/10: ')))
    lista.append(valores)
    if valores % 2 == 0:
        pares += 1

print(f'\nVocê informou {pares} números pares.')
