#Escreva um programa que receba uma idade e retorne se é maior de idade ou não
idade = int(input("Digite sua idade: "))
resp = idade >=18

if resp == True:
	print("Você pode entrar na balada!")
else:
	print("Você não pode entrar na balada!")
