#Leia um valor em metros e converta de centrímetros e em milímetros

valorMetros = float(input('Digite um valor em metros: '))
valorCentrimetros = valorMetros / 100
valorMilimetros = valorMetros / 1000

print('O valor {} metros em centrímetros é {} e em milímetros {}'.format(valorMetros, valorCentrimetros, valorMilimetros))