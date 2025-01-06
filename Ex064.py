numero = 0
tentativa = 0
soma = 0
print('Para parar, digite 999')
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        print('Foram digitados {} números e a soma entre eles é {}'.format(tentativa, soma))
    else:
        tentativa = tentativa + 1
        soma = soma + numero
print('Acabou!')
