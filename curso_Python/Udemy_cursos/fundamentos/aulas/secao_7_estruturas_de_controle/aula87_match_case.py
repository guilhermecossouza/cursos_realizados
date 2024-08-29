def get_dias_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunada"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "** Dia inválido"


def get_dias_semana_dois(dia):
    match dia:
        case 1 | 7:
            return "Final de semana"
        case 2 | 3 | 4 | 5 | 6:
            return "Dia da semana"


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia}: {get_dias_semana(dia)}")
    print("-=-"*50)
    for dia in range(0, 9):
        print(f"{dia}: {get_dias_semana_dois(dia)}")
