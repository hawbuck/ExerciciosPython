#Faça um programa que leia dois números e retorne o maior deles

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
	print("O número {} é maior que o número {}".format(numero1, numero2))
else:
	print("O número {} é maior que o número {}".format(numero2, numero1))	