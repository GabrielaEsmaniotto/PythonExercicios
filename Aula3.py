nome = str(input('Digite seu nome: '))
if nome == 'Marlon':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))



n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi de: {:.1f}'.format(media))
if media >= 6.0:
    print('Sua média foi boa, PARABÉNS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')
