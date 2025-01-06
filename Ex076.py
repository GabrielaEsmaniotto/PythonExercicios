listagem = ('Mouse', 170.50,
            'Teclado', 450.00,
            'MousePad', 99.99,
            'Fone', 450.95,
            'Cadeira', 800.59)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
