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
