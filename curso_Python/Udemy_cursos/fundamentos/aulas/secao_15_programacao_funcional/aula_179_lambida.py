compras = (
    {"quantidaade": 2, "preco": 10},
    {"quantidaade": 3, "preco": 20},
    {"quantidaade": 5, "preco": 14},
)

totais = tuple(
    map(lambda compra: compra["quantidaade"] * compra["preco"], compras))

print(f"Preços totais: {totais}")
print(f"Toral geral: {sum(totais)}")
