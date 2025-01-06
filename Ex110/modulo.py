def aumentar(preço=0, taxa=0, formato=False):
    resultado = preço + (preço * taxa / 100)
    if formato==False:
        return resultado
    else:
        return moeda(resultado)


def diminuir(preço=0, taxa=0, formato=False):
    resultado = preço - (preço * taxa / 100)
    if formato == False:
        return resultado
    else:
        return moeda(resultado)


def dobro(preço=0, formato=False):
    resultado = preço * 2
    if formato == False:
        return resultado
    else:
        return moeda(resultado)


def metade(preço=0, formato=False):
    resultado = preço / 2
    if formato==False:
        return resultado
    else:
        return moeda(resultado)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaaumento=10, taxareduçao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaaumento} de aumento: \t\t{aumentar(preço, taxaaumento, True)}')
    print(f'{taxareduçao} de redução: \t\t{diminuir(preço, taxareduçao, True)}')
    print('-' * 30)
#\t vai centralizar os valores
