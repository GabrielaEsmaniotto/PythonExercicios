import math
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print('A raiz de {} é igual a {:.2f}'.format(numero, raiz))

#OU

from math import sqrt
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {:.2f}'.format(numero, raiz))

#Gerar números aleatórios

import random
numero = random.randint(1, 10)
print(numero)

###

import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
