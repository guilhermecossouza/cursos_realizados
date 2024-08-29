''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''
maior_peso = 0
menor_peso = 0
for contador in range(0, 5):
    peso = float(input("Informe seu peso: "))
    if contador == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print("Maior peso foi {:.2f} e o menor peso {:.2f}".format(
    maior_peso, menor_peso))
