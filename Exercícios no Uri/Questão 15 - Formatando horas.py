#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
# e informe-o expresso no formato horas:minutos:segundos.

#Entrada
segundos = int(input())

#processamento

if segundos >= 3600:
	horas = segundos // 3600
	segundos = segundos % 3600

else: 
	horas = 0

if segundos >= 60:
	minutos = segundos // 60
	segundos = segundos % 60

else:
	minutos = 0

if segundos <= 0:
	segundos = 0
else:
	segundos = segundos

print("{}:{}:{}".format(horas, minutos, segundos))