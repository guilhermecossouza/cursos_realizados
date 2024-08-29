# Crie um programa que faça o computador jogar Jokenpô com você.
'''
Regras computador:
1 - pedra
2 - papel
3 - tesoura
'''
import random
print("ESCOLHA: \n1 - pedra \n2 - papel \n3 - tesoura")
jogador = int(input("Digite sua escolha: "))
if jogador == 1:
    escolha_jogador = "pedra"
elif jogador == 2:
    escolha_jogador = "papel"
else:
    escolha_jogador = "tesoura"

computador = random.randint(1, 3)
if computador == 1:
    escolha_computador = "pedra"
elif computador == 2:
    escolha_computador = "papel"
else:
    escolha_computador = "tesoura"

if jogador == computador:
    print("Deu empate! jogar escolheu {} e computador escolheu {}".format(
        escolha_jogador, escolha_computador))
else:
    match jogador:
        case 1:
            if computador == 2:
                print("Derrota! O computador escolheu {} e jogador escolheu {}".format(
                    escolha_computador, escolha_jogador))
            else:
                print("Vitória! O computador escolheu {} e jogador escolheu {}".format(
                    escolha_computador, escolha_jogador))
        case 2:
            if computador == 1:
                print("Vitória! O computador escolheu {} e jogador escolheu {}".format(
                    escolha_computador, escolha_jogador))
            else:
                print("Derrota! O computador escolheu {} e jogador escolheu {}".format(
                    escolha_computador, escolha_jogador))
        case 3:
            if computador == 1:
                print("Derrota! O computador escolheu {} e jogador escolheu {}".format(
                    escolha_computador, escolha_jogador))
            else:
                print("Vitória! O computador escolheu {} e jogador escolheu {}".format(
                    escolha_computador, escolha_jogador))
