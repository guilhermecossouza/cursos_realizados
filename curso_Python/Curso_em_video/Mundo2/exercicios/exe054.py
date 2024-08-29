''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
import datetime
maior = 0
menor = 0
for contador in range(1, 3):
    ano = int(input("Digte o ano de seu nascimento: "))
    if ano <= datetime.date.today().year:
        idade = datetime.date.today().year - ano
        if idade >= 18:
            maior += 1
        else:
            menor += 1

print("Tivemos {} maiores de idade e {} menores de idade".format(maior, menor))
