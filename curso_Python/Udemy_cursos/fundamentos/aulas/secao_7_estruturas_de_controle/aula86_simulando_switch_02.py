def get_dias_semana(dia):
    dias = {
        1: "Final de semana",
        2: "Dia semana",
        3: "Dia semana",
        4: "Dia semana",
        5: "Dia semana",
        6: "Dia semana",
        7: "Final de semana",
    }
    # podemos passar um valor default no get cado não exista dado na lista
    return dias.get(dia, "** Dia inválido **")


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia}: {get_dias_semana(dia)}")
