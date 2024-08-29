# passando um tupla para o format e lista
print("Nome: {}, Idade: {}".format("guilherme", 39))  # NOrmal
# print("Nome: {}, Idade: {}".format(("guilherme", 39))) #Erro
print("Nome: {}, Idade: {}".format(*("guilherme", 39)))  # Erro
pessoa_lista = ["guilherme", 39]
print("{}, {}".format(*pessoa_lista))
