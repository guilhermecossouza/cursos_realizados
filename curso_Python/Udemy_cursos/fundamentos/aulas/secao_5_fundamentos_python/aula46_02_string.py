nome = "Ana Paula"
print(nome[0])
print(nome[6])
print(nome[-3])  # realiza a leitura de traz para frente 0 zero não conta
# range
print(nome[4:])
print(nome[-5:])  # realiza a leitura de traz para frente 0 zero não conta
print(nome[:3])  # obs: não conta o último caracter
print(nome[2:5])

numeros = "1234567890"
print(numeros[ : : ]) # mostra a variável por completo porque não foi informado o inicio e nem o fim e nem os steps
print(numeros[ : : 2]) # pula de 2 em 2 que são os steps ou passos
print(numeros[1 : : 2])
print(numeros[ : : -1]) # nostrando a variável de traz para frente
print(nome[ : : -1])
