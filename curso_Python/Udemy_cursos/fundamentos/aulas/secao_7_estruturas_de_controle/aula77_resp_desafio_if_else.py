ERRO = "\033[91m"
NORMAL = "\033[0m"


def conceito(nota=0):
    mensagem = ""
    if nota > 10 or nota == 0:
        mensagem = f"{ERRO}Nota Inválida {nota}{NORMAL}"
    elif 9 < nota <= 10:
        mensagem = "Nota A"
    elif 8 < nota <= 9:
        mensagem = "Nota A-"
    elif 7 < nota <= 8:
        mensagem = "Nota B"
    elif 6 < nota <= 7:
        mensagem = "Nota B-"
    elif 5 < nota <= 6:
        mensagem = "Nota C"
    elif 4 < nota <= 5:
        mensagem = "Nota C-"
    elif 3 < nota <= 4:
        mensagem = "Nota D"
    elif 2 < nota <= 3:
        mensagem = "Nota D-"
    elif 1 < nota <= 2:
        mensagem = "Nota E"
    elif 0 < nota <= 1:
        mensagem = "Nota E-"
    return mensagem


if __name__ == "__main__":
    nota = float(input("Digite sua nota: "))
    print(conceito(nota=nota))
