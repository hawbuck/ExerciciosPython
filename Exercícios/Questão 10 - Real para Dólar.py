#Crie um progrma que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

#pegando o valor em Real
valorReal = float(input("Quanto dinheiro você tem na carteira? "))

#Convertendo pra dólar
valorDolar = valorReal / 3.27

print("Com {} reais, você pode comprar {} dólares".format(valorReal,valorDolar))