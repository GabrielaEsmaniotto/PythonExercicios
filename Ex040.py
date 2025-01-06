nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
     print('\033[31mREPROVADO')
elif media >= 5 and media < 7:
     print('\033[34mRECUPERAÇÃO')
else:
     print('\033[32mAPROVADO')
