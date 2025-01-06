ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    escolha = str(input('Deseja continuar? [S/N] '))
    if escolha in 'Nn':
        break
print('=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('=' * 35)
    operação = (int(input('Mostrar notas de qual aluno? (999 interrompe): ')))
    if operação == 999:
        print('FINALIZANDO...')
        break
    if operação <= len(ficha) -1:
        print(f'Notas de {ficha[operação][0]} são {ficha[operação][1]}')
print('<<< VOLTE SEMPRE! >>>')
