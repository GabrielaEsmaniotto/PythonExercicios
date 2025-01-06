frase = 'Curso em Vídeo Python'
print(frase) #Frase inteira
print(frase[3]) #Mostra a letra 3, lembrando que começa do 0
print(frase[3:13]) #Mostra da letra 3 até a 13, lembrando que a última corta, ou seja ate a 12
print(frase[:13]) #Não indica o inicio, apenas o fim
print(frase[13:]) #Não indica o fim, apenas o inicio
print(frase[1:15:2]) #Mostra da letra 1 até a 15 pulando de 2 em 2
print(frase[1::2]) #Mostra a partir da letras 1, não indica o fim e pula de 2 em 2 até acabar a frase
print(frase[::2]) #Não indica inicio e nem fim, pula de 2 em 2 ate acabar a frase

print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos 
aprender são o Fatiamento de String.""")
#Aspas triplas para escrever na tela um texto grande de uma vez.


#ANÁLISE

frase = ('Curso em Vídeo Python')
print(len(frase)) #Vai dizer o tamanho da frase

frase = ('Curso em Vídeo Python')
print(frase.count('o')) #Vai contar quantas vezes tem a letra 'o' na frase

frase = ('Curso em Vídeo Python')
print(frase.count('o', 0 , 13))
# Vai contar quantas vezes tem a letra 'o' da posição 0 até a 13, lembrando que o 13 corta

frase = ('Curso em Vídeo Python')
print(frase.find('Curso')) #Vai dizer em qual posição começar a frase 'Curso'

frase = ('Curso em Vídeo Python')
print(frase.find('Android'))
#Se for colocado dentro do find uma string que não existe dentro da frase vai retornar -1

frase = ('Curso em Vídeo Python')
print('Curso' in frase) #Vai dizer ser a palavra 'Curso' está dentro da frase


#TRANSFORMAÇÃO

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python, Android')
print(frase) #Vai trocar uma letra por outra

frase = ('Curso em Vídeo Python')
frase.upper() #Vai transformar todas as letras em maiusculas

frase = ('Curso em Vídeo Python')
frase.lower() #Vai transformar todas as letras em minusculas

frase = ('Curso em Vídeo Python')
frase.capitalize()
#Vai jogar todas as letras para minusculas e apenas a primeira letra permanece maiúscula

frase = ('Curso em Video Python')
frase.title()
#Vai analisar frase por frase e deixar as primeiras letras de cada frase em maiuscula

frase = ('   Curso em Vídeo Python   ')
print(len(frase.strip())) #Vai remover os espaços indesejados antes e depois da frase

frase = ('   Curso em Vídeo Python   ')
print(len(frase.rstrip())) #Vai remover os espaços da direita

frase = ('   Curso em Vídeo Python   ')
print(len(frase.lstrip())) #Vai remover os espaços da esquerda


#DIVISÃO

frase = ('Curso em Vídeo Python')
dividido = frase.split() #Vai separar cada frase em uma lista e começar a contagem de novo
print(dividido[0]) #Vai mostrar o primeiro item da lista na posição '0'

frase = ('Curso em Vídeo Python')
dividido = frase.split()
print(dividido[2][3]) #Vai mostrar a letra 3 do item da lista na posição '2'


#JUNÇÃO

frase = ('Curso em Vídeo Python')
'-'.join(frase) #Vai juntar as frases que estavam separadas
#OU
' '.join(frase) #Vai juntar as frases sem aparecer o traço '-'
