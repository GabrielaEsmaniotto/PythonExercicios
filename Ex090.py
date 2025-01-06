valor = {}
valor['Nome'] = str(input('Nome: '))
valor['Média'] = float(input(f'Média de {valor['Nome']}: '))

if valor['Média'] >= 7:
    valor['Situação'] = 'Aprovado'
elif 5 <= valor['Média'] < 7:
    valor['Situação'] = 'Recuperação'
else:
    valor['Situação'] = 'Reprovado'

print(valor)
print(f'Nome é igual a {valor['Nome']}')
print(f'Média é igual a {valor['Média']}')
print(f'A Situação é igual a {valor['Situação']}')
#OU
for k, v in valor.items():
    print(f' - {k} é igual a {v}')
