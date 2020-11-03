#encoding: utf-8
'''
Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este numero. 
Isto e, janeiro se 1, fevereiro se 2, e assim por diante.
'''
n1 = int(input("Digite um número de 1 a 12: "))

if n1 == 1:
 	print("Janeiro")
elif n1 == 2:
	print("Fevereiro") 
elif n1 == 3: 
	print("Março")
elif n1 == 4:
	print("Abril")
elif n1 == 5:
	print("Maio")
elif n1 == 6:
	print("Junho")
elif n1 == 7:
	print("Julho")
elif n1 == 8:
	print("Agosto")
elif n1 == 9:
	print("Setembro")
elif n1 == 10:
	print("Outubro")
elif n1 == 11:
	print("Novembro")
elif n1 == 12:
	print("Dezembro")
else:
	print("Opção Inválida") 