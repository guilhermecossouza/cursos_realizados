from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente("Guilherme", 38)
    vendedor = Vendedor("Vandim", 38, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 6, 4), 256)
    cliente.registar_compras(compra1)
    cliente.registar_compras(compra2)
    print(f'Cliente: {cliente} {"Adulto" if cliente.is_adult() else ""}')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtd_compras = len(cliente.compras)
    print(f"Total: {valor_total} em {qtd_compras} compras")
    print(f"Última compra {cliente.get_data_ultima_compra()}")


if __name__ == '__main__':
    main()
