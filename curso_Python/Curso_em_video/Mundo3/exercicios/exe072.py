'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20)
e mostrá-lo por extenso'''

numeros_por_extensos = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    )

while True:
    numero = int(input("Informe um número de 0 à 20: "))
    if 0 <= numero <= 20:
        print(f"Número escolhido foi {numero}, o mesmo por extenso {numeros_por_extensos[numero]}")
    else:
        print("Número incorreto!")
        break