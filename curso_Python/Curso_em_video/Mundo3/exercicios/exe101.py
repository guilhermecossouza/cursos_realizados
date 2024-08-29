"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""
import datetime

def valida_ano(ano=0):
    if(len(str(ano)) != 4 and str(ano) != "0000"):
        return False
    else:
        return True

def voto(ano=0):
    msg = ""
    idade = datetime.date.today().year - ano
    print(idade)
    if idade < 16:
        msg = "negado"
    elif 16 <= idade < 18:
        msg = "opcional"
    elif 17 < idade <= 70:
        msg = "obrigatório"
    elif idade > 70:
        msg = "opcional"
    else:
        msg = "Ops! algo deu errado."    
    return msg


ano = int(input("Informe o ano de seu nascimento: "))
if valida_ano(ano) is True:
    print(f"O seu voto é: {voto(ano)}")
else:
    print("Ano de nascimento informado é inválido.")
