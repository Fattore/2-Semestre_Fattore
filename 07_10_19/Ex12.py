#coding: utf-8
"""
Defina uma função com o nome horas_dias que recebe um inteiro correspondente a 
um certo número de horas e que tem como valor um número real que traduz o número de dias correspondentes ao seu argumento.
"""

def horas_dias(i):
	i = float(i / 24)
	return i

horas = int(input("Digite o quantidade de horas: "))
print(">>>",horas_dias(horas))