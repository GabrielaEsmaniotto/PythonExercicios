produto = float(input('Digite o valor do produto R$'))
print('\033[35m=\033[m' * 30)
print('''Escolha a forma de pagamento...
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print('\033[35m=\033[m' * 30)
escolha = int(input('Qual a forma de pagamento? '))

if escolha == 1:
    desconto = produto - ((produto * 10) / 100)
    print('Seu produto no valor de R${} com 10% de desconto vai ficar no valor de R${}'.format(produto, desconto))
elif escolha == 2:
    desconto = produto - ((produto * 5) / 100)
    print('Seu produto no valor de R${} com 5% de desconto vai ficar no valor de R${}'.format(produto, desconto))
elif escolha == 3:
    parcela = produto / 2
    print('Seu produto vai continuar no valor normal de R${}'.format(produto))
    print('Seu produto em 2x no cartão fica no valor de R${} mensal.'.format(parcela))
elif escolha == 4:
    juros = produto + ((produto * 20) / 100)
    print('Seu produto com 20% de juros fica no valor de R${}'.format(juros))
    parcelas = int(input('Em quantas vezes deseja parcelar? '))
    jurosPar = juros / parcelas
    print('Parcelado em {} vezes fica no valor de R${} mensal.'.format(parcelas, jurosPar))
else:
    print('Opção inválida. Tente novamente.')
