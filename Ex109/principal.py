import modulo

valor = float(input(f'Digite o valor R$'))
print(f'{modulo.moeda(valor)} com 10% de juros fica: {modulo.aumentar(valor, 10, True)}')
print(f'{modulo.moeda(valor)} com 5% de desconto fica: {modulo.diminuir(valor, 5, True)}')
print(f'Dobro de {modulo.moeda(valor)}: {modulo.dobro(valor, True)}')
print(f'Metade de {modulo.moeda(valor)}: {modulo.metade(valor, True)}')
