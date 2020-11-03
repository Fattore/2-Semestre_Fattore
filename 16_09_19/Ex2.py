#coding: utf-8#
'''
Faça um aplicativo que calcule o produto dos inteiros ímpares de 1 a 15 e exiba o resultado na tela.
'''
soma = 1
for i in range (1,16,1):
	if (i%2 != 0):
		soma = soma * i
		print(i,"",soma)
print ("O produto dos inteiros ímpares de 1 a 15 = ",soma)		