from random import randint
# tempo = int(input("Qunatos anos seu carro tem? "))
tempo = randint(1, 40)
if tempo <= 3:
    print("Carro nonvo")
else:
    print("Carro velho")
print("--fim--")

# condição simplificada
# idade = int(input("Qual a sua idade? "))
idade = randint(1, 110)
print("maior" if idade >= 18 else "menor")

# prática
nome = input("Qual o seu nome? ")
if nome == "Guilherme":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")
print("Bom dia {}".format(nome))
