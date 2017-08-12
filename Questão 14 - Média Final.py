#Receba as 4 médias bimestrais de um aluno e cálcule se ele foi aprovado ou não

b1 = float(input("Digite a média do 1º Bimestre: "))
b2 = float(input("Digite a média do 2º Bimestre: "))
b3 = float(input("Digite a média do 3º Bimestre: "))
b4 = float(input("Digite a média do 4º Bimestre: "))

mediaFinal = (b1+b2+b3+b4)/4

if mediaFinal < 6: 
	print("O aluno foi reprovado!")
else: 
	print("O aluno foi aprovado!")	