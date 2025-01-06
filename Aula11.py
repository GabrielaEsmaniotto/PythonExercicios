teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
#Existem duas listas até o momento
galera.append(teste[:]) #Vai colocar uma lista dentro da outra
teste[0] = 'Maria'
teste[1] = 22
#A partir do momento que a gente modifica uma lista, ela tem uma conexão com a outra lista,
#sendo assim, as duas serão motificadas, a menos que tenha sido motificado uma cópia.
galera.append(teste[:]) #[:] isso vai criar uma cópia
print(galera) #Vai imprimir duas vezes o valor modificado da segunda lista





galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) #Vai imprimir: João
print(galera[1][0]) #Vai imprimir: Ana
print(galera[2][1]) #Vai imprimir: 13

for pessoa in galera:
    print(pessoa[0]) #Vai imprimir so os nomes de cada um
    print(f'Nome: {pessoa[0]}')
    print(f'Idade: {pessoa[1]}')
    print(f'{pessoa[0]} tem {pessoa[1]} anos')






galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #Vai limpar as informações após a lista GALERA pegar uma cópia
#Temos duas listas, as informações estão sendo incluidas na lista 'DADO', a lista 'GALERA'
#vai pegar uma cópia e mostrar na tela.
print(galera)

for pessoas in galera:
    if pessoas[1] >= 21:
        print(f'{pessoas[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{pessoas[0]} é menor de idade!')
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade')
