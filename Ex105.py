def notas(*numeros, situacao=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param numeros: Uma ou mais notas dos alunos (aceita várias).
    :param situacao: Valor adicional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com vários informações sobre a situação da turma.
    '''
    dicionario = dict()
    dicionario['Total'] = len(numeros)
    dicionario['Maior'] = max(numeros)
    dicionario['Menor'] = min(numeros)
    dicionario['Média'] = sum(numeros)/len(numeros)
    if situacao:
        if dicionario['Média'] >= 7:
            dicionario['Situação'] = 'BOA'
        elif dicionario['Média'] >= 5:
            dicionario['Situação'] = 'RAZOÁVEL'
        else:
            dicionario['Situação'] = 'RUIM'
    return dicionario


resposta = notas(5.5, 2.5, 3.9, 8.9, situacao=True)
print(resposta)
help(notas)
