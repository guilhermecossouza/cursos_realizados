# Generator ele trabalha sob demamada, ou seja, so mai ocupar memória caso ele seje solicitado.
generator = (i * 2 for i in range(10) if i % 2 == 0)
# print(generator) Erro ele não maostar tudo e sim de um por um
print(next(generator))  # 1 -> 0
print(next(generator))  # 2 -> 4
print(next(generator))  # 3 -> 8
print(next(generator))  # 4 -> 12
print(next(generator))  # 5 -> 16
# ERRO -> StopIteration -> não tem mais posições para interar
print(next(generator))
