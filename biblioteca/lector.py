"""
lector.py: Módulo que implementa los lectores de la biblioteca.
copyright: (c) 2022 Ricardo Pérez <ricardo@iesdonana.org>
licencia: GPL-3 <https://www.gnu.org/licenses/gpl-3.0.txt>
"""

from numerable import Numerable

class Lector(Numerable):
    """
    Los lectores de la biblioteca.
    """

    def __init__(self, nombre, numero=None):
        super().__init__(numero)
        self.set_nombre(nombre)

    def __repr__(self):
        return f'Lector({self.get_nombre()!r}, {self.get_numero()!r})'

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
