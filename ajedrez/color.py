class Color:
    def __init__(self, color: str):
        self.__color = color

    def get_color(self):
        return self.__color

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_color() == otro.get_color()

    def __hash__(self):
        return hash(self.get_color())

    def __repr__(self):
        return f'Color({self.get_color()!r})'

    def __str__(self):
        return self.get_color()
