# Faça um programa que mostre na tela
# Uma contagem regressiva para o estouro e fogos de artifício,
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# USANDO LOOP AGORA
import time
for contador in range(10, -1, -1):

    if contador == 0:
        print("BUM!BUM!BUM!BUM!BUM!")
    else:
        print(contador)
        time.sleep(1)
