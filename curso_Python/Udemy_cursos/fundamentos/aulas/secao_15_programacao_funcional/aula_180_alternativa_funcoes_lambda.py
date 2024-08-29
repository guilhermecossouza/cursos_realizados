compras = (
    {"quantidaade": 2, "preco": 10},
    {"quantidaade": 3, "preco": 20},
    {"quantidaade": 5, "preco": 14},
)


# def calc_preco_total(compra):
#     return compra["quantidaade"] * compra["preco"]

# podemos fazer funcções assim sem ferir a regra do pep 8
def calc_preco_total(compra): return compra["quantidaade"] * compra["preco"]

# totais = tuple(
#     map(lambda compra: compra["quantidaade"] * compra["preco"], compras))


# podemos passar também funções para o map
totais = map(calc_preco_total, compras)

print(f"Preços totais: {totais}")
print(f"Toral geral: {sum(totais)}")
