"""
Faça um programa que tenha uma função chamada area(), 
que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
"""
def regista_informacoes(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"A área do terreno é {area_terreno} metros")

largura = float(input("Informe a largura: "))
comprimento = float(input("Informe o comprimento: "))

regista_informacoes(largura, comprimento)
    




