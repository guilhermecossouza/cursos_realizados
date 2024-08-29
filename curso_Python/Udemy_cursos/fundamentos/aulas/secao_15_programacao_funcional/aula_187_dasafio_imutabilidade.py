from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

setlocale(LC_ALL, "pt_BR")

meses_31 = list(filter(lambda m: mdays[m] == 31, range(1, 13)))
nome_meses = list(map(lambda nome: month_name[nome], meses_31))
texto = reduce(lambda todos, nome_meses: f"{todos} \n- {nome_meses}", nome_meses, "Meses com 31 dias")
print(texto)
