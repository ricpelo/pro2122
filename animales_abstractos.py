from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.set_nombre(nombre)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @abstractmethod
    def mover(self):
        ...

class Terrestre(Animal):
    def get_patas(self):
        return self.__patas

    def set_patas(self, patas):
        self.__patas = patas

    def mover(self):
        print('Caminando voy...')

class Acuatico(Animal):
    def get_aletas(self):
        return self.__aletas

    def set_aletas(self, aletas):
        self.__aletas = aletas

    def mover(self):
        print('Glu glu glu...')

class Ave(Animal):
    def mover(self):
        print('Volando voy')
