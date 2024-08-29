# + -> Adição
# - -> subitração
# * -> multiplicação
# / -> divisão
# **  -> Potência
# // -> Divisão inteira
# % -> resto da divisão

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)

# orderm de prioridade em execuções de expressão
# 1 -> ()
# 2 -> **
# 3 -> * / // %
# 4 -> + -

print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

# pratica
# funcção interna
print(pow(4, 3))
print("oi" * 5)
print("=-"*50)
nome = input("Digite seu nome :")
print("Prazer em te conhecer {}!".format(nome))
print("Prazer em te conhecer {:20}!".format(nome))  # ocupando 20 caracters
print("Prazer em te conhecer {:>20}!".format(nome))  # alinhado a direita
print("Prazer em te conhecer {:<20}!".format(nome))  # alinhado a esquerda
print("Prazer em te conhecer {:^20}!".format(nome))  # alinhado ao centro
print("Prazer em te conhecer {:=^20}!".format(nome))  # alinhado ao centro

n1 = int(input("Digite uma núemro: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
e_pow = pow(n1, n2)
# adicionando o end="" como parâmetro no ptint não deixa quebrar a linha
print("A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.2f}".format(
    s, su, m, d), end=" ")
print("A divisão inteira e {}, potência {}, potência função é {}".format(di, e, e_pow))
