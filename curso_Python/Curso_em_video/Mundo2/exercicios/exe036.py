'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
from math import floor
valor_casa = float(input("Informe o valor da casa R$"))
salario_comprador = float(input("Informe seu salário R$"))
parcelas = int(input("Em quantas parcelas dejeja pagar: "))

max_valor_parcela = salario_comprador - ((salario_comprador * 30) / 100)
valor_parcela = valor_casa / parcelas
if valor_parcela <= max_valor_parcela:
    print("O Emprestimo foi aprovado! Com {} parcelas no valor R${:.2f}".format(parcelas, valor_parcela))
else:
    qtd_parcelas_sugerida = valor_casa / max_valor_parcela
    qtd_parcelas_sugerida = floor(qtd_parcelas_sugerida) + 1
    valor_parcela_sugerido = valor_casa / qtd_parcelas_sugerida
    print("Sugerimos {} parcelas, no valor dê R${:.2f}".format(qtd_parcelas_sugerida, valor_parcela_sugerido))
    
