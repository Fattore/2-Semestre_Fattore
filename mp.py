#encoding: utf-8
'''
Faça um algoritmo que calcule a media ponderada das notas de 3 provas. 
A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. 
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. 
A nota para aprovação deve ser igual ou superior a 6.0 pontos.
'''
n1 = float(input("Digite a nota da 1º prova: "))
n2 = float(input("Digite a nota da 2º prova: "))
n3 = float(input("Digite a nota da 3º prova: "))

p1 = 1.0
p2 = 2.0
#p3 = 3 nenhuma delas tem peso 3

mp = (n1 * p1 + n2 * p1 + n3 * p2) / (p1 + p1 + p2) # calculo de media ponderada

if mp >= 6.0:
	print("Aluno aprovado com média: {:.2f}".format(mp))
else:
	print("Aluno reprovado com média: {:.2f}".format(mp))