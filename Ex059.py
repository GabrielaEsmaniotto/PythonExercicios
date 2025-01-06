from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print('''Opções...
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    escolha = int(input('Qual opção você deseja? '))

    if escolha == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Saindo...')
    else:
        print('Opção inválida, tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
