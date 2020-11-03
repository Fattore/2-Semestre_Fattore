#coding: utf-8
"""
Escreva uma função para calcular o fatorial de um número inteiro.
"""
def fatorial(numero):
	fat = 1
	for i in range(numero,1,-1):
		fat = fat * i
	return fat

n1 = int(input("Digite o número que deseja saber o fatorial: "))
print("{}! = {}".format(n1,fatorial(n1)))
