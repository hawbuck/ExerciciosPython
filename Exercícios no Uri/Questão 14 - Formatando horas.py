#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
# e informe-o expresso no formato horas:minutos:segundos.

#Entrada
tempoSegundos = int(input())

#Processamento
if tempoSegundos >= 3600:
	horas = tempoSegundos // 3600
	tempoSegundos = tempoSegundos % 3600
else:
	horas = 0
if tempoSegundos >= 60:
	minutos = tempoSegundos // 60
else:
	minutos = 0

#Saída
print("{}:{}:{}".format(horas, minutos, tempoSegundos))			