loop = 'continua'
soma = 0
tentativa = 0
maior = 0
menor = 0
media = 0
while loop == 'continua':
    numero = int(input('Digite um número: '))
    escolha = str(input('Deseja continuar? [SIM/NÃO] ')).upper()
    if escolha == 'SIM':
        loop = 'continua'
    if escolha == 'NÃO':
        tentativa = tentativa + 1
        soma = soma + numero
        loop = 'para'
    if numero > maior:
        maior = numero
    if numero < menor or menor == 0:
        menor = numero
media = soma / tentativa
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))
print('A média dos valores foi de {}'.format(media))
