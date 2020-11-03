#coding: utf-8#
'''
Faça um programa  que apresente a série de Fibonacci até o décimo quinto termo
'''
qtd = int(input("Quantos fibonacci vai querer? "))
soma = 0
n1 = 1
n2 = 1
print("1\n1")
aux_qtd = qtd - 2
for i in range (aux_qtd):
	soma = n1 + n2
	n2 = soma
	n1 = soma - n1
	print(soma)