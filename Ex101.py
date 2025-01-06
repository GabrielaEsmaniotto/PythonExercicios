from datetime import date

anoAtual = date.today().year

def Voto():
    print(f'Você está com {idade} anos!')
    if idade < 16:
        return 'NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO!'


anoNasc = int(input('Qual seu ano de nascimento?  '))
idade = anoAtual - anoNasc
print(Voto())
