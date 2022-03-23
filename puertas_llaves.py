class Llave:
    def __init__(self, color):
        self.__color = color

    def color(self):
        return self.__color

class Puerta:
    def __init__(self, color):
        self.__color = color
        self.__llave = None
        self.__abierta = False

    def poner(self, llave):
        self.__llave = llave
        return self

    def quitar(self):
        llave = self.__llave
        self.__llave = None
        return llave

    def abrir(self):
        if self.__llave is not None and \
           self.__llave.color() == self.__color:
            self.__abierta = True
            return True
        return False

    def abierta(self):
        return self.__abierta

    def cerrar(self):
        self.__abierta = False

assert Puerta('rojo').poner(Llave('rojo')).abrir() == True
assert Puerta('rojo').poner(Llave('verde')).abrir() == False
assert Puerta('rojo').abrir() == False
