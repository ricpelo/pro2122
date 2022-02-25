"""
fondos.py: Módulo que implementa los fondos de la biblioteca.
copyright: (c) 2022 Ricardo Pérez <ricardo@iesdonana.org>
licencia: GPL-3 <https://www.gnu.org/licenses/gpl-3.0.txt>
"""

from abc import ABC, abstractmethod

class Fondo(ABC):
    __fondos = {}

    @staticmethod
    def _insertar(fondo):
        Fondo.__fondos[fondo.get_numero()] = fondo

    @staticmethod
    def _buscar(numero):
        return Fondo.__fondos.get(numero)

    @staticmethod
    def _borrar(fondo):
        del Fondo.__fondos[fondo.get_numero()]

    @staticmethod
    def _siguiente_numero_libre():
        return 1 if len(Fondo.__fondos) == 0 else \
               max(Fondo.__fondos) + 1

    @abstractmethod
    def es_prestable(self):
        ...

    def __init__(self):
        self.__numero = Fondo._siguiente_numero_libre()

    def get_numero(self):
        return self.__numero

class Prestable(Fondo, ABC):
    def es_prestable(self):
        return True

    @abstractmethod
    def plazo_devolucion(self):
        ...

    def __init__(self):
        super().__init__()
        self.__disponible = True

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible

class NoPrestable(Fondo, ABC):
    def es_prestable(self):
        return False

    def __init__(self):
        raise ValueError('La clase es abstracta')

class Libro(Prestable):
    def __init__(self, signatura, titulo, autor, num_paginas):
        self.__signatura = signatura
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = num_paginas

    def plazo_devolucion(self):
        return 15

class Multimedia(Prestable):
    pass
