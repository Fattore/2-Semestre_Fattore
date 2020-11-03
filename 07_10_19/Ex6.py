#coding: utf-8
"""
Escreva uma função para calcular o quadrado de um número. 
"""
def quadrado(n1):
	resultado = (n1 ** 2)
	return resultado

n1 = int(input("Digite o valor: "))
print("O numero {} ao quadrado é {}".format(n1,quadrado(n1)))