#Crie uma função numero_par que permita verificar um dado número, x, passado como parâmetro é número par.

#Criando a função
def numero_par(numero):
	if(numero % 2 == 0):
		return "par"
	else:
		return "impar"	

#Código principal

#Entrada
numero = int(input("Digite um número: "))

#Processamento
resposta = numero_par(numero)

#Saída
print("O número {} é {}!".format(numero, resposta))		