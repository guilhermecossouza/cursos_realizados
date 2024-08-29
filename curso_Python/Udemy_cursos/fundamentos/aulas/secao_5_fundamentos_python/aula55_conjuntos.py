# Conjunto ingles : set
a = {1, 2, 3}
print(a)
print(type(a))
# -> irá criar um set de guilherme ou seja: g,u,i,l,h,e,r,m,e
a = set("guilherme")
# OBS: Não garente a ordenação
print(a)
# O set aceita operadores de mmbro
print("g" in a, 4 not in a)

# True ou False?
# será true porque os mesmos elementos contem nos dois
# A ordem não importa
# E os elementos duplicados seram removidos
print({1, 2, 3} == {3, 2, 1, 3})
print({1, 2, 3} == {3, 2, 1, 3, 4})  # False
# OPERADORES
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))  # vai unir os elementos e ignorar os valores repetidos
print(c1.intersection(c2))  # vai mostrar os valores que se repetem na união
# realizado de fato alterando o set
#c1.update(c2)  # -> altera o elemento c1
print(c1)
# verificar se uma elemento é subconjunto de outro
print(c1 <= c2)
print(c1 >= c2)
print({1, 2, 3} - {2}) #-> diferença de dois conjuntos
