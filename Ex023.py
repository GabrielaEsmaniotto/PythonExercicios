numero = str(input('Digite um número de 0 a 9999: '))
tamanhoNumero = len(numero)
print('Unidade: {}'.format(numero[tamanhoNumero - 1]))
if(tamanhoNumero >= 2):
    print('Dezena: {}'.format(numero[tamanhoNumero - 2]))
if(tamanhoNumero >= 3):
    print('Centena: {}'.format(numero[tamanhoNumero - 3]))
if(tamanhoNumero >= 4):
    print('Milhar:: {}'.format(numero[tamanhoNumero - 4]))

#OU

numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
