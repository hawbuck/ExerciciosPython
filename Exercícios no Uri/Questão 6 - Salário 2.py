#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total 
#de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor 
#ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final 
#do mês, com duas casas decimais.

#Entrada
nome = input()
salarioFixo = float(input())
totalDeVendas = float(input())#montante de vendas, não a quantidade

#Processamento
salarioTotal = salarioFixo + totalDeVendas*0.15
salarioTotal = "%.2f" % (salarioTotal)

#Saída
print("TOTAL = R$ {}".format(salarioTotal))