from color import Color
from casilla import Casilla
from pieza import Pieza, Torre, Alfil

class Tablero:
    def __init__(self, blanco: Color, negro: Color):
        self.__tablero = {}
        for i in range(8):
            for j in range(8):
                color = blanco if (i + j) % 2 == 0 else negro
                self.__tablero[(i, j)] = Casilla(i, j, color)
        for i in (0, 7):
            self.get_casilla(0, i).set_pieza(Torre(blanco))
        for i in (0, 7):
            self.get_casilla(7, i).set_pieza(Torre(negro))
        for i in (2, 5):
            self.get_casilla(0, i).set_pieza(Alfil(blanco))
        for i in (2, 5):
            self.get_casilla(7, i).set_pieza(Alfil(negro))

    def get_casilla(self, fila, col):
        if fila not in range(8):
            raise ValueError('Fila incorrecta')
        if col not in range(8):
            raise ValueError('Columna incorrecta')
        return self.__tablero[(fila, col)]

    def movimiento_valido(self, inicial: Casilla, final: Casilla) -> bool:
        pieza = inicial.get_pieza()
        if pieza is None:
            return False

    def devolver_piezas(self, color: Color) -> list[Pieza]:
        res = []
        for casilla in self.__tablero.values():
            pieza = casilla.get_pieza()
            if pieza is not None and pieza.get_color() == color:
                res.append(pieza)
        return res
