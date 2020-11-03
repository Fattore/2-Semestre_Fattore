#coding: utf-8
"""
Defina uma função com o nome dias_mes que recebe uma cadeia de caracteres, correspondentes às 
3 primeiras letras (minúsculas) do nome de um mês, e tem como valor um número inteiro correspondendo a número de dias desse mês. 
No caso de uma
cadeia de caracteres inválida, a sua função deverá gerar um erro de valor (ValueError).
Assuma que o mês de Fevereiro tem sempre 28 dias.

"""

def dias_mes(mes):
	if (mes == "JAN"):
		mes = "Janeiro"
		dia = 31
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "FEV"):
		mes = "Fevereiro"
		dia = 28
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "MAR"):
		mes = "Março"
		dia = 31
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "ABR"):
		mes = "Abril"
		dia = 30
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "MAI"):
		mes = "Maio"
		dia = 31
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "JUN"):
		mes = "Junho"
		dia = 30
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "JUL"):
		mes = "Julho"
		dia = 31
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "SET"):
		mes = "Setembro"
		dia = 30
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "OUT"):
		mes = "Outubro"
		dia = 31
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "NOV"):
		mes = "Novembro"
		dia = 30
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	elif (mes == "DEZ"):
		mes = "Dezembro"
		dia = 31
		result = ("Mês: {}\nDias: {}".format(mes,dia))
		return (result)
	else:
		mes = "ValueError"
		return (mes)

mes = input("Digite a sigla do mês desejado:\nEX: Fev\n>>> ").upper()
print(dias_mes(mes))
