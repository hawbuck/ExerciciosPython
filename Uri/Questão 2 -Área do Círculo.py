#A fórmula para calcular a área de uma circunferência é: area = π . raio2.
#Considerando para este problema que π = 3.14159:
#Efetue o cálculo da área, elevando o valor de Raio ao quadrado e multiplicando por π.

#Entrada
raio = float(input())
pi = 3.14159

#Processamento
area = pi*(raio**2)
area = 	"%.4f" % (area)

#Saída
print("A={}".format(area))