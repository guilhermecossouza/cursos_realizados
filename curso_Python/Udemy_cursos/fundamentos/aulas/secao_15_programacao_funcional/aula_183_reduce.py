from functools import reduce

pessoas = [
    {"nome": "Pedro", "idade": 11},
    {"nome": "Mariana", "idade": 18},
    {"nome": "Arthur", "idade": 26},
    {"nome": "Rebeca", "idade": 6},
    {"nome": "Thiago", "idade": 19},
    {"nome": "Gabriela", "idade": 17},
]

soma_idades = reduce(lambda idade, p: idade + p["idade"], pessoas, 0)
print(soma_idades)
print("-="*30)

# menores_idade = filter(lambda idade: idade["idade"] < 18, pessoas)
# print(list(menores_idade))

soma_idade_menores = reduce(lambda idades, p: idades + p["idade"],
                            filter(lambda menores: menores["idade"] < 18, pessoas), 0)
print(soma_idade_menores)
