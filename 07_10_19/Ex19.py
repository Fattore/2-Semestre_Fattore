#coding utf-8
"""
Escreva uma função em Python com o nome numero_algarismos
que recebe um inteiro positivo, n, e devolve o número de algarismos de n. Por exemplo:
"""
def numero_algarismos(n):
	qtd = len(n)
	return ("A palavra: {} é composto de {} digito(s)".format(n,qtd))

n = input("Digite uma palavra: ")
print(numero_algarismos(n))