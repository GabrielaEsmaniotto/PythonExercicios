distancia = float(input('Qual a distância da sua viagem em Km? '))
print('Você esta prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = (distancia * 0.50)
else:
    preco = (distancia * 0.45)
print('Sua passagem ficou no valor de R${:.2f}'.format(preco))
