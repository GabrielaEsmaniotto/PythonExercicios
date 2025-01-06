from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções...
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if jogador > 2:
    print('JOGADA INVÁLIDA!')
else:
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')
    if computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        else:
            print('JOGADOR VENCE')
    if computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        else:
            print('EMPATE')
