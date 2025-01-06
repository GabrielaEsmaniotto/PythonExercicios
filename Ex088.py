from random import randint
from time import sleep
lista = []
jogos = []
print('=' * 30)
print('         MEGA SENA       ')
print('=' * 30)
quantidade = int(input('Quantos jogos você quer jogar? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(0, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
