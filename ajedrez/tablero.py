from color import Color
from casilla import Casilla

class Tablero:
    def __init__(self, blanco: Color, negro: Color):
        self.__tablero = {}
        for i in range(8):
            for j in range(8):
                color = blanco if (i + j) % 2 == 0 else negro
                self.__tablero[(i, j)] = Casilla(color)

    def get_casilla(self, fila, col):
        if fila not in range(8):
            raise ValueError('Fila incorrecta')
        if col not in range(8):
            raise ValueError('Columna incorrecta')
        return self.__tablero[(fila, col)]
