salario = float(input('Digite o valor do seu salário R$ '))
if salario > 1250:
    aumento = (salario * (10 / 100)) + salario
    print('Seu salário com aumento de 10% fica em R${}'.format(aumento))
else:
    aumento = (salario * (15 / 100)) + salario
    print('Seu salário com aumento de 15% fica em R${}'.format(aumento))
