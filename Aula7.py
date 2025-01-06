numero = 1
while numero < 11:
    print(numero)
    numero = numero + 1
print('Fim!')


numero = 1
while numero != 0:
    numero = int(input('Digite um valor: '))
print('Fim!')


resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('Fim!')


numero = 1
par = 0
impar = 0
while numero != 0:
    numero = int(input('Digite um número: '))
    if numero != 0:
        if numero % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Tem {} números pares e {} números ímpares.'.format(par, impar))
