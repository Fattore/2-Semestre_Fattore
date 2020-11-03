#coding utf-8
"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação 
e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. 

Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar 
até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, 
exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.

O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""
def valorPagamento(prestação,dias):
	soma = 0
	total = 0
	if(dias == 0):
		total = prestação + total
	elif(dias > 0):
		juros = dias * 0.01
		multa = (prestação * 0.3) + juros
		total = prestação + multa + total
	soma = total + soma
	return soma

n1 = 1
i = 0
totalResult = 0
while(n1 != 0):
	i += 1
	n1 = float(input("Digite o valor da prestação: "))
	n2 = float(input("Digite o número de dias em atraso: "))
	print()
	result = valorPagamento(n1,n2)
	print("Valor a ser pago é: {}".format(result))
	totalResult = result + totalResult
	print()
print("Relatório do Dia:\nQuantidade de prestações pagas: {}\nValor total pago: {}".format(i,totalResult))
