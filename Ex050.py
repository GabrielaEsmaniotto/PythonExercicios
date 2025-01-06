soma = 0
for contador in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma de todos os números pares são: {}'.format(soma))
