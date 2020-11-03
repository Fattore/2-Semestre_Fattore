#coding: utf-8
"""10) Escreva uma função que desenhe um retângulo de 5 linhas por 20 colunas usando os caracteres ‘+’ , ‘-’ e ‘|’. 
O número de linhas, o de colunas e os caracteres do desenho são argumentos “default” da função. 
Quando a função é chamada sem nenhum argumento, desenha o seguinte retângulo:
+--------------------------------+
|                                |
|                                |
|                                |
+--------------------------------+

"""

def imprimir():
		print ("+" , 18 * "-", "+")
		print ("|" , 18 * " ", "|")
		print ("|" , 18 * " ", "|")
		print ("|" , 18 * " ", "|")
		print ("+" , 18 * "-", "+")

imprimir()