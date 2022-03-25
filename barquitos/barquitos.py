class Barco:
    def __init__(self, tamanyo):
        self.__tamanyo = tamanyo
        self.__golpes = 0

    def tamanyo(self):
        return self.__tamanyo

    def golpes(self):
        return self.__golpes

    def incr_golpes(self):
        self.__golpes += 1

    def tocado(self):
        return self.golpes() > 0

    def hundido(self):
        return self.golpes() == self.tamanyo()

class Tablero:
    NUM_FILAS = 10
    NUM_COLUMNAS = 10

    def __init__(self, num_filas=Tablero.NUM_FILAS, num_columnas=Tablero.NUM_COLUMNAS):
        self.__num_filas = num_filas
        self.__num_columnas = num_columnas
        self.__tablero = {}

    def num_filas(self):
        return self.__num_filas

    def num_columnas(self):
        return self.__num_columnas

    def colocar_barco(self, barco, posicion, direccion):
        pass

j1 = Tablero()
j2 = Tablero()
