produto = {"nome": "Caneta Chic", "preco": 14.90,
           "importada": True, "estoque": 793}

for chave in produto:  # por padrão ele vai imprimir as chaves da dicionário
    print(chave)

print("=-"*40)
for chave in produto.keys():  # podemos imprimir pela chave usando o metodo keys()
    print(chave)

print("-="*40)
for valor in produto.values():  # podemos imprimir os valores do docionário usando a função values()
    print(valor)

print("-="*40)
for chave, valor in produto.items():  # podemos imprimir as chaves e valores do dicionário usando a função items()
    print(f"{chave} = {valor}")

print("-="*30)
# OBS: Os valores usados nas variáver dentro do laço for ficam disponíveis com o ultimo vaor passado no for
print(f"{chave} = {valor}")
