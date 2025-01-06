def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: (Opcional) Mostra ou não a conta
    :return: O valor de fatorial de um número N
    '''
    fatorial = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= c
    return fatorial


valor = int(input('Quer mostrar o fatorial de qual número? '))
print(fatorial(valor, show=True))
#show=True vai mostrar o calculo inteiro do fatorial
help(fatorial)
