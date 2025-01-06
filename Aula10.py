numero = [2, 5, 9, 1]

numero[2] = 3 #O valor que estava na posição 2 passa a valer 3
numero.append(7) #Vai adicionar o valor 7 na lista
numero.sort() #Vai colocar a lista em ordem
numero.sort(reverse=True) #Vai colocar a lista em ordem decrescente
numero.insert(2, 0) #Vai inserir na posição 2 o número 0
numero.pop() #Vai excluir o último valor da lista
numero.pop(2) #Vai excluir o valor que está na posição 2
numero.remove(2) #Vai remover o primeiro valor 2 da lista, APENAS O PRIMEIRO

if 4 in numero:
    numero.remove(4)
else:
    print('Não achei o número 4!')

print(numero)
print(f'Essa lista tem {len(numero)} elementos.') #LEN vai contar quantos elementos tem na lista




valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
    #Vai mostrar os valores que foram adicionados na lista

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
    #O enumerate vai mostrar também a posição dos valores dentro da lista
print('Cheguei ao final da lista!')




valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    #Vai adicionar na lista os 5 valores digitados pelo teclado
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
    #Vai mostrar o valor e a sua posição dentro da lista dos valores digitados pelo teclado




a = [2, 3, 4, 7]

b = a
#Se igualar uma lista a outra, o python cria uma ligação entre elas
#Se mudar o valor de uma lista, automaticamente mudará da outra

b = a[:]
#Assim, o B vai receber uma cópia da lista de A, e se alterar algum valor, não ira
#influenciar na lista A, pois está mexendo com uma cópia

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
