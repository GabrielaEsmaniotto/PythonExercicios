from datetime import date
dado = {}
dado['Nome'] = str(input('Nome: '))
dado['Idade'] = int(input('Ano de nascimento: '))
dado['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

idade = dado['Idade']
anoatual = date.today().year
idadehoje = anoatual - idade
dado['Idade'] = idadehoje

print(dado)
print(f'O nome é: {dado['Nome']}')
print(f'Tem {dado['Idade']} anos')
print(f'Número da CTPS: {dado['CTPS']}')

if dado['CTPS'] != 0:
    dado['Contratação'] = int(input('Ano de Contratação: '))
    dado['Salário'] = float(input('Salário: '))
    inicio = dado['Contratação']
    dado['Aposentadoria'] = inicio + 35

    print(f'Contratado no ano de {dado['Contratação']}')
    print(f'Com salário de: R${dado['Salário']:.3f}')
    print(f'Irá se aposentar em: {dado['Aposentadoria']}')
else:
    print('Finalizando...')
