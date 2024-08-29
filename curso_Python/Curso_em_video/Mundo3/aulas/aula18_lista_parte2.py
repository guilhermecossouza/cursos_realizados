# lista composta lista dentro de lista
# teste = list()
# teste.append("Guilherme")
# teste.append(39)
# galera = list()
# galera.append(teste.copy())
# teste[0] = "Kenia"
# teste[1] = 36
# galera.append(teste.copy())
# print(galera)

# galera = [["guilherme", 39], ["Kenia", 36], [
#     "Hiago", 17], ["Gabriel", 17], ["Maria Vitória", 15]]
# print(galera)
# print(galera[0])
# print(galera[0][0])
# print(galera[2:]) #podemos usar fatiamento
# print(galera[0][0:]) #podemos usar fatiamento

# for g in galera:
#     print(g[0])  # somente os nomes

galera = list()
dado = list()
total_maior_idade = total_menor_idade = 0
for c in range(0, 2):
    dado.append(str(input("Nome: ").strip()))
    dado.append(int(input("Idade: ").strip()))
    galera.append(dado.copy())
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade")
        total_maior_idade += 1
    else:
        print(f"{pessoa[0]} é menor de idade")
        total_menor_idade += 1
        
print(f"Total de maiores de idade: {total_maior_idade}")
print(f"Total de manor de idade: {total_menor_idade}")
