import random

numero_informado = -1
numero_secreto = random.randint(0, 0)

while numero_informado != numero_secreto:
    numero_informado = int(input("Informe um número: "))

print(f"Numero secreto {numero_secreto} foi encontrado!")
