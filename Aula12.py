pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': '22'}
print(pessoas)
print(pessoas['Nome'])
print(pessoas['Idade'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
    #Para a informação funcionar dentro de um texto formatado precisa colocar em "" duplas.
print(pessoas.keys())
#Vai mostrar na tela apenas os índices
print(pessoas.values())
#Vai mostrar apenas os valores atribuídos
print(pessoas.items())
#Vai mostrar todos os índices com seus valores separadamente
for indice in pessoas.keys():
     print(indice)
for indice in pessoas.values():
    print(indice)

del pessoas['Sexo']
#Vai excluir o índice junto com o valor de 'Sexo'
pessoas['Nome'] = 'Leandro'
#Vai substituir o nome 'Gustavo' por 'Leandro'
pessoas['Peso'] = 98.5
#Vai adicionar um novo índice no dicionário
for indice, valor in pessoas.items():
    print(f'{indice}: {valor}')





brasil = []
estado1 = {'Cidade': 'Rio de Janeiro', 'Estado': 'RJ'}
estado2 = {'Cidade': 'São Paulo', 'Estado': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
#Vai colocar dois dicionários dentro de uma lista
print(brasil)
print(brasil[0])
#Vai mostrar o primeiro dicionário dentro da lista
print(brasil[0]['Cidade'])
#Vai mostrar a cidade do primeiro dicionário que é 'Rio de Janeiro'
print(f'A cidade {brasil[0]['Cidade']} fica no estado de {brasil[0]['Estado']}')
print(f'A cidade {brasil[1]['Cidade']} fica no estado de {brasil[1]['Estado']}')





estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    #Está fazendo uma cópia do dicionário para dentro da lista
for est in brasil:
    for indice, valor in est.items():
        print(f'O campo {indice} tem o valor {valor}.')
    for valor in est.values():
        print(valor, end=' ')
    print()
