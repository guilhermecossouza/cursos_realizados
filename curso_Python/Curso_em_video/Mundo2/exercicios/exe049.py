''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

numero = int(input("Digite um numero para ver sua tabuada: "))
for contador in range(0, 11, 1):
    print("{} X {} = {}".format(numero, contador, (numero * contador)))