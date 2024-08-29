# podemos declarar o dicionário dessas duas formas
# pessoas = {}
# pessoas = dict()

pessoas = {"nome": "Guilherme", "idade": 40, "sexo": "M"}
print(pessoas["nome"])
print(pessoas["idade"])
print(pessoas["sexo"])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())  # vai printar as chaves -> nome, idade, sexo
# vai printar as chaves -> nome, idade, sexo e os valores guilherme, 40, M
print(pessoas.items())
print(pessoas.values())  # vai printar os valores guilherme, 40, M

print("-=" * 50)
for key in pessoas.keys():
    print(key)

print("-=" * 50)
for value in pessoas.values():
    print(value)

print("-=" * 50)
for key, value in pessoas.items():
    print(f"chave: {key} e valor: {value}")

print("-=" * 50)
del pessoas["sexo"]
print(pessoas)

print("-=" * 50)
pessoas["nome"] = "Gustavo"  # alterando os valor
print(pessoas)

print("-=" * 50)
pessoas["peso"] = 98.5
print(pessoas)

# print("-=" * 50)
# brasil = list()
# estado1 = {"uf": "Minas Gerais", "sigla": "MG"}
# estado2 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)1
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]["uf"])
# print(brasil[1]["sigla"])

print("-=" * 50)
estado = dict()
brasil = list()
for contador in range(0, 1):
    estado["uf"] = str(input("Unidade Federativa: ").strip())
    estado["sigla"] = str(input("Sigla do estado: ").strip())
    brasil.append(estado.copy())

for e in brasil:
    for chave, valor in e.items():
        print(f"O {chave} tem valor de {valor}")
