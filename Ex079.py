numeros = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')
    escolha = str(input('Quer continuar? [S/N]'))
    if escolha in 'Nn':
        break
print('=' * 40)
numeros.sort()
print(f'Você digitou os valores {numeros}')
