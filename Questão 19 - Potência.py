#Crie uma função potencia que receba dois n´umeros a e b (base e expoente, respectivamente) e retorne a^b.

#Função Potência
def potencia(base, expoente):
	return a**b

#Código principal
#Entrada
a = int(input("Digite uma base: "))
b = int(input("Digite um expoente: "))

#Cálculo
resultado = potencia(a, b)

#Saída
print("O resultado de {} elevado a {} é {}".format(a, b, resultado))