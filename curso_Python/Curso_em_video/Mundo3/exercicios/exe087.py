'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''

lista = list()
listb = list()


for i in range(0, 3):  
    for j in range(0, 3):  
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

    lista.append(listb[:])  
    listb.clear()

for l in lista:
    print(l)


soma = 0

for i in range(3):
    for j in range(3):
        if lista[i][j] % 2 == 0:
            soma += lista[i][j]

print(f"Soma dos valores pares: {soma}.")

soma_coluna = 0

for i in range(3):
    for j in range(3):
        if j == 2:  
            soma_coluna += lista[i][j]
print(f"Soma terceira coluna: {soma_coluna}.")

maior = 0

for i in range(3):
    for j in range(3):
        if i == 1: 
            if lista[i][j] > maior:
                maior = lista[i][j]
print(f"Maior valor da segunda linha: {maior}.")