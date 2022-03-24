from abc import ABC, abstractmethod

class Expresion(ABC):
    @abstractmethod
    def valor(self):
        ...

class Numero(Expresion):
    def __init__(self, numero):
        self.__numero = numero

    def valor(self):
        return self.__numero

class Suma(Expresion):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def valor(self):
        return self.__x.valor() + self.__y.valor()

class Producto(Expresion):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def valor(self):
        return self.__x.valor() * self.__y.valor()

assert Numero(2).valor() == 2
assert Suma(Numero(2), Producto(Numero(3), Numero(5))).valor() == 17
assert Producto(Numero(2), Suma(Numero(3), Numero(5))).valor() == 16
