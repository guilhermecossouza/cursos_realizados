# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar
valor = float(input("Qual valor possui na sua carteira R$"))
print("Você possui R${:.2f}, com esse valor pode comprar US${:.2f}".format(
    valor, (valor / 4.79)))
print("Você possuirá um troco de R${:.2f}".format((valor % 4.79)))
