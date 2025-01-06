soma = 0
conta = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma = soma + contador
        conta = conta + 1
print('A soma de todos os {} valores solicitados é de {}'.format(conta, soma))
