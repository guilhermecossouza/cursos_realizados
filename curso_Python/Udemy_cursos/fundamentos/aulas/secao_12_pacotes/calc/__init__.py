from pacotes.modulo1 import soma
from pacotes2.modulo1 import subtracao
# __all__ recebe um lista de todas as funções que vai exportar
# isso faz com que consiga expor essa funcionalidade desse pacote
__all__ = ["soma", "subtracao"]
