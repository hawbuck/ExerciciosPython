#Crie uma função que permita a conversão de graus Celsius para Fahrenheit.

#Cálculo de Celsius para fahrenheit
def celsiusFahrenheit(temperaturaEmCelsius):
	temperaturaEmFahranheit = ((temperaturaEmCelsius*9)/5) + 32;
	return temperaturaEmFahranheit

#Código principal

#Entrada
celsius = float(input("Digite a temperatura em Celsius: "))

#Processamento
fahrenheit = celsiusFahrenheit(celsius)

#Saída
print("\nCelsius:{} graus \nFahrenheit:{} graus\n".format(celsius, fahrenheit))