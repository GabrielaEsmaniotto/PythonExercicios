'''loop = 'continua'
while loop == 'continua':
    sexo = str(input('Digite seu sexo: [M/F] ')).upper()
    if sexo == 'F' or sexo == 'M':
        print('Acabou! ')
        loop = 'para'
    else:
        print('Opção incorreta, digite novamente! ')'''


sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'Mm or Ff':
    sexo = str(input('Opção inválida, digite seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
