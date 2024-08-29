"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

ex.:
n = leia_int("Digite um n")
"""

def leia_int(texto=""):
    e_numero = False
    while True:
        n = input(f"{texto}")        
        if n.isnumeric():
            a = n
            e_numero = True
        else:
            print("Informe um número inteiro")
        if e_numero is True:
            break
    return a
    

n = leia_int("Digite um número: ")
print(f"Você digitiu o número: {n}")