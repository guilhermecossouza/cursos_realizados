# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Informe seu salário R$"))
valor_acrescentado = (salario * 15) / 100
print("Salário atual de R${:.2f}, com 15% de aumento será R${:.2f}".format(
    salario, (salario + valor_acrescentado)))
