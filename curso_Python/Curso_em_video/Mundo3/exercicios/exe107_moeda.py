def aumentar(preco=0.00, porcentagem=0.00):
    aumento = (preco * porcentagem) / 100
    print(f"O valor informado foi de R${preco:.2f}, aumentou {porcentagem}% e foi para R${(preco + aumento):.2f}")


def diminuir(preco=0.00, porcentagem=0.00):
    valor = (preco * porcentagem) / 100
    print(f"O valor informado foi de R${preco:.2f}, aumentou {porcentagem}% e foi para R${(preco - valor):.2f}")

def dobro(valor=0.00):
    dobrar = valor * 2
    print(f"O valor informado foi de {valor:.2f} dobrado foi para R${dobrar:.2f}")

def metade(valor=0.00):
    metade = valor / 2
    print(f"O valor informado foi de R${valor:.2f} e sua metade é R${metade:.2f}")
    