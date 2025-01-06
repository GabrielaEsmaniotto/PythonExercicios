import random
n1 = str(input('Digite o nome do Aluno 01: '))
n2 = str(input('Digite o nome do Aluno 02: '))
n3 = str(input('Digite o nome do Aluno 03: '))
n4 = str(input('Digite o nome do Aluno 04: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
