#coding: utf-8#
'''
Faça um programa que leia um número natural e calcule o seu fatorial
'''
n1 = int(input("Digite um número natural: "))
fat = 1
for i in range(2,n1+1):
	fat = fat * i
	
print("%d! = %d" %(n1, fat))  

