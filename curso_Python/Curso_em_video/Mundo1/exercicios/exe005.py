# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
numero = int(input("Digite um número inteiro: "))
print("O antecessor do número {} é {}".format(numero, (numero - 1)))
print("O sucessor do número {} é {}".format(numero, (numero + 1)))