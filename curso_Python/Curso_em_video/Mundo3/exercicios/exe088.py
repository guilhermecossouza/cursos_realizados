'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
import random
lista_todos_jogos = []
lista_jogo = []
qtd_jogos = int(input("Quantos jogos deseja gerar: "))
for jogo in range(qtd_jogos):
    for contador in range(6):
        numero = random.randint(1, 60)
        if lista_jogo.count(numero) == 0:
            lista_jogo.append(numero)

    lista_jogo.sort()
    lista_todos_jogos.append(lista_jogo)
    lista_jogo = []

for i, l in enumerate(lista_todos_jogos):
    print(f"Jogo {i + 1}: {l}")    





    