lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[-3:])

#Tuplas são imutáveis

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')


print(len(lanche)) #Vai contar quantos elementos tem dentro de 'lanche'


for comida in range(0, len(lanche)): #0, len = vai começar da posição 0 até o final
    print(lanche[comida])
    print(f'Eu vou comer {lanche[comida]} na posição {comida}')


for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print(sorted(lanche)) #Vai organizar os elementos que estão na tupla


a = (1, 4, 3)
b = (2, 9, 7, 4)
c = a + b
print(a)
print(b)
print(c)
print(len(c))
print(c.count(5)) #Vai mostrar quantas vezes está aparecendo o número 5
print(c.index(9)) #Vai mostrar em qual posição está o 9
print(c.index(4, 2)) #Vai mostrar em qual posição está o próximo 4 a partir de posição 2



pessoa = ('Gabriela', 23, 'Feminino', 66.8)
del(pessoa) #Vai excluir a tupla 'pessoa'
