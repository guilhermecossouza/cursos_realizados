'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''
import datetime
ano_nascimento = int(input("informe o ano de seu nascimento: "))
idade_atleta = int(datetime.date.today().year) - ano_nascimento
print(idade_atleta)
str_mensagem = "Sua idade é {}, e sua categoria é: {}"
if idade_atleta <= 9:
    print(str_mensagem.format(idade_atleta, "mirim"))
elif 9 < idade_atleta <= 14:
    print(str_mensagem.format(idade_atleta, "infantil"))
elif 14 < idade_atleta <= 19:
    print(str_mensagem.format(idade_atleta, "júnior"))
elif 19 < idade_atleta <= 20:
    print(str_mensagem.format(idade_atleta, "sênior"))
else:
    print(str_mensagem.format(idade_atleta, "master"))
