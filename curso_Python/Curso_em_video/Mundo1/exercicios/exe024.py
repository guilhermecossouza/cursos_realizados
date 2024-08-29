# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
cidade = str(input("Digite o nome da cidade: ")).upper().strip().split()
print(cidade[0] == "SANTO")
