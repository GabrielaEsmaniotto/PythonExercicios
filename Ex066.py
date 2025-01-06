soma = quantidade = 0
print('Digite 999 para finalizar.')
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    quantidade = quantidade + 1
    soma = soma + numero
print(f'A soma dos {quantidade} valores digitados é {soma}!')
