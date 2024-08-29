lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {"nome": "João", "idade": 31},
    {"nome": "Maria", "idade": 37},
    {"nome": "José", "idade": 26}
]

nomes = list(map(lambda nome: nome["nome"], lista_2))
print(nomes)

idade = tuple(map(lambda idade: idade["idade"], lista_2))
print(idade)

sum_idade = map(lambda idade: idade["idade"], lista_2)
print(sum(sum_idade))

# Desafio


def set_fase(lista):
    return f"{lista['nome']} tem {lista['idade']} anos"


frase = map(set_fase, lista_2)
print(list(frase))

frase_2 = map(
    lambda frase: f"{frase['nome']} tem {frase['idade']} anos.", lista_2)
print(list(frase_2))
