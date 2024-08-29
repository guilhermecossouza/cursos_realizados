# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
from math import sqrt

numero = int(input("Digite um número inteiro:"))
print("O dobro do número {} é {}".format(numero, (numero * 2)))
print("O trípulo do número {} é {}".format(numero, (numero * 3)))
print("A raiz quadrada do número {} é {:.2f}". format(numero, sqrt(numero)))
