total = totmil = menor = contador = 0
nomeProduto = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Preço R$'))
    contador = contador + 1
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if contador == 1 or preço < menor:
        menor = preço
        nomeProduto = nome
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'O total gasto na compra é de {total}')
print(f'Existem {totmil} produtos maior de R$1.000 reais')
print(f'O produto mais barato é o {nomeProduto} no valor de {menor}')
