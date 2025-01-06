valor = float(input('Qual o valor da casa que deseja comprar R$ '))
salario = float(input('Qual o valor do seu salario R$ '))
anos = float(input('Em quantos anos deseja pagar a casa? '))
mensal = 12 * anos
parcela = valor / mensal
salario30 = salario * 30 / 100
print('Sua parcela ficará no valor de {:.2f}'.format(parcela))
if parcela > salario30:
    print('A parcela ultrapassa 30% do seu salário.')
    print('\033[31mEMPRÉSTIMO NEGADO!')
else:
    print('\033[32mEMPRÉSTIMO APROVADO!')
