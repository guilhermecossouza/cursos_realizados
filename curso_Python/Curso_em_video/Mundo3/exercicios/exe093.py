"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
gols = list()
total_gols = 0
jogador["nome"] = str(input("Informe o nome do jogador: "))
total_partidas = int(input("Informe a quantidade de partidas jogadas: "))
for contador in range(1, total_partidas + 1):
    qtd_gols = int(input(f"Na {contador}° partida fez quantos gols: "))
    gols.append(qtd_gols)
    total_gols += qtd_gols

jogador["gols"] = gols[:]
jogador["total"] = total_gols
jogador["média"] = total_gols / total_partidas

print("-=" * 30)
print(f"Nome jogador: {jogador['nome']}")
for i, v in enumerate(jogador["gols"]):
    print(f"Na partida {i + 1}° partida, o jogador fez {v} gols.")
print(f"Um total de {jogador['total']} gols no capeonato.")
print(f"Uma média de {jogador['média']} gols por partida.")
print("-=" * 30)