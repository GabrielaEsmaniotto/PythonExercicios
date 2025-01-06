def area(largura, comprimento):
    soma = largura * comprimento
    print(f'A área total do terreno é de {largura}x{comprimento} = {soma:.2f}m².')


print(' CONTROLE DE TERRENOS')
print('=' * 22)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
