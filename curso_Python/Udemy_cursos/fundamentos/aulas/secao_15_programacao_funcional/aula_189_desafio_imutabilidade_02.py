from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

setlocale(LC_ALL, "pt_BR")


def mes_com_31(mes): return mdays[mes] == 31


def get_nome_mes(mes): return month_name[mes]


def juntar_meses(todos, nome_mes): return f"{todos} \n- {nome_mes}"


print(reduce(juntar_meses, map(get_nome_mes, filter(
    mes_com_31, range(1, 13))), "Mese com 31 dias."))
