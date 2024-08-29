def faixa_etaria(idade):
    if 0 <= idade < 18:
        return "Menor de idade"
    elif idade in range(18, 64):  # range também faz interválos entre números
        return "Adulto"
    elif idade in range(65, 100):  # range também faz interválos
        return "Melhor idade"
    elif idade >= 100:
        return "Centenário"
    else:
        return "Idade inválida"


if __name__ == "__main__":
    for idade in (17, 35, 87, 113, -2):
        print(f"{idade}: {faixa_etaria(idade=idade)}")
