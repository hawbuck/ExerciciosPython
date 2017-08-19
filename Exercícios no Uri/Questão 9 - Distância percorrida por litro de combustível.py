#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) 
#e o total de combustível gasto (em litros).

#Entrada
x = int(input())
y = float(input())

#Processamento
gasto = x/y
gasto = "%.3f" % gasto

#Saída
print("{} km/l".format(gasto))
