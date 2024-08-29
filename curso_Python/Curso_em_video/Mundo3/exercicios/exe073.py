'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro", "
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Internacional
'''

tabela_compeonato_brasileiro = ("Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Fluminense", "Bragantino", "Athletico-PR", "Fortaleza", "Atlético-MG", 
                               "Cuiabá", "São Paulo", "Internacional", "Cruzeiro", "Corinthians", "Goiás", "Bahia", "Santos", "Vasco", "Coritiba", "América-MG")

print(f"Os cincos primeiros colocados na tabela: {tabela_compeonato_brasileiro[:6]}")
print(f"Os quatros últimos colocados na tabela: {tabela_compeonato_brasileiro[-4:]}")
print(f"A table em orderm alfabética: {sorted(tabela_compeonato_brasileiro)}")
print(f"Posição do time do Internacional na tabela: {tabela_compeonato_brasileiro.index('Internacional') + 1}")