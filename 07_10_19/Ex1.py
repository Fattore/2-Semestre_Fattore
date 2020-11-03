#coding: utf-8
"""
Crie um aplicativo que receba o raio de uma esfera (do tipo float) e chame o função volume
Esfera para calcular e exibir o volume da esfera na tela.
Para o cálculo do volume deve ser usada a fórmula seguinte: volume=(4.0/3.0)*PI*raio³.
"""
def volume_Esfera(var):
	volume = (4.0/3.0) * 3.14 * (var ** 3)
	return volume

raio = float(input("Digite o raio de uma esfera: "))
print("O valor do volume de uma esfera com o raio {} é {:.2f}!".format(raio,volume_Esfera(raio)))
