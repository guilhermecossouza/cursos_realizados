# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input("Digite o seu nome: ")).lower().strip().split()
'''if int(nome.find("silva")) > 0:
    print("Seu nome possui a palavra silva.")
else:
    print("Seu nome não possui a palavra silva")'''

'''if "silva" in nome:
    print("Seu nome possui a palavra silva.")
else:
    print("Seu nome não possui a palavra silva")'''

print("silva" in nome)

