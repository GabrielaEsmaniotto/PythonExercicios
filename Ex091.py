'''from random import randint
dicionario = {}
for c in range(1, 5):
    dados = randint(0, 7)
    print(f'{c}º Jogador: {dados}')
    dicionario[dados] = c
print(dicionario)
ordenado = sorted(dicionario.keys(),reverse=True)
maiorDado = ordenado[0]
print(dicionario[maiorDado])
print(f'O vencedor foi o {dicionario[maiorDado]}º jogador com {maiorDado} pontos.')'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
