numeros = ('Digite o 1º valor: ', 'Digite o 2º valor: ',
            'Digite o 3º valor: ', 'Digite o 4º valor: ')
print(f'Você digitou os valores: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if numeros == 3:
    print(f'O primeiro valor 3 está na {numeros.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
