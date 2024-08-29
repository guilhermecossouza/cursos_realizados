PALAVRAS_PROIBIDAS = {"futebol", "religião",
                      "política"}  # Transformando em um set

textos = [
    "João gosta de futebol e política",
    "A praia foi divertida"
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print(f"Existe ao menos uma palavra proibida no texto: {intersecao}")
    else:
        print("Texto autorizado")
