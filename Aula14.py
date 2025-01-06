#DOCSTRINGS
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)
#Vai mostrar o manual explicando o que foi escrito no código



#PARAMETROS OPCIONAIS
def soma(a=0, b=0, c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: Sem retorno
    '''
    soma = a + b + c
    print(f'A soma vale {soma}')

soma(3, 2, 5)
soma(9)
soma(2, 4)
soma()
soma(b=4, c=2)
soma(c=3, a=2, b=9)



#ESCOPO DE VARIÁVEIS
def teste():
    x = 8
    #A variável X só existe dentro do teste, não vai funcionar fora e sé é condiderada
    #dentro do teste, é chamada de ESCOPO LOCAL
    print(f'Na função teste, N vale {n}')
    #O N vai valer 2
    print(f'Na função teste, X vale {x}')


#PROGRAMA PRINCIPAL
n = 2
#Mesmo o N sendo declarado aqui embaixo, o valor vai ser considerado no programa todo.
#Isso é chamado de ESCOPO GLOBAL
print(f'No programa principal, N vale {n}')
teste()
print(f'No programa principal, X vale {x}')
#Vai dar erro por a varíavel X é de ESCOPO LOCAL


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')
    #ESCOPO LOCAL

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
#ESCOPO GLOBAL



def teste(b):
    global a
    #Vai obrigar o programa a usar a varíavel A do escopo global
    a = 8
    #Vai fazer a varíavel A do escopo global passar a valer 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    #Vai criar uma nova varíavel A com valor 8 e imprimir o A do escopo local
         #CASO NÃO TENHA DECLARADO O (GLOBAL A)
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
#Se for declarado (GLOBAL A) dentro do escopo local, a varíavel A do escopo global
#perde seu valor e passa a valer 8 que foi declarado no escopo local
teste(a)
print(f'A fora vale {a}')
#Vai imprimir o A do escopo global a=5
   #CASO NÃO TENHA DECLARADO O GLOBAL A NO ESCOPO LOCAL



#RETORNANDO VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    #Com o return é possível mostrar vários resultados de uma vez só

r1 = somar(2, 3, 5)
r2 = somar(4, 1)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')




#EXERCÍCIO DE FATORIAL
def fatorial(num=1):
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
    return fatorial


numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é igual a: {fatorial(numero)}')
#Caso queira pedir um número ao usuário

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
#Com números de fatoriais já declarados


0
#EXERCÍCIO DE PAR E ÍMPAR
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É PAR!')
else:
    print('NÃO É PAR!')
