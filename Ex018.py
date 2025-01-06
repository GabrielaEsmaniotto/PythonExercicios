import math
numero = float(input('Qual o valor do ângulo: '))
seno = math.sin(math.radians(numero))
cosseno = math.cos(math.radians(numero))
tangente = math.tan(math.radians(numero))
print('O ângulo é {}'.format(numero))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))
