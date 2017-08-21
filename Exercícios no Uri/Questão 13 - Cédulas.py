#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
# no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
#A seguir mostre o valor lido e a relação de notas necessárias.

#Entrada
quantia = int(input())
quantiaInicial = quantia
#Processamento
if 0 < quantia < 1000000:

	if quantia >= 100:
		notas100 = quantia // 100
		quantia = quantia % 100
	else:
		notas100 = 0	

	if quantia >= 50:
		notas50 = quantia // 50
		quantia = quantia % 50
	else:
		notas50 = 0

	if quantia >= 20:
		notas20	= quantia // 20
		quantia = quantia % 20
	else:
		notas20 = 0

	if quantia >=10:
		notas10 = quantia // 10
		quantia = quantia % 10
	else:
		notas10 = 0	

	if quantia >=5:
		notas5 = quantia // 5
		quantia = quantia % 5
	else:
		notas5 = 0	

	if quantia >= 2:
		notas2 = quantia // 2
		quantia = quantia % 2
	else:
		notas2 = 0		

	if quantia >=1:
		notas1 = quantia // 1
		quantia = quantia % 1
	else:
		notas1 = 0		

#Saída
print("{}".format(quantiaInicial))
print("{} nota (s) de R$ 100,00".format(notas100))
print("{} nota (s) de R$ 50,00".format(notas50))
print("{} nota (s) de R$ 20,00".format(notas20))
print("{} nota (s) de R$ 10,00".format(notas10))
print("{} nota (s) de R$ 5,00".format(notas5))
print("{} nota (s) de R$ 2,00".format(notas2))
print("{} nota (s) de R$ 1,00".format(notas1))