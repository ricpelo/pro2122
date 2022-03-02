from abc import ABC

class Numerable(ABC):
    """
    La clase de los objetos que tienen número.
    """
    def __init__(self, numero=None):
        self.set_numero(numero)

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_numero() == otro.get_numero()

    def __hash__(self):
        return hash(self.get_numero())

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero
