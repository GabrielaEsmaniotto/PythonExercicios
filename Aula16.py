try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except:
    print('Infelizmente tivemos um problema!')

else:
    print(f'O resultado é {r:.2f}')

finally:
    print('Volte sempre! Muito obrigado.')


#Dentro do try pode existir vários except, informando vários tipos de excessões

#SEGUNDO CASO:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um erro com os tipos de dados que você digitou!')
    #Erro de valor e erro de tipo

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usúario preferiu não informar os dados!')

except Exception as erro:
    print(f'Tivemos um problema! {erro.__class__}')
    #Vai informar qual foi a classe do problema

else:
    print(f'O resultado é {r:.2f}')

finally:
    print('Volte sempre! Muito obrigado.')



#try: Tente fazer isso
#except: Caso não dê certo, faça isso
#else: Caso dê certo, faça isso
#finally: Sempre vai acontecer, mesmo se der CERTO OU NÃO
