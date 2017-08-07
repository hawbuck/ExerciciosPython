#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessário para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2 metros²

#Recebendo Valores
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

#Calculando a área da parede
area  = largura * altura

#Calculando o gasto de tinta 
quantidadeTinta = area / 2

#Mostrando o gasto de tinta
print('Uma parede com {} metros de largura e {} metros de altura, vai utilizar {} litros de tinta'.format(largura, altura, quantidadeTinta))
