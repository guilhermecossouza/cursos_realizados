'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''
import random
valores = []
maior = 0
menor = 0
while len(valores) <= 4:
    numero = random.randint(0, 100000)    
    if len(valores) == 0:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
    valores.append(numero)
    

valores.sort()

print(valores)
print(f"O maior número informado foi {maior}, de outra forma maoir {valores[4]}")
print(f"O menor valir informado foi o {menor}, de outra forma o menor valor {valores[0]}")



