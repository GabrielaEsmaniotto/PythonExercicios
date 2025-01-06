def ficha(nome='<<Desconhecido>>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')

jogador = str(input('Qual o nome do jogador? '))
numeroGols = str(input('Número de gols: '))
if numeroGols.isnumeric():
    numerGols = int(numeroGols)
else:
    numeroGols = 0
if jogador.strip() == '':
    ficha(gols=numeroGols)
else:
    ficha(jogador, numeroGols)
