#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
#caso haja uma divisão por 0 ou raiz de numero negativo.

#Entrada

a, b, c = map(float, raw_input().split())

#Processamento

delta = (b**2)-4*(a)*(c)

x1 = ((-b)+(delta**1/2))/(2*a)
x2 = ((-b)-(delta**1/2))/(2*a)

x1 = "%.5f" % x1
x2 = "%.5f" % x2

if a == 0:
	print("Impossivel calcular")
elif delta < 0:
	print("Impossivel calcular")
else:
	print("R1 = {}\nRn2 = {}\n".format(x1, x2))
	