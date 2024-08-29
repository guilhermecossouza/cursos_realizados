# OBS: o end="" serve para inserir alguma coisa ao final da impressão
# por padrão ele vem com o \n
palavra = "paralelepípedo"
for letra in palavra:
    print(letra)  # iprimir linha por linha de cada letra

print("-="*30)
for letra in palavra:
    # vai imprimir em uma linha só pois o end foi passado vazio ex: paralelepípedo
    print(letra, end="")

print("-="*30)
for letra in palavra:
    # vai imprimir em uma linha separado por , ex: p,a,r,a,l,e,l,e,p,í,p,e,d,o,
    print(letra, end=",")

print("-="*30)
# Percorrendo uma lista []
nomes_pessoas = ["Guilherme", "Kenia", "Gustavo"]
for nome in nomes_pessoas:
    print(nome)

print("-="*30)
# enumerate -> Vai mostrar o indice començando do 0
for posicao, nome in enumerate(nomes_pessoas):
    print(f"{posicao}: {nome}")

print("-="*30)
dias_semana = ("Domingo", "Segunda-feira", "Terça-feira",
               "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")
for dia in dias_semana:
    print(f"Hoje é dia: {dia}")

print("-="*30)
for letra in set("ola mundo"):
    print(letra)

print("-="*30)
for numero in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
    print(numero)
