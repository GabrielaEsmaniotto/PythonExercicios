from datetime import date
anoatual = date.today().year
nome = str(input('Digite seu nome: '))
print('[1] FEMININO')
print('[2] MASCULINO')
sexo = int(input('Qual seu sexo? '))
anonasc = int(input('Qual seu ano de nascimento?  '))
idade = anoatual - anonasc
if sexo == 1:
     print('Mulheres não são obrigadas a se alistar no serviço militar!')
elif sexo == 2:
     print('Todos os homens precisam se alistar no serviço militar!')
     if idade < 18:
          tempo = 18 - idade
          print('Faltam {} anos para você se alistar no serviço militar'.format(tempo))
          ano = anoatual + tempo
          print('Seu alistamento será em {}'.format(ano))
     elif idade == 18:
          print('Voce tem 18 anos, está na hora de se alistar no serviço militar')
     elif idade > 18:
          prazo = idade - 18
          print('Ja passou {} anos que você deveria ter se alistado no serviço militar'.format(prazo))
          ano = anoatual - prazo
          print('Seu alistamento foi em {}'.format(ano))
