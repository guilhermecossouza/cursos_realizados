try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
# except:
#     print("Infelizmente tivemos um erro :(")
except ZeroDivisionError as divisao_zero:
    print("Não existe divisão por 0")
except ValueError as erro_valor:
    print("Favor digitar corretamente.")
except Exception as erro:
    print(erro.__class__)
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Vo,te sempre! Muito obrigado.")
