def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsúaio preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')
