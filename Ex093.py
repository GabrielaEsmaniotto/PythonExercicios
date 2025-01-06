lista = []
dados = {}
dados['Nome'] = str(input('Qual seu nome? '))
dados['Partidas'] = int(input('Quantas partidas você jogou? '))
quantidade = 0

for c in range(dados['Partidas']):
    gols = int(input(f'Quantos gols na {c+1} partida: '))
    lista.append(gols)
    quantidade += gols

dados['Total'] = quantidade
dados['Gols'] = lista

print('=' * 40)
print(dados)
print(f'Nome: {dados['Nome']}')
print(f'Gols em cada partida: {dados['Gols']}')
print(f'Total de gols: {dados['Total']}')
print('=' * 40)

print(f'O jogador {dados['Nome']} jogou {dados['Partidas']} partidas')
for c in range(len(dados['Gols'])):
    print(f'Na partida {c+1}, fez {dados['Gols'][c]} gols.')
