pessoa = {"nome": "Ana", "idade": 38, "aulas": ["Portugues", "ingles"]}
print(pessoa)
pessoa["idade"] = 44
print(pessoa)
pessoa["aulas"].append("matemática")
print(pessoa)
#pop lê o item e retira o item do dicionario
print(pessoa.pop("idade"))
print(pessoa)
#atualizando a lisat
pessoa.update({"idade": 50, "sexo": "F"})
print(pessoa)
#deletando item da lista
del pessoa["aulas"]
print(pessoa)
#limpar o dicionário
pessoa.clear()
print(pessoa)