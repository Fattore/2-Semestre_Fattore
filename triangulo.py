#encoding: utf-8
'''
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo e, se forem, 
se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes conceitos:
• O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
• Chama-se equilátero o triângulo que tem três lados iguais.
• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais. 
• Recebe o nome de escaleno o triangulo que tem os três lados diferentes.
'''

var_a = int(input("Digite o 1º valor inteiro: ")) 
var_b = int(input("Digite o 2º valor inteiro: ")) 
var_c = int(input("Digite o 3º valor inteiro: "))

if (var_a < var_b + var_c) or (var_b < var_c + var_a) or (var_c < var_a + var_b):
	print("É um triângulo!!")
	print()
	if (var_a == var_b == var_c):
		print("O tipo do triângulo é: Equilátero")
		print("Equilátero: Tem todos os lados iguais!!")
	elif (var_a == var_b != var_c) or (var_b == var_c != var_a) or (var_c == var_a != var_b):
		print("O tipo de triângulo é: Isósceles")
		print("Isósceles: Dois lados iguais apenas!!")
	elif (var_a != var_b != var_c):
		print("O tipo de triângulo é: Escaleno")
		print("Escaleno: Todos os lados diferentes!!")
	else:
		print("Opção Inválida!!")