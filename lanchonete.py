#encoding: utf-8
'''
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. 
Considere que a cada execução somente será calculado um pedido. 
O cardápio da lanchonete segue o padrão abaixo:
'''
pedido = True
val_tot = 0
cont = 0
#cardapio = []
while(pedido):
	print("[Seu pedido fora aberto !]")
	cod = input("\nDigite o código do produto que deseja: ")

	if (cod == "100"):
		print("Produto selecionado: Cachorro-Quente\n")
		qtd_0 = int(input("Digite a quantidade do produto que deseja: "))
		val_0 = 5.00
		result = qtd_0 * val_0
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Cachorro-Quente")#
		
		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False
	
	elif (cod == "101"):
		print("Produto selecionado: Bauru Simples\n")
		qtd_1 = int(input("Digite a quantidade do produto que deseja: "))
		val_1 = 11.90
		result = qtd_1 * val_1
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Bauru Simples")#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False

	elif (cod == "102"):
		print("Produto selecionado: Bauru com Ovo\n")
		qtd_2 = int(input("Digite a quantidade do produto que deseja: "))
		val_2 = 7.90
		result = qtd_2 * val_2
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Bauru com Ovo")#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False

	elif (cod == "103"):
		print("Produto selecionado: Hamburguer\n")
		qtd_3 = int(input("Digite a quantidade do produto que deseja: "))
		val_3 = 5.50
		result = qtd_3 * val_3
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Hamburguer")#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False

	elif (cod == "104"):
		print("Produto selecionado: Cheeseburguer\n")
		qtd_4 = int(input("Digite a quantidade do produto que deseja: "))
		val_4 = 6.00
		result = qtd_4 * val_4
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Cheeseburguer")#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False

	elif (cod == "105"):
		print("Produto selecionado: Suco\n")
		qtd_5 = int(input("Digite a quantidade do produto que deseja: "))
		val_5 = 5.90
		result = qtd_5 * val_5
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Suco")#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False

	elif (cod == "106"):
		print("Produto selecionado: Refrigerante\n")
		qtd_6 = int(input("Digite a quantidade do produto que deseja: "))
		val_6 = 12.90
		result = qtd_6 * val_6
		val_tot = val_tot + result#
		cont += 1#
		cardapio[cont] = cardapio.append("Refrigerante")#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			pedido = False

	else:
		print("Opção inválida!\nEstá opção não existe no cardápio!")

cont_cf = 0
print("[CUPOM FISCAL]\n")
for cont_cf in cardapio:
	print("Quantidade: " + cont + "Un X " + cont_cf)
	print("O valor total a ser pago será: R${:.2f}".format(val_tot))