# Crie um programa que leia o nome completo de uma pessoa:
#nome = str(input("Digite seu nome completo: \n")).strip()
nome = "Guilherme Costa de Souza"
print("Nome com letras maiúsculas: {}".format(nome.upper()))
print("Nome com letras minusculas: {}".format(nome.lower()))
print("Quantidade de caracters sem espaços: {}".format(len(nome.replace(" ", ""))))
nome = nome.split()
print("Primeiro nome {}, ele tem {} letras".format(nome[0], len(nome[0])))
