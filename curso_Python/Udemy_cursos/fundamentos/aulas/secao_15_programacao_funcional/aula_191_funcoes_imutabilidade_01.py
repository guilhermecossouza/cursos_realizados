from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]
# Imutabilidade
# ele vai gerar uma nova lista com os valores ordenado e não vai alterar a lista original
print(sorted(valores))
print(valores)

# nenhuma das funções abaixo irá alterar o valor original da lista
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(list(reversed(valores)))


# valores.sort()  # nesse caso ele irá alterar a lista passada
# print(valores)
