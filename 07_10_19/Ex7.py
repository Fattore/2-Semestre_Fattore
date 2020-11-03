#coding: utf-8
"""
Escreva uma função que receba como parâmetro o preço atual de uma mercadoria e calcule
 o novo preço da mercadoria com reajuste de 20%.
"""
def novoPreco(var):
	reajuste = (var*0.20)
	novo_preco = var + reajuste
	return novo_preco

n1 = float(input("Digite o valor do produto: "))
print("O preço do produto é: {:.2f}\nO preço com reajuste de 20% é: {:.2f}".format(n1,novoPreco(n1)))
