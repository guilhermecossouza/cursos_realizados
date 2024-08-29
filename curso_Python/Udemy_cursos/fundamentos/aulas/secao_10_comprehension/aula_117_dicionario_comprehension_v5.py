# podemos usar ua fstring
# dicionario = {f"Dobro de {i}": i * 2 for i in range(10) if i % 2 == 0}
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)
for chave, valor in dicionario.items():
    print(f"O dobo de {chave} é {valor}")
