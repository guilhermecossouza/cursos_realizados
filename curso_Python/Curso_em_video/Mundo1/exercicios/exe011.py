# Faça um programa que leia a largura e a algura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = altura * largura
print("Sua parede tem o dimensão {}X{} e sua área é de {}m²".format(altura, largura, area))
latas_tinta = area / 2
print("Para pintar a parede você precisará de {} latas de tinta".format(latas_tinta))






