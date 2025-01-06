#SEM USAR FUNÇÕES:
a = 2
b = 5
soma = a + b
print(soma)
a = 9
b = 6
soma = a + b
print(soma)

#USANDO FUNÇÕES:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma de A + B = {soma}')

soma(4, 1)
soma(7, 9)
soma(4) #Vai dar erro pois no 'def soma' foi definido dois valores para serem somados,
#não pode ter um parametro só.
soma(a=5, b=9) #Pode definir qual valor vai estar em casa parametro
soma(b=5, a=9)
soma(a=5, 9) #Não funcionar se for definido apenas um valor
soma(3, 9, 5) #Vai dar erro pois na definição só diz que vai receber dois valores



#EMPACOTAMENTO:
def contador(* num):
#O def não sabe exatamente a quantidade de números que vão entrar, com o * ele vai receber
#qualquer valor que esteja no contador, sem precisar ter uma quantidade de valores exata.
    print(num)

    for valor in num:
        print(f'{valor}', end='')
    print('FIM!')
    #Vai mostrar cada valor um por um sem fazer as separações por contador

    tamanho = len(num) #Vai contar quantos valores tem no total dentro de 'num'
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador(3, 5 ,9)
contador(0, 8)
contador(4, 8, 9, 1, 6, 5)
#Vai transformar em tuplas e mostrar na tela dentro de uma tupla.



#OUTRA FORMA DE FAZER SOMA
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(2, 1)
soma(2, 9, 4)



#LISTAS
#Lista são alteravéis então é melhor mexer com elas do que com tuplas.
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
#Vai dobrar todos os valores que foram declarados dentro da lista

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
