temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('=' * 30)
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for peso in principal:
    if peso[1] == maior:
        print(f'[{peso[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for peso in principal:
    if peso[1] == menor:
        print(f'[{peso[0]}] ', end='')
print()
