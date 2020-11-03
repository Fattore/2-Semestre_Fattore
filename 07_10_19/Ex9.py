#coding: utf-8
"""Escreva um programa que solicite ao usuário um ano e imprima o calendário desse ano. 
Utilize o método abaixo para calcular o dia da semana:"""
def semana (dia,mes,ano):
    f=ano+dia+3*(mes-1)-1;
    if(mes<3):
        ano=ano-1
    else:
        f-=(int)(0.4*mes+2.3);
    f+=(int)(ano/4)-(int)((ano/100+1)*0.75);
    f%=7;
    return(f);

dia = int(input("Digite o dia de sua escolha: "))
mes = int(input("Digite o mes de sua escolha: "))
ano = int(input("Digite o ano de sua escolha: "))

print(semana(dia,mes,ano))
