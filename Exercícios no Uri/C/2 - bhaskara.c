/*Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.*/

#include<stdio.h>
int main(){
	float a, b, c;
	float delta, x1, x2;

	scanf("%f %f %f", &a, &b, &c);

	delta = (pow(b,2)) - 4*(a)*(c);
	x1 = (-b + sqrt(delta))/2*a;
	x2 = (-b - sqrt(delta))/2*a;
	x1 = x1/100;
	x2 = x2/100;
	if(a == 0){
		printf("Impossivel calcular\n");
	} 
	else if(delta < 0){
		printf("Impossivel calcular\n");
	}
	else{
		printf("R1 = %.5f\n", x1);
		printf("R2 = %.5f\n", x2);
	}
	return 0;
}