#coding: utf-8
"""
Escreva uma função que receba como argumento o ano e retorne 1 se for um ano bissexto e 0 se não for um ano bissexto.
Um ano é bissexto se for divisível por 4, mas não por 100.
Um ano também é bissexto se for divisível por 400.
"""
def bissexto(ano):
	if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
		return 1
	elif (ano%4 == 0 and ano%100 == 0):
		return 0

ano = int(input("Digite o ano ques deseja descobrir: "))
print(bissexto(ano))
