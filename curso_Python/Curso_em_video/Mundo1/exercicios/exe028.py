# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
from random import randint
print("-="*30)
print("{:^30}".format("Jogo da adivinhação"))
print("-="*30)
print("{}".format("Estou pensando em um número"))
sleep(1.5)
computador = randint(0, 5)
print("pensei...")
print("-="*30)
print(computador)
print("-="*30)
usuario = int(input("Digite um número de [0 à 5]: "))
if computador == usuario:
    print("Parabéns! Você ganhou, pensei no número {}".format(computador))
else:
    print("Você errou! o número que pensei foi {}.".format(computador))
