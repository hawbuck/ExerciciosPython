#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#primitivo e todas as informações possíveis sobre ele
qualquerCoisa = input("Digite qualquer coisa: ")
print('O seu tipo primitivo é:',type(qualquerCoisa))
print('É númerico?', qualquerCoisa.isnumeric())
print('É alfabético?', qualquerCoisa.isalpha())
print('Está em maiúsculo?', qualquerCoisa.isupper())