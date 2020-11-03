#coding: utf-8#
'''
Crie um programa que leia dois números  e realize a contagem do primeiro até o segundo número, com passo um.
'''
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
aux_n2 = n2 + 1

if (n1 < n2):
	for i in range (n1,aux_n2,1):
		print (i)
else:
	for i in range (n1,n2,-1):
		print (i)


	