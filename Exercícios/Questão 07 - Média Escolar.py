#Leia as duas notas de um aluno e mostre a média dele

nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

print('A média do aluno {} é: {}'.format(nome, ((nota1 + nota2)/2)))