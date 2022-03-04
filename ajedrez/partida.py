from jugador import Jugador
from tablero import Tablero
from color import Color

class Partida:
    def __init__(
        self,
        nombre_jugador_blancas: str,
        nombre_jugador_negras: str
    ):
        self.__color_blanco = Color('BLANCO')
        self.__color_negro = Color('NEGRO')
        self.__tablero = Tablero(
            self.get_color_blanco(),
            self.get_color_negro()
        )
        self.__jugadores = {
            self.get_color_blanco(): Jugador(nombre_jugador_blancas),
            self.get_color_negro(): Jugador(nombre_jugador_negras)
        }

    def get_jugador_blancas(self):
        return self.__jugadores[self.get_color_blanco()]

    def get_jugador_negras(self):
        return self.__jugadores[self.get_color_negro()]

    def get_tablero(self):
        return self.__tablero

    def get_color_blanco(self):
        return self.__color_blanco

    def get_color_negro(self):
        return self.__color_negro

    def quien_gana_en_puntos(self):
        piezas_blancas = self.get_tablero().devolver_piezas(self.get_color_blanco())
        piezas_negras = self.get_tablero().devolver_piezas(self.get_color_negro())
        if len(piezas_blancas) == len(piezas_negras):
            return None
        if len(piezas_blancas) > len(piezas_negras):
            return self.get_jugador_blancas()
        return self.get_jugador_negras()
