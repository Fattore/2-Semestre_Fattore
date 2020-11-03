#coding: utf-8
"""
Escreva uma função com o nome potencia que recebe como argumentos dois números inteiros não negativos, b e n, e tem como valor 
a potência n de b, i.e., bn
Neste exercício não pode usar a função pow nem o operador **.
"""

def potencia(n,b):
	calc = 0
	for i in range(1,b+1):
		calc = (n * n) + calc
	return calc

n1 = int(input("Digite o número que sera potencializado: "))
n2 = int(input("Digite a potência: "))
print(potencia(n1,n2))

