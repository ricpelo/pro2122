from color import Color

class Casilla:
    def __init__(self, color: Color):
        self.__color = color

    def get_color(self):
        return self.__color
