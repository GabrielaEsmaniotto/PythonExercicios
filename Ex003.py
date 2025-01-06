n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
s = n1 + n2
#print('A soma entre ', n1, 'e', n2, 'vale: ', s)
print('A soma entre \033[31m{0}\033[m e \033[31m{1}\033[m vale: \033[31m{2}'.format(n1, n2, s))
