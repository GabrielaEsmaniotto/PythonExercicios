termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
for contador in range(0, 10):
    pa = termo + (razao * contador)
    print(pa)
