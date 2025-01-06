valores = []
while True:
    valores.append(int(input(f'Digite um valor: ')))
    escolha = str(input('Deseja continuar? [S/N]'))
    if escolha in 'Nn':
        print(f'Valores digitados: {valores}')
        break
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente: {valores}')
if 5 in valores:
    print('O número 5 foi digitado e está na lista!')
else:
    print('O número 5 nõa foi encontrado na lista!')
