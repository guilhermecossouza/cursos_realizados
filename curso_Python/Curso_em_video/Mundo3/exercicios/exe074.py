'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''
import random
list_numeros = []

for contador in range(5):
    list_numeros.append(random.randint(0, 1000000))
tupla_numero = tuple(list_numeros)

maior = 0
menor = 0
#pegar o maior e o menor
# for posicao, num_sorteados in enumerate(tupla_numero):
#     if num_sorteados < menor:
#         menor = posicao
#     elif num_sorteados > maior:
#         maior = posicao
sorted(tupla_numero)
print(tupla_numero)
print(tupla_numero[0])
print(tupla_numero[4])

