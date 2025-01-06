print('Informe o valor de três retas... ')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('É possível formar um triângulo')
    if r1 == r2 == r3:
        print('Triângulo Equilátero: Todos os lados são iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo Isósceles: Dois lados iguais')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno: Todos os lados são diferentes')
else:
    print('Não é possível formar um triângulo')
