numero = int(input('Digite um número para ver sua tabuada: '))
for contador in range(1, 11):
    print('{} x {:2} = {}'.format(numero, contador, numero*contador))
