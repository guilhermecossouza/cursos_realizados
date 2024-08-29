tupla = tuple()
tupla = ()
# print(type(tupla))
# print(dir(tupla))
# print(help(tuple))

# -> declarando dessa forma não vai ser reconhecido com uma tupla e sim como uma string
tupla = ("um")
print(type(tupla))  # -> String
# para atribuir um só elemento deve-se adicionar um virgula ao final.
tupla = ("um", )  # -> Agora sim é uma tuple
print(type(tupla))  # -> tuple
# Acessando o elemento da lista tupla[0]
cores = ("verde", "amarelo", "azul", "branco", "azul", "azul")
print(cores[0])
print(cores[1])
print(cores[-1])
print(cores[1])
# podemos usar fatiamento
print(cores[1:])

print(cores.index("azul"))
print(cores.count("azul"))
print(len(cores))
