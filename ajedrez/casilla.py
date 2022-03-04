from color import Color
from pieza import Pieza

class Casilla:
    def __init__(self, fila, columna, color: Color):
        self.__fila = fila
        self.__columna = columna
        self.__color = color
        self.set_pieza(None)

    def get_fila(self):
        return self.__fila

    def get_columna(self):
        return self.__columna

    def get_color(self):
        return self.__color

    def get_pieza(self):
        return self.__pieza

    def set_pieza(self, pieza: Pieza):
        self.__pieza = pieza
