from random import randint
from time import sleep  #Faz o computador esperar alguns segundos
computador = randint(0, 5) #Faz o computador "PENSAR", sortear um número.
print('=' * 53)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('=' * 53)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)  #Computador vai esperar 2 segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))
