# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
import calendar

ano = int(input("Informe um ano qualquer? "))
if calendar.isleap(ano) is True:
    print("O ano digitao foi {}, e ele é um ano bixesto.".format(ano))
else:
    print("O ano digitao foi {}, e ele não é um ano bixesto.".format(ano))