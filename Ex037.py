numero = int(input('Digite um número inteiro: '))
print('=' * 15)
print('''[1] Binário')
[2] Octal')
[3] Hexadecimal')
[4] Sair''')
print('=' * 15)
escolha = int(input('Escolha qual opção deseja converter: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
elif escolha == 4:
    print('Saindo...')
else:
    print('Opção inválida!')
