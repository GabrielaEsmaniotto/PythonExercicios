numero = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('=' * 30)
numero[0].sort()
numero[1].sort()
print(f'Lista de pares: {numero[0]}')
print(f'Lista de ímpares: {numero[1]}')
