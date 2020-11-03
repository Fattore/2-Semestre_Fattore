#coding: utf-8#
'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1
'''
n1 = 1
while (n1 > 0):
	n1 = int(input("Verificar numeros primos ate: "))
	aux=0

	for i in range(2,n1):
	    if (n1 % i == 0):
	        print("Número: {} não é primo!\n".format(n1))
	        print("Múltiplo de",i)
	        aux += 1

	if(aux==0):
	    print("Número: {} é um número primo!\n".format(n1))
	else:
	    print("Tem",aux," múltiplos acima de 2 e abaixo de",n1)












