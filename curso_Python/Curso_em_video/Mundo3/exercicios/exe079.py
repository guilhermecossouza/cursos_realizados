'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = []
while True:
    numero = int(input("informe um valor inteiro, caso deseje para digitar [999]: "))
    if numero == 999:
        break
    else:
        if valores.count(numero) == 0:
            valores.append(numero)
valores.sort()
print(f"Os valores informado em ordemcrecente: {valores}")
        
