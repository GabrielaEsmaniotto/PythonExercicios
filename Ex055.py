maiorPeso = 0
menorPeso = 0
for contador in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(contador)))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso or menorPeso == 0:
        menorPeso = peso
print('O maior peso é {}'.format(maiorPeso))
print('O menor peso é {}'.format(menorPeso))
