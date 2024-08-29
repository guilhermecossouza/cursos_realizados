def get_tipo_dia(dia):
    dias = {
        (1, 7): "final de semana",
        range(2, 7): "dia de semama"
    }
    dia_escolhido = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(dia_escolhido, "** Dia inválido **")


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"Dia {dia} é {get_tipo_dia(dia)}")
