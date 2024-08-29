# podemos criar o dicionário de dias formas
# 1° dicionario = dict()
# 2° dicionario = {}
# podemos também ter um dicionário dentro do outro
pessoa = {"nome": "Ana", "idade": 38, "aulas": ["Portugues", "ingles"]}
print(type(pessoa))
print(dir(dict))
print(len(pessoa))
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["aulas"])
print(pessoa["aulas"][0])
print(pessoa["aulas"][1])
# para ver as chaver do docionario
print(pessoa.keys())
# para pegar somente os valores do docionario
print(pessoa.values())
# para pegar a chave e valor do dicionário
print(pessoa.items())
print(type(pessoa.items()))
# também pode buscar um valor usando o get
print(pessoa.get("idade"))
# caso a propriedade dad busca não existe ex: pessoa.get("carros"), você tem a possibilidade de retornar uma valor dafault
# pode ser assim ou print(pessoa.get("carros", "carro Não existe")) ou vazio print(pessoa.get("carros", [])) ou print(pessoa.get("carros", ""))
print(pessoa.get("carros", ["carro Não existe"]))
