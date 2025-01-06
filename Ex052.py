numero = int(input('Digite um número: '))
texto = 'É um número primo!'
for contador in range(2, numero):
    if numero % contador == 0:
        texto = 'Não é um número primo!'
print(texto)
