# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input("Digite um valor em metros: "))
print("A medida de {}m corresponde a:")
print("Em kilometros: {}".format((metros * 1000)))
print("Em equitrômetros: {}".format(metros * 100))
print("Em decâmetros: {}".format(metros * 10))
print("Em decímetros {}".format((metros / 10)))
print("Em centímetros {}".format((metros / 100)))
print("Em milímetros: {}".format((metros / 1000)))