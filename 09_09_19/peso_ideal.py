#encoding: utf-8
'''
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
utilizando as seguintes formulas (onde h corresponde a altura): `
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7

'''
altura = float(input("Digite a sua altura: "))
sexo = input("Você é Homem ou Mulher ? ").capitalize()

if sexo == "Homem" or sexo == "H":
	homem = (72.7 * altura) - 58
	print("Seu peso ideal é: {:.2f}".format(homem)) #{:.2f} é para definir as casas decimais
elif sexo == "Mulher" or sexo == "M":
	mulher = (62.1 * altura) - 44.7
	print("Seu peso ideal é: {:.2f}".format(mulher))
else: 
	print("Opção Invalida")
