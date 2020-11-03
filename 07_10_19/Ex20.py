#coding utf-8
"""
Suponha que a operação de multiplicação não existia em Python, 
existindo as operações de adição, +, de subtração, −, e o operador relacional >. 
Escreva em Python uma função com o nome vezes, que efetua a multiplicação de dois inteiros positivos. 
"""
def vezes(x,y):
	resultado = 0; 
	for i in range(x): 
		resultado += y
	return resultado

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
result = vezes(n1,n2)
print("{} > {}: {}".format(n1,n2,result))