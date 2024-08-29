"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""
import random
import time
import operator
jogadores = {
    "jogador_um": random.randint(1, 6),
    "jogador_dois": random.randint(1, 6),
    "jogador_tres": random.randint(1, 6),
    "jogador_quatro": random.randint(1, 6),
}

for key, value in jogadores.items():
    print(f"O jogador {key}, tirou {value}")
    time.sleep(1)

rank = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
for item, valor in enumerate(rank):
    print(f"Em {item + 1} lugar ficou o {valor[0]}, com o valor {valor[1]}")


