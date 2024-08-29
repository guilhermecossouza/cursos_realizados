# No python não existe por padão constantes
# Más caso deseje indicar que a variável é constante colocalas sempre com letras maiusculas.
PALAVRAS_PROIBIDAS = ("futebol", "religião", "política")

textos = [
    "João gosta de futebol e política",
    "A praia foi divertida"
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            found = True
            print(f"Existe ao menos uma palavra proibida: {palavra}")
            break

    if not found:
        print("Texto liberado")
