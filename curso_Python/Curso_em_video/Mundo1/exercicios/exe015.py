# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
km_rodados = float(input("Digita os kms rodados com o carro: "))
dias_alugado = int(input("Informe a quantidade de dias em que foi alugado: "))
print("Os kms rodados foram {}Km, valor da kilometragem é R$0,15, total de R${:.2f}".format(
    km_rodados, (km_rodados * 0.15)))
print("Os dias em que foi alugado foram {}, a diário é R$60,00 dia, dá um total de R${}".format(
    dias_alugado, (dias_alugado * 60)))
