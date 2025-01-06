while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    if numero <= 0:
        break
    for contador in range(1, 11):
        print(f'{numero} x {contador:2} = {numero*contador}')
print('Saindo...')
