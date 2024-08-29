from locale import setlocale, LC_ALL
from calendar import month_name, mdays

setlocale(LC_ALL, "pt_BR")

print("Meses com 31 dias...")
# Abordagem declarativa você diz o que quer  e espera sem saber como vai ser feiro
# Aqui estou dizendo como deve ser feito - aboradagem imperativa
for num in range(1, 13):
    if mdays[num] == 31:
        print(f"- {month_name[num]}")
