# Temos dis tipos de parâmetros em funções
# 1° -> Posicional Ex:
def funcao_posicional(p1, p2, p3):
    pass


# Ou seja p1 = 1 -- p2 = 2 -- p3 = 3
print(funcao_posicional(1, 2, 3))

# 2° -> Nomeado Ex:


def funcao_nomeada(p3=0, p2=0, p1=0):
    pass


# troquei as posições
print(funcao_nomeada(p1=1, p3=3, p2=2))


# Temos mais doi tipos de parametros:
# *args => vai gerar uam turpla
# **kwargs => vai gerar uma lista lista
