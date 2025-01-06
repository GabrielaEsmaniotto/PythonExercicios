km = float(input('Qual a quantidade de Km percorridos? '))
dias = int(input('Quantos dias de aluguel? '))
preço = (dias * 60) + (km * 0.15)
print('O preço a pagar é de: {}'.format(preço))
