''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    else:
        print("-=" * 30)
        msg = "Tabuada n°{}".format(numero)
        print("{:^20}".format(msg))
        for contador in range(11):
            print("{} X {} = {}".format(numero, contador, (numero * contador)))
        print("-=" * 30)
