#coding: utf-8#
'''
Faça um programa que apresente o total 
da soma dos cem primeiros números inteiros.
'''
soma = 0
for i in range (1,101,1):
	soma = soma + i
	print(i,"",soma)
print ("A soma dos 100 primeiros números inteiros é = ",soma)
