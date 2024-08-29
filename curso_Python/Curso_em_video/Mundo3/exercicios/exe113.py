def leia_int():
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Favor informar um valor inteiro.")
        else:
            break
        finally:
            print("Obrigado e volte sempre.")

def leia_float():    
    while True:
        try:
            n = float(input("Digite um número real: "))
        except ValueError:
            print("Favor informar um valor inteiro.")
        else:
            break
        finally:
            print("Obrigado e volte sempre.")
            

leia_int()
leia_float()