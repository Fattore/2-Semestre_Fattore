#coding utf-8
"""
Escreva uma função com o nome soma_divisores que recebe um número inteiro positivo n, e tem como valor a soma de todos os divisores de n. 
No caso de n ser 0 deverá devolver 0.
"""
def soma_divisores(n):
	if(n == 0):
		n = 0
		return n
	calc = 0
	for i in range(1,n+1):
		if(n % i == 0):
			calc = calc + i
	return calc

n = int(input("Digite um número: "))
print(soma_divisores(n))