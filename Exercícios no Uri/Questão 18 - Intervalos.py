#Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem
# dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra.
# Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

#Entrada
number = float(input())

#processamento e saída
if number >= 0 and number <= 25:
	print("Intervalo [0,25]\n")
elif number > 25 and number <= 50:
	print("Intervalo (25,50]\n")
elif number > 50 and number <= 75:
	print("Intervalo (50,75]\n")
elif number > 75 and number <= 100:
	print("Intervalo (75, 100]\n")
else:
	print("Fora de intervalo\n")