import modulo

valor = float(input(f'Digite o valor R$'))
print(f'{modulo.moeda(valor)} com 10% de juros fica: {modulo.moeda(modulo.aumentar(valor, 10))}')
print(f'{modulo.moeda(valor)} com 5% de desconto fica: {modulo.moeda(modulo.diminuir(valor, 5))}')
print(f'Dobro de {modulo.moeda(valor)}: {modulo.moeda(modulo.dobro(valor))}')
print(f'Metade de {modulo.moeda(valor)}: {modulo.moeda(modulo.metade(valor))}')
