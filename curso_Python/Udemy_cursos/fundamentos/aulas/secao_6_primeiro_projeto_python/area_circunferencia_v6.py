# Aula 65 Um pouco sobre módulos
import math
# print(dir(math))
pi = math.pi
# -> Foi realizado um conversão explicita
raio = float(input("Informe o raio: "))
print(f"A área do circulo: {pi * raio ** 2}")
print("-="*30)
print(f"Nome do módulo: {__name__}")
print(f"Nome do pcote: {__package__}")

if __name__ == "__main__":
    print("teste")
