# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior; os dois são iguais
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
if numero1 > numero2:
    print("O primeiro número diditado é maior")
elif numero2 > numero1:
    print("O segundo número diditado é maior")
else:
    print("Não existe valor maior, os dois são iguais")
