#coding: utf-8
"""
Crie um aplicativo que receba uma temperatura qualquer em Fahrenheit e apresente seu correspondente em Celsius
por meio de uma função. Para o cálculo utilize a seguinte fórmula: celsius=5.0/9.0 *(f-32).
"""
def converte(f):
	celsius = 5.0/9.0 * (f - 32)
	return celsius

Fahrenheit = float(input("Digite a temperatura: "))
print("A temperatura em Fahrenheit: {:.2f} °F\nA temperatura em Celcius: {:.2f} °C".format(Fahrenheit,converte(Fahrenheit)))