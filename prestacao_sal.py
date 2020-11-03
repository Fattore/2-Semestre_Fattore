#encoding: utf-8
'''
Leia o salario de um trabalhador e o valor da prestação de um empréstimo. 
Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, 
caso contrario imprima: ´ Empréstimo concedido.
'''
salario = int(input("Digite seu salário: "))
prestacao = int(input("Digite o valor da prestação do empréstimo: "))

if prestacao > salario * 0.2:
	print("Empréstimo não concedido!")
else:
	print("Empréstimo concedido")
