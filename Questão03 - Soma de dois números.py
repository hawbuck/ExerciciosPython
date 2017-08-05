#Crie um script python que leia dois números e tente mostrar a soma entre eles

numero1 = input("Digite um número:")
numero2 = input("Digite outro número:")
soma = int(numero1) + int(numero2)
#o print a seguir segue padrões antigos
#print("A soma dos números",numero1,"e",numero2,"é:", soma)
print("A soma dos números {} e {} é: {}".format(numero1, numero2, soma))
