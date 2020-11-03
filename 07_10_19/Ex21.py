#coding utf-8
"""
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, 
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
def somaImposto(taxaImposto,custo):
	return custo * (taxaImposto/10) 

def altera(x,y):
	return x+y

n1 = int(input("Digite o custo do item: "))
n2 = int(input("Digite a quantia do imposto: "))
n3 = somaImposto(n2,n1)
n4 = altera(n1,n3)
print("O valor original é: {}\nO valor atual do item é: {}".format(n1,n4))
