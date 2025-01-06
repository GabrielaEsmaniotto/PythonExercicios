maior18 = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{maior18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres tem menos de 20 anos')
