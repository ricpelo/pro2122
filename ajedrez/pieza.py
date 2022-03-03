from color import Color
from movimiento import Movimiento
from abc import ABC, abstractclassmethod

class Pieza(ABC):
    def __init__(self, color: Color):
        self.__color = color

    def get_color(self):
        return self.__color

    @abstractclassmethod
    def se_puede_mover(self, movimiento: Movimiento) -> bool:
        ...
