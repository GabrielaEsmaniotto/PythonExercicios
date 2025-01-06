numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print('O número {} é o MAIOR e o número {} é o MENOR'.format(numero1, numero2))
elif numero2 > numero1:
    print('O numéro {} é o MAIOR e o número {} é o MENOR'.format(numero2, numero1))
else:
    print('Os dois números são iguais!')
