nomeHomem = ' '
menos20 = 0
maiorIdade = 0
totalIdade = 0
for contador in range(1, 5):
    print('----- {}º PESSOA -----'.format(contador))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = int(input('Sexo: [1]Masculino [2]Feminino '))
    totalIdade = totalIdade + idade

    if sexo == 1:
        if idade > maiorIdade:
            maiorIdade = idade
            nomeHomem = nome
    else:
        if idade < 20:
            menos20 = menos20 + 1

mediaIdade = totalIdade / 4
print('A média de idade é de {}'.format(mediaIdade))
print('{} mulheres tem menos de 20 anos'.format(menos20))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomeHomem, maiorIdade))
