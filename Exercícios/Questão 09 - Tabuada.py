#Leia um inteiro e mostre sua tabuada

#input e definição do título
numero = int(input('Digite um número inteiro: '))
tabuada = 'TABUADA'

#operações
vezes0 = numero * 0
vezes1 = numero * 1
vezes2 = numero * 2
vezes3 = numero * 3
vezes4 = numero * 4
vezes5 = numero * 5
vezes6 = numero * 6
vezes7 = numero * 7
vezes8 = numero * 8
vezes9 = numero * 9

#tabuada
print('{:=^20}\n'.format(tabuada))
print(' {} x 0 = {}'.format(numero, vezes0))
print(' {} x 1 = {}'.format(numero, vezes1))
print(' {} x 2 = {}'.format(numero, vezes2))
print(' {} x 3 = {}'.format(numero, vezes3))
print(' {} x 4 = {}'.format(numero, vezes4))
print(' {} x 5 = {}'.format(numero, vezes5))
print(' {} x 6 = {}'.format(numero, vezes6))
print(' {} x 7 = {}'.format(numero, vezes7))
print(' {} x 8 = {}'.format(numero, vezes8))
print(' {} x 9 = {}'.format(numero, vezes9))