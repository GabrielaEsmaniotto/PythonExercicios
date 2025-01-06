numero = []
pares = []
impares = []
while True:
    numero.append(int(input('Digite um valor: ')))
    escolha = str(input('Deseja continuar? [S/N]'))
    if escolha in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * 40)
print(f'A lista completa é {numero}')
print(f'A lista com pares é {pares}')
print(f'A lista com ímpares é {impares}')
