''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''
from random import randint
from time import sleep
print("-="*30)
print("O carro está passando")
sleep(1.5)
velocidade_carro = randint(0, 100)
print("O carro passou, velocidade? {}Km/h".format(velocidade_carro))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80)  * 7.00
    print("A velocidade foi de {}Kn/h, sua multa será de R${:.2f}".format(velocidade_carro, multa))
else:
    print("O carro passou abaixo da velocidade permitida.")
