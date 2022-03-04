from color import Color
from movimiento import Movimiento
from casilla import Casilla
from abc import ABC, abstractclassmethod

class Pieza(ABC):
    def __init__(self, color: Color):
        self.__color = color
        self.__movida = False

    def get_color(self):
        return self.__color

    def get_movida(self):
        return self.__movida

    @abstractclassmethod
    def se_puede_mover(self, inicial: Casilla, final: Casilla) -> bool:
        ...

    @abstractclassmethod
    def puede_saltar(self):
        ...

class Torre(Pieza):
    def se_puede_mover(self, inicial: Casilla, final: Casilla) -> bool:
        if inicial == final:
            return False
        return inicial.get_columna() == final.get_columna() or \
               inicial.get_fila() == final.get_fila()

    def puede_saltar(self):
        return False

class Alfil(Pieza):
    def se_puede_mover(self, inicial: Casilla, final: Casilla) -> bool:
        if inicial == final:
            return False
        return abs(final.get_columna() - inicial.get_columna()) == \
               abs(final.get_fila() - inicial.get_fila())

    def puede_saltar(self):
        return False

class Peon(Pieza):
    def se_puede_mover(self, inicial: Casilla, final: Casilla) -> bool:
        if inicial == final:
            return False
        if final.get_fila() != inicial.get_fila():
            return False
        avance = abs(final.get_columna() - inicial.get_columna())
        if self.get_movida():
            return avance == 1
        return avance <= 2
