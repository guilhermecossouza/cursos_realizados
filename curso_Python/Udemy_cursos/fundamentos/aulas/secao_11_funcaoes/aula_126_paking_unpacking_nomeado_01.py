# **kwargs vai criar um dicionário
# Nome **kwargs não é obrigatório o nome é opcional desde que esteja companhado o **
def resultado_f1(**podium):
    print(type(podium))
    print(dir(podium))
    print(podium)
    for posicao, piloto in podium.items():
        print(f"{posicao} => {piloto}")


def resultado_f1_02(primeiro, segundo, terceiro):
    print(f"1) {primeiro}")
    print(f"2) {segundo}")
    print(f"3) {terceiro}")


def resultado_f1_03(**podium):
    for posicao, piloto in podium.items():
        print(f"{posicao} => {piloto}")


if __name__ == "__main__":
    print(resultado_f1(primeiro="Max Verstappen",
          segundo="Lando Norris", terceiro="Fernando Alonso"))

    print("-=" * 30)

    dict_podim = {"terceiro": "Fernando Alonso",
                  "primeiro": "Max Verstappen", "segundo": "Lando Norris"}
    print(resultado_f1_02(**dict_podim))

    print("-=" * 30)

    print(resultado_f1_03(**dict_podim))
