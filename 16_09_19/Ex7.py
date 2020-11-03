#coding: utf-8#
'''
Faça um programa, utilizando o comando de repetição while, 
que leia n valores inteiros do teclado e ao final do programa imprima a somatória destes números, 
o laço deverá ser finalizado quando um número negativo for digitado
'''
soma = 0
n1 = 0
while (n1 >= 0):
	n1 = int(input("Digite um número inteiro: "))
	if (n1 >= 0):
		soma = soma + n1
print(soma)
print("número negativo digitado!")