# operadores membro
lista = [1, 2, 3, "Ana", "Carla"]
print(2 in lista)  # True
print("Ana" not in lista)  # False
print("Zaca" not in lista)  # True
# operadores de indentidade
x = 3
y = x
z = 3
print(x is y)  # True
print(y is z)  # True
print(x is not z)  # False

print("-="*30)
lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)
