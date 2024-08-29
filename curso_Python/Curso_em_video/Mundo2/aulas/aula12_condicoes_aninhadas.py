nome = input("Qual o seu nome? ")
# só um if chama-se condição simples
# if e else chama-se de estrutura composta
# if elif else chama-se de estrutura condicional aninhada
if nome == "Guilherme":
    print("Que nome lindo!")
elif nome == "Gabriel" or nome == "Maria Vitória" or nome == "Hiago":
    print("Seu nome é bem popular no Brasil!")
elif nome in "zaca vando pedro":
    print("há nemm")
else:
    print("Seu nome é bem normal!")

print("Tenha um bom dia, {}".format(nome))
