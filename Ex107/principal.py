import modulo

valor = float(input('Digite o valor R$'))
print(f'R${valor} com 10% de juros fica: R${modulo.aumentar(valor, 10)}')
print(f'R${valor} com 5% de desconto fica: R${modulo.diminuir(valor, 5)}')
print(f'Dobro de R${valor}: R${modulo.dobro(valor)}')
print(f'Metade de R${valor}: R${modulo.metade(valor)}')
