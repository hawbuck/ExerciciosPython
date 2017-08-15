#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Recebendo o nome e o sexo
nome = input("Digite o seu nome:")
sexo = input("Digite seu sexo[F - feminino; M - Masculino]: ")

#Verificando
if sexo == "m":
	print("{} é do sexo Masculino".format(nome))
if sexo == "f":
	print("{} é do sexo Feminino".format(nome))	