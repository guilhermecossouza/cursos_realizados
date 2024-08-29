"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior(lista_numeros):
    lista_numeros.sort()
    print(f"O maior número informado é {lista_numeros[len(lista_numeros) - 1]}")

numeros = list()
numero = int(input("Deseja cadastrar quantos números "))
while numero >= 1:
    n = int(input("Informe um númeor: "))
    numeros.append(n)
    numero -= 1
maior(numeros)