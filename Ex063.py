'''atual = 1
anterior = 0
sequencia = 0
fibonacci = 0
numero = int(input('Digite um qualquer: '))
while numero > sequencia:
    print(anterior)
    fibonacci = anterior + atual
    anterior = atual
    atual = fibonacci
    sequencia += 1'''



numero = int(input('Quantos termos de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
contador = 3
while contador <= numero:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' - FIM!')
