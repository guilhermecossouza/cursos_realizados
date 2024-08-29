"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 

Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.

Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""
import datetime

pessoa = dict()

pessoa["nome"] = str(input("Informe o nome: ")).upper().strip()
ano_nasc = int(input("Informe o ano de nascimento: "))
pessoa["idade"] = datetime.date.today().year - ano_nasc
pessoa["ctps"] = int(input("Informe o número da carteira de trabalho: "))
if pessoa["ctps"] > 0:
    pessoa["contratacao"] = int(input("Informe o ano contratação: "))
    pessoa["salario"] = float(input("Informe o valor do salário: R$"))
    pessoa["aposentadoria"] = (pessoa['contratacao'] + 35) - ano_nasc

for item, valor in pessoa.items():
    print(f"{item}: {valor}")






