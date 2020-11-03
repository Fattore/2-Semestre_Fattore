#coding: utf-8
"""
Um número d é divisor de n se o resto da divisão de n por d for 0. 
Escreva uma função com o nome num_divisores que recebe um número inteiro positivo n, e tem como valor o número de divisores de n. 
No caso de n ser 0 deverá devolver 0.
"""
def num_divisores(n):
	if(n == 0):
		n = 0
		return n
	calc = 0
	for i in range(1,n+1):
		if(n % i == 0):
			calc = calc + 1
	return calc

n = int(input("Digite um número: "))
print(num_divisores(n))