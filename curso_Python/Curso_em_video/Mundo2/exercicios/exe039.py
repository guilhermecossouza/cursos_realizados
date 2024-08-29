# Faça um programa que leia o ano de nascimento de um jovem e informe
# de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
import datetime

ano_nascimento = int(input("Informe o ano de nascimento: "))
idade = datetime.datetime.today().year - ano_nascimento
if idade < 18:
    print("Você ainda não pode se alistar no serviço militar!\n faltam {} anos para isso.".format(18 - idade))
elif idade == 18:
    print("Já está na hora de se alistar no serviço militar")
else:
    print("Já passou {} anos para se alistar".format(idade - 18))