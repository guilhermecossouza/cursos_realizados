# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de R$ 15%.
salario = float(input("Digite o seu salário R$"))
print(salario)
if salario > 1250.00:
    novo_salaro = salario + ((salario * 10) / 100)
    print("Salário digitado foi R${:.2f}, e seu aumento será de 10 e seun novo salário R${:.2f}".format(
        salario, novo_salaro))
else:
    novo_salaro = salario + ((salario * 15) / 100)
    print("Salário digitado foi R${:.2f}, e seu aumento será de 15 e seun novo salário R${:.2f}".format(
        salario, novo_salaro))
