from datetime import date
anoatual = date.today().year
maioresDeIdade = 0
menoresDeIdade = 0
for contador in range(1, 8):
    anonasc = int(input('Em que ano a {}º pessoa nasceu? '.format(contador)))
    idade = anoatual - anonasc
    if idade >= 21:
        maioresDeIdade = maioresDeIdade + 1
    else:
        menoresDeIdade = menoresDeIdade + 1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(maioresDeIdade, menoresDeIdade))
