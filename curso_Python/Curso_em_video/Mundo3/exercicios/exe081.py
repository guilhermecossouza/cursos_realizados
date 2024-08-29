'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''
lista_numeros = []
while True:
    numero = int(input("Informe um valor, para sair digite [999]: "))
    if numero == 999:
        break
    else:
        lista_numeros.append(numero)

print(f"Foram digitados um totade de {len(lista_numeros)} numeros")
lista_numeros.sort()
print("Números informado de forma crescente", end="")
for enum, num in enumerate(lista_numeros):
    if enum == 0:
        print(f" {num}", end="")
    else:
        print(f", {num}", end="")
print("")
if 5 in lista_numeros:
    print("O valor 5 foi digitado.")
else:
    print("O valor 5 não foi digitado.")

