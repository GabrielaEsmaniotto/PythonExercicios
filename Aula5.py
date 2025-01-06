nome = str(input('Digite seu nome: '))
if nome == 'Marlon':
    print('Que nome bonito você tem!')
elif nome == 'Gabriela' or nome == 'Pedro' or nome == 'Jose' or nome == 'Maria':
    print('Seu nome é bem comum no Brasil!')
elif nome in 'Ana Juliana Jessica Paula':
    print('Belo nome feminino!')
else:
    print('Seu nome é muito normal!')
print('Tenha um bom dia, \033[35m{}\033[m!'.format(nome))
