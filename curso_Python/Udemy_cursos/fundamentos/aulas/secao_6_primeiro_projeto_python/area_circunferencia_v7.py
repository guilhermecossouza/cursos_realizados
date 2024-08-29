# Aula 66 Testando se é o módulo principal
import math
# print(dir(math))
pi = math.pi
# -> Foi realizado um conversão explicita

if __name__ == "__main__":
    raio = float(input("Informe o raio: "))

print(f"A área do circulo: {pi * raio ** 2}")
