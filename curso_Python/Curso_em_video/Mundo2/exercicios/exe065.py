''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

continuar = True
n_media = 0
n_maior = 0
soma = 0
media = 0
while continuar is True:
    num = int(input("Digite um número: "))
    opcao = str(input("Deseja continuar [S/N]? ")).upper().strip()[:1]
    
    if num > n_maior:
        n_maior = num

    n_media += 1
    soma += num
    if opcao == "N":
        continuar = False
media = soma / n_media
print("O maior número digitado foi {}".format(n_maior))
print("A média dos números digitados é {}".format(media))
