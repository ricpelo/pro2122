class Ficha:
    def __init__(self, color):
        if color not in ('B', 'N'):
            raise ValueError('Color incorrecto')
        self.__color = color

    def color(self):
        return self.__color

class Tablero:
    MAX_FILAS = 6
    MAX_COLUMNAS = 7

    def __init__(self):
        self.__tablero = []
        for _ in range(Tablero.MAX_COLUMNAS):
            self.__tablero.append([])

    @staticmethod
    def __fila_valida(fila):
        if fila not in range(Tablero.MAX_FILAS):
            raise ValueError('Fila incorrecta')

    @staticmethod
    def __columna_valida(col):
        if col not in range(Tablero.MAX_COLUMNAS):
            raise ValueError('Columna incorrecta')

    def meter(self, ficha, col):
        Tablero.__columna_valida(col)
        columna = self.__tablero[col]
        if len(columna) > Tablero.MAX_FILAS:
            raise ValueError('Columna llena')
        columna.append(ficha)
        return self

    def ficha(self, fila, col):
        Tablero.__fila_valida(fila)
        Tablero.__columna_valida(col)
        columna = self.__tablero[col]
        if fila + 1 <= len(columna):
            return columna[fila]
        return None

tablero = Tablero().meter(Ficha('N'), 0).meter(Ficha('B'), 0).meter(Ficha('N'), 0)

assert tablero.ficha(0, 0) is not None
assert tablero.ficha(0, 0).color() == 'N'
assert tablero.ficha(1, 0) is not None
assert tablero.ficha(0, 1) is None
