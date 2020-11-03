#coding: utf-8#
'''
Calcular e mostrar o MDC entre 2 (dois) números naturais lidos
'''

n1 = int(input("Digite o primeiro número natural: "))
n2 = int(input("Digite o segundo número natural: "))
div_1 = 0
div_2 = 0
i = 1
while (i != 0):
	i = i + 1
	div_1 = (n1 / i)
	div_2 = (n2 / i)
	if (div_1 == 1 and div_2 != 1) or (div_1 != 1 and div_2 == 1):
		break
print(i)
#mdc (6,12) = 6
