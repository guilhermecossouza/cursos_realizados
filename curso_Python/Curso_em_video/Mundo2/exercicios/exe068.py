''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''
import random
import time

numero_vitorias = 0
while True:
    print("Vamos jogar par ou impar!")
    opcao_jogador = str(input("Você escolhe par ou impar? ")).upper().strip()
    numero_jogador = int(input("Digite um valor: "))    
    numero_computador = random.randint(1, 10)  
    match opcao_jogador:
        case "PAR":
            opcao_computador = "IMPAR"
        case "IMPAR":
            opcao_computador = "PAR"
    print("Vamos lá?")
    time.sleep(1)
    print("Computador {}".format(opcao_computador))
    time.sleep(1)
    print("jogador {}".format(opcao_jogador))
    time.sleep(1)
    soma = numero_jogador + numero_computador
    if soma % 2 == 0 and opcao_jogador == "PAR":
        print("Resultado:{}".format(soma))
        numero_vitorias += 1
        print("Vitória! parabéns!")
    elif soma % 3 == 0 and opcao_jogador == "IMPAR":
        print("Resultado:{}".format(soma))
        numero_vitorias += 1
        print("Vitória! parabéns!")
    else:
        print("Resultado:{}".format(soma))
        print("Dettota!")
        print("Você teve {} Vitórias".format(numero_vitorias))
        break
