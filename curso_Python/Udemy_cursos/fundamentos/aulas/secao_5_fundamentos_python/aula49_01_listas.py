lista = []  # Pode ser criada assim ou assim lista = list()
print(dir(lista))
lista.append(1)  # adiconando elemento
lista.append(5)
print(len(lista))
print(lista.__len__())
print(lista)

# incializando a lista com valores OBS: Não é uma boa prática usar com tipos destintos dentro de uma lista
nova_lista = [1, 5, "Ana", "Bia"]
print(nova_lista)
nova_lista.remove(5)  # Remove um item da lista
print(nova_lista)
nova_lista.reverse()  # revertendo as posições da lista
print(nova_lista)
