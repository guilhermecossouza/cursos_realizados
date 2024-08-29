# listas são mutáveis -> podem ser alteradas
# declaração lista = []
num = [2, 5, 9, 1]
print(num)
num[2] = 3  # alterar o valor da posição informada
print(num)
# num[4] = 7  # Erro não pode alterar um valor de uma posição que não existe
num.append(7)  # Adiciona um valor a lista que será adicionado na ultima posição
print(num)
num.sort()  # vai origanizar a lista
print(num)
num.sort(reverse=True)  # vai origanizar a lista de forma inversa
print(num)
print(f"Essa lista tem {len(num)} posições")
# inseri um valoe na lista de a cordo com a posição informada
# 1° parametro wé a posição,
# 2° parametro e o valor
num.insert(2, 0)
print(num)
num.pop()  # remove o último elemento da lista
print(num)
num.pop(2)  # remove o elemento da lista na posição informada
print(num)
num.insert(3, 5)
print(num)
# caso tenha valores iguai ele vai remover a primiera ocorrência achada
num.remove(5)
print(num)

# caso queira deletar um valoe rua não exite vai dar erro.
# podemos fazer isso usando um if

if 4 in num:
    num.remove(4)
else:
    print("O valor 4 não exixte na lista")
