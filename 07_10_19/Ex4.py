#coding: utf-8
"""
Escreva uma função para calcular a área de um retângulo. 
"""

def area(base,altura):
	area = (base * altura) /2
	return area

base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
print("a area do retangulo é: {}".format(area(base,altura)))