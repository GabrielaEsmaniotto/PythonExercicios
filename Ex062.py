contador = 0
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        pa = termo + (razao * contador)
        print('{} - '.format(pa), end='')
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizado com {} termos mostrados'.format(total))
