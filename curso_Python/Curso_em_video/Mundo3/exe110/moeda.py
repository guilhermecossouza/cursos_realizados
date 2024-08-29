import locale

def aumentar(preco=0.00, porcentagem=0.00):
    aumento = (preco * porcentagem) / 100
    return f"O valor informado foi de R${preco:.2f}, aumentou {porcentagem}% e foi para R${(preco + aumento):.2f}"


def diminuir(preco=0.00, porcentagem=0.00):
    valor = (preco * porcentagem) / 100
    return f"O valor informado foi de R${preco:.2f}, aumentou {porcentagem}% e foi para R${(preco - valor):.2f}"

def dobro(valor=0.00):
    dobrar = valor * 2
    return f"O valor informado foi de {valor:.2f} dobrado foi para R${dobrar:.2f}"

def metade(valor=0.00):
    metade = valor / 2
    return f"O valor informado foi de R${valor:.2f} e sua metade é R${metade:.2f}"

def moeda(valor=0.00):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor, grouping=True, symbol="R$")
    print(valor)
    

def resumo(valor, formatado=False):
    print("-*"*30)
    print("RESUMO:")
    print(f"{aumentar(2.00, 10)}\n{dobro(2.00)}\n{metade(2.00)}\n{moeda(2000.00)}\n{diminuir(2.00, 10)}")
    print("-*"*30)
