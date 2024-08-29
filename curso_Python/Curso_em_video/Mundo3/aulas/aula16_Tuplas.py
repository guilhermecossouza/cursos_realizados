# As tuplas são imutavés
# depois da tupla atribuida não pode ser alterada
# tupla = "hambúrguer", "Suco", "Pizza", "pudim" -> pode ser criada assim também
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata frita")
print("{:^50}".format("Maneiras de exibir valores da tupla"))
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

print(len(lanche))  # mostra quantos elementos há dentro da tupla lanche = 5
print(sorted(lanche))  # vao roganizar a tupla lanche


print("-="*50)
for comida in lanche:
    print(f"Eu vou comer {comida}.")
print("comi pra caramba!")
print("-="*50)
for contador in range(0, len(lanche), 2):
    print(f"Vou comer {lanche[contador]}")
print("-="*50)
for posicao, comida in enumerate(lanche):
    if posicao == 1:
        print(f"Vou beber {comida}, que está na posição n°{posicao}")
    else:
        print(f"Vou comer {comida}, que está na posição n°{posicao}")
print("-="*50)
for comida in lanche:
    match comida:
        case "Suco":
            print(f"Eu vou beber {comida}.")
        case _:
            print(f"Eu vou comer {comida}.")
print("-="*50)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # vai realizar a união entre as tuplas
print(a)
print(b)
print(c)
print(c.count(5))
print(c.count(4))
print(c.count(9))
# vai mostrar a posição do elemento passado no index vai pegar a primeira ocorrência
print(c.index(8))
print(c.index(5, 1))  # vai mostrar a posição apartir da posição 1
print("-="*50)
# A tupla pode ter vários tipos diferentes
pessoa = ("Guilherme", 39, "M", 80.75)
print(pessoa)
del (pessoa)  # Apaga da memória pessoa
# del (pessoa[0])  # ERRO NÃO PODE APAGAR UM ELEMENTO DA LISTA [ LISTA É IMUTÁVEL ]
# print(pessoa)  # Deu erro pessoa não declarada
