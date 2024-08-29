# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele
#algo = str(input("Digite algo: "))
algo = "Programador"
print("O tipo primitivo desse valor é {}".format(type(algo)))
print("Só tem espaçoes? {}".format(algo.isspace()))
print("É numérico? {}".format(algo.isnumeric()))
print("É alfabético? {}".format(algo.isalpha()))
print("É alfanumérico? {}".format(algo.isalnum()))
print("Está em letras maiúsculas? {}".format(algo.isupper()))
print("Está em letras minúsculas? {}".format(algo.islower()))
print("Está captalizado? {}".format(algo.istitle()))