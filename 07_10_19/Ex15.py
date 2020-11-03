#coding: utf-8
"""
Escreva uma função com o nome soma_quadrados que recebe um número inteiro positivo, n, e tem como valor 
a soma do quadrado de todos os números até n.
"""

def soma_quadrados(n):
	soma = 0
	for i in range (1,n+1):
		soma = (i ** 2) + soma
	return soma
	#return soma 

n = int(input("Digite um número: "))
print(soma_quadrados(n))