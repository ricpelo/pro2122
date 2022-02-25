"""
prestamos.py: Módulo que implementa los prestamos de la biblioteca.
copyright: (c) 2022 Ricardo Pérez <ricardo@iesdonana.org>
licencia: GPL-3 <https://www.gnu.org/licenses/gpl-3.0.txt>
"""

import datetime

class Prestamo:
    __prestamos = {}

    @staticmethod
    def __insertar(prestamo):
        Prestamo.__prestamos[prestamo.get_numero()] = prestamo

    @staticmethod
    def __buscar(numero):
        return Prestamo.__prestamos.get(numero)

    @staticmethod
    def __borrar(prestamo):
        del Prestamo.__prestamos[prestamo.get_numero()]

    @staticmethod
    def __siguiente_numero_libre():
        return 1 if len(Prestamo.__prestamos) == 0 else \
               max(Prestamo.__prestamos) + 1

    def __init__(self, lector, prestable):
        if not prestable.es_prestable():
            raise ValueError('Ese fondo no se puede prestar')
        if not prestable.disponible():
            raise ValueError('Ese fondo no está disponible')
        self.__lector = lector
        self.__prestable = prestable
        self.__fecha_prestamo = datetime.date.today()
        self.__fecha_devolucion = None
        self.__numero = Prestamo._siguiente_numero_libre()

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
