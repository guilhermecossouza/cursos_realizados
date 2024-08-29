"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
import random

def sorteia():
    numeros = list()
    for c in range(5):
        n = random.randint(0, 100000)
        if numeros.count(n) == 0:
            numeros.append(n)
    return numeros

def soma_par(lista):
    soma = 0
    for numoro in lista:
        if numoro % 2 == 0:
            soma += numoro
    return soma

numeros = sorteia()
resultado = soma_par(numeros)

print(f"lista de números sorteados: {numeros}")
print(f"A soma dos numros pares sorteados: {resultado}")




