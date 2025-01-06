catetoOposto = float(input('Digite o valor do Cateto Oposto: '))
catetoAdjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusaAoQuadrado = (catetoOposto ** 2) + (catetoAdjacente ** 2)
hipotenusa = hipotenusaAoQuadrado ** (1/2)
print('O comprimento da Hipotenusa é {:.2f}'.format(hipotenusa))

#OU

from math import hypot
catetoOposto = float(input('Digite o valor do Cateto Oposto: '))
catetoAdjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('O comprimento da Hipotenusa é {:.2f}'.format(hipotenusa))
