'''import uteis

numero = int(input('Digite um valor: '))
fatorial = uteis.fatorial(numero)
print(f'O fatorial de {numero} é {fatorial}')
print(f'O dobro de {numero} é {uteis.dobro(numero)}')
print(f'O triplo de {numero} é {uteis.triplo(numero)}')'''


from pacotes import numeros
numero = int(input('Digite um valor: '))
fatorial = numeros.fatorial(numero)
print(f'O fatorial de {numero} é {fatorial}')
print(f'O dobro de {numero} é {numeros.dobro(numero)}')
print(f'O triplo de {numero} é {numeros.triplo(numero)}')
