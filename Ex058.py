from random import randint
computador = randint(0, 10)
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS!!!'.format(palpites))
