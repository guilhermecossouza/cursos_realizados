'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''
list_numero = []
for contador in range(0, 4):
    list_numero.append(int(input("Informe quatro valores inteiros: ")))

tupla_numero = tuple(list_numero[:])
list_numero = []

for numeros in tupla_numero:
    if numeros % 2 == 0:
        list_numero.append(numeros)
tupla_pares = tuple(list_numero[:])
list_numero = []

print(f"Quantas vezes apareceu o número 9: {tupla_numero.count(9)} vezes")
if 3 in tupla_numero:
    print(f"Em que posição foi digitado o primeiro valor 3: {tupla_numero.index(3)} posição")
else:
    print("O número 3 não foi informado.")
print(f"Os números pares foram: {tupla_pares}")

