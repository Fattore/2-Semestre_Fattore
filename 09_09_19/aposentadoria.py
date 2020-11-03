#encoding: utf-8
'''
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. 
As condições para aposentadoria são:• Ter 65 anos ou mais;
  • Ou ter trabalhado pelo menos 35 anos,
  • Ou ter pelo menos 60 anos e trabalhado pelo menos 35 anos.
'''
idade = int(input("Digite sua idade: "))
tmp_trab = int(input("Digite o tempo de serviço: "))

if (idade >= 65) or (idade == 60 and tmp_trab >= 35):
	print("Você pode se aposentar!\nVocê tem atualmente: {} anos.\nSeu tempo de serviço atual é: {} anos.".format(idade,tmp_trab))
else:
	print("Você não está dentro das regras de aposentadoria")
