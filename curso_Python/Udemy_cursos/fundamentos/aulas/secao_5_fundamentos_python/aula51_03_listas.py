lista = ["Ana", "Lia", "Rui", "Paulo", "Dani"]
print(lista[1: 3])
print(lista[1: -1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
lista.reverse()
print(lista)
print(dir(lista))
del lista[2]
print(lista)
del lista[1:]
print(lista)
