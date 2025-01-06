'''from random import randint
numero = acerto = soma = par = impar = escolha = 0
computador = randint(0, 100)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    numero = int(input('Digite um número: '))
    escolha = int(input('PAR ou ÍMPAR? [1]PAR [2]ÍMPAR'))
    soma = computador + numero
    print(f'Você jogou {numero} e o computador {computador}. Somando: {soma}.')

    if escolha == 1 and soma % 2 == 1 or escolha == 2 and soma % 2 == 0:
        print(f'GAME OVER! Você venceu {acerto} vezes')
        break
    if escolha == 1 and soma % 2 == 0 or escolha == 2 and soma % 2 == 1:
        print('Você venceu!')
    acerto = acerto + 1
print('Saindo...')'''



from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes')
