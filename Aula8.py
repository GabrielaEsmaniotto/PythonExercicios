numero = 0
soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma = soma + numero
print('A soma dos valores é {}'.format(soma))
print(f'A soma dos valores é {soma}') #Atualização Python


nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')
