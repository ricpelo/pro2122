"""
prestamos.py: Módulo que implementa los prestamos de la biblioteca.
copyright: (c) 2022 Ricardo Pérez <ricardo@iesdonana.org>
licencia: GPL-3 <https://www.gnu.org/licenses/gpl-3.0.txt>
"""

import datetime

from numerable import Numerable

class Prestamo(Numerable):
    def __init__(self, lector, prestable):
        if not prestable.es_prestable():
            raise ValueError('Ese fondo no se puede prestar')
        if not prestable.esta_disponible():
            raise ValueError('Ese fondo no está disponible')
        super().__init__()
        prestable.set_disponible(False)
        self.__lector = lector
        self.__prestable = prestable
        self.__fecha_prestamo = datetime.date.today()
        self.__fecha_devolucion = None

    def get_lector(self):
        return self.__lector

    def get_prestable(self):
        return self.__prestable

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        if self.get_fecha_devolucion() is not None or \
           fecha_devolucion is None:
            raise ValueError('Intento incorrecto de cambiar la fecha de devolución')
        self.__fecha_devolucion = fecha_devolucion
