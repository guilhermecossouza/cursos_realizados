# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input("Digite o valor do produto R$"))
desconto = (preco * 5) / 100
print("O valor do produto informado R${:.2f}, com 5% de desconto vai para R${:.2f}".format(
    preco, (preco - desconto)))
