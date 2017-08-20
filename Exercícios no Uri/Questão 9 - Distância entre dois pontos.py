#Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
#p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, 
#segundo a fórmula: distancia = raiz de (x2-x1)²+(y2-y1)²

#Entrada
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

#Processamento
distancia = (((x2 - x1)**2)+((y2 - y1)**2))**(1/2)

distancia = "%.4f" % distancia

#Saída
print("{}".format(distancia))