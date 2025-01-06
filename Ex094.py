'''dicionario = {}
lista = []
listaMulheres = []
idadeAcima = []
quantidade = media = idade = 0

while True:
    dicionario['Nome'] = str(input('Nome: '))
    dicionario['Sexo'] = str(input('Sexo: [M/F]'))
    dicionario['Idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())

    quantidade += 1
    idade += dicionario['Idade']

    if dicionario['Sexo'] in 'Ff':
        listaMulheres.append(dicionario.copy()['Nome'])

    media = (media + idade) / quantidade
    if dicionario['Idade'] > media:
        idadeAcima.append(dicionario.copy()['Nome'])

    escolha = str(input('Quer continuar? [S/N]'))
    if escolha in 'Nn':
        break

print(lista)
print(f'Quantidade de pessoas cadastradas: {quantidade}')
print(f'A média de idade do grupo é igual a: {media:.2f}')
print(f'As mulheres cadastradas são: {listaMulheres}')
print(f'Nome das pessoas com idade acima da média: {idadeAcima}')'''

#OU

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p['Nome']} ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(' << ENCERRANDO >>')
