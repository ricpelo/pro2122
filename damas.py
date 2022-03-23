import random

class Ficha:
    def __init__(self, color):
        if color not in ('B', 'N'):
            raise ValueError('El color no es correcto')
        self.__color = color

    def color(self):
        return self.__color

class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__fichas = []

    def nombre(self):
        return self.__nombre

    def fichas(self):
        return self.__fichas

    def quitar_ficha(self, ficha):
        for pos, f in enumerate(self.fichas()):
            if f == ficha:
                del self.__fichas[pos]
                return

    def siguiente_movimiento(self):
        if len(self.fichas()) == 0:
            return False
        ficha = random.choice(self.fichas())
        direccion = random.choice(('IZQ', 'DER'))
        ...


class Tablero:
    def __init__(self, j1, j2):
        self.__contenido = {}
        self.__jugador_blancas = j1
        self.__jugador_negras = j2
        self.__rellenar(j1, 'B', 1, 1)
        self.__rellenar(j2, 'N', 6, 2)

    def __quitar_ficha(self, ficha):
        jugador = self.__jugador_blancas if ficha.color() == 'B' else \
                  self.__jugador_negras
        jugador.quitar_ficha(ficha)

    def __rellenar(self, jugador, color, fila, col):
        while len(jugador.fichas()) < 12:
            f = Ficha(color)
            jugador.fichas().append(f)
            self.__contenido[(fila,col)] = f
            if col + 2 <= 8:
                col += 2
            else:
                fila += 1
                col = 1 if fila % 2 != 0 else 2

    def ficha(self, fila, col):
        return self.__contenido.get((fila,col))

    @staticmethod
    def __nueva_posicion(fila, col, color, direccion):
        if (color, direccion) == ('B', 'IZQ'):
            if fila != 8 and col != 1:
                fila += 1
                col -= 1
        elif (color, direccion) == ('B', 'DER'):
            if fila != 8 and col != 8:
                fila += 1
                col += 1
        elif (color, direccion) == ('N', 'IZQ'):
            if fila != 1 and col != 8:
                fila -= 1
                col += 1
        elif (color, direccion) == ('N', 'DER'):
            if fila != 1 and col != 1:
                fila -= 1
                col -= 1
        return (fila, col)

    def mover(self, ficha, direccion):
        if direccion not in ('IZQ', 'DER'):
            raise ValueError('Dirección incorrecta')
        if ficha is None:
            raise ValueError('No hay ficha para mover')
        encontrado = False
        for k, v in self.__contenido.items():
            if v == ficha:
                encontrado = True
                fila, col = k
                break
        if not encontrado:
            raise ValueError('La ficha no está en el tablero')
        nueva_fila, nueva_col = Tablero.__nueva_posicion(fila, col, ficha.color(), direccion)
        if (nueva_fila, nueva_col) == (fila, col):
            return (fila, col) # La ficha se ha intentado mover fuera de los límites del tablero
        otra_ficha = self.ficha(nueva_fila, nueva_col)
        if otra_ficha is not None:
            if otra_ficha.color() == ficha.color():
                return (fila, col)  # La ficha no se mueve
            else:
                self.__quitar_ficha(otra_ficha)  # Quita la otra ficha a su jugador
        # Movemos la ficha:
        self.__contenido[(nueva_fila, nueva_col)] = ficha
        del self.__contenido[(fila, col)]
        return (nueva_fila, nueva_col)
