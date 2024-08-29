# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente
# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome = str(input("Digite seu nome: "))
nome = nome.split()
print("Seu primairo nome é: {}".format(nome[0]))
print("Seu último nome é: {}".format(nome[len(nome) - 1]))
print("Seu último nome é: {}".format(nome[-1]))
