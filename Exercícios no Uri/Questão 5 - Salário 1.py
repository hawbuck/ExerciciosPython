#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
#o valor que recebe por hora e calcula o salário desse funcionário. 
#A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

#Entrada 
number = int(input())
hours = int(input())
salaryPerHour = float(input())

#Processamento
salary = float(hours*salaryPerHour)
salary = "%.2f" % (salary)

#Saída
print("NUMBER = {}\nSALARY = U$ {}".format(number, salary))