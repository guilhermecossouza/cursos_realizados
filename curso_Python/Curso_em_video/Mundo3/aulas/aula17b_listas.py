# podemos iniciar as lista
# list() ou []

valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for valor in valores:
#     print(f"{valor}...", end=" ")
# print("\n")

for valor in range(0, 5):
    valores.append(int(input("Digite uma valor: ")))


for posicao, valor in enumerate(valores):
    print(f"Na posição {posicao}, tenho o valor {valor}")
