'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
print("{}".format("-="*20))
valor_produto = float(input("Informe o valor do produto: "))
print("{}".format("-="*20))
print("{:^40}".format("Menu:"))
print("1 - à vista dinheiro/cheque: 10% de desconto")
print("2 - à vista no cartão: 5% de desconto")
print("3 - em até 2x no cartão: preço normal")
print("4 - em 3x ou mais no cartão: 20% de juros")
print("{}".format("-="*20))
opcao = int(input("Escolha a sua forma de pagamento: "))

match opcao:
    case 1:
        print("valor do produto R${:.2f}, com 10% de desconto: R${:.2f}".format(
            valor_produto, (valor_produto - (valor_produto * 10) / 100)))
    case 2:
        print("valor do produto R${:.2f}, com 10% de desconto: R${:.2f}".format(
            valor_produto, (valor_produto - (valor_produto * 5) / 100)))
    case 3:
        print("valor do produto R${:.2f}, de 2X cada parcela sairá R${:.2f}".format(
            valor_produto, (valor_produto / 2)))
    case 4:
        valor_com_juros = valor_produto + (valor_produto * 20) / 100
        print("Em 3X ou mais terá 20% de juros.\n O valor do produto sairá R${:.2f}".format(
            valor_com_juros))
