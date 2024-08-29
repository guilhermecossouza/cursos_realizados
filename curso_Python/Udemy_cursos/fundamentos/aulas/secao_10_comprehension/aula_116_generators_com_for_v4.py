# Generator el ta=rabalha sob demamada, ou seja, so mai ocupar memória caso ele seje solicitado.
generator = (i * 2 for i in range(10) if i % 2 == 0)
#usando com o for não precisa usar a função next
for numero in generator:
    print(numero)