nome = str(input('Digite seu nome completo: ')).strip()
nomeMaiusculo = nome.upper()
print('Seu nome com todas as letras maiúsculas fica: {}'.format(nomeMaiusculo))
nomeMinusculo = nome.lower()
print('Seu nome com todas as letras minúsculas fica: {}'.format(nomeMinusculo))
nomeJunto = len(nome) - nome.count(' ')
print('Seu nome tem {} letras'.format(nomeJunto))
nomeDividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nomeDividido[0])))
