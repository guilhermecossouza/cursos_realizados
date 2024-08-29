''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

print("{}".format("-=" * 20))
print("{:^40}".format("MENU"))
print("OPÇÔES:")
print("1: somar")
print("2: multiplicar")
print("3: maior")
print("4: novos números")
print("5: sair do programa")
print("{}".format("-=" * 20))
opcao = int(input("Informe a sua opção: "))
novos_numero = False
while opcao != 5:
    if not novos_numero:
        num1 = float(input("digite um valor: "))
        num2 = float(input("digite outro valor: "))
   
    if opcao == 1:
        novos_numero = False
        print("Você escolheu soma:")
        print("A soma de {} + {} = {}".format(num1, num2, (num1 + num2)))
        opcao = int(input("Informe a sua opção: "))
    elif opcao == 2:
        novos_numero = False
        print("Você escolheu multiplicação: ")
        print("A soma de {} + {} = {}".format(num1, num2, (num1 * num2)))
        opcao = int(input("Informe a sua opção: "))
    elif opcao == 3:
        novos_numero = False
        print("Você escolheu o maoir numéro")
        if num1 > num2:
            print("O maior entre {} e {} é: {}".format(num1, num2, num1))
        else:
            print("O maior entre {} e {} é: {}".format(num1, num2, num2))
        opcao = int(input("Informe a sua opção: "))
    elif opcao == 4:
        print("Você escolheu noves números: ")
        novos_numero = True
        num1 = float(input("digite um valor: "))
        num2 = float(input("digite outro valor: "))
        opcao = int(input("Informe a sua opção: "))
    elif opcao == 5:
        break
    else:
        opcao = int(input("Informe a sua opção: "))
