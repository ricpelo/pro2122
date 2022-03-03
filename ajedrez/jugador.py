class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.get_nombre() == otro.get_nombre()

    def __hash__(self):
        return hash(self.get_nombre())

    def __repr__(self):
        return f'Jugador({self.get_nombre()!r})'

    def __str__(self):
        return self.get_nombre()
