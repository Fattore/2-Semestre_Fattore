#encoding: utf-8
'''
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. 
Considere que a cada execução somente será calculado um pedido. 
O cardápio da lanchonete segue o padrão abaixo:
'''
pedido = True
cont = 0
cod_ar = ["100","101","102","103","104","105","106"]#
cardapio_ar = ["Cachorro-Quente","Bauru Simples","Bauru com Ovo","Hamburguer","Cheeseburguer","Suco","Refrigerante"]#
val_ar = [5.00,11.90,7.90,5.50,6.00,5.90,12.90]#
qtd_ar = [0] * 20#
tot_ar = [0] * 20#

print("[Seu pedido fora aberto !]")
while(pedido):
	cod = input("\nDigite o código do produto que deseja: ")

	if (cod == cod_ar[0]):
		print("Produto selecionado: Cachorro-Quente\n")
		qtd_0 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_0 * val_ar[cont]
		tot_ar[cont] = tot_ar[cont] + result# 
		qtd_ar[cont] = qtd_0#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			cont += 1#
			pedido = True
		else:
			loop_cupom = "{}  {}\n{}Un x  {} R$: {};;".format(cod,cardapio_ar[cont],qtd_ar[cont],val_ar[cont],result)
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			if (cont != 0): 
				print(loop_cupom * cont)
			print(loop_cupom)
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar[cont]))
			pedido = False

	elif (cod == cod_ar[1]):
		print("Produto selecionado: Bauru Simples\n")
		qtd_1 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_1 * val_ar[cont]
		tot_ar[cont] = tot_ar[cont-1] + result# 
		qtd_ar[cont] = qtd_1#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			cont += 1#
			pedido = True
		else:
			loop_cupom = "{}  {}\n{}Un x  {} R$: {};;".format(cod,cardapio_ar[cont],qtd_ar[cont],val_ar[cont],result)
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			if (cont != 0): 
				print(loop_cupom * cont)
			print(loop_cupom)
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar[cont]))
			pedido = False

	elif (cod == cod_ar[2]):
		print("Produto selecionado: Bauru com Ovo\n")
		qtd_2 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_2 * val_ar[2]
		tot_ar = sum(tot_ar + result)# 
		qtd_ar = qtd_ar.append(qtd_2)#
		cont += 1#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			print("%d  %d\n%dUn x  %d R$:%d;;" % (cod_ar[0],cardapio_ar[0],qtd_ar[0],val_ar[0],val_ar[0]))
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar))
			pedido = False

	elif (cod == cod_ar[3]):
		print("Produto selecionado: Hamburguer\n")
		qtd_3 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_3 * val_ar[3]
		tot_ar = sum(tot_ar + result)# 
		qtd_ar = qtd_ar.append(qtd_3)#
		cont += 1#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			print("%d  %d\n%dUn x  %d R$:%d;;" % (cod_ar[0],cardapio_ar[0],qtd_ar[0],val_ar[0],val_ar[0]))
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar))
			pedido = False

	elif (cod == cod_ar[4]):
		print("Produto selecionado: Cheeseburguer\n")
		qtd_4 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_4 * val_ar[4]
		tot_ar = sum(tot_ar + result)# 
		qtd_ar = qtd_ar.append(qtd_4)#
		cont += 1#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			print("%d  %d\n%dUn x  %d R$:%d;;" % (cod_ar[0],cardapio_ar[0],qtd_ar[0],val_ar[0],val_ar[0]))
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar))
			pedido = False

	elif (cod == cod_ar[5]):
		print("Produto selecionado: Suco\n")
		qtd_5 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_5 * val_ar[5]
		tot_ar = sum(tot_ar + result)# 
		qtd_ar = qtd_ar.append(qtd_5)#
		cont += 1#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			print("%d  %d\n%dUn x  %d R$:%d;;" % (cod_ar[0],cardapio_ar[0],qtd_ar[0],val_ar[0],val_ar[0]))
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar))
			pedido = False

	elif (cod == cod_ar[6]):
		print("Produto selecionado: Refrigerante\n")
		qtd_6 = int(input("Digite a quantidade do produto que deseja: "))
		result = qtd_6 * val_ar[6]
		tot_ar = sum(tot_ar + result)# 
		qtd_ar = qtd_ar.append(qtd_6)#
		cont += 1#

		opcao = input("Deseja pedir outra coisa: ").capitalize()
		if (opcao == "Sim" or opcao == "S"):
			pedido = True
		else:
			print("\n[CUPOM FISCAL]\nITEM CÓDIGO  DESCRIÇÃO\nQTD.  UN.  VL.UNIT.( R$)  VAL.ITEM.( R$)\n________________________________________")
			print("%d  %d\n%dUn x  %d R$:%d;;" % (cod_ar[0],cardapio_ar[0],qtd_ar[0],val_ar[0],val_ar[0]))
			print("________________________________________\nTOTAL R$ {:.2f}".format(tot_ar))
			pedido = False

	else:
		print("Opção inválida!\nEstá opção não existe no cardápio!")
