"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""

def contador(ini, fim, passo):
    for c in range(ini, fim, passo):
        print(f"{c}", end=" ")
    print("")
    print("-="* 30)


i = int(input("Informe o início da contagem; "))
f = int(input("Informe o fim da contagem: "))
p = int(input("informe o passo da contagem: "))
contador(1, 11, 1)
contador(10, -1, -2)
contador(i, f + 1, p)