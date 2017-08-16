#Neste problema, deve-se ler o código de uma peça 1, 
#o número de peças 1, o valor unitário de cada peça 1,
#o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
#Após, calcule e mostre o valor a ser pago.

#Entrada
cod1, num1, valor1 = float(input().split(' '))
cod2, num2, valor2 = float(input().split(' '))

#processamento
total1 = num1 * valor1
total1 = "%.2f" % (total1)
total2 = num2 * valor2
total2 = "%.2f" % (total2)

total = total1 + total2
#Saída
print("VALOR A PAGAR: R$ {}".format(total))
