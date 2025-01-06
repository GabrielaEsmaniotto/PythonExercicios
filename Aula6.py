for contador in range(0, 6):
    print('Oi')
print('FIM')


for contador in range(1, 7):  #Vai mostrar todos os números de 1 a 7
    print(contador)
print('FIM')


for contador in range(7, 0, -1):  #Vai mostrar todos os números de 7 a 1 ao contrario
    print(contador)
print('FIM')


for contador in range(0, 12, 2):  #Vai mostrar todos os números de 0 a 12, pulando de 2 em 2
    print(contador)
print('FIM')


numero = int(input('Digite um número: '))
for contador in range(0, numero+1):  #+1 vai adicionar o valor que seria excluído do último número
    print(contador)
print('FIM')


inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for contador in range(inicio, fim+1, passo):
    print(contador)
print('FIM')


soma = 0
for contador in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma = soma + numero
print('A soma dos valor é igual a: {}'.format(soma))
print('FIM')
