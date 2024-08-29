'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = []

while True:
    numero = int(input("Informe um valor inteiro, para sair digite [999]: "))
    if numero == 999:
        break
    else:
        lista_numeros.append(numero)

for num in lista_numeros:
    if num % 2 == 0:
        lista_numeros_pares.append(num)
    else:
        lista_numeros_impares.append(num)

print(f"lista números informados: {lista_numeros}")
print(f"lista números pares: {lista_numeros_pares}")
print(f"Lista números impares: {lista_numeros_impares}")
