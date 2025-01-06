frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} veze(s).'.format(frase.count('A')))
print('A letra A aparece pela primeira vez em {} posição'.format(frase.find('A')+1))
print('A letra A aparece pelo última vez na {} posição'.format(frase.rfind('A')+1))
