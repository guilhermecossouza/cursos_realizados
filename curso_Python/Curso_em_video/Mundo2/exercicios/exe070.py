'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
total_valor = 0
valor_acima_de_mil = 0
produto_menor_valor = 0
strNomeProduto = ""
contador = 0
while True:
    continuar = str(input("Deseja passar as compras? [S/N] ")).upper().strip()   
    match continuar:
        case "S":
            nome_produto = str(input("Nome do produto: ")).lower().strip()
            preco_produto = float(input("Digite o valor do produto R$"))
            total_valor += preco_produto
            if preco_produto > 1000.00:
                valor_acima_de_mil += 1
            
            if contador == 0:
                produto_menor_valor = preco_produto
            else:
                if preco_produto < produto_menor_valor:
                    strNomeProduto = nome_produto
                    produto_menor_valor = preco_produto
        case "N":
            break
    contador += 1

print(f"O valor total da compra R${total_valor:.2f}")
print(f"total de produtos com valor acima de $1000,00 : {valor_acima_de_mil}")
print(f"Nome do produto com o menor valor: {nome_produto}")


