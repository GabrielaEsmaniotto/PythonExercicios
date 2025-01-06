contador = 0
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
while contador < 10:
    pa = termo + (razao * contador)
    print('{} - '.format(pa), end='')
    contador = contador + 1
print('FIM')
