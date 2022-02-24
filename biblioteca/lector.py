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

    def __init__(self, nombre):
        self.__numero = Lector.__siguiente_numero_libre()
        self.set_nombre(nombre)
        Lector.__insertar(self)

    def get_numero(self):
        return self.__numero

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
