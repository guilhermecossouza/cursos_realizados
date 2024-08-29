'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("--> {}".format(media))

if media <= 5:
    print(
        "Sua média foi de {:.1f} e está a baixo de 5.0 situação reprovado".format(media))
elif media >= 7.0:
    print(
        "Sua média foi de {:.1f} e está a baixo de 5.0 situação aprovado".format(media))
else:
    print(
        "Sua média foi de {:.1f} e está a baixo de 5.0 situação recuperação".format(media))
