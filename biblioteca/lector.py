"""
lector.py: Módulo que implementa los lectores de la biblioteca.
copyright: (c) 2022 Ricardo Pérez <ricardo@iesdonana.org>
licencia: GPL-3 <https://www.gnu.org/licenses/gpl-3.0.txt>
"""

class Lector:
    """
    Los lectores de la biblioteca.
    """

    __lectores = {}

    @staticmethod
    def __insertar(lector):
        Lector.__lectores[lector.get_numero()] = lector

    @staticmethod
    def __buscar(numero):
        return Lector.__lectores.get(numero)

    @staticmethod
    def __borrar(lector):
        del Lector.__lectores[lector.get_numero()]

    @staticmethod
    def __siguiente_numero_libre():
        return 1 if len(Lector.__lectores) == 0 else \
               max(Lector.__lectores) + 1

    def __init__(self, nombre, numero=None):
        if numero is None:
            self.__numero = Lector.__siguiente_numero_libre()
        else:
            if Lector.__buscar(numero) is None:
                self.__numero = numero
            else:
                raise ValueError('Ya existe un lector con ese número')
        self.set_nombre(nombre)
        Lector.__insertar(self)

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_numero() == otro.get_numero()

    def __hash__(self):
        return hash(self.get_numero())

    def __repr__(self):
        return f'Lector({self.get_nombre()!r}, {self.get_numero()!r})'

    def get_numero(self):
        return self.__numero

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
