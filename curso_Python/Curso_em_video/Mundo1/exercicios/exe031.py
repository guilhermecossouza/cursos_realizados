'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''
kilometro_viagem = int(input("Informe a kilometragem do seu destino: "))
if kilometro_viagem <= 200:
    valor_passagem = kilometro_viagem * 0.50
else:
    valor_passagem = kilometro_viagem * 0.45

print("Sua viagem terá {}Km e o valor vai custar R${}".format(kilometro_viagem, valor_passagem))