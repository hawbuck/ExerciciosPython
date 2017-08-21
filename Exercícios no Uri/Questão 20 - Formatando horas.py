#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
# e informe-o expresso no formato horas:minutos:segundos.

#Entrada
N = int(input())

#Processamento
horas = N / 3600
minutos = (N % 3600) / 60
segundos = (N % 3600) % 60
#Saída
print("{}:{}:{}".format(horas, minutos, segundos))			