#Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A,
# e a soma de C com D for maior que a soma de A e B e se C e D, ambos, 
#forem positivos e se a variável A for par escrever a mensagem "Valores aceitos",
# senão escrever "Valores nao aceitos".

#entrada
entrada = input("") # lendo os números
# quebrando a entrada em tokens separados por espaço (poderia ser outro separador)
numerosComoString = entrada.split(" ")
# criando uma nova lista com a conversão para float de cada número
numeros = [float(numero) for numero in numerosComoString] 

# atribuindo cada posição da lista a uma variável
a, b, c, d = numeros
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

#processamento
somaCD = c+d
somaAB = a+b

if(b > c & d > a & somaCD > somaAB & c > 0 & d > 0 & a%2 == 0):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")	