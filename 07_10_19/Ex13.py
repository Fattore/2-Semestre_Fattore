#coding: utf-8
"""
Defina uma função com o nome area_circulo que tem como valor a área de um círculo cujo raio é r. 
Note-se que esta área é dada pela fórmula πr2. Use o valor 3.14 para a constante π.
"""

def area_circulo(r):
	r = (3.14 * r)**2
	return(r)
raio = float(input("Digite o raio: "))
print(area_circulo(raio))

