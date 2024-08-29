'''
Crie um programa onde o usuário possa digitar
sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares
em ordem crescente.
'''
listas = [[], []]
for contador in range(7):
    numero  = int(input("infrome um valor inteiro: "))
    if numero % 2 == 0:
        listas[0].append(numero)
    else:
        listas[1].append(numero)

listas[0].sort()
listas[1].sort()

print(f"Números pares {listas[0]}")
print(f"Números impares {listas[1]}")