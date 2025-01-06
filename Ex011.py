largura = float(input('Qual a largura? '))
altura = float(input('Qual a altura? '))
area = largura * altura
tinta = area / 2
print('Sua parede tem {}x{} e sua área total é de {}'.format(largura, altura, area))
print('Para pintar essa parede você vai precisar de {} litros de tinta'.format(tinta))
