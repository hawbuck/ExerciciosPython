#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto

#Recebendo o preço de um produto
preco = float(input('Digite o preço do produto: '))

#Calculando o preço com o desconto
desconto = preco * 0.95

#Mostrando o preço com o desconto
print("O produto de que custava {} reais, fica {} reais com desconto de 5%".format(preco, desconto))